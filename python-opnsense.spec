%global pypi_name pyopnsense
%global pkg_name opnsense

Name:           python-%{pkg_name}
Version:        0.3.0
Release:        15%{?dist}
Summary:        Python API client for OPNsense

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/mtreinish/pyopnsense
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python API client for the OPNsense API. This module provides a Python
interface for interacting with the OPNsense API.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(stestr)

%description -n python3-%{pkg_name}
A Python API client for the OPNsense API. This module provides a Python
interface for interacting with the OPNsense API.

%package -n python-%{pkg_name}-doc
Summary:        pyopnsense documentation

BuildRequires:  python3dist(sphinx)
%description -n python-%{pkg_name}-doc
Documentation for pyopnsense.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v pyopnsense/tests

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.3.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.3.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.3.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Update to latest upstream release 0.3.0

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora