%global pypi_name HASS-data-detective
%global pkg_name hass-data-detective

Name:           python-%{pkg_name}
Version:        2.4
Release:        14%{?dist}
Summary:        Tools for studying Home Assistant data

License:        MIT
URL:            https://github.com/robmarkcole/HASS-data-detective
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides a set of convenience functions and classes to analyze the
data in your Home Assistant database.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pandas
BuildRequires:  python3-pytz
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
This package provides a set of convenience functions and classes to analyze the
data in your Home Assistant database.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e 's/2.1/2.3/g' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/detective/
%{python3_sitelib}/HASS_data_detective-%{version}.dist-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.4-13
- Rebuilt for Python 3.13

* Mon Mar 25 2024 Nils Philippsen <nils@tiptoe.de> - 2.4-12
- Reenable test which failed in the past

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.4-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.4-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4-2
- Rebuilt for Python 3.10

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.4-1
- Update to latest upstream release 2.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-4
- Fix FTBFS (rhbz#1865291)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-1
- Update to new upstream release 2.3

* Tue Jun 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1-1
- Initial package for Fedora
