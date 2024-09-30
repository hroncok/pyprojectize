%global sum Simple packet creation/parsing library

Name:           python-dpkt
Version:        1.9.8
Release:        8%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/kbandla/dpkt
Source0:        https://github.com/kbandla/dpkt/archive/v%{version}.tar.gz
Patch0:         nostdeb-1.8.8.patch
Patch1:         python3-fixes-1.8.8.patch


BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest

%description
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.

%package -n python3-dpkt
Summary:        %{sum}

%description -n python3-dpkt
Fast, simple packet creation and parsing library
with definitions for the basic TCP/IP protocols.


%prep
%setup -q -n dpkt-%{version}
#%patch0 -p1
#%patch1 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dpkt

%check
# One test, "test_deprecated_decorator" fails, but doesn't appear
# to test actual functionality.
%ifarch s390x
%{__python3} -m pytest dpkt -k "not test_deprecated_decorator"
%endif


%files -n python3-dpkt -f %{pyproject_files}
%doc AUTHORS LICENSE README.md examples docs

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.8-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.9.8-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.9.8-2
- Rebuilt for Python 3.12

* Tue Jun 6 2023 Michele Baldessari <michele@acksyn.org> - 1.9.8-1
- New upstream

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Michele Baldessari <michele@acksyn.org> - 1.9.7.2-1
- New upstream
- Skip unit tests on s390x

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Michele Baldessari <michele@acksyn.org> - 1.9.4-1
- New upstream
- Add python3-setuptools BR

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-12
- Subpackage python2-dpkt has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 24 2019 Petr Viktorin <pviktori@redhat.com> - 1.9.1-11
- Run tests on Python 3
- Remove test dependencies for Python 2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-5
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-4
- Fix BuildRequires to require the tox command and not the python2 module

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 02 2017 Michele Baldessari <michele@acksyn.org> - 1.9.1-1
- New upstream release
- Build python3 packages

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Michele Baldessari <michele@acksyn.org> - 1.8.8-1
- New upstream + fix rawhide build error (BZ#1424142) for now by disabling tox

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 10 2016 Michele Baldessari <michele@acksyn.org> - 1.8.7-1
- New upstream
- New homepage
- Add check section in order to run tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Yanko Kaneti <yaneti@declera.com> - 1.8-1
- Update to 1.8. Drop patch. Drop ancient obsolete

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 28 2010 Yanko Kaneti <yaneti@declera.com> - 1.7-1
- python-dpkt previously known as dpkt
- Incorporated feedback from the new review
