%global osname  %(cat /etc/redhat-release | awk '{sub(/ release.*/,""); print}')
%global pkgmgr  dnf

%bcond_without  python3

Name:           krop
Version:        0.5.1
Release:        23%{?dist}
Summary:        Tool to crop PDF files with an eye towards eReaders
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://arminstraub.com/software/krop
Source0:        http://arminstraub.com/downloads/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# upstreamable patch, see also
# https://bugzilla.redhat.com/show_bug.cgi?id=1707034
# https://github.com/arminstraub/krop/issues/23
Patch1: krop-0.5.1-sip_namespace.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if %without python3
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-%{name} = %{version}-%{release}
%else
BuildRequires:  python3-devel
Requires:       python3-%{name} = %{version}-%{release}
%endif


%description
Krop is a simple graphical tool to crop the pages of PDF files. A unique feature
of krop is its ability to automatically split pages into subpages to fit the
limited screen size of devices such as eReaders. This is particularly useful, if
your eReader does not support convenient scrolling.

%if %without python3
%package -n python2-%{name}
Summary:    Python2 module for %{name}
Requires:   python-PyPDF2 PyQt5 python-poppler-qt5

%description -n python2-%{name}
%else
%package -n python3-%{name}
Summary:    Python3 module for %{name}
Requires:   python3-PyPDF2 python3-PyQt5 python3-poppler-qt5

%description -n python3-%{name}
%endif
%{summary}.


%prep
%setup -q
# In terms of OS available on Koji. "of" is needed since Ubuntu appears as font.
find . -type f -name '*.py' -exec sed -i -e 's/of ubuntu/of %{osname}/Ig' \
 -e 's|apt-get|%{pkgmgr}|g' -e 's|python-pypdf|pyPdf|g' '{}' +

%patch -P1 -p1 -b .sip_namespace

%generate_buildrequires
%pyproject_buildrequires

%build
%if %without python3
%py2_build
%else
%pyproject_wheel
%endif

%install
%if %without python3
%py2_install
%else
%pyproject_install
%pyproject_save_files %{name}
%endif
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
DESTDIR="%{buildroot}" appstream-util install %{name}.appdata.xml


%check
%if %without python3
%{__python2} setup.py check
%else
%{__python3} setup.py check
%endif
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%if %without python3
%files -n python2-%{name}
%{python2_sitelib}/%{name}-%{version}.dist-info
%{python2_sitelib}/%{name}/
%else
%files -n python3-%{name} -f %{pyproject_files}
%endif
%license LICENSE


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.1-21
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.1-17
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.1-14
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.1-11
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-8
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.5.1-6
- drop explicit dep pythonX-sip, use default name-spaced sip insetad (#1707034)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Tomas Hozza <thozza@redhat.com> - 0.5.1-3
- Add explicit dependency on pythonX-sip package (#1707034)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Tomas Hozza <thozza@redhat.com> - 0.5.1-1
- Update to latest upstream version 0.5.1 (#1544282)
- Switch to PyQt5, since Krop now supports it

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.13-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Tomas Hozza <thozza@redhat.com> - 0.4.13-1
- Update to 0.4.13 (#1473983, #1438018)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Raphael Groner <projects.rg@smart.ms> - 0.4.12-1
- rhbz#1370721
- build with python3 as upstream fixed
- drop useless build conditionals for rhel
- reference for description and license file only once

* Fri Oct 14 2016 Tomas Hozza <thozza@redhat.com> - 0.4.11-3
- Revert back to Python 2 (#1321376)

* Wed Aug 31 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.11-2
- add license file to subpackages

* Wed Aug 31 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.11-1
- new version
- migrate to python3 and split subpackage for module

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 03 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.10-1
- new version

* Fri May 06 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.9-6
- R: python2-pyPDF2 (instead of python-pyPDF2)

* Fri May 06 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.9-5
- revert to python2 because source is not compatible with python3, rhbz#1321376

* Sun Apr 24 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.9-4
- replace shebang for python3, rhbz#1321376

* Fri Mar 25 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.9-3
- revert to Qt4 because python3-poppler-qt5 is not available (yet)
- refactor python runtime needs
- simplify check, no tests for python available

* Fri Mar 25 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.9-2
- port to PyPDF2, Python3, Qt5

* Fri Mar 25 2016 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.4.9-1
- Update to 0.4.9 (#1276890)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Christopher Meng <rpm@cicku.me> - 0.4.8-1
- Update to 0.4.8

* Tue Feb 17 2015 Christopher Meng <rpm@cicku.me> - 0.4.7-1
- Update to 0.4.7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Richard Hughes <richard@hughsie.com> - 0.4.6-1
- Update to 0.4.6

* Sat Mar 01 2014 Christopher Meng <rpm@cicku.me> - 0.4.5-1
- Update to 0.4.5

* Sun Aug 25 2013 Christopher Meng <rpm@cicku.me> - 0.4.4-1
- Update to 0.4.4

* Wed Aug 14 2013 Christopher Meng <rpm@cicku.me> - 0.4.3-1
- Update to 0.4.3
- Correct desktop MIME update script.

* Wed Jul 31 2013 Christopher Meng <rpm@cicku.me> - 0.4.1-1
- Update to 0.4.1

* Sat Nov 12 2011 Christopher Meng <rpm@cicku.me> - 0.3.0-1
- Initial Package.
