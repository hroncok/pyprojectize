Name:           ufw
Version:        0.35
Release:        33%{?dist}
Summary:        Uncomplicated Firewall

License:        GPL-3.0-only
URL:            https://launchpad.net/%{name}
Source0:        https://launchpad.net/%{name}/%{version}/%{version}/+download/ufw-%{version}.tar.gz
# systemd service file
Source1:        ufw.service
# Install translations to the systemwide standard location for %%find_lang
Patch0:         ufw-0.35-trans-dir.patch
# Separate libexec_dir from state_dir because the state files must go into /var,
# whereas the scripts don't belong there (we install them to /usr/libexec
# instead). Upstream used to install everything into /lib/ufw, a hack to make
# separate /var work on Ubuntu, but /lib/ufw is /usr/lib/ufw in Fedora and that
# must not contain writable state data according to Fedora packaging guidelines.
# Now, upstream essentially uses state_dir only for libexec-type stuff, and has
# moved user.rules and user6.rules back to /etc, we move them back to /var/lib.
Patch1:         ufw-0.35-libexec-dir.patch
# Default to enabled, let systemd handle whether ufw is actually enabled
Patch2:         ufw-0.34~rc-default-enabled.patch
# Allow SSH connections by default
Patch3:         ufw-0.34~rc-default-allow-ssh.patch
# Define multicast protocols (mDNS, UPnP) as a normal protocol profile
# Use a managed rule instead of a "before" rule for default-allowing mDNS
# Do not allow UPnP by default at all, document in ufw.8 how it can be allowed
# Update the README file and the ufw.8 manpage according to the above changes
Patch4:         ufw-0.34~rc-multicast.patch
# Add protocol profiles for KDE Connect (#1257699) and Icecream (#1262009)
Patch5:         ufw-0.34~rc-additional-profiles.patch
# Fix check-requirements for Python 3.5, add 3.6, remove unsupported 3.2/3.3
Patch6:         ufw-0.35-python36.patch
# Change permissions of the *.rules files from 0640 to 0644
# Change permissions of the before.init and after.init hooks from 0640 to 0755
Patch7:         ufw-0.35-permissions.patch
# Don't prepend /usr/bin/env to sys.executable, which is always an absolute path
Patch8:         ufw-0.35-no-pointless-env.patch
# Switch to Python setuptools because Python 3.12 removed deprecated distutils
Patch9:         ufw-0.35-distutils-setuptools.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  iptables
BuildRequires:  gettext
BuildRequires:  systemd
BuildRequires:  make

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires:       systemd
Requires:       iptables

%description
The Uncomplicated Firewall(ufw) is a front-end for netfilter, which
aims to make it easier for people unfamiliar with firewall concepts.
Ufw provides a framework for managing netfilter as well as
manipulating the firewall.

%prep
%setup -q
%patch -P0 -p1 -b .trans-dir
%patch -P1 -p1 -b .libexec-dir
%patch -P2 -p1 -b .default-enabled
%patch -P3 -p1 -b .default-allow-ssh
%patch -P4 -p1 -b .multicast
rm -f profiles/*.multicast
%patch -P5 -p1 -b .additional-profiles
rm -f profiles/*.additional-profiles
%patch -P6 -p1 -b .python36
%patch -P7 -p1 -b .permissions
%patch -P8 -p1 -b .no-pointless-env
%patch -P9 -p1 -b .distutils-setuptools

%build
%py3_build

%install
%py3_install
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/ufw.service
%find_lang %{name}

%post
%systemd_post ufw.service

%preun
%systemd_preun ufw.service

%postun
%systemd_postun_with_restart ufw.service

%files -f %{name}.lang
%license COPYING
%doc ChangeLog README TODO AUTHORS
%{_sbindir}/ufw
%{_libexecdir}/ufw/
%{python3_sitelib}/ufw-%{version}-py*.egg-info
%{python3_sitelib}/ufw/
%{_datadir}/ufw/
%{_unitdir}/ufw.service
# config files under /etc, directly user-editable, should survive updates
%dir %{_sysconfdir}/ufw/
%config(noreplace) %{_sysconfdir}/ufw/after.init
%config(noreplace) %{_sysconfdir}/ufw/after.rules
%config(noreplace) %{_sysconfdir}/ufw/after6.rules
%config(noreplace) %{_sysconfdir}/ufw/before.init
%config(noreplace) %{_sysconfdir}/ufw/before.rules
%config(noreplace) %{_sysconfdir}/ufw/before6.rules
%config(noreplace) %{_sysconfdir}/ufw/sysctl.conf
%config(noreplace) %{_sysconfdir}/ufw/ufw.conf
%dir %{_sysconfdir}/ufw/applications.d/
%config(noreplace) %{_sysconfdir}/ufw/applications.d/ufw-*
%config(noreplace) %{_sysconfdir}/ufw/applications.d/fedora-*
%config(noreplace) %{_sysconfdir}/default/ufw
# state files under /var, not directly user-editable, but should survive updates
%dir %{_sharedstatedir}/ufw/
%config(noreplace) %{_sharedstatedir}/ufw/user.rules
%config(noreplace) %{_sharedstatedir}/ufw/user6.rules
%{_mandir}/man8/ufw-framework.8*
%{_mandir}/man8/ufw.8*


%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.35-32
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Robert Scheck <robert@fedoraproject.org> - 0.35-29
- Switch from deprecated distutils to setuptools for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.35-28
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.35-25
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.35-22
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.35-21
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.35-18
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.35-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.35-15
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.35-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.35-7
- Bump Release for official build

* Fri Dec 30 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.35-6
- Change permissions of the *.rules files from 0640 to 0644
- Change permissions of the before.init and after.init hooks from 0640 to 0755
- Don't prepend /usr/bin/env to sys.executable, which is always an absolute path

* Fri Dec 30 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.35-5
- Change URL to https
- Get the tarball directly from upstream rather than from Ubuntu
- Remove redundant "-n %%{name}-%%{version}" from %%setup
- Use %%py3_build and %%py3_install macros
- Add Python 3.6 to check-requirements

* Tue Nov 01 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.35-4
- Fix KDE Connect profile (port ranges can only be specified per protocol)

* Tue Nov 01 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.35-3
- Fix wrong path to user.rules and user6.rules in backend_iptables.py

* Tue Nov 01 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.35-2
- Fix wrong path to user.rules and user6.rules in ufw-init-functions

* Wed Oct 05 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.35-1
- Update to 0.35
- Drop upstreamed Ubuntu patches
- Drop setup-lp819600 patch, fixed differently upstream
- Rebase trans-dir patch
- Rebase libexec-dir patch, move user.rules and user6.rules back to /var/lib/ufw
- Fix check-requirements for Python 3.5 (and remove no longer supported 3.2/3.3)

* Thu Sep 10 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.11.rc
- Add protocol profiles for KDE Connect (#1257699) and Icecream (#1262009)

* Mon Aug 17 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.10.rc
- Change COPYING from %%doc to %%license

* Mon Aug 17 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.9.rc
- Rebuild

* Sat Jan 24 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.8.rc
- Use a managed rule instead of a "before" rule for default-allowing mDNS
- Do not allow UPnP by default at all, document in ufw.8 how it can be allowed
- Update the README file and the ufw.8 manpage according to the above changes

* Tue Jan 20 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.7.rc
- Define multicast protocols (mDNS, UPnP) as a normal protocol profile

* Fri Dec 12 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.6.rc
- Fix License tag (GPLv3 only, not GPLv3+, unfortunately)

* Mon Dec 08 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.5.rc
- Allow SSH connections by default

* Mon Dec 08 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.4.rc
- Fix config(noreplace) marking
- Install systemd service ufw.service
- Default to enabled, let systemd handle whether ufw is actually enabled
- Requires: systemd iptables
- Don't install README.* (patch backup files and developer documentation)
- Drop 0001-optimize-boot.patch, not useful in our setup

* Mon Dec 01 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.3.rc
- Install state data to /var/lib/ufw instead of /lib/ufw
- Install helper scripts to /usr/libexec/ufw instead of /lib/ufw

* Mon Dec 01 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.2.rc
- Enable translations: BR gettext, use %%find_lang
- Apply a patch to install translations to the standard location for %%find_lang

* Sat Nov 29 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.34-0.1.rc
- Upgrade to 0.34 RC from Ubuntu
- Apply the bugfix patches from Ubuntu packaging
- Better fix for lp#819600 (directory locations with python3 setup.py build)
- Use Python 3
- Clean up BuildRequires
- Specfile cleanups

* Tue Aug 02 2011 Nathan Owe <ndowens at fedoraproject dot org> 0.30.1-4
- Cleaned the file list a little more
- Added more detail about the patch file

* Tue Aug 02 2011 Nathan Owe <ndowens at fedoraproject dot org> 0.30.1-3
- Made the file list a little smaller

* Mon Aug 01 2011 Nathan Owe <ndowens at fedoraproject dot org> 0.30.1-2
- Set dir ownership
- Patch to fix directory locations

* Sun Jul 31 2011 Nathan Owe <ndowens at fedoraproject dot org> 0.30.1-1
- Initial Release
