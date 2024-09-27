%global srcname pystatgrab

Name:           pystatgrab
Version:        0.7.3
Release:        2%{?dist}
Summary:        Python bindings for libstatgrab

License:        LGPL-2.0-or-later
URL:            https://libstatgrab.org/pystatgrab/
Source0:        https://github.com/libstatgrab/pystatgrab/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libstatgrab-devel > 0.91

%description
Pystatgrab contains Python bindings for libstatgrab.

%package -n python3-%{name}
Summary:        %{summary}

BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Pystatgrab contains Python bindings for libstatgrab.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
rm -rf statgrab.c
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}/%{python3_sitearch} %{__python3} test.py

%files -n python3-%{name}
%doc AUTHORS NEWS README
%license COPYING.LGPL
%{python3_sitearch}/*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Jonathan Wright <jonathan@almalinux.org> - 0.7.3-1
- update to 0.7.3 rhbz#2284643

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jonathan Wright <jonathan@almalinux.org> - 0.7.2-1
- Update to 0.7.2 rhbz#2255754
- Update URL
- Update Source

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.1-10
- Rebuilt for Python 3.12

* Sat Feb 25 2023 Tim Orling <ticotimo@gmail.com> - 0.7.1-9
  - Add patch for deprecated distuls (rhbz 2154875)
  - https://github.com/libstatgrab/pystatgrab/pull/7
  - minimum libstatgrab is 0.91
  - BR python3-setuptools
  - drop .rpmlint (unused filters)
  - migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Update to latest upstream release 0.7.1 (rhbz#1869110)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7-18
- Remove Python 2 subpackage (rhbz#1746756)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Tim Orling <ticotimo@gmail.com> - 0.7-15
- Fix build for rawhide and python 3.8 (rhbz#1716485) 

* Sat Mar 23 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7-14
- Fix ownership (rhbz#1672099)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Tim Orling <ticotimo@gmail.com> - 0.7-11
- Remove bundled statgrab.c so cython will generate it
- Drop unnecessary Provides/Obsoletes

* Fri Jul 06 2018 Tim Orling <ticotimo@gmail.com> - 0.7-10
- Add python[2,3]-Cython to BuildRequires
- Remove bundled statgrab.c before python3 build
- Fixes FTBFS on python3.7 (changes in tstate API)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7-9
- Rebuilt for Python 3.7

* Sat Feb 24 2018 Tim Orling <ticotimo@gmail.com> - 0.7-8
- Add gcc to BuildRequires
- Use https for Source0
- Add rpmlint filters for spelling errors

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 13 2016 Tim Orling <ticotimo@gmail.com> - 0.7-1
- Upstream bump to 0.7 for python3 fixes
- Drop merged patch

* Sun Mar 27 2016 Tim Orling <ticotimo@gmail.com> - 0.6-2
- Add patch to fix pkg-config bytes to string exception
- whitespace cleanup

* Fri Mar 25 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- Update for py3
- Update to latest upstream release 0.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 16 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-13
- Spec file update
- Rebuild against libstatgrab 0.90

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5-4
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5-3
- Rebuild for Python 2.6

* Sun Sep 28 2008 Soumya Chakraborty <soumya@fedoraproject.org> 0.5-2
- Changed from the noarch package to sitearch package and changed the name from python-statgrab to pystatgrab.

* Wed Aug 13 2008 Soumya Chakraborty <soumya@fedoraproject.org> 0.5-1
- Initial Package Release
