# SPDX-License-Identifier: MIT-0
"""
This helps you convert a Fedora RPM spec file from `%py3_build` etc. to `%pyproject` macros.
This program only operates on the spec file itself, and hence has limited knowledge.
The resulting spec file is not guaranteed to be buildable and manual verification
and completion of the transition is strongly advised.
"""

import argparse
import collections.abc
import enum
import fnmatch
import pathlib
import re
import shlex
import sys
import textwrap

from packaging.utils import canonicalize_name, canonicalize_version
from specfile import Specfile
from specfile.sections import Section, Sections
from specfile.exceptions import RPMException


class Result(enum.StrEnum):
    UPDATED = "✅"
    NOT_NEEDED = "👌"
    NOT_IMPLEMENTED = "🚧"
    ERROR = "🚨"


ResultMsg = tuple[Result, str]
ModFunc = collections.abc.Callable[[Specfile, Sections], ResultMsg]

_modifiers: dict[str, ModFunc] = {}


def register(func: ModFunc) -> ModFunc:
    _modifiers[func.__name__] = func
    return func


@register
def add_pyproject_buildrequires(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    If there is no `%generate_buildrequires` section, add it after `%prep`.

    Insert `%pyproject_buildrequires` to the end of `%generate_buildrequires`.
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
        if re.search(r"(?<!%)%({\??)?pyproject_buildrequires\b", line):
            return (
                Result.NOT_NEEDED,
                "%generate_buildrequires already has %pyproject_buildrequires",
            )

    sections.generate_buildrequires.extend(pb)
    return (
        Result.UPDATED,
        "existing %generate_buildrequires extended with %pyproject_buildrequires",
    )


@register
def remove_setuptools_br(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    Remove BuildRequires for setuptools, they should be generated.
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


def try_expand(s: str, *, spec: Specfile) -> str:
    """
    Call spec.expand() but return the input if it raises RPMException.
    """
    try:
        return spec.expand(s)
    except RPMException:
        return s


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
    In the `%build` section, replace `%py3_build` with `%pyproject_wheel`.
    Arguments (if any) are passed to `-C--global-option`.
    Environment variables (if any) are exported on the previous line.
    """
    if "build" not in sections:
        return Result.ERROR, "no %build section"

    index = None
    for idx, line in enumerate(sections.build):
        if re.search(r"(?<!%)%({\??)?pyproject_wheel\b", line):
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
        rpmcond = m["rpmcond"] or ""
        prefix = m["prefix"] or ""
        if prefix.strip():
            environment = prefix.rstrip()
            prefix = f"export {environment}\n"
        if m["arguments"]:
            arguments = shlex_quote_with_macros(m["arguments"], spec=spec)
            return f"{rpmcond}{prefix}%{LB}pyproject_wheel -C--global-option={arguments}{RB}"
        return f"{rpmcond}{prefix}%{LB}pyproject_wheel{RB}"

    newline = re.sub(
        r"(?P<rpmcond>%{?[?!]+\S+:)?(?P<prefix>[^;]*\s)?(?<!%)%(?P<LB>{)?\??py3_build(\s+(--\s+)?(?P<arguments>[^}]+))?(?P<RB>})?",
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
    In the `%install` section, replace `%py3_install` with `%pyproject_install`.
    Any arguments or environment variables are discarded. Installing a wheel does not need those.
    """
    if "install" not in sections:
        return Result.ERROR, "no %install section"

    index = None
    for idx, line in enumerate(sections.install):
        if re.search(r"(?<!%)%({\??)?pyproject_install\b", line):
            return (
                Result.NOT_NEEDED,
                "%install already has %pyproject_install",
            )
        found = re.findall(r"(?<!%)%{?\??py3_install\b", line)
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
        r"(?P<rpmcond>%{?[?!]+\S+:)?(?P<spaces>\s*)([^;]*\s)?(?<!%)%(?P<LB>{)?\??py3_install(\s[^}]*)?(?P<RB>})?(\s[^}]*)?$",
        r"\g<rpmcond>\g<spaces>%\g<LB>pyproject_install\g<RB>",
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
        expanded = try_expand(name, spec=spec)
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
        expanded = try_expand(version, spec=spec)
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
    In all the `%files` sections, replace `.egg-info` with `.dist-info`.
    The `.dist-info` filename is updated if possible (e.g. to use canonical name and version).
    Works reasonably well even with macronized filenames.
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
                    if "python2" in line or "python3_other" in line:
                        continue
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
def add_pyproject_files(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    If there is only one `%files` section with `%{python3_sitelib}` or `%{python3_sitearch}`,
    replace the manually listed files with `%pyproject_save_files` and `-f %{pyproject_files}`.

    In case the `%license` files match patterns recognized by setuptools' defaults,
    uses `%pyproject_save_files` with `-l` and removes them.
    """
    if "install" not in sections:
        return Result.ERROR, "no %install section"

    sections_options = set()
    pysite_re = r"^[^#]*(?<!%)%{?python3_site(arch|lib)}?/(?P<topname>[^/\.]*)"
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
        if re.search(r"(?<!%)%({\??)?pyproject_install\b", line):
            pyproject_install_index = idx
        elif re.search(r"(?<!%)%({\??)?pyproject_save_files\b", line):
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
            assert_license = False
            for idx, line in enumerate(section):
                if line.startswith("%license"):
                    tokens = shlex.split(line)
                    for token in tokens.copy()[1:]:
                        for pattern in (
                            "LICEN[CS]E*",
                            "COPYING*",
                            "NOTICE*",
                            "AUTHORS*",
                        ):
                            if fnmatch.fnmatch(token, pattern):
                                assert_license = True
                                tokens.remove(token)
                                break
                    if len(tokens) == 1:
                        pysite_lines.append(line)
                    else:
                        section[idx] = " ".join(tokens)
            for line in pysite_lines:
                section.remove(line)
    pyproject_save_files = (
        f"%pyproject_save_files{' -l' if assert_license else ''} "
        + " ".join(shlex_quote_with_macros(t, spec=spec) for t in sorted(topnames))
    )
    sections.install.insert(pyproject_install_index + 1, pyproject_save_files)
    return (
        Result.UPDATED,
        "%{python3_sitelib}/%{python3_sitearch} lines replaced with %{pyproject_files}",
    )


@register
def add_pyproject_check_import(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    If `%pyproject_save_files` is used in `%install` and `%pyproject_check_import`
    is not used in `%check`, add `%pyproject_check_import` to the beginning of `%check`
    (create the section if needed).
    """
    if "install" not in sections:
        return Result.ERROR, "no %install section"
    for idx, line in enumerate(sections.install):
        if re.search(r"(?<!%)%({\??)?pyproject_save_files\b", line):
            break
    else:
        return (
            Result.NOT_IMPLEMENTED,
            "%install does not use %pyproject_save_files",
        )

    if "check" not in sections:
        endlines = 0
        for line in reversed(sections.install):
            if line.strip():
                break
            endlines += 1
        pci = ["%pyproject_check_import"] + [""] * endlines
        check = Section("check", data=pci)
        index = sections.index(sections.install) + 1
        sections.insert(index, check)
        return (
            Result.UPDATED,
            "%check with %pyproject_check_import added",
        )

    for line in sections.check:
        if re.search(r"(?<!%)%({\??)?pyproject_check_import\b", line):
            return (
                Result.NOT_NEEDED,
                "%check already has %pyproject_check_import",
            )

    sections.check[:0] = ["%pyproject_check_import", ""]
    return (
        Result.UPDATED,
        "existing %check prepended with %pyproject_check_import",
    )


@register
def update_extras_subpkg(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    Replace `%python_extras_subpkg -i ...` with `%pyproject_extras_subpkg`,
    preserve other arguments.
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
                        r"(?<!%)%{\?python_extras_subpkg:%python_extras_subpkg(?P<before>.*)\s+-i\s*\S+(?P<after>\s+.*)}",
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
    Remove `%python_provide` or replace it with `%py_provides` if the package name isn't the same.

    If `%py_provides` is added, also remove the `Provides:` for the same name.

    This does not detect packages without files yet.
    Packages without files need  `%py_provides` even when the package name is the same.
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
            del_lines = set()
            if section.options:
                name = getattr(section.options, "n", "")
            for idx, line in enumerate(section):
                if not name and (match := re.search(r"\s*name:", line.lower())):
                    name = line.partition(":")[-1].strip()
                if match := re.search(provide_re, line):
                    provided_name = match["name"]
                    expanded_provided_name = try_expand(provided_name, spec=spec)
                    expanded_name = try_expand(name, spec=spec)
                    if expanded_provided_name == expanded_name:
                        del_lines.add(idx)
                    else:
                        section[idx] = align(
                            "%py_provides", provided_name, *last_alignment
                        )
                        for idx, line in enumerate(section):
                            if line.lstrip().lower().startswith("provides:"):
                                line = try_expand(line, spec=spec)
                                if re.match(
                                    rf"\s*provides:\s*{expanded_provided_name}\s*([<>=]+\s*\S+)?\s*$",
                                    line,
                                    flags=re.I,
                                ):
                                    del_lines.add(idx)
                    ret = (
                        Result.UPDATED,
                        "%python_provide removed or replaced with %py_provides",
                    )
                elif alignment := alignment_of(line):
                    last_alignment = alignment
            for idx in sorted(del_lines, reverse=True):
                del section[idx]

    return ret


def remove_lines(
    spec: Specfile,
    sections: Sections,
    regexes: list[str],
    msg_not_remvoed: str,
    msg_removed: str,
    *,
    limit_sections: collections.abc.Container[str] | None = None,
) -> ResultMsg:
    ret = Result.NOT_NEEDED, msg_not_remvoed
    for section in sections:
        if limit_sections is not None and section.name not in limit_sections:
            continue
        del_lines = []
        maxidx = len(section) - 1
        for idx, line in enumerate(section):
            if any(re.match(r, line) for r in regexes):
                ret = Result.UPDATED, msg_removed
                del_lines.append(idx)
                if (idx == 0 or not section[idx - 1].strip()) and (
                    idx != maxidx and not section[idx + 1].strip()
                ):
                    del_lines.append(idx + 1)
        for idx in reversed(del_lines):
            del section[idx]

    return ret


@register
def remove_python_enable_dependency_generator(
    spec: Specfile, sections: Sections
) -> ResultMsg:
    """
    Remove `%python_enable_dependency_generator`, as the generator is enabled by default.
    """
    return remove_lines(
        spec,
        sections,
        [r"\s*%{?\??python_enable_dependency_generator}?\s*$"],
        "no %python_enable_dependency_generator",
        "%python_enable_dependency_generator removed",
    )


@register
def remove_pyp2rpm_comment(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    Remove the `# Created by pyp2rpm-X.Y.Z` comment.
    The spec file is changed enough for this to no longer matter.
    """
    return remove_lines(
        spec,
        sections,
        [r"# Created by pyp2rpm"],
        "no # Created by pyp2rpm-X.Y.Z comment",
        "# Created by pyp2rpm-X.Y.Z comment removed",
        limit_sections={"package"},
    )


@register
def remove_remove_bundled_egginfo(spec: Specfile, sections: Sections) -> ResultMsg:
    """
    Remove the `# Remove bundled egg-info` comment and the followup `rm ...egg-info`.
    There is no such thing as "bundled egg-info".
    """
    return remove_lines(
        spec,
        sections,
        [r"# Remove bundled egg-info", r"rm(\s+-[rf]+)?\s+\S+\.egg-info"],
        "no removal of bundled .egg-info",
        "removal of bundled .egg-info removed",
        limit_sections={"prep"},
    )


def specfile_path() -> pathlib.Path | None:
    ret = None
    for path in pathlib.Path(".").glob("*.spec"):
        if ret is not None:
            # two or more spec files? return none of them
            return None
        ret = path
    return ret


def argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pyprojectize",
        description=__doc__,
        epilog="If you wish to process multiple specfiles at a time, run this tool via parallel, etc. "
        "If you wish to inspect/commit result of each modififer separatelly, "
        "you can loop over %(prog)s -l calling %(prog)s -o $modifer each time.",
    )

    spec = specfile_path()
    group = parser.add_mutually_exclusive_group(required=not spec)
    group.add_argument(
        "SPECFILE",
        help="path to the spec file to convert"
        + (f" (default: {spec})" if spec else ""),
        type=pathlib.Path,
        nargs="?",
        default=spec,
    )
    group.add_argument(
        "-l",
        "--list-modifiers",
        help="list all available modifiers and exit",
        action="store_true",
    )
    group.add_argument(
        "-i",
        "--info",
        metavar="MODIFIER",
        help="display documentation for given modifier",
        choices=_modifiers.keys(),
    )

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-x",
        "--exclude",
        nargs="+",
        metavar="MODIFIER",
        action="extend",
        help="exclude given modifier",
        choices=_modifiers.keys(),
        default=[],
    )
    group.add_argument(
        "-o",
        "--only",
        metavar="MODIFIER",
        help="run only one given modifier",
        choices=_modifiers.keys(),
        default=[],
    )

    parser.add_argument(
        "-s",
        "--sourcedir",
        help="path to the source directory, relevant for %%include etc. (default: spec's parent)",
        type=pathlib.Path,
    )

    return parser


def docstring(modifier: ModFunc) -> str:
    return textwrap.dedent(modifier.__doc__ or "N/A").strip()


def main(argv: list[str] = sys.argv[1:]) -> int:
    modifiers = _modifiers.copy()

    args = argparser().parse_args(argv)
    if args.info:
        print(docstring(modifiers[args.info]))
        return 0

    for modifier in set(args.exclude):
        del modifiers[modifier]

    if args.only:
        modifiers = {args.only: modifiers[args.only]}

    if args.list_modifiers:
        for modifier in modifiers:
            print(modifier)
        return 0

    spec = Specfile(args.SPECFILE, sourcedir=args.sourcedir or args.SPECFILE.parent)
    results = set()

    with spec.sections() as sections:
        for name, modifier in modifiers.items():
            result, message = modifier(spec, sections)
            results.add(result)
            print(f"{result} {name}: {message}")

    if Result.UPDATED in results:
        spec.save()

    return 1 if Result.ERROR in results else 0


if __name__ == "__main__":
    sys.exit(main())
