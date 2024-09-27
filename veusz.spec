Name:           veusz
Version:        3.6.2
Release:        6%{?dist}
Summary:        GUI scientific plotting package

License:        GPL-2.0-or-later AND (LGPL-2.1-only OR GPL-3.0-only) AND PSF-2.0 AND CC0-1.0
URL:            https://veusz.github.io/
Source0:        https://github.com/veusz/veusz/releases/download/veusz-%{version}/veusz-%{version}.tar.gz

BuildRequires:  gcc gcc-c++
BuildRequires:  python3 python3-devel
BuildRequires:  python3-numpy
BuildRequires:  qt5-qtbase-devel qt5-qtsvg-devel
BuildRequires:  python3-qt5 python3-qt5-devel
BuildRequires:  python3-pyqt5-sip python3dist(sip)
BuildRequires:  python3-h5py
BuildRequires:  python3-tomli
BuildRequires:  desktop-file-utils

Requires:       python3dist(pyqt5-sip) >= 12.8, python3dist(pyqt5-sip) < 13
Requires:       python3-numpy python3-qt5 /usr/bin/env
Provides:       python3-veusz

# we don't want to provide private python extension libs
# https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
%global __provides_exclude_from ^%{python3_sitearch}/veusz/helpers/.*\\.so$

# install docs in version specific for old releases
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Veusz is a 2D and 3D scientific plotting package, designed to create
publication-ready vector PDF and SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with error bars, keys, labels, stacked plots,
ternary plots, vector plots, contours, images, shapes and fitting
data. 3D point, surface, volume and function plots are also supported.

%prep
%setup -q -n veusz-%{version}

find -name \*~ | xargs rm -f

# remove shebangs from scripts which aren't installed
# (veusz allows these to be executed if app isn't installed properly)
sed -i '/^#!/d' veusz/veusz_main.py
sed -i '/^#!/d' veusz/veusz_listen.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
rm -rf %{buildroot}

# veusz-resource-dir: put data files in location given
%{__python3} setup.py install --skip-build --root %{buildroot} \
    --veusz-resource-dir=%{buildroot}/%{_datadir}/veusz \
    --disable-install-examples

# tell veusz where its resource directory is in _datadir
ln -s %{_datadir}/veusz \
    %{buildroot}%{python3_sitearch}/veusz/resources

# tell it where to look for examples and COPYING
ln -s %{_pkgdocdir}/examples \
   %{buildroot}%{_datadir}/veusz

# install desktop file
desktop-file-install  \
    --dir %{buildroot}%{_datadir}/applications \
    support/veusz.desktop

# file to register .vsz mimetype
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -p support/veusz.xml -m 0644 %{buildroot}%{_datadir}/mime/packages/

# appdata file
mkdir -p %{buildroot}%{_datadir}/appdata/
install -p support/veusz.appdata.xml -m 0644 %{buildroot}%{_datadir}/appdata/

# symlink main veusz icon into pixmaps (for desktop file)
mkdir %{buildroot}%{_datadir}/pixmaps
ln -s ../veusz/icons/veusz_48.png %{buildroot}%{_datadir}/pixmaps/veusz.png

# also link in hicolor icons
for size in 16 32 48 64 128; do
    odir=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mkdir -p $odir
    ln -s %{_datadir}/veusz/icons/veusz_${size}.png ${odir}/veusz.png
done
odir=%{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $odir
ln -s %{_datadir}/veusz/icons/veusz.svg $odir

# install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -p Documents/man-page/veusz.1 -m 0644 \
    %{buildroot}%{_mandir}/man1

%check
# as the data directory hasn't got the same absolute path we have
# to define VEUSZ_RESOURCE_DIR
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    VEUSZ_RESOURCE_DIR=%{buildroot}%{_datadir}/veusz \
    QT_QPA_PLATFORM=minimal \
    %{__python3} tests/runselftest.py

%files
%doc README.md AUTHORS COPYING
%doc examples
%doc Documents/manual/html
%{_bindir}/veusz
%{_mandir}/man1/veusz.1.gz
%{_datadir}/applications/veusz.desktop
%{_datadir}/mime/packages/veusz.xml
%{_datadir}/appdata/veusz.appdata.xml
%{_datadir}/pixmaps/veusz.png
%{_datadir}/icons/hicolor/*/apps/veusz.*
%{_datadir}/veusz
%{python3_sitearch}/veusz.dist-info
%{python3_sitearch}/veusz

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.6.2-5
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 3.6.2-2
- Rebuilt for Python 3.12

* Sun Feb 26 2023 Jeremy Sanders <jeremy@jeremysanders.net> - 3.6.2-1
- Update to Veusz 3.6.2 (fixes resource issue)

* Sun Feb 26 2023 Jeremy Sanders <jeremy@jeremysanders.net> - 3.6.1-1
- Update to Veusz 3.6.1 (fixes appdata issue)

* Sat Feb 25 2023 Jeremy Sanders <jeremy@jeremysanders.net> - 3.6-1
- Update to Veusz 3.6

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jeremy Sanders <jeremy@jeremysanders.net> - 3.5.3-2
- Use explicit files, rather than glob all
- Update licence to new rules
- Update provide filtering to new method for internal libraries

* Tue Nov 01 2022 Jeremy Sanders <jeremy@jeremysanders.net> - 3.5.3-1
- Update to Veusz 3.5.3

* Tue Nov 01 2022 Jeremy Sanders <jeremy@jeremysanders.net> - 3.5-1
- Update to Veusz 3.5

* Wed Aug 17 2022 Jeremy Sanders <jeremy@jeremysanders.net> - 3.4-5
- Patch to fix build system for new sip versions (RHBZ#2113753)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.4-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 17 2021 Jeremy Sanders <jeremy@jeremysanders.net> - 3.4-1
- Update to Veusz 3.4
- Switch to sip 6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Scott Talbert <swt@techie.net> - 3.3.1-6
- Revert back to building with sip 4 due to no sip 6 support

* Wed Jun 16 2021 Scott Talbert <swt@techie.net> - 3.3.1-5
- Update to build with sip 5

* Wed Jun 16 2021 Jeremy Sanders <jeremy@jeremysanders.net> - 3.3.1-4
- Drop astropy build requirement as python3-astropy not currently building

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Jeremy Sanders <jeremy@jeremysanders.net> - 3.3.1-1
- Update to Veusz 3.3.1, dropping upstreamed patches

* Sat Dec 05 2020 Jeremy Sanders <jeremy@jeremysanders.net> - 3.3-2
- Depend on namespaced sip module
- Drop sip requirement in setup.py (RHBZ#1904473)

* Sun Nov 29 2020 Jeremy Sanders <jeremy@jeremysanders.net> - 3.3-1
- Update to Veusz 3.3
- Fix Python 10 compatibility (RHBZ#1903072)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Jeremy Sanders <jeremy@jeremysanders.net> - 3.2.1-1
- Update to Veusz 3.2.1

* Sun Mar 08 2020 Jeremy Sanders <jeremy@jeremysanders.net> - 3.2-1
- Update to Veusz 3.2
- Fixes failure to build on Python 3.9 (#1794334)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Jeremy Sanders <jeremy@jeremysanders.net> - 3.1-1
- Update to Veusz 3.1
- Remove old sip-devel dependency

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-6
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Jeremy Sanders <jeremy@jeremysanders.net> - 3.0.1-5
- Patch for bug to fix RHBZ#1736948 (build failure on rawhide)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 3.0.1-1
- Update to Veusz 3.0.1
- Remove xvfb dependency on build

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0-2
- Rebuilt for Python 3.7

* Sun Jun 10 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 3.0-1
- Update to Veusz 3.0, which now includes 3D plotting. See
  https://veusz.github.io/news/2018/06/10/veusz-3.0

* Sun Apr 08 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 2.2.2-1
- Update to Veusz 2.2.2

* Sun Mar 11 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 2.2.1-1
- Update to Veusz 2.2.1

* Mon Feb 19 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 2.1.1-5
- Add gcc and gcc-c++ build deps

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Jeremy Sanders <jeremy@jeremysanders.net> - 2.1.1-3
- Rename urw-fonts to urw-base35-fonts (RHBZ #1541096)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.1-2
- Remove obsolete scriptlets

* Sat Nov 11 2017 Jeremy Sanders <jeremy@jeremysanders.net> - 2.1.1-1
- Update to Veusz 2.1.1
- Remove override as now fixed upstream

* Sun Oct 29 2017 Jeremy Sanders <jeremy@jeremysanders.net> - 2.1-2
- Override sip file location

* Sun Oct 29 2017 Jeremy Sanders <jeremy@jeremysanders.net> - 2.1-1
- Update to Veusz 2.1

* Sat Sep 23 2017 Jeremy Sanders <jeremy@jeremysanders.net> - 2.0.1-1
- Update to Veusz 2.0.1

* Sun Sep 17 2017 Jeremy Sanders <jeremy@jeremysanders.net> - 2.0-1
- Update to Veusz 2.0
- Switch to Qt 5
- Drop deprecated veusz_listen

* Sat Sep 02 2017 Jeremy Sanders <jeremy@jeremysanders.net> - 1.27-1
- Update to Veusz 1.27

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.26.1-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Tue May 16 2017 Jeremy Sanders <jeremy@jeremysanders.net> - 1.26.1-1
- Update to Veusz 1.26.1
- Update website and new download location

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Jeremy Sanders <jeremy@jeremysanders.net> - 1.25.1-1
- Update to Veusz 1.25.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.25-2
- Rebuild for Python 3.6

* Sat Dec 03 2016 Jeremy Sanders <jeremy@jeremysanders.net> - 1.25-1
- Update to Veusz 1.25

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 05 2016 Jeremy Sanders <jeremy@jeremysanders.net> - 1.24-1
- Update to Veusz 1.24

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan  2 2016 Jeremy Sanders <jeremy@jeremysanders.net> - 1.23.2-1
- Update to Veusz 1.23.2
- Update to python3

* Sat Apr 18 2015 Jeremy Sanders <jeremy@jeremysanders.net> - 1.23-2
- Fix COPYING bug

* Sat Apr 18 2015 Jeremy Sanders <jeremy@jeremysanders.net> - 1.23-1
- Update to Veusz 1.23

* Sun Oct 19 2014 Jeremy Sanders <jeremy@jeremysanders.net> - 1.22-1
- Update to Veusz 1.22

* Sun Aug 31 2014 Jeremy Sanders <jeremy@jeremysanders.net> - 1.21.1-1
- Update to Veusz 1.21.1

* Wed Aug 20 2014 Kevin Fenzi <kevin@scrye.com> - 1.21-5
- Rebuild for rpm bug 1131892

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 1.21-3
- update mime scriptlet

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Jeremy Sanders <jeremy@jeremysanders.net> 1.21-1
- Update to Veusz 1.21
- Add patch for self test failures

* Sun Mar 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1.20.1-3
- rebuild (sip)

* Sat Mar 01 2014 Jeremy Sanders <jeremy@jeremysanders.net> 1.20.1-2
- Change BuildRequires python-setuptools-devel to python-setuptools
  (as https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel)

* Thu Feb 13 2014 Jeremy Sanders <jeremy@jeremysanders.net> 1.20.1-1
- Update to Veusz 1.20.1
- BuildRequires urw-fonts to fix self tests
- Patch self test failure on arm

* Mon Jan 27 2014 Jeremy Sanders <jeremy@jeremysanders.net> 1.20-1
- Update to Veusz 1.20

* Fri Nov 29 2013 Jeremy Sanders <jeremy@jeremysanders.net> 1.19.1-1
- Update to Veusz 1.19.1 (bug fix release)

* Sun Nov 24 2013 Jeremy Sanders <jeremy@jeremysanders.net> 1.19-1
- Update to Veusz 1.19

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 1.18-4
- rebuild (sip)

* Wed Aug 07 2013 Jeremy Sanders <jeremy@jeremysanders.net> 1.18-3
- Remove version-specfic docdir (fix bug 993895)
- Fix COPYING location

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Jeremy Sanders <jeremy@jeremysanders.net> 1.18-1
- Update to Veusz 1.18

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 1.17.1-2
- rebuild (skip)

* Fri Apr 12 2013 Jeremy Sanders <jeremy@jeremysanders.net> - 1.17.1-1
- Update to Veusz 1.17.1

* Sat Mar 23 2013 Jeremy Sanders <jeremy@jeremysanders.net> - 1.17-1
- Update to Veusz 1.17

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.16-2
- rebuild (sip)

* Sat Jul 21 2012 Jeremy Sanders <jeremy@jeremysanders.net> - 1.16-1
- Update to Veusz 1.16

* Wed Apr 04 2012 Jeremy Sanders <jeremy@jeremysanders.net> - 1.15-1
- Update to Veusz 1.15

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 1.14-2
- rebuild (sip/PyQt4)

* Sun Nov 27 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 1.14-1
- Update to Veusz 1.14
- Significant simplifications of spec file
- Install all data files in _datadir/veusz
- Add icons to hicolor theme
- Filter provides from private python modules

* Mon Aug 22 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 1.13-1
- Update to Veusz 1.13

* Sat Jul 02 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 1.12-1
- Update to Veusz 1.12

* Wed Apr 06 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 1.11-3
- Fix version numbers in changelog

* Mon Apr 04 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 1.11-2
- Run self test after build
- Remove duplicate file statements

* Mon Apr 04 2011 Jeremy Sanders <jeremy@jeremysanders.net> - 1.11-1
- Update to Veusz 1.11

* Tue Mar 22 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.10-3
- fix scriptlet usage

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 1.10-1
- Update to Veusz 1.10
- Install man pages

* Fri Sep 10 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 1.9-2
- Add SIP API requirement

* Thu Sep  2 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 1.9-1
- Update to Veusz 1.9

* Wed Aug 18 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 1.8-3
- Remove extra source tar.gz from previous release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 19 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 1.8-1
- Update to Veusz 1.8

* Tue Mar 30 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 1.7-1
- Update to Veusz 1.7

* Fri Jan 29 2010 Jeremy Sanders <jeremy@jeremysanders.net> - 1.6-1
- Update to Veusz 1.6

* Mon Sep 28 2009 Jeremy Sanders <jeremy@jeremysanders.net> - 1.5-1
- Update to Veusz 1.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Jeremy Sanders <jeremy@jeremysanders.net> - 1.4-1
- Update to Veusz 1.4

* Mon Apr 6 2009 Jeremy Sanders <jeremy@jeremysanders.net> - 1.3-3
- Remove file that is not included

* Mon Apr 6 2009 Jeremy Sanders <jeremy@jeremysanders.net> - 1.3-2
- Fix readme location build issue

* Mon Apr 6 2009 Jeremy Sanders <jeremy@jeremysanders.net> - 1.3-1
- Update to Veusz 1.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 7 2008 Jeremy Sanders <jeremy@jeremysanders.net> - 1.2.1-1
- Update to Veusz 1.2.1
- Fix location of COPYING file for about dialog

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2-4
- Rebuild for Python 2.6

* Tue Nov 25 2008 Jeremy Sanders <jeremy@jeremysanders.net> - 1.2-3
- Fix bug in icon symlink

* Tue Nov 25 2008 Jeremy Sanders <jeremy@jeremysanders.net> - 1.2-2
- Fix move of icon location

* Tue Nov 25 2008 Jeremy Sanders <jeremy@jeremysanders.net> - 1.2-1
- Move to Veusz 1.2

* Thu Oct  2 2008 Jeremy Sanders <jeremy@jeremysanders.net> - 1.1-3
- Got email address wrong - bumping again

* Thu Oct  2 2008 Jeremy Sanders <jeremy@jeremysanders.net> - 1.1-2
- Forgot to add changelog for previous entry. Bumping.

* Thu Oct  2 2008 Jeremy Sanders <jeremy@jeremysanders.net> - 1.1-1
- Updated to Veusz 1.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-3
- Autorebuild for GCC 4.3

* Thu Dec 20 2007 Jeremy Sanders <jeremy@jeremysanders.net> - 1.0-2
- Package egg file

* Thu Dec 20 2007 Jeremy Sanders <jeremy@jeremysanders.net> - 1.0-1
- Update to Veusz-1.0 (now based on PyQt4/numpy)

* Thu Aug  2 2007 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-16
- Rebuilt as forgot to commit changes before make tag

* Thu Aug  2 2007 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-15
- Rebuilt as forgot to include comment for license update

* Thu Aug 2 2007 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-14
- Changed for new licensing guidelines. Now indicates the single file
with Python licensing

* Mon Dec 11 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-13
- Bumped for FC-devel

* Sat Sep 16 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-12
- Bump release for FC-devel rebuild

* Wed Sep  6 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-11
- Package .pyo files

* Wed Sep  6 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-10
- Removed ghosts, as per new Fedora guidelines

* Wed Jul 12 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-9
- Add -O1 to install to generate .pyo files on FC4

* Mon Jul 10 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-8
- Remove tab characters from spec file

* Fri Jul  7 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-7
- Change from python_sitelib to python_sitearch to fix x86_64

* Wed Jun 28 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-6
- Added semicolon to end of categories in .desktop file

* Mon Jun 26 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-5
- Add desktop-file-utils dependancy to post and postun
- Explicitly ghost *.pyo files
- Add X-Fedora category to installed .desktop file

* Tue Jun 20 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-4
- Own python module and pixmaps directory
- Fix location of icon for Gnome (use symlink)
- Register application/x-veusz mimetype
- Update mime and desktop databases in post and postun

* Mon Jun 19 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-3
- Fix rpmlint errors

* Mon Jun 19 2006 Jeremy Sanders <jeremy@jeremysanders.net> - 0.10-2
- Renamed from python-veusz to veusz

