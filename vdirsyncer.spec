# invoke with "--with tests" to enable tests, currently disabled
# as we need to package both wsgi_intercept and pytest-localserver
# for them to work. Will also need BR: pystest once the two
# above packages exist in Fedora

%global sum Synchronize calendars and contacts
%global srcname vdirsyncer
# Share doc between python- and python3-
%global _docdir_fmt %{name}

Name:       vdirsyncer
Version:    0.19.2
Release:    6%{?dist}
Summary:    %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://github.com/pimutils/%{name}
Source0:    %{pypi_source}

Patch0:     aiostream-version-bump.patch

BuildArch:  noarch
Obsoletes:  python2-%{srcname} <= 0.12.1

BuildRequires:  make
BuildRequires:  python3-atomicwrites >= 0.1.7
BuildRequires:  python3-click >= 5.0
BuildRequires:  python3-click-log >= 0.4
BuildRequires:  python3-click-threading >= 0.4.0
BuildRequires:  python3-devel
BuildRequires:  python3-icalendar
BuildRequires:  python3-lxml
BuildRequires:  python3-requests >= 2.10
BuildRequires:  python3-requests-toolbelt >= 0.4.0
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-aiohttp-oauthlib
BuildRequires:  python3-trustme
BuildRequires:  python3-pytest-httpserver
BuildRequires:  python3-pytest-localserver

Requires:       python3-atomicwrites >= 0.1.7
Requires:       python3-click >= 5.0
Requires:       python3-click-log >= 0.4
Requires:       python3-click-threading >= 0.4.0
Requires:       python3-icalendar
Requires:       python3-lxml >= 3.1
Requires:       python3-requests >= 2.10
Requires:       python3-requests-toolbelt >= 0.4.0
Requires:       python3-aiohttp-oauthlib
Requires:       python3-vdirsyncer = %{version}
Requires:       sqlite

%description
vdirsyncer synchronizes your calendars and address books between two entities.
The supported protocols are CalDAV, CardDAV, arbitrary HTTP resources and some
more.

It aims to be for CalDAV and CardDAV what OfflineIMAP is for IMAP.

%package -n python3-%{srcname}
Summary:        %{sum}

Requires:       python3-atomicwrites >= 0.1.7
Requires:       python3-click >= 5.0
Requires:       python3-click-log >= 0.4
Requires:       python3-click-threading >= 0.4.0
Requires:       python3-icalendar
Requires:       python3-lxml >= 3.1
Requires:       python3-requests >= 2.10
Requires:       python3-requests-toolbelt >= 0.4.0
Requires:       python3-aiohttp-oauthlib

%description -n python3-%{srcname}
vdirsyncer synchronizes your calendars and address books between two entities.
The supported protocols are CalDAV, CardDAV, arbitrary HTTP resources and some
more.

It aims to be for CalDAV and CardDAV what OfflineIMAP is for IMAP.
This package contains the python3 modules.

%package doc
Summary:        Documentation for vdirsyncer

%description doc
The vdirsyncer-doc package provides all the documentation
for the vdirsyncer calendar/address-book synchronization utility.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
# From: https://athoscr.fedorapeople.org/packaging/python-setuptools_scm_git_archive.spec
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

# Custom sphinx docs need to import vdirsyncer classes from the untarred
# source tree
export PYTHONPATH=`pwd`
cd docs
# NOT using smp_mflags because sphinx cannot really cope with it
# i.e. one out of 20 builds will misteriously fail
make SPHINXBUILD=sphinx-build-3 man html text
cd ..
unset PYTHONPATH
# Remove extra copy of text docs
rm -vrf docs/_build/html/_sources
rm -fv docs/_build/html/{.buildinfo,objects.inv}


%install
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
# From: https://athoscr.fedorapeople.org/packaging/python-setuptools_scm_git_archive.spec
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l %{srcname}

install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r docs/_build/man/%{name}.1 "$RPM_BUILD_ROOT%{_mandir}/man1"

%check
%if %{with tests}
sh build.sh tests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS.rst README.rst CONTRIBUTING.rst


%files
%license LICENSE
%{_bindir}/vdirsyncer
%{_mandir}/man1/%{name}.1.*

# Still one rpmlint warning due to BZ 1107813
# W: wrong-file-end-of-line-encoding /usr/share/doc/vdirsyncer-doc/html/_static/jquery.js
%files doc
%doc docs/_build/html docs/_build/text

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.19.2-6
- convert license to SPDX

* Mon Aug 26 2024 Michel Lind <salimma@fedoraproject.org> - 0.19.2-5
- Bump allowed version of aiostream again
- Fixes: RHBZ#2308075

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.19.2-3
- Rebuilt for Python 3.13

* Sat Feb 03 2024 David Kaufmann <astra@ionic.at> - 0.19.2-1
- Update to v0.19.2

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.18.0-9
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 17 2022 David Kaufmann <astra@ionic.at> - 0.18.0-7
- Fix autogenerated dependency

* Mon Aug 15 2022 David Kaufmann <astra@ionic.at> - 0.18.0-6
- Update click-log dependency in all places

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.18.0-4
- Rebuilt for Python 3.11

* Fri Mar 18 2022 David Kaufmann <astra@ionic.at> - 0.18.0-3
- Update click-log dependency

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 David Kaufmann <astra@ionic.at> - 0.18.0-1
- Update to v0.18.0

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.8-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.16.8-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 01 2020 David Kaufmann <astra@ionic.at> - 0.16.8-4
- Fix patch, as only Patch0 gets applied by default

* Sat Oct 31 2020 David Kaufmann <astra@ionic.at> - 0.16.8-3
- Fix for python 3.9 deprecation of getiterator

* Thu Aug 13 2020 David Kaufmann <astra@ionic.at> - 0.16.8-1
- Update to v0.16.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16.7-8
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 David Kaufmann <astra@ionic.at> - 0.16.7-6
- Fix url
- Inject version string for setuptools_scm, as it builds from tarball, not git

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.16.7-5
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.16.7-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Timothée Floure <fnux@fedoraproject.org> - 0.16.7-1
- New upstream release
- Use the proper pypi_source macro to define the source tag

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.16.3-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Michele Baldessari <michele@acksyn.org> - 0.16.3-1
- New upstream

* Thu Aug 24 2017 Michele Baldessari <michele@acksyn.org> - 0.16.2-1
- New upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Michele Baldessari <michele@acksyn.org> - 0.16.0-1
- New upstream
- License is now BSD
- Require sqlite3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Michele Baldessari <michele@acksyn.org> - 0.14.1-1
- New upstream

* Wed Dec 28 2016 Michele Baldessari <michele@acksyn.org> - 0.14.0-1
- New upstream
- Since 0.13.0 there is no longer python2 support, so drop it and obsolete python2-vdirsyncer

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-2
- Rebuild for Python 3.6

* Sun Sep 04 2016 Michele Baldessari <michele@acksyn.org> - 0.12.1-1
- New upstream

* Mon Aug 01 2016 Michele Baldessari <michele@acksyn.org> - 0.11.3-1
- New upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 19 2016 Michele Baldessari <michele@acksyn.org> - 0.11.2-2
- Bump python-click-threading requirement

* Fri Jun 17 2016 Michele Baldessari <michele@acksyn.org> - 0.11.2-1
- New upstream

* Mon May 23 2016 Michele Baldessari <michele@acksyn.org> - 0.11.0-2
- Add requests-oauthlib to requires to get google integration

* Sun May 22 2016 Michele Baldessari <michele@acksyn.org> - 0.11.0-1
- New upstream (BZ#1329867)
- Split the package in python{2,3}-vdirsyncer containing the python modules and
  vdirsyncer containing the binary (needs the python3-modules)
- Add a python2 vdirsyncer module (BZ#1323555)

* Tue May 03 2016 Michele Baldessari <michele@acksyn.org> - 0.10.0-1
- New upstream

* Wed Mar 23 2016 Michele Baldessari <michele@acksyn.org> - 0.9.3-1
- New upstream

* Mon Mar 14 2016 Michele Baldessari <michele@acksyn.org> - 0.9.2-1
- New upstream
- Fix up some requires versioning

* Tue Feb 16 2016 Michele Baldessari <michele@acksyn.org> - 0.9.0-1
- New upstream

* Sat Feb 13 2016 Michele Baldessari <michele@acksyn.org> - 0.8.1-2
- Switch to python3 by default

* Fri Feb 12 2016 Michele Baldessari <michele@acksyn.org> - 0.8.1-1
- New upstream (requires python-click-{log,threading})

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Michele Baldessari <michele@acksyn.org> - 0.7.5-1
- New upstream, requires 0.5.0 python-requests-toolbelt

* Sat Nov 28 2015 Michele Baldessari <michele@acksyn.org> - 0.7.3-1
- New upstream (BZ 1275860)

* Sun Sep 13 2015 Michele Baldessari <michele@acksyn.org> - 0.6.0-2
- Add python-atomicwrites requires (BZ 1262597)

* Thu Aug 06 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.0-1
- Update to 0.6.0
- Use %%license
- Use PyPI tarball (see setup.py)

* Mon Jul 06 2015 Michele Baldessari <michele@acksyn.org> - 0.5.2-2
- Fix FTBFS (BZ#1046338)
* Tue Jun 16 2015 Michele Baldessari <michele@acksyn.org> - 0.5.2-1
- Update to 0.5.2
- Drop doc build patch
* Wed Jun 03 2015 Michele Baldessari <michele@acksyn.org> - 0.5.1-1
- Update to 0.5.1
- Drop system-urllib3.patch

* Fri Mar 13 2015 Michele Baldessari <michele@acksyn.org> - 0.4.4-1
- Update to 0.4.4

* Mon Mar 02 2015 Michele Baldessari <michele@redhat.com> - 0.4.3-5
- Disable python3 for now until khal supports it

* Sun Mar 01 2015 Michele Baldessari <michele@redhat.com> - 0.4.3-4
- Port to python3

* Sun Mar 01 2015 Michele Baldessari <michele@redhat.com> - 0.4.3-3
- Split out a -doc subpackage as fedora-review complained

* Sat Feb 28 2015 Michele Baldessari <michele@redhat.com> - 0.4.3-2
- Conditional test builds

* Mon Feb 23 2015 Michele Baldessari <michele@redhat.com> - 0.4.3-1
- New upstream

* Wed Feb 11 2015 Michele Baldessari <michele@redhat.com> - 0.4.2-3
- Add html and text documentation

* Wed Feb 04 2015 Michele Baldessari <michele@redhat.com> - 0.4.2-2
- Add python-atomicwrites dependency

* Tue Feb 03 2015 Michele Baldessari <michele@redhat.com> - 0.4.2-1
- New upstream

* Mon Jan 05 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-2
- Force use of system urllib3

* Mon Jan 05 2015 Michele Baldessari <michele@redhat.com> - 0.4.0-1
- New upstream

* Mon Jan 05 2015 Michele Baldessari <michele@redhat.com> - 0.3.4-2
- Added python-icalendar and python-click Requires

* Mon Dec 15 2014 Michele Baldessari <michele@redhat.com> - 0.3.4-1
- New upstream

* Wed Oct 01 2014 Michele Baldessari <michele@redhat.com> - 0.3.0-1
- Initial packaging
