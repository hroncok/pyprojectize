%global github_name python-overpy
%global pretty_name overpy

%global _description %{expand:
overpy is a wrapper written in Python to access the Overpass API.}

Name:           python-%{pretty_name}
Version:        0.7
Release:        6%{?dist}
Summary:        Python Wrapper to access the Overpass API

# SPDX
License:        MIT
URL:            https://github.com/DinoTools/python-overpy
Source0:        %{url}/archive/%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

#for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis

#for docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)

%description -n python3-%{pretty_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{github_name}-%{version}
rm -rf %{pretty_name}.egg-info

%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst CHANGELOG.rst examples/
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%files -n python-%{pretty_name}-doc
%license LICENSE
%doc html/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.7-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 4 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7-1
- Update to 0.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.6-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-2
- Rebuilt for Python 3.10

* Sat May 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6-1
- Initial package
