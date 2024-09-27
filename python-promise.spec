%global pypi_name promise

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        20%{?dist}
Summary:        Promises/A+ implementation for Python

License:        MIT
URL:            https://github.com/syrusakbary/promise
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# https://github.com/syrusakbary/promise/pull/96
Patch0:         https://github.com/syrusakbary/promise/commit/381687df55fda715a87395f7ffba1c91428650e2.patch

# Patch for Python 3.11 compatibility
Patch1:         https://github.com/syrusakbary/promise/pull/99.patch

BuildArch:      noarch

%description
This is a implementation of Promises in Python. It is a super set of
Promises/A+ designed to have readable, performant code and to provide just the
extensions that are absolutely necessary for using promises in Python.
It's fully compatible with the Promises/A+ spec.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-coveralls
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a implementation of Promises in Python. It is a super set of
Promises/A+ designed to have readable, performant code and to provide just the
extensions that are absolutely necessary for using promises in Python.
It's fully compatible with the Promises/A+ spec.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-19
- Rebuilt for Python 3.13

* Thu Feb 22 2024 Michel Lind <salimma@fedoraproject.org> - 2.3.0-18
- Remove unnecessary and deprecated python3-mock BR

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.3.0-14
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 2.3.0-11
- Add patch for Python 3.11 compatibility

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-10
- Rebuilt for Python 3.11

* Fri Mar 04 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-9
- Add patch for Pytest 7 (closes rhbz#2059964)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-3
- Fix changelog entry

* Thu Jul 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-2
- Add major release to BR (rhzb#1836559)

* Thu May 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-1
- Initial package for Fedora
