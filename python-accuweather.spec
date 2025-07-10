%global pypi_name accuweather

Name:           python-%{pypi_name}
Version:        0.0.11
Release:        15%{?dist}
Summary:        Python wrapper for getting data from AccuWeather servers

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/bieniu/accuweather
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python wrapper for getting weather data from AccuWeather
servers for Limited Trial package.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)

%description -n python3-%{pypi_name}
Python wrapper for getting weather data from AccuWeather
servers for Limited Trial package.

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

%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.11-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.11-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.0.11-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.0.11-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.11-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.11-1
- Update to latest upstream release 0.0.11

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Initial package for Fedora