%global pkgname anyconfig

%global desc \
Python library provides common APIs to load and dump configuration files in\
various formats such like JSON, YAML and XML with some useful features such as\
contents merge, templates, query, schema validation and generation support.

%bcond_with optionals
%bcond_with tests

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without doc
%bcond_without extras
%else
%bcond_with doc
%bcond_with extras
%endif

Name:           python-%{pkgname}
Version:        0.13.0
Release:        10%{?dist}
Summary:        Python library to load and dump configuration files in various formats
License:        MIT
URL:            https://github.com/ssato/python-anyconfig
Source0:        %{url}/archive/RELEASE_%{version}.tar.gz
BuildArch:      noarch

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx
BuildRequires:  python3-configobj
BuildRequires:  python3-toml
BuildRequires:  python3-PyYAML
BuildRequires:  python3-sphinx-autodoc-typehints
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description    %{desc}

%package -n python3-%{pkgname}
Summary:        %{summary}
Requires:       python3-PyYAML
Requires:       python3-setuptools
%if %{with extras}
Requires:       python3-jinja2
Requires:       python3-jsonschema
Requires:       python3-ruamel-yaml
%endif
%if %{with optionals}
Requires:       python3-configobj
Requires:       python3-toml
%endif
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname} %{desc}

%if %{with doc}
%package        doc
Summary:        Documentation for %{name}

%description    doc
HTML documentation for %{name}.
%endif

%prep
%autosetup -n %{name}-RELEASE_%{version}

%build

%py3_build

%if %{with doc}
make -C docs/ SPHINXBUILD=sphinx-build-3 html
rm -f docs/build/html/.buildinfo
rm -frv docs/build/html/_sources
%endif

%install
%py3_install

%if %{with tests}
%check
export WITH_PYTHON_3=1
./pkg/runtest.sh
%endif

%files -n python3-%{pkgname}
%doc README.rst
%license LICENSE.MIT
%{python3_sitelib}/*
%{_bindir}/anyconfig*
%{_mandir}/*/anyconfig*.*.gz

%if %{with doc}
%files doc
%doc README.rst
%doc docs/build/html
%endif

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.13.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.13.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.11

* Mon Apr 04 2022 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.13.0-1
- Update to version 0.13.0 (#2071366)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 30 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.12.0-1
- Update to version 0.12.0 (#2005745)

* Tue Aug 31 2021 Chedi Toueiti <chedi.toueigi@gmail.com> - 0.11.1-1
- Update to version 0.11.1 (#1998704)

* Thu Aug 05 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.11.0-1
- Update to version 0.11.0 (#1986615)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.9-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.9.9-1
- Update to 0.9.9

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-2
- Subpackage python2-anyconfig has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Brett Lentz <blentz@redhat.com) - 0.9.7-1
- update to 0.9.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Satoru SATOH <ssato@redhat.com> - 0.9.4-1
- change: drop python 3.3 support as isort required by pylint does so
- change: separate some backends (cbor, bson and msgpack) from this package
- fix: [ini] configparser.ConfigParser.readfp is deprecated method
- fix/refactor: cleanup, refactor and fix test cases
- change: [api] change the parameter name, s/.*safe/ac_schema_safe/g
- fix: [rpm] A lot of cleanups originally from rhbz#1538658
- enhancement: add support to catch all errors during validation (issue#79),
  and its test case

* Mon Jun 19 2017 Satoru SATOH <ssato@redhat.com> - 0.9.3-1
- Just add an workaround for travi-ci test errors in python 3.{3,4}

* Sat Jun 10 2017 Satoru SATOH <ssato@redhat.com> - 0.9.2-1
- enhancement: allow ac_merge to be a callable for user-defined merge
  strategies (thanks to csboling!)
- enhancement: [yaml] Use ruamel.yaml instead of PyYAML if it's available
- fix: remove staff of wercker bought by oracle
- fix: replace '\n' w/ os.linesep
- fix: [xml] misc fixes and refactorings
- refactor: split backend parser to some base classes to simplify and make them
  clean as much as possible
- doc: a lot of cleanups and enhancements

* Sun Mar 12 2017 Satoru SATOH <ssato@redhat.com> - 0.9.1-1
- fix: correct behavior around ac_dict to ignore ac_dict if backend cannot
  support to customize dict to be used in making results from loaded data.
- fix: check if result mapping objects are not None in some backend to avoid
  critical errors and add such test cases
- fix: [yaml] make ac_ordered and ac_dict worked on load
- change: [cli] switch from optparse to argparse as it is deprecated
- doc: minor expression updates

* Thu Mar  9 2017 Satoru SATOH <ssato@redhat.com> - 0.9.0-1
- api: remove m9dicts dependency and utilize anyconfig.dicts.* instead
- api: export merge (anyconfig.dicts.merge) instead of to_container which was
  deprecated and removed
- api: add 'ac_dict' keyword option for *load* APIs to be used in backends
- api: add experimental new API 'query', just an wrapper for .query.query
  actually with JMESPath expressions
- api: do not convert resuls from load APIs with to_container any more
- fix: [xml] ensure {namespace}:{tag,attribute} converted to
  namespace_prefix:{tag,attribute} on load
- fix/enhancement: [xml] Some more code cleanups, fixes and enhancements
- fix: [shellvars] remove the member _dict_options 'container' which conflicts
  with container keyword argument and 'ac_dict' alternates it
- fix: [properties] remove the member _dict_options 'container' which conflicts
  with container keyword argument and 'ac_dict' alternates it
- enhancement: make backend implementations not depends on container class and
- enhancement: move test cases in anyconfig/tests/ to tests/ and consolidate
  backend tests; now most backend parser should be checked in same manner
- enhancement: [cli] add -Q/--query option to query with JMESPath expression
- refactor: enhance and consolidate common functions into backend base class
  and implement backend parsers more declarative and with less code
- doc: add short description of ac_query keyword argument for *load* APIs
- doc: add tables to explain some keyword options for load/dump APIs
- doc: add JMESpath usage section
- doc: add some --query usage examples
- doc: add some missing module docs and misc fixes
- A lot of other enhancements, refactorings and bug fixes

* Mon Feb 20 2017 Satoru SATOH <ssato@redhat.com> - 0.8.2-1
- fix/enhancement: [xml] A lot of code cleanups, fixes and enhancements
- doc: fix indentations and other misc fixes
- A lot of other enhancements, refactorings and bug fixes

* Sun Feb 12 2017 Satoru SATOH <ssato@redhat.com> - 0.8.1-1
- fix: doc indentations and other misc fixes
- fix: do not build doc in the RPM SPEC to avoid possible docutils bug

* Sun Feb 12 2017 Satoru SATOH <ssato@redhat.com> - 0.8.0-1
- api: remove 'set_loglevel' API
- api: add 'open' API to open files with correct open mode, derived from the
  issue reported by ajays20078, thanks!
- change: now all API calls may fail if it could not find the appropriate
  backend and cannot process more
- change: add python 3.6 support
- change: drop python 3.2 support
- enhancement: add development status headers to all backend modules' code
- change: [ini] Keep order of items as much as possible if ac_ordered == True
- change: [properties] Fix the parser in mind key and value seprators
  correctly, original issue was reported by meticulous, thanks!
- change: [shellvars] Added to load vars in b-shell (bash) scripts
- change: [xml] make use of cElementTree (C version of ElementTree) if possible
- change: [xml] treat some cases as special to avoid extra node added and
  simplify the result dict as muc h as possible
- enhancement: update docs to add notes of the new 'open' API, section about
  logging, notes of JSON schema generation and so on
- A lot of other enhancements, refactorings and bug fixes

* Tue Oct 11 2016 Satoru SATOH <ssato@redhat.com> - 0.7.0-1
- enhancement: introduced ac_schema_type to generate more strict schema
- enhancement: introduced shellvars backend originally suggested by ajays20078
- fix: comment processing and some related fixes in properties backend most of
  all reported and actual fix implementations by ajays20078; thanks a lot
- fix: Add missing import error test cases
- some other enhancements, refactorings and bug fixes

* Sat Apr 30 2016 Satoru SATOH <ssato@redhat.com> - 0.6.0-1
- fix: remove extra line breaks just after each section headers and items when
  dumping INI format config files in ini backend, reported by ajays20078
- fix: make ac_safe option worked for dump API of yaml backend as expected,
  reported by ajays20078
- refactor: log error messages in anyconfig.find_loader always if something
  goes wrong; no parser given or given parser not found
- fix: make anyconfig.loads returning None if no parser or parser is not found
- change: try parsing optional arguments with anyconfig.parser.parse instead of
  anyconfig.loads in the CLI frontend
- enhancement: improve package description in setup.py, README.rst and doc
- enhancement: add AUTHORS.txt to list authors and contributors

* Sun Feb 21 2016 Satoru SATOH <ssato@redhat.com> - 0.5.0-1
- change: switch to m9dicts as mearge-able dict, successor of .mergeabledict
- enhancement: try to keep order of keys in all backends as wanted, although
  some ones such as bson, json in python 2.6, msgpack in python 3 and yaml does
  not work still
- enhancement: support namedtuple <-> dict[-like] object conversion
- fix: resolve some rpmlint warns such as macro used in the comment lines
- fix/enhancement: add missing corner and ordered test cases
- refactor: Refactoring all test backend test cases to simplify them

* Sun Nov 22 2015 Satoru SATOH <ssato@redhat.com> - 0.4.0-1
- fix: correct escape/unescape process in Java properties backend, closed #31
- enhancement: Added naive impl. of JSON Pointer support (getter only)
- refactor: Refactoring around backend base classes, loaders and dumpers
- some other enhancements, refactorings and bug fixes

* Tue Oct 20 2015 Satoru SATOH <ssato@redhat.com> - 0.3.0-1
- Enhance anyconfig.multiload not to resolv appropriate config parsers
  everytime loading config files
- Remove a few backend (common and specific) and common options such as merge
  (ac_merge), marker (ac_marker), etc. from definitions of some public API
  functions
- Add 'ac_' prefix to some keyword arguments to public APIs
- fix wrong definition of extensions in BSON backend
- fix a bug that ini (configparser) backend behaves different from original;
  may close #28
- fix a bug to pass extra keyword parameters to yaml.safe_load
- fix a bug that anyconfig.backend.base.LParser.load_from_string does not
  process and pass process keyword args `kwargs`
- add some more API usage code examples in the doc
- a lot of other enhancements, refactorings and bug fixes; some of them might
  break public nad internal APIs so that bumped up the version

* Mon Sep 21 2015 Satoru SATOH <ssato@redhat.com> - 0.2.2-1
- Lower the level of some warn logging messages if backend support module is
  not available
- Cleanup the doc of PyPI page
- Add logging settings in the doc

* Fri Sep 18 2015 Satoru SATOH <ssato@redhat.com> - 0.2.0-1
- new API anyconfig.to_container, factory method to create container objects
- enale processing of stream in anyconfig.*load and anyconfig.*dump
- add a native implementation of Java properties file backend
- misc doc updates about new backend, APIs, etc.
- massive refactoring of some complex modules such as api, cli, mergeabledict,
  parser and some backends and also add some more corner test cases
- some more minor possible bug fixes found by pylint and flake8

* Sat Aug 15 2015 Satoru SATOH <ssato@redhat.com> - 0.1.0-1
- add BSON support
- add TOML support
- fix XML load and dump functions
- add some more corner test cases to improve test coverage
- clean up and refactor some test cases
- clean up the RPM SPEC to sort out requirements
- make HTML doc built for fedora only
- some more minor possible bug fixes found by pylint and flake8

* Mon Aug 10 2015 Satoru SATOH <ssato@redhat.com> - 0.0.13-1
- fix up broken PyPI description page

* Mon Aug 10 2015 Satoru SATOH <ssato@redhat.com> - 0.0.12-1
- add some usage examples of the CLI frontend in the doc
- fix some trivial bugs in the CLI frontend
- make the contents of README and the doc consistent
- make the doc included in RPM packages

* Wed Aug  5 2015 Satoru SATOH <ssato@redhat.com> - 0.0.11-1
- add MessagePack load/dump support
- add new API 'gen_schema' to generate JSON schema for given configs
- fix some bugs around JSON schema validation while loading configs
- add HTML doc in a package
- simplify README.rst a lot and just left a reference to
  http://python-anyconfig.readthedocs.org provides online HTML doc
- some more minor possible bug fixes found by pylint and flake8

* Sun Jun 21 2015 Satoru SATOH <ssato@redhat.com> - 0.0.10-1
- add new API 'validate' to validate config files with json schema
- some more minor possible bug fixes found by pylint and flake8

* Sun Jun 14 2015 Satoru SATOH <ssato@redhat.com> - 0.0.9-1
- merge configobj backend
- some more minor possible bug fixes found by pylint and flake8
- minor expression updates and fixes in README.rst

* Tue May 26 2015 Satoru SATOH <ssato@redhat.com> - 0.0.8-1
- remove os.curdir from a list of default template search paths, may close #18
- remove a global, SUPPORTED and import-error hack around it completely; now
  implementation of backends are simplified a lot
- fix a lot of pylint and flake8 warnings
- some more minor bug fixes and enhancements

* Thu Apr 23 2015 Satoru SATOH <ssato@redhat.com> - 0.0.7-1
- module level logging fixes and improvements, may close issue#13 and issue#14
- export anyconfig.api.set_ to public which was not exported
- rename a few function parameters template and context passed to *load* to
  avoid conflicts with parameters intended to pass to backends
- reorder some arguments passed to anyconfig.api.*load to keep consistency in
  the order of arguments among them
- add --env option to the CLI frontend to pass configuration default values
  from envrionment variables
- some more minor bug fixes and enhancements

* Fri Mar 13 2015 Satoru SATOH <ssato@redhat.com> - 0.0.6-1
- show ini file structure erros by Kamil Chmielewski, closes PR#8
- beautify README.rst by Florian Ludwig, closes PR#10
- add support to load template config files
- removes all custom logging magic and changes the behaviour to the standard
  way of logging for Python libraries by Wouter Bolsterlee, closed PR#11
- re-enable Travis-CI tests for python 2.6
- some more minor bug fixes and enhancements

* Sun Oct 26 2014 Satoru SATOH <ssato@redhat.com> - 0.0.5-1
- start to monitor code coverage w/ using coveralls.io
- start to do extra health check by landscape.io
- introduce 'ignore_missing' optional parameter to ignore missing config
  file[s] in anyconfig.apy.*load() originally suggested by chmac in issue#4
- add -x/--ignore-missing option to allow ignoring missing files in anyconfig_cli
- make xml backend loader worked although it nees a lot more work
- fix a typo in README.rst by Jonathan Eunice, closes PR#1
- some more minor bug fixes and enhancements

* Tue Aug 19 2014 Satoru SATOH <ssato@redhat.com> - 0.0.4-1
- Change the versioning scheme and bump up the version to fix the issue #3

* Fri Aug  1 2014 Satoru SATOH <ssato@redhat.com> - 0.0.3.13-1
- Enable flake8 (pyFlake + pep8) testing
- Fix some minor errors like F401 (import-but-not-used eror) found by flake8
- Introduce an environment variable ANYCONFIG_DEBUG to control module's log
  level from outside world
- Add anyconfig.getset module and --get option to anyconfig cli frontend to get
  (extract) partial configuration[s] from loaded config files
- Add python 3.4 support and also make it tested in CI process

* Sat May  3 2014 Satoru SATOH <ssato@redhat.com> - 0.0.3.12-1
- Support safe_{load,dump} in YAML backend by safe=True argument
- Add some more keyword arguments support in JSON backend
- Add man page of anyconfig_cli
- Misc fixes and enhancements in anyconfig_cli
- Some PEP8 and pylint errors and warnings
- Fix some rpmlint errors

* Fri Jan 10 2014 Satoru SATOH <ssato@redhat.com> - 0.0.3.11-1
- Just a maintenance update release
- Add pylint checks and refactor test driver script
- Fix some PEP8 and pylint errors and warnings

* Thu May  2 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.10-1
- [anyconfig_cli] Fix a typo in its filename; s/anyconfg/anyconfig/g,
  it's alsot pointed by jonathaneunice-san. Thanks a lot!
- Swtich to use setuptools instead of standard distutils to allow writing
  various pluggable backends
- Implement pluggable backend system w/ using setuptools
- Fix some build and runtime dependencies to PyYAML and setuptools
- Spin off java properties file backend into a separate project:
  https://github.com/ssato/python-anyconfig-pyjavaproperties-backend
- Fix some type mismatches in methods of backend modules
- Make cli frontend generated w/ setuptools' help and remove tools/*

* Sun Mar 31 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.9-1
- Some fixes and enhancements around logging code
- [anyconfig_cli] add -s/--silent and -v/--verbose option to control log level
  and removed -d/--debug option
- Allow swtich from/to build time snapshot-versioning-mode dynamically
- Build also RPMs for python-3.x
- Allow backend specific options passed to load*/dump* methods of some backends
- Ensure dir to dump output created if that dir not exist

* Wed Mar 13 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.8-1
- Do not expose internal repr. of loaded data when dump them
- Fix for ini (configparser) backend

* Tue Mar 12 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.7-1
- change API from anyconfig.find_parser to anyconfig.find_loader
- [anyconfig_cli] rename cli frontend from anyconfig_cui to anyconfig_cli
- [anyconfig_cli] add new option '-M/--merge' to select strategy to merge
  multiple configs
- add 'noreplace' merging strategy
- fix the bug that 'replace' merge strategy (value: 0) was evaluated as False
  and cause an 'invalid strategy' error, and change default merging strategy
- other misc fixes for PEP8 errors and warns, etc.

* Fri Feb  1 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.6-1
- Added -A and --atype option to anyconfig_cui to override configs w/ -A option
- Fixed an error in anyconfig.api.loads when config type is None
- Updated usage example of anyconfig_cui in README

* Fri Jan 18 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.5-1
- Changed the default merge strategy of anyconfig.mergeabledict.MergeableDict
  from merge_dicts_and_lists to merge_dicts
- Updated README and added some usage examples

* Thu Jan 17 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.4-1
- Fine tunes in some APIs to load multi config files
- Updated and enhanced CUI frontend, anyconfig_cui
- Fixed a bug in anyconfig.Bunch.update_w_merge that cause error when merging
  lists with passing merge_lists=True argument
- Updated module's doctext and added some usage examples
- Removed strong dependency to anyconfig.Bunch.Bunch, and switched to
  anyconfig.mergeabledict.MergeableDict which is stripped-down version of
  anyconfig.Bunch.Bunch object

* Fri Jan  4 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.3-1
- Changed APIs (new: load, {single,mulit}_load) and some cleanups
- Complemented some meta package info to register this module to PyPI
- Changed the name of python module; stripped 'python-' from its name

* Fri Jan  4 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.2-1
- Fixed a few that yaml.* and etree.* not defined when yaml and etree module is
  not found, causing build time error

* Fri Jan  4 2013 Satoru SATOH <ssato@redhat.com> - 0.0.3.1-1
- Added metaconfig module to control config-loading behavior
- Added some new APIs including anyconfig.{mload,loads}, etc.
- Started CI tests w/ Travis

* Sat Aug  4 2012 Satoru SATOH <ssato@redhat.com> - 0.0.3-1
- Fixed a grave syntax error in anyconfig.backend.properties_
- Some docstring cleanups
- Some refactoring
- Implemented dicts merge/replacements came from config files

* Mon Jul  2 2012 Satoru SATOH <ssato@redhat.com> - 0.0.2-1
- Fixed packaging bug that some modules were missing from the list

* Fri Jun 29 2012 Satoru SATOH <ssato@redhat.com> - 0.0.1-1
- Initial packaging
