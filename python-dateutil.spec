%global modname dateutil

Name:           python-%{modname}
Version:        2.8.2
Release:        16%{?dist}
Epoch:          1
Summary:        Powerful extensions to the standard datetime module

# According to the LICENSE file:
# - Apache-2.0 applies to all contributions after 2017-12-01, as well as
#   all contributions that have been re-licensed.
# - BSD-3-Clause applies to all code, even that also covered by Apache-2.0
License:        (Apache-2.0 AND BSD-3-Clause) OR BSD-3-Clause

URL:            https://github.com/dateutil/dateutil
Source:         %{pypi_source}

# Remove deprecated pytest.warns(None) from test_internals.py
#
# Fixes:
# python-dateutil fails to build with pytest 7
# https://bugzilla.redhat.com/show_bug.cgi?id=2059950
Patch1:         %{url}/commit/2bdd63158b7f981fc6d70a869680451bdfd8d848.patch

# Backport the replacement for the deprecated in Python 3.12
# datetime.datetime.utcfromtimestamp()
Patch2:         %{url}/commit/f2293200747fb03d56c6c5997bfebeabe703576f.patch

# when bootstrapping dateutil-freezegun, we cannot run tests
# on RHEL, we do not have or want all test dependencies
%bcond tests %{undefined rhel}

BuildArch:      noarch
BuildRequires: make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%global _description \
The dateutil module provides powerful extensions to the standard datetime\
module available in Python.

%description %_description

%package -n python3-%{modname}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
# Runtime deps
BuildRequires:  python3-six
%if %{with tests}
BuildRequires:  python3-freezegun
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest
%endif
Requires:       tzdata
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}  %_description

%package doc
Summary: API documentation for python-dateutil
%description doc
This package contains %{summary}.

%prep
%autosetup -N
# the tests were moved outside of %%{modname} directory upstream after 2.8.2
# so we apply the patch with new paths from within it
pushd %{modname}/test
%patch -P1 -p2
popd
%patch -P2 -p2
iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS

%build
%py3_build
make -C docs html

%install
%py3_install

%check
%if %{with tests}
%{__python3} -m pytest -W ignore::pytest.PytestUnknownMarkWarning
%else
%py3_check_import dateutil dateutil.easter dateutil.parser dateutil.relativedelta dateutil.rrule dateutil.tz dateutil.utils dateutil.zoneinfo
%endif

%files -n python3-%{modname}
%license LICENSE
%doc NEWS README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/*.egg-info

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1:2.8.2-15
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:2.8.2-14
- Bootstrap for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Miro Hrončok <mhroncok@redhat.com> - 1:2.8.2-11
- Clarify the SPDX License tag

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Karolina Surma <ksurma@redhat.com> - 1:2.8.2-9
- Backport replacement for deprecated datetime.datetime.utcfromtimestamp()

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1:2.8.2-8
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1:2.8.2-7
- Bootstrap for Python 3.12

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:2.8.2-6
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:2.8.2-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:2.8.2-2
- Bootstrap for Python 3.11

* Thu Mar 10 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1:2.8.2-1
- Update to 3.8.2 (fix RHBZ#1982169)
- Backport 2bdd631: remove deprecated pytest.warns(None) (fix RHBZ#2059950)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1:2.8.1-6
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1:2.8.1-5
- Bootstrap for Python 3.10

* Wed Jun 02 2021 Petr Viktorin <pviktori@redhat.com> - 1:2.8.1-4
- Add the ASL 2.0 license

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:2.8.1-1
- 2.8.1

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1:2.8.0-10
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1:2.8.0-9
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Miro Hrončok <mhroncok@redhat.com> - 1:2.8.0-7
- Subpackage python2-dateutil has been removed
  See https://fedoraproject.org/wiki/Changes/RetirePython2

* Fri Sep 13 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.8.0-6
- Reduce Python 2 build dependencies on Fedora 32

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.8.0-5
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.8.0-4
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Petr Viktorin <pviktori@redhat.com> - 1:2.8.0-2
- Enable tests (but keep a few skipped on Python 2)
- Add explicit dependency on python3-sphinx_rtd_theme
- Remove test dependency on python2-hypothesis

* Wed Feb 06 2019 Gwyn Ciesla <limburgher@gmail.com> - 1:2.8.0-1
- 2.8.0

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1:2.7.5-1
- 2.7.5

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.7.3-1
- Update to 2.7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.7.0-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.7.0-1
- Fix license tag (should be BSD)
- Update to latest version (#1469314)
  See https://github.com/dateutil/dateutil/blob/master/NEWS for details.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1:2.6.1-2
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Nov  2 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1:2.6.1-1
- Upstream 2.6.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.6.0-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.6.0-1
- Update to 2.6.0 (RHBZ #1393159)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.5.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May  5 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.5.3-1
- Update to latest version (#1318828)

* Thu May  5 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.5.2-2
- Use separate dirs for docs for py2 and py3 subpackages (#1332623)

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 1:2.5.2-1
- Update to 2.5.2
- Adopt for new packaging guidelines

* Mon Feb 29 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 1:2.5.0-1
- Update to latest upstream version
- The patch to make dateutil.zoneinfo.gettz() use the system database is dropped.
  Upstream recommends using dateutil.tz.gettz() instead.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 1:2.4.2-3
- Rebuilt for Python3.5 rebuild
- Add BuildRequires: python3-setuptools

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr  6 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.4.2-1
- Update to latest upstream release.

* Tue Mar  3 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.4.0-3
- Add patch for string handling in dateutil.tz.tzstr (#1197791)

* Wed Jan 21 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.4.0-2
- Add python3 subpackage.
- Conflict with python-vobject <= 0.8.1c-10 (workaround until #1183377
  is fixed one way or another).

* Wed Jan 21 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.4.0-1
- Change to new upstream, update to 2.4 (#1126521)
- Build documentation.

* Tue Aug 05 2014 Jon Ciesla <limburgher@gmail.com> - 1:1.5-9
- Reverting to 1.5 pre user feedback and upstream.

* Mon Aug 04 2014 Jon Ciesla <limburgher@gmail.com> - 2.2-1
- Update to 2.2, BZ 1126521.
- Fix bad dates.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 15 2011 Jef Spaleta <jspaleta@fedoraproject.org> - 1.5-3
- Adjust patch to respect systemwide tzdata. Ref bug 729786

* Thu Sep 15 2011 Jef Spaleta <jspaleta@fedoraproject.org> - 1.5-2
- Added a patch to respect systemwide tzdata. Ref bug 729786

* Wed Jul 13 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5-1
- New upstream release
- Fix UTF8 encoding correctly
- Drop buildroot, clean, defattr and use macro for Source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 1.4.1-2
- small specfile fix

* Fri Feb 20 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 1.4.1-2
- New upstream version

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.4-3
- Rebuild for Python 2.6

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-2
- fix license tag

* Tue Jul 01 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 1.4-1
- Latest upstream release

* Fri Jan 04 2008 Jef Spaleta <jspaleta@fedoraproject.org> 1.2-2
- Fix for egg-info file creation

* Thu Jun 28 2007 Orion Poplawski <orion@cora.nwra.com> 1.2-1
- Update to 1.2

* Mon Dec 11 2006 Jef Spaleta <jspaleta@gmail.com> 1.1-5
- Fix python-devel BR, as per discussion in maintainers-list

* Mon Dec 11 2006 Jef Spaleta <jspaleta@gmail.com> 1.1-4
- Release bump for rebuild against python 2.5 in devel tree

* Wed Jul 26 2006 Orion Poplawski <orion@cora.nwra.com> 1.1-3
- Add patch to fix building on x86_64

* Wed Feb 15 2006 Orion Poplawski <orion@cora.nwra.com> 1.1-2
- Rebuild for gcc/glibc changes

* Thu Dec 22 2005 Orion Poplawski <orion@cora.nwra.com> 1.1-1
- Update to 1.1

* Thu Jul 28 2005 Orion Poplawski <orion@cora.nwra.com> 1.0-1
- Update to 1.0

* Tue Jul 05 2005 Orion Poplawski <orion@cora.nwra.com> 0.9-1
- Initial Fedora Extras package
