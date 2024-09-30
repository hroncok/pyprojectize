%global pypi_name pydeconz
%global pkg_name deconz

Name:           python-%{pkg_name}
Version:        76
Release:        14%{?dist}
Summary:        Python library for communicating with deCONZ REST API

License:        MIT
URL:            https://github.com/Kane610/deconz
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python library for communicating with deCONZ REST API by
dresden elektronik. This implementation should cover most
devices supported by deCONZ.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiohttp)

%description -n python3-%{pkg_name}
Python library for communicating with deCONZ REST API by
dresden elektronik. This implementation should cover most
devices supported by deCONZ.

%prep
%autosetup -n %{pkg_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# Tests requires asynctest
# https://github.com/Kane610/deconz/issues/76
#%%check
#%%pytest -v tests

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 76-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 76-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 76-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 76-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 76-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 76-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 76-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 76-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 76-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 76-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 76-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 76-1
- Update to latest upstream release 76

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 73-1
- Update to latest upstream release 73

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 72-1
- Initial package