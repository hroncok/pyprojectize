%bcond_with tests

Name:           adb-enhanced
Version:        2.5.14
Release:        11%{?dist}
Summary:        Tool for Android testing and development

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/ashishb/adb-enhanced
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
ADB-Enhanced is a Swiss-army knife for Android testing and development. A
command-line interface to trigger various scenarios like screen rotation,
battery saver mode, data saver mode, doze mode, permission grant/revocation.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files adbe

%if %{with tests}
%check
%pytest -v tests/adbe_tests.py
%endif

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/adbe

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.14-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.5.14-9
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.5.14-5
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.14-2
- Rebuilt for Python 3.11

* Fri Mar 11 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.14-1
- Update to latest upstream release 2.5.14 (closes rhbz#2063059)

* Thu Mar 03 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.13-1
- Update to latest upstream release 2.5.13 (closes rhbz#2058429)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.12-1
- Update to latest upstream release 2.5.12 (closes rhbz#2014826)

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.11-1
- Update to latest upstream release 2.5.11 (closes rhbz#1953156)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.5.10-2
- Rebuilt for Python 3.10

* Wed Feb 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.10-1
- Update to latest upstream release 2.5.10 (#1922957)

* Tue Feb 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.9-1
- Update to latest upstream release 2.5.9 (#1922957)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.8-1
- Update to latest upstream release 2.5.8 (#1910345)

* Tue Dec 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.7-1
- Update to latest upstream release 2.5.7 (#1898458)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.4-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.4-1
- Update prep section
- Update to latest upstream release (#1819115)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.2-1
- Initial package for Fedora
