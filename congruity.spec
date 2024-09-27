Name:		congruity
Version:	21
Release:	9%{?dist}
Summary:	Applications to program Logitech Harmony universal remote controls

# Code is GPLv3+, icons are the other two licenses
License:	GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-1.0-or-later
URL:		https://sourceforge.net/projects/congruity
Source0:	https://downloads.sourceforge.net/congruity/%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
Requires:	python3-wxpython4
Requires:	python3-libconcord
# For mhgui
Requires:	python3-suds

%description
congruity is a GUI application for programming Logitech Harmony universal
remote controls. congruity builds upon the work of libconcord, which
provides the underlying communication.

congruity is configured to handle the configuration files downloaded
from the Logitech configuration website. After installing this package
you can just use the Logitech configuration website and congruity will
launch automatically when appropriate.

A tool called 'mhgui' is also included for configuring remotes that only
work through the myharmony.com website, which does not work with Linux.
This includes the Harmony 200 and Harmony 300. To use it, simply run
'mhgui' and follow the prompts.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/mhgui.desktop

%files
%doc Changelog COPYING README.txt
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-*egg-info/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/mhgui.desktop
%{_mandir}/*/*

%changelog
* Wed Jul 31 2024 Scott Talbert <swt@techie.net> - 21-9
- Update License tag to use SPDX identifiers

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 21-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 21-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Scott Talbert <swt@techie.net> - 21-1
- Update to new upstream release 21 (#2118211)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 20-16
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20-13
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Scott Talbert <swt@techie.net> - 20-10
- Add missing BR for setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 20-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 20-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Scott Talbert <swt@techie.net> - 20-1
- New upstream release 20

* Mon Jun 11 2018 Scott Talbert <swt@techie.net> - 19-1
- New upstream release 19
- Remove patches (incorporated upstream)
- Switch to Python 3 and wxPython 4
- Remove scriptlets that are no longer needed

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jul 29 2017 Scott Talbert <swt@techie.net> - 18-13
- Minor python/general packaging updates

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Scott Talbert <swt@techie.net> - 18-9
- Removed superfluous defattr
- Fix bogus changelog date

* Tue Jan 05 2016 Scott Talbert <swt@techie.net> - 18-8
- Modernize packaging, libconcord-python -> python2-libconcord on F24+

* Mon Nov 02 2015 Scott Talbert <swt@techie.net> - 18-7
- Included upstream patch to fix login issues in mhgui

* Tue Aug 11 2015 Scott Talbert <swt@techie.net> - 18-6
- Included upstream patch to fix SupportedCapabilities issue in mhgui

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 08 2015 Scott Talbert <swt@techie.net> - 18-4
- Include upstream commits to fix login traceback (#1190230)

* Wed Dec 31 2014 Scott Talbert <swt@techie.net> - 18-3
- Include upstream patch for wxPython 3.0 support (#1177990)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Scott Talbert <swt@techie.net> - 18-1
- New upstream release 18
- Add handling for mhgui .desktop file
- Remove old unnecessary items

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Adam Williamson <awilliam@redhat.com> - 17-2
- requires: python-suds for mhgui, add mhgui note to description

* Fri Jun 21 2013 Adam Williamson <awilliam@redhat.com> - 17-1
- new release 17

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Adam Williamson <awilliam@redhat.com> - 15-1
- new release 15

* Thu Jan 14 2010 Adam Williamson <awilliam@redhat.com> - 14-1
- new release 14

* Thu Aug 06 2009 Adam Williamson <awilliam@redhat.com> - 13-1
- new release 13

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Adam Williamson <awilliam@redhat.com> - 12-1
- new release 12
- upstream now includes the .desktop file

* Thu Jun 18 2009 Adam Williamson <awilliam@redhat.com> - 11-4
- add CC-BY-SA to the license field
- don't explicitly specify permissions in file list

* Thu Jun 18 2009 Adam Williamson <awilliam@redhat.com> - 11-3
- don't do 'make all', there's nothing to make

* Thu Jun 18 2009 Adam Williamson <awilliam@redhat.com> - 11-2
- validate the desktop file on install

* Wed Jun 17 2009 Adam Williamson <awilliam@redhat.com> - 11-1
- New release 11
- Drop the .desktop patch (merged upstream)
- Include the .desktop file from upstream SVN as a source: it was
  accidentally left out of the tarball
- Disable desktop database update during install
- Version the wxPython require

* Wed Jun 17 2009 Adam Williamson <awilliam@redhat.com> - 10-1
- New release 10
- Add a .desktop file to associate congruity with appropriate files
- take out trademark characters in description, doing this is Bad

* Sun Sep 07 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 9-1
- Initial packaging

