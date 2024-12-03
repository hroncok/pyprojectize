Name: python-beaker
Version: 1.12.1
Release: 8%{?dist}
Summary: WSGI middleware layer to provide sessions
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://beaker.readthedocs.io
Source0: https://github.com/bbangert/beaker/archive/%{version}/beaker-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  %{_bindir}/redis-server
BuildRequires:  %{_bindir}/netstat

%global _description\
Beaker is a caching library that includes Session and Cache objects built on\
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to\
manage Session objects and signed cookies.

Patch:          beaker-use-system-paste.patch
Patch:          unittest.mock.patch
# https://github.com/bbangert/beaker/issues/242
# https://github.com/bbangert/beaker/pull/243
# Avoid the new dbm.sqlite3 backend to fix tests
Patch:          0001-Avoid-using-dbm.sqlite3-242.patch

%description %_description

%package -n python3-beaker
Summary: %summary
BuildRequires: python3-devel
BuildRequires: python3dist(cryptography)
BuildRequires: python3dist(funcsigs)
BuildRequires: python3dist(paste)
BuildRequires: python3dist(pycrypto)
BuildRequires: python3dist(redis)
BuildRequires: python3dist(sqlalchemy)
BuildRequires: python3dist(webtest)
# for tests
BuildRequires: python3dist(pytest)
BuildRequires: glibc-langpack-it

Requires: python3dist(paste)
Recommends: python3dist(cryptography)
Recommends: python3dist(pycrypto)
Recommends: python3dist(pycryptodome)
Recommends: python3dist(pycryptopp)


%description -n python3-beaker %_description


%prep
%autosetup -p1 -n beaker-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l 'Beaker*' beaker


%check
%pyproject_check_import

# we can't test mongo
rm -f tests/test_managers/test_ext_mongodb.py

redis-server &

%pytest

%files -n python3-beaker -f %{pyproject_files}
%doc README.rst CHANGELOG


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12.1-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Adam Williamson <awilliam@redhat.com> - 1.12.1-6
- Backport PR #243 to fix build with Python 3.13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.12.1-2
- Rebuilt for Python 3.12

* Tue May 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.12.1-1
- Update to 1.12.1 rhbz#1679788

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.10.0-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-3
- Remove python2-beaker

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-1
- Update to 1.10.0 (#860617)
- Rebuilt for Python 3.7 (#1605613)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.4-21
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 1.5.4-19
- Cleanup spec file conditionals

* Wed Aug 09 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
- Python 2 binary package renamed to python2-
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.4-15
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-14
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.5.4-6
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.5.4-5
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 09 2012 Luke Macken <lmacken@redhat.com> - 1.5.4-3
- Remove the python3-paste dependency.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 6 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4
- Fix for python3 module and anydbm
- Tried enabling unittests on python3 -- still no joy

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 27 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.3-8
- Remove explicit call to 2to3; setup.py handles this

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.5.3-7
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Thu Aug 12 2010 Kyle VanderBeek <kylev@kylev.com> - 1.5.3-6
- Disable broken test_dbm_container2 test.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 28 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.3-4
- Add Requires for crypto libs so we have encrypted cookies
- Add patch to unbundle file that comes from paste

* Sun Jun 27 2010 Kyle VanderBeek <kylev@kylev.com> - 1.5.3-3
- Add python3 conditionals

* Thu May 06 2010 Luke Macken <lmacken@redhat.com> - 1.5.3-2
- Add a python3 subpackage

* Mon Mar 22 2010 Luke Macken <lmacken@redhat.com> - 1.5.3-1
- Update to 1.5.3
- Remove the abspath patch, which was fixed upstream
- Run the test suite

* Fri Jan 22 2010 Luke Macken <lmacken@redhat.com> - 1.5.1-1
- Update to 1.5.1
- Remove beaker-hmac2.4.patch, which made it into 1.4 upstream
- Remove middleware-config.patch which is also upstream

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Kyle VanderBeek <kylev@kylev.com> - 1.3.1-5
- Add patch based on upstream hg 403ef7c82d32 for config overwriting that
  breaks Pylons unit tests

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-4
- Add a patch to remove the use of __future__.absolute_import in the google
  backend

* Sat Jun 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-3
- Different hmac patch suitable for upstream inclusion.

* Tue Jun 02 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-2
- Add a patch to remove Beaker's use of hashlib on Python2.4,
  due to incompatiblities with Python's hmac module (#503772)

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Tue Apr 07 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3-1
- Update to 1.3
 
* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.3-1
- Update to 1.2.3
 
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Sat Dec 20 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.1.2-1
- Update to 1.1.2
 
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.3-2
- Rebuild for Python 2.6

* Tue Jun 24 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.0.3-1
- Update to 1.0.3.

* Tue Jun 24 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.5-1
- Update to 0.9.5.
- Remove license patch which is now corrected upstream.

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-4
- Fix files to not use wildcard, fixing dir ownership

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-3
- Corrected license

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-2
- More restrictive file includes for safety

* Sun May 11 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-1
- Update to 0.9.4 (security fix)
- Fix rpmlint complaints, add CHANGELOG and LICENSE

* Wed Apr  9 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.3-1
- Initial version.
