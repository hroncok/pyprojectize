%global         pypi_name cli_helpers

Summary:        Python helpers for common CLI tasks
Name:           python-cli-helpers
Version:        2.3.1
Release:        4%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dbcli/cli_helpers
Source0:        https://github.com/dbcli/cli_helpers/archive/v%{version}/cli_helpers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-configobj
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-tabulate
BuildRequires:  python3-terminaltables
BuildRequires:  python3-wcwidth
%global _description\
CLI Helpers is a Python package that makes it easy to perform common\
tasks when building command-line apps. Its a helper library for\
command-line interfaces.
%description %_description

%package -n     python3-cli-helpers
Summary:        %{summary}
Requires:       python3-configobj >= 5.0.5
Requires:       python3-pygments >= 1.6
Requires:       python3-tabulate >= 0.8.2
Requires:       python3-terminaltables >= 3.0.0
Requires:       python3-wcwidth
%description -n python3-cli-helpers %_description

%pyproject_extras_subpkg -n python3-cli-helpers styles

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
PYTHONPATH=build/lib/ py.test-3

%files -n python3-cli-helpers -f %{pyproject_files}
%doc AUTHORS CHANGELOG README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.1-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.3.1-2
- Rebuilt for Python 3.13

* Tue Feb 06 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-1
- 2.3.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.12

* Wed Apr 05 2023 Terje Rosten <terje.rosten@ntnu.no> - 2.3.0-3
- mock dep was removed in 2.0.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 23 2022 Terje Rosten <terje.rosten@ntnu.no> - 2.3.0-1
- 2.3.0
- Remove lagacy Python 2 subpackage

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Terje Rosten <terje.rosten@ntnu.no> - 2.2.1-1
- 2.2.1

* Sat Sep 04 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-1
- 2.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.1.0-1
- 2.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.0.1-1
- 2.0.1

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Add cli-helpers[styles] subpackage

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-1
- 1.2.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-1
- 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.7

* Mon May 21 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.2-2
- Fix description, (rhzb#1580109), thanks to Dick Marinus!

* Sun Apr 08 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.2-1
- 1.0.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-2
- Fix reqs.

* Thu Jan 04 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1

* Tue Oct 24 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.0.0-1
- 1.0.0

* Wed Aug 16 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-1
- 0.2.3
- Rename
- Use summary and desc macros
- Drop Python 2 sub package for now, backports.csv not available
- Add patch to remove Python 2 specific reqs into Python 3 package

* Mon Jun 26 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.2.0-1
- 0.2.0
- Rename

* Mon May 15 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.1.0-2
- Minor tweaks

* Sat May 13 2017 Dick Marinus <dick@mrns.nl> - 0.1.0-1
- Initial package
