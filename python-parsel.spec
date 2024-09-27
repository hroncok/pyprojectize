%{?python_enable_dependency_generator}

%global modname parsel

Name:           python-%{modname}
Version:        1.7.0
Release:        9%{?dist}
Summary:        Library to extract data from HTML and XML using XPath and CSS selectors

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/scrapy/parsel
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-w3lib >= 1.8.0
BuildRequires:  python3-lxml >= 2.3
BuildRequires:  python3-six >= 1.5.2
BuildRequires:  python3-cssselect >= 0.9
BuildRequires:  python3-sybil
BuildRequires:  python3-psutil

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py ptr

%files -n python3-%{modname}
%license LICENSE
%doc README.rst NEWS
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.0-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.7.0-1
- Update to 1.7.0 rhbz#1742642
- Fix changelog for 1.6.0

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.0-1
- Update to 1.6.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.0-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Petr Viktorin <pviktori@redhat.com> - 1.5.0-3
- Remove the Python 2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1654012

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Tue Oct 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-1
- Initial package
