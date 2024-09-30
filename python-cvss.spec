%global srcname cvss

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_without python2
%bcond_with python3
%else
%bcond_with python2
%bcond_without python3
%endif

Name:           python-%{srcname}
Version:        2.5
Release:        9%{?dist}
Summary:        CVSS2/3 library with interactive calculator

License:        LGPL-3.0-or-later
URL:            https://github.com/skontar/cvss
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This Python package contains CVSS v2 and v3 computation utilities and\
interactive calculator.

%description %{_description}

# Python 2 Package
# (RHEL Only)
%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
%if 0%{?rhel} == 6
Requires:       python-ordereddict
%endif
%else
BuildRequires:  python2-setuptools
%endif

%description -n python2-%{srcname} %{_description}

Python 2 version.
%endif
# end with python2

# Python 3 Package
%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.
%endif
# end with python3

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%pyproject_wheel
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%pyproject_install
%endif

# Tests are not ran (have to patch code and use nose/pytest)
#check

%if %{with python2}
%files -n python2-%{srcname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{srcname}-*.dist-info/
%{python2_sitelib}/%{srcname}/
%endif

%if %{with python3}
%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/
%endif

%{_bindir}/cvss_calculator

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-8
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.5-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.5-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Viliam Krizan <vkrizan@redhat.com> - 2.5-1
- Update to 2.5 (#2111103)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Viliam Krizan <vkrizan@redhat.com> - 2.4-1
- New release 2.3 (#2087588)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 2.3-2
- Rebuilt for Python 3.10

* Mon Jun 07 2021 Viliam Krizan <vkrizan@redhat.com> - 2.3-1
- New release 2.3 (#1966866)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2-2
- Rebuilt for Python 3.10

* Fri Feb 19 2021 Viliam Krizan <vkrizan@redhat.com> - 2.2-1
- New release 2.2 (#1913945)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-2
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Viliam Krizan <vkrizan@redhat.com> - 2.1-1
- New release 2.1 (#1793040)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Viliam Krizan <vkrizan@redhat.com> - 2.0-1
- New release 2.0 with CVSSv3.1 support (rhbz#1747163)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Viliam Krizan <vkrizan@redhat.com> - 1.10-1
- New release 1.10

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Viliam Krizan <vkrizan@redhat.com> - 1.9-2
- Removal of deprecated python2-cvss package for Fedora,
  as part of https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
  (RHBZ #1628566)

* Mon Aug 06 2018 Viliam Krizan <vkrizan@redhat.com> - 1.9-1
- New release 1.9
- The CVSS vector parser from an arbitrary text was added.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-2
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Viliam Krizan <vkrizan@redhat.com> - 1.8-1
- New release 1.8 (RHBZ #1594561)
- Convenience improvements for testing and interactive calculator
- Improved handling of empty fields

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 pjp <pjp@fedoraproject.org> - 1.7-1
- New release 1.7 (RHBZ #1412158)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6-2
- Rebuild for Python 3.6

* Fri Dec 09 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.6-1
- Update to 1.6 (RHBZ #1402174)

* Fri Nov 04 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.5-1
- Update to 1.5

* Thu Sep 08 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.4-2
- Fixes in packaging

* Wed Aug 31 2016 pjp <pjp@fedoraproject.org> - 1.4-1
- New release v1.4.
- License changed to LGPLv3+

* Fri Aug 26 2016 pjp <pjp@fedoraproject.org> - 1.3-2
- Separate sections for Fedora and EPEL builds

* Wed Aug 24 2016 pjp <pjp@fedoraproject.org> - 1.3-1
- Update to new release.

* Wed Aug 17 2016 pjp <pjp@fedoraproject.org> - 1.2-4
- Updated Source0 URL BZ#1334611#c6.

* Wed Aug 17 2016 pjp <pjp@fedoraproject.org> - 1.2-3
- Added BuildRequires and summary macro as per BZ#1334611#c4.

* Wed Aug 17 2016 pjp <pjp@fedoraproject.org> - 1.2-2
- Separated Python v2 and v3 builds in respective packages as
  suggested in BZ#1334611#c1.

* Tue May 10 2016 pjp <pjp@fedoraproject.org> - 1.2-1
- Initial build of Python cvss package.
