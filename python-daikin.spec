%global pypi_name pydaikin
%global pkg_name daikin

Name:           python-%{pkg_name}
Version:        2.4.0
Release:        15%{?dist}
Summary:        Python Daikin HVAC appliances interface

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://bitbucket.org/mustang51/pydaikin
Source0:        %{url}/get/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyDaikin is a standalone program and a library that interface air conditioners
from Daikin. Currently the following Daikin WiFi modules are supported:

- BRP069Axx/BRP069Bxx/BRP072Axx
- BRP15B61 aka. AirBase (similar protocol as BRP069Axx)
- BRP072B/Cxx (needs HTTPS access and a key)
- SKYFi (different protocol, have a password)

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(netifaces)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(urllib3)

%description -n python3-%{pkg_name}
PyDaikin is a standalone program and a library that interface air conditioners
from Daikin. Currently the following Daikin WiFi modules are supported:

- BRP069Axx/BRP069Bxx/BRP072Axx
- BRP15B61 aka. AirBase (similar protocol as BRP069Axx)
- BRP072B/Cxx (needs HTTPS access and a key)
- SKYFi (different protocol, have a password)

%prep
%autosetup -n mustang51-%{pypi_name}-d768d0acee75
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%pytest -v tests

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/pydaikin

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.4.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.4.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.4.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Initial package for Fedora
