%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})

# unfortunately, radicale major version upgrades are breakable updates, therefore
# Fedora >= 31: introduce radicale3
#
# Note: this is the simplified spec file for Fedora

### supports following defines during RPM build:
#
### specific git commit on upstream (EXAMPLE)
## build SRPMS
# fedpkg srpm --define "gitcommit 49d0ad5b18a3867925e2ffd1d8cec21d99e13b3e" -- --undefine=_disable_source_fetch
#
## build RPMS local
# fedpkg local --define "gitcommit 49d0ad5b18a3867925e2ffd1d8cec21d99e13b3e" -- --undefine=_disable_source_fetch
#
## rebuild SRPMS on a different system using
# rpmbuild --rebuild -D "gitcommit 49d0ad5b18a3867925e2ffd1d8cec21d99e13b3e" radicale3-<VERSION>-<RELEASE>.YYYYMMDDgitSHORTHASH.DIST.src.rpm

%define	radicale_major	3

%define	radicale_version	3.2.3
%define	radicale_release	1

%define	radicale_name	radicale

%define	radicale_package_name	radicale3

%if 0%{?gitcommit:1}
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%global gittag .%{build_timestamp}git%{shortcommit}
%endif

Name:             radicale
Version:          %{radicale_version}
Release:          %{radicale_release}%{?gittag}%{?dist}
Summary:          A simple CalDAV (calendar) and CardDAV (contact) server
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later
URL:              https://radicale.org

%if 0%{?gitcommit:1}
Source0:          https://github.com/Kozea/Radicale/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz
%else
Source0:          https://github.com/Kozea/Radicale/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

Source1:          %{name}.service
Source4:          %{name}.te
Source5:          %{name}.fc
Source6:          %{name}.if
Source7:          %{name}-tmpfiles.conf

Source50:	  %{name}-test-example.ics
Source51:	  %{name}-test-example.vcf

BuildArch:        noarch


%package -n %{radicale_package_name}
Summary:          %{summary}

BuildRequires:    python3-devel
BuildRequires:    systemd
BuildRequires:    checkpolicy
BuildRequires:    selinux-policy-devel
BuildRequires:    hardlink

# for 'make check' of major version 3.0.6
BuildRequires:    python3-defusedxml
BuildRequires:    python3-passlib
BuildRequires:    python3-vobject >= 0.9.6
BuildRequires:    python3-dateutil >= 2.7.3

Conflicts:        radicale < 3.0.0
Conflicts:        radicale2

Requires:         python3-%{radicale_package_name} = %{version}-%{release}
Requires(pre):    shadow-utils
%{?systemd_requires}
Suggests:         %{radicale_package_name}-selinux = %{version}-%{release}


%description
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.


%description -n %{radicale_package_name}
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.

THIS IS MAJOR VERSION %{?radicale_major}

UPGRADE BETWEEN MAJOR VERSIONS IS NOT SUPPORTED
	-> deinstall old major version
	-> install new version
	-> follow migration hints
Upgrade hints from major version 2 -> 3 can be found here:
 https://github.com/Kozea/Radicale/blob/v3.1.0/NEWS.md
  (section '3.0.0')


%package -n python3-%{radicale_package_name}
Summary:          Python module for Radicale
Recommends:       python3-bcrypt
Recommends:       python3-passlib
%py_provides      python3-%{name}
Obsoletes:        python-%{radicale_package_name} < %{version}-%{release}

Conflicts:        python3-radicale < 3.0.0
Conflicts:        python3-radicale2


%description -n python3-%{radicale_package_name}
Python module for Radicale


%package -n %{radicale_package_name}-httpd
Summary:        httpd config for Radicale
Requires:       %{radicale_package_name} = %{version}-%{release}
Requires:       httpd
Requires:       python3-mod_wsgi

Conflicts:        radicale-httpd < 3.0.0
Conflicts:        radicale2-httpd


%description -n %{radicale_package_name}-httpd
httpd example config for Radicale (Python3).


%package -n %{radicale_package_name}-selinux
Summary:        SELinux definitions for Radicale
Requires:       %{radicale_package_name} = %{version}-%{release}
%if "%{_selinux_policy_version}" != ""
Requires:         selinux-policy >= %{_selinux_policy_version}
%endif
Requires(post):   /usr/sbin/semodule
Requires(post):   /usr/sbin/fixfiles
Requires(post):   /usr/sbin/restorecon
Requires(post):   policycoreutils-python-utils
Requires(postun): /usr/sbin/semodule
Requires(postun): /usr/sbin/fixfiles
Requires(postun): /usr/sbin/restorecon
Requires(postun): policycoreutils-python-utils

%description -n %{radicale_package_name}-selinux
SELinux definitions for Radicale (Python3).

Note: storage hooks configuration is currently not supported by packaged
 SELinux policy and requires a local custom policy extension (RHBZ#1928899)


%prep
%if 0%{?gitcommit:1}
%define build_version %{gitcommit}
%else
%define build_version %{version}
%endif
%autosetup -n Radicale-%{build_version} -p 1

# inject SELinux note
sed -i 's|\(#hook =\)|# Note: storage hook configuration is currently not supported by packaged SELinux policy and requires a local custom policy extension (RHBZ#1928899)\n\1|' config

mkdir SELinux
cp -p %{SOURCE4} %{SOURCE5} %{SOURCE6} SELinux

# adjust _rundir according to definition
sed -i 's|\(/var/run\)|%{_rundir}|' SELinux/%{name}.fc

# restore original version after applying patches
sed -i 's|VERSION = "%{radicale_major}.dev"|VERSION = "%{radicale_version}"|' setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
cd SELinux

for selinuxvariant in %{selinux_variants}
do
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
    %{__mv} %{name}.pp %{name}.pp.${selinuxvariant}
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -


%install
%pyproject_install
%pyproject_save_files -l %{name}

# move scripts away from _bindir to avoid conflicts and create a wrapper scripts
install -d -p %{buildroot}%{_libexecdir}/%{name}
%{__mv} %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}/

cat > %{buildroot}%{_bindir}/%{radicale_name} << EOF
#!/bin/sh
if [ "\$(whoami)" != "%{name}" ]; then
    echo "This command must be run under the radicale user (%{name})."
    exit 1
fi
%{_libexecdir}/%{name}/%{radicale_name} \$@
EOF
chmod a+x %{buildroot}%{_bindir}/%{radicale_name}

# Install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 config %{buildroot}%{_sysconfdir}/%{name}/
sed -i 's|^#\(level =\).*|\1 info|' %{buildroot}%{_sysconfdir}/%{name}/config
install -p -m 640 rights %{buildroot}%{_sysconfdir}/%{name}/

# Empty configuration file
touch %{buildroot}%{_sysconfdir}/%{name}/users

# Install wsgi file
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 radicale.wsgi %{buildroot}%{_datadir}/%{name}/
sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' %{buildroot}%{_datadir}/%{name}/radicale.wsgi

# Install apache's configuration file
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 644 contrib/apache/radicale.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Create folder where the calendar will be stored (and radicale's home directory)
install -d -p  %{buildroot}%{_sharedstatedir}/%{name}/

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

install -D -p -m 644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_rundir}/%{name}

# adjust _rundir
sed -i 's|\(/var/run\)|%{_rundir}|' %{buildroot}%{_tmpfilesdir}/%{name}.conf
sed -i 's|\(/var/run\)|%{_rundir}|' %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_rundir}/%{name}

for selinuxvariant in %{selinux_variants}
do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
        %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done

%if 0%{?rhel} == 7 || 0%{?rhel} == 8
/usr/sbin/hardlink -cv %{buildroot}%{_datadir}/selinux
%else
/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux
%endif


%check
%pyproject_check_import

PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONPATH

# check whether radicale binary is at least displaying help
echo "Check whether 'radicale' is at least able to display online help"
%{buildroot}%{_libexecdir}/%{name}/%{radicale_name} --help >/dev/null
if [ $? -eq 0 ]; then
  echo "Check whether 'radicale' is at least able to display online help - SUCCESSFUL"
else
  exit 1
fi

# create radicale collections with examples
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf
cp %{SOURCE50} %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics/
cp %{SOURCE51} %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf/
echo '{"tag": "VADDRESSBOOK"}' >%{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf/.Radicale.props
echo '{"tag": "VCALENDAR"}'    >%{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics/.Radicale.props

echo "Check whether 'radicale' is able to verify example storage"
%{buildroot}%{_libexecdir}/%{name}/%{radicale_name} -D --verify-storage --storage-filesystem-folder /%{buildroot}%{_sharedstatedir}/%{name}
if [ $? -eq 0 ]; then
  echo "Check whether 'radicale' is able to verify example storage - SUCCESSFUL"
else
  exit 1
fi

# cleanup before packaging
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/collection-root
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/.Radicale.lock


%pre -n %{radicale_package_name}
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "Radicale service account" %{name}
exit 0


%post -n %{radicale_package_name}
%systemd_post %{name}.service


%post -n %{radicale_package_name}-selinux
for selinuxvariant in %{selinux_variants}
do
  if rpm -q selinux-policy-$selinuxvariant >/dev/null 2>&1; then
    echo "SELinux semodule store for %{radicale_package_name} ($selinuxvariant)"
    /usr/sbin/semodule -s ${selinuxvariant} -i \
      %{_datadir}/selinux/${selinuxvariant}/%{name}.pp
  else
    echo "SELinux semodule store for %{radicale_package_name} ($selinuxvariant) SKIPPED - policy not installed"
  fi
done
# http://danwalsh.livejournal.com/10607.html
if semanage port -l | grep -q "^radicale_port_t\s*tcp\s*5232$"; then
  echo "SELinux adjustments for %{radicale_package_name} port tcp/5232 already done"
else
  echo "SELinux adjustments for %{radicale_package_name} port tcp/5232"
  semanage port -a -t radicale_port_t -p tcp 5232
fi

echo "SELinux fixfiles for: %{radicale_package_name}"
/usr/sbin/fixfiles -R %{radicale_package_name} restore >/dev/null

if [ -d %{_localstatedir}/log/%{name} ]; then
  echo "SELinux restorecon for: %{_localstatedir}/log/%{name}"
  /usr/sbin/restorecon -R %{_localstatedir}/log/%{name}
fi


%post -n python3-%{radicale_package_name}
# nothing related included so far in radicale.fc
#echo "SELinux fixfiles for: python3-%{radicale_package_name}"
#/usr/sbin/fixfiles -R python3-%{radicale_package_name} restore >/dev/null


%post -n %{radicale_package_name}-httpd
# nothing related included so far in radicale.fc
#echo "SELinux fixfiles for: %{radicale_package_name}-httpd"
#/usr/sbin/fixfiles -R %{radicale_package_name}-httpd restore >/dev/null


%preun -n %{radicale_package_name}
%systemd_preun %{name}.service


%postun -n %{radicale_package_name}
%systemd_postun_with_restart %{name}.service 


%postun -n %{radicale_package_name}-selinux
if [ $1 -eq 0 ] ; then
  if semanage port -l | grep -q "^radicale_port_t\s*tcp\s*5232$"; then
    echo "SELinux delete for %{radicale_package_name} port tcp/5232"
    semanage port -d -p tcp 5232
  fi
  for selinuxvariant in %{selinux_variants}
  do
    if rpm -q selinux-policy-$selinuxvariant >/dev/null 2>&1; then
      echo "SELinux semodule reset %{radicale_package_name} ($selinuxvariant)"
      /usr/sbin/semodule -s ${selinuxvariant} -r %{name}
    else
      echo "SELinux semodule reset %{radicale_package_name} ($selinuxvariant) SKIPPED - policy not installed"
    fi
  done

  if [ -d %{_localstatedir}/log/%{name} ]; then
    echo "SELinux restorecon for: %{_localstatedir}/log/%{name}"
    /usr/sbin/restorecon -R %{_localstatedir}/log/%{name}
  fi
fi


%files -n %{radicale_package_name}
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/config
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/rights
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/users
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(750, %{name}, %{name}) %{_sharedstatedir}/%{name}/
%dir %{_datadir}/%{name}
%dir %attr(755, %{name}, %{name}) %{_rundir}/%{name}

%{_libexecdir}/%{name}


%files -n %{radicale_package_name}-selinux
%doc SELinux/*
%{_datadir}/selinux/*/%{name}.pp


%files -n python3-%{radicale_package_name} -f %{pyproject_files}


%files -n %{radicale_package_name}-httpd
%{_datadir}/%{name}/%{name}.wsgi
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf


%changelog
* Fri Aug 30 2024 Peter Bieringer <pb@bieringer.de> - 3.2.3-1
- Update to 3.2.3

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.2-1.2
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Peter Bieringer <pb@bieringer.de> - 3.2.2-1
- Update to 3.2.2
- Obsolete radicale-config-storage-hooks-SELinux-note.patch by inject inside spec file
- Obsolete radicale-httpd by contrib config from upstream

* Tue Jun 11 2024 Peter Bieringer <pb@bieringer.de> - 3.2.1-4
- Fix an unexpected unicode char in /etc/radicale/config (git#ce321344)

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 3.2.1-3.1
- Rebuilt for Python 3.13

* Sat Jun 08 2024 Peter Bieringer <pb@bieringer.de> - 3.2.1-3
- Additional review+extension of bundled Apache configuration example
- Fix group+permissions of /etc/radicale/rights
- Create an empty file /etc/radicale/users with proper permissions

* Sat Jun 08 2024 Peter Bieringer <pb@bieringer.de> - 3.2.1-2
- Major review of bundled Apache configuration example

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.2.1-1.1
- Rebuilt for Python 3.13

* Sun Jun 02 2024 Peter Bieringer <pb@bieringer.de> - 3.2.1-1
- Update to 3.2.1

* Fri May 03 2024 Peter Bieringer <pb@bieringer.de> - 3.2.0-1
- Update to 3.2.0
- SELinux/radicale.te: new boolean and policy for radicale_use_fusefs

* Mon Mar 18 2024 Peter Bieringer <pb@bieringer.de> - 3.1.9-1
- Update to 3.1.9
- Remove obsolete patches
- Add support for intermediate build using gitcommit

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-54.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-54.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 08 2023 Peter Bieringer <pb@bieringer.de> - 3.1.8-54
- Readjust setup.py after applying patch to proper version (#2229519)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-52.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 3.1.8-52.1
- Rebuilt for Python 3.12

* Wed Jun 21 2023 Peter Bieringer <pb@bieringer.de> - 3.1.8-53
- Update patch release/upstream to d7ce2f0b (2023-04-22)
- Add radicale-3.1.8-fix-main-component-PR-1252.patch
- Remove cases for radicale major version 1 and 2
- Partially align spec file with EPEL variant
- Move binaries to libexec and create a wrapper script
- Align systemd unit file and SELinux definition with EPEL variant

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.1.8-39
- Rebuilt for Python 3.12

* Tue Mar 21 2023 Peter Bieringer <pb@bieringer.de> - 3.1.8-38
- Add patch against upstream 6ae831a3
- Extend SELinux policy to allow native journald logging
- Update to 3.1.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Peter Bieringer <pb@bieringer.de> - 3.1.7-37
- Add radicale-disable-timestamp-if-started-by-systemd-PR-1276.patch
- Fix still unsolved SELinux issues (#2156633)
- Add radicale-fix-move-behind-proxy-PR-1271.patch

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.1.7-31
- Rebuilt for Python 3.11

* Wed Apr 20 2022 Peter Bieringer <pb@bieringer.de> - 3.1.7-30
- Update to 3.1.7 (#2077126)

* Tue Apr 19 2022 Peter Bieringer <pb@bieringer.de> - 3.1.6-29
- Update to 3.1.6 (#2076547)

* Tue Feb 08 2022 Peter Bieringer <pb@bieringer.de> - 3.1.5-29
- Update to 3.1.5 (#2052179)

* Thu Feb 03 2022 Peter Bieringer <pb@bieringer.de> - 3.1.4-28
- Update to 3.1.4 (#2049932)

* Fri Jan 28 2022 Peter Bieringer <pb@bieringer.de> - 3.1.3-27
- Update to 3.1.3 (#2047522)

* Sun Jan 23 2022 Peter Bieringer <pb@bieringer.de> - 3.1.2-26
- Update to 3.1.2 (#2043986)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Peter Bieringer <pb@bieringer.de> - 3.1.1-24
- Version 3.1.1
- Fix URLs to major version upgrade notes
- Replace NEWS.md by CHANGELOG.md

* Mon Dec 27 2021 Peter Bieringer <pb@bieringer.de> - 3.1.0-23
- SELinux policy: add notes in subpackage description and default config file that storage hooks are not supported so far (RHBZ#1928899)
- add required init_nnp_daemon_domain to radicale.te (1.0.9): (RHBZ#2020942)

* Mon Dec 27 2021 Peter Bieringer <pb@bieringer.de> - 3.1.0-22
- Version 3.1.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.6-18
- Rebuilt for Python 3.10

* Fri Mar 05 2021 Peter Bieringer <pb@bieringer.de> - 3.0.6-17
- Move SELinux into dedicated subpackage and add as suggestion to main package (RHBZ#1934895)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.6-15
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-13
- Only SELinux relabel log directory if existing
- Remove no longer required/supported log directory from SELinux file context

* Tue Sep 22 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-10
- Disable -D in systemd unit file for major version 3
- Toggle loglevel to info by default
- No longer package /var/log/radicale and the logrotate config for major version 3 (logs only to stdout/stderr now)
- Replace /var/run with _rundir (additional leftovers found)

* Tue Sep 22 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-9
- Add additional test with an example collection

* Tue Sep 22 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-8
- Cosmetic cleanup

* Mon Sep 21 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-7
- Do not use fixfiles in subpackages which have nothing related defined so far
- Enable -D in systemd unit file for major version 3
- Add 'check' section and related build requirements

* Mon Sep 21 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-6
- Remove additional failsafe checks to prevent manual upgrade from major version 2 (no longer needed)
- Revert use of radicale_package name (no no longer needed)
- Fix hidden SELinux post-install/post-uninstall issues
- Fix attributes for wsgi/fcgi
- Fix not working pre/post with new major version in package

* Sun Sep 20 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-5
- Include major version in package name
- Adjust systemd unit file for major version 3

* Sun Sep 20 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-4
- Version 3.0.6 (obsoletes fcgi and logging config file)
- Add additional failsafe checks to prevent manual upgrade from major version 2
- Replace /var/run with _rundir

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.12-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.12-1
- Version 2.1.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.11-2
- Fix hardlink path on epel

* Sun Jan 05 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.11-1
- Version 2.1.11

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.10-6
- Use autogenerated python dependencies

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.10-3
- hardlink moved to /usr/bin

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.10-1
- Version 2.1.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.9-4
- Rebuilt for Python 3.7

* Thu May 31 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-3
- Add versioned dependencies

* Wed May 23 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-2
- Recommends: python3-bcrypt, python3-passlib

* Wed May 16 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-1
- Version 2.1.9

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-3
- SELinux rule to allow connection to POP port

* Sun Oct 08 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-2
- Run in daemon mode so it creates the PID file

* Mon Sep 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-1
- Version 2.1.8

* Wed Sep 20 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.7-1
- Version 2.1.7

* Tue Sep 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.6-2
- Upload 2.1.6 sources

* Tue Sep 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.6-1
- Version 2.1.6

* Sun Aug 27 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.5-1
- Version 2.1.5

* Mon Aug 07 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-1
- Version 2.1.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.2-1
- Version 2.1.2

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.1-1
- Version 2.1.1

* Fri Jun 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-3
- Update SELinux policy

* Fri Jun 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-2
- Remove PrivateDevices=true (RHBZ#1452328)

* Sun Jun 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-1
- Version 2.1.0

* Sun May 28 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0-1
- Version 2.0.0

* Wed May 03 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0rc2-2
- Run in foreground

* Wed May 03 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0rc2-1
- Version 2.0.0rc2
- Drop python2 support

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-10
- Rebuild for Python 3.6

* Fri Dec 09 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-9
- Allow radicale_t to execute bin_t in SELinux policy RHBZ#1393569

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 01 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-7
- Additional systemd hardening

* Fri Jun 24 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-6
- Correctly label the files

* Wed Jun 22 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-5
- Add /var/run/radicale directory

* Tue Jun 21 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-4
- Update dependencies

* Tue Jun 21 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-3
- Create python2 subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (#1296746)

* Fri Jan 01 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1-1
- Version 1.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-3
- Fix radicale-httpd for python3

* Thu Sep 24 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-2
- Unify spec for Fedora and epel7

* Tue Sep 22 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-1
- Version 1.0.1

* Tue Sep 15 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0-1
- Version 1.0
- Merge SELinux subpackage into the main package

* Mon Sep 07 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-7
- Drop old _selinux_policy_version hack
- Require radicale-selinux

* Fri Jul 24 2015 Tomas Radej <tradej@redhat.com> - 0.10-6
- Updated dep on policycoreutils-python-utils

* Wed Jun 17 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-5
- Switch to python3

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-4
- Use license macro

* Mon Apr 06 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-3
- Add patch1 to fix rhbz#1206813

* Tue Feb 24 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-2
- Add radicale_var_run_t to SELinux policy 1.0.3

* Tue Jan 13 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-1
- Version 0.10

* Mon Aug 18 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9-2
- Hide error when re-adding SELinux port label.

* Thu Aug 14 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9-1
- Version 0.9
- Automatically restart service if it dies.
- Update systemwide patch

* Mon Aug 04 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-11
- Handle PID file.

* Thu Jul 17 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-10
- Add network-online.target dependency. Bug #1119818

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-8
- Add PrivateDevices to unit file

* Wed Dec 25 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-7
- SELinux policy 1.0.2

* Fri Nov 29 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-6
- SELinux policy 1.0.1 fix bug #1035925

* Fri Nov 08 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-5
- Hardcode _selinux_policy_version in F20 because of #999584

* Thu Oct 03 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-4
- Update httpd config file and add SELinux policy. Bug #1014408

* Tue Aug 27 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-3
- Move .wsgi and .fcgi to main package

* Sun Jul 21 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-2
- BuildRequire python2-devel

* Thu Jul 18 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-1
- Update to version 0.8
- Merge Till Maas's spec file. Bug #922276

* Mon Jul 08 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.7.1-1
- Initial packaging
