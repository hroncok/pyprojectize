%global pypi_name mongomock

Name:           python-%{pypi_name}
Version:        4.1.2
Release:        1%{?dist}
Summary:        Module for testing MongoDB-dependent code

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mongomock/mongomock
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Mongomock is a small library to help testing Python code that interacts
with MongoDB via Pymongo.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(sentinels)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
Mongomock is a small library to help testing Python code that interacts
with MongoDB via Pymongo.

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
%pytest -v tests -k "not BulkOperationsWithPymongoTest and not CollectionComparisonTest \
  and not MongoClientCollectionTest and not MongoClientSortSkipLimitTest \
  and not test__insert_do_not_modify_input"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Sep 17 2024 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.2-1
- Update to new upstream version (closes rhbz#2196806)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.20.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.20.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.20.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.20.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.20.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.20.0-1
- Initial package for Fedora
