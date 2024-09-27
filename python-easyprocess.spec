%global pypi_name EasyProcess
%global dist_name %{py_dist_name %{pypi_name}}

Name:           python-%{dist_name}
Version:        1.1
Release:        4%{?dist}
Summary:        Easy to use Python subprocess interface

License:        BSD-2-Clause
URL:            https://github.com/ponty/EasyProcess
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For Tests
BuildRequires:  iputils
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-timeout}
BuildRequires:  %{py3_dist six}

%global _description %{expand:
EasyProcess is an easy to use python subprocess interface.}

%description %_description

%package -n     python3-%{dist_name}
Summary:        %{summary}

Requires:       %{py3_dist py}
%description -n python3-%{dist_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Avoid circular dependency with PyVirtualDisplay
rm -f tests/test_fast/test_deadlock.py

%build
%py3_build

%install
%py3_install

%check
%pytest


%files -n python3-%{dist_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{dist_name}/

%changelog
* Thu Aug 01 2024 Scott Talbert <swt@techie.net> - 1.1-4
- Update License tag to use SPDX identifiers

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-2
- Rebuilt for Python 3.13

* Tue May 28 2024 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1-1
- Update to 1.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.3-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3-2
- Rebuilt for Python 3.10

* Sat Feb 13 2021 Scott Talbert <swt@techie.net> - 0.3-1
- Initial package
