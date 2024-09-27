%global commit c2f5d130c91b1696385a6ae0b5bcfd5214bcc9ca
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: tre
Version: 0.8.0
Release: 46.20140228git%{shortcommit}%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source0: https://github.com/laurikari/tre/archive/%{commit}/tre-%{commit}.tar.gz
# based on https://github.com/laurikari/tre/pull/19
Patch0: %{name}-chicken.patch
# make internal tests of agrep work with just-built shared library
Patch1: %{name}-tests.patch
# don't force build-time LDFLAGS into tre.pc
Patch2: %{name}-ldflags.patch
# CVE-2016-8859, based on http://seclists.org/oss-sec/2016/q4/att-183/0001-fix-missing-integer-overflow-checks-in-regexec-buffe.patch
Patch3: %{name}-CVE-2016-8859.patch
# last hunk from the patch from https://github.com/laurikari/tre/issues/37
Patch4: %{name}-issue37.patch
# https://github.com/laurikari/tre/issues/50
# https://github.com/wch/r-source/commit/55f210ad56828ba2c63ccf027cb64e95adde7119
Patch5: %{name}-issue50.patch
# based on https://github.com/laurikari/tre/pull/49
Patch10: %{name}-python3.patch
# Remove broken agrep test entry (fails with bash >= 5.2)
Patch11: https://github.com/laurikari/tre/pull/87.patch
# Deprecated PyUnicode APIs
Patch12: %{name}-pep623.patch
Summary: POSIX compatible regexp library with approximate matching
URL: http://laurikari.net/tre/
# rebuild autotools for bug #926655
BuildRequires: make
BuildRequires: gettext-devel
# required for tests
BuildRequires: glibc-langpack-en
BuildRequires: libtool
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: %{name}-common = %{version}-%{release}

%description
TRE is a lightweight, robust, and efficient POSIX compatible regexp
matching library with some exciting features such as approximate
matching.

%package common
Summary: Cross-platform files for use with the tre package
BuildArch: noarch

%description common
This package contains platform-agnostic files used by the TRE
library.

%package devel
Requires: tre = %{version}-%{release}
Summary: Development files for use with the tre package

%description devel
This package contains header files and static libraries for use when
building applications which use the TRE library.

%package -n python3-%{name}
Summary: Python bindings for the tre library
%{?python_provide:%python_provide python3-tre}

%description -n python3-%{name}
This package contains the python bindings for the TRE library.

%package -n agrep
Summary: Approximate grep utility

%description -n agrep
The agrep tool is similar to the commonly used grep utility, but agrep
can be used to search for approximate matches.

The agrep tool searches text input for lines (or records separated by
strings matching arbitrary regexps) that contain an approximate, or
fuzzy, match to a specified regexp, and prints the matching lines.
Limits can be set on how many errors of each kind are allowed, or
only the best matching lines can be output.

Unlike other agrep implementations, TRE agrep allows full POSIX
regexps of any length, any number of errors, and non-uniform costs.

%prep
%setup -q -n tre-%{commit}
%patch -P0 -p1 -b .chicken
%patch -P1 -p1 -b .tests
%patch -P2 -p1 -b .ldflags
%patch -P3 -p1 -b .CVE-2016-8859
%patch -P4 -p1 -b .issue37
%patch -P5 -p1 -b .issue50
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1 -b .pep623
# rebuild autotools for bug #926655
touch ChangeLog
autoreconf -vif

%build
%configure --disable-static --disable-rpath
%make_build
pushd python
%py3_build
popd

%install
%make_install
pushd python
%py3_install
popd
rm $RPM_BUILD_ROOT%{_libdir}/*.la
%find_lang %{name}

%check
%{__make} check

%ldconfig_scriptlets

%files
%{_libdir}/libtre.so.*

%files common -f %{name}.lang
%license LICENSE
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/*.html doc/*.css

%files devel
%{_libdir}/libtre.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files -n python3-%{name}
%attr(0755,root,root) %{python3_sitearch}/tre%{python3_ext_suffix}
%{python3_sitearch}/tre-%{version}-py%{python3_version}.egg-info

%files -n agrep
%{_bindir}/agrep
%{_mandir}/man1/agrep.1*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-46.20140228gitc2f5d13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-45.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.0-44.20140228gitc2f5d13
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-43.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Dominik Mierzejewski <dominik@greysector.net> 0.8.0-42.20140228gitc2f5d13
- Fix deprecated PyUnicode API usage (PEP-623)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-41.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.0-40.20140228gitc2f5d13
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-39.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Dominik Mierzejewski <dominik@greysector.net> 0.8.0-38.20140228gitc2f5d13
- remove broken agrep test entry (fails with bash >= 5.2) (https://github.com/laurikari/tre/pull/87)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-37.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-36.20140228gitc2f5d13
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-35.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-34.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-33.20140228gitc2f5d13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-32.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-31.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-30.20140228gitc2f5d13
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-29.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-28.20140228gitc2f5d13
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Orion Poplawski <orion@nwra.com> - 0.8.0-27.20140228gitc2f5d13
- Use newer make macro, %%license

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-26.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-25.20140228gitc2f5d13
- improve python bindings build patch based on upstream PR
- fix infinite loop for certain regexps (upstream issue #50)
- switch to python3 (#1634955)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-24.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-23.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-22.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-21.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-20.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-19.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-18.20140228gitc2f5d13
- fix CVE-2016-8859 (#1387112, #1387113)
- probably fix CVE-2015-3796 (see upstream issue #37 and
  https://bugs.chromium.org/p/project-zero/issues/detail?id=428)
- update python bindings subpackage to current guidelines
- fix parallel installation of multilib packages (patch by joseba.gar at gmail.com)
  (bug #1275830)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-17.20140228gitc2f5d13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-16.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-15.20140228gitc2f5d13
- keep old timestamps embedded in .mo files (bug #1275830)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-14.20140228gitc2f5d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-13.20140228gitc2f5d13
- update to latest snapshot from github
- drop patches merged upstream
- fix broken LDFLAGS in tre.pc (#1224203)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-10
- fix build on aarch64 (bug #926655)
- drop obsolete specfile parts
- fix deprecated python macro usage

* Tue Feb  4 2014 Tom Callaway <spot@fedoraproject.org> - 0.8.0-9
- add missing changes from R to be able to use tre in R as system lib (and resolve arm fails)
  Credit to Orion Poplawski.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for glibc bug#747377

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Sep 20 2009 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-1
- updated to 0.8.0 (ABI change)

* Sat Aug 22 2009 Dominik Mierzejewski <rpm@greysector.net> 0.7.6-2
- added missing defattr for python subpackage
- dropped conditionals for Fedora <10
- used alternative method for rpath removal
- fixed internal testsuite to run with just-built shared library
- dropped unnecessary build dependencies

* Tue Jul 28 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.7.6-1
- new version 0.7.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.7.5-6
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.5-5
- Autorebuild for GCC 4.3

* Tue Jan 01 2008 Dominik Mierzejewski <rpm@greysector.net> 0.7.5-4
- fix build in rawhide (include python egg-info file)

* Wed Oct 31 2007 Dominik Mierzejewski <rpm@greysector.net> 0.7.5-3
- include python bindings (bug #355241)
- fix chicken-and-egg problem when building python bindings

* Wed Aug 29 2007 Dominik Mierzejewski <rpm@greysector.net> 0.7.5-2
- rebuild for BuildID
- update license tag

* Mon Jan 29 2007 Dominik Mierzejewski <rpm@greysector.net> 0.7.5-1
- update to 0.7.5
- remove redundant BRs
- add %%check

* Thu Sep 14 2006 Dominik Mierzejewski <rpm@greysector.net> 0.7.4-6
- remove ExcludeArch, the bug is in crm114

* Tue Aug 29 2006 Dominik Mierzejewski <rpm@greysector.net> 0.7.4-5
- mass rebuild

* Fri Aug 04 2006 Dominik Mierzejewski <rpm@greysector.net> 0.7.4-4
- bump release to fix CVS tag

* Thu Aug 03 2006 Dominik Mierzejewski <rpm@greysector.net> 0.7.4-3
- per FE guidelines, ExcludeArch only those problematic arches

* Wed Aug 02 2006 Dominik Mierzejewski <rpm@greysector.net> 0.7.4-2
- fixed rpmlint warnings
- ExclusiveArch: %%{ix86} until amd64 crash is fixed and somebody
  tests ppc(32)

* Wed Jul 26 2006 Dominik Mierzejewski <rpm@greysector.net> 0.7.4-1
- 0.7.4
- disable evil rpath
- added necessary BRs
- license changed to LGPL

* Sun Feb 19 2006 Dominik Mierzejewski <rpm@greysector.net> 0.7.2-1
- \E bug patch
- FE compliance

* Sun Nov 21 2004 Ville Laurikari <vl@iki.fi>
- added agrep man page

* Sun Mar 21 2004 Ville Laurikari <vl@iki.fi>
- added %%doc doc

* Wed Feb 25 2004 Ville Laurikari <vl@iki.fi>
- removed the .la file from devel package

* Mon Dec 22 2003 Ville Laurikari <vl@iki.fi>
- added %%post/%%postun ldconfig scriplets.

* Fri Oct 03 2003 Ville Laurikari <vl@iki.fi>
- included in the TRE source tree as `tre.spec.in'.

* Tue Sep 30 2003 Matthew Berg <mberg@synacor.com>
- tagged release 1
- initial build
