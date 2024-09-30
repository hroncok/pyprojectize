# python bluechi module is enabled by default, it can be disabled passing `--define "with_python 0"` option to rpmbuild
%if 0%{!?with_python:1}
%global with_python 1
%endif

Name:		bluechi
Version:	0.8.0
Release:	4%{?dist}
Summary:	A systemd service controller for multi-nodes environments
License:	LGPL-2.1-or-later AND CC0-1.0
URL:		https://github.com/eclipse-bluechi/bluechi
Vendor:		Fedora Project
Packager:	Red Hat
# When downloading from github - no longer works due to a git submodule
#Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# To download the manually uploaded tarball
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# Required to apply the patch
BuildRequires:	git-core
BuildRequires:	gcc
# Meson needs to detect C++, because part of inih library (which we don't use)
# provides C++ functionality
BuildRequires:	gcc-c++
BuildRequires:	meson
BuildRequires:	systemd-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:	golang-github-cpuguy83-md2man

%description
BlueChi is a systemd service controller for multi-node environments with a
predefined number of nodes and with a focus on highly regulated environments
such as those requiring functional safety (for example in cars).

%package	controller
Summary:	BlueChi service controller
Requires:	systemd
Recommends:	bluechi-selinux
Obsoletes:	hirte < 0.4.0
Provides:	hirte = %{version}-%{release}
Obsoletes:	bluechi < 0.7.0
Provides:	bluechi = %{version}-%{release}

%description controller
BlueChi is a systemd service controller for multi-node environments with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).

This package contains the controller service.

%post controller
%systemd_post bluechi-controller.service

%preun controller
%systemd_preun bluechi-controller.service

%postun controller
%systemd_postun_with_restart bluechi-controller.service

%files controller
%ghost %{_sysconfdir}/bluechi/controller.conf
%dir %{_sysconfdir}/bluechi
%dir %{_sysconfdir}/bluechi/controller.conf.d
%doc README.md
%doc README.developer.md
%license LICENSE
%{_libexecdir}/bluechi-controller
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Job.xml
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Controller.xml
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Monitor.xml
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Node.xml
%{_datadir}/dbus-1/system.d/org.eclipse.bluechi.conf
%{_datadir}/bluechi/config/controller.conf
%{_mandir}/man1/bluechi-controller.*
%{_mandir}/man5/bluechi-controller.conf.*
%{_sysconfdir}/bluechi/controller.conf.d/README.md
%{_unitdir}/bluechi-controller.service
%{_unitdir}/bluechi-controller.socket

#--------------------------------------------------

%package agent
Summary:	BlueChi service controller agent
Requires:	systemd
Recommends:	bluechi-selinux
Obsoletes:	hirte-agent < 0.4.0
Provides:	hirte-agent = %{version}-%{release}

%description agent
BlueChi is a systemd service controller for multi-node environments with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).

This package contains the node agent.

%post agent
%systemd_post bluechi-agent.service

%preun agent
%systemd_preun bluechi-agent.service

%postun agent
%systemd_postun_with_restart bluechi-agent.service

%files agent
%ghost %{_sysconfdir}/bluechi/agent.conf
%dir %{_sysconfdir}/bluechi
%dir %{_sysconfdir}/bluechi/agent.conf.d
%doc README.md
%license LICENSE
%{_libexecdir}/bluechi-agent
%{_libexecdir}/bluechi-proxy
%{_datadir}/dbus-1/system.d/org.eclipse.bluechi.Agent.conf
%{_datadir}/bluechi-agent/config/agent.conf
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Agent.xml
%{_mandir}/man1/bluechi-agent.*
%{_mandir}/man1/bluechi-proxy.*
%{_mandir}/man5/bluechi-agent.conf.*
%{_sysconfdir}/bluechi/agent.conf.d/README.md
%{_unitdir}/bluechi-agent.service
%{_userunitdir}/bluechi-agent.service
%{_unitdir}/bluechi-proxy@.service
%{_userunitdir}/bluechi-proxy@.service
%{_unitdir}/bluechi-dep@.service
%{_userunitdir}/bluechi-dep@.service

#--------------------------------------------------

%package selinux
Summary:	BlueChi SELinux policy
BuildArch:	noarch
BuildRequires:	checkpolicy
BuildRequires:	selinux-policy-devel

%if "%{_selinux_policy_version}" != ""
Requires:	selinux-policy >= %{_selinux_policy_version}
%endif

Requires(post):	policycoreutils

Obsoletes:	hirte-selinux < 0.4.0
Provides:	hirte-selinux = %{version}-%{release}

%global selinuxtype targeted

%description selinux
SELinux policy associated with the bluechi and bluechi-agent daemons

%files selinux
%{_datadir}/selinux/devel/include/services/bluechi.if
%{_datadir}/selinux/packages/bluechi.pp.bz2
%{_mandir}/man8/bluechi*selinux.*

%post selinux
# Remove hirte policy
if [ $1 -eq 1 ]; then
   semodule -N -X 200 -r hirte 2>/dev/null || true
fi
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/bluechi.pp.bz2
restorecon -R %{_bindir}/bluechi* &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ]; then
   %selinux_modules_uninstall -s %{selinuxtype} bluechi
   restorecon -R %{_bindir}/bluechi* &> /dev/null || :
fi


#--------------------------------------------------

%package ctl
Summary:	BlueChi service controller command line tool
Requires:	%{name} = %{version}-%{release}
Provides:	bluechictl = %{version}
Obsoletes:	hirte-ctl < 0.4.0
Provides:	hirte-ctl = %{version}-%{release}

%description ctl
BlueChi is a systemd service controller for multi-nodes environements with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).
This package contains the service controller command line tool.

%files ctl
%doc README.md
%license LICENSE
%{_bindir}/bluechictl
%{_mandir}/man1/bluechictl.*

#--------------------------------------------------

%if %{with_python}
%package -n python3-bluechi
Summary:	Python bindings for BlueChi
BuildArch:	noarch
BuildRequires:	python3-devel
Requires:	python3-dasbus

Obsoletes:	python3-pyhirte < 0.4.0
Provides:	python3-pyhirte = %{version}-%{release}

%description -n python3-bluechi
bluechi is a python module to access the public D-Bus API of BlueChi project.
It contains typed python code that is auto-generated from BlueChi's
API description and manually written code to simplify recurring tasks.

%files -n python3-bluechi -f %{pyproject_files}
%doc README.md

%endif

#--------------------------------------------------

%prep
%autosetup -S git_am

%generate_buildrequires
%pyproject_buildrequires

%build
%meson -Dapi_bus=system
%meson_build

%if %{with_python}
pushd src/bindings/python
%pyproject_wheel
popd
%endif


%install
%meson_install

%if %{with_python}
pushd src/bindings/python
%pyproject_install
%pyproject_save_files -l bluechi
popd
%endif


%check
%meson_test


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.13

* Tue Apr 30 2024 Michael Engel <mengel@redhat.com> - 0.8.0-2
- Resolved asterisk for dbus interface xml files by explicitly listing files
- Aligned formatting with GitHub repo from upstream

* Tue Apr 30 2024 Michael Engel <mengel@redhat.com> - 0.8.0-1
- Update to 0.8.0
- Added Vendor and Packager
- Updated selinux policy according to upstream

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Michael Engel <mengel@redhat.com> - 0.7.0-1
- Update to 0.7.0
- Updated URL to new eclipse-bluechi GitHub organization
- Fixed typos in description
- Aligned selinux policy according to GitHub repo

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Michael Engel <mengel@redhat.com> - 0.6.0-1
- Update to 0.6.0
- Rename bluechi package to controller

* Tue Sep 05 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.5.0-1
- Update to 0.5.0
- Rename package to BlueChi
- Update license to LGPL-2.1-or-later

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.0-2
- Fix the conditional used to enable/disable the python3-pyhirte subpackage

* Mon Jul 17 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.0-1
- Update to 0.4.0
- Introduce the python3-pyhirte subpackage

* Fri Jun 09 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.3.0-1
- Update to 0.3.0
- Backport patch from PR #355 which fixes building on i686

* Tue May 02 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.0-1
- Update to 0.2.0
- Introduce the hirte-selinux sub-package

* Tue Mar 28 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-3
- Drop the man page for hirtectl from the main hirte package

* Mon Mar 27 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-2
- Remove hirtectl from the hirte package since it is now in its own subpackage

* Mon Mar 27 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-1
- Update to 0.1.1
- Adjust Source0 to point to /archive/v<version>/hirte-<version>.tar.gz
- Adjust the location of dbus-1/system.d/org.containers.hirte.conf and
  bus-1/system.d/org.containers.hirte.Agent.conf so they are in _datadir
- Add the hirte-ctl subpackage (which provides hirtectl for convenience)

* Wed Mar 22 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.0-5
- Adjust summary and description according to the changes made upstream

* Wed Mar 22 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.0-4
- Fix the Source0 to point to a resolvable url
- Replace tabs with spaces

* Tue Mar 21 2023 Martin Perina <mperina@redhat.com> - 0.1.0-3
- Move the different files section near the different package definition

* Tue Mar 21 2023 Martin Perina <mperina@redhat.com> - 0.1.0-2
- Make rpmlint happier

* Tue Mar 21 2023 Martin Perina <mperina@redhat.com> - 0.1.0-1
- Initial release

