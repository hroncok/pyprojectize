%global pypi_name graphql-relay

Name:           python-%{pypi_name}
Version:        3.2.0
Release:        9%{?dist}
Summary:        Relay library for Graphql

License:        MIT
URL:            https://github.com/graphql-python/graphql-relay-py
Source0:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
GraphQL-relay is the Relay library for GraphQL-core implemented in Python.
It allows the easy creation of Relay-compliant servers using GraphQL-core.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-graphql-core
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(graphql-core)
%description -n python3-%{pypi_name}
GraphQL-relay is the Relay library for GraphQL-core implemented in Python.
It allows the easy creation of Relay-compliant servers using GraphQL-core.

%prep
%autosetup -n %{pypi_name}-py-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

#%%check
#%%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/graphql_relay/
%{python3_sitelib}/graphql_relay-%{version}.dist-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.0-8
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Fabian Affolter <mail@fabian-affolter.ch> - 3.2.0-1
- Update to latest upstream release 3.2.0 (closes rhbz#2043703)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.10

* Fri Feb 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to latest upstream release 3.1.0 (#1933192)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-3
- Add missing BRs

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-2
- Remove requirement (rhbz#1836568)

* Thu May 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Initial package for Fedora
