pyprojectize
============

<!-- [[[cog
import pyprojectize, os, pathlib, urllib3
print(pyprojectize.__doc__)
print("```")
print("$ python pyprojectize.py --help")
pyprojectize.__doc__ = ""
pyprojectize.argparser().print_help()
print()
commit = "16a7deeb"
spec = pathlib.Path("ampy.spec")
response = urllib3.PoolManager().request("GET", f"https://src.fedoraproject.org/rpms/ampy/raw/{commit}/f/ampy.spec")
spec.write_bytes(response.data)
print(f"$ python pyprojectize.py ampy.spec  # {commit}")
pyprojectize.main([str(spec)])
spec.unlink()
print("```")
]]] -->

This helps you convert a Fedora RPM spec file from `%py3_build` etc. to `%pyproject` macros.
This program only operates on the spec file itself, and hence has limited knowledge.
The resulting spec file is not guaranteed to be buildable and manual verification
and completion of the transition is strongly advised.

```
$ python pyprojectize.py --help
usage: pyprojectize.py [-h] [-l] [-i MODIFIER] [-x MODIFIER [MODIFIER ...]] [-s SOURCEDIR] [SPECFILE]

positional arguments:
  SPECFILE              path to the spec file to convert

options:
  -h, --help            show this help message and exit
  -l, --list-modifiers  list all available modifiers and exit
  -i MODIFIER, --info MODIFIER
                        display documentation for given modifier
  -x MODIFIER [MODIFIER ...], --exclude MODIFIER [MODIFIER ...]
                        exclude given modifier
  -s SOURCEDIR, --sourcedir SOURCEDIR
                        path to the source directory, relevant for %include etc. (default: spec's parent)

If you wish to process multiple specfiles at a time, run this tool via parallel, etc.

$ python pyprojectize.py ampy.spec  # 16a7deeb
✅ add_pyproject_buildrequires: %generate_buildrequires with %pyproject_buildrequires added
✅ remove_setuptools_br: removed BuildRequires for setuptools
✅ py3_build_to_pyproject_wheel: replaced %py3_build with %pyproject_wheel in %build
✅ py3_install_to_pyproject_install: replaced %py3_install with %pyproject_install in %install
✅ egginfo_to_distinfo: replaced .egg-info with .dist-info in %files
✅ add_pyproject_files: %{python3_sitelib}/%{python3_sitearch} lines replaced with %{pyproject_files}
👌 update_extras_subpkg: %{?python_extras_subpkg:%python_extras_subpkg ...} not found
✅ remove_python_provide: %python_provide removed or replaced with %py_provides
✅ remove_python_enable_dependency_generator: %python_enable_dependency_generator removed
```
<!-- [[[end]]] -->

## Demo

https://github.com/hroncok/pyprojectize/compare/originals..specfiles

## Installation

Not yet installable. Install [specfile] and [packaging] and run the script directly with Python.

[specfile]: https://pypi.org/project/specfile/
[packaging]: https://pypi.org/project/packaging/

## Available modifiers

<!-- [[[cog
for name, func in pyprojectize._modifiers.items():
    print()
    print(f"### {name}")
    print()
    print(pyprojectize.docstring(func))
    print()
]]] -->

### add_pyproject_buildrequires

If there is no `%generate_buildrequires` section, add it after `%prep`.

Insert `%pyproject_buildrequires` to the end of `%generate_buildrequires`.


### remove_setuptools_br

Remove BuildRequires for setuptools, they should be generated.


### py3_build_to_pyproject_wheel

In the `%build` section, replace `%py3_build` with `%pyproject_wheel`.
Arguments (if any) are passed to `-C--global-option`.


### py3_install_to_pyproject_install

In the `%install` section, replace `%py3_install` with `%pyproject_install`.
Any arguments are discarded. Installing a wheel does not need arguments.


### egginfo_to_distinfo

In all the `%files` sections, replace `.egg-info` with `.dist-info`.
The `.dist-info` filename is updated if possible (e.g. to use canonical name and version).
Works reasonably well even with macronized filenames.


### add_pyproject_files

If there is only one `%files` section with `%{python3_sitelib}` or `%{python3_sitearch}`,
replace the manually listed files with `%pyproject_save_files` and `-f %{pyproject_files}`.

In case the `%license` files match patterns recognized by setuptools' defaults,
uses `%pyproject_save_files` with `-l` and removes them.


### update_extras_subpkg

Replace `%python_extras_subpkg -i ...` with `%pyproject_extras_subpkg`,
preserve other arguments.


### remove_python_provide

Remove `%python_provide` or replace it with `%py_provides` if the package name isn't the same.

This does not detect packages without files yet.
Packages without files need  `%py_provides` even when the package name is the same.


### remove_python_enable_dependency_generator

Remove `%python_enable_dependency_generator`, as the generator is enabled by default.

<!-- [[[end]]] -->

## License

MIT No Attribution

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
