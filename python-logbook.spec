Name:		python-logbook
Version:	1.7.0
Release:	6%{?dist}
Summary:	A logging replacement for Python

License:	BSD-3-Clause
URL:		https://logbook.readthedocs.io
Source0:	https://github.com/getlogbook/logbook/archive/%{version}.tar.gz#/Logbook-%{version}.tar.gz

%description
Logbook is a logging system for Python that replaces the standard library's
logging module. It was designed with both complex and simple applications
and mind and the idea to make logging fun. What makes it fun? What about
getting log messages on your phone or desktop notification system?
Logbook can do that.

%package -n python3-logbook
Summary:	%{summary}

BuildRequires:  gcc
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-sqlalchemy
BuildRequires:	python3-redis
BuildRequires:	python3-zmq
BuildRequires:	python3-brotli
BuildRequires:  python3-Cython

%description -n python3-logbook
Logbook is a logging system for Python that replaces the standard library's
logging module. It was designed with both complex and simple applications
and mind and the idea to make logging fun. What makes it fun? What about
getting log messages on your phone or desktop notification system?
Logbook can do that.

%prep
%autosetup -n logbook-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files logbook

%check
%pytest -k "not test_redis_handler"

%files -n python3-logbook -f %{pyproject_files}
%doc CHANGES README.md
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.7.0-5
- Rebuilt for Python 3.13

* Mon Mar 25 2024 Nils Philippsen <nils@tiptoe.de> - 1.7.0-4
- Reenable performing (most) tests

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.7.0-1
- 1.7.0

* Mon Jul 31 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-1
- 1.6.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.5.3-14
- Rebuilt for Python 3.12

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.3-13
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.5.3-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.3-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-4
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.3-3
- BR gcc.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.5.3-1
- 1.5.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-2
- Rebuilt for Python 3.8

* Wed Aug 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-1
- 1.5.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.3-2
- Fix build failure for Python 3.8 (rhbz#1716506)

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.4.3-1
- 1.4.3

* Thu Oct 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.4.0-1
- Drop python2, 1.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-11
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-10
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-7
- Python 2 binary package renamed to python2-logbook
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuild for Python 3.6

* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 1.0.0-1
- 1.0.0.
- Disabled tests.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Jon Ciesla <limburgher@gmail.com> - 0.11.3-1
- Latest upstream.
- Fix Python 3 build.
- Moved from noarch to arched.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Jon Ciesla <limburgher@gmail.com> - 0.7.0-1
- Latest upstream, BZ 1148946.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Nov 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-1
- Latest upstream.
- Re-enable Python 3, 1028774.

* Fri Sep 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.5.0-1
- Latest upstream.
- Switched to noarch.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.1-1
- Latest upstream, BZ 904886.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Jon Ciesla <limb@jcomserv.net> - 0.3-3
- Dropped test suite from Python 3 package.
- Testing via setuptools.
- Filtered .so in Python 3 package.
- Dropped Python 3 subpackage, see comments.
- Added python-jinja2 BR.

* Wed Oct 26 2011 Jon Ciesla <limb@jcomserv.net> - 0.3-2
- Ownership and macro fixes.
- Dropped spurious Requires.
- Added test suite to check, dropped from package.

* Tue Oct 11 2011 Jon Ciesla <limb@jcomserv.net> - 0.3-1
- Initial RPM release
