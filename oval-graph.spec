%global name        oval-graph
%global module      oval_graph

Summary:            Tool for visualization of SCAP rule evaluation results
Name:               %{name}
Version:            1.3.3
Release:            11%{?dist}
# The entire source code is ASL 2.0 except schemas/ which is Public Domain
License:            ASL 2.0 and Public Domain

Url:                https://pypi.org/project/%{name}/
Source0:            https://files.pythonhosted.org/packages/source/o/%{name}/%{module}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
Requires:           python3-lxml

%description
Oval_graph is a tool that displays the results of evaluating SCAP rules.
In the form of a tree according to the OVAL standard. Using the
`arf-to-graph` command, you can simply view the result of rule.
Use `arf-to-json` to generate a rule result in json. Using the
`json-to-graph` command, you can view the results of rules from json file.

%prep
%autosetup -n %{module}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{module}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/arf-to-graph
%{_bindir}/arf-to-json
%{_bindir}/json-to-graph

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.3-10
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.3-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.3-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 1.3.3-1
- 1.3.3 (Jan Rodak)
- Create unit test (Jan Rodak)
- Fix issue 204 (Jan Rodak)
- Remove unused variable (Jan Rodak)
- Add missing var declarator (Jan Rodak)
- Fix pylint R0801: Similar lines in 2 files (Jan Rodak)
- Fix pylint too-many-public-methods (Jan Rodak)
- Ignore pylint too-few-public-methods (Jan Rodak)
- Ignore pylint consider-using-with (Jan Rodak)
- Fix pylint use-dict-literal (Jan Rodak)
- Fix pylint unspecified-encoding (Jan Rodak)
- Format string with f-string (Jan Rodak)
- Fix typo (Jan Rodak)

* Fri Oct 15 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 1.3.2-1
- 1.3.2 (Jan Rodak)
- Create test for fix (Jan Rodak)
- Fix bugzilla 2011382 (Jan Rodak)

* Mon Sep 20 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 1.3.1-1
- 1.3.1 (Jan Rodak)
- Fix missing test files (Jan Rodak)

* Mon Aug 02 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 1.2.8-1
- 1.2.8 (Jan Rodak)
- Changes name of test functions (Jan Rodak)
- Changes output of test_commands (Jan Rodak)
- Changes how are loaded path (Jan Rodak)
- Removes an unnecessary method (Jan Rodak)
- Improves naming of metodes (Jan Rodak)
- Reworks completion of message (Jan Rodak)
- Creates global namespaces for parsing XML (Jan Rodak)
- Renames parsers classes (Jan Rodak)
- Changes methods to static methods in the parser for comments (Jan Rodak)
- Reduces the number of parameters in the method (Jan Rodak)
- Moves the creation of the test node and the extended definition node to separate methods (Jan Rodak)
- Changes method to static method in the parser for oval scan definitions (Jan Rodak)
- Uses global dictionary for conversion bool values (Jan Rodak)
- Simplify the method (Jan Rodak)
- Changes methods to static methods in the parser for test info (Jan Rodak)
- Improves code formatting (Jan Rodak)
- Removes an unnecessary method (Jan Rodak)
- Improves search in oval system characteristics (Jan Rodak)
- Changes tests for new arf xml parser (Jan Rodak)
- Changes clinet for new arf xml parser (Jan Rodak)
- Improves raise error (Jan Rodak)
- Removes unnecessary variables (Jan Rodak)
- Improves xml validation (Jan Rodak)
- Reworks loading rules form profile (Jan Rodak)
- Changes formatting in a benchmark for ARF XML parser (Jan Rodak)
- Moves XML parser part to separate directory (Jan Rodak)
- Reworks check for the generated HTML (Jan Rodak)
- Reworks generating HTML (Jan Rodak)
- Reworks opening web browser with a report (Jan Rodak)
- Fixes tests after change verbose output (Jan Rodak)
- Removes unnecessary function parameter (Jan Rodak)
- Rework verbose output (Jan Rodak)
- Renemes class (Jan Rodak)
- Creates sub modul for creating HTML (Jan Rodak)
- Updates tests (Jan Rodak)
- Implements new OVAL gate evaluation to OVAL tree (Jan Rodak)
- Reworks OVAL gate evaluation (Jan Rodak)

* Mon Aug 02 2021 Jan Rodak <jrodak@redhat.com> - 1.2.8-1
- release 1.2.8

* Wed May 26 2021 Jan Rodak <jrodak@redhat.com> - 1.2.7-1
- release 1.2.7

* Wed May 26 2021 Jan Rodak <jrodak@redhat.com> - 1.2.6-1
- release 1.2.6

* Tue Feb 23 2021 Jan Rodak <jrodak@redhat.com> - 1.2.5-1
- release 1.2.5

* Thu Dec 10 2020 Jan Rodak <jrodak@redhat.com> - 1.2.4-1
- release 1.2.4

* Mon Nov 09 2020 Jan Rodak <jrodak@redhat.com> - 1.2.3-1
- release 1.2.3

* Mon Oct 12 2020 Jan Rodak <jrodak@redhat.com> - 1.2.2-1
- release 1.2.2

* Mon Sep 21 2020 Jan Rodak <jrodak@redhat.com> - 1.2.1-1
- release 1.2.1

* Thu Sep 03 2020 Jan Rodak <jrodak@redhat.com> - 1.2.0-1
- release 1.2.0

* Fri Apr 17 2020 Jan Rodak <jrodak@redhat.com> - 1.1.1-1
- release 1.1.1

* Fri Apr 17 2020 Jan Rodak <jrodak@redhat.com> - 1.1.0-2
- Fixes the required dependency

* Wed Apr 15 2020 Jan Rodak <jrodak@redhat.com> - 1.1.0-1
- release 1.1.0

* Mon Mar 09 2020 Jan Rodak <jrodak@redhat.com> - 1.0.1-1
- release 1.0.1

* Mon Mar 09 2020 Jan Rodak <jrodak@redhat.com> - 1.0.0-1
- release 1.0.0

* Wed Jan 22 2020  Jan Rodak <jrodak@redhat.com> - 0.1.2-1
- Improved performance
- New commands

* Wed Nov 13 2019  Jan Rodak <jrodak@redhat.com> - 0.0.2-1
- Changed CR+LF to LF line endings.

* Wed Oct 23 2019  Jan Rodak <jrodak@redhat.com> - 0.0.1-1
- Initial version of the package.

