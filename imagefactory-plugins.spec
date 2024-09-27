# Some Openstack supporting packages from EPEL have been removed due to updated
# deps that override RHEL and, thus, violate EPEL rules.  We would like to 
# eventually support these features as part of an EL6 and EL7 set of factory
# plugin packages in RDO.  Until this is sorted out we must disable things when
# building on RHEL.
# TODO: If we end up building as part of RDO either remove this for RDO
# SPEC builds or find a way to detect an RDO build and automagically negate this
# UPDATE: F24 dropped the supporting modules we currently use
# TODO: Refresh/refactor OpenStack support to use newer module and then update below
%if 0%{?fedora} >= 24 || 0%{?rhel} >= 3
%define include_openstack 0
%else
%define include_openstack 1
%endif

# For now, do not build this sub RPM - It has bitrotted and needs to be revisited
%define include_nova_image_builder 0



%global auto_register_macro_post() # create it if it doesn't already exist as a link \
# If it is an existing file other than a link, do nothing \
[ -L %{_sysconfdir}/imagefactory/plugins.d/%1.info ] || \
[ -e %{_sysconfdir}/imagefactory/plugins.d/%1.info ] || \
ln -s %{python3_sitelib}/imagefactory_plugins/%1/%1.info %{_sysconfdir}/imagefactory/plugins.d/%1.info \
exit 0 

%global auto_register_macro_postun() if [ "\$1" = "0" ]; then \
  # clean up the link if it exists - if it doesn't or if this is a regular file, do nothing \
  [ -L %{_sysconfdir}/imagefactory/plugins.d/%1.info ] && rm -f  %{_sysconfdir}/imagefactory/plugins.d/%1.info \
fi \
exit 0


Name: imagefactory-plugins
Version: 1.1.16
Release: 14%{?dist}
Summary: Default plugins for the Image Factory system image generation tool
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/redhat-imaging/imagefactory

Source0: https://github.com/redhat-imaging/imagefactory/archive/imagefactory-%{version}-1.tar.gz
Patch0: imagefactory-1.1.14-utf8-config-id.patch
Patch1: container-github-pr434.patch
Patch2: fix-armv7l.patch
# https://github.com/redhat-imaging/imagefactory/pull/455
Patch3: imagefactory-Docker.py-Pass-the-use_ino-option-to-fix-hardlnks.patch
# https://github.com/redhat-imaging/imagefactory/pull/458
# this goes along with https://github.com/clalancette/oz/pull/310
# which was backported to oz in
# https://src.fedoraproject.org/rpms/oz/c/4e5dbe2
Patch4: 0001-TinMan.py-adjust-to-oz-generate_diskimage-size-unit-.patch
# https://github.com/redhat-imaging/imagefactory/pull/459
# Python 3.12 support
Patch5: 0002-Python-3.12-adjust-for-removal-of-SafeConfigParser.patch

BuildArch: noarch
BuildRequires: python3
BuildRequires: python3-devel
Requires: imagefactory

# Obsolete the old EC2 plugins as they need python2 based euca2ools thats not in Fedora anymore.
Obsoletes: imagefactory-plugins-EC2 < 1.1.15-3
Obsoletes: imagefactory-plugins-EC2-jeos-images < 1.1.15-3

%description
This is a placeholder top level package for a collection of plugins for the
Image Factory cloud system image generation tool.

imagefactory allows the creation of system images for multiple virtualization
and cloud providers from a single template definition. See
https://github.com/redhat-imaging/imagefactory for more information.

%package ovfcommon
Summary: common utilities to manipulate ovf-related objects
Requires: oz >= 0.7.0
Requires: imagefactory-plugins

%description ovfcommon
This pseudo-plugin is used to provide common OVF functionality to other
plugins.

%package OVA
Summary: Cloud plugin for generating OVA archives
Requires: oz >= 0.7.0
Requires: imagefactory-plugins
Requires: imagefactory-plugins-ovfcommon
Requires: imagefactory-plugin-api = 1.0

%description OVA
This Cloud plugin allows users to specify a Base Image to generate an OVA
archive from.

%package IndirectionCloud
Summary: Cloud plugin for allowing images to modify other images
Requires: oz >= 0.12.0
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description IndirectionCloud
This Cloud plugin allows users to specify a Base Image to use to manipulate
another Base Image to generate a Target Image.

It was originally created to produce Live CDs and other live media using an
arbitrary  host OS and package selection for the actual media creation tools.

%package TinMan
Summary: OS plugin for Fedora
Requires: oz >= 0.12.0
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description TinMan
An OS plugin to support Fedora OSes

%if 0%{include_openstack}
%package OpenStack
Summary: Cloud plugin for OpenStack running on KVM
Requires: python3-glanceclient
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description OpenStack
A Cloud plugin to support OpenStack running on top of KVM.

%package Rackspace
Summary: Cloud plugin for Rackspace
Requires: python-novaclient
Requires: python-pyrax
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description Rackspace
A Cloud plugin to support Rackspace

%package Rackspace-JEOS-images
Summary: JEOS images for various OSes to support Rackspace snapshot builds
Requires: imagefactory-plugins-Rackspace

%description Rackspace-JEOS-images
These configuration files point to existing JEOS Image ID's on Rackspace that
can be used to do "snapshot" style builds.
%endif

%if 0%{include_nova_image_builder}
%package Nova
Summary: OS plugin that allows imagefactory to use Nova instances to build base images.
Requires: python3-novaclient
Requires: oz >= 0.12.0
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description Nova
An alternative to the TinMan plugin for creating base images using an OpenStack cloud.
%endif

%if 0%{?build_mock}
%package MockOS
Summary: Mock OS plugin
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description MockOS
This plugin mimcs some of the behaviour of the RPM based OS plugins without
actually doing a build.

For testing use only.

%package MockCloud
Summary: Mock Cloud plugin
Requires: imagefactory-plugins
Requires: imagefactory-plugin-api = 1.0

%description MockCloud
This plugin mimcs some of the behaviour of a real cloud plugin without needing
any real external infra.

For testing use only.

%endif

%package RHEVM
Summary: RHEVM Cloud plugin
Requires: imagefactory-plugins
Requires: imagefactory-plugins-ovfcommon
#Make optional for now to allow core coversion features to work
#Requires: ovirt-engine-sdk >= 3.1.0
Requires: qemu-img
Requires: imagefactory-plugin-api = 1.0

%description RHEVM
A plugin for RHEVM "clouds"

%package vSphere
Summary: vSphere Cloud plugin
Requires: imagefactory-plugins
#This has been made conditional in the plugin - will need to be replaced
#Requires: python-psphere
Requires: imagefactory-plugin-api = 1.0
Requires: qemu-img
Requires: python3-pyyaml

%description vSphere
A plugin for vSphere "clouds"

%package Docker
Summary: Cloud plugin for Docker
Requires: tar

%description Docker
A Cloud plugin to support Docker

%package HyperV
Summary: Cloud plugin for HyperV
Requires: qemu-img

%description HyperV
A Cloud plugin to support HyperV

%package GCE
Summary: Cloud plugin for GCE
Requires: qemu-img
Requires: tar

%description GCE
A Cloud plugin to support the Google Compute Engine

%prep
%setup -q -n imagefactory-imagefactory-%{version}-1
mv imagefactory_plugins ../
rm -rf *
mv ../imagefactory_plugins/* .
rmdir ../imagefactory_plugins/
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p2
%patch -P4 -p2
%patch -P5 -p2

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# TODO: Cleaner negative conditional
%if 0%{?build_mock}
%else
rm -rf %{buildroot}%{python3_sitelib}/imagefactory_plugins/MockOS
rm -rf %{buildroot}%{python3_sitelib}/imagefactory_plugins/MockCloud
%endif

%if 0%{include_openstack}
%else
rm -rf  %{buildroot}%{python3_sitelib}/imagefactory_plugins/OpenStack
rm -rf  %{buildroot}%{python3_sitelib}/imagefactory_plugins/Rackspace
rm -f  %{buildroot}%{_sysconfdir}/imagefactory/jeos_images/rackspace_fedora_jeos.conf
rm -f  %{buildroot}%{_sysconfdir}/imagefactory/jeos_images/rackspace_rhel_jeos.conf
%endif

%if 0%{include_nova_image_builder}
%else
rm -rf  %{buildroot}%{python3_sitelib}/imagefactory_plugins/Nova
%endif

# delete old EC2 and EC2-json-images plugins
rm -rf %{buildroot}%{_sysconfdir}/imagefactory/jeos_images
rm -rf %{buildroot}%{_bindir}/create-ec2-factory-credentials
rm -rf %{buildroot}%{python3_sitelib}/imagefactory_plugins/EC2

%post OVA
%auto_register_macro_post OVA
%postun OVA
%auto_register_macro_postun OVA

%post IndirectionCloud
%auto_register_macro_post IndirectionCloud
%postun IndirectionCloud
%auto_register_macro_postun IndirectionCloud

%post TinMan
%auto_register_macro_post TinMan
%postun TinMan
%auto_register_macro_postun TinMan

%if 0%{include_openstack}
%post OpenStack
%auto_register_macro_post OpenStack
%postun OpenStack
%auto_register_macro_postun OpenStack

%post Rackspace
%auto_register_macro_post Rackspace
%postun Rackspace
%auto_register_macro_postun Rackspace
%endif

%if 0%{include_nova_image_builder}
%post Nova
%auto_register_macro_post Nova
%postun Nova
%auto_register_macro_postrun Nova
%endif

%post RHEVM
%auto_register_macro_post RHEVM
%postun RHEVM
%auto_register_macro_postun RHEVM

%if 0%{?build_mock}
%post MockOS
%auto_register_macro_post MockOS
%postun MockOS
%auto_register_macro_postun MockOS

%post MockCloud
%auto_register_macro_post MockCloud
%postun MockCloud
%auto_register_macro_postun MockCloud
%endif

%post vSphere
%auto_register_macro_post vSphere
%postun vSphere
%auto_register_macro_postun vSphere

%post Docker
%auto_register_macro_post Docker
%postun Docker
%auto_register_macro_postun Docker

%post HyperV
%auto_register_macro_post HyperV
%postun HyperV
%auto_register_macro_postun HyperV

%post GCE
%auto_register_macro_post GCE
%postun GCE
%auto_register_macro_postun GCE

%files
%license COPYING
%dir %{python3_sitelib}/imagefactory_plugins
%{python3_sitelib}/imagefactory_plugins/__init__.py*
%{python3_sitelib}/imagefactory_plugins/__pycache__/*.py*
%{python3_sitelib}/imagefactory_plugins*.dist-info

%files ovfcommon
%dir %{python3_sitelib}/imagefactory_plugins/ovfcommon
%{python3_sitelib}/imagefactory_plugins/ovfcommon/*

%files OVA
%dir %{python3_sitelib}/imagefactory_plugins/OVA
%{python3_sitelib}/imagefactory_plugins/OVA/*

%files IndirectionCloud
%dir %{python3_sitelib}/imagefactory_plugins/IndirectionCloud
%{python3_sitelib}/imagefactory_plugins/IndirectionCloud/*

%files TinMan
%dir %{python3_sitelib}/imagefactory_plugins/TinMan
%{python3_sitelib}/imagefactory_plugins/TinMan/*

%if 0%{include_openstack}
%files OpenStack
%dir %{python3_sitelib}/imagefactory_plugins/OpenStack
%{python3_sitelib}/imagefactory_plugins/OpenStack/*

%files Rackspace
%dir %{python3_sitelib}/imagefactory_plugins/Rackspace
%{python3_sitelib}/imagefactory_plugins/Rackspace/*

%files Rackspace-JEOS-images
%{_sysconfdir}/imagefactory/jeos_images/rackspace_fedora_jeos.conf
%{_sysconfdir}/imagefactory/jeos_images/rackspace_rhel_jeos.conf
%endif

%if 0%{include_nova_image_builder}
%files Nova
%dir %{python3_sitelib}/imagefactory_plugins/Nova
%{python3_sitelib}/imagefactory_plugins/Nova/*
%endif

%if 0%{?build_mock}
%files MockOS
%dir %{python3_sitelib}/imagefactory_plugins/MockOS
%{python3_sitelib}/imagefactory_plugins/MockOS/*

%files MockCloud
%dir %{python3_sitelib}/imagefactory_plugins/MockCloud
%{python3_sitelib}/imagefactory_plugins/MockCloud/*
%endif

%files RHEVM
%dir %{python3_sitelib}/imagefactory_plugins/RHEVM
%{python3_sitelib}/imagefactory_plugins/RHEVM/*

%files vSphere
%dir %{python3_sitelib}/imagefactory_plugins/vSphere
%{python3_sitelib}/imagefactory_plugins/vSphere/*

%files Docker
%dir %{python3_sitelib}/imagefactory_plugins/Docker
%{python3_sitelib}/imagefactory_plugins/Docker/*

%files HyperV
%dir %{python3_sitelib}/imagefactory_plugins/HyperV
%{python3_sitelib}/imagefactory_plugins/HyperV/*

%files GCE
%dir %{python3_sitelib}/imagefactory_plugins/GCE
%{python3_sitelib}/imagefactory_plugins/GCE/*

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.16-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.16-12
- Rebuilt for Python 3.13

* Sat Feb 10 2024 Adam Williamson <awilliam@redhat.com> - 1.1.16-11
- Bump with no changes to exceed F39 infra repo build NVR

* Sat Feb 10 2024 Adam Williamson <awilliam@redhat.com> - 1.1.16-10
- Backport PR #458 to go with backport of oz PR #310 (image size units)
- Backport PR #459 to hopefully fix Python 3.12 compatibility

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

* Wed Feb 16 2022 - Sandro Bonazzola <sbonazzo@redhat.com> - 1.1.16-1
- Rebase on 1.1.16

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 12 2021 Kevin Fenzi <kevin@scrye.com> - 1.1.15-12
- Add patch for stray isAlive call.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.15-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Kevin Fenzi <kevin@scrye.com> - 1.1.15-8.1
- Add patch for deprecated isAlive

* Tue Oct 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-8
- Add armv7l arch mapping

* Sat Oct 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-7
- Minor build fixes

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-5
- Update container patch to latest rev

* Wed Mar 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.15-4
- fix for RHBZ#1793927

* Fri Feb 07 2020 Kevin Fenzi <kevin@scrye.com> - 1.1.15-3
- Drop EC2 plugin as it uses euca2ools which is python2 and no longer in Fedora. Fixes bug #1762327

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.1.15-1
- 1.1.15

* Sat Nov 02 2019 Kevin Fenzi <kevin@scrye.com> - 1.1.14-2
- Upgrade to 1.1.14.
- Add patch for utf encoding in Docker plugin.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-0.20190528024256gita117084
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Aug 02 2018 Brendan Reilly <breilly@redhat.com> 1.1.12-2
- supports OVAs with subdirectories

* Tue May 01 2018 Brendan Reilly <breilly@redhat.com> - 1.1.12-1
- adding reference param section for new build for vsphere

* Tue Jan 16 2018 Brendan Reilly <breilly@redhat.com> - 1.1.11-2
- Add vsphere_os_type for OVF build

* Tue Oct 25 2016 Geert Jansen <gjansen@redhat.com> - 1.1.9-3
- Fix packaging for GCE plugin.

* Wed Jun 15 2016 Ian McLeod <imcleod@redhat.com> - 1.1.9-2
- remove xattr saving in Docker tar file creation

* Tue May 31 2016 Ian McLeod <imcleod@redhat.com> - 1.1.9-1
- Upstream release 1.1.9
  - Add HyperV Vagrant support
  - enhance vSphere and VMWare Fusion support

* Thu Mar 24 2016 Ian McLeod <imcleod@redhat.com> - 1.1.8-4
- add new docker base image version options
- fix koji issue when ICICLE generation is disabled

* Thu Mar 17 2016 Ian McLeod <imcleod@redhat.com> - 1.1.8-3
- temporarily disable OpenShift and RAX for F24

* Wed Mar 16 2016 Ian McLeod <imcleod@redhat.com> - 1.1.8-2
- enable non-x86_64 Docker base image builds

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

* Tue Oct 21 2014 Ian McLeod <imcleod@redhat.com> - 1.1.6-1
- Upstream 1.1.6 release

* Wed Jul 9 2014 Steve Loranz <sloranz@redhat.com> - 1.1.6
- Add Nova plugin

* Tue May 6 2014 Ian McLeod <imcleod@redhat.com> - 1.1.5-2
- Rebase with upstream
- Improved parameters parsing that couples with improved parameters CLI support in core imagefactory
- Add support for "offline" ICICLE generation in TinMan
- Rework IndirectionCloud to work with recent Oz releases

* Mon Sep 23 2013 Ian McLeod <imcleod@redhat.com> - 1.1.3-2
- Add abort() method to TinMan plugin

* Thu Aug 15 2013 Ian McLeod <imcleod@redhat.com> - 1.1.3
- Rebase with upstream
