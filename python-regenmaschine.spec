%global pypi_name regenmaschine

Name:           python-%{pypi_name}
Version:        2022.9.2
Release:        8%{?dist}
Summary:        Python API for RainMachine sprinkler controllers

License:        MIT
URL:            https://github.com/bachya/regenmaschine
Source0:        %{pypi_source}
BuildArch:      noarch

%description
regenmaschine (German for "rain machine") is a simple Python library for
interacting with RainMachine smart sprinkler controllers. It gives developers
an easy API to manage their controllers over their local LAN or remotely via
the RainMachine cloud.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
regenmaschine (German for "rain machine") is a simple Python library for
interacting with RainMachine smart sprinkler controllers. It gives developers
an easy API to manage their controllers over their local LAN or remotely via
the RainMachine cloud.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2022.9.2-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2022.9.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2022.9.2-1
- Update to latest upstream release 3.1.5 (closes rhbz#2010505)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.5-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.5-1
- Update to latest upstream release 3.1.5 (closes rhbz#1917134)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.2-2
- Rebuilt for Python 3.10

* Tue Mar 02 2021  Fabian Affolter <mail@fabian-affolter.ch> - 3.1.2-1
- Update to latest upstream release 3.1.2 (#1917134)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021  Fabian Affolter <mail@fabian-affolter.ch> - 3.1.1-1
- Update to latest upstream release 3.1.1

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Initial package for Fedora
