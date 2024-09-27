# SPDX-License-Identifier: MIT-0

import collections.abc
import enum
import glob
import re
import shlex
import sys

import specfile


class Result(enum.Enum):
    UPDATED = 1
    NOT_NEEDED = 2
    ERROR = 3


ResultMsg = tuple[Result, str]
ModFunc = collections.abc.Callable[[specfile.sections.Sections], ResultMsg]

_modifiers: list[ModFunc] = []


def register(func: ModFunc) -> ModFunc:
    _modifiers.append(func)
    return func


@register
def add_pyproject_buildrequires(sections: specfile.sections.Sections) -> ResultMsg:
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
        gb = specfile.sections.Section("generate_buildrequires", data=pb)
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


@register
def py3_build_to_pyproject_wheel(sections: specfile.sections.Sections) -> ResultMsg:
    """
    In the %build section, replace %py3_build with %pyproject_wheel.
    Arguments (if any) are passed to -C--global-option.
    """
    if "build" not in sections:
        return Result.ERROR, "no %build section"

    index = None
    for idx, line in enumerate(sections.build):
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
            arguments = shlex.quote(m["arguments"])
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
def py3_install_to_pyproject_install(sections: specfile.sections.Sections) -> ResultMsg:
    """
    In the %install section, replace %py3_install with %pyproject_install.
    Arguments are discarded (should we error instead?).
    """
    if "install" not in sections:
        return Result.ERROR, "no %install section"

    index = None
    for idx, line in enumerate(sections.install):
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


@register
def egginfo_to_distinfo(sections: specfile.sections.Sections) -> ResultMsg:
    """
    In all the %files sections, replace .egg-info with .dist-info.
    """
    ret = Result.NOT_NEEDED, "no .egg-info in %files"

    for section in sections:
        if section.name == "files":
            for idx, line in enumerate(section):
                if ".egg-info" in line:
                    section[idx] = re.sub(
                        r"(-(\*|py\*|py%{python3_version}))?.egg-info",
                        ".dist-info",
                        line,
                    )
                    ret = Result.UPDATED, "replaced .egg-info with .dist-info in %files"

    return ret


@register
def remove_setuptools_br(sections: specfile.sections.Sections) -> ResultMsg:
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


def specfile_path() -> str:
    if len(sys.argv) == 2:
        return sys.argv[1]
    if len(specs := glob.glob("*.spec")) == 1:
        return specs[0]
    raise NotImplementedError


def main() -> int:
    spec = specfile.Specfile(specfile_path(), sourcedir=".")
    results = set()

    with spec.sections() as sections:
        # TODO CLI to enable, disable, nicer result reporting (with rich?)
        for modifier in _modifiers:
            print(modifier.__name__, resmes := modifier(sections))
            results.add(resmes[0])

    if Result.UPDATED in resmes:
        spec.save()

    return 1 if Result.ERROR in resmes else 0


if __name__ == "__main__":
    sys.exit(main())
