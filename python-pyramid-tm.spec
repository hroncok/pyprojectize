%global modname pyramid_tm
%global sum A package which allows Pyramid requests to join the active transaction
%global desc pyramid_tm is a package which allows Pyramid requests to join the\
active transaction as provided by the transaction\
http://pypi.python.org/pypi/transaction\
\
See http://docs.pylonsproject.org/projects/pyramid_tm/dev/\
or docs/index.rst in this distribution for detailed documentation.


Name:           python-pyramid-tm
Version:        2.5
Release:        12%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/pyramid_tm
Source0:        https://github.com/Pylons/pyramid_tm/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch


BuildRequires:  python3-devel
BuildRequires:  python3-pyramid >= 1.5
BuildRequires:  python3-transaction >= 2.0
BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-webtest


%description
%{desc}


%package -n python3-pyramid-tm
Summary:        %{sum}


Requires:       python3-pyramid >= 1.5
Requires:       python3-transaction >= 2.0

%description -n python3-pyramid-tm
pyramid_tm is a package which allows Pyramid requests to join the
active transaction as provided by the transaction
http://pypi.python.org/pypi/transaction

See http://docs.pylonsproject.org/projects/pyramid_tm/dev/
or docs/index.rst in this distribution for detailed documentation.


%prep
%setup -q -n %{modname}-%{version}


# Make sure that setuptools picks the right version of zope.interface (el6)
awk 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"zope.interface>=3.8\"]; import pkg_resources"}1' setup.py > setup.py.tmp
mv setup.py.tmp setup.py

# Remove bundled egg info

rm docs/.gitignore

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pyproject_check_import
%{__python3} setup.py test

%files -n python3-pyramid-tm -f %{pyproject_files}
%doc README.rst docs CONTRIBUTORS.txt CHANGES.rst
%license COPYRIGHT.txt


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 2.5-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.5-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Mattia Verga <mattia.verga@proton.me> - 2.5-4
- Rebuilt for Pyramid 2.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 2.5-2
- Rebuilt for Python 3.11

* Sun May 29 2022 Kevin Fenzi <kevin@scrye.com> - 2.5-1
- Update to 2.5. Fixes rhbz#2063479

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 27 2020 Kevin Fenzi <kevin@scrye.com> - 2.4-1
- Update to 2.4. Fixes 1788205

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3-1
- Update to 2.3 (#1757160).
- https://github.com/Pylons/pyramid_tm/blob/2.3/CHANGES.rst

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Subpackage python2-pyramid-tm has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.2.1-1
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.2-6
- Modernize the spec file a little
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Sep 15 2017 Kevin Fenzi <kevin@scrye.com> - 2.2-1
- Update to 2.2. Fixes bug #1467463

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1-1
- Update to 2.1 (#1462289).
- http://docs.pylonsproject.org/projects/pyramid_tm/en/latest/#id3

* Fri Jun 16 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.1-4
- I mistakenly had this package depend on python2-{pyramid,transaction}.
  This update fixes that error.

* Fri Jun 16 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.1-3
- Rename python-pyramid-tm to python2-pyramid-tm.
- Always build for python 3.
- Remove the .gitignore file from the docs.

* Fri Jun 16 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.1-2
- Use python2- versions of three BuildRequires.

* Fri Jun 16 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (#1462252).
- Drop the EL 6 patch, since this update can only go into F26 and Rawhide.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 15 2015 Ralph Bean <rbean@redhat.com> - 0.12-1
- new version
- Move license and copyright to a %%license field.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Ralph Bean <rbean@redhat.com> - 0.7-2
- Patch to remove a block that requires python-transaction>=1.1 which is
  unavailable on el6.

* Fri Jun 21 2013 Ralph Bean <rbean@redhat.com> - 0.7-1
- Latest upstream
- Added python3 subpackage.
- Added test suite to check section.
- Included upstream docs.
- Write unauthenticated userid and request.path_info as transaction metadata
  via t.setUser and t.note respectively during a commit.
- Disuse the confusing and bug-ridden generator-plus-context-manager "attempts"
  mechanism from the transaction package for retrying retryable exceptions
  (e.g. ZODB ConflictError). Use a simple while loop plus a counter and
  imperative logic instead
- When a non-retryable exception was raised as the result of a call to
  transaction.manager.commit, the exception was not reraised properly. Symptom:
  an unrecoverable exception such as Unsupported: Storing blobs in
  <somestorage> is not supported. would be swallowed inappropriately.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Ross Delinger <rossdylan@csh.rit.edu> 0.4-1
- initial package for Fedora
