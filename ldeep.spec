%global pypi_name ldeep

Name:           %{pypi_name}
Version:        1.0.9
Release:        14%{?dist}
Summary:        LDAP enumeration utility

License:        MIT
URL:            https://github.com/franc-pentest/ldeep
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Tool to interact and enumerate LDAP instances.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Tool to interact and enumerate LDAP instances.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.9-13
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.9-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.9-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.9-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.9-1
- Update to latest upstream release 1.0.9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.8-1
- Initial package for Fedora

