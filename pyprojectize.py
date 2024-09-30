# SPDX-License-Identifier: MIT-0

import collections.abc
import enum
import glob
import re
import shlex
import sys

from packaging.utils import canonicalize_name, canonicalize_version
from specfile import Specfile
from specfile.sections import Section, Sections
from specfile.exceptions import RPMException


class Result(enum.Enum):
    UPDATED = 1
    NOT_NEEDED = 2
    NOT_IMPLEMENTED = 3
    ERROR = 4


ResultMsg = tuple[Result, str]
ModFunc = collections.abc.Callable[[Specfile, Sections], ResultMsg]

_modifiers: list[ModFunc] = []


def register(func: ModFunc) -> ModFunc:
    _modifiers.append(func)
    return func


@register
def add_pyproject_buildrequires(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    If there is no %generate_buildrequires section, add it after %prep.

    Insert %pyproject_buildrequires to the end of %generate_buildrequires.
    """
    if "prep" in sections:
        endlines = 0
        for line in reversed(sections.prep):
            if line.strip():
                break
            endlines += 1
    else:
        endlines = 1
    pb = ["%pyproject_buildrequires"] + [""] * endlines

    if "generate_buildrequires" not in sections:
        if "prep" not in sections:
            return Result.ERROR, "no %prep section"
        gb = Section("generate_buildrequires", data=pb)
        index = sections.index(sections.prep) + 1  # this could be missing?
        sections.insert(index, gb)
        return (
            Result.UPDATED,
            "%generate_buildrequires with %pyproject_buildrequires added",
        )

    for line in sections.generate_buildrequires:
        if re.search(r"%({\??)?pyproject_buildrequires\b", line):
            return (
                Result.NOT_NEEDED,
                "%generate_buildrequires already has %pyproject_buildrequires",
            )

    sections.generate_buildrequires.extend(pb)
    return (
        Result.UPDATED,
        "existing %generate_buildrequires extended with %pyproject_buildrequires",
    )


def shlex_quote_with_macros(s: str, *, spec: Specfile) -> str:
    """
    Often want to sh-quote the actual content of maconized strings.
    He try quoting the expanded macros and if there are no quotes, we don't quote the macronized input.

    Note that if some of the 's are hidden in the macros, we have no proper way of escaping.
    """
    if "%" not in s:  # short circuit, no macros present
        return shlex.quote(s)
    try:
        expanded = spec.expand(s)
        if shlex.quote(expanded) == expanded:
            # no escaping needed on expanded values, no escaping done on the macros
            return s
    except RPMException:
        pass
    # finally force quote it, this bit is copied from shlex.quote code
    return "'" + s.replace("'", "'\"'\"'") + "'"


@register
def py3_build_to_pyproject_wheel(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    In the %build section, replace %py3_build with %pyproject_wheel.
    Arguments (if any) are passed to -C--global-option.
    """
    if "build" not in sections:
        return Result.ERROR, "no %build section"

    index = None
    for idx, line in enumerate(sections.build):
        if re.search(r"%({\??)?pyproject_wheel\b", line):
            return (
                Result.NOT_NEEDED,
                "%build already has %pyproject_wheel",
            )
        found = re.findall(r"%{?\??py3_build\b", line)
        if found:
            if index is not None or len(found) > 1:
                return Result.ERROR, "multiple %py3_build macros in %build section"
            index = idx

    if index is None:
        return (
            Result.NOT_NEEDED,
            "no %py3_build macro in %build section",
        )

    if sections.build[index].rstrip().endswith("\\"):
        return (
            Result.ERROR,
            "line with %py3_build ends with backslash, not touching that'",
        )

    def repl(m):
        LB = m["LB"] or ""
        RB = m["RB"] or ""
        if m["arguments"]:
            arguments = shlex_quote_with_macros(m["arguments"], spec=spec)
            return f"%{LB}pyproject_wheel -C--global-option={arguments}{RB}"
        return f"%{LB}pyproject_wheel{RB}"

    newline = re.sub(
        r"%(?P<LB>{)?\??py3_build(\s+(--\s+)?(?P<arguments>[^}]+))?(?P<RB>})?",
        repl,
        sections.build[index],
    )

    if sections.build[index] == newline:
        return (
            Result.ERROR,
            "replacement regex failed",
        )

    sections.build[index] = newline
    return (
        Result.UPDATED,
        "replaced %py3_build with %pyproject_wheel in %build",
    )


@register
def py3_install_to_pyproject_install(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    In the %install section, replace %py3_install with %pyproject_install.
    Arguments are discarded (should we error instead?).
    """
    if "install" not in sections:
        return Result.ERROR, "no %install section"

    index = None
    for idx, line in enumerate(sections.install):
        if re.search(r"%({\??)?pyproject_install\b", line):
            return (
                Result.NOT_NEEDED,
                "%install already has %pyproject_install",
            )
        found = re.findall(r"%{?\??py3_install\b", line)
        if found:
            if index is not None or len(found) > 1:
                return Result.ERROR, "multiple %py3_install macros in %install section"
            index = idx

    if index is None:
        return (
            Result.NOT_NEEDED,
            "no %py3_install macro in %install section",
        )

    if sections.install[index].rstrip().endswith("\\"):
        return (
            Result.ERROR,
            "line with %py3_install ends with backslash, not touching that'",
        )

    newline = re.sub(
        r"%(?P<LB>{)?\??py3_install(\s[^}]*)?(?P<RB>})?(\s[^}]*)?$",
        r"%\g<LB>pyproject_install\g<RB>",
        sections.install[index],
    )

    if sections.install[index] == newline:
        return (
            Result.ERROR,
            "replacement regex failed",
        )

    sections.install[index] = newline
    return (
        Result.UPDATED,
        "replaced %py3_install with %pyproject_install in %install",
    )


def canonicalize_name_with_macros(name: str, *, spec: Specfile) -> str:
    if "%" in name:
        expanded = spec.expand(name)
        canonical = canonicalize_name(expanded).replace("-", "_")
        if expanded == canonical:
            return name
        # let's see if there is some nice macro we can use here
        with spec.macro_definitions() as macros:
            for macro in macros:
                if macro.body == canonical:
                    return f"%{{{macro.name}}}"
            if match := re.match(r"%{(?P<macro>[^}]+)}(?P<rest>.+)$", name):
                for macro in macros:
                    if f"{macro.body}{match['rest']}" == canonical:
                        return f"%{{{macro.name}}}{match['rest']}"
        # no macro? return the expanded canonical name
        return canonical
    return canonicalize_name(name).replace("-", "_")


def canonicalize_version_with_macros(version: str, *, spec: Specfile) -> str:
    if "%" in version:
        expanded = spec.expand(version)
        canonical = canonicalize_version(expanded).replace("-", "_")
        if expanded == canonical:
            return version
        # we could return the canonical version, but that would make a weird specfile
        # there is no RPM macro to turn 0.4.0 to 0.4, so we just glob it
        return "*"
    return canonicalize_version(version).replace("-", "_")


@register
def egginfo_to_distinfo(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    In all the %files sections, replace .egg-info with .dist-info.
    """
    ret = Result.NOT_NEEDED, "no .egg-info in %files"

    def repl(m):
        if m["name"]:
            name = canonicalize_name_with_macros(m["name"], spec=spec)
            version = canonicalize_version_with_macros(m["version"], spec=spec)
            filename = f"{name}-{version}"
        else:
            filename = m["all"]
            # anecdotal evidence: everything before * is a name
            sep = "-" if "-" in filename else "*"
            name, sep, rest = filename.partition(sep)
            name = canonicalize_name_with_macros(name, spec=spec)
            filename = f"{name}{sep}{rest}"
        return f"/{filename}{m['dot'] or ''}dist-info{m['end']}"

    for section in sections:
        if section.name == "files":
            for idx, line in enumerate(section):
                if "egg-info" in line:
                    newline = re.sub(
                        r"/((?P<name>[^/-]+)-(?P<version>[^/-]+)-[^/-]*[^/\.-]|(?P<all>[^/]*[^/\.]))(?P<dot>\.)?egg-info(?P<end>(/|}|$))",
                        repl,
                        line,
                    )
                    if line != newline:
                        ret = (
                            Result.UPDATED,
                            "replaced .egg-info with .dist-info in %files",
                        )
                        section[idx] = newline

    return ret


@register
def remove_setuptools_br(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    Remove BuildRequires for setuptools, they should be generated
    """
    ret = Result.NOT_NEEDED, "no BuildRequires for setuptools found"

    setuptools = r"(python(3|%{python3_pkgversion})-setuptools|python3dist\(setuptools\)|%{py3_dist setuptools})"
    rich = rf"\({setuptools}\s+.+\)"
    last_rich = rf",?\s*{rich}\s*$"
    nolast_rich = rf"{rich}\s*,?(\s+|$)"
    regular = rf"{setuptools}(\s+[<>=]{{1,3}}\s+\S+)?"
    last_regular = rf",?\s*{regular}\s*$"
    nolast_regular = rf"{regular}\s*,?(\s+|$)"
    drop_me = rf"({last_rich}|{nolast_rich}|{last_regular}|{nolast_regular})"

    for section in sections:
        if section.name == "package":  # the spec preamble is also here
            del_lines = []
            for idx, line in enumerate(section):
                if line.lstrip().lower().startswith("buildrequires:"):
                    newline = re.sub(drop_me, "", line)
                    if line != newline:
                        section[idx] = newline
                        ret = Result.UPDATED, "removed BuildRequires for setuptools"
                        if newline.strip().lower() == "buildrequires:":
                            del_lines.append(idx)
            for idx in reversed(del_lines):
                del section[idx]

    return ret


@register
def update_extras_subpkg(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    %{?python_extras_subpkg:%python_extras_subpkg -n python3-ipython -i %{python3_sitelib}/*.egg-info notebook}
    ->
    %pyproject_extras_subpkg -n python3-ipython notebook
    """
    ret = (
        Result.NOT_NEEDED,
        "%{?python_extras_subpkg:%python_extras_subpkg ...} not found",
    )

    for section in sections:
        if section.name in ("package", "description", "files"):
            for idx, line in enumerate(section):
                if "%python_extras_subpkg" in line:
                    newline = re.sub(
                        r"%{\?python_extras_subpkg:%python_extras_subpkg(?P<before>.*)\s+-i\s*\S+(?P<after>\s+.*)}",
                        r"%pyproject_extras_subpkg\g<before>\g<after>",
                        line,
                    )
                    if line != newline:
                        section[idx] = newline
                        ret = (
                            Result.UPDATED,
                            "replaced %python_extras_subpkg with %pyproject_extras_subpkg",
                        )

    return ret


def alignment_of(line: str) -> tuple[str, int, str] | None:
    tag_re = r"^(?P<prespace>\s*)(?P<align>\S+\s*:(?P<spaces>\s*))\S"
    if match := re.search(tag_re, line):
        prespace = match["prespace"]
        col = len(match["align"])
        space_counts = {c: match["spaces"].count(c) for c in set(match["spaces"])}
        most_common_space = max(space_counts, default=" ", key=space_counts.__getitem__)
        for space in match["spaces"]:
            if space == "\t":
                col += 7  # approximation
        return prespace, col, most_common_space
    return None


def align(tag: str, value: str, prespace: str, col: int, most_common_space: str) -> str:
    spaces = col - len(tag)
    if most_common_space == "\t":
        spaces //= 8  # approximation
    spaces = max(1, spaces)
    return f"{prespace}{tag}{spaces*most_common_space}{value}"


@register
def remove_python_provide(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    Remove %python_provide or replace it with %py_provides if the name isn't the same.

    This does not detect packages without files, that would be hard.
    """
    ret = (
        Result.NOT_NEEDED,
        "%python_provide not found",
    )
    provide_re = r"^\s*%{\?python_provide:%python_provide\s+(?P<name>\S+)}\s*$"

    for section in sections:
        if section.name == "package":
            name = ""
            last_alignment = "", 16, " "
            del_lines = []
            if section.options:
                name = getattr(section.options, "n", "")
            for idx, line in enumerate(section):
                if not name and (match := re.search(r"\s*name:", line.lower())):
                    name = line.partition(":")[-1].strip()
                if match := re.search(provide_re, line):
                    provided_name = match["name"]
                    try:
                        if spec.expand(provided_name) == spec.expand(name):
                            del_lines.append(idx)
                    except RPMException:
                        if provided_name == name:
                            del_lines.append(idx)
                    else:
                        section[idx] = align(
                            "%py_provides", provided_name, *last_alignment
                        )
                    ret = (
                        Result.UPDATED,
                        "%python_provide removed or replaced with %py_provides",
                    )
                elif alignment := alignment_of(line):
                    last_alignment = alignment
            for idx in reversed(del_lines):
                del section[idx]

    return ret


@register
def add_pyproject_files(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    Remove %python_provide or replace it with %py_provides if the name isn't the same.

    This does not detect packages without files, that would be hard.
    """
    if "install" not in sections:
        return Result.ERROR, "no %install section"

    sections_options = set()
    pysite_re = r"^[^#]*%{?python3_site(arch|lib)}?/(?P<topname>[^/\.]*)"
    pysite_lines = []
    for section in sections:
        if section.name == "files":
            if section.options.f:
                if "pyproject_files" in str(section.options.f):
                    return (
                        Result.NOT_NEEDED,
                        "%files -f %{pyproject_files} already used",
                    )
            for line in section:
                if re.search(pysite_re, line):
                    sections_options.add(str(section.options))
                    pysite_lines.append(line)

    if not sections_options:
        return (
            Result.NOT_NEEDED,
            "No %{python3_sitelib}/%{python3_sitearch} files in %files",
        )

    if len(sections_options) > 1:
        return (
            Result.NOT_IMPLEMENTED,
            "Multiple %files sections with %{python3_sitelib}/%{python3_sitearch}",
        )

    section_options = sections_options.pop()
    for line in pysite_lines:
        if "%exclude" in line:
            return (
                Result.NOT_IMPLEMENTED,
                "%exclude %{python3_sitelib}/%{python3_sitearch} used in %files",
            )

    topnames = set()
    for line in pysite_lines.copy():
        if "egg-info" in line or "dist-info" in line or "__pycache__" in line:
            continue
        if line.endswith(".pth"):
            pysite_lines.remove(line)
            continue
        # we know the match matches, but mypyp is not happy without the check
        # we could store the match from previous search, but meh
        if (match := re.search(pysite_re, line)) and (topname := match["topname"]):
            # sometimes there is a weirdly listed distinfo, like: %{modname}-%{version}*
            # we should only add valid module names here, but mostly it's the -
            if "-" not in topname:
                topnames.add(topname)

    if not topnames:
        return (
            Result.NOT_NEEDED,
            "No modules to pass to %pyproject_save_files",
        )

    if not pysite_lines:
        return (
            Result.NOT_NEEDED,
            "No %{python3_sitelib}/%{python3_sitearch} lines left to remove from %files",
        )

    pyproject_install_index = None
    for idx, line in enumerate(sections.install):
        if re.search(r"%({\??)?pyproject_install\b", line):
            pyproject_install_index = idx
        elif re.search(r"%({\??)?pyproject_save_files\b", line):
            return (
                Result.NOT_NEEDED,
                "%install already uses %pyproject_save_files",
            )
    if pyproject_install_index is None:
        return (
            Result.NOT_IMPLEMENTED,
            "%install does not have %pyproject_install",
        )

    for section in sections:
        if section.name == "files" and str(section.options) == section_options:
            if section.options.f:
                return (
                    Result.NOT_IMPLEMENTED,
                    "%files with %{python3_sitelib}/%{python3_sitearch} already has -f",
                )
            section.options.f = "%{pyproject_files}"
            for line in pysite_lines:
                section.remove(line)
    pyproject_save_files = "%pyproject_save_files " + " ".join(
        shlex_quote_with_macros(t, spec=spec) for t in sorted(topnames)
    )
    sections.install.insert(pyproject_install_index + 1, pyproject_save_files)
    return (
        Result.UPDATED,
        "%{python3_sitelib}/%{python3_sitearch} lines replaced with %{pyproject_files}",
    )


def specfile_path() -> str:
    if len(sys.argv) == 2:
        return sys.argv[1]
    if len(specs := glob.glob("*.spec")) == 1:
        return specs[0]
    raise NotImplementedError


def main() -> int:
    spec = Specfile(specfile_path(), sourcedir=".")
    results = set()

    with spec.sections() as sections:
        # TODO CLI to enable, disable, nicer result reporting (with rich?)
        for modifier in _modifiers:
            print(modifier.__name__, resmes := modifier(spec, sections))
            results.add(resmes[0])

    if Result.UPDATED in results:
        spec.save()

    return 1 if Result.ERROR in resmes else 0


if __name__ == "__main__":
    sys.exit(main())
