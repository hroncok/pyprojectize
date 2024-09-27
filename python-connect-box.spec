%global pypi_name connect_box
%global pkg_name connect-box

Name:           python-%{pkg_name}
Version:        0.4.0
Release:        3%{?dist}
Summary:        Python client for interacting with Compal CH7465LG devices

License:        MIT
URL:            https://github.com/home-assistant-ecosystem/python-connect-box
Source0:        %{pypi_source}
BuildArch:      noarch

%description
connect-box is a Python Client for interacting with the cable modem/router
Compal CH7465LG which is provided under different names by various ISP in
Europe.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
connect-box is a Python Client for interacting with the cable modem/router
Compal CH7465LG which is provided under different names by various ISP in
Europe.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.13

* Mon Apr 08 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-7
- Update to latest upstream release (closes rhbz#2270411)

* Mon Feb 05 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream release (closes rhbz#2257488)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Update to new upstream version 0.3.0 (rhbz#1965162)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.9-2
- Rebuilt for Python 3.10

* Sat Feb 06 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.9-1
- Update to latest upstream release 0.2.9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.8-1
- Update to latest upstream release 0.2.8 (#1874641)

* Tue Sep 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Initial package for Fedora
