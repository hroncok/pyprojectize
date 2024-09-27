%global tftpboot_dir %{_sharedstatedir}/tftpboot/

%global commit 700eb5bdfb28baba4de5e4083bec9e132a763bcb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global selinuxtype targeted

Name:           cobbler
Version:        3.3.6
Release:        1%{?dist}
Summary:        Boot server configurator
URL:            https://cobbler.github.io/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        https://github.com/cobbler/cobbler/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        migrate-settings.sh
Source2:        %{name}.te
Source3:        %{name}.if
Source4:        %{name}.fc

# Do not run coverage tests
Patch0:         cobbler-nocov.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: %{py3_dist cheetah3}
BuildRequires: %{py3_dist distro}
BuildRequires: %{py3_dist netaddr}
BuildRequires: %{py3_dist pyyaml}
BuildRequires: %{py3_dist requests}
BuildRequires: %{py3_dist schema}
BuildRequires: %{py3_dist simplejson}
# For docs
BuildRequires: %{py3_dist sphinx}

# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires: (%{name}-selinux if selinux-policy-%{selinuxtype})

Requires: httpd
Requires: tftp-server
Requires: dosfstools
Requires: createrepo_c
Requires: rsync
Requires: xorriso
Requires: %{py3_dist cheetah3}
Requires: %{py3_dist distro}
Requires: %{py3_dist dnspython}
Requires: %{py3_dist file-magic}
Requires: %{py3_dist mod_wsgi}
Requires: %{py3_dist netaddr}
Requires: %{py3_dist pyyaml}
Requires: %{py3_dist requests}
Requires: %{py3_dist schema}
Requires: %{py3_dist simplejson}

Requires: genisoimage
# Not everyone wants bash-completion...?
Recommends: bash-completion
Requires: dnf-plugins-core
# syslinux is only available on x86
Requires: (syslinux if (filesystem.x86_64 or filesystem.i686))
# grub2 efi stuff is only available on x86
Recommends: grub2-efi-ia32
Recommends: grub2-efi-x64
Recommends: logrotate
Recommends: %{py3_dist ldap}
Recommends: %{py3_dist librepo}
# https://github.com/cobbler/cobbler/issues/1685
Requires: /sbin/service
Obsoletes: cobbler-web < 3.3

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Cobbler is a network install server. Cobbler supports PXE, ISO
virtualized installs, and re-installing existing Linux machines. The
last two modes use a helper tool, 'koan', that integrates with cobbler.
Cobbler's advanced features include importing distributions from DVDs
and rsync mirrors, kickstart templating, integrated yum mirroring, and
built-in DHCP/DNS Management. Cobbler has a XML-RPC API for integration
with other applications.


%package selinux
Summary:        SELinux policies for %{name}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
BuildArch:      noarch
%{?selinux_requires}


%description selinux
SELinux policies for %{name}.


%package tests
Summary:        Unit tests for cobbler
Requires:       cobbler = %{version}-%{release}

%description tests
Unit test files from the Cobbler project.


%package tests-containers
Summary:        Dockerfiles and scripts to setup testing containers
Requires:       cobbler = %{version}-%{release}

%description tests-containers
Dockerfiles and scripts to setup testing containers.


%prep
%autosetup -p1
mkdir -p selinux
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} selinux/


%generate_buildrequires
%pyproject_buildrequires


%build
. ./distro_build_configs.sh
%pyproject_wheel
make man

# SELinux
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp


%install
. ./distro_build_configs.sh
# bypass install errors ( don't chown in install step)
%pyproject_install

# cobbler
rm %{buildroot}%{_sysconfdir}/cobbler/cobbler.conf

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd_rotate %{buildroot}%{_sysconfdir}/logrotate.d/cobblerd

# Create data directories in tftpboot_dir
mkdir -p %{buildroot}%{tftpboot_dir}/{boot,etc,grub/system{,_link},images{,2},ppc,pxelinux.cfg,s390x}

# systemd - move to proper location
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd.service %{buildroot}%{_unitdir}

# ghosted files
touch %{buildroot}%{_sharedstatedir}/cobbler/web.ss

# migrate-settings.sh
install -p -m0755 %SOURCE1 %{buildroot}%{_datadir}/cobbler/bin/migrate-settings.sh

# SELinux
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if


%check
# These require an installed system with root access
#pytest -v


%pre
if [ $1 -ge 2 ]; then
    # package upgrade: backup configuration
    DATE=$(date "+%%Y%%m%%d-%%H%%M%%S")
    if [ ! -d "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}" ]; then
        mkdir -p "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
    for i in "config" "snippets" "templates" "triggers" "scripts"; do
        if [ -d "%{_sharedstatedir}/cobbler/${i}" ]; then
            cp -r "%{_sharedstatedir}/cobbler/${i}" "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
        fi
    done
    if [ -d %{_sysconfdir}/cobbler ]; then
        cp -r %{_sysconfdir}/cobbler "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
fi

%post
%systemd_post cobblerd.service
# Fixup permission for world readable settings files
chmod 640 %{_sysconfdir}/cobbler/settings.yaml
chmod 600 %{_sysconfdir}/cobbler/mongodb.conf
chmod 600 %{_sysconfdir}/cobbler/modules.conf
chmod 640 %{_sysconfdir}/cobbler/users.conf
chmod 640 %{_sysconfdir}/cobbler/users.digest
chmod 750 %{_sysconfdir}/cobbler/settings.d
chmod 640 %{_sysconfdir}/cobbler/settings.d/*
chgrp apache %{_sysconfdir}/cobbler/settings.yaml
chgrp apache %{_sysconfdir}/cobbler/users.conf
chgrp apache %{_sysconfdir}/cobbler/users.digest
chgrp apache %{_sysconfdir}/cobbler/settings.d
chgrp apache %{_sysconfdir}/cobbler/settings.d/*
# Change from apache
if [ -f %{_sharedstatedir}/cobbler/web.ss ]; then
    chown root %{_sharedstatedir}/cobbler/web.ss
fi

%posttrans
# Migrate pre-3.2.1 settings to settings.yaml
if [ -f %{_sysconfdir}/cobbler/settings.rpmsave ]; then
    echo warning: migrating old settings to settings.yaml
    mv %{_sysconfdir}/cobbler/settings.yaml{,.rpmnew}
    cp -a %{_sysconfdir}/cobbler/settings.{rpmsave,rpmorig}
    mv %{_sysconfdir}/cobbler/settings.{rpmsave,yaml}
    %{_datadir}/cobbler/bin/migrate-settings.sh
fi
# Add some missing options if needed
grep -q '^reposync_rsync_flags:' %{_sysconfdir}/cobbler/settings.yaml || echo -e '#ADDED:\nreposync_rsync_flags: "-rltDv --copy-unsafe-links"' >> %{_sysconfdir}/cobbler/settings.yaml
# Migrate pre-3 configuration data if needed
if [ -d %{_sharedstatedir}/cobbler/kickstarts -a $(find %{_sharedstatedir}/cobbler/collections -type f | wc -l) -eq 0  ]; then
    echo warning: migrating pre cobbler 3 configuration data
    %{_datadir}/cobbler/bin/migrate-data-v2-to-v3.py
fi

%preun
%systemd_preun cobblerd.service

%postun
%systemd_postun_with_restart cobblerd.service


%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   # the daemon needs to be restarted for the custom label to be applied
   %systemd_postun_with_restart cobblerd.service
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi


%files
%license COPYING
%doc AUTHORS.in README.md
%doc docs/developer-guide.rst docs/quickstart-guide.rst docs/installation-guide.rst
%dir %{_sysconfdir}/cobbler
%config(noreplace) %{_sysconfdir}/cobbler/auth.conf
%config(noreplace) %{_sysconfdir}/cobbler/boot_loader_conf/
%config(noreplace) %{_sysconfdir}/cobbler/cheetah_macros
%config(noreplace) %{_sysconfdir}/cobbler/dhcp.template
%config(noreplace) %{_sysconfdir}/cobbler/dhcp6.template
%config(noreplace) %{_sysconfdir}/cobbler/dnsmasq.template
%config(noreplace) %{_sysconfdir}/cobbler/genders.template
%config(noreplace) %{_sysconfdir}/cobbler/import_rsync_whitelist
%config(noreplace) %{_sysconfdir}/cobbler/iso/
%config(noreplace) %{_sysconfdir}/cobbler/logging_config.conf
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/cobbler/modules.conf
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/cobbler/mongodb.conf
%config(noreplace) %{_sysconfdir}/cobbler/named.template
%config(noreplace) %{_sysconfdir}/cobbler/ndjbdns.template
%config(noreplace) %{_sysconfdir}/cobbler/reporting/
%config(noreplace) %{_sysconfdir}/cobbler/rsync.exclude
%config(noreplace) %{_sysconfdir}/cobbler/rsync.template
%config(noreplace) %{_sysconfdir}/cobbler/secondary.template
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.yaml
%attr(750, root, apache) %dir %{_sysconfdir}/cobbler/settings.d
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/bind_manage_ipmi.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/manage_genders.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/nsupdate.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/settings.d/windows.settings
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/users.conf
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/cobbler/users.digest
%config(noreplace) %{_sysconfdir}/cobbler/version
%config(noreplace) %{_sysconfdir}/cobbler/windows/
%config(noreplace) %{_sysconfdir}/cobbler/zone.template
%config(noreplace) %{_sysconfdir}/cobbler/zone_templates/
%config(noreplace) %{_sysconfdir}/logrotate.d/cobblerd
%config(noreplace) /etc/httpd/conf.d/cobbler.conf
%{_bindir}/cobbler
%{_bindir}/cobbler-settings
%{_bindir}/cobbler-ext-nodes
%{_bindir}/cobblerd
%{_datadir}/bash-completion/
%dir %{_datadir}/cobbler
%{_datadir}/cobbler/bin
%{_mandir}/man1/cobbler.1*
%{_mandir}/man5/cobbler.conf.5*
%{_mandir}/man8/cobblerd.8*
%{python3_sitelib}/cobbler/
%{python3_sitelib}/cobbler*.dist-info
%{_unitdir}/cobblerd.service
%{tftpboot_dir}/*
/var/www/cobbler
%dir %{_sharedstatedir}/cobbler
%ghost %attr(0755,root,root) %{_sharedstatedir}/cobbler/backup/
%config(noreplace) %{_sharedstatedir}/cobbler/collections/
%config(noreplace) %{_sharedstatedir}/cobbler/distro_signatures.json
%config(noreplace) %{_sharedstatedir}/cobbler/grub_config/
%config(noreplace) %{_sharedstatedir}/cobbler/loaders/
%config(noreplace) %{_sharedstatedir}/cobbler/scripts/
%config(noreplace) %{_sharedstatedir}/cobbler/snippets/
%config(noreplace) %{_sharedstatedir}/cobbler/templates/
%config(noreplace) %{_sharedstatedir}/cobbler/triggers/
%ghost %attr(0644,root,root) %{_sharedstatedir}/cobbler/lock
# Currently used for cli auth
%ghost %attr(0644,root,root) %{_sharedstatedir}/cobbler/web.ss
/var/log/cobbler

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}

%files tests
%{_datadir}/cobbler/tests/

%files tests-containers
%{_datadir}/cobbler/docker/


%changelog
* Wed Jul 31 2024 Orion Poplawski <orion@nwra.com> - 3.3.6-1
- Update to 3.3.6

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.5-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Orion Poplawski <orion@nwra.com> - 3.3.5-1
- Update to 3.3.5

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.4-5
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.4-4
- Rebuilt for Python 3.13

* Sat Apr 27 2024 Orion Poplawski <orion@nwra.com> - 3.3.4-3
- Fix service name in selinux post install script

* Fri Apr 26 2024 Orion Poplawski <orion@nwra.com> - 3.3.4-2
- Test for existence of web.ss before chowning it (bz#2276860)

* Mon Feb 26 2024 Orion Poplawski <orion@nwra.com> - 3.3.4-1
- Update to 3.3.4
- Add local SELinux policy and allow cobbler to check service statuses,
  run mkfs.fat, and check for reposync and yumdownloader (bz#2251220)
- Change owndership of web.ss to root (bz#2247653)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Orion Poplawski <orion@nwra.com> - 3.3.3-6
- Add patch to fix build with Sphinx 7

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.3.3-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Python Maint <python-maint@redhat.com> - 3.3.3-2
- Rebuilt for Python 3.11

* Tue Jun 14 2022 Orion Poplawski <orion@nwra.com> - 3.3.3-1
- Update to 3.3.3

* Wed May 04 2022 Orion Poplawski <orion@nwra.com> - 3.3.2-2
- Drop setting cache_enabled no longer present in 3.3

* Sat Mar 12 2022 Orion Poplawski <orion@nwra.com> - 3.3.2-1
- Update to 3.3.2

* Tue Mar 01 2022 Orion Poplawski <orion@nwra.com> - 3.3.1-1
- Update to 3.3.1, removes web interface

* Tue Mar 01 2022 Orion Poplawski <orion@nwra.com> - 3.2.2-9
- Apply fixes for CVE-2021-45082/3
- Remove BR on python3-coverage

* Mon Jan 24 2022 Orion Poplawski <orion@nwra.com> - 3.2.2-8
- Fix posttrans script

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Orion Poplawski <orion@nwra.com> - 3.2.2-6
- Fix path to settings.yaml in scriptlet

* Thu Dec 09 2021 Orion Poplawski <orion@nwra.com> - 3.2.2-5
- Remove defunct get-loaders command

* Mon Nov 22 2021 Orion Poplawski <orion@nwra.com> - 3.2.2-4
- Add new keys to settings.yaml on migration or if missing
- Save original settings to settings.rpmorig

* Fri Oct 08 2021 Orion Poplawski <orion@nwra.com> - 3.2.2-3
- Fix dependencies (bz#2010567)

* Thu Sep 23 2021 Orion Poplawski <orion@nwra.com> - 3.2.2-2
- Migrate settings to settings.yaml
- Migrate pre-cobbler 3 data if needed
- Fix autoinstall_templates -> templates

* Thu Sep 23 2021 Orion Poplawski <orion@nwra.com> - 3.2.2-1
- Update to 3.2.2
- bz#2006840: CVE-2021-40323: Arbitrary file disclosure/Template Injection
- bz#2006897: CVE-2021-40324: Arbitrary file write via upload_log_data XMLRPC function
- bz#2006904: CVE-2021-40325: Authorization bypass allows modifying settings

* Wed Sep 22 2021 Orion Poplawski <orion@nwra.com> - 3.2.1-1
- Update to 3.2.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.0-5
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Orion Poplawski <orion@nwra.com> - 3.2.0-2
- Give root RW permission to /var/lib/cobbler/web.ss
- Fix SELinux cobbler logging issue

* Sat Oct 24 2020 Orion Poplawski <orion@nwra.com> - 3.2.0-1
- Update to 3.2.0

* Thu Sep 17 2020 Orion Poplawski <orion@nwra.com> - 3.1.2-4
- Add requires on python-distro and file

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Orion Poplawski <orion@nwra.com> - 3.1.2-2
- Fix apache configuration

* Fri May 29 2020 Orion Poplawski <orion@nwra.com> - 3.1.2-1
- Update to 3.1.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-4
- Rebuilt for Python 3.9

* Fri Feb 21 2020 Orion Poplawski <orion@nwra.com> - 3.1.1-3
- Add requires for python3-dns

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Orion Poplawski <orion@nwra.com> - 3.1.1-1
- Update to 3.1.1

* Tue Oct 22 2019 Orion Poplawski <orion@nwra.com> - 3.0.1-4
- Drop koan completely, including obsoletes.  It is a separate package now.

* Thu Oct 10 2019 Orion Poplawski <orion@nwra.com> - 3.0.1-3
- Require /sbin/service

* Tue Oct  8 2019 Orion Poplawski <orion@nwra.com> - 3.0.1-2
- Fix requires (requests instead of urlgrabber)
- Fix BR for EL8

* Mon Sep 09 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Fri Aug 30 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Mon Aug 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.8.5-0.1
- Update to 2.8.5 - pre-release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-5
- Fix empty man pages (BZ 1653415)

* Mon Nov 26 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-4
- Revert bind_manage_ipmi feature that is broken on 2.8

* Sun Nov 25 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-3
- Use pathfix.py to fix python shebangs

* Sun Nov 25 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-2
- Make koan require python2-ethtool (BZ 1638933)

* Sat Nov 24 2018 Orion Poplawski <orion@nwra.com> - 2.8.4-1
- Update to 2.8.4 (Fixes BZ 1613292, 1643860, 1614433, CVE-2018-1000226, CVE-2018-10931)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Orion Poplawski <orion@nwra.com> - 2.8.3-3
- koan requires urlgrabber

* Mon May 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.8.3-2
- Restore mergeability with epel7

* Mon May 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.8.3-1
- Update to 2.8.3 - security bugfix

* Wed Feb 21 2018 Orion Poplawski <orion@nwra.com> - 2.8.2-6
- Really fix django requires for Fedora 28+

* Tue Feb 20 2018 Orion Poplawski <orion@nwra.com> - 2.8.2-5
- Fix django requires for Fedora 28+

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.2-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.8.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Sep 18 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.2-1
- Update to 2.8.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-3
- Suppress logrotate output

* Mon Jun 12 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-2
- Fix module loading

* Wed May 24 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-1
- Update to 2.8.1

* Fri Feb 17 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-6
- Add patch to fix handling of multiple bridge interfaces

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-4
- Fix named patch

* Tue Jan 24 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-3
- Restart named-chroot service if used

* Fri Jan 20 2017 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-2
- Fix logrotate script for systemd (bug #1414617)

* Thu Dec 1 2016 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-1
- Update to 2.8.0
- Restructure spec file

* Thu Sep 1 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-11.gitf78af86
- Add patches to fix TEMPLATE_DIRS and use OrderedDict

* Thu Aug 11 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-10.gitf78af86
- Force IPv4 connections to cobblerd from web proxy

* Thu Jul 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-9.gitf78af86
- Suppress "virt-install --os-variant list" error messages

* Thu Jul 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-8.git5680bf8
- Fix handling unknown os variants with osinfo-query

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.11-7.git95749a6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-6.git95749a6
- Fix typo in koan/app.py

* Wed Jul 13 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-5.git13b035f
- Update to current git snapshot (bug #1276896)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 1 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-3
- Require dnf-plugins-core

* Sun Jan 24 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-2
- Require dnf-core-plugins instead of yum-utils for repoquery on Fedora 23+

* Sun Jan 24 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.11-1
- Update to 2.6.11
- Make cobbler arch specific to allow for arch specific requires

* Thu Oct 1 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.10-1
- Update to 2.6.10

* Mon Jun 22 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.9-1
- Update to 2.6.9

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.8-2
- Support django 1.8 in Fedora 22+

* Fri May 8 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.8-1
- Update to 2.6.8
- Backport upstream patch to fix centos version detection (bug #1201879)

* Tue Apr 28 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.7-3
- Add patch to fix virt-install support for F21+/EL7 (bug #1188424)

* Mon Apr 27 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.7-2
- Create and own directories in tftp_dir

* Wed Dec 31 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.7-1
- Update to 2.6.7

* Sun Oct 19 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.6-1
- Update to 2.6.6

* Fri Aug 15 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.5-1
- Update to 2.6.5

* Wed Aug 13 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.4-2
- Require Django >= 1.4

* Mon Aug 11 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.4-1
- Update to 2.6.4

* Fri Jul 18 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.3-1
- Update to 2.6.3

* Wed Jul 16 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.2-1
- Update to 2.6.2
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-1
- Update to 2.6.1
- Drop koan patch applied upstream

* Tue Apr 22 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-2
- Only require syslinux on x86

* Mon Apr 21 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-1
- Update to 2.6.0
