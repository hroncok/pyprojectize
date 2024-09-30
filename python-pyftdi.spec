%global pypi_name pyftdi

Name:           python-%{pypi_name}
Version:        0.55.4
Release:        4%{?dist}
Summary:        Python support for FTDI devices

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/eblot/pyftdi
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyFtdi aims at providing a user-space driver for modern FTDI devices.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
PyFtdi aims at providing a user-space driver for modern FTDI devices.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/*.py

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.55.4-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.55.4-2
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.55.4-1
- Update to latest upstream release (closes rhbz#2274307)

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.55.3-1
- Update to latest upstream release 0.55.3 (closes rhbz#2273801)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.55.0-1
- Update to latest upstream release 0.55.0 (closes rhbz#2231618)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.54.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.54.0-2
- Rebuilt for Python 3.11

* Fri Mar 18 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.54.0-1
- Update to latest upstream release 0.54.0 (closes rhbz#2063586)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.53.3-1
- Update to latest upstream release 0.53.3 (rhbz#1959517)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.52.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.52.9-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.52.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.52.9-1
- Update to latest upstream release 0.52.9 (#1915565)

* Tue Sep 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.52.0-1
- Update to latest upstream release 0.52.0 (#1882892)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.51.2-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.51.2-1
- Update to latest upstream release 0.51.2 (#1826260)

* Wed Apr 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.50.2-1
- Update to latest upstream release 0.50.1 (#1826260)

* Fri Apr 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.50.1-1
- Update to latest upstream release 0.50.1 (#1821032)

* Sun Apr 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.50.0-1
- Update to latest upstream release 0.50.0 (#1821032)

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.48.3-1
- Update to latest upstream release 0.48.3 (#1816213)

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.48.2-1
- Update to latest upstream release 0.48.2 (#1816213)

* Tue Mar 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.47.2-1
- Update to latest upstream release 0.47.2 (#1815122)

* Tue Mar 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.46-1
- Update to latest upstream release 0.46

* Sat Feb 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.44.2-1
- Move docs to subpackage
- Update to latest upstream release 0.44.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.42.2-1
- Update to latest upstream release 0.42.2

* Wed Sep 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.30.3-1
- Update to latest upstream release 0.30.3

* Sat Sep 07 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.30.0-1
- Update to latest upstream release 0.30.0

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.29.6-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.29.6-1
- Update to latest upstream release 0.29.6
- Fix license tag (#1732803)

* Wed Jul 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.29.2-1
- Initial package for Fedora
