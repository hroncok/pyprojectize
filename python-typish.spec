%global pypi_name typish

Name:           python-%{pypi_name}
Version:        1.9.3
Release:        13%{?dist}
Summary:        Python library for additional control over types

License:        MIT
URL:            https://github.com/ramonhagenaars/typish
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Suport for functions to allow thorough checks on types. Including instance
checks considering generics and typesafe duck-typing.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(nptyping)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(coverage)

%description -n python3-%{pypi_name}
Suport for functions to allow thorough checks on types. Including instance
checks considering generics and typesafe duck-typing.

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
# https://github.com/ramonhagenaars/typish/issues/18
%pytest -v tests -k "not test_instance_of_union and not test_is_type_annotation and not test_subclass_of_union and not test_get_origin and not test_instance_of_nptyping_ndarray"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.9.3-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 1.9.3-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.3-6
- Disable failing test

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.3-5
- Fix build (closes rhbz#2113659)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.3-1
- Update to latest upstream release 1.9.3 (rhbz#1948213)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.1-1
- Update to latest upstream release 1.9.1 (#1905677)

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-2
- Disable failing tests (rhbz#1875996)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Initial package for Fedora
