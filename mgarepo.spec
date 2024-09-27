%define Uname MgaRepo

Name: mgarepo
Version: 1.13.2
Release: 31%{?dist}
Summary: Tools for Mageia repository access and management
# tarball needs to be created manually, since tags don't generate releases
# git clone git://git.mageia.org/software/build-system/mgarepo; cd mgarepo; git reset --hard %{version} && make dist
Source:  %{name}-%{version}.tar.xz

# Local fixes to upstream
Patch0500: 0001-Fix-iterating-on-log-entries-with-Python-3.9.patch

# Fedora-specific patches
# Mageia's urpmi is not available in Fedora, so we force DNF for buildrpm command
Patch1000: 0001-buildrpm-Always-use-DNF.patch

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://gitweb.mageia.org/software/build-system/mgarepo/
BuildRequires: python3-devel
Requires: subversion
Requires: openssh-clients
Requires: python3-rpm
Requires: python3-PyGithub >= 1.27.1
Requires: python3-httplib2
Requires: wget
BuildArch: noarch

%description
Tools for Mageia repository access and management.

It is a fork of repsys :
<http://wiki.mandriva.com/en/Development/Packaging/Tools/repsys>

%package ldap
Summary: Plugin for retrieving maintainer information from LDAP for mgarepo
Requires: %{name} = %{version}-%{release}
Requires: python3-ldap3

%description ldap
A mgarepo plugin that allows retrieving maintainer information shown in
changelogs from a LDAP server.

See mgarepo --help-plugin ldapusers for more information.


%prep
%autosetup -p1

# Fix requires for RPM Python bindings
sed -e "s/rpm-python/rpm/" -i setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files
%doc README.BINREPO CHANGES %{name}-example.conf
%attr(0644,-,-) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-ssh
%{_datadir}/%{name}
%{_mandir}/*/*
%{python3_sitelib}/%{Uname}
%exclude %{python3_sitelib}/%{Uname}/plugins/ldapusers.py*
%exclude %{python3_sitelib}/%{Uname}/plugins/__pycache__/__init__*
%exclude %{python3_sitelib}/%{Uname}/plugins/__pycache__/ldapusers*
%{python3_sitelib}/*.dist-info
%{_datadir}/bash-completion/completions/%{name}

%files ldap
%doc README.LDAP
%{python3_sitelib}/%{Uname}/plugins/ldapusers.py*
%{python3_sitelib}/%{Uname}/plugins/__pycache__/__init__*
%{python3_sitelib}/%{Uname}/plugins/__pycache__/ldapusers*


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13.2-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.13.2-29
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.13.2-25
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.13.2-22
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.13.2-19
- Rebuilt for Python 3.10

* Sun Mar 14 2021 Neal Gompa <ngompa13@gmail.com> - 1.13.2-18
- Add patch to fix iterating on log entries with Python 3.9+

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Neal Gompa <ngompa13@gmail.com> - 1.13.2-16
- Add BR python3-setuptools

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.2-14
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.2-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.2-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Neal Gompa <ngompa13@gmail.com> - 1.13.2-9
- Fix requires on RPM Python bindings
- Fix older changelog entries to use full author names

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.13.2-6
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.13.2-2
- Rebuild for Python 3.6

* Mon Oct 10 2016 Neal Gompa <ngompa13@gmail.com> - 1.13.2-1
- Update to 1.13.2

* Sat Oct 08 2016 Neal Gompa <ngompa13@gmail.com> - 1.13.1-2
- Add patch to remove buildrpm's call to urpmi, as we only have DNF

* Sat Oct 08 2016 Neal Gompa <ngompa13@gmail.com> - 1.13.1-1
- Update to 1.13.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 14 2016 Neal Gompa <ngompa13@gmail.com> - 1.12.3-1
- Update to 1.12.3

* Sat Feb 20 2016 Neal Gompa <ngompa13@gmail.com> - 1.11.9-1
- Update to 1.11.9
- Remove redundant actions in install section
- Add mgarepo-ldap subpackage since plugin has been ported

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Neal Gompa <ngompa13@gmail.com> - 1.11.6-1
- Update to 1.11.6 (switches to Python 3)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Nov 26 2011 Michael Scherer <misc@fedoraproject.org> 1.10.2-1
* Adapt to Fedora

* Thu Nov 24 2011 Nicolas Vigier <boklm@mageia.org> 1.10.2-1.mga2
+ Revision: 171653
- version 1.10.2
- add require on wget
- version 1.10.1
- fix require on python-httplib
- add require on httplib2
- add python-devel as build require
- version 1.10.0

* Tue Jul 12 2011 Nicolas Vigier <boklm@mageia.org> 1.9.11-1.mga2
+ Revision: 123440
- Version 1.9.11: add maintdb command

  + Ahmad Samir <ahmad@mageia.org>
  - Fix the URL tag

* Wed May 25 2011 Nicolas Vigier <boklm@mageia.org> 1.9.10-1.mga1
+ Revision: 100367
- version 1.9.10

  + Michael Scherer <misc@mageia.org>
  - add source url
  - remove requires on python-devel ( should not be needed )
  - do not add version requires on mgarepo ( as all version should be ok )
  - fix missing defattr on ldap plugin ( rpmlint )

* Thu Mar 10 2011 Michael Scherer <misc@mageia.org> 1.9.9-2.mga1
+ Revision: 67691
- fix License
- use newer and upstream python macros
- clean the spec by removing mention of old mandriva hack
- remove old python macros

* Sat Feb 26 2011 Nicolas Vigier <boklm@mageia.org> 1.9.9-1.mga1
+ Revision: 60148
- version 1.9.9

* Fri Jan 28 2011 Nicolas Vigier <boklm@mageia.org> 1.9.8-1.mga1
+ Revision: 42505
- version 1.9.8

* Thu Jan 27 2011 Nicolas Vigier <boklm@mageia.org> 1.9.7-1.mga1
+ Revision: 42188
- version 1.9.7

* Mon Jan 17 2011 Olivier Blin <blino@mageia.org> 1.9.6-2.mga1
+ Revision: 20916
- rebuild with new python

* Thu Jan 13 2011 Nicolas Vigier <boklm@mageia.org> 1.9.6-1.mga1
+ Revision: 7984
- version 1.9.6

* Wed Jan 12 2011 Olivier Blin <blino@mageia.org> 1.9.5-1.mga1
+ Revision: 6829
- install as mgarepo, not repsys
- do not conflict with repsys anymore
- 1.9.5

  + Nicolas Vigier <boklm@mageia.org>
  - mgarepo version 1.9.4
  - add conflict with repsys
  - cleaning
  - repsys package renamed to mgarepo
  - version 1.9.2

  + Michael Scherer <misc@mageia.org>
  - remove rest of Mandriva reference

* Tue Jan 04 2011 Nicolas Vigier <boklm@mageia.org> 1:1.9.1-1mdv2010.0
+ Revision: 120
- version 1.9.1
- version 1.9
- add patch from blino to enable binrepo in create-srpm
- imported package repsys
