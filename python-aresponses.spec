%global pypi_name aresponses
%bcond_with network

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        3%{?dist}
Summary:        Asyncio testing server

License:        MIT
URL:            https://github.com/circleup/aresponses
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
An asyncio testing server for mocking external services.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%description -n python3-%{pypi_name}
An asyncio testing server for mocking external services.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%if %{with network}
%pytest -v tests
%endif
%pytest -v tests -k "not test_foo and not test_passthrough"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.13

* Sat Feb 10 2024 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Update to latest upstream release (closes rhbz#2258019)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.1.6-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.6-1
- Update to new upstream version 2.1.6 (closes rhbz#2102952)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.1.5-2
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.5-1
- Update to new upstream version 2.1.5 (closes rhbz#2048030)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 08:26:21 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Update to latest upstream release 2.1.3 (#1917037)

* Sun Jan 17 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Update to latest upstream release 2.1.2 (#1917037)

* Mon Jan 11 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0 (#1910316)

* Wed Dec 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Update to latest upstream release 2.0.2 (#1910316)

* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Initial package for Fedora
