%global srcname bowler

%bcond_without tests

Name:           python-%{srcname}
Version:        0.9.0
Release:        14%{?dist}
Summary:        Safe code refactoring for modern Python projects
License:        MIT
URL:            https://pybowler.io
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  %{py3_dist attrs}
BuildRequires:  %{py3_dist click}
BuildRequires:  %{py3_dist coverage}
BuildRequires:  %{py3_dist fissix}
BuildRequires:  %{py3_dist moreorless} >= 0.2.0
BuildRequires:  %{py3_dist volatile}
%endif


%global _description %{expand:
Bowler is a refactoring tool for manipulating Python at the syntax tree level.
It enables safe, large scale code modifications while guaranteeing that the
resulting code compiles and runs. It provides both a simple command line
interface and a fluent API in Python for generating complex code modifications
in code.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%package -n python3-%{srcname}-docs
Summary:        Documentation for python3-%{srcname}
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-docs %_description

The python3-%{srcname}-docs package contains documentation for python3-%{srcname}.


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i '1d' $(grep -l '#!/usr/bin/env' bowler/*.py)
# this is only needed for testing
sed -i '/volatile/d' requirements.txt


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%{python3} -m coverage run -m bowler.tests
%endif


%files -n  python3-%{srcname}
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}/
%exclude %{python3_sitelib}/%{srcname}/tests
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n python3-%{srcname}-docs
%doc docs/*.md


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 0.9.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-1
- Initial package
