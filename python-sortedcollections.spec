%global pypi_name sortedcollections

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        17%{?dist}
Summary:        Python Sorted Collections

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://www.grantjenks.com/docs/sortedcollections
Source0:        https://github.com/grantjenks/python-sortedcollections/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python Sorted Collections Sorted Collections is an Apache2 licensed Python
sorted collections library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(sortedcontainers)

%description -n python3-%{pypi_name}
Python Sorted Collections Sorted Collections is an Apache2 licensed Python
sorted collections library.

%prep
%autosetup -n python-%{pypi_name}-%{version}
# Requiring 100% test coverage may make sense upstream, but it is needlessly
# brittle here. This patch modifies tox.ini so that pytest does not fail based
# on coverage.
sed -i -e '/--cov-fail-under=100/d' tox.ini
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-17
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.0-15
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.0-6
- Patch tox.ini to allow less than 100% test coverage (fixes RHBZ#1958936)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0 (#1917090)

* Mon Jan 18 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Update to latest upstream release 2.0.1 (#1917090)

* Wed Jan 06 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-1
- Update to latest upstream release 1.2.3 (#1913147)

* Sun Sep 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-3
- Add missing BR

* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-2
- Change source to GitHub
- Run tests (rhbz#1876911)

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Initial package for Fedora
