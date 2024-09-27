Name:           pyhunspell
Version:        0.5.5
Release:        8%{?dist}
Summary:        Python bindings for hunspell

License:        LGPL-3.0-or-later
URL:            https://github.com/blatinier/pyhunspell
Source0:        https://github.com/blatinier/pyhunspell/archive/pyhunspell-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# make it build with hunspell-1.7:
Patch0: pyhunspell-fix-build.patch

%global _description\
These are python bindings for hunspell, that allow to use the hunspell library\
in python.

%description %_description

%package -n python3-pyhunspell
Summary: %summary
%{?python_provide:%python_provide python3-pyhunspell}

%description -n python3-pyhunspell
This package contains a Python3 module to use the hunspell library
from Python3.

%prep
%setup -q -n pyhunspell-%{version}
%patch -P0 -p1 -b .hunspell13

%build
%py3_build

%install
%py3_install

%files -n python3-pyhunspell
%doc AUTHORS.md CHANGELOG.md COPYING COPYING.LESSER gpl-3.0.txt lgpl-3.0.txt PKG-INFO README.md
%{python3_sitearch}/*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.5-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.5-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Mike FABIAN <mfabian@redhat.com> - 0.5.5-1
- Update to 0.5.5
- Migrate license tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.4-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.4-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Mike FABIAN <mfabian@redhat.com> - 0.5.4-6
- Remove python2 subpackage from Fedora 30+: remove python2-pyhunspell
- Resolves: rhbz#1634647

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 0.5.4-5
- rebuild for hunspell 1.7.0

* Mon Jul 23 2018 Mike FABIAN <mfabian@redhat.com> - 0.5.4-4
- Fix build in Fedora rawhide
- Resolves: rhbz#1605551

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-2
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Mike FABIAN <mfabian@redhat.com> - 0.5.4-1
- update to 0.5.4

* Tue Mar  6 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-5
- Drop Requires/Provides/Obsoletes pyhunspell from the python3 subpackage
- Rename python3 subpackage to python3-pyhunspell

* Tue Mar 06 2018 Mike FABIAN <mfabian@redhat.com> - 0.5.0-4
- Apply fix for encoding problem from upstream.
  (See: https://github.com/blatinier/pyhunspell/issues/32)
- Provide “pyhunspell” also from the pyhunspell-python3 package, otherwise
  one cannot install pyhunspell-python3 because there is no “pyhunspell” package
  anymore.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> - 0.5.0-2
- rebuild for hunspell 1.6.2

* Fri Sep 01 2017 Mike FABIAN <mfabian@redhat.com> - 0.5.0-1
- update to 0.5.0

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-10
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-9
- Python 2 binary package renamed to python2-pyhunspell
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuild for Python 3.6

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.4.1-4
- Rebuild for hunspell 1.5.x

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 18 2016 Caolán McNamara <caolanm@redhat.com> - 0.4.1-2
- rebuild for hunspell 1.4.0

* Mon Apr 04 2016 Mike FABIAN <mfabian@redhat.com> - 0.4.1-1
- update to 0.4.1

* Mon Mar 21 2016 Mike FABIAN <mfabian@redhat.com> - 0.4.0-1
- update to 0.4.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 Mike FABIAN <mfabian@redhat.com> - 0.3.3-1
- update to 0.3.3
- remove patch for the leaks found with the gcc-with-cpychecker
  static analyzer, it is included upstream
- add a python3 sub-package
- Resolves: rhbz#800116

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Mike FABIAN <mfabian@redhat.com> - 0.1-9
- Resolves: #800116 - Bugs found in pyhunspell-0.1-6.fc17 using gcc-with-cpychecker static analyzer 

* Wed Jan 09 2013 Till Maas <opensource@till.name> - 0.1-8
- python site_arch macro is not needed now, remove it
- remove buildroot tag
- Add comment/bz reference for patch
- removal of buildroot in %%install
- remove %%clean section
- remove defattr(-,root,root,-)
- Add PKG-INFO to %%doc
- BuildRequires should be python2-devel and not just python-devel

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 25 2011 Caolán McNamara <caolanm@redhat.com> - 0.1-5
- rebuild for new hunspell

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Aug 25 2009 Till Maas <opensource@till.name> - 0.1-2
- Remove CFLAGS, whiche are used automagically
- Change the %%description to a full sentence
- Adjust the license tag, it's actually LGPLv3+

* Wed Jul 29 2009 Till Maas <opensource@till.name> - 0.1-1
- Initial spec for Fedora
