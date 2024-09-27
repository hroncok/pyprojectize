%global pypi_name graphql-core

Name:           python-%{pypi_name}
Version:        3.2.4
Release:        1%{?dist}
Summary:        GraphQL implementation for Python

License:        MIT
URL:            https://github.com/graphql-python/graphql-core
Source0:        %{pypi_source}
BuildArch:      noarch

%description
GraphQL-core-3 is a Python port of GraphQL.js, the JavaScript reference
implementation for GraphQL, a query language for APIs.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-benchmark
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
GraphQL-core-3 is a Python port of GraphQL.js, the JavaScript reference
implementation for GraphQL, a query language for APIs.

%package -n python-%{pypi_name}-doc
Summary:       Documentation for %{name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for graphql-core.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# Not docs because of https://bugzilla.redhat.com/show_bug.cgi?id=1900509
#PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 docs html
#rm -rf html/.{doctrees,buildinfo}

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/graphql/
%{python3_sitelib}/graphql_core-%{version}.dist-info

%files -n python-%{pypi_name}-doc
#%%doc html
%license LICENSE

%changelog
* Fri Sep 13 2024 Sandro <devel@penguinpee.nl> - 3.2.4-1
- Update to 3.2.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.3-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.2.3-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Fabian Affolter <mail@fabian-affolter.ch> - 3.2.3-1
- Update to latest upstream release 3.2.3

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.6-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.6-1
- Update to latest upstream release 3.1.6 (closes rhbz#1947481)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.3-2
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.3-1
- Update to latest upstream release 3.1.3 (#1926445)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.2-1
- Update to latest upstream release 3.1.2 (#1893531)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.1-1
- Generate docs in install (#1836567)
- Update BR name
- Update to latest upstream release 3.1.1

* Thu May 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Initial package for Fedora
