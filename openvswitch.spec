# Uncomment these for snapshot releases:
# commit0 is the git sha of the last commit
# date is the date YYYYMMDD of the snapshot
#%%global commit0 bd916d13dbb845746983a6780da772154df647ba
#%%global date 20180219
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# If wants to run tests while building, specify the '--with check'
# option. For example:
# rpmbuild -bb --with check openvswitch.spec

# Enable PIE, bz#955181
%global _hardened_build 1

# RHEL-7 doesn't define _rundir macro yet
# Fedora 15 onwards uses /run as _rundir
%if 0%{!?_rundir:1}
%define _rundir /run
%endif

# To disable DPDK support, specify '--without dpdk' when building
%bcond_without dpdk

# To disable AF_XDP support, specify '--without afxdp' when building
%bcond_without afxdp

# test-suite is broken for big endians
# https://bugzilla.redhat.com/show_bug.cgi?id=1105458#c10
# "ofproto-dpif - select group with dp_hash selection method" test is broken on armv7lh
# FIXME often tests fails on non-x86_64 architectures due to timing problems
%ifarch x86_64
%bcond_without check
%else
%bcond_with check
%endif
# option to run kernel datapath tests, requires building as root!
%bcond_with check_datapath_kernel
# option to build with libcap-ng, needed for running OVS as regular user
%bcond_without libcapng


%if 0%{?centos} == 7
# Carried over from 2.6.1 CBS builds, introduced to win over 2.6.90
Epoch:   1
%endif

Name: openvswitch
Summary: Open vSwitch daemon/database/utilities
URL: https://www.openvswitch.org/
Version: 3.4.0
Release: 2%{?dist}

# Nearly all of openvswitch is Apache-2.0.  The bugtool is LGPLv2+, and the
# lib/sflow*.[ch] files are SISSL
# datapath/ is GPLv2 (although not built into any of the binary packages)
License: Apache-2.0 AND LGPL-2.0-or-later AND SISSL

# NOTE: DPDK does not currently build for s390x
%define dpdkarches aarch64 i686 ppc64le x86_64

%if 0%{?commit0:1}
Source0: https://github.com/openvswitch/ovs/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0: https://www.openvswitch.org/releases/%{name}-%{version}.tar.gz
%endif
Source1: openvswitch.sysusers

# ovs-patches

# OVS (including OVN) backports (0 - 300)

BuildRequires: gcc gcc-c++ make
BuildRequires: autoconf automake libtool
BuildRequires: systemd-rpm-macros
BuildRequires: openssl openssl-devel
BuildRequires: python3-devel python3-six python3-sortedcontainers
BuildRequires: python3-sphinx
BuildRequires: desktop-file-utils
BuildRequires: groff-base graphviz
BuildRequires: unbound-devel
BuildRequires: systemtap-sdt-devel
%if %{with afxdp}
BuildRequires: libxdp-devel libbpf-devel numactl-devel
%endif
# make check dependencies
BuildRequires: procps-ng
%if 0%{?rhel} > 7 || 0%{?fedora}
BuildRequires: groff
BuildRequires: python3-pyOpenSSL
%endif

%if %{with check_datapath_kernel}
BuildRequires: nmap-ncat
# would be useful but not available in RHEL or EPEL
#BuildRequires: pyftpdlib
%endif

%if %{with libcapng}
BuildRequires: libcap-ng libcap-ng-devel
%endif

%if %{with dpdk}
%ifarch %{dpdkarches}
BuildRequires: dpdk-devel libpcap-devel numactl-devel
# Currently DPDK on Extras/AppStream includes the mlx{4,5} glue libraries, so
# libibverbs is needed to run the tests (make check).
%if 0%{?rhel}
BuildRequires: libibverbs >= 15
%endif
%endif
%endif

Requires: openssl iproute module-init-tools
#Upstream kernel commit 4f647e0a3c37b8d5086214128614a136064110c3
#Requires: kernel >= 3.15.0-0

%{?systemd_requires}
%{?sysusers_requires_compat}

Requires(post): /bin/sed
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Obsoletes: openvswitch-controller <= 0:2.1.0-1

%description
Open vSwitch provides standard network bridging functions and
support for the OpenFlow protocol for remote per-flow control of
traffic.

%package -n python3-openvswitch
Summary: Open vSwitch python3 bindings
License: Apache-2.0
Requires: python3 python3-six
Obsoletes: python-openvswitch < 2.10.0-6
Provides: python-openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-openvswitch
Python bindings for the Open vSwitch database

%package test
Summary: Open vSwitch testing utilities
License: Apache-2.0
BuildArch: noarch
Requires: python3-openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}

%description test
Utilities that are useful to diagnose performance and connectivity
issues in Open vSwitch setup.

%package testcontroller
Summary: Simple controller for testing OpenFlow setups
License: Apache-2.0
Requires: openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}

%description testcontroller
This controller enables OpenFlow switches that connect to it to act as
MAC-learning Ethernet switches.
It can be used for initial testing of OpenFlow networks.
It is not a necessary or desirable part of a production OpenFlow deployment.

%package devel
Summary: Open vSwitch OpenFlow development package (library, headers)
License: Apache-2.0

%description devel
This provides shared library, libopenswitch.so and the openvswitch header
files needed to build an external application.

%if 0%{?rhel} == 8 || ( 0%{?fedora} > 28 && 0%{?fedora} < 40)
%package -n network-scripts-%{name}
Summary: Open vSwitch legacy network service support
License: Apache-2.0
Requires: network-scripts
Supplements: (%{name} and network-scripts)

%description -n network-scripts-%{name}
This provides the ifup and ifdown scripts for use with the legacy network
service.
%endif

%package ipsec
Summary: Open vSwitch IPsec tunneling support
License: Apache-2.0
Requires: openvswitch libreswan
Requires: python3-openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}

%description ipsec
This package provides IPsec tunneling support for OVS tunnels.

%if %{with dpdk}
%ifarch %{dpdkarches}
%package dpdk
Summary: Open vSwitch OpenFlow development package (switch, linked with DPDK)
License: Apache-2.0
Supplements: %{name}

%description dpdk
This provides ovs-vswitchd linked with DPDK library.
%endif
%endif

%prep
%if 0%{?commit0:1}
%autosetup -n ovs-%{commit0} -p 1
%else
%autosetup -p 1
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?commit0:1}
# fix the snapshot unreleased version to be the released one.
sed -i.old -e "s/^AC_INIT(openvswitch,.*,/AC_INIT(openvswitch, %{version},/" configure.ac
%endif

# BZ#2055576
rm -f python/ovs/dirs.py

# version.h and version.py should not be included in release tarball
rm -f include/openvswitch/version.h python/ovs/version.py

./boot.sh
mkdir build build-dpdk
pushd build
ln -s ../configure
%configure \
%if %{with libcapng}
        --enable-libcapng \
%else
        --disable-libcapng \
%endif
        --disable-static \
        --enable-shared \
        --enable-ssl \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
        --enable-usdt-probes \
        --with-version-suffix=-%{release} \
%if %{with afxdp}
        --enable-afxdp
%else
        --disable-afxdp
%endif
make %{?_smp_mflags}
popd
%if %{with dpdk}
%ifarch %{dpdkarches}
pushd build-dpdk
ln -s ../configure
%configure \
%if %{with libcapng}
        --enable-libcapng \
%else
        --disable-libcapng \
%endif
        --disable-static \
        --enable-shared \
        --enable-ssl \
        --enable-usdt-probes \
        --with-dpdk=shared \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
        --libdir=%{_libdir}/openvswitch-dpdk \
        --program-suffix=.dpdk \
        --with-version-suffix=-%{release} \
%if %{with afxdp}
        --enable-afxdp
%else
        --disable-afxdp
%endif
make %{?_smp_mflags}
popd
%endif
%endif

/usr/bin/python3 build-aux/dpdkstrip.py \
        --dpdk \
        < rhel/usr_lib_systemd_system_ovs-vswitchd.service.in \
        > rhel/usr_lib_systemd_system_ovs-vswitchd.service

%install
rm -rf $RPM_BUILD_ROOT

%if %{with dpdk}
%ifarch %{dpdkarches}
make -C build-dpdk install-exec DESTDIR=$RPM_BUILD_ROOT

# We only need ovs-vswitchd-dpdk and some libraries for dpdk subpackage
rm -rf $RPM_BUILD_ROOT%{_bindir}
find $RPM_BUILD_ROOT%{_sbindir} -mindepth 1 -maxdepth 1 -not -name ovs-vswitchd.dpdk -delete
find $RPM_BUILD_ROOT%{_libdir}/openvswitch-dpdk -mindepth 1 -maxdepth 1 -not -name "libofproto*.so.*" -not -name "libopenvswitch*.so.*" -delete
%endif
%endif

make -C build install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_sbindir}/ovs-vswitchd $RPM_BUILD_ROOT%{_sbindir}/ovs-vswitchd.nodpdk
touch $RPM_BUILD_ROOT%{_sbindir}/ovs-vswitchd

install -d -m 0755 $RPM_BUILD_ROOT%{_rundir}/openvswitch
install -d -m 0750 $RPM_BUILD_ROOT%{_localstatedir}/log/openvswitch
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch

install -p -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysusersdir}/openvswitch.conf

install -p -D -m 0644 rhel/usr_lib_udev_rules.d_91-vfio.rules \
        $RPM_BUILD_ROOT%{_udevrulesdir}/91-vfio.rules

install -p -D -m 0644 \
        rhel/usr_share_openvswitch_scripts_systemd_sysconfig.template \
        $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/openvswitch

for service in openvswitch ovsdb-server ovs-vswitchd ovs-delete-transient-ports \
               openvswitch-ipsec; do
        install -p -D -m 0644 \
                        rhel/usr_lib_systemd_system_${service}.service \
                        $RPM_BUILD_ROOT%{_unitdir}/${service}.service
done

install -m 0755 rhel/etc_init.d_openvswitch \
        $RPM_BUILD_ROOT%{_datadir}/openvswitch/scripts/openvswitch.init

install -p -D -m 0644 rhel/etc_openvswitch_default.conf \
        $RPM_BUILD_ROOT/%{_sysconfdir}/openvswitch/default.conf

install -p -D -m 0644 rhel/etc_logrotate.d_openvswitch \
        $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/openvswitch

install -m 0644 vswitchd/vswitch.ovsschema \
        $RPM_BUILD_ROOT/%{_datadir}/openvswitch/vswitch.ovsschema

%if ( 0%{?rhel} && 0%{?rhel} < 9 ) || ( 0%{?fedora} && 0%{?fedora} < 40)
install -d -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts/
install -p -m 0755 rhel/etc_sysconfig_network-scripts_ifdown-ovs \
        $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts/ifdown-ovs
install -p -m 0755 rhel/etc_sysconfig_network-scripts_ifup-ovs \
        $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts/ifup-ovs
%endif

install -d -m 0755 $RPM_BUILD_ROOT%{python3_sitelib}
cp -a $RPM_BUILD_ROOT/%{_datadir}/openvswitch/python/ovstest \
        $RPM_BUILD_ROOT%{python3_sitelib}

# Build the JSON C extension for the Python lib (#1417738)
pushd python
(
export CPPFLAGS="-I ../build/include -I ../include"
export LDFLAGS="%{__global_ldflags} -L $RPM_BUILD_ROOT%{_libdir}"
%py3_build
%pyproject_install
[ -f "$RPM_BUILD_ROOT/%{python3_sitearch}/ovs/_json$(python3-config --extension-suffix)" ]
)
popd

rm -rf $RPM_BUILD_ROOT/%{_datadir}/openvswitch/python/

install -d -m 0755 $RPM_BUILD_ROOT/%{_sharedstatedir}/openvswitch

install -d -m 0755 $RPM_BUILD_ROOT%{_prefix}/lib/firewalld/services/

install -p -D -m 0755 \
        rhel/usr_share_openvswitch_scripts_ovs-systemd-reload \
        $RPM_BUILD_ROOT%{_datadir}/openvswitch/scripts/ovs-systemd-reload

touch $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch/conf.db
# The db needs special permission as IPsec Pre-shared keys are stored in it.
chmod 0640 $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch/conf.db
touch $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch/system-id.conf

# remove unpackaged files
rm -f $RPM_BUILD_ROOT/%{_bindir}/ovs-benchmark \
        $RPM_BUILD_ROOT/%{_bindir}/ovs-docker \
        $RPM_BUILD_ROOT/%{_bindir}/ovs-parse-backtrace \
        $RPM_BUILD_ROOT/%{_sbindir}/ovs-vlan-bug-workaround \
        $RPM_BUILD_ROOT/%{_mandir}/man1/ovs-benchmark.1* \
        $RPM_BUILD_ROOT/%{_mandir}/man8/ovs-vlan-bug-workaround.8*

# remove ovn unpackages files
rm -f $RPM_BUILD_ROOT%{_bindir}/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/ovn*
rm -f $RPM_BUILD_ROOT%{_datadir}/openvswitch/ovn*
rm -f $RPM_BUILD_ROOT%{_datadir}/openvswitch/scripts/ovn*
rm -f $RPM_BUILD_ROOT%{_includedir}/ovn/*

%check
for dir in build \
%if %{with dpdk}
%ifarch %{dpdkarches}
build-dpdk \
%endif
%endif
; do
pushd $dir
%if %{with check}
    touch resolv.conf
    export OVS_RESOLV_CONF=$(pwd)/resolv.conf
    if make check TESTSUITEFLAGS='%{_smp_mflags}' ||
       make check TESTSUITEFLAGS='--recheck' ||
       make check TESTSUITEFLAGS='--recheck'; then :;
    else
        cat tests/testsuite.log
        exit 1
    fi
%endif
%if %{with check_datapath_kernel}
    if make check-kernel RECHECK=yes; then :;
    else
        cat tests/system-kmod-testsuite.log
        exit 1
    fi
%endif
popd
done

%preun
%if 0%{?systemd_preun:1}
    %systemd_preun %{name}.service
%else
    if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
        /bin/systemctl --no-reload disable %{name}.service >/dev/null 2>&1 || :
        /bin/systemctl stop %{name}.service >/dev/null 2>&1 || :
    fi
%endif

%pre
%sysusers_create_compat %{SOURCE1}
[ -L %{_sbindir}/ovs-vswitchd ] || rm -f %{_sbindir}/ovs-vswitchd

%post
%{_sbindir}/update-alternatives --install %{_sbindir}/ovs-vswitchd \
  ovs-vswitchd %{_sbindir}/ovs-vswitchd.nodpdk 10
if [ $1 -eq 1 ]; then
    sed -i 's:^#OVS_USER_ID=:OVS_USER_ID=:' /etc/sysconfig/openvswitch

    sed -i \
        's@OVS_USER_ID="openvswitch:openvswitch"@OVS_USER_ID="openvswitch:hugetlbfs"@'\
        /etc/sysconfig/openvswitch
fi
chown -R openvswitch:openvswitch /etc/openvswitch

%if 0%{?systemd_post:1}
    %systemd_post %{name}.service
%else
    # Package install, not upgrade
    if [ $1 -eq 1 ]; then
        /bin/systemctl daemon-reload >dev/null || :
    fi
%endif

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove ovs-vswitchd %{_sbindir}/ovs-vswitchd.nodpdk
fi
%if 0%{?systemd_postun:1}
    %systemd_postun %{name}.service
%else
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
%endif

%if %{with dpdk}
%ifarch %{dpdkarches}
%post dpdk
if grep -Fqw sse4_1 /proc/cpuinfo; then
    priority=20
else
    echo "Warning: the CPU doesn't support SSE 4.1, dpdk support is not enabled." >&2
    priority=5
fi
%{_sbindir}/update-alternatives --install %{_sbindir}/ovs-vswitchd \
  ovs-vswitchd %{_sbindir}/ovs-vswitchd.dpdk $priority

%postun dpdk
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove ovs-vswitchd %{_sbindir}/ovs-vswitchd.dpdk
fi
%endif
%endif

%files -n python3-openvswitch
%{python3_sitearch}/ovs
%{python3_sitearch}/ovs-*.dist-info
%{_datadir}/openvswitch/bugtool-plugins/
%{_datadir}/openvswitch/scripts/ovs-bugtool-*
%{_datadir}/openvswitch/scripts/ovs-check-dead-ifs
%{_datadir}/openvswitch/scripts/ovs-vtep
%{_bindir}/ovs-dpctl-top
%{_sbindir}/ovs-bugtool
%{_mandir}/man8/ovs-dpctl-top.8*
%{_mandir}/man8/ovs-bugtool.8*
%doc LICENSE

%files test
%{_bindir}/ovs-pcap
%{_bindir}/ovs-tcpdump
%{_bindir}/ovs-tcpundump
%{_datadir}/openvswitch/scripts/usdt/*
%{_mandir}/man1/ovs-pcap.1*
%{_mandir}/man8/ovs-tcpdump.8*
%{_mandir}/man1/ovs-tcpundump.1*
%{_bindir}/ovs-test
%{_bindir}/ovs-vlan-test
%{_bindir}/ovs-l3ping
%{_mandir}/man8/ovs-test.8*
%{_mandir}/man8/ovs-vlan-test.8*
%{_mandir}/man8/ovs-l3ping.8*
%{python3_sitelib}/ovstest

%files testcontroller
%{_bindir}/ovs-testcontroller
%{_mandir}/man8/ovs-testcontroller.8*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/openvswitch/*
%{_includedir}/openflow/*
%exclude %{_libdir}/*.a

%if 0%{?rhel} == 8 || ( 0%{?fedora} > 28 && 0%{?fedora} < 40 )
%files -n network-scripts-%{name}
%{_sysconfdir}/sysconfig/network-scripts/ifup-ovs
%{_sysconfdir}/sysconfig/network-scripts/ifdown-ovs
%endif

%files ipsec
%{_datadir}/openvswitch/scripts/ovs-monitor-ipsec
%{_unitdir}/openvswitch-ipsec.service

%if %{with dpdk}
%ifarch %{dpdkarches}
%files dpdk
%{_libdir}/openvswitch-dpdk/
%ghost %{_sbindir}/ovs-vswitchd
%{_sbindir}/ovs-vswitchd.dpdk
%endif
%endif

%files
%defattr(-,openvswitch,openvswitch)
%dir %{_sysconfdir}/openvswitch
%{_sysconfdir}/openvswitch/default.conf
%config %ghost %verify(not owner group md5 size mtime) %{_sysconfdir}/openvswitch/conf.db
%ghost %attr(0600,-,-) %verify(not owner group md5 size mtime) %{_sysconfdir}/openvswitch/.conf.db.~lock~
%config %ghost %{_sysconfdir}/openvswitch/system-id.conf
%defattr(-,root,root)
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/openvswitch
%{_sysconfdir}/bash_completion.d/ovs-appctl-bashcomp.bash
%{_sysconfdir}/bash_completion.d/ovs-vsctl-bashcomp.bash
%config(noreplace) %{_sysconfdir}/logrotate.d/openvswitch
%{_unitdir}/openvswitch.service
%{_unitdir}/ovsdb-server.service
%{_unitdir}/ovs-vswitchd.service
%{_unitdir}/ovs-delete-transient-ports.service
%{_datadir}/openvswitch/scripts/openvswitch.init
%{_datadir}/openvswitch/scripts/ovs-lib
%{_datadir}/openvswitch/scripts/ovs-save
%{_datadir}/openvswitch/scripts/ovs-ctl
%{_datadir}/openvswitch/scripts/ovs-kmod-ctl
%{_datadir}/openvswitch/scripts/ovs-systemd-reload
%config %{_datadir}/openvswitch/local-config.ovsschema
%config %{_datadir}/openvswitch/vswitch.ovsschema
%config %{_datadir}/openvswitch/vtep.ovsschema
%{_bindir}/ovs-appctl
%{_bindir}/ovs-dpctl
%{_bindir}/ovs-ofctl
%{_bindir}/ovs-vsctl
%{_bindir}/ovsdb-client
%{_bindir}/ovsdb-tool
%{_bindir}/ovs-pki
%{_bindir}/vtep-ctl
%{_libdir}/*.so.*
%ghost %{_sbindir}/ovs-vswitchd
%{_sbindir}/ovs-vswitchd.nodpdk
%{_sbindir}/ovsdb-server
%{_mandir}/man1/ovsdb-client.1*
%{_mandir}/man1/ovsdb-server.1*
%{_mandir}/man1/ovsdb-tool.1*
%{_mandir}/man5/ovsdb.5*
%{_mandir}/man5/ovsdb.local-config.5*
%{_mandir}/man5/ovsdb-server.5.*
%{_mandir}/man5/ovs-vswitchd.conf.db.5*
%{_mandir}/man5/vtep.5*
%{_mandir}/man7/ovsdb-server.7*
%{_mandir}/man7/ovsdb.7*
%{_mandir}/man7/ovs-actions.7*
%{_mandir}/man7/ovs-fields.7*
%{_mandir}/man8/vtep-ctl.8*
%{_mandir}/man8/ovs-appctl.8*
%{_mandir}/man8/ovs-ctl.8*
%{_mandir}/man8/ovs-dpctl.8*
%{_mandir}/man8/ovs-kmod-ctl.8.*
%{_mandir}/man8/ovs-ofctl.8*
%{_mandir}/man8/ovs-pki.8*
%{_mandir}/man8/ovs-vsctl.8*
%{_mandir}/man8/ovs-vswitchd.8*
%{_mandir}/man8/ovs-parse-backtrace.8*
%{_udevrulesdir}/91-vfio.rules
%doc LICENSE NOTICE README.rst NEWS rhel/README.RHEL.rst
/var/lib/openvswitch
%attr(750,openvswitch,openvswitch) %verify(not owner group) /var/log/openvswitch
%ghost %attr(755,root,root) %verify(not owner group) %{_rundir}/openvswitch
%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} < 29)
%{_sysconfdir}/sysconfig/network-scripts/ifup-ovs
%{_sysconfdir}/sysconfig/network-scripts/ifdown-ovs
%endif
%{_sysusersdir}/openvswitch.conf

%changelog
* Tue Aug 27 2024 Timothy Redaelli <tredaelli@redhat.com> - 3.4.0-2
- Add -release to version

* Tue Aug 27 2024 Timothy Redaelli <tredaelli@redhat.com> - 3.4.0-1
- Update to 3.4.0 (#2291057)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 9 2024 Michael Santana <msantana@redhat.com> - 3.3.0-4
- Backport "tests: Fix compatibility issue with Python 3.13 in vlog.at." (#2250661)

* Fri Jun 07 2024 Timothy Redaelli <tredaelli@redhat.com> - 3.3.0-3
- Rebuilt with dpdk 23.11 (#2277736)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.13

* Wed Feb 21 2024 Timothy Redaelli <tredaelli@redhat.com> - 3.3.0-1
- Update to 3.3.0 (#2245052)
- Remove network-scripts subpackage starting from Fedora 40 (#2263335)
- Backport a simple fix to avoid "SSL db: implementation" test to fail

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Timothy Redaelli <tredaelli@redhat.com> - 3.2.1-1
- Update to 3.2.1 (#2245052)

* Wed Oct 04 2023 Timothy Redaelli <tredaelli@redhat.com> - 3.2.0-1
- Update to 3.2.0 (#2218328)
- Fix building with groff 1.23.0 (#2226068)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.1.1-4
- Rebuilt for Python 3.12

* Thu Jun 08 2023 Timothy Redaelli <tredaelli@redhat.com> - 3.1.1-3
- Backport "cpu: Fix cpuid check for some AMD processors." (#2211747)

* Mon May 22 2023 Timothy Redaelli <tredaelli@redhat.com> - 3.1.1-2
- Replace fgrep with grep -F (#2203601)
- Delete ovs-vswitchd, if it's not a link (#2188710)

* Wed Apr 12 2023 Timothy Redaelli <tredaelli@redhat.com> - 3.1.1-1
- Update for 3.1.1 (#2185071), includes fixes for CVE-2023-1668 (#2186245)

* Fri Mar 03 2023 Timothy Redaelli <tredaelli@redhat.com> - 3.1.0-1
- Update to 3.1.0 (#2150440)

* Wed Feb 01 2023 Timothy Redaelli <tredaelli@redhat.com> - 3.0.3-1
- Rebase to 3.0.3 (#2150440), includes fixes for CVE-2022-4337 (#2155379)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Timothy Redaelli <tredaelli@redhat.com> - 3.0.1-1
- Update to 3.0.1 (#2073644)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.17.0-5
- Rebuilt for Python 3.11

* Tue May 24 2022 Timothy Redaelli <tredaelli@redhat.com> - 2.17.0-4
- Create openvswitch-dpdk subpackage, install it by default (weak dependency),
  but enable it only if the CPU is new enough (#2081665)

* Mon Mar 28 2022 Timothy Redaelli <tredaelli@redhat.com> - 2.17.0-3
- Be sure dirs.py is updated (#2055576)

* Tue Mar 15 2022 Christian Glombek <lorbus@fedoraproject.org> - 2.17.0-2
- Provide a sysusers.d file to get user() and group() provides
  (see https://fedoraproject.org/wiki/Changes/Adopting_sysusers.d_format).

* Fri Mar 11 2022 Timothy Redaelli <tredaelli@redhat.com> - 2.17.0-1
- Update to 2.17.0 (#1978767)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 22 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.16.0-1
- Update to 2.16.0 (#1978767)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.15.0-8
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.15.0-6
- Rebuilt for Python 3.10

* Wed Feb 24 2021 Timothy Redaelli <tredaelli@redhat.com> - 2.15.0-5
- Move scripts that requires python in python3-openvswitch (#1901144)

* Tue Feb 23 2021 Timothy Redaelli <tredaelli@redhat.com> - 2.15.0-4
- Add openvswitch-testcontroller subpackage since it's required by mininet (#1914605)

* Mon Feb 22 2021 Timothy Redaelli <tredaelli@redhat.com> - 2.15.0-3
- Add python3-sortedcontainers as dependency (#1926202)

* Sun Feb 21 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.0-2
- Properly build with dpdk specifying shared option

* Wed Feb 17 2021 Timothy Redaelli <tredaelli@redhat.com> - 2.15.0-1
- Updated to 2.15.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Timothy Redaelli <tredaelli@redhat.com> - 2.14.0-3
- Backport patches for CVE-2015-8011 (#1899303)

* Mon Sep 14 2020 Aaron Conole <aconole@redhat.com> - 2.14.0-2
- Merge 'https://src.fedoraproject.org/rpms/openvswitch/pull-request/11'
  to set hugetlbfs group as a system group.

* Tue Sep 01 2020 Timothy Redaelli <tredaelli@redhat.com> - 2.14.0-1
- Updated to 2.14.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.13.0-2
- Rebuilt for Python 3.9

* Tue Apr 07 2020 Timothy Redaelli <tredaelli@redhat.com> - 2.13.0-1
- Updated to 2.13.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Flavio Leitner <fbl@redhat.com> - 2.12.0-1
- Updated to 2.12.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Charalampos Stratakis <cstratak@redhat.com> - 2.11.1-2
- Don't hard-code python's abi flags

* Wed May 08 2019 Timothy Redaelli <tredaelli@redhat.com> - 2.11.1-1
- Rebase to 2.11.1
- Ignore sortedcontainer python2.7 dependency (#1701921)

* Tue Apr 09 2019 Numan Siddique <numan.sididque@gmail.com> - 2.11.0-3
- Remove openvswitch-ovn* subpackages.

* Fri Mar 08 2019 Timothy Redaelli <tredaelli@redhat.com> - 2.11.0-2
- Add libmnl-devel as build requirement for RHEL/CentOS.

* Thu Feb 28 2019 Timothy Redaelli <tredaelli@redhat.com> - 2.11.0-1
- Rebase to 2.11.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.10.1-1
- Rebase to 2.10.1

* Wed Nov 21 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.10.0-4
- Fix C JSON library creation on Fedora Rawhide and exit if shared library cannot be created

* Fri Nov 02 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.10.0-3
- Build for any architectures

* Thu Oct 11 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.10.0-2
- Rebuilt for new unbound (#1638428)

* Fri Oct 05 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.10.0-1
- Align with "Fast Datapath" 2.10.0-10 (#1633555)

* Fri Sep 14 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.2-6
- Backport "Add ovs.compat module to python package" (#1619712)
- Backport a variant of "dhparams: Fix .c file generation with OpenSSL >= 1.1.1-pre9"

* Mon Aug 13 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.2-5
- Backport "Don't enable new TLS versions by default"

* Mon Aug 06 2018 Lubomir Rintel <lkundrak@v3.sk> - 2.9.2-4
- Split out the network-scripts

* Wed Aug 01 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.2-3
- Build OVS as shared library
- Build the C json native extension for Python (60x faster)
- Fix TPS VerifyTest (rpm -V) by do not verify md5, size and mtime of
  /etc/sysconfig/openvswitch
- Backport spec file modfications from "rhel: Use openvswitch user/group for
  the log directory"

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.2-1
- Update to OVS 2.9.2
- Backport a patch to make some tests pass on Fedora Rawhide

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.9.1-2
- Rebuilt for Python 3.7

* Tue May 22 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.1-1
- Update to OVS 2.9.1

* Tue Apr 10 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.0-4
- Align with with RHEL "Fast Datapath" 2.9.0-15
- Backport "rhel: don't drop capabilities when running as root"
- Change owner of /etc/openvswitch during upgrade
- Use DPDK as shared library

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.9.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 20 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.0-2
- Align totally with RHEL "Fast Datapath" channel 2.9.0-1

* Tue Feb 20 2018 Timothy Redaelli <tredaelli@redhat.com> - 2.9.0-1
- Update to Open vSwitch 2.9.0 and DPDK 17.11
- Align with RHEL "Fast Datapath" channel 2.9.0-1

* Fri Feb 09 2018 Aaron Conole <aconole@redhat.com> - 2.8.1-2
- Update to include 94cd8383e297 and 951d79e638ec from upstream

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.8.1-1
- Update to Open vSwitch 2.8.1

* Tue Sep 19 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.8.0-2
- Update DPDK to 17.05.2 (bugfixes)

* Mon Sep 04 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.8.0-1
- Update to Open vSwitch 2.8.0 and DPDK 17.05.1 (#1487971)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.2-1
- Update to Open vSwitch 2.7.2
- Add a symlink of the OCF script in the OCF resources folder

* Fri Jul 14 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.1-2
- Backport fix for CVE-2017-9263 (#1457327)
- Backport fix for CVE-2017-9265 (#1457335)

* Thu Jul 06 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.1-1
- Updated to Open vSwitch 2.7.1 and DPDK 16.11.2 (#1468234)

* Tue Jun 13 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.0-5
- Backport fix for CVE-2017-9264 (#1457329)

* Wed Jun 07 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.0-4
- Remove PYTHONCOERCECLOCALE=0 workaround and backport upstream patch (#1454364)

* Wed May 31 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.0-3
- Backport fix for CVE-2017-9214 (#1456797)
- Use %%autosetup instead of %%setup

* Mon May 29 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.0-2
- Install OVN firewalld rules

* Thu May 18 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.0-1
- Link statically with DPDK 16.11.1 (#1451476)
- Build OVS without DPDK support on all architectures not supported by DPDK
- Added python3-six to BuildRequires in order to launch python3 tests too
- Export PYTHONCOERCECLOCALE=0 in order to workaround an incompatibility
  between Python 3.6.0 (with PEP 538) on Fedora 26+ and testsuite (#1454364)
- Disable tests on armv7hl

* Fri Feb 24 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.7.0-0
- Updated to Open vSwitch 2.7.0 (#1426596)
- Enable DPDK support

* Thu Feb 16 2017 Timothy Redaelli <tredaelli@redhat.com> - 2.6.1-2
- Added python3-openvswitch and renamed python-openvswitch to python2-openvswitch

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Flavio Leitner <fbl@redhat.com> - 2.6.1-0
- Updated to Open vSwitch 2.6.1

* Tue Nov 01 2016 Aaron Conole <aconole@redhat.com> - 2.6.0-0
- Update to Open vSwitch 2.6.0
- Enable OVN

* Wed Aug 24 2016 Dan Horák <dan[at]danny.cz> - 2.5.0-4
- don't run the test-suite for big endian arches

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 15 2016 Panu Matilainen <pmatilai@redhat.com> - 2.5.0-2
- Remove unpackaged files instead of excluding (#1281913)

* Wed Mar 02 2016 Panu Matilainen <pmatilai@redhat.com> - 2.5.0-1
- Update to 2.5.0 (#1312617)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Flavio Leitner - 2.4.0-1
- updated to 2.4.0 (#1256171)

* Thu Jun 18 2015 Flavio Leitner - 2.3.2-1
- updated to 2.3.2 (#1233442)
- fixed to own /var/run/openvswitch directory (#1200887)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4.git20150327
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Flavio Leitner - 2.3.1-3.git20150327
- updated to 2.3.1-git4750c96
- commented out kernel requires
- added requires to procps-ng (testsuite #84)

* Wed Jan 14 2015 Flavio Leitner - 2.3.1-2.git20150113
- updated to 2.3.1-git3282e51

* Fri Dec 05 2014 Flavio Leitner - 2.3.1-1
- updated to 2.3.1

* Fri Nov 07 2014 Flavio Leitner - 2.3.0-3.git20141107
- updated to 2.3.0-git39ebb203

* Thu Oct 23 2014 Flavio Leitner - 2.3.0-2
- fixed to own conf.db and system-id.conf in /etc/openvswitch.
  (#1132707)

* Tue Aug 19 2014 Flavio Leitner - 2.3.0-1
- updated to 2.3.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Flavio Leitner - 2.1.2-4
- moved README.RHEL to be in the standard doc dir.
- added FAQ and NEWS files to the doc list.
- excluded PPC arch

* Thu Jun 12 2014 Flavio Leitner - 2.1.2-3
- removed ovsdbmonitor packaging

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Flavio Leitner - 2.1.2-1
- updated to 2.1.2

* Tue Mar 25 2014 Flavio Leitner - 2.1.0-1
- updated to 2.1.0
- obsoleted openvswitch-controller package
- requires kernel 3.15.0-0 or newer
  (kernel commit 4f647e0a3c37b8d5086214128614a136064110c3
   openvswitch: fix a possible deadlock and lockdep warning)
- ovs-lib: allow non-root users to check service status
  (upstream commit 691e47554dd03dd6492e00bab5bd6d215f5cbd4f)
- rhel: Add Patch Port support to initscripts
  (upstream commit e2bcc8ef49f5e51f48983b87ab1010f0f9ab1454)

* Mon Jan 27 2014 Flavio Leitner - 2.0.1-1
- updated to 2.0.1

* Mon Jan 27 2014 Flavio Leitner - 2.0.0-6
- create a -devel package
  (from Chris Wright <chrisw@redhat.com>)

* Wed Jan 15 2014 Flavio Leitner <fbl@redhat.com> - 2.0.0-5
- Enable DHCP support for internal ports
  (upstream commit 490db96efaf89c63656b192d5ca287b0908a6c77)

* Wed Jan 15 2014 Flavio Leitner <fbl@redhat.com> - 2.0.0-4
- disabled ovsdbmonitor packaging
  (upstream has removed the component)

* Wed Jan 15 2014 Flavio Leitner <fbl@redhat.com> - 2.0.0-3
- fedora package: fix systemd ordering and deps.
  (upstream commit b49c106ef00438b1c59876dad90d00e8d6e7b627)

* Wed Jan 15 2014 Flavio Leitner <fbl@redhat.com> - 2.0.0-2
- util: use gcc builtins to better check array sizes
  (upstream commit 878f1972909b33f27b32ad2ded208eb465b98a9b)

* Mon Oct 28 2013 Flavio Leitner <fbl@redhat.com> - 2.0.0-1
- updated to 2.0.0 (#1023184)

* Mon Oct 28 2013 Flavio Leitner <fbl@redhat.com> - 1.11.0-8
- applied upstream commit 7b75828bf5654c494a53fa57be90713c625085e2
  rhel: Option to create tunnel through ifcfg scripts.

* Mon Oct 28 2013 Flavio Leitner <fbl@redhat.com> - 1.11.0-7
- applied upstream commit 32aa46891af5e173144d672e15fec7c305f9a4f3
  rhel: Set STP of a bridge during bridge creation.

* Mon Oct 28 2013 Flavio Leitner <fbl@redhat.com> - 1.11.0-6
- applied upstream commit 5b56f96aaad4a55a26576e0610fb49bde448dabe
  rhel: Prevent duplicate ifup calls.

* Mon Oct 28 2013 Flavio Leitner <fbl@redhat.com> - 1.11.0-5
- applied upstream commit 79416011612541d103a1d396d888bb8c84eb1da4
  rhel: Return an exit value of 0 for ifup-ovs.

* Mon Oct 28 2013 Flavio Leitner <fbl@redhat.com> - 1.11.0-4
- applied upstream commit 2517bad92eec7e5625bc8b248db22fdeaa5fcde9
  Added RHEL ovs-ifup STP option handling

* Tue Oct 1 2013 Flavio Leitner <fbl@redhat.com> - 1.11.0-3
- don't use /var/lock/subsys with systemd (#1006412)

* Thu Sep 19 2013 Flavio Leitner <fbl@redhat.com> - 1.11.0-2
- ovsdbmonitor package is optional

* Thu Aug 29 2013 Thomas Graf <tgraf@redhat.com> - 1.11.0-1
- Update to 1.11.0

* Tue Aug 13 2013 Flavio Leitner <fbl@redhat.com> - 1.10.0-7
- Fixed openvswitch-nonetwork to start openvswitch.service (#996804)

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.10.0-6
- Perl 5.18 rebuild

* Tue Jul 23 2013 Thomas Graf <tgraf@redhat.com> - 1.10.0-5
- Typo

* Tue Jul 23 2013 Thomas Graf <tgraf@redhat.com> - 1.10.0-4
- Spec file fixes
- Maintain local copy of sysconfig.template

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.10.0-3
- Perl 5.18 rebuild

* Mon Jul 01 2013 Thomas Graf <tgraf@redhat.com> - 1.10.0-2
- Enable PIE (#955181)
- Provide native systemd unit files (#818754)

* Thu May 02 2013 Thomas Graf <tgraf@redhat.com> - 1.10.0-1
- Update to 1.10.0 (#958814)

* Thu Feb 28 2013 Thomas Graf <tgraf@redhat.com> - 1.9.0-1
- Update to 1.9.0 (#916537)

* Tue Feb 12 2013 Thomas Graf <tgraf@redhat.com> - 1.7.3-8
- Fix systemd service dependency loop (#818754)

* Fri Jan 25 2013 Thomas Graf <tgraf@redhat.com> - 1.7.3-7
- Auto-start openvswitch service on ifup/ifdown (#818754)
- Add OVSREQUIRES to allow defining OpenFlow interface dependencies

* Thu Jan 24 2013 Thomas Graf <tgraf@redhat.com> - 1.7.3-6
- Update to Open vSwitch 1.7.3

* Tue Nov 20 2012 Thomas Graf <tgraf@redhat.com> - 1.7.1-6
- Increase max fd limit to support 256 bridges (#873072)

* Thu Nov  1 2012 Thomas Graf <tgraf@redhat.com> - 1.7.1-5
- Don't create world writable pki/*/incomming directory (#845351)

* Thu Oct 25 2012 Thomas Graf <tgraf@redhat.com> - 1.7.1-4
- Don't add iptables accept rule for -p GRE as GRE tunneling is unsupported

* Tue Oct 16 2012 Thomas Graf <tgraf@redhat.com> - 1.7.1-3
- require systemd instead of systemd-units to use macro helpers (#850258)

* Tue Oct  9 2012 Thomas Graf <tgraf@redhat.com> - 1.7.1-2
- make ovs-vsctl timeout if daemon is not running (#858722)

* Mon Sep 10 2012 Thomas Graf <tgraf@redhat.com> - 1.7.1.-1
- Update to 1.7.1

* Fri Sep  7 2012 Thomas Graf <tgraf@redhat.com> - 1.7.0.-3
- add controller package containing ovs-controller

* Thu Aug 23 2012 Tomas Hozza <thozza@redhat.com> - 1.7.0-2
- fixed SPEC file so it comply with new systemd-rpm macros guidelines (#850258)

* Fri Aug 17 2012 Tomas Hozza <thozza@redhat.com> - 1.7.0-1
- Update to 1.7.0
- Fixed openvswitch-configure-ovskmod-var-autoconfd.patch because
  openvswitch kernel module name changed in 1.7.0
- Removed Source8: ovsdbmonitor-move-to-its-own-data-directory.patch
- Patches merged:
  - ovsdbmonitor-move-to-its-own-data-directory-automaked.patch
  - openvswitch-rhel-initscripts-resync.patch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Chris Wright <chrisw@redhat.com> - 1.4.0-5
- fix ovs network initscripts DHCP address acquisition (#803843)

* Tue Mar  6 2012 Chris Wright <chrisw@redhat.com> - 1.4.0-4
- make BuildRequires openssl explicit (needed on f18/rawhide now)

* Tue Mar  6 2012 Chris Wright <chrisw@redhat.com> - 1.4.0-3
- use glob to catch compressed manpages

* Thu Mar  1 2012 Chris Wright <chrisw@redhat.com> - 1.4.0-2
- Update License comment, use consitent macros as per review comments bz799171

* Wed Feb 29 2012 Chris Wright <chrisw@redhat.com> - 1.4.0-1
- Initial package for Fedora
