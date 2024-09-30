%global summary A set of libraries and tools for managing boot loader entries
%global sphinx_docs 1

Name:		boom-boot
Version:	1.6.5
Release:	1%{?dist}
Summary:	%{summary}

License:	GPL-2.0-only
URL:		https://github.com/snapshotmanager/boom
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	make
BuildRequires:	python3-devel
%if 0%{?sphinx_docs}
BuildRequires:	python3-dbus
BuildRequires:	python3-sphinx
%endif
BuildRequires: make

Requires: python3-boom = %{version}-%{release}
Requires: %{name}-conf = %{version}-%{release}
Requires: python3-dbus
Requires: systemd >= 254

Obsoletes: boom-boot-grub2 <= 1.3
# boom-grub2 was not an official name of subpackage in fedora, but was used upstream:
Obsoletes: boom-grub2 <= 1.3

%package -n python3-boom
Summary: %{summary}
Requires: %{__python3}
Recommends: (lvm2 or brtfs-progs)
Recommends: %{name}-conf = %{version}-%{release}

# There used to be a boom package in fedora, and there is boom packaged in
# copr. How to tell which one is installed? We need python3-boom and no boom
# only.
Conflicts: boom

%package conf
Summary: %{summary}

%description
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function: either the
systemd-boot project, or Grub2 with the BLS patch (Red Hat Grub2 builds
include this support in both Red Hat Enterprise Linux 7 and Fedora).

%description -n python3-boom
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function: either the
systemd-boot project, or Grub2 with the BLS patch (Red Hat Grub2 builds
include this support in both Red Hat Enterprise Linux 7 and Fedora).

This package provides python3 boom module.

%description conf
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function: either the
systemd-boot project, or Grub2 with the BLS patch (Red Hat Grub2 builds
include this support in both Red Hat Enterprise Linux 7 and Fedora).

This package provides configuration files for boom.

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?sphinx_docs}
make %{?_smp_mflags} -C doc html
rm doc/_build/html/.buildinfo
mv doc/_build/html doc/html
rm -r doc/_build
%endif

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files boom

# Make configuration directories
# mode 0700 - in line with /boot/grub2 directory:
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/profiles
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/hosts
install -d -m 700 ${RPM_BUILD_ROOT}/boot/loader/entries
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/cache
install -m 644 examples/boom.conf ${RPM_BUILD_ROOT}/boot/boom

mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man5
install -m 644 man/man8/boom.8 ${RPM_BUILD_ROOT}/%{_mandir}/man8
install -m 644 man/man5/boom.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5

rm doc/Makefile
rm doc/conf.py

# Test suite currently does not operate in rpmbuild environment
#%%check
#%%{__python3} setup.py test

%files
%license COPYING
%doc README.md
%{_bindir}/boom
%doc %{_mandir}/man*/boom.*

%files -n python3-boom -f %{pyproject_files}
%license COPYING
%doc README.md
%doc doc
%doc examples
%doc tests

%files conf
%license COPYING
%doc README.md
%dir /boot/boom
%config(noreplace) /boot/boom/boom.conf
%dir /boot/boom/profiles
%dir /boot/boom/hosts
%dir /boot/boom/cache
%dir /boot/loader/entries


%changelog
* Wed Sep 18 2024 Bryan Gurney <bgurney@redhat.com> - 1.6.5-1
- Update to release 1.6.5.

* Fri Jul 26 2024 Bryn M. Reeves <bmr@redhat.com> - 1.6.4-1
* Update to release 1.6.4.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Bryan Gurney <bgurney@redhat.com> - 1.6.3-1
- Update to release 1.6.3.

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.2-2
- Rebuilt for Python 3.13

* Thu May 30 2024 Bryan Gurney <bgurney@redhat.com> - 1.6.2-1
- Update to release 1.6.2.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Marian Csontos <mcsontos@redhat.com> - 1.6.0-1
- Update to release 1.6.0.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.12

* Tue May 16 2023 Marian Csontos <mcsontos@redhat.com> - 1.5.1-1
- Update to release 1.5.1.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Marian Csontos <mcsontos@redhat.com> 1.4-1
- Update to release 1.4.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3-5
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3-2
- Rebuilt for Python 3.10

* Fri Jan 29 2021 Marian Csontos <mcsontos@redhat.com> 1.3-1
- Update to release 1.3.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Marian Csontos <mcsontos@redhat.com> 1.2-1
- Update to bug fix release 1.2.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuilt for Python 3.9

* Tue May 26 2020 Marian Csontos <mcsontos@redhat.com> 1.1-3
- Fix unicode entries handling.
- Add tracebacks when --debug is used.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Marian Csontos <mcsontos@redhat.com> 1.1-1
- Update to new upstream release 1.1.
- Add caching of kernel and init ramdisk images.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Marian Csontos <mcsontos@redhat.com> 1.0-1
- Update to new upstream release 1.0.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.5.20190329git6ff3e08
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.4.20190329git6ff3e08
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.3.20190329git6ff3e08
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Marian Csontos <mcsontos@redhat.com> 1.0-0.2.20190329git6ff3e08
- Fix packaging issues.

* Thu May 09 2019 Marian Csontos <mcsontos@redhat.com> 1.0-0.1.20190329git6ff3e08
- Pre-release of new version.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Marian Csontos <mcsontos@redhat.com> 0.9-4
- Change dependencies.

* Mon Jul 16 2018 Marian Csontos <mcsontos@redhat.com> 0.9-3
- Split executable, python module and configuration.

* Wed Jun 27 2018 Marian Csontos <mcsontos@redhat.com> 0.9-2
- Spin off grub2 into subpackage

* Wed Jun 27 2018 Marian Csontos <mcsontos@redhat.com> 0.9-1
- Update to new upstream 0.9.
- Fix boot_id caching.

* Fri Jun 08 2018 Marian Csontos <mcsontos@redhat.com> 0.8.5-6.2
- Remove example files from /boot/boom/profiles.

* Fri May 11 2018 Marian Csontos <mcsontos@redhat.com> 0.8.5-6.1
- Files in /boot are treated as configuration files.

* Thu Apr 26 2018 Marian Csontos <mcsontos@redhat.com> 0.8.5-6
- Package upstream version 0.8-5.6

