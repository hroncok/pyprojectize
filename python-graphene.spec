# NOTE(jpena): The project requirements specify minimum and maximum versions
#              for all packages, so disabling the automated generation
%{?python_disable_dependency_generator}

%global pypi_name graphene

Name:           python-%{pypi_name}
Version:        3.0b6
Release:        14%{?dist}
Summary:        GraphQL Framework for Python

License:        MIT
URL:            https://github.com/graphql-python/graphene
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(coveralls) >= 1.11
BuildRequires:  python3dist(iso8601) >= 0.1
BuildRequires:  python3dist(promise) >= 2.3
BuildRequires:  python3dist(pytest) >= 5.3
BuildRequires:  python3dist(pytest-asyncio) >= 0.10
BuildRequires:  python3dist(pytest-benchmark) >= 3.2
BuildRequires:  python3dist(pytest-cov) >= 2.8
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
#NOTE(jpena): some build requirements are not available in Fedora, so we have to
#             skip unit tests
# BuildRequires:  python3dist(mock) >= 4
# BuildRequires:  python3dist(pytest-mock) >= 2
# BuildRequires:  python3dist(snapshottest) >= 0.5


%description
Graphene is a Python library for building GraphQL schemas/types fast and easily.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aniso8601) >= 8
# NOTE(jpena): upstream states >= 3.1.2, we will change this when the version is built in Rawhide
Requires:       python3dist(graphql-core) >= 3.1.1
Requires:       python3dist(graphql-relay) >= 3

%description -n python3-%{pypi_name}
Graphene is a Python library for building GraphQL schemas/types fast and easily.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.0b6-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.0b6-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Python Maint <python-maint@redhat.com> - 3.0b6-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0b6-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Javier Peña <jpena@redhat.com> - 3.0b6-1
- Update to release 3.0b6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0b4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Javier Peña <jpena@redhat.com> - 3.0b4-1
- Update to release 3.0b4

* Tue Jun 23 2020 Javier Peña <jpena@redhat.com> - 3.0b2-2
- Disable automated dependency generator

* Mon Jun 22 2020 Javier Peña <jpena@redhat.com> - 3.0b2-1
- Initial package.
