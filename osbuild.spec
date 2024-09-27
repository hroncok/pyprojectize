%global         forgeurl https://github.com/osbuild/osbuild
%global         selinuxtype targeted

Version:        129

%forgemeta

%global         pypi_name osbuild
%global         pkgdir %{_prefix}/lib/%{pypi_name}

Name:           %{pypi_name}
Release:        1%{?dist}
License:        Apache-2.0

URL:            %{forgeurl}

Source0:        %{forgesource}
BuildArch:      noarch
Summary:        A build system for OS images

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  systemd

Requires:       bash
Requires:       bubblewrap
Requires:       coreutils
Requires:       curl
Requires:       dnf
Requires:       e2fsprogs
Requires:       glibc
Requires:       policycoreutils
Requires:       qemu-img
Requires:       systemd
Requires:       skopeo
Requires:       tar
Requires:       util-linux
Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})

# This is required for `osbuild`, for RHEL-10 and above
# the stdlib toml package can be used instead
%if 0%{?rhel} < 10
Requires:       python3-tomli
%endif

# Turn off dependency generators for runners. The reason is that runners are
# tailored to the platform, e.g. on RHEL they are using platform-python. We
# don't want to pick up those dependencies on other platform.
%global __requires_exclude_from ^%{pkgdir}/(runners)/.*$

# Turn off shebang mangling on RHEL. brp-mangle-shebangs (from package
# redhat-rpm-config) is run on all executables in a package after the `install`
# section runs. The below macro turns this behavior off for:
#   - runners, because they already have the correct shebang for the platform
#     they're meant for, and
#   - stages and assemblers, because they are run within osbuild build roots,
#     which are not required to contain the same OS as the host and might thus
#     have a different notion of "platform-python".
# RHEL NB: Since assemblers and stages are not excluded from the dependency
# generator, this also means that an additional dependency on /usr/bin/python3
# will be added. This is intended and needed, so that in the host build root
# /usr/bin/python3 is present so stages and assemblers can be run.
%global __brp_mangle_shebangs_exclude_from ^%{pkgdir}/(assemblers|runners|stages)/.*$

%{?python_enable_dependency_generator}

%description
A build system for OS images

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A build system for OS images

%package        lvm2
Summary:        LVM2 support
Requires:       %{name} = %{version}-%{release}
Requires:       lvm2

%description lvm2
Contains the necessary stages and device host
services to build LVM2 based images.

%package        luks2
Summary:        LUKS2 support
Requires:       %{name} = %{version}-%{release}
Requires:       cryptsetup

%description luks2
Contains the necessary stages and device host
services to build LUKS2 encrypted images.

%package        ostree
Summary:        OSTree support
Requires:       %{name} = %{version}-%{release}
Requires:       ostree
Requires:       rpm-ostree

%description ostree
Contains the necessary stages, assembler and source
to build OSTree based images.

%package        selinux
Summary:        SELinux policies
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description    selinux
Contains the necessary SELinux policies that allows
osbuild to use labels unknown to the host inside the
containers it uses to build OS artifacts.

%package        tools
Summary:        Extra tools and utilities
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pyyaml

# These are required for `osbuild-dev`, only packaged for Fedora
%if 0%{?fedora}
Requires:       python3-rich
Requires:       python3-attrs
Requires:       python3-typer
%endif

%description    tools
Contains additional tools and utilities for development of
manifests and osbuild.

%package        depsolve-dnf
Summary:        Dependency solving support for DNF
Requires:       %{name} = %{version}-%{release}

# Fedora 41 and later use libdnf5, RHEL and Fedora < 41 use libdnf
%if 0%{?fedora} >= 41
Requires: python3-libdnf5 >= 5.2.1
%else
Requires: python3-libdnf
%endif

# osbuild 125 added a new "solver" field and osbuild-composer only
# supports this since 116
Conflicts: osbuild-composer <= 115

# This version needs to get bumped every time the osbuild-dnf-json
# version changes in an incompatible way. Packages like osbuild-composer
# can depend on the exact API version this way
Provides: osbuild-dnf-json-api = 7

%description    depsolve-dnf
Contains depsolving capabilities for package managers.

%prep
%forgeautosetup -p1

%build
%py3_build
make man

# SELinux
make -f /usr/share/selinux/devel/Makefile osbuild.pp
bzip2 -9 osbuild.pp

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%install
%py3_install

mkdir -p %{buildroot}%{pkgdir}/stages
install -p -m 0755 $(find stages -type f -not -name "test_*.py") %{buildroot}%{pkgdir}/stages/

mkdir -p %{buildroot}%{pkgdir}/assemblers
install -p -m 0755 $(find assemblers -type f) %{buildroot}%{pkgdir}/assemblers/

mkdir -p %{buildroot}%{pkgdir}/runners
install -p -m 0755 $(find runners -type f -or -type l) %{buildroot}%{pkgdir}/runners

mkdir -p %{buildroot}%{pkgdir}/sources
install -p -m 0755 $(find sources -type f) %{buildroot}%{pkgdir}/sources

mkdir -p %{buildroot}%{pkgdir}/devices
install -p -m 0755 $(find devices -type f) %{buildroot}%{pkgdir}/devices

mkdir -p %{buildroot}%{pkgdir}/inputs
install -p -m 0755 $(find inputs -type f) %{buildroot}%{pkgdir}/inputs

mkdir -p %{buildroot}%{pkgdir}/mounts
install -p -m 0755 $(find mounts -type f) %{buildroot}%{pkgdir}/mounts

# mount point for bind mounting the osbuild library
mkdir -p %{buildroot}%{pkgdir}/osbuild

# schemata
mkdir -p %{buildroot}%{_datadir}/osbuild/schemas
install -p -m 0644 $(find schemas/*.json) %{buildroot}%{_datadir}/osbuild/schemas
ln -s %{_datadir}/osbuild/schemas %{buildroot}%{pkgdir}/schemas

# documentation
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
install -p -m 0644 -t %{buildroot}%{_mandir}/man1/ docs/*.1
install -p -m 0644 -t %{buildroot}%{_mandir}/man5/ docs/*.5

# SELinux
install -D -m 0644 -t %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype} %{name}.pp.bz2
install -D -m 0644 -t %{buildroot}%{_mandir}/man8 selinux/%{name}_selinux.8
install -D -p -m 0644 selinux/osbuild.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if

# Udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 0755 data/10-osbuild-inhibitor.rules %{buildroot}%{_udevrulesdir}

# Remove `osbuild-dev` on non-fedora systems
%{!?fedora:rm %{buildroot}%{_bindir}/osbuild-dev}

# Install `osbuild-depsolve-dnf` into libexec
mkdir -p %{buildroot}%{_libexecdir}
install -p -m 0755 tools/osbuild-depsolve-dnf %{buildroot}%{_libexecdir}/osbuild-depsolve-dnf

# Configure the solver for dnf
mkdir -p %{buildroot}%{_datadir}/osbuild
# Fedora 41 and later use dnf5, RHEL and Fedora < 41 use dnf
%if 0%{?fedora} >= 41
install -p -m 0644 tools/solver-dnf5.json %{buildroot}%{pkgdir}/solver.json
%else
install -p -m 0644 tools/solver-dnf.json %{buildroot}%{pkgdir}/solver.json
%endif

%check
exit 0
# We have some integration tests, but those require running a VM, so that would
# be an overkill for RPM check script.

%files
%license LICENSE
%{_bindir}/osbuild
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}-manifest.5*
%{_datadir}/osbuild/schemas
%{pkgdir}
%{_udevrulesdir}/*.rules
# the following files are in the lvm2 sub-package
%exclude %{pkgdir}/devices/org.osbuild.lvm2*
%exclude %{pkgdir}/stages/org.osbuild.lvm2*
# the following files are in the luks2 sub-package
%exclude %{pkgdir}/devices/org.osbuild.luks2*
%exclude %{pkgdir}/stages/org.osbuild.crypttab
%exclude %{pkgdir}/stages/org.osbuild.luks2*
# the following files are in the ostree sub-package
%exclude %{pkgdir}/assemblers/org.osbuild.ostree*
%exclude %{pkgdir}/inputs/org.osbuild.ostree*
%exclude %{pkgdir}/sources/org.osbuild.ostree*
%exclude %{pkgdir}/stages/org.osbuild.ostree*
%exclude %{pkgdir}/stages/org.osbuild.experimental.ostree*
%exclude %{pkgdir}/stages/org.osbuild.rpm-ostree

%files -n       python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%files lvm2
%{pkgdir}/devices/org.osbuild.lvm2*
%{pkgdir}/stages/org.osbuild.lvm2*

%files luks2
%{pkgdir}/devices/org.osbuild.luks2*
%{pkgdir}/stages/org.osbuild.crypttab
%{pkgdir}/stages/org.osbuild.luks2*

%files ostree
%{pkgdir}/assemblers/org.osbuild.ostree*
%{pkgdir}/inputs/org.osbuild.ostree*
%{pkgdir}/sources/org.osbuild.ostree*
%{pkgdir}/stages/org.osbuild.ostree*
%{pkgdir}/stages/org.osbuild.experimental.ostree*
%{pkgdir}/stages/org.osbuild.rpm-ostree

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%{_mandir}/man8/%{name}_selinux.8.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files tools
%{_bindir}/osbuild-mpp
%{?fedora:%{_bindir}/osbuild-dev}

%files depsolve-dnf
%{_libexecdir}/osbuild-depsolve-dnf
%{pkgdir}/solver.json

%changelog
* Wed Sep 18 2024 Packit <hello@packit.dev> - 129-1
Changes with 129
----------------
  * Add initial support for generating SPDX SBOM documents (COMPOSER-2274) (#1818)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli, Simon de Vlieger
  * devices/loopback: add read-only option (#1842)
    * Author: Jonathan Lebon, Reviewers: Michael Vogt, Simon de Vlieger
  * jsoncomm: transparently handle huge messages via fds (#1838)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * stages/coreos.platform: use shutil.copy (#1888)
    * Author: Dusty Mabe, Reviewers: Michael Vogt, Simon de Vlieger
  * stages: fix btrfs subvolume creation under subdirectories (#1883)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * test: add test that ensures return value of `chroot.run()` (#1880)
    * Author: Michael Vogt, Reviewers: Paweł Poławski, Simon de Vlieger

— Somewhere on the Internet, 2024-09-18


* Wed Aug 21 2024 Packit <hello@packit.dev> - 126-1
Changes with 126
----------------
  * CI: update terraform hash (#1859)
    * Author: Achilleas Koutsou, Reviewers: Florian Schüller, Michael Vogt, Ondřej Budai, Sanne Raymaekers, Tomáš Hozza
  * New utility module: chroot (#1860)
    * Author: Achilleas Koutsou, Reviewers: Michael Vogt, Tomáš Hozza
  * Stages/`org.osbuild.dracut`: fix runtime environment for dracut (COMPOSER-2193) (#1846)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Michael Vogt
  * Update snapshots to 20240819 (#1856)
    * Author: SchutzBot, Reviewers: Achilleas Koutsou, Michael Vogt
  * osbuild: add "Conflicts"/"Provides" to avoid breaking composer (#1849)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Tomáš Hozza
  * schutzbot: add Achilleas' SSH keys (#1858)
    * Author: Achilleas Koutsou, Reviewers: Tomáš Hozza
  * test/depsolve: use strings for pytest.skip() (#1852)
    * Author: Achilleas Koutsou, Reviewers: Brian C. Lane, Michael Vogt, Paweł Poławski

— Somewhere on the Internet, 2024-08-21


* Wed Aug 14 2024 Packit <hello@packit.dev> - 125-1
Changes with 125
----------------
  * Makefile: run `tox parallel` without the spinner (#1835)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Tomáš Hozza
  * Test/dnf4.mark: adjust the test for markings used by DNF5 (#1827)
    * Author: Tomáš Hozza, Reviewers: Michael Vogt, Paweł Poławski
  * Tests: Add unit tests for org.osbuild.gunzip stage (#1689)
    * Author: Paweł Poławski, Reviewers: Brian C. Lane, Michael Vogt
  * jsoncom: gracefully report EMSGSIZE errors (#1840)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * main,monitor: fix total steps in progress reporting (#1826)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * osbuild-depsolve-dnf: fix some bugs and extend test coverage (#1834)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli
  * osbuild-depsolve-dnf: refactor into osbuild.solver module (#1776)
    * Author: Brian C. Lane, Reviewers: Michael Vogt, Simon de Vlieger
  * osbuild: make `inputs` `map()` function use fd for reply as well (#1836)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * solver: include "solver" key in the dnfjson reply (#1829)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Paweł Poławski
  * test_dnf4_mark(): disable all plugins when inspecting markings (#1837)
    * Author: Tomáš Hozza, Reviewers: Gianluca Zuccarelli, Paweł Poławski

— Somewhere on the Internet, 2024-08-14


* Wed Jul 31 2024 Packit <hello@packit.dev> - 124-1
Changes with 124
----------------
  * CI: build RPMs for RHEL-10.0-nightly (COMPOSER-2161) (#1822)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Florian Schüller
  * Fix dnf4 mark stage test (#1825)
    * Author: Tomáš Hozza, Reviewers: Michael Vogt, Simon de Vlieger
  * Make `tailored_profile_id` required for `json` autotailoring (#1794)
    * Author: Gianluca Zuccarelli, Reviewers: Achilleas Koutsou, Sanne Raymaekers
  * Test/manifests: start testing on c10s and el10.0-nightly (COMPOSER-2161) (#1821)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Alexander Todorov
  * Test: fix dnf4.mark stage test with DNF5 (#1824)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli
  * mpp: Allow container-storage image resolution (#1792)
    * Author: Roberto Majadas, Reviewers: Achilleas Koutsou, Ondřej Budai
  * sources(curl): error if curl exists 0 but there are downloads left (#1816)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * sources(curl): use json like output inside of custom record (#1817)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * stages/autotailor: fix stage schema (#1823)
    * Author: Gianluca Zuccarelli, Reviewers: Sanne Raymaekers, Tomáš Hozza
  * test: add new `https_serve_directory()` and test certs (#1815)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski

— Somewhere on the Internet, 2024-07-31


* Thu Jul 25 2024 Packit <hello@packit.dev> - 123-1
Changes with 123
----------------
  * Start building RPMs on CentOS Stream 10 for testing (#1799)
    * Author: Alexander Todorov, Reviewers: Florian Schüller, Tomáš Hozza
  * Tests: force checkout manifest-db (#1820)
    * Author: Tomáš Hozza, Reviewers: Florian Schüller, Gianluca Zuccarelli
  * sources(curl): disable `curl --parallel` by default (#1811)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger, Tomáš Hozza
  * sources(curl): download multiple URLs with the same curl command (#1573)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * stages/oscap.remediation: small import adjustment (#1814)
    * Author: Gianluca Zuccarelli, Reviewers: Achilleas Koutsou, Michael Vogt
  * stages: add stage for creating dm-verity partitions (#1806)
    * Author: Nikita Dubrovski, Reviewers: Achilleas Koutsou, Michael Vogt, Paweł Poławski

— Somewhere on the Internet, 2024-07-17

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Packit <hello@packit.dev> - 122-1
Changes with 122
----------------
  * CI: Add testing based on Centos containers (COMPOSER-2125) (#1585)
    * Author: Paweł Poławski, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * Test/assemblers: update manifest to use Fedora 40 + update manifests testing (#1808)
    * Author: Tomáš Hozza, Reviewers: Alexander Todorov, Michael Vogt
  * Update snapshots for rhel-9.5 to make them in sync with osbuild-composer (#1807)
    * Author: Alexander Todorov, Reviewers: Sanne Raymaekers, Tomáš Hozza
  * sources/curl: use `--user-agent` option to set the user-agent (#1809)
    * Author: Sanne Raymaekers, Reviewers: Michael Vogt, Simon de Vlieger

— Somewhere on the Internet, 2024-07-03


* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 119-2
- Rebuilt for Python 3.13

* Wed May 22 2024 Packit <hello@packit.dev> - 119-1
Changes with 119
----------------
  * Add user force password reset (#1778)
    * Author: andremarianiello, Reviewers: Brian C. Lane, Paweł Poławski
  * Tests: Add unit tests for org.osbuild.mkfs.fat stage (#1677)
    * Author: Paweł Poławski, Reviewers: Brian C. Lane, Michael Vogt
  * Update snapshots to 20240514 (#1784)
    * Author: SchutzBot, Reviewers: Achilleas Koutsou, Brian C. Lane
  * runners: revert "runners: clean up temp files before exiting the runner" (#1788)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * stage/systemd.unit.create: add Before option (#1782)
    * Author: Achilleas Koutsou, Reviewers: Brian C. Lane, Michael Vogt
  * stages/systemd.unit.create: update schema to support [Mount] (#1748)
    * Author: Achilleas Koutsou, Reviewers: Gianluca Zuccarelli, Michael Vogt
  * test/buildroot: fix checking /var/tmp mode (#1787)
    * Author: Tomáš Hozza, Reviewers: Michael Vogt, Ondřej Budai
  * tests: update stage tests readme (#1738)
    * Author: Paweł Poławski, Reviewers: Michael Vogt, Ondřej Budai, Tomáš Hozza

— Somewhere on the Internet, 2024-05-22


* Wed May 08 2024 Packit <hello@packit.dev> - 118-1
Changes with 118
----------------
  * Fix bug with sslverify and add test (#1758)
    * Author: Brian C. Lane, Reviewers: Achilleas Koutsou, Michael Vogt
  * Revert "Disable F40 CI (CVE-2024-3094 response)" (#1762)
    * Author: Brian C. Lane, Reviewers: Achilleas Koutsou, Michael Vogt, Tomáš Hozza
  * Start building RPMs on 9.5 nightly (#1770)
    * Author: Alexander Todorov, Reviewers: Jakub Rusz, Tomáš Hozza
  * Update snapshots to 20240502 (#1771)
    * Author: SchutzBot, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * osbuild: fix error match in mount test for rawhide (#1754)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * sources/curl: Use our own User-Agent (#1766)
    * Author: Ondřej Budai, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli, Michael Vogt, Simon de Vlieger
  * spec: Install osbuild-depsolve-dnf not dnf5 (#1769)
    * Author: Brian C. Lane, Reviewers: Michael Vogt, Simon de Vlieger
  * stages/kickstart: add support for the dir transport (#1764)
    * Author: Ondřej Budai, Reviewers: Michael Vogt, Tomáš Hozza
  * stages/skopeo:  Fix the remove-signatures option (#1763)
    * Author: Ondřej Budai, Reviewers: Achilleas Koutsou, Florian Schüller, Gianluca Zuccarelli, Michael Vogt
  * stages: add support for destination {dir,oci-archive} to the skopeo stage (#1752)
    * Author: Florian Schüller, Reviewers: Achilleas Koutsou, Michael Vogt
  * stages: new bootc.install.config stage (#1747)
    * Author: Achilleas Koutsou, Reviewers: Michael Vogt, Ondřej Budai
  * stages: remove redundant entries of devices/mounts in schemas (#1733)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Tomáš Hozza
  * stages: tweak the skopeo copy test (#1761)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Brian C. Lane, Florian Schüller
  * test_clamp_mtime: avoid clashing with chrony (#1760)
    * Author: Florian Schüller, Reviewers: Brian C. Lane, Michael Vogt
  * testutil: fix `make_container()` cleanup (#1757)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Brian C. Lane
  * workflow: bump osbuild-ci container to include podman, et al. (#1759)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Ondřej Budai
  * workflow: show summary why tests are skipped (#1755)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Brian C. Lane

— Somewhere on the Internet, 2024-05-08


* Wed Apr 24 2024 Packit <hello@packit.dev> - 117-1
Changes with 117
----------------
  * Enable osbuild-depsolve-dnf5 testing and fix a bug (#1744)
    * Author: Brian C. Lane, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * Enable unit tests for osbuild-depsolve-dnf(5) (#1731)
    * Author: Achilleas Koutsou, Reviewers: Michael Vogt, Sanne Raymaekers
  * Makefile: make sure that `make test-all` really runs all tests (#1734)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * Stages/SELinux: force auto-relabel of full contexts (#1737)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Michael Vogt, Simon de Vlieger
  * Stages/cloud-init: support additional datasources (COMPOSER-2060) (#1729)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Michael Vogt
  * Update snapshots to 20240415 (#1725)
    * Author: SchutzBot, Reviewers: Sanne Raymaekers, Simon de Vlieger
  * meta: automatically allow `devices` as input in the stages schemas (#1727)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * org.osbuld.systemd: support unit files that start with - (#1749)
    * Author: Achilleas Koutsou, Reviewers: Alexander Larsson, Brian C. Lane, Gianluca Zuccarelli
  * stages(groups): add support for the mounts for `bootc install to-filesystem`  (#1726)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai
  * stages: add support for `--target-imgref` to bootc install to-filesystem (#1740)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai
  * stages: allow `bootloader --append` via kickstart (#1742)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * systemd.unit.create: support the After option in the Unit section (HMS-3814) (#1741)
    * Author: Achilleas Koutsou, Reviewers: Michael Vogt, Sanne Raymaekers
  * tools: extract common _test_depsolve_both_dnf_dnf5 helper. (#1716)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * tools: fix error when `releasever` cannot be found (#1739)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * tox,workflow: run all tests in the GH worfklow (#1735)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai

— Somewhere on the Internet, 2024-04-24


* Wed Apr 10 2024 Packit <hello@packit.dev> - 115-1
Changes with 115
----------------
  * Main bump checkout action to v4 (#1713)
    * Author: Brian C. Lane, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * Stage: Schema migration to separated JSON files (#1697)
    * Author: Paweł Poławski, Reviewers: Brian C. Lane, Simon de Vlieger
  * Tests: Add unit tests for org.osbuild.mkfs.btrfs stage (#1681)
    * Author: Paweł Poławski, Reviewers: Michael Vogt, Simon de Vlieger
  * Tests: Add unit tests for org.osbuild.mkfs.xfs stage (#1678)
    * Author: Paweł Poławski, Reviewers: Michael Vogt, Simon de Vlieger
  * Update snapshots to 20240327 (#1690)
    * Author: SchutzBot, Reviewers: Achilleas Koutsou, Ondřej Budai
  * inputs,sources: add new `{inputs,sources}_service` fixtures (#1685)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai
  * osbuild-mpp: Expand information in PkgInfo (#1688)
    * Author: Pierre-Yves Chibon, Reviewers: Paweł Poławski, Simon de Vlieger
  * source: add curl test in preparation for #1573 (#1703)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * sources(curl): set HTTP proxy through the environment (#1708)
    * Author: Sanne Raymaekers, Reviewers: Achilleas Koutsou, Michael Vogt, Paweł Poławski
  * sources(curl): tweak tests to use monkeypatch.setenv() (#1709)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Ondřej Budai
  * sources: add regression test for issue#1693 (#1699)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * sources: some small tweaks to the curl tests (#1700)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * stages(mkdir): allow to pass in devices/mounts (#1712)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai
  * stages: add org.osbuild.zip (#1692)
    * Author: Luke Yang, Reviewers: Achilleas Koutsou, Michael Vogt
  * stages: move users/selinux to v2 and add devices/mounts support (#1705)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Paweł Poławski
  * systemd.unit.create: Add Environment and EnvironmentFile options (HMS-3814) (#1684)
    * Author: Achilleas Koutsou, Reviewers: Michael Vogt, Simon de Vlieger
  * testutil: add AtomicCounter() as a threadsafe counter (#1707)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Ondřej Budai

— Somewhere on the Internet, 2024-04-10


* Fri Mar 29 2024 Packit <hello@packit.dev> - 114-1
Changes with 114
----------------
  * curl: fix RHSM url retrieval (#1694)
    * Author: andremarianiello, Reviewers: Paweł Poławski, Sanne Raymaekers, Simon de Vlieger

— Somewhere on the Internet, 2024-03-29


* Wed Mar 27 2024 Packit <hello@packit.dev> - 113-1
Changes with 113
----------------
  * Reformat all JSON files for consistency (#1687)
    * Author: Achilleas Koutsou, Reviewers: Paweł Poławski, Simon de Vlieger
  * Revert "osbuild: ensure loop.Loop() has the required device node" (#1646)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Brian C. Lane, Simon de Vlieger
  * Update snapshots to 20240313 (#1662)
    * Author: SchutzBot, Reviewers: Brian C. Lane, Simon de Vlieger
  * doc: document the new json-sequence monitor (HMS-3258) (#1659)
    * Author: Michael Vogt, Reviewers: Simon Steinbeiß, Simon de Vlieger
  * osbuild: ensure /var/tmp is a real directory (#1673)
    * Author: Michael Vogt, Reviewers: Gianluca Zuccarelli, Simon de Vlieger
  * osbuild: first step towards stage separation - allow meta.json for stages (#1618)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * osbuild: make the entire /etc/selinux avaialble for the buildroot (HMS-3453) (#1675)
    * Author: Michael Vogt, Reviewers: Colin Walters, Ondřej Budai, Simon de Vlieger
  * sources: transform() is only used in the curl sources, remove  from ABC and rename (#1667)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * stage/systemd-unit-create:new systemd unit config params (#1666)
    * Author: Sayan Paul, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * stages(selinux): add option exclude_paths (#1670)
    * Author: Michael Vogt, Reviewers: Paweł Poławski, Simon de Vlieger
  * stages: add functional user expiredate tests (#1664)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Brian C. Lane
  * stages: add support for  options to bootc-install-to-fs (#1658)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Florian Schüller, Simon de Vlieger
  * stages: allow bootc.install-to-filesystem work without selinux (HMS-3453) (#1682)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * stages: convert schemas to external (#1663)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli
  * test: Add stage test trigger to makefile (#1660)
    * Author: Paweł Poławski, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * test: return container_id in `make_container` (#1657)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * tests: migrate manifest tests (#1622)
    * Author: tkoscieln, Reviewers: Alexander Todorov, Jakub Rusz
  * tox.ini: update autopep8/pyocdestyle to support py3.12 (#1661)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * util: Consolidate parse functions into util (#1615)
    * Author: Renata Ravanelli, Reviewers: Michael Vogt, Simon de Vlieger
  * workflow: re-enable parallel runs to improve speed of test_stages and test_assemblers (#1683)
    * Author: Florian Schüller, Reviewers: Michael Vogt, Paweł Poławski

— Somewhere on the Internet, 2024-03-27


* Wed Mar 13 2024 Packit <hello@packit.dev> - 112-1
Changes with 112
----------------
  * Remount containers-store bind mount as `rw` (#1651)
    * Author: Gianluca Zuccarelli, Reviewers: Achilleas Koutsou, Ondřej Budai
  * Schutzbot: Remove RH-IT-Root-CA (#1627)
    * Author: Jakub Rusz, Reviewers: Michael Vogt, Ondřej Budai, Simon Steinbeiß, Simon de Vlieger
  * Update snapshots to 20240301 (#1619)
    * Author: SchutzBot, Reviewers: Achilleas Koutsou, Simon Steinbeiß
  * actions/sonarqube: Drop SonarQube in favor of Snyk (HMS-3697) (#1626)
    * Author: Simon Steinbeiß, Reviewers: Jakub Rusz
  * actions/test: Only test assemblers in Python 3.6 (HMS-3697) (#1621)
    * Author: Simon Steinbeiß, Reviewers: Michael Vogt
  * actions: Add a PR best practices check (#1628)
    * Author: Simon Steinbeiß, Reviewers: Achilleas Koutsou, Michael Vogt
  * lint: replace `isort` with `ruff` and provide `lint-quick` (HMS-3697) (#1634)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Michael Vogt
  * many: jsonseq based progress reporting for osbuild (#1545)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * osbuild: ensure a usable /var/tmp is available inside the buildroot (#1649)
    * Author: Michael Vogt, Reviewers: Colin Walters, Ondřej Budai
  * osbuild: reuse loop_for_fd() in LoopServer (#1642)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai
  * sources/curl: add org.osbuild.mtls secrets support (#1644)
    * Author: Sanne Raymaekers, Reviewers: Brian C. Lane, Simon de Vlieger
  * stage/systemd-unit-create: parametrize file location (#1620)
    * Author: Sayan Paul, Reviewers: Achilleas Koutsou, Michael Vogt, Simon de Vlieger
  * stages,util: tweaks for the platform/bls handling (#1612)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * stages/kickstart: add `noswap` to `autopart` (#1654)
    * Author: Simon de Vlieger, Reviewers: Florian Schüller, Michael Vogt
  * stages/org.osbuild.gzip: add compression level option (#1616)
    * Author: Luke Yang, Reviewers: Michael Vogt, Simon de Vlieger
  * stages/org.osbuild.users: add expire date (#1648)
    * Author: andremarianiello, Reviewers: Michael Vogt, Simon de Vlieger
  * test: add unit-{type,path} test coverage (#1650)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Simon de Vlieger
  * test: fix test_assembler to support parallel runs and run in parallel (HMS-3697) (#1641)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon Steinbeiß, Simon de Vlieger
  * test: use OSBUILD_TEST_STORE in test_assemblers.py and run in parallel (HMS-3697) (#1630)
    * Author: Michael Vogt, Reviewers: Simon Steinbeiß, Simon de Vlieger
  * test: use `del os.environ[]` instead of `os.unsetenv` (thanks Simon) (#1653)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * tests/manifest: Don't retain image-info artifacts (HMS-3697) (#1640)
    * Author: Simon Steinbeiß, Reviewers: Simon de Vlieger, Thomas Lavocat
  * tests: Cancel in-progress tests on PR updates (HMS-3697) (#1636)
    * Author: Simon Steinbeiß, Reviewers: Michael Vogt, Ondřej Budai
  * tests: Report GitLab job failures globally (HMS-3697) (#1632)
    * Author: Achilleas Koutsou, Reviewers: Jakub Rusz, Simon Steinbeiß, Simon de Vlieger
  * tests: improve the gitlab tests (HMS-3697) (#1629)
    * Author: Ondřej Budai, Reviewers: Achilleas Koutsou, Simon Steinbeiß
  * tests: revert "workflow: run assembler tests in parallel" /o\ (#1637)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * utils/mnt: fix mount permissions (#1643)
    * Author: Gianluca Zuccarelli, Reviewers: Michael Vogt, Simon de Vlieger, Tomáš Hozza
  * workflow, osbuild-mpp: run with cache (HMS-3697) (#1623)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * workflow: drop python3.11 from matrix (HMS-3697) (#1625)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * workflow: run all unit tests in parallel (#1655)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger

— Somewhere on the Internet, 2024-03-13


* Wed Feb 28 2024 Packit <hello@packit.dev> - 111-1
Changes with 111
----------------
  * many: tweak `containers-storage` implementation (#1609)
    * Author: Michael Vogt, Reviewers: Gianluca Zuccarelli, Ondřej Budai
  * stages/org.osbuild.tar: add sparse option (#1614)
    * Author: Luke Yang, Reviewers: Brian C. Lane, Michael Vogt

— Somewhere on the Internet, 2024-02-28


* Mon Feb 26 2024 Packit <hello@packit.dev> - 110-1
Changes with 110
----------------
  * Add coreos.platforms stage (#1589)
    * Author: Renata Ravanelli, Reviewers: Nobody
  * Sources/containers-storage: make the code Python 3.6 compliant (#1610)
    * Author: Tomáš Hozza, Reviewers: Gianluca Zuccarelli, Simon de Vlieger

— Somewhere on the Internet, 2024-02-26


* Thu Feb 22 2024 Packit <hello@packit.dev> - 109-1
Changes with 109
----------------
  * Extend `grub2`/`grub2.legacy` stage default config options (#1601)
    * Author: Tomáš Hozza, Reviewers: Michael Vogt, Ondřej Budai
  * Fix developer guide link in README.md (#1602)
    * Author: Adam Williamson, Reviewers: Brian C. Lane, Michael Vogt
  * Stages/grub2.legacy: make config options a subset of grub2 stage (#1606)
    * Author: Tomáš Hozza, Reviewers: Gianluca Zuccarelli, Michael Vogt
  * Systemd unit creation stage (#1578)
    * Author: Sayan Paul, Reviewers: Achilleas Koutsou, Sanne Raymaekers
  * osbuild-depsolve-dnf5: Fix url substitutions (#1597)
    * Author: Brian C. Lane, Reviewers: Michael Vogt, Simon de Vlieger
  * osbuild-depsolve-dnf5: module_hotfixes wasn't really set (#1598)
    * Author: Brian C. Lane, Reviewers: Michael Vogt, Simon de Vlieger
  * sources,util: add containers-storage source (#1550)
    * Author: Gianluca Zuccarelli, Reviewers: Nobody
  * stages(dracut): add small unittest for initoverlayfs (#1607)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * stages(org.osbuild.systemd.unit.create): add small unit test (#1596)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * stages/bootc.install-to-fs: fix root mount handling (#1593)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai
  * stages/dracut: Add functionality to build initoverlayfs with dracut (#1586)
    * Author: Eric Curtin, Reviewers: Michael Vogt, Ondřej Budai
  * stages/oscap.remediation: Mount host's /proc and /dev earlier (#1590)
    * Author: Evgeny Kolesnikov, Reviewers: Gianluca Zuccarelli, Michael Vogt
  * stages/ostree-container-deploy: make sure `/var/tmp` exists (#1605)
    * Author: Gianluca Zuccarelli, Reviewers: Ondřej Budai, Tomáš Hozza
  * tox,tools: add tools back to lintables (#1600)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Ondřej Budai

— Somewhere on the Internet, 2024-02-22


* Wed Jan 31 2024 Packit <hello@packit.dev> - 106-1
Changes with 106
----------------
  * CI: update terraform SHA (#1559)
    * Author: Jakub Rusz, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * stages/org.osbuild.cloud-init: fix dump format of `datasource_list` key (#1556)
    * Author: Tomáš Hozza, Reviewers: Michael Vogt
  * test: drop `-k` from `-k stages/test` test matrix (#1564)
    * Author: Michael Vogt, Reviewers: Dusty Mabe, Tomáš Hozza

— Somewhere on the Internet, 2024-01-31


* Wed Jan 31 2024 Packit <hello@packit.dev> - 105-1
Changes with 105
----------------
  * move source parallelization into sources (#1549)
    * Author: Simon de Vlieger, Reviewers: Brian C. Lane
  * osbuild-depsolve-dnf5: Add libdnf5 based depsolving for Fedora 40 (#1530)
    * Author: Brian C. Lane, Reviewers: Simon de Vlieger
  * osbuild: add "mypy-strict" check (#1476)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * osbuild: error when {Device,Mount} is modified after creation (#1516)
    * Author: Michael Vogt, Reviewers: Brian C. Lane
  * schutzbot: add dustymabe SSH key to team_ssh_keys (#1546)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou
  * stages(container-deploy): add new `exclude` option (#1552)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * stages/org.osbuild.mkfs.ext4: add ext4 options (#1538)
    * Author: Luke Yang, Reviewers: Dusty Mabe
  * stages/ostree.aleph: don't manipulate image name from origin (#1548)
    * Author: Dusty Mabe, Reviewers: Luke Yang
  * test: add new testutil.assert_jsonschema_error_contains() helper (#1543)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * test: check that `mkfs.fat` has the `-g` option in `test_fat` (#1540)
    * Author: Michael Vogt, Reviewers: Paweł Poławski
  * test: export schemas in testing_libdir_fixture (#1539)
    * Author: Michael Vogt, Reviewers: Paweł Poławski
  * test: fix `test_libc_futimes_works` (#1541)
    * Author: Michael Vogt, Reviewers: Paweł Poławski
  * test: fix test_schema_validation_containers_storage_conf (#1542)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * tests/CI: Add RHEL 9.3 and 8.9 GA to pipeline (#1536)
    * Author: tkoscieln, Reviewers: Jakub Rusz

— Somewhere on the Internet, 2024-01-31


* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Packit <hello@packit.dev> - 104-1
Changes with 104
----------------
  * HMS-3235: Skopeo source storage location (#1504)
    * Author: Gianluca Zuccarelli, Reviewers: Achilleas Koutsou
  * add --break for requesting a debug shell (#1532)
    * Author: Dusty Mabe, Reviewers: Brian C. Lane, Michael Vogt, Tomáš Hozza
  * create org.osbuild.bootupd stage (#1519)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou
  * minor updates for fedora-coreos-container manifest (#1533)
    * Author: Dusty Mabe, Reviewers: Simon de Vlieger
  * osbuild: test OSBUILD_EXPORT_FORCE_NO_PRESERVE_OWNER (#1511)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * stages(container-deploy): ensure `/var/tmp` is available (#1531)
    * Author: Michael Vogt, Reviewers: Ondřej Budai
  * stages(grub2): allow pulling efi binaries from alternative efi roots (#1529)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * stages,util: add org.osbuild.selinux tests and small functional tweaks (#1526)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages/org.osbuild.ostree.config: support bls-append-except-default (#1534)
    * Author: Luke Yang, Reviewers: Dusty Mabe
  * stages: add new `org.osbuild.container-deploy` stage (#1509)
    * Author: Michael Vogt, Reviewers: Brian C. Lane
  * test: fix new mount tests under rhel8 (#1537)
    * Author: Michael Vogt, Reviewers: Paweł Poławski, Tomáš Hozza
  * tools/osbuild-mpp: run _process_format() for mpp-embed dict (#1528)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou

— Somewhere on the Internet, 2024-01-16


* Wed Jan 03 2024 Packit <hello@packit.dev> - 103-1
Changes with 103
----------------
  * Update snapshots to 20240101 (#1520)
    * Author: SchutzBot, Reviewers: Tomáš Hozza
  * github: run tests on push again (#1517)
    * Author: Achilleas Koutsou, Reviewers: Michael Vogt, Simon de Vlieger, Tom Gundersen
  * mounts: support mounting partitions (#1501)
    * Author: Dusty Mabe, Reviewers: Michael Vogt
  * osbuild: allow to export a tree without preserving the ownership (less tests) (#1512)
    * Author: Michael Vogt, Reviewers: Tomáš Hozza
  * test: add more output when ensure_mtime() assert fails (#1518)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * test: fix running on debian hosts (#1522)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * test: include tests in `make lint` and fix issues (#1521)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * test: rename TestFileSystemMountService->FakeFileSystemMountService (#1513)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger

— Somewhere on the Internet, 2024-01-03


* Wed Dec 20 2023 Packit <hello@packit.dev> - 102-1
Changes with 102
----------------
  * Add tests for org.osbuild.xz and org.osbuild.zstd (#1496)
    * Author: Brian C. Lane, Reviewers: Michael Vogt
  * Fedora 40 (#1486)
    * Author: Jakub Rusz, Reviewers: Alexander Todorov, Simon de Vlieger
  * HMS-3235 sources/skopeo: check containers-storage (#1489)
    * Author: Gianluca Zuccarelli, Reviewers: Achilleas Koutsou
  * Switch nightly testing to RHEL-8.10 and RHEL-9.4 (#1422)
    * Author: Jakub Rusz, Reviewers: Alexander Todorov
  * Update containers storage conf stage (#1487)
    * Author: Alexander Larsson, Reviewers: Giuseppe Scrivano, Simon de Vlieger
  * create org.osbuild.ostree.aleph stage (#1475)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou
  * fix for inaccurate mountinfo inside bwrap env (#1493)
    * Author: Dusty Mabe, Reviewers: Michael Vogt
  * fscache: implement "last_used()" helper (#1498)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * org.osbuild.systemd: Support masking generators (#1505)
    * Author: Alexander Larsson, Reviewers: Michael Vogt
  * osbuild: include std{out,err} in FileSystemMountService.mount() errors (#1497)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * osbuild: pytoml is deprecated, replace with toml (#1499)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages(kickstart): add `ostreecontainer` (#1488)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt
  * stages(mkfs.ext4): add basic unit test (#1502)
    * Author: Michael Vogt, Reviewers: Brian C. Lane
  * stages/skopeo: destinations (#1494)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Brian C. Lane
  * test,util: fix mount and add test that ensures mount output is part of the exception (#1490)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger

— Somewhere on the Internet, 2023-12-20


* Wed Dec 06 2023 Packit <hello@packit.dev> - 101-1
Changes with 101
----------------
  * Create fake `machine-id` and cleanup before exiting (#1458)
    * Author: Miguel Martin, Reviewers: Brian C. Lane, Michael Vogt, Simon de Vlieger
  * Move org.osbuild.experimental.ostree.config to osbuild-ostree subpackage (#1464)
    * Author: Alexander Larsson, Reviewers: Simon de Vlieger
  * Packit: make COPR builds for new releases in a separate project (#1479)
    * Author: Tomáš Hozza, Reviewers: Eric Curtin, Simon Steinbeiß
  * Readme update (#1483)
    * Author: Paweł Poławski, Reviewers: Simon de Vlieger
  * enhance support for creating 4k native disk images (#1461)
    * Author: Dusty Mabe, Reviewers: Simon de Vlieger
  * osbuild-mpp: Print better errors if eval fails (#1477)
    * Author: Alexander Larsson, Reviewers: Simon de Vlieger
  * osbuild-mpp: conditional losetup (#1478)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Alexander Larsson, Michael Vogt
  * osbuild. add comment why AST is used and not importlib (#1463)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * osbuild/util/fscache: calculate actual size of files (#1453)
    * Author: Dusty Mabe, Reviewers: Simon de Vlieger
  * osbuild: ensure loop.Loop() has the required device node (#1468)
    * Author: Michael Vogt, Reviewers: Ondřej Budai
  * osbuild: fix missing initialization of fd in osbuild.loop.Loop (#1467)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Ondřej Budai
  * osbuild: improve monitor docstrings/signatures (#1473)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stage(oscap.remediation): link /proc/self/fd to /dev/fd (#1459)
    * Author: Marcos Libanori Sanches Júnior, Reviewers: Gianluca Zuccarelli, Simon de Vlieger
  * stages(autotailor): add small unit test (#1481)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli, Simon de Vlieger
  * stages(erofs): add org.osbuild.erofs (#1437)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages(kickstart): add `network` support to kickstart (#1451)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages(machine-id): add a new "machine-id"  stage (#1452)
    * Author: Michael Vogt, Reviewers: Nobody
  * stages(ostree.post-copy): add stage unit test and comment (#1465)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages: Add stages to support ostree signatures and composefs (#1343)
    * Author: Alexander Larsson, Reviewers: Nobody
  * stages:oscap.autotailor: add key/value overrides (#1407)
    * Author: Gianluca Zuccarelli, Reviewers: Evgeny Kolesnikov, Simon de Vlieger
  * test: fix broken oscap remediation tests (#1470)
    * Author: Gianluca Zuccarelli, Reviewers: Simon de Vlieger
  * test: stage tests -> stage integration tests (#1469)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt
  * tests: remove custom tempdir_fixture (#1462)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * tests: remove custom tmpdir() fixtures and use tmp_path (#1466)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger

— Somewhere on the Internet, 2023-12-06


* Wed Nov 22 2023 Packit <hello@packit.dev> - 100-1
Changes with 100
----------------
  * Add stages to sign ostree commits (#1445)
    * Author: Alexander Larsson, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * Consolidate functions used by runners (#1446)
    * Author: Miguel Martin, Reviewers: Michael Vogt
  * RPM stage: link /proc/self/fd to /dev/fd (#1448)
    * Author: Miguel Martin, Reviewers: Simon de Vlieger
  * docs: tweak the man-page a bit to make the example more useful (#1455)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * schutzbot/terraform: aws instance types rework (#1436)
    * Author: Sanne Raymaekers, Reviewers: Simon de Vlieger
  * stage/test: skip kickstart validate test if no ksvalidator (#1438)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt
  * stages(kickstart): add test for schema validation (#1432)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages(kickstart): add unittest test for zerombr/clearpart (#1430)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages(kickstart): ensure test inputs pass schema validation (#1440)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages(kickstart): implement "display_mode" option and tiny test addition (#1442)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * stages(kickstart): implement "reboot" option (#1435)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * stages(kickstart): run ksvalidator as part of the tests (#1434)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Brian C. Lane
  * stages(kickstart): support autopart (#1449)
    * Author: Michael Vogt, Reviewers: Brian C. Lane, Simon de Vlieger
  * stages: add `org.osbuild.update-crypto-policies` stage (#1443)
    * Author: Miguel Martin, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * stages: add kernel-cmdline.bls-append stage (#1429)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou
  * tests: finish the conversion to the parametrized Fedora v2 manifest (#1441)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * tools: tweak `gen-stage-test-diff` to fix defaults for max-size and allow running from a git checkout (#1447)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * tox: move to pylint 3.0.2 for py312 support (#1450)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger

— Somewhere on the Internet, 2023-11-22


* Wed Nov 08 2023 Packit <hello@packit.dev> - 99-1
Changes with 99
----------------
  * :package: Packit configuration enhancements (#1416)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Simon Steinbeiß, Simon de Vlieger
  * Add a tool script to help check for unused runners (#1367)
    * Author: Brian C. Lane, Reviewers: Simon de Vlieger
  * Add selinux-label-version to the org.osbuild.ostree.commit stage (#1415)
    * Author: Alexander Larsson, Reviewers: Colin Walters, Simon de Vlieger
  * Build rpms on RHEL-8.10 and RHEL-9.4 (#1417)
    * Author: Jakub Rusz, Reviewers: Alexander Todorov
  * Update snapshots to 20231101 (#1419)
    * Author: SchutzBot, Reviewers: Simon de Vlieger
  * depsolve-dnf: enable weak deps selection (#1413)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou
  * depsolve-dnf: helpful exception for repo (#1412)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou
  * kickstart: add support for "zerombr","clearpart" (#1426)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * objectstore: also mount /etc/containers for "host" buildroot (#1410)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou
  * stage/copy: fix exception msg when parsing mounts and inputs (#1421)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Ondřej Budai
  * stages(kickstart): add options "lang", "keyboard", "timezone" (#1424)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * stages/mkdir: fix its schema (#1409)
    * Author: Ondřej Budai, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * stages: add new unit test for kickstart stage (#1425)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * tests: run the `test_stages` category in parallel (#1431)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * tools: add Fedora 38 runner for OSTree image tests (COMPOSER-1998) (#1427)
    * Author: Paweł Poławski, Reviewers: Ondřej Budai

— Somewhere on the Internet, 2023-11-08


* Wed Oct 25 2023 Packit <hello@packit.dev> - 98-1
Changes with 98
----------------
  * Update snapshots to 20231012 (#1400)
    * Author: SchutzBot, Reviewers: Achilleas Koutsou
  * Update snapshots to 20231015 (#1403)
    * Author: SchutzBot, Reviewers: Achilleas Koutsou
  * depsolve: import `dnf-json` (#1396)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou
  * manifests/fedora-vars: bump snapshot date (#1408)
    * Author: Dusty Mabe, Reviewers: Simon de Vlieger
  * stages/org.osbuild.users: support multiple SSH keys (#1386)
    * Author: Michael Ho, Reviewers: Achilleas Koutsou
  * stages/oscap.remediation: Properly utilize offline capabilities (#1395)
    * Author: Evgeny Kolesnikov, Reviewers: Nobody
  * stages/ostree.deploy.container: allow deploying from container (#1402)
    * Author: Dusty Mabe, Reviewers: Nobody
  * test/stages/users: make test data date agnostic (#1406)
    * Author: Michael Ho, Reviewers: Ondřej Budai, Simon de Vlieger, Tomáš Hozza
  * tools/osbuild-mpp: Really fix empty ostree commit object in deploy stage (#1405)
    * Author: Alexander Larsson, Reviewers: Achilleas Koutsou
  * tools/osbuild-mpp: add mpp-resolve-ostree-commits helper (#1399)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou

— Somewhere on the Internet, 2023-10-25


* Wed Oct 11 2023 Packit <hello@packit.dev> - 97-1
Changes with 97
----------------
  * Support FAT FS Geometry Options (#1391)
    * Author: Maxime Ripard, Reviewers: Simon de Vlieger
  * Update Fedora 39 x86_64 runner (#1392)
    * Author: Achilleas Koutsou, Reviewers: Sanne Raymaekers
  * fix link to developer guide (#1388)
    * Author: Otto Fowler, Reviewers: Brian C. Lane
  * osbuild/util: hoist container handling code from skopeo stage into util/containers (#1389)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou
  * refactor ostree stages; add inputs to ostree.deploy stage (#1393)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * stages/ostree.deploy: switch to v2 schema (#1390)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou

— Somewhere on the Internet, 2023-10-11


* Wed Sep 27 2023 Packit <hello@packit.dev> - 96-1
Changes with 96
----------------
  * docs: update the samples used in osbuild.1.rst (#1384)
    * Author: Michael Vogt, Reviewers: Sanne Raymaekers, Simon de Vlieger
  * stages/ostree.deploy: drop requirement on rootfs option (#1385)
    * Author: Dusty Mabe, Reviewers: Achilleas Koutsou, Colin Walters

— Somewhere on the Internet, 2023-09-27


* Wed Sep 13 2023 Packit <hello@packit.dev> - 95-1
Changes with 95
----------------
  * Actions: add workflow for marking and closing stale issues and PRs (#1382)
  * osbuild.ostree.selinux: xref ostree issue for this (#1377)
  * runners: add autosd runner (#1381)

Contributions from: Colin Walters, Eric Curtin, Tomáš Hozza

— Somewhere on the Internet, 2023-09-13


* Wed Aug 30 2023 Packit <hello@packit.dev> - 94-1
Changes with 94
----------------
  * .gitlab-ci: update RHEL ga runners (#1371)
  * Add support for btrfs subvolumes, metadata profiles and compression (#1312)
  * Update snapshots to 20230824 (#1373)
  * stages/dracut: add dracut omit drivers option (#1374)
  * tests/ostree-container: Drop hardcoded max layers (#1375)

Contributions from: Brian Masney, Colin Walters, Ondřej Budai, Sanne Raymaekers, schutzbot

— Somewhere on the Internet, 2023-08-30


* Wed Aug 23 2023 Packit <hello@packit.dev> - 93-1
Changes with 93
----------------
  * extend org.osbuild.systemd.unit stage ability to update user units (#1363)
  * schutzbot: unregister test hosts (#1372)
  * tests: Add a check for valid snapshot urls (#1366)

Contributions from: Brian C. Lane, Sanne Raymaekers, Sayan Paul

— Somewhere on the Internet, 2023-08-23


* Wed Aug 16 2023 Packit <hello@packit.dev> - 92-1
Changes with 92
----------------
  * Improve the linting setup (#1362)
  * Refactor Fedora test manifests v2 and update them to F38 (#1351)
  * Update fedora-39 runners and repositories (#1369)
  * Update snapshots to 20230801 (#1355)
  * Update snapshots to 20230815 (#1370)
  * autopep8: Increase aggressive level (#1361)
  * dnf4.mark: mark packages in DNF state database (#1333)
  * osbuild: add `--checkpoint` can now use globs (#1358)
  * ostree.encapsulate: It's rpm-ostree, not ostree (#1359)

Contributions from: Brian C. Lane, Colin Walters, Jakub Rusz, Ondřej Budai, Simon de Vlieger, schutzbot

— Somewhere on the Internet, 2023-08-16


* Wed Aug 02 2023 Packit <hello@packit.dev> - 91-1
Changes with 91
----------------
  * ci: add tox (#1262)
  * tools: `osbuild-dev` quality of life (#1348)

Contributions from: Simon de Vlieger

— Somewhere on the Internet, 2023-08-02


* Wed Jul 19 2023 Packit <hello@packit.dev> - 90-1
Changes with 90
----------------
  * .gitlab-ci.yml: Run rpmbuild for Fedora 39 (#1344)
  * Expand `sysconfig` stage with `livesys` and `desktop` (#1345)
  * Schutzfile: Fix f38 snapshot references (#1347)
  * org.osbuild.rpm: Add some context to rpmkeys failure (#1244)
  * runners: Asahi Fedora Remix to Fedora Asahi Remix (#1338)
  * stage: anaconda, allow access to more config (#1320)
  * stages/rpm: chmod `machine-id` to 0444 (#1342)
  * stages/squashfs: add support for zstd compression (#1232)
  * stages: add openscap autotailor stage (#1336)
  * test/data: introduce UKI also for CentOS Stream (#1233)

Contributions from: Brian C. Lane, Eric Curtin, Gianluca Zuccarelli, Ondřej Budai, Simon de Vlieger

— Somewhere on the Internet, 2023-07-19


* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 89-2
- Rebuilt for Python 3.12

* Tue Jun 27 2023 Packit <hello@packit.dev> - 89-1
Changes with 89
----------------
  * CI variable name has changed, (#1330)
  * inputs: Move arguments for InputService.map to a temporary file (#1331)

Contributions from: Alexander Todorov, Ondřej Budai

— Somewhere on the Internet, 2023-06-27


* Wed Jun 21 2023 Packit <hello@packit.dev> - 88-1
Changes with 88
----------------
  * COMPOSER-1959: Also test on RHEL 8.9 and 9.3 nightly (#1301)
  * Restore LOOP_CONFIGURE fallback for kernel < 5.8 (#1327)
  * stages: add new zstd stage (#1322)

Contributions from: Alexander Todorov, Antonio Murdaca, Michael Hofmann

— Somewhere on the Internet, 2023-06-21


* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 87-2
- Rebuilt for Python 3.12

* Wed Jun 07 2023 Packit <hello@packit.dev> - 87-1
Changes with 87
----------------
  * Spec: use `%%forgeautosetup` macro in `%%prep` phase (#1318)
  * Support GPT partition attribute bits when creating images (#1296)
  * Test: make partitioning tools stage tests pass on RHEL-8 + add unit test for `sfdisk` stage (#1317)
  * add livesys stage (#1311)
  * mockbuild.sh: retry dnf install up to 5 times (#1319)
  * readme: mention matrix, redo headings (#1305)
  * schutzfile: update manifest-db ref 2023-06-05 (#1323)
  * stages/sgdisk: option to not quote partition names passed to sgdisk (#1316)

Contributions from: Eric Chanudet, SchutzBot, Simon de Vlieger, Tomáš Hozza

— Somewhere on the Internet, 2023-06-07


* Wed May 24 2023 Packit <hello@packit.dev> - 86-1
Changes with 86
----------------
  * org.osbuild.mkfs.ext4: Add verity option to (#1310)
  * runners: add fedora-38 specific logic for SHA1 key support (#1307)
  * schutzfile: update manifest-db ref 2023-05-20 (#1313)
  * stages/isolinux: default list (#1309)

Contributions from: Alexander Larsson, Michael Ho, SchutzBot, Simon de Vlieger, Thomas Lavocat

— Somewhere on the Internet, 2023-05-24


* Wed May 10 2023 Packit <hello@packit.dev> - 85-1
Changes with 85
----------------
  * COMPOSER-1959: Start building osbuild on RHEL 8.9 and 9.3 nightly (#1300)
  * Python 3.6 compatibility fixes (#1294)
  * Update terraform SHA (#1299)
  * Update test runners for 8.8 & 9.2 nightly (#1162)
  * Various fixes (#1295)
  * loop: use LOOP_CONFIGURE when available (#1253)
  * stages/org.osbuild.ovf: support older python3 versions (#1306)
  * stages/yum.repo: add `sslverify` field (#1298)

Contributions from: Alexander Todorov, Gianluca Zuccarelli, Jakub Rusz, Sanne Raymaekers, Thomas Lavocat, Tomáš Hozza

— Somewhere on the Internet, 2023-05-10


* Thu Apr 27 2023 Packit <hello@packit.dev> - 84-1
Changes with 84
----------------
  * CI tests cleanup and maintenance (#1282)
  * Remove SSH keys of people who left the team (#1290)
  * Test: skip test cases if the tested filesystem is not supported on the platform (#1287)
  * lint: provide bandit configuration (#1265)
  * mockbuild.sh: use dnf to install local package, not rpm (#1292)
  * stages/lorax-script: minor schema adjustments (#1257)

Contributions from: Ondřej Budai, Simon de Vlieger, Tomáš Hozza

— Somewhere on the Internet, 2023-04-26


* Wed Apr 12 2023 Packit <hello@packit.dev> - 83-1
Changes with 83
----------------
  * .gitlab-ci: drop fedora-35 (#1281)
  * .gitlab-ci: remove RHEL 8.6/9.0 ga runners (#1279)
  * Preserve manifest list digest when embedding containers (#1252)
  * WSL conf stage (#1278)
  * ci: remove codecov (#1271)
  * schutzfile: update manifest-db ref 2023-03-20 (#1260)
  * stage/systemd: be able to write a preset file (#1269)
  * stages/org.osbuild.ovf: support older python3 versions (#1276)

Contributions from: Achilleas Koutsou, Sanne Raymaekers, SchutzBot, Simon de Vlieger

— Somewhere on the Internet, 2023-04-12


* Wed Mar 29 2023 Packit <hello@packit.dev> - 82-1
Changes with 82
----------------
  * CI: update fedora-38 images (#1273)
  * ci: update manifest tests (#1242)
  * rpmbuild: build on fedora-38 (#1268)
  * stages: add ovf stage (#1266)
  * test: this test requires to be able to bindmount (#1261)

Contributions from: Jakub Rusz, Sanne Raymaekers, Simon de Vlieger, Thomas Lavocat

— Somewhere on the Internet, 2023-03-29


* Mon Feb 27 2023 Tomáš Hozza <thozza@redhat.com> - 81-1
Changes with 81
----------------
  * stages/ignition: support multi kargs in network kcmdline (#1249)

Contributions from: Antonio Murdaca, Thomas Lavocat

— Somewhere on the Internet, 2023-02-27


* Mon Feb 20 2023 Packit <hello@packit.dev> - 80-1
Changes with 80
----------------
  * stages/copy: add option to remove destination before copying (#1241)
  * stages/shell.init: add pattern for env var names (#1239)

Contributions from: Achilleas Koutsou, Tomáš Hozza

— Somewhere on the Internet, 2023-02-20


* Wed Feb 15 2023 Packit <hello@packit.dev> - 79-1
Changes with 79
----------------
  * New stage: org.osbuild.shell.init (#1234)
  * mounts: add the norecovery option for xfs and ext4 (#1238)

Contributions from: Achilleas Koutsou, Thomas Lavocat

— Somewhere on the Internet, 2023-02-15


* Tue Feb 07 2023 Packit <hello@packit.dev> - 78-1
Changes with 78
----------------
  * Add org.osbuild.chown stage  (#1228)
  * mounts: accept a wider set of mount options (#1229)

Contributions from: Thomas Lavocat, Tomáš Hozza

— Somewhere on the Internet, 2023-02-07


* Fri Jan 20 2023 Packit <hello@packit.dev> - 77-1
Changes with 77
----------------
  * CI deploy script and SSH keys cleanup (#1225)
  * stages/mkdir: revert explicitly setting mode using `os.chmod` (#1227)

Contributions from: Tomáš Hozza

— Somewhere on the Internet, 2023-01-20


* Thu Jan 19 2023 Packit <hello@packit.dev> - 76-1
Changes with 76
----------------
  * sources/ostree: fix quotation marks in mTLS remote options (#1222)
  * stages/mkdir: explicitly set mode using `chmod` and support handling of existing directories (#1224)

Contributions from: Ondřej Budai, Sanne Raymaekers, Tomáš Hozza

— Somewhere on the Internet, 2023-01-18


* Wed Jan 04 2023 Packit <hello@packit.dev> - 75-1
Changes with 75
----------------
  * runners: add Fedora Asahi runner (#1216)
  * stages/rhsm.facts: create facts file in /etc (#1220)
  * test/objectstore: use os.stat instead Path.stat (#1217)

Contributions from: Achilleas Koutsou, Christian Kellner, Eric Curtin

— Somewhere on the Internet, 2023-01-04



* Wed Dec 21 2022 Packit <hello@packit.dev> - 74-1
Changes with 74
----------------
  * Clamp mtime to `source-epoch` if specified (#1207)
  * New `ostree.encapsulate` for "native ostree containers" (#1091)
  * [v2] util/fscache: introduce versioning (#1198)
  * fscache: post-merge improvements (#1211)
  * ostree.config: add aboot (Android) bootloader config option (#1204)
  * runners: add AutoSD runner (#1210)
  * schutzbot: set the cache size for the correct store (#1199)
  * stages/users: accept identical uid for existing users (#1188)
  * test/fscache: drop PathLike annotation (#1196)
  * test/stages/users: ignore non-deterministic files (#1197)
  * test: convert objectstore test to pytest (#1201)
  * util/fscache: add cachedir-tag support (#1212)
  * util: fix typo in get_consumer_secrets (#1200)
  * 🗄Write and read metadata from the store and integrate `FsCache` into `ObjectStore` (#1187)

Contributions from: Christian Kellner, David Rheinsberg, Eric Curtin, Sanne Raymaekers

— Somewhere on the Internet, 2022-12-21



* Wed Dec 07 2022 Packit <hello@packit.dev> - 73-1
Changes with 73
----------------
  * cache: provide FsCache utility for concurrent caches (#1130)
  * ci: use the latest terraform to fix missing images (#1185)
  * mounts: use the options object for mountopts (#1182)
  * schutzfile: update manifest-db ref 2022-12-05 (#1194)

Contributions from: David Rheinsberg, SchutzBot, Thomas Lavocat

— Somewhere on the Internet, 2022-12-07



* Wed Nov 23 2022 Packit <hello@packit.dev> - 72-1
Changes with 72
----------------
  * UKI: Add support for building unified kernel images (#1167)
  * Update snapshots to 20221115 (#1177)
  * `objectstore`: use direct path input/output for `Object` (#1179)
  * `stages/containers.storage.conf`: ability to specify a base file  (#1173)
  * devices: tolerate existing device nodes (#1181)
  * grub2.iso: add timeout option (#1175)
  * ignition: fix ignition_network_kcmdline (#1172)
  * test/data: persist the journal for ostree images (#1178)
  * ❌ 🐮 Remove copy-on-write support for `Object` (no-cow) (#1169)

Contributions from: Antonio Murdaca, Christian Kellner, Thomas Lavocat, schutzbot

— Somewhere on the Internet, 2022-11-23



* Wed Nov 09 2022 Packit <hello@packit.dev> - 71-1
Changes with 71
----------------
  * Extend firewall stage to add sources (continues from PR #1137) (#1157)
  * Update snapshots to 20221025 (#1159)
  * Update snapshots to 20221028 (#1161)
  * ci(lint): add shell linter - Differential ShellCheck (#1147)
  * ci: update to containers/privdocker@552e30c (#1166)
  * ci: upgrade to actions/checkout@v3 (#1165)
  * osbuild-dev: a new tool to help with manifests (#1152)
  * osbuild-mpp: recognize manifest without mediaType and with manifests fields as a list (#1168)
  * stages/ostree.preptree: link to rpm-ostree code (#1151)
  * stages: add new cpio.out stage (#1164)
Contributions from: Antonio Murdaca, Christian Kellner, Colin Walters, David Rheinsberg, Irene Diez, Jan Macku, Simon de Vlieger, Ygal Blum, schutzbot
— Somewhere on the Internet, 2022-11-09





* Wed Oct 26 2022 Packit <hello@packit.dev> - 70-1
Changes with 70
----------------
  * Build rpms on RHEL 8.8 and 9.2 (#1141)
  * packit: Replace deprecated config options (#1145)
  * schutzbot/mockbuild: stop running mock as root (#1148)
  * schutzfile: update manifest-db ref 2022-10-20 (#1155)
  * sources/ostree: set contenturl when pulling from remote (#1140)
  * stages/keymap: add font option (#1158)
  * stages/logind-systemd: add `ReserveVT` option (#1156)
  * stages/rpm: make the fake machine-id newline-terminated (#1150)
  * stages: add systemd-journald stage (#1143)
  * test: add README.md on how to make tests for stages (#1149)
Contributions from: Christian Kellner, Irene Diez, Jakub Rusz, Jan Macku, Ondřej Budai, Sanne Raymaekers, SchutzBot
— Somewhere on the Internet, 2022-10-26





* Wed Oct 12 2022 Packit <hello@packit.dev> - 69-1
Changes with 69
----------------
  * runners: auto detection based on best matching distro+version (#996)
  * sources/ostree: pull from remote using rhsm mTLS certs (#1138)
  * stages: fix ostree config stage (#1129)
Contributions from: Antonio Murdaca, Christian Kellner, Sanne Raymaekers
— Somewhere on the Internet, 2022-10-12





* Wed Sep 28 2022 Packit <hello@packit.dev> - 68-1
Changes with 68
----------------
  * manifest-db: propage the osbuild SHA on manifest-db (#1124)
  * packit: Enable Bodhi updates for unstable Fedoras (#1128)
  * packit: add epel-9 to copr_build (#1118)
  * selinux: Update based on latest packaging guide (#1127)
  * stages/greenboot: avoid new pylint suppressions (#1114)
  * test/src: improve file enumeration (#1106)
Contributions from: David Rheinsberg, Ondřej Budai, Simon Steinbeiss, Thomas Lavocat, Vit Mojzis
— Somewhere on the Internet, 2022-09-28





* Wed Sep 14 2022 Packit <hello@packit.dev> - 67-1
Changes with 67
----------------
  * Quote URL paths before downloading in curl source (#1100)
  * Use isort to sort all imports (#1087)
  * ci: remove the composer image test (#1110)
  * org.osbuild.oci-archive: Support setting Entrypoint (#1103)
  * osbuild-mpp: Add url option to mpp-embed (#1104)
  * osbuild-mpp: fix minor issues and coding-style (#1112)
  * osbuild: explicit encodings for `open()` (#1108)
  * osbuild: pylint version fixes (#1094)
  * osbuild: share terminal formats between files (#1072)
  * packit: Enable Bodhi updates workflow (#1102)
  * rpmbuild: add fedora-37 (#1101)
  * test: run mypy in test-src not in GH actions (#1093)
  * tree: fix newer pylint warnings (#1107)
Contributions from: Achilleas Koutsou, Alexander Larsson, David Rheinsberg, Simon Steinbeiss, Simon de Vlieger, Thomas Lavocat, Ygal Blum
— Somewhere on the Internet, 2022-09-14





* Wed Aug 31 2022 Packit <hello@packit.dev> - 66-1
Changes with 66
----------------
  * test: manifests testing on each PR (#1052)
Contributions from: Thomas Lavocat
— Somewhere on the Internet, 2022-08-31





* Fri Aug 26 2022 Packit <hello@packit.dev> - 65-1
Changes with 65
----------------
  * Add greenboot configuration management via osbuild (#1086)
  * Add new properties to ostree.remotes stage: gpgkeypath and contenturl (#1097)
  * pipeline: include mounts in stage checksum (#1098)
  * runners: add fedora38 (#1092)
Contributions from: Achilleas Koutsou, Christian Kellner, Ondřej Budai, Sayan Paul
— Somewhere on the Internet, 2022-08-26





* Wed Aug 17 2022 Packit <hello@packit.dev> - 64-1
Changes with 64
----------------
  * Ability to mark installation as `ostree-booted` (#1085)
  * Add org.osbuild.gcp.guest-agent.conf stage (#1080)
  * Check source via `autopep8` (#1083)
  * `stages/gcp.guest-agent.conf`: various small fixes (#1081)
  * osbuild-mpp: Allow use of mpp-* operations for stages (#1084)
  * stages/rpm: allow setting the dbpath (#666)
Contributions from: Alexander Larsson, Christian Kellner, fkolwa
— Somewhere on the Internet, 2022-08-17





* Wed Aug 03 2022 Packit <hello@packit.dev> - 63-1
Changes with 63
----------------
  * stage: add an rhsm.facts stage (#1060)
Contributions from: Simon de Vlieger
— Somewhere on the Internet, 2022-08-03





* Wed Jul 27 2022 Packit <hello@packit.dev> - 62-1
Changes with 62
----------------
  * COMPOSER-1622: Enable Fedora 36 testing (#1061)
  * `stages/container.storage.conf`: fix `filename` property lookup (#1077)
  * mounts: minor fixes with no functional changes (#1076)
  * schema: assorted fixes for schema formatting and handling (#1079)
  * stages/containers.storage.conf: support pytoml (#1078)
  * stages/users: support a dot inside a username (#1075)
Contributions from: Alexander Todorov, Christian Kellner, David Rheinsberg, Ondřej Budai
— Somewhere on the Internet, 2022-07-27





* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Packit <hello@packit.dev> - 61-1
Changes with 61
----------------
  * Add new `containers.storage.conf` stage to edit `containers-storage.conf(5)` files (#1069)
  * docs: update osbuild(1) (#1068)
  * osbuild: fix current partial type annotations (#1067)
  * source/skopeo: use subprocess.check_output (#1071)
  * stages/skopeo: use extra intermediate download dir (#1074)
  * tests: Run tests on RHEL 9.1 and 8.7 nightly (#1051)
Contributions from: Christian Kellner, David Rheinsberg, Jakub Rusz, Simon de Vlieger
— Somewhere on the Internet, 2022-07-20





* Wed Jul 06 2022 Packit <hello@packit.dev> - 60-1
Changes with 60
----------------
  * Add `_install langs` support (#1064)
  * Add a Vagrant libvirt stage (#947)
  * `stages/dnf.config`: ability to configure rpm transaction flags (#1063)
  * `stages/oci-archive`: small cleanups (#1062)
  * ci: push tags to gitlab (#1058)
  * git: ignore common virtual env locations (#1066)
  * main: add a --version argument (#1039)
  * osbuild-mpp: small python cleanups (#1056)
  * rpmbuild: add fedora-36 (#1053)
  * stages: OpenSCAP remediation at build time (#1059)
  * stages: add new org.osbuild.rpmkeys.import stage (#1057)
Contributions from: Christian Kellner, Gianluca Zuccarelli, Jakub Rusz, Jelle van der Waa, Simon de Vlieger
— Somewhere on the Internet, 2022-07-06





* Wed Jun 22 2022 Packit <hello@packit.dev> - 59-1
Changes with 59
----------------
  * Remove `options` from the v1 result (#1044)
  * Run rpmbuild on new nightlies. (#1049)
  * Support calling curl with --insecure (#1047)
  * ci: Adjust release schedule timer (#1045)
  * stages/mkfs.fat: pass `-I` command line option (#1050)
  * stages/qemu: expose vpc options (#1046)
  * store: various code cleanups (#1032)
Contributions from: Achilleas Koutsou, Christian Kellner, Jakub Rusz, Simon Steinbeiss
— Somewhere on the Internet, 2022-06-22





* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 58-2
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Packit <hello@packit.dev> - 58-1
Changes with 58
----------------
  * COMPOSER-1576: rpmbuild on 8.6 and 9.0 ga (#1043)
  * `grub2.legacy`: stricter schema, replace `architecture` with `bios.platform`  (#1035)
  * `stages/grub2.legacy`: small schema fixes (#1034)
  * stages: add OpenSCAP first boot remediation (#1033)
  * tests: handle `-` in the sfdisk version test (#1037)
Contributions from: Alexander Todorov, Christian Kellner, Gianluca Zuccarelli, Simon de Vlieger
— Somewhere on the Internet, 2022-06-08





* Wed May 25 2022 Packit <hello@packit.dev> - 57-1
Changes with 57
----------------
  * meta: show stage name when schema is missing (#1022)
  * sources: curl max_workers 2 * num_cpus (#1024)
  * stages/ostree.passwd: fix subid source path (#1027)
  * stages/udev.rules: use correct separator (#1026)
  * stages: add new sgdisk stage (#1029)
Contributions from: Christian Kellner, Simon de Vlieger
— Somewhere on the Internet, 2022-05-25





* Wed May 11 2022 Packit <hello@packit.dev> - 56-1
Changes with 56
----------------
  * Re-enable pylint warning W0201 (attribute-defined-outside-init) (#1019)
  * Restrict capabilities is stages (#1010)
  * org.osbuild.luks2.format: Support dm-integrity (#1015)
  * packit: Enable Koji build integration (#1021)
  * sources: refactor the SourceService class (#998)
  * stage/ostree.passwd: also merge /etc/sub{u,g}id (#1013)
  * stages: add new org.osbuild.udev.rules stage (#1018)
  * test: remove old `pipelines` contents & directory (#1011)
Contributions from: Alexander Larsson, Christian Kellner, Simon Steinbeiss, Thomas Lavocat
— Somewhere on the Internet, 2022-05-11





* Thu Apr 28 2022 Packit <hello@packit.dev> - 53.1-1
CHANGES WITH 53.1:
----------------
 * devices/lvm2.lv: add support for lvm devices files (#1009)
Contributions from: Christian Kellner
— Liberec, 2022-04-28




* Wed Apr 27 2022 Packit <hello@packit.dev> - 55-1
Changes with 55
----------------
  * Support specifying multiple devices in all mkfs versions (like xfs) (#1004)
  * buildroot: don't explicitly add `CAP_MAC_ADMIN` (#1008)
  * devices/lvm2.lv: add support for lvm devices files (#1009)
  * inputs/org.osbuild.tree: fix typo (#1006)
  * inputs: support array of objects references (#1003)
  * workflows/trigger-gitlab: run Gitlab CI in new image-builder project (#1002)
Contributions from: Alexander Larsson, Christian Kellner, Jakub Rusz, Jelle van der Waa
— Somewhere on the Internet, 2022-04-27





* Wed Apr 13 2022 Packit <hello@packit.dev> - 54-1
Changes with 54
----------------
  * Allow specifying subformat for the `vmdk` type in `org.osbuild.qemu` stage (#999)
  * Pin rpmrepo snapshots for CI runners + use them in mockbuild + ci improvements (#1001)
  * Support VMDK subformat in qemu assembler (#1000)
Contributions from: Jakub Rusz, Tomas Hozza
— Somewhere on the Internet, 2022-04-13





* Thu Mar 24 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 53-1
CHANGES WITH 53:
----------------
  * stages/sfdisk: support changing GPT partition attribute bits (#966)
  * Enable scheduled upstream releases (#997)
  * stages/rpm: don't verify package or header signatures when installing (#995)
  * stages/selinux: directly call setfilecon (#993)
  * stages/selinux: directly call setfilecon (#993)
  * stages/selinux: directly call setfilecon (#993)
  * stages/selinux: directly call setfilecon (#993)
  * sources/curl: don't limit total download time (#990)
  * Packit: build SRPMs in Copr (#987)
Contributions from: Christian Kellner, Enric Balletbo i Serra, Laura Barcziova, Simon Steinbeiss, Tom Gundersen, Tomas Hozza
— Somewhere on the Internet, 2022-03-24





* Fri Mar 04 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 52-1
CHANGES WITH 52:
----------------
  * `stages/grub2`: write GRUB_DEFAULT on saved_entry (#981)
  * `stages/firewall`: fix fail when setting only the default zone (#984)
  * `stages/rpm`: option to import gpg keys from tree (#985)
  * LVM2: separate stderr, stdout (#982)
  * Extend firewall stage to set the default zone (#980)
  * runners: add org.osbuild.fedora37 (#983)
  * ci/deploy: use public EPEL-9 (#979)
Contributions from: Christian Kellner, Jakub Rusz, Tomas Hozza, Thomas
Lavocat
— Wien, 2022-03-04




* Wed Mar 02 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 51-1
CHANGES WITH 51:
----------------
  * stages: add the ability to configure pacman repos (#955)
Contributions from: Jelle van der Waa, Simon Steinbeiß
Grenoble Location, 2022-03-02




* Sun Feb 27 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 50-1
CHANGES WITH 50:
----------------
  * util/udev: fix path for udev device inhibitor (#976)
  * Add RHEL-9.1 runner (#975)
Contributions from: Christian Kellner, Tomas Hozza
— Vöcklabruck, 2022-02-27




* Wed Feb 23 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 49-1
CHANGES WITH 49:
----------------
  * `stages/fdo`: add new stage (#857)
  * `stages/clevis-luks-bind`, `stages/luks-remove-key`: add new stages (#967)
  * `stages/oci-archive`: fix creation time format (#973)
  * rpmbuild: run on centos-9 (#974)
  * Host.Service: add signals (#969)
Contributions from: Antonio Murdaca, Christian Kellner, Chloe Kaubisch, Jakub Rusz,
                    Thomas Lavocat
— Vöcklabruck, 2022-02-23




* Wed Feb 16 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 48-1
CHANGES WITH 48:
----------------
  * skopeo stage: remove overlay/backingFsBlockDev file after install (#970)
  * Add support for embedding containers in images (#952)
  * Initial work on more reproducible builds (#962)
  * Bootiso: add the option to compress using lz4 (#951)
  * runners: add rhel-87 (#963)
Contributions from: Alexander Larsson, Christian Kellner, Jakub Rusz, Ondřej Budai, Roy Golan, Thomas Lavocat, jkozol
— Berlin, 2022-02-16




* Wed Feb 02 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 47-1
CHANGES WITH 47:       ----------------   * `util/linux`: fix BLK_IOC_FLSBUF on ppc64le (osbuild#954)   * ci: make jobs interruptible (osbuild#902)   * `test/ci`: fix sonarqube run on main (osbuild#950)   * Enable Sonarqube scan (osbuild#898)
Contributions from: Christian Kellner, Jakub Rusz, Simon Steinbeiss
— Berlin, 2022-02-02



* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 46-1
CHANGES WITH 46:
----------------
  * Add the option of compressing using lz4 (#946)
Contributions from: Thomas Lavocat, Tomáš Hozza
— Vöcklabruck, 2022-01-19




* Fri Jan 07 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 45-1
NGES WITH 45:
----------------
  * `stages/grub2`: ability to not write kernel cmdline (#939)
  * Arch legacy grub compatibility (#941)
  * org.osbuild.kickstart adjustments (#943)
  * Fix typo in tar stage schema option enum (#940)
  * Add mkinitcpio stage (#937)
  * stages: allow using sysconfig stage multiple times. (#938)
  * objectstore: don't store objects by their treesum (#861)
Contributions from: Christian Kellner, Jelle van der Waa, Ondřej Budai, Tom Gundersen, Tomáš Hozza, Simon Steinbeiss
— Drásov (Brno-venkov), 2022-01-07




* Thu Dec 16 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 44-1
CHANGES WITH 44:
----------------
  * LUKS (v2) support (#879)
  * osbuild-mpp: Add support for a pacman resolver (#911)
  * `stages/dnf-automatic`: add new stage for configuring DNF Automatic (#936)
  * `stages/yum.repos`: add new stage for creating YUM / DNF repo files (#932)
  * `stages/users`: explicitly create a home directory (#929)
  * `stages/dnf`: edit /etc/dnf/dnf.conf (#928)
  * `stages/sshd`: support PermitRootLogin option (#917)
  * build root: isolate container environment from the host and set `CONTAINER` (#926)
  * Small fix for `mounts/ostree.deployment` and an order check for `depsolve` (#915)
  * Added poll() with a time out of 10 minutes for building images (#888, #918)
  * Apply autopep8 to osbuild-mpp and resolve Constructor is undefined (#914)
  * Support for on demand pipeline building (#855)
  * util/rmrf: handle broken symlinks (#913)
Contributions from: Aaron Hetherington, Achilleas Koutsou, Christian Kellner, Jelle van der Waa,
                    Ondřej Budai, Sanne Raymaekers, Simon Steinbeiss, Tomas Hozza
— Vöcklabruck, 2021-12-16




* Wed Dec 01 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 43-1
CHANGES WITH 43:
----------------
  * Buildroot: mask `/proc/cmdline` (#895)
  * stages/grub2.inst: Make grub-mkimage binary configurable (#905)
  * tests: enable testing on aarch64 RHEL (#844)
  * gitignore: Ignore generated man pages (#903)
  * stages/ostree.fillvar: fill the correct var (#904)
  * osbuild-mpp: Allow importing multiple pipelines from a manifest (#900)
  * ci: switch to rhel-9 runners (#901)
  * spec: require python3-pyyaml for osbuild-tools (#899)
  * osbuild-mpp: Support loading yaml as well as json files (#893)
  * CI: update the osbuild-ci container (#896)
  * osbuild: Add org.osbuild.gunzip stage (#886)
  * osbuild-mpp: Report the path of the json file when parsing fails (#890)
  * packit: enable copr builds for CS9 on main (#894)
  * tools/osbuild-mpp: add ability to embed files (#859)
  * osbuild-mpp: Add mpp-if feature (#885)
Contributions from: Alexander Larsson, Christian Kellner, Jakub Rusz, Jelle van der Waa, Ondřej Budai, kingsleyzissou
— Berlin, 2021-12-01


















* Thu Nov 18 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 42-1
CHANGES WITH 42:
----------------
  * packit: enable copr build for CS9 (#887)
  * test/lvm2: use LoopControl.loop_for_fd (#884)
  * packit: Use upstream github release description (#880)
Contributions from: Christian Kellner, Ondřej Budai, Simon Steinbeiss
— Cork, 2021-11-17
-----BEGIN PGP SIGNATURE-----
iQIzBAABCAAdFiEErKmAeFdguKfr5RbZC04GHB6SbNcFAmGU3x8ACgkQC04GHB6S
bNcXqBAAxWLL5kFhhrbboXShLmgdVbryYv8muxsyF0YFdE8qHdJmwDZkURoUH2Mh
RzWDl4Lq1FKoGJZ6WP3S0/Mj/8cpHhhXSnUzcGZamz6hJrsoyeUfYRQrB67/Mkm5
HEWWMxYBA1qvf+tfzVAr4BjlUfmDAHqjbRu5loHqANJSKNCmcg2jrHnvV5VrjBQf
t1NCQOm960kik5gjFfAemsmEYlkPN8MtD/VxxUJC2dKCDkY7tQBITB+40fB0lDdF
EIODFooKE0b2rXumEJUr95V6vGmmEOyFOcsOajls58pJSbak01g2I6J6WpSb9EiS
RZbhNYhh59BKNrsbfpO8JAYrqVy+OyPZxTwdpIUYbP4KndNbGe/QH5L/Vbdt1Dv9
HokDnTGD2jLrHyK1HP+NkjHmGy+s5XCiFwtFPbZeI7RIgxugIkJjM985u9vi0Ufd
uzbI0DP302DRiafXgR9CX/YXkEWjHpu8RSeoFsbTj6KzSAZtacK7gXWcSF5TUMlZ
kGVGy/b9xz5Ily2SOI07FBNMCHH705BRXsZGuugPlmslACTEVUh377DpvYcgBHVx
oclxqFXW17xwcxCrC6JBcXM9h2h59KJ60BSGnVHpg2bdqZat01we1p2rbcN6Dn2H
45KWO7O678oRBnIpt4lsnY/Avs7DZ83HfX4ctNfcgdwRDISFyts=
=jsoz
-----END PGP SIGNATURE-----








* Wed Nov 17 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 42-1
CHANGES WITH 42:
----------------
  * packit: enable copr build for CS9 (#887)
  * test/lvm2: use LoopControl.loop_for_fd (#884)
  * packit: Use upstream github release description (#880)
Contributions from: Christian Kellner, Ondřej Budai, Simon Steinbeiss
— Cork, 2021-11-17
-----BEGIN PGP SIGNATURE-----
iQIzBAABCAAdFiEErKmAeFdguKfr5RbZC04GHB6SbNcFAmGU3x8ACgkQC04GHB6S
bNcXqBAAxWLL5kFhhrbboXShLmgdVbryYv8muxsyF0YFdE8qHdJmwDZkURoUH2Mh
RzWDl4Lq1FKoGJZ6WP3S0/Mj/8cpHhhXSnUzcGZamz6hJrsoyeUfYRQrB67/Mkm5
HEWWMxYBA1qvf+tfzVAr4BjlUfmDAHqjbRu5loHqANJSKNCmcg2jrHnvV5VrjBQf
t1NCQOm960kik5gjFfAemsmEYlkPN8MtD/VxxUJC2dKCDkY7tQBITB+40fB0lDdF
EIODFooKE0b2rXumEJUr95V6vGmmEOyFOcsOajls58pJSbak01g2I6J6WpSb9EiS
RZbhNYhh59BKNrsbfpO8JAYrqVy+OyPZxTwdpIUYbP4KndNbGe/QH5L/Vbdt1Dv9
HokDnTGD2jLrHyK1HP+NkjHmGy+s5XCiFwtFPbZeI7RIgxugIkJjM985u9vi0Ufd
uzbI0DP302DRiafXgR9CX/YXkEWjHpu8RSeoFsbTj6KzSAZtacK7gXWcSF5TUMlZ
kGVGy/b9xz5Ily2SOI07FBNMCHH705BRXsZGuugPlmslACTEVUh377DpvYcgBHVx
oclxqFXW17xwcxCrC6JBcXM9h2h59KJ60BSGnVHpg2bdqZat01we1p2rbcN6Dn2H
45KWO7O678oRBnIpt4lsnY/Avs7DZ83HfX4ctNfcgdwRDISFyts=
=jsoz
-----END PGP SIGNATURE-----








* Mon Nov 08 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 41-1
- stages/authconfig: run authconfig (Tom Gundersen)
- stages/yum.config: add an option to configure langpacks plugin (Ondřej Budai)
- formats/v2: fix describe for mount without source (Christian Kellner)
- stages/selinux: ability to force an auto-relabel (Christian Kellner)
- stages/pwquality.conf: set pwquality configuration (Tom Gundersen)
- stages/rhsm: add support to configure yum plugins (Christian Kellner)
- stages/rhsm: extract plugins defintion (Christian Kellner)
- Add new `org.osbuild.yum.config` stage (Tomas Hozza)
- test/cloud-init: add new options to stage test (Achilleas Koutsou)
- stages/cloud-init: disable default_flow_style when writing configs (Achilleas Koutsou)
- stages/cloud-init: add support for configuring output logging (Achilleas Koutsou)
- stages/cloud-init: add support for configuring reporting handlers (Achilleas Koutsou)
- stages/cloud-init: add support for configuring Azure datasource (Achilleas Koutsou)
- stages: add new org.osbuild.cron.script stage (Christian Kellner)
- stages/grub2: add support for terminal, serial and timeout config (Ondřej Budai)
- stages/waagent.conf: set WALinuxAgent configuration (Tom Gundersen)
- stages/sshd.config: set sshd configuration (Tom Gundersen)
- Support 'install' command in org.osbuild.modprobe stage (Tomas Hozza)
- Post release version bump (msehnout)

* Wed Nov 03 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 40-1
- stages/lvm2.create: fix 'size' and add 'extents' (Christian Kellner)
- Let schutzbot do the post-release version bump (Simon Steinbeiss)
- test/data: use ostree.deployment in fedora image (Christian Kellner)
- mounts: add new ostree.deployment service (Christian Kellner)
- mounts: include tree directory in arguments (Christian Kellner)
- mounts: allow empty returns from service (Christian Kellner)
- mounts: separate file system mount service (Christian Kellner)
- meta: allow mounts for all stages (Christian Kellner)
- schema/v2: make mount source and target optional (Christian Kellner)
- mounts: change schema meta information (Christian Kellner)
- mounts: introduce new mount manager class (Christian Kellner)
- devices: add device path helper functions (Christian Kellner)
- devices: introduce new device manager class (Christian Kellner)
- test/data: add RHEL 7 manifests (Christian Kellner)
- test/stages: add check for `parted` stage (Christian Kellner)
- runners: add rhel7 runner (Christian Kellner)
- stages/grub2.legacy: new stage for non-bls config (Christian Kellner)
- stages/parted: new stage to partition a device (Christian Kellner)
- pipeline: don't bind-mount /boot from the host (Christian Kellner)
- buildroot: make mounting /boot optional (Christian Kellner)
- setup.cfg: increase max-statements to 75 (Christian Kellner)
- runners: add new centos9 runner (Christian Kellner)
- ci: remove 8.5 nightly testing (Ondřej Budai)
- mpp: fix long options (Christian Kellner)
- osbuild-mpp: Set the "arch" variable to the current rpm arch (Alexander Larsson)
- osbuild-mpp: Better handling of variable defaults and propagation (Alexander Larsson)
- osbuild-mpp: Better handling of -D overrides (Alexander Larsson)
- osbuild-mpp: Allow using formating in depsolver node (Alexander Larsson)
- osbuild-mpp: Add mpp-join (Alexander Larsson)
- osbuild-mpp: Add mpp-eval (Alexander Larsson)
- Fix GitHub Action tag pattern (Simon Steinbeiss)
- mockbuild: reuse mock repos from the system ones (Ondřej Budai)
- mockbuild: rotate a variable name (Ondřej Budai)
- gitlab: don't save journal (Ondřej Budai)
- deploy: update to the latest composer commit (Ondřej Budai)
- ci: don't register the runners (Ondřej Budai)
- trigger-gitlab: do not interpret the fetch_pulls outputs (Ondřej Budai)
- Bump version numbers ahead of release (Simon Steinbeiss)
- Switch to simple upstream releases (Simon Steinbeiss)
- stages/grub2.inst: ensure /var/tmp exists (Christian Kellner)
- devices/loopback: remove extra "'" from print (Christian Kellner)
- tests/ci: Switch to testing on 8.4 GA (Jakub Rusz)
- tests: enable testing on RHEl-8.5 and RHEL-9.0 (Jakub Rusz)
- .github: Write PR data to a file first in trigger-gitlab (Sanne Raymaekers)
- README: Add a link to our developer guide (Simon Steinbeiss)

* Wed Oct 06 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 39-1
- 39 (Thomas Lavocat)
- packit: enable builds on ppc64le (Tomas Hozza)
- CI: rename rhel-8.5 runners to rhel-8.5-nightly (Achilleas Koutsou)
- mockbuild: add RHEL 8.6 (Achilleas Koutsou)
- docs: document osbuild and selinux integration (Christian Kellner)
- ci: trigger gitlab from checks not tests (Christian Kellner)
- ci: split out checks from tests (Christian Kellner)
- .github: Get PR number from sha (Sanne Raymaekers)
- .github: Use the workflow_run event data in trigger-gitlab (Sanne Raymaekers)
- ci: trigger gitlab ci via workflow run event (Christian Kellner)

* Mon Sep 27 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 38-1
- 38 (Simon Steinbeiss)
- Copy the local_vars dictionary to avoid eval modifying it (Pierre-Yves Chibon)
- Add support for defining variables from other variables or basic expression (Pierre-Yves Chibon)
- test/host: checks for invalid fd handling (Christian Kellner)
- host: check reply_fds before sending them (Christian Kellner)
- host: raise a protocol error for empty messages (Christian Kellner)
- sources: pass items via temporary file (Christian Kellner)
- test/host: add check for call with fds (Christian Kellner)
- host: properly clean up passed fds (Christian Kellner)
- stages/qemu: fix 'compat' option (Christian Kellner)

* Wed Sep 22 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 37-1
- 37 (Martin Sehnoutka)
- sources: port to host services (Christian Kellner)
- org.osbuild.curl: Don't load secrets if not needed (Alexander Larsson)
- pipeline: split out downloading from building (Christian Kellner)
- Fix the assert as `.sort()`  returns None (Pierre-Yves Chibon)
- schutzbot: Update terraform sha (Sanne Raymaekers)
- packit: Propose PRs to all Fedoras (Simon Steinbeiss)
- stages: pam_limits.conf → pam.limits.conf (Christian Kellner)
- Add a new stage for configuring `pam_limits` module (Tomas Hozza)
- ostree.config: add `bootloader` config option (Christian Kellner)
- Add a new stage for setting kernel parameters via sysctl.d (Tomas Hozza)

* Wed Sep 08 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 36-1
- 36 (Diaa Sami)
- Add a new stage `org.osbuild.tmpfilesd` for configuring tmpfiles.d (Tomas Hozza)
- Add a new stage for configuring SELinux state on the system (Tomas Hozza)
- Add a new `org.osbuild.dnf.config` stage for configuring DNF (Tomas Hozza)
- Add new `org.osbuild.tuned` stage for setting active TuneD profile (Tomas Hozza)
- util/rhsm: Check if repositories is None before iterating (Sanne Raymaekers)
- stages/kickstart: set passwords with --iscrypted (Achilleas Koutsou)

* Sun Aug 29 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 35-1
- 35 (Tom Gundersen)
- stages/kickstart: quote ssh-key (Christian Kellner)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1-3
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Martin Sehnoutka <msehnout@redhat.com> - 1-2
- update upstream URL to the new Github organization

* Wed Jul 17 2019 Martin Sehnoutka <msehnout@redhat.com> - 1-1
- Initial package
