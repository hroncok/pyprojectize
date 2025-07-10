Name:           wad
Version:        0.4.6
Release:        16%{?dist}
Summary:        Tool for detecting technologies used by web applications

# wad is GPLv3, wappalyzer source is MIT
# Automatically converted from old format: GPLv3 and MIT - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-MIT
URL:            https://github.com/CERN-CERT/WAD
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist mock
BuildRequires:  %py3_dist six

%description
WAD lets you analyze given URL(s) and detect technologies used by web
application behind that URL, from the OS and web server level, to the
programming platform and frameworks, as well as server- and client-side
applications, tools and libraries.

%prep
%autosetup -n %{name}-%{version}
mv wad/etc/README.md wad/etc/README-wappalyzer.md

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%check
%pyproject_check_import

%pytest -v %{name}/tests

%files -f %{pyproject_files}
%doc README.md wad/etc/README-wappalyzer.md
%{_bindir}/wad

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.6-16
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.6-14
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.6-11
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.6-8
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-6
- BuildRequire python3-six which is used but was only transitively pulled in by python3-mock

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.6-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.6-2
- Update macros

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.6-1
- Update to latest upstream release 0.4.6 (#1883156)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.5-1
- Update to latest upstream release 0.4.5 (#1882610)

* Thu Aug 20 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 0.4.4-1
- Update to latest upstream release 0.4.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 0.4.3-1
- Update to latest upstream release 0.4.3

* Sat May 16 2020 Fabian Affolter  <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream release 0.4.2
- Fix for Python 3.9 (rhbz#1834183)
 
* Thu Apr 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora

