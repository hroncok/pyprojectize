%if 0%{?rhel} >= 9
%bcond_with     shorewall
%else
%bcond_without  shorewall
%endif

# RHEL < 10 and Fedora < 40 use file context entries in /var/run
%if %{defined rhel} && 0%{?rhel} < 10
%define legacy_var_run 1
%endif
%if %{defined fedora} && 0%{?fedora} < 40
%define legacy_var_run 1
%endif

Name: fail2ban
Version: 1.1.0
Release: 3%{?dist}
Summary: Daemon to ban hosts that cause multiple authentication errors

License: GPL-2.0-or-later
URL: https://fail2ban.sourceforge.net
Source0: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
# Releases are signed by Serg G. Brester (sebres) <info AT sebres.de>.  The
# fingerprint can be found in a signature file:
#   gpg --list-packets fail2ban-1.0.2.tar.gz.asc | grep 'issuer fpr'
#
# The following commands can be used to fetch the signing key via fingerprint
# and extract it:
#   fpr=8738559E26F671DF9E2C6D9E683BF1BEBD0A882C
#   gpg --receive-keys $fpr
#   gpg -a --export-options export-minimal --export $fpr >gpgkey-$fpr.asc
Source2: gpgkey-8738559E26F671DF9E2C6D9E683BF1BEBD0A882C.asc
# SELinux policy
Source3: fail2ban.fc
Source4: fail2ban.if
Source5: fail2ban.te
Source6: Makefile

# Give up being PartOf iptables and ipset for now
# https://bugzilla.redhat.com/show_bug.cgi?id=1379141
# https://bugzilla.redhat.com/show_bug.cgi?id=1573185
Patch0: fail2ban-partof.patch
# default port in jail.conf is not compatible with firewalld-cmd syntax
# https://bugzilla.redhat.com/show_bug.cgi?id=1850164
Patch1: fail2ban-nftables.patch
# Work around encoding issues during tests
Patch2: https://github.com/fail2ban/fail2ban/commit/ab9d41e5309b417a3c7a84fa8f03cf4f93831f1b.patch


BuildArch: noarch

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: python-devel
BuildRequires: python-setuptools
# For testcases
BuildRequires: python-inotify
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# For testcases
BuildRequires: python3-inotify
%endif
# using a python3_version-based conditional does not work here, so
# this is a proxy for "Python version greater than 3.12". asyncore
# and asynchat were dropped from cpython core in 3.12, these modules
# make them available again. See:
# https://github.com/fail2ban/fail2ban/issues/3487
# https://bugzilla.redhat.com/show_bug.cgi?id=2219991
%if 0%{?fedora} > 38
BuildRequires: python3-pyasyncore
BuildRequires: python3-pyasynchat
%endif
BuildRequires: sqlite
BuildRequires: systemd
BuildRequires: selinux-policy-devel
BuildRequires: make
%if 0%{?fedora} >= 41
BuildRequires: bash-completion-devel
%else
BuildRequires: bash-completion
%endif
BuildRequires: gnupg2

# Default components
Requires: %{name}-firewalld = %{version}-%{release}
Requires: %{name}-sendmail = %{version}-%{release}
Requires: %{name}-server = %{version}-%{release}


%description
Fail2Ban scans log files and bans IP addresses that makes too many password
failures. It updates firewall rules to reject the IP address. These rules can
be defined by the user. Fail2Ban can read multiple log files such as sshd or
Apache web server ones.

Fail2Ban is able to reduce the rate of incorrect authentications attempts
however it cannot eliminate the risk that weak authentication presents.
Configure services to use only two factor or public/private authentication
mechanisms if you really want to protect services.

This is a meta-package that will install the default configuration.  Other
sub-packages are available to install support for other actions and
configurations.


%package selinux
Summary: SELinux policies for Fail2Ban
%{?selinux_requires}
%global modulename fail2ban
%global selinuxtype targeted

%description selinux
SELinux policies for Fail2Ban.


%package server
Summary: Core server component for Fail2Ban
%if 0%{?rhel} && 0%{?rhel} < 8
Requires: systemd-python
Requires: ipset
Requires: iptables
%else
Requires: python3-systemd
Requires: nftables
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires: (%{name}-selinux if selinux-policy-%{selinuxtype})
%else
Requires: %{name}-selinux
%endif
# see note above in BuildRequires section
%if 0%{?fedora} > 38
Requires: python3-pyasyncore
Requires: python3-pyasynchat
%endif

%description server
This package contains the core server components for Fail2Ban with minimal
dependencies.  You can install this directly if you want to have a small
installation and know what you are doing.


%package all
Summary: Install all Fail2Ban packages and dependencies
Requires: %{name}-firewalld = %{version}-%{release}
Requires: %{name}-hostsdeny = %{version}-%{release}
Requires: %{name}-mail = %{version}-%{release}
Requires: %{name}-sendmail = %{version}-%{release}
Requires: %{name}-server = %{version}-%{release}
%if %{with shorewall}
Requires: %{name}-shorewall = %{version}-%{release}
%endif
Requires: perl-interpreter
%if 0%{?rhel} && 0%{?rhel} < 8
Requires: python-inotify
# No python3 support for gamin so epel only
Requires: gamin-python
%else
Requires: python3-inotify
%endif
Requires: /usr/bin/whois

%description all
This package installs all of the Fail2Ban packages and dependencies.


%package firewalld
Summary: Firewalld support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: firewalld

%description firewalld
This package enables support for manipulating firewalld rules.  This is the
default firewall service in Fedora.


%package hostsdeny
Summary: Hostsdeny (tcp_wrappers) support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: ed
Requires: tcp_wrappers

%description hostsdeny
This package enables support for manipulating tcp_wrapper's /etc/hosts.deny
files.


%package tests
Summary: Fail2Ban testcases
Requires: %{name}-server = %{version}-%{release}

%description tests
This package contains Fail2Ban's testscases and scripts.


%package mail
Summary: Mail actions for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: /usr/bin/mail

%description mail
This package installs Fail2Ban's mail actions.  These are an alternative
to the default sendmail actions.


%package sendmail
Summary: Sendmail actions for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: /usr/sbin/sendmail

%description sendmail
This package installs Fail2Ban's sendmail actions.  This is the default
mail actions for Fail2Ban.


%if %{with shorewall}
%package shorewall
Summary: Shorewall support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: shorewall
Conflicts: %{name}-shorewall-lite

%description shorewall
This package enables support for manipulating shorewall rules.


%package shorewall-lite
Summary: Shorewall lite support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: shorewall-lite
Conflicts: %{name}-shorewall

%description shorewall-lite
This package enables support for manipulating shorewall rules.
%endif


%package systemd
Summary: Systemd journal configuration for Fail2Ban
Requires: %{name}-server = %{version}-%{release}

%description systemd
This package configures Fail2Ban to use the systemd journal for its log input
by default.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# this test uses smtpd which is removed in Python 3.12, rewriting it
# isn't trivial
%if 0%{?fedora} > 38
rm -f fail2ban/tests/action_d/test_smtp.py
%endif

# Use Fedora paths
sed -i -e 's/^before = paths-.*/before = paths-fedora.conf/' config/jail.conf

# SELinux sources
cp -p %SOURCE3 %SOURCE4 %SOURCE5 .

%if %{defined legacy_var_run}
sed -i 's|^/run/|/var/run/|' %{name}.fc
%endif

# 2to3 has been removed from setuptools and we already use the binary in
# %%prep.
sed -i "/use_2to3/d" setup.py


%build
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_build
%else
%py3_build
%endif
make -f %SOURCE6


%install
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_install
# Make symbolic link relative
ln -fs python2 %{buildroot}%{_bindir}/fail2ban-python
%else
%py3_install
ln -fs python3 %{buildroot}%{_bindir}/fail2ban-python
%endif

mkdir -p %{buildroot}%{_unitdir}
cp -p build/fail2ban.service %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_mandir}/man{1,5}
install -p -m 644 man/*.1 %{buildroot}%{_mandir}/man1
install -p -m 644 man/*.5 %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 files/fail2ban-logrotate %{buildroot}%{_sysconfdir}/logrotate.d/fail2ban
install -d -m 0755 %{buildroot}/run/fail2ban/
install -m 0600 /dev/null %{buildroot}/run/fail2ban/fail2ban.pid
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/fail2ban/
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 0644 files/fail2ban-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/fail2ban.conf

# Remove non-Linux actions
rm %{buildroot}%{_sysconfdir}/%{name}/action.d/*ipfw.conf
rm %{buildroot}%{_sysconfdir}/%{name}/action.d/{ipfilter,pf,ufw}.conf
rm %{buildroot}%{_sysconfdir}/%{name}/action.d/osx-*.conf

# Remove config files for other distros
rm -f %{buildroot}%{_sysconfdir}/fail2ban/paths-{arch,debian,freebsd,opensuse,osx}.conf

# firewalld configuration
cat > %{buildroot}%{_sysconfdir}/%{name}/jail.d/00-firewalld.conf <<EOF
# This file is part of the fail2ban-firewalld package to configure the use of
# the firewalld actions as the default actions.  You can remove this package
# (along with the empty fail2ban meta-package) if you do not use firewalld
[DEFAULT]
banaction = firewallcmd-rich-rules
banaction_allports = firewallcmd-rich-rules
EOF

# systemd journal configuration
cat > %{buildroot}%{_sysconfdir}/%{name}/jail.d/00-systemd.conf <<EOF
# This file is part of the fail2ban-systemd package to configure the use of
# the systemd journal as the default backend.  You can remove this package
# (along with the empty fail2ban meta-package) if you do not want to use the
# journal backend
[DEFAULT]
backend=systemd
EOF

# Remove installed doc, use doc macro instead
rm -r %{buildroot}%{_docdir}/%{name}

# SELinux
# install policy modules
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}

#BASH completion
COMPLETIONDIR=%{buildroot}$(pkg-config --variable=completionsdir bash-completion)
%__mkdir_p $COMPLETIONDIR
%__install -p -m 644 files/bash-completion $COMPLETIONDIR/fail2ban


%check
%if 0%{?rhel} && 0%{?rhel} < 8
%python2 bin/fail2ban-testcases --verbosity=2 --no-network
%else
%if 0%{?fedora} > 38
# testRepairDb does not work with sqlite 3.42.0+
# https://github.com/fail2ban/fail2ban/issues/3586
%python3 bin/fail2ban-testcases --verbosity=2 --no-network -i testRepairDb
%else
%python3 bin/fail2ban-testcases --verbosity=2 --no-network
%endif
%endif


%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%post server
%systemd_post fail2ban.service

%preun server
%systemd_preun fail2ban.service

%postun server
%systemd_postun_with_restart fail2ban.service


%files

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%license COPYING

%files server
%doc README.md TODO ChangeLog COPYING doc/*.txt
%{_bindir}/fail2ban-client
%{_bindir}/fail2ban-python
%{_bindir}/fail2ban-regex
%{_bindir}/fail2ban-server
%if 0%{?rhel} && 0%{?rhel} < 8
%{python2_sitelib}/*
%exclude %{python2_sitelib}/fail2ban/tests
%else
%{python3_sitelib}/*
%exclude %{python3_sitelib}/fail2ban/tests
%endif
%{_unitdir}/fail2ban.service
%{_datadir}/bash-completion/
%{_mandir}/man1/fail2ban.1*
%{_mandir}/man1/fail2ban-client.1*
%{_mandir}/man1/fail2ban-python.1*
%{_mandir}/man1/fail2ban-regex.1*
%{_mandir}/man1/fail2ban-server.1*
%{_mandir}/man5/*.5*
%config(noreplace) %{_sysconfdir}/fail2ban/
%exclude %{_sysconfdir}/fail2ban/action.d/complain.conf
%exclude %{_sysconfdir}/fail2ban/action.d/hostsdeny.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail-buffered.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail-whois.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail-whois-lines.conf
%exclude %{_sysconfdir}/fail2ban/action.d/sendmail-*.conf
%exclude %{_sysconfdir}/fail2ban/action.d/shorewall.conf
%exclude %{_sysconfdir}/fail2ban/jail.d/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/fail2ban
%{_tmpfilesdir}/fail2ban.conf
%dir %{_localstatedir}/lib/fail2ban/
%dir /run/%{name}/
%ghost %verify(not size mtime md5) /run/%{name}/%{name}.pid

%files all

%files firewalld
%config(noreplace) %{_sysconfdir}/fail2ban/jail.d/00-firewalld.conf

%files hostsdeny
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/hostsdeny.conf

%files tests
%{_bindir}/fail2ban-testcases
%{_mandir}/man1/fail2ban-testcases.1*
%if 0%{?rhel} && 0%{?rhel} < 8
%{python2_sitelib}/fail2ban/tests
%else
%{python3_sitelib}/fail2ban/tests
%endif

%files mail
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/complain.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail-buffered.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail-whois.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail-whois-lines.conf

%files sendmail
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/sendmail-*.conf

%if %{with shorewall}
%files shorewall
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/shorewall.conf

%files shorewall-lite
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/shorewall.conf
%endif

%files systemd
%config(noreplace) %{_sysconfdir}/fail2ban/jail.d/00-systemd.conf


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Nils Philippsen <nils@tiptoe.de> - 1.1.0-2
- Use SPDX license identifier
- Use https upstream URL

* Wed Jun 12 2024 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-1
- Update to 1.1.0 for Python 3.13 support.

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.2-16
- Rebuilt for Python 3.13

* Sat May 11 2024 Todd Zullinger <tmz@pobox.com> - 1.0.2-15
- Handle /var/run->/run transition in older Fedora and EPEL (RHBZ#2279054)

* Sun May 05 2024 Richard Shaw <hobbes1069@gmail.com> - 1.0.2-14
- Increment SELinux module version.
- Tweak selinux regex for /run/fail2ban.

* Thu Apr 25 2024 Richard Shaw <hobbes1069@gmail.com> - 1.0.2-13
- Add nftables patch and fix selinux /var/run->/run issue, fixes RHBZ#1850164
  and RHBZ#2272476.

* Thu Feb 22 2024 Orion Poplawski <orion@nwra.com> - 1.0.2-12
- Allow watch on more logfiles

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Adam Williamson <awilliam@redhat.com> - 1.0.2-9
- Require pyasynchat and pyasyncore with Python 3.12+
- Disable smtp tests on F39+ due to removal of smtpd from Python 3.12
- Disable db repair test on F39+ as it's broken with sqlite 3.42.0+

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Todd Zullinger <tmz@pobox.com> - 1.0.2-7
- exclude shorewall subpackage on epel9 (rhbz#2217649)

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.0.2-6
- Rebuilt for Python 3.12

* Tue Apr 04 2023 Orion Poplawski <orion@nwra.com> - 1.0.2-5
- Drop downstream python3.11 patch, upstream went with a different fix

* Sun Apr 02 2023 Todd Zullinger <tmz@pobox.com> - 1.0.2-4
- verify upstream source signature

* Thu Mar 30 2023 Orion Poplawski <orion@nwra.com> - 1.0.2-3
- Add upstream patch to remove warning about allowipv6 (bz#2160781)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.2-1
- Update to 1.0.2.

* Wed Nov 02 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-2
- Add patch for dovecot eating 100% CPU.

* Sun Oct 02 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-1
- Update to 1.0.1.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.11.2-13
- Rebuilt for Python 3.11

* Wed May 18 2022 Orion Poplawski <orion@nwra.com> - 0.11.2-12
- Fix SELinux policy to allow watch on var_log_t (bz#2083923)

* Fri Jan 28 2022 Orion Poplawski <orion@nwra.com> - 0.11.2-11
- Require /usr/bin/mail instead of mailx

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 26 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.11.2-9
- Fix CVE-2021-32749 RHBZ#1983223

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 0.11.2-7
- Rebuilt for Python 3.10

* Sun Jun 06 2021 Richard Shaw <hobbes1069@gmail.com> - 0.11.2-6
- Update selinux policy for Fedora 34+

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.11.2-5
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Richard Shaw <hobbes1069@gmail.com> - 0.11.2-2
- Add patch to deal with a new century in tests (2021).

* Tue Nov 24 2020 Richard Shaw <hobbes1069@gmail.com> - 0.11.2-1
- Update to 0.11.2.

* Fri Aug 28 2020 Richard Shaw <hobbes1069@gmail.com> - 0.11.1-10.2
- Create shorewall-lite subpackage package which conflicts with shorewall
  subpackage. Fixes RHBZ#1872759.

* Tue Jul 28 2020 Richard Shaw <hobbes1069@gmail.com> - 0.11.1-9.2
- Fix python2 requires for EPEL 7.

* Mon Jul 27 2020 Richard Shaw <hobbes1069@gmail.com> - 0.11.1-9
- Add conditonals back for EL 7 as it's being brought up to date.
- Add patch to deal with nftables not accepting ":" as a port separator.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-7
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Richard Shaw <hobbes1069@gmail.com> - 0.11.1-6
- Change default firewalld backend from ipset to rich-rules as ipset causes
  firewalld to use legacy iptables. Fixes RHBZ#1823746.
- Remove conditionals for EL versions less than 7.

* Thu Mar 19 2020 Richard Shaw <hobbes1069@gmail.com> - 0.11.1-5
- Update for Python 3.9.

* Wed Feb 26 2020 Orion Poplawski <orion@nwra.com> - 0.11.1-4
- Add SELinux policy

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Orion Poplawski <orion@nwra.com> - 0.11.1-2
- Move action.d/mail-whois-common.conf into fail2ban-server

* Tue Jan 14 2020 Orion Poplawski <orion@nwra.com> - 0.11.1-1
- Update to 0.11.1

* Tue Jan 14 2020 Orion Poplawski <orion@nwra.com> - 0.10.5-1
- Update to 0.10.5

* Thu Nov 21 2019 Orion Poplawski <orion@nwra.com> - 0.10.4-8
- Define banaction_allports for firewalld, update banaction (bz#1775175)
- Update sendmail-reject with TLSMTA & MSA port IDs (bz#1722625)

* Thu Oct 31 2019 Orion Poplawski <orion@nwra.com> - 0.10.4-7
- Remove config files for other distros (bz#1533113)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.4-2
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Oct 5 2018 Orion Poplawski <orion@nwra.com> - 0.10.4-1
- Update to 0.10.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Orion Poplawski <orion@nwra.com> - 0.10.3.1-2
- Remove PartOf ipset.service (bug #1573185)

* Tue Jun 19 2018 Orion Poplawski <orion@nwra.com> - 0.10.3.1-1
- Update to 0.10.3.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.7

* Wed Mar 28 2018 Orion Poplawski <orion@nwra.com> - 0.10.2-1
- Update to 0.10.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Orion Poplawski <orion@nwra.com> - 0.10.1-3
- Add upstream patch to fix ipset issue (bug #1525134)

* Sat Dec 30 2017 Orion Poplawski <orion@nwra.com> - 0.10.1-2
- Add upstream patch to fix buildroot issue

* Tue Nov 14 2017 Orion Poplawski <orion@cora.nwra.com> - 0.10.1-1
- Update to 0.10.1

* Wed Sep 20 2017 Orion Poplawski <orion@cora.nwra.com> - 0.10.0-1
- Update to 0.10.0

* Wed Aug 16 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-4
- Use BR /usr/bin/2to3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.9.7-2
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Wed Jul 12 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-1
- Update to 0.9.7

* Wed Feb 15 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-4
- Properly handle /run/fail2ban (bug #1422500)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-2
- Add upstream patch to fix fail2ban-regex with journal

* Fri Jan 6 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-1
- Update to 0.9.6
- Fix sendmail-auth filter (bug #1329919)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-5
- Rebuild for Python 3.6

* Fri Oct 7 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-4
- %%ghost /run/fail2ban
- Fix typo in shorewall description
- Move tests to -tests sub-package

* Mon Oct 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-3
- Add journalmatch entries for sendmail (bug #1329919)

* Mon Oct 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-2
- Give up being PartOf iptables to allow firewalld restarts to work
  (bug #1379141)

* Mon Oct 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-1
- Add patch to fix failing test

* Sun Sep 25 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-1
- Update to 0.9.5
- Drop mysql patch applied upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 5 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-5
- Fix python3 usage (bug #1324113)

* Sun Mar 27 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-4
- Use %%{_tmpfilesdir} for systemd tmpfile config

* Wed Mar 9 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-3
- No longer need to add After=firewalld.service (bug #1301910)

* Wed Mar 9 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-2
- Fix mariadb/mysql log handling

* Wed Mar 9 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-1
- Update to 0.9.4
- Use mariadb log path by default

* Tue Feb 23 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-3
- Use python3 (bug #1282498)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-1
- Update to 0.9.3
- Cleanup spec, use new python macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-1
- Update to 0.9.2

* Mon Mar 16 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-4
- Do not load user paths for fail2ban-{client,server} (bug #1202151)

* Sun Feb 22 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-3
- Do not use systemd by default

* Fri Nov 28 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-2
- Fix php-url-fopen logpath (bug #1169026)

* Tue Oct 28 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-1
- Update to 0.9.1

* Fri Aug 15 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-8
- Add patch to fix tests

* Fri Aug 8 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-8
- Fix log paths for some jails (bug #1128152)

* Mon Jul 21 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-7
- Use systemd for EL7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-5
- Require mailx for /usr/bin/mail

* Thu Mar 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-4
- Need empty %%files to produce main and -all package

* Wed Mar 19 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-3
- Split into sub-packages for different components
- Enable journal filter by default (bug #985567)
- Enable firewalld action by default (bug #1046816)
- Add upstream patch to fix setting loglevel in fail2ban.conf
- Add upstream patches to fix tests in mock, run tests

* Tue Mar 18 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-2
- Use Fedora paths
- Start after firewalld (bug #1067147)

* Mon Mar 17 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9-1
- Update to 0.9

* Tue Sep 24 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.3.git1f1a561
- Update to current 0.9 git branch
- Rebase init patch, drop jail.d and notmp patch applied upstream

* Fri Aug 9 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.2.gitd529151
- Ship jail.conf(5) man page
- Ship empty /etc/fail2ban/jail.d directory

* Thu Aug 8 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.1.gitd529151
- Update to 0.9 git branch
- Rebase patches
- Require systemd-python for journal support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-1
- Update to 0.8.10 security release
- Use upstream provided systemd files
- Drop upstreamed patches, rebase log2syslog and notmp patches

* Fri Mar 15 2013 Orion Poplawski <orion@cora.nwra.com> - 0.8.8-4
- Use systemd init for Fedora 19+ (bug #883158)

* Thu Feb 14 2013 Orion Poplawski <orion@cora.nwra.com> - 0.8.8-3
- Add patch from upstream to fix module imports (Bug #892365)
- Add patch from upstream to UTF-8 characters in syslog (Bug #905097)
- Drop Requires: tcp_wrappers and shorewall (Bug #781341)

* Fri Jan 18 2013 Orion Poplawski <orion@cora.nwra.com> - 0.8.8-2
- Add patch to prevent sshd blocks of successful logins for systems that use
  sssd or ldap

* Mon Dec 17 2012 Orion Poplawski <orion@cora.nwra.com> - 0.8.8-1
- Update to 0.8.8 (CVE-2012-5642 Bug #887914)

* Thu Oct 11 2012 Orion Poplawski <orion@cora.nwra.com> - 0.8.7.1-1
- Update to 0.8.7.1
- Drop fd_cloexec, pyinotify, and examplemail patches fixed upstream
- Rebase sshd and notmp patches
- Use _initddir macro

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr  9 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.4-27
- Move tmp files to /var/lib (suggested by Phil Anderson).
- Enable inotify support (by Jonathan Underwood).
- Fixes RH bugs #669966, #669965, #551895, #552947, #658849, #656584.

* Sun Feb 14 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.4-24
- Patch by Jonathan G. Underwood <jonathan.underwood@gmail.com> to
  cloexec another fd leak.

* Fri Sep 11 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.4-23
- update to 0.8.4.

* Wed Sep  2 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.3-22
- Update to a newer svn snapshot to fix python 2.6 issue.

* Thu Aug 27 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.3-21
- Log to syslog (RH bug #491983). Also deals with RH bug #515116.
- Check inodes of log files (RH bug #503852).

* Sat Feb 14 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.3-18
- Fix CVE-2009-0362 (Fedora bugs #485461, #485464, #485465, #485466).

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8.3-17
- Rebuild for Python 2.6

* Sun Aug 24 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.3-16
- Update to 0.8.3.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8.2-15
- fix license tag

* Thu Mar 27 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.2-14
- Close on exec fixes by Jonathan Underwood.

* Sun Mar 16 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.2-13
- Add %%{_localstatedir}/run/fail2ban (David Rees).

* Fri Mar 14 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.2-12
- Update to 0.8.2.

* Thu Jan 31 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.8.1-11
- Move socket file from /tmp to /var/run to prevent SElinux from stopping
  fail2ban from starting (BZ #429281)
- Change logic in init file to start with -x to remove the socket file in case
  of unclean shutdown

* Wed Aug 15 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.1-10
- Update to 0.8.1.
- Remove patch fixing CVE-2007-4321 (upstream).
- Remove AllowUsers patch (upstream).
- Add dependency to gamin-python.

* Thu Jun 21 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-9
- Fix remote log injection (no CVE assignment yet).

* Sun Jun  3 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-8
- Also trigger on non-AllowUsers failures (Jonathan Underwood
  <jonathan.underwood@gmail.com>).

* Wed May 23 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-7
- logrotate should restart fail2ban (Zing <zing@fastmail.fm>).
- send mail to root; logrotate (Jonathan Underwood
  <jonathan.underwood@gmail.com>)

* Sat May 19 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-4
- Update to 0.8.0.
- enable ssh by default, fix log file for ssh scanning, adjust python
  dependency (Jonathan Underwood <jonathan.underwood@gmail.com>)

* Sat Dec 30 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.2-3
- Remove forgotten condrestart.

* Fri Dec 29 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.2-2
- Move /usr/lib/fail2ban to %%{_datadir}/fail2ban.
- Don't default chkconfig to enabled.
- Add dependencies on service/chkconfig.
- Use example iptables/ssh config as default config.

* Mon Dec 25 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.2-1
- Initial build.
