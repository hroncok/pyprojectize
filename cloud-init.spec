%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           cloud-init
Version:        24.2
Release:        %autorelease
Summary:        Cloud instance init scripts
License:        Apache-2.0 OR GPL-3.0-only
URL:            https://github.com/canonical/cloud-init

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        cloud-init-tmpfiles.conf

# Fix btrfs version check for btrfs 6.10+
# https://github.com/canonical/cloud-init/issues/5614
# not upstreamed as a PR due to Canonical CLA, remove when upstream
# has fixed it themselves
Patch:          0001-Fix-btrfs-version-check-for-btrfs-6.10.patch

BuildArch:      noarch

BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(systemd)

%if %{with tests}
BuildRequires:  iproute
BuildRequires:  passwd
BuildRequires:  procps-ng
# dnf is needed to make cc_ntp unit tests work
# https://bugs.launchpad.net/cloud-init/+bug/1721573
BuildRequires:  /usr/bin/dnf
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(passlib)
%endif

Requires:       dhcpcd

Requires:       hostname
Requires:       e2fsprogs
Requires:       iproute
Requires:       python3-libselinux
Requires:       policycoreutils-python3
Requires:       procps
Requires:       shadow-utils
Requires:       util-linux
Requires:       xfsprogs
# https://bugzilla.redhat.com/show_bug.cgi?id=1974262
Requires:       gdisk
Requires:       openssl

%{?systemd_requires}


%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.


%prep
%autosetup -p1

# Change shebangs
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
       -e 's|#!/usr/bin/python|#!/usr/bin/python3|' tools/* cloudinit/ssh_util.py

# Removing shebang manually because of rpmlint, will update upstream later
sed -i -e 's|#!/usr/bin/python||' cloudinit/cmd/main.py

# Use unittest from the standard library. unittest2 is old and being
# retired in Fedora. See https://bugzilla.redhat.com/show_bug.cgi?id=1794222
find tests/ -type f | xargs sed -i s/unittest2/unittest/
find tests/ -type f | xargs sed -i s/assertItemsEqual/assertCountEqual/


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '*'

# Generate cloud-config file
python3 tools/render-template --variant %{?rhel:rhel}%{!?rhel:fedora} > $RPM_BUILD_ROOT/%{_sysconfdir}/cloud/cloud.cfg

mkdir -p $RPM_BUILD_ROOT/var/lib/cloud

# /run/cloud-init needs a tmpfiles.d entry
mkdir -p $RPM_BUILD_ROOT/run/cloud-init
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d
cp -p tools/21-cloudinit.conf $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf

# installing man pages
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/
for man in cloud-id.1 cloud-init.1 cloud-init-per.1; do
    install -c -m 0644 doc/man/${man} ${RPM_BUILD_ROOT}%{_mandir}/man1/${man}
    chmod -x ${RPM_BUILD_ROOT}%{_mandir}/man1/*
done

# Put files in /etc/systemd/system in the right place
cp -a %{buildroot}/etc/systemd %{buildroot}/usr/lib
rm -rf %{buildroot}/etc/systemd


%check
%if %{with tests}
python3 -m pytest tests/unittests
%else
%py3_check_import cloudinit
%endif

%post
%systemd_post cloud-config.service cloud-config.target cloud-final.service cloud-init.service cloud-init.target cloud-init-local.service


%preun
%systemd_preun cloud-config.service cloud-config.target cloud-final.service cloud-init.service cloud-init.target cloud-init-local.service


%postun
%systemd_postun cloud-config.service cloud-config.target cloud-final.service cloud-init.service cloud-init.target cloud-init-local.service


%files -f %{pyproject_files}
%doc ChangeLog
%doc doc/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg
%dir               %{_sysconfdir}/cloud/cloud.cfg.d
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg.d/*.cfg
%doc               %{_sysconfdir}/cloud/cloud.cfg.d/README
%dir               %{_sysconfdir}/cloud/templates
%config(noreplace) %{_sysconfdir}/cloud/templates/*
%dir               %{_sysconfdir}/rsyslog.d
%config(noreplace) %{_sysconfdir}/rsyslog.d/21-cloudinit.conf
%{_udevrulesdir}/66-azure-ephemeral.rules
%{_unitdir}/cloud-config.service
%{_unitdir}/cloud-final.service
%{_unitdir}/cloud-init.service
%{_unitdir}/cloud-init-local.service
%{_unitdir}/cloud-config.target
%{_unitdir}/cloud-init.target
/usr/lib/systemd/system-generators/cloud-init-generator
%{_unitdir}/cloud-init-hotplugd.service
%{_unitdir}/cloud-init-hotplugd.socket
%{_unitdir}/sshd-keygen@.service.d/disable-sshd-keygen-if-cloud-init-active.conf
%{_tmpfilesdir}/%{name}.conf
%{_libexecdir}/%{name}
%{_bindir}/cloud-init*
%{_bindir}/cloud-id
%dir /run/cloud-init
%dir /var/lib/cloud
%{_datadir}/bash-completion/completions/cloud-init


%changelog
%autochangelog
