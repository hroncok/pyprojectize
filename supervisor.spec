Name: supervisor
Summary:  A System for Allowing the Control of Process State on UNIX
Version: 4.2.5
Release: 5%{?dist}
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://supervisord.org/
Source0: https://pypi.python.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz
Source1: supervisord.service
Source2: supervisord.conf
Source3: supervisor.logrotate
Source4: supervisor.tmpfiles
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd

Requires: python3-setuptools

%description
The supervisor is a client/server system that allows its users to control a
number of processes on UNIX-like operating systems.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/%{_sysconfdir}/supervisord.d
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}/%{_rundir}/%{name}
chmod 755 %{buildroot}/%{_localstatedir}/log/%{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/supervisord.service
install -p -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/supervisord.conf
install -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/supervisor
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
sed -i s'/^#!.*//' $( find %{buildroot}/%{python3_sitelib}/supervisor/ -type f)

rm -f %{buildroot}%{_prefix}/doc/*.txt

%post
%systemd_post %{name}d.service

%preun
%systemd_preun %{name}d.service

%postun
%systemd_postun %{name}d.service

%files
%doc CHANGES.rst README.rst
%license COPYRIGHT.txt LICENSES.txt
%dir %{_localstatedir}/log/%{name}
%{_unitdir}/supervisord.service
%{python3_sitelib}/supervisor*
%{_bindir}/supervisor*
%{_bindir}/echo_supervisord_conf
%{_bindir}/pidproxy
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/supervisord.conf
%dir %{_sysconfdir}/supervisord.d
%dir %{_rundir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/supervisor

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.5-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.2.5-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 29 2023 Jonathan Steffan <jsteffan@fedoraproject.org> - 4.2.5-1
- Update to 4.2.5 (RHBZ#2239529)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.2.2-7
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.2.2-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Francisco Javier Tsao Santín <tsao@disroot.org> - 4.2.2-1
- Upgraded to 4.2.2 version.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Francisco Javier Tsao Santín <tsao@gpul.org> - 4.2.1-1
- Fix missing /run/supervisor in containers (#1898106). Updated to 4.2.1 version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-3
- Rebuilt for Python 3.9

* Thu May 14 2020 Neal Gompa <ngompa13@gmail.com> - 4.2.0-2
- Packaging cleanups to align with current Fedora Packaging Guidelines

* Fri May 01 2020 Francisco Javier Tsao Santín <tsao@gpul.org> - 4.2.0-1
- Upgraded to 4.2.0 version. Removed meld3 dependency (#1830213)

* Wed Apr 01 2020 Francisco Javier Tsao Santín <tsao@gpul.org> - 4.1.0-1
- Upgraded to 4.1.0 version. Removed meld3 dependency
- Fix systemd post tasks

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 4.0.4-3
- Fix for #1770452 missing /var/supervisor directory

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.4-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Oct 02 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 4.0.4-1
- Upgraded to 4.0.4 version; updated /var/run to /run temporary dir

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 4.0.2-1
- Upgraded to 4.0.2 version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0.dev0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Francisco Javier Tsao Santín <tsao@gpul.org> - 4.0.0.dev0-1
- Upgraded to 4.0.0.dev0 in order to remove python2 dependencies.
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jul 29 2017 Francisco Javier Tsao Santín <tsao@gpul.org> - 3.3.3-1
- Security fix for CVE-2017-11610

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Ville Skyttä <ville.skytta@iki.fi> - 3.3.1-2
- Move tmpfiles.d config to %%{_tmpfilesdir}
- Install license files as %%license

* Sun Jan 08 2017 Francisco J. Tsao Santín <tsao@gpul.org> 3.3.1-1
- upgraded to 3.3.1 version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Tue May 17 2016 Nils Philippsen <nils@redhat.com> - 3.2.3-3
- remove obsolete SysVStartPriority tag from service file (#1336878)

* Mon Apr 25 2016 Nils Philippsen <nils@redhat.com> - 3.2.3-2
- add back setuptools dependency

* Wed Apr 20 2016 Nils Philippsen <nils@redhat.com> - 3.2.3-1
- version 3.2.3
- use python2 macros and package names
- remove ZPLv2.1 from license
- clean up some legacy cruft

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Nils Philippsen <nils@redhat.com>
- use %%global instead of %%define

* Wed Aug 19 2015 Kevin Fenzi <kevin@scrye.com> 3.1.3-3
- Fix tmpfiles.d files.

* Sat Aug 01 2015 Kevin Fenzi <kevin@scrye.com> 3.1.3-2
- Actually commit some more cleanup and fixes I tested with.

* Sat Aug 01 2015 Kevin Fenzi <kevin@scrye.com> 3.1.3-1
- Update to 3.1.3
- Move socket to /var/run/supervisor. Fixes bug #1247877
- Clean up old spec cruft. Possibly fixes bug #1094933

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 01 2013 Nils Philippsen <nils@redhat.com> - 3.0-1
- version 3.0 (final)
- fix changelog dates

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.11.a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 01 2012 Nils Philippsen <nils@redhat.com> - 3.0-0.10.a12
- add [Install] section to service file, so systemctl can enable it

* Tue Aug 21 2012 Nils Philippsen <nils@redhat.com> - 3.0-0.9.a12
- use systemd macros from F-18/RHEL-7 on
- use %%{_unitdir} macro for systemd unit paths

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.8.a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 3.0-0.7.a12
- version 3.0a12

* Tue Aug 02 2011 Nils Philippsen <nils@redhat.com> - 3.0-0.6.a10
- add native systemd support

* Mon Aug 01 2011 Nils Philippsen <nils@redhat.com> - 3.0-0.5.a10
- require python-setuptools (#725191)

* Tue Apr 05 2011 Nils Philippsen <nils@redhat.com> - 3.0-0.4.a10
- version 3.0a10
- fix source URL
- don't use macros for system executables (except python)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.3.a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.0-0.2.a8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 Nils Philippsen <nils@redhat.com> - 3.0-0.1.a8
- add BR: python-setuptools

* Mon Apr 12 2010 Nils Philippsen <nils@redhat.com>
- bundle updated config file

* Sat Apr 10 2010 Nils Philippsen <nils@redhat.com>
- version 3.0a8
- update URLs
- versionize python-meld3 dependency

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.1-6
- Rebuild for Python 2.6

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-5
- fix license tag

* Mon Jan 07 2008 Toshio Kuratomi <toshio@fedoraproject.org>  2.1-4
- Include egginfo files when python generates them.

* Sun Apr 22 2007 Mike McGrath <mmcgrath@redhat.com> 2.1-3
- Added BuildRequires of python-devel

* Fri Apr 20 2007 Mike McGrath <mmcgrath@redhat.com> 2.1-2
- Added patch suggested in #153225

* Fri Apr 20 2007 Mike McGrath <mmcgrath@redhat.com> 2.1-1
- Initial packaging

