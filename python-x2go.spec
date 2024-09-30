%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-x2go
Version:        0.6.1.4
Release:        7%{?dist}
Summary:        Python module providing X2Go client API

License:        AGPL-3.0-or-later
URL:            https://www.x2go.org/
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
# Rename SafeConfigParser to ConfigParser
Patch0:         https://gitlab.x2go.org/x2go/client/libs/python-x2go/-/merge_requests/7.patch

BuildArch:      noarch

BuildRequires: make

%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client side mass storage mounting support
   - audio support
   - authentication by smartcard and USB stick

This Python module allows you to integrate X2Go client support into your
Python applications by providing a Python-based X2Go client API.


%package        doc
Summary:        Python X2Go client API documentation

%description    doc
This package contains the Python X2Go client API documentation.


%if 0%{with python2}
%package -n python2-x2go
Summary:        Python module providing X2Go client API
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For doc build
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  python2-configparser
BuildRequires:  python2-gevent
BuildRequires:  python2-future
BuildRequires:  python2-paramiko
BuildRequires:  python2-requests
BuildRequires:  python2-simplejson
# For docs
BuildRequires:  python2-xlib
Requires:       nxproxy
Requires:       python2-configparser
Requires:       python2-gevent
Requires:       python2-future
Requires:       python2-paramiko
Requires:       python2-requests
Requires:       python2-simplejson
Requires:       python2-xlib

%description -n python2-x2go
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client side mass storage mounting support
   - audio support
   - authentication by smartcard and USB stick

This Python module allows you to integrate X2Go client support into your
Python applications by providing a Python-based X2Go client API.
%endif


%package -n python%{python3_pkgversion}-x2go
Summary:        Python module providing X2Go client API
BuildRequires:  python%{python3_pkgversion}-devel
# For doc build
BuildRequires:  /usr/bin/sphinx-build-3
BuildRequires:  python%{python3_pkgversion}-gevent
BuildRequires:  python%{python3_pkgversion}-paramiko
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-simplejson
BuildRequires:  python%{python3_pkgversion}-xlib
Requires:       nxproxy
Requires:       python%{python3_pkgversion}-gevent
Requires:       python%{python3_pkgversion}-paramiko
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-simplejson
Requires:       python%{python3_pkgversion}-xlib

%description -n python%{python3_pkgversion}-x2go
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client side mass storage mounting support
   - audio support
   - authentication by smartcard and USB stick

This Python module allows you to integrate X2Go client support into your
Python applications by providing a Python-based X2Go client API.


%prep
%setup -q


%generate_buildrequires
%pyproject_buildrequires


%build
%if 0%{with python2}
%py2_build
%endif
%pyproject_wheel
make -C docs SPHINXBUILD=/usr/bin/sphinx-build-3 html


%install
%pyproject_install
%pyproject_save_files -l 'x2go*'
%if 0%{with python2}
%py2_install
%endif


%if 0%{with python2}
%files -n python2-x2go
%license COPYING
%doc ChangeLog README* TODO
%{python2_sitelib}/x2go*
%endif

%files -n python%{python3_pkgversion}-x2go -f %{pyproject_files}
%doc ChangeLog README* TODO

%files doc
%doc docs/build/html


%changelog
* Sat Aug 31 2024 Orion Poplawski <orion@nwra.com> - 0.6.1.4-7
- Add patch to rename SafeConfigParser to ConfigParser (bz#2308657)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.6.1.4-5
- Rebuilt for Python 3.13

* Sun Apr 21 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.1.4-4
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Orion Poplawski <orion@nwra.com> - 0.6.1.4-1
- Update to 0.6.1.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.6.1.3-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.6.1.3-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.1.3-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Orion Poplawski <orion@nwra.com> - 0.6.1.3-1
- Update to 0.6.1.3

* Sun Nov 24 2019 Orion Poplawski <orion@nwra.com> - 0.6.1.1-1
- Update to 0.6.1.1

* Wed Nov 20 2019 Orion Poplawski <orion@nwra.com> - 0.6.1.0-1
- Update to 0.6.1.0

* Tue Oct 29 2019 Orion Poplawski <orion@nwra.com> - 0.6.0.2-7
- Drop dep on python2-x2go from -doc sub-package

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  8 2019 Orion Poplawski <orion@nwra.com> - 0.6.0.2-3
- Drop requires on python3-configparser, part of python3 standard library

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Orion Poplawski <orion@nwra.com> - 0.6.0.2-1
- Update to 0.6.0.2

* Sun Oct 07 2018 Orion Poplawski <orion@cora.nwra.com> - 0.6.0.0-2
- Drop Python 2 package for Fedora 30+ (bugz #1632309)

* Thu Sep 20 2018 Orion Poplawski <orion@nwra.com> - 0.6.0.0-1
- Update to 0.6.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.6-4
- Rebuilt for Python 3.7

* Fri Mar 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0.6-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.6-1
- Update to 0.5.0.6
- Build python3 version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.5-1
- Update to 0.5.0.5
- Ship python2-x2go
- Modernize spec

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.4-1
- Update to 0.5.0.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.3-1
- Update to 0.5.0.3

* Thu Nov 27 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.2-1
- Update to 0.5.0.2

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.1-1
- Update to 0.5.0.1

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.0-1
- Update to 0.5.0.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 8 2014 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.9-1
- Update to 0.4.0.9
- Drop python-cups requires

* Wed Dec 11 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.8-1
- Update to 0.4.0.8

* Tue Aug 6 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.7-1
- Update to 0.4.0.7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 2 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.6-3
- Add requires nxproxy and python-cups
- Build the documentation and ship in -doc sub-package

* Thu Aug 1 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.6-2
- Remove python shbangs from library scripts

* Wed Jul 31 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.6-1
- Update to 0.4.0.6

* Wed Jul 10 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.4-1
- Update to 0.4.0.4

* Tue Feb 12 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.0-1
- Update to 0.4.0.0

* Tue Dec 18 2012 Orion Poplawski <orion@cora.nwra.com> - 0.2.1.1-1
- Initial Fedora package
