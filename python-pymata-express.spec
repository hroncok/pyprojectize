%global pypi_name pymata-express

Name:           python-%{pypi_name}
Version:        1.21
Release:        12%{?dist}
Summary:        Python Protocol Abstraction Library For Arduino Firmata

# Automatically converted from old format: AGPLv3
License:        AGPL-3.0-only
URL:            https://github.com/MrYsLab/pymata-express
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Pymata-Express is a Firmata client that allows you to control an Arduino using
the high-performance FirmataExpress sketch. It uses a conventional Python API
for those that do not need or wish to use the asyncio programming paradigm of
pymata-express.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pymata-Express is a Firmata client that allows you to control an Arduino using
the high-performance FirmataExpress sketch. It uses a conventional Python API
for those that do not need or wish to use the asyncio programming paradigm of
pymata-express.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license license.txt
%{python3_sitelib}/pymata_express/
%{python3_sitelib}/pymata_express-%{version}-py*.egg-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.21-11
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.21-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.21-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.21-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.21-1
- Update to latest upstream release 1.21 (rhbz#1965824)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.20-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.20-1
- Update to latest upstream release 1.20 (rhbz#1965824)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.19-1
- Update to latest upstream release 1.19

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.17-1
- Update to latest upstream release 1.17

* Wed May 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.15-1
- Update to latest upstream release 1.15

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.13-1
- Update to latest upstream release 1.13

* Wed Apr 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-1
- Initial package for Fedora
