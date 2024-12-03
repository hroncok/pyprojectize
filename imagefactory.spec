Name: imagefactory
Version: 1.1.16
Release: 15%{?dist}
Summary: System image generation tool
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/redhat-imaging/imagefactory

Source0: https://github.com/redhat-imaging/imagefactory/archive/imagefactory-%{version}-1.tar.gz
Patch0: imagefactory-1.1.14-utf8-config-id.patch
# https://github.com/redhat-imaging/imagefactory/pull/434
Patch1: container-github-pr434.patch
# https://github.com/redhat-imaging/imagefactory/pull/438
Patch2: 0001-ApplicationConfiguration.py-drop-encoding-from-json..patch
# https://github.com/redhat-imaging/imagefactory/issues/412
# https://bugzilla.redhat.com/show_bug.cgi?id=2245066
# https://github.com/redhat-imaging/imagefactory/pull/455
Patch3: imagefactory-Docker.py-Pass-the-use_ino-option-to-fix-hardlnks.patch
# https://github.com/redhat-imaging/imagefactory/pull/458
# this goes along with https://github.com/clalancette/oz/pull/310
# which was backported to oz in
# https://src.fedoraproject.org/rpms/oz/c/4e5dbe2
# Might only be needed in imagefactory-plugins, but let's have it
# here just to be safe
Patch4: 0001-TinMan.py-adjust-to-oz-generate_diskimage-size-unit-.patch
# https://github.com/redhat-imaging/imagefactory/pull/459
# Python 3.12 support and CVE-2022-31799 fix for bundled bottle
Patch5: 0001-bottle-fix-for-Python-3.12-backport-CVE-2022-31799-f.patch
Patch6: 0002-Python-3.12-adjust-for-removal-of-SafeConfigParser.patch

BuildArch: noarch

BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: systemd-units

Requires: python3-pycurl
Requires: python3-libguestfs
Requires: python3-zope-interface
Requires: python3-libxml2
Requires: python3-httplib2
Requires: python3-cherrypy
Requires: python3-oauth2
Requires: python3-libs
# uses distutils at runtime, was removed from core Python in 3.12
Requires: python3-setuptools
Requires: oz

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# Has a vendored copy of bottle.py as imgfac/rest/bottle.py
Provides: bundled(python-bottle)

# TODO: Any changes to the _internal_ API must increment this version or, in
#       the case of backwards compatible changes, add a new version (RPM
#       allows multiple version "=" lines for the same package or
#       pseudo-package name)
Provides: imagefactory-plugin-api = 1.0

%description
imagefactory allows the creation of system images for multiple virtualization
and cloud providers from a single template definition. See
https://github.com/redhat-imaging/imagefactory for more information.

%prep
%autosetup -p1 -n imagefactory-imagefactory-%{version}-1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l imgfac


install -d %{buildroot}/%{_sysconfdir}/imagefactory/jeos_images
install -d %{buildroot}/%{_localstatedir}/lib/imagefactory/images
install -d %{buildroot}/%{_sysconfdir}/imagefactory/plugins.d
install -d %{buildroot}/%{_sysconfdir}/logrotate.d

install -m0600 conf/sysconfig/imagefactoryd %{buildroot}/%{_sysconfdir}/sysconfig/imagefactoryd
install -m0600 conf/logrotate.d/imagefactoryd %{buildroot}/%{_sysconfdir}/logrotate.d/imagefactoryd

rm -f %{buildroot}/%{_initddir}/imagefactoryd

%check
%pyproject_check_import

%post
%systemd_post imagefactoryd.service

%preun
%systemd_preun imagefactoryd.service

%postun
%systemd_postun imagefactoryd.service


%files -f %{pyproject_files}
%{_unitdir}/imagefactoryd.service
%config(noreplace) %{_sysconfdir}/imagefactory/imagefactory.conf
%config(noreplace) %{_sysconfdir}/sysconfig/imagefactoryd
%config(noreplace) %{_sysconfdir}/logrotate.d/imagefactoryd
%dir %attr(0755, root, root) %{_sysconfdir}/pki/imagefactory/
%dir %attr(0755, root, root) %{_sysconfdir}/imagefactory/jeos_images/
%dir %attr(0755, root, root) %{_sysconfdir}/imagefactory/plugins.d/
%dir %attr(0755, root, root) %{_localstatedir}/lib/imagefactory/images
%config %{_sysconfdir}/pki/imagefactory/cert-ec2.pem
%{_bindir}/imagefactory
%{_bindir}/imagefactoryd

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.16-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.16-13
- Rebuilt for Python 3.13

* Sat Feb 10 2024 Adam Williamson <awilliam@redhat.com> - 1.1.16-12
- Requires python3-setuptools (for distutils stuff removed in Python 3.12)

* Sat Feb 10 2024 Adam Williamson <awilliam@redhat.com> - 1.1.16-11
- Backport PR #459 to hopefully fix Python 3.12 compatibility

* Sat Feb 10 2024 Adam Williamson <awilliam@redhat.com> - 1.1.16-10
- Backport PR #458 to go with backport of oz PR #310 (image size units)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Debarshi Ray <rishi@fedoraproject.org> - 1.1.16-7
- Preserve hard links when building Docker images

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.16-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.16-2
- Rebuilt for Python 3.11

* Wed Feb 16 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 1.1.16-1
- Rebased on 1.1.16

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.15-8
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Kevin Fenzi <kevin@scrye.com> - 1.1.15-6.1
- Add patch for isAlive issue

* Sat Oct 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-6
- Fix for deprecated change dropped in py3.9

* Sat Oct 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-5
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-2
- Update container patch to latest rev

* Wed Mar 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-1
- Update to 1.1.15.

* Wed Mar 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.14-3
- Upstream patch for container fixes
- Drop non systemd support as it requires python3 of which older distros won't have
- Spec cleanup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 02 2019 Kevin Fenzi <kevin@scrye.com> - 1.1.14-1
- Update to 1.1.14.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-0.20190527193659gita117084
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 26 2018 Brendan Reilly <breilly@redhat.com> - 1.1.11-1
- Upstream release 1.1.11
  - ovfcommon: supporting OVAs with subdirectories

* Tue May 31 2016 Ian McLeod <imcleod@redhat.com> - 1.1.9-1
- Upstream release 1.1.9
  - Add HyperV Vagrant support
  - enhance vSphere and VMWare Fusion support

* Thu Mar 17 2016 Ian McLeod <imcleod@redhat.com> - 1.1.8-2
- fix RHEL7 conditional for systemd unit file content

* Wed Mar 16 2016 Ian McLeod <imcleod@redhat.com> - 1.1.8-1
- Upstream release 1.1.8
- systemd support
- docker base image updates
- significant EC2 updates for regions and instance types
- VMWare fusion vagrant box support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 7 2015 Ian McLeod <imcleod@redhat.com> - 1.1.7-1
- Upstream release 1.1.7
- Vagrant box support added to OVA plugin

* Mon Nov 24 2014 Ian McLeod <imcleod@redhat.com> - 1.1.6-2
- Assorted fixes and features to enable rpm-ostree-toolbox integration

* Tue Oct 21 2014 Ian McLeod <imcleod@redhat.com> -1.1.6-1
- Upstream 1.1.6 release

* Tue May 6 2014 Ian McLeod <imcleod@redhat.com> - 1.1.5-1
- Rebase with upstream
- Improved CLI parameter passing support

* Thu Jan 30 2014 Steve Loranz <sloranz@redhat.com> - 1.1.3-1
- Remove references to man directories. Documentation will be hosted @ imgfac.org.

* Thu Aug 15 2013 Ian McLeod <imcleod@redhat.com> - 1.1.3
- Rebase with upstream

* Thu Sep 15 2011 Ian McLeod <imcleod@redhat.com> - 0.6.1
- Update Oz requirement to 0.7.0 or later for new target-specific package config
- Update SPEC file to restart service after an install

* Mon Apr 04 2011 Chris Lalancette <clalance@redhat.com> - 0.1.6-1
- Initial spec file.
