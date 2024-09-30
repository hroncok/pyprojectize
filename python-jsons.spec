%global pypi_name jsons

Name:           python-%{pypi_name}
Version:        1.5.0
Release:        12%{?dist}
Summary:        Python library for (de)serializing objects to/from JSON

License:        MIT
URL:            https://github.com/ramonhagenaars/jsons
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Jsons is a library that allows you to serialize your plain old Python
objects to readable json (dicts or strings) and deserialize them back.
No magic, no special types, no polluting your objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:	python3dist(typish)

%description -n python3-%{pypi_name}
Jsons is a library that allows you to serialize your plain old Python
objects to readable json (dicts or strings) and deserialize them back.
No magic, no special types, no polluting your objects.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -v tests --ignore tests/test_performance.py \
  -k "not test_dump_list_strict_no_cls and not test_dump_union and not test_dump_load_parameterized_collections"

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.5.0-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 1.5.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-5
- Disable failing test (closes rhbz#2113633)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to latest upstream release 1.5.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Remove condition
- Update to latest upstream release 1.3.0

* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-3
- Make performance tests optional

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-2
- Add missing BR (#1875997)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Initial package for Fedora
