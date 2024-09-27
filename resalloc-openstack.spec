%global srcname resalloc-openstack
%global pkgname resalloc_openstack

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with python2
%global default_sitelib %python3_sitelib
%global python python3
%global pythonpfx python3
%else
%bcond_without python2
%global default_sitelib %python2_sitelib
%global python python2
%global pythonpfx python
%endif

Name:       %srcname
Summary:    Resource allocator scripts for OpenStack
Version:    9.8
Release:    4%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://github.com/praiskup/resalloc-openstack
BuildArch:  noarch


BuildRequires: %pythonpfx-devel
BuildRequires: %pythonpfx-setuptools
BuildRequires: %python-argparse-manpage

Requires: %pythonpfx-cinderclient
Requires: %pythonpfx-glanceclient
Requires: %pythonpfx-keystoneauth1
Requires: %pythonpfx-neutronclient
Requires: %pythonpfx-novaclient

Source0: https://github.com/praiskup/%name/releases/download/v%version/%name-%version.tar.gz

%description
Resource allocator spawner/terminator scripts for OpenStack virtual machines,
designed so they either allocate all the sub-resources, or nothing (in case of
some failure).  This is especially useful if working with older OpenStack
deployments which all the time keep orphaned servers, floating IPs, volumes,
etc. dangling around.

These scripts are primarily designed to be used with resalloc-server.rpm, but in
general might be used separately.


%prep
%setup -q


%build
%if %{with python2}
%py2_build
%else
%py3_build
%endif


%install
%if %{with python2}
%py2_install
%else
%py3_install
%endif


%check


%files
%license COPYING
%doc README
%{_bindir}/%{name}-*
%_mandir/man1/%{name}-*.1*
%{default_sitelib}/%{pkgname}
%{default_sitelib}/%{pkgname}-*.egg-info


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 9.8-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 9.8-2
- Rebuilt for Python 3.13

* Fri Mar 01 2024 Pavel Raiskup <praiskup@redhat.com> - 9.8-1
- new upstream release: https://github.com/praiskup/resalloc-openstack/releases/tag/v9.8

* Tue Feb 06 2024 Pavel Raiskup <praiskup@redhat.com> - 9.7-1
- new upstream release:
  https://github.com/praiskup/resalloc-openstack/releases/tag/v9.7

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 9.6-2
- Rebuilt for Python 3.12

* Wed Mar 22 2023 Pavel Raiskup <praiskup@redhat.com> - 9.6-1
- new upstream release, allow logging in with app credential

* Tue Mar 07 2023 Pavel Raiskup <praiskup@redhat.com> - 9.5-1
- new upstream release, the -new script has --security-group option

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Pavel Raiskup <praiskup@redhat.com> - 9.4-1
- new upstream release, compat fix for F37

* Tue Sep 20 2022 Pavel Raiskup <praiskup@redhat.com> - 9.3-1
- new upstream release
- adjust cleaning-up with the new `cmd_list` Resalloc feature
- more pedantic cleanup of volumes

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Pavel Raiskup <praiskup@redhat.com> - 8-1
- new upstream release, with two new cleanup scripts

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Pavel Raiskup <praiskup@redhat.com> - 7-1
- more aggressive volume detach/removal

* Tue Jun 25 2019 Pavel Raiskup <praiskup@redhat.com> - 6-1
- don't indefinitely wait for booting of ERRORed instances

* Thu Jun 13 2019 Pavel Raiskup <praiskup@redhat.com> - 5-2
- start using the released tarball
- more descriptive %%description

* Wed Jun 12 2019 Pavel Raiskup <praiskup@redhat.com> - 5-1
- compat for older novaclient

* Fri Apr 19 2019 Pavel Raiskup <praiskup@redhat.com> - 4-1
- work-around broken fedorainfracloud:
  https://pagure.io/fedora-infrastructure/issue/7711

* Thu Apr 18 2019 Pavel Raiskup <praiskup@redhat.com> - 3-2
- add missing Requires

* Thu Apr 18 2019 Pavel Raiskup <praiskup@redhat.com> - 3-1
- more solid VM termination
- dump verbosely what is going on

* Sat Mar 23 2019 Pavel Raiskup <praiskup@redhat.com> - 2-1
- support v3 connection API

* Wed Oct 31 2018 Pavel Raiskup <praiskup@redhat.com> - 1-1
- rebuild for Python 3.7

* Tue Jan 30 2018 Pavel Raiskup <praiskup@redhat.com> - 1.dev0-0
- first tagged release

* Wed Jan 10 2018 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-4
- add 'resalloc-openstack --nic' option
- 'resalloc-openstack-new --image' accepts image name, too

* Fri Oct 13 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-3
- fix the volume attaching

* Thu Oct 05 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-2
- new: add --key-pair-id option

* Thu Oct 05 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-1
- add handler explicitly for python2

* Wed Oct 04 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-0
- initial build
