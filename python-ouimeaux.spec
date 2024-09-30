%global srcname ouimeaux

# This is the correct folder for firewalld service files, even on x86_64
# It is not used for shared objects
%global fw_services %{_prefix}/lib/firewalld/services

Name: python-%{srcname}
Version: 0.8.2
Release: 26%{?dist}
Summary: Open source control for Belkin WeMo devices

# Automatically converted from old format: BSD and ASL 2.0 and MIT - review is highly recommended.
License: LicenseRef-Callaway-BSD AND Apache-2.0 AND LicenseRef-Callaway-MIT
Url: https://github.com/iancmcc/ouimeaux
Source0: https://github.com/iancmcc/%{srcname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: README.firewall
Source2: ouimeaux.xml

# https://patch-diff.githubusercontent.com/raw/iancmcc/ouimeaux/pull/204.patch
Patch0:  python-ouimeaux-cElementTree.patch
# https://github.com/knight-of-ni/ouimeaux/commit/2cea05f127499f42179b3699866b8e1444761b9f.patch
Patch1:  python-ouimeaux-unbundle-pysignals.patch

# https://github.com/iancmcc/ouimeaux/commit/607bfb3627c32937ca7e542e462053bbb124ee06.patch
Patch2:  python-ouimeaux-move-statechange.patch

# https://github.com/iancmcc/ouimeaux/commit/531c9d2c12d11ddaa6a5eaf2f87d5afc386f1d9a.patch
Patch3: python-ouimeaux-jquery.patch

# https://github.com/iancmcc/ouimeaux/commit/40cdcf352cc883bfc815c1a7a15aeb5520a63aaa.patch
Patch4: python-ouimeaux-getchildren.patch

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: findutils
BuildRequires: sed
BuildRequires: coreutils
BuildRequires: firewalld-filesystem

# Required for check
BuildRequires: %{py3_dist gevent} >= 1.3
BuildRequires: %{py3_dist requests} >= 2.3.0
BuildRequires: %{py3_dist pyyaml}
BuildRequires: %{py3_dist six}
BuildRequires: %{py3_dist pysignals}

%global _description %{expand:
Open source control for Belkin WeMo devices

- Supports WeMo Switch, Light Switch, Insight Switch and Motion
- Command-line tool to discover and control devices in your environment
- REST API to obtain information and perform actions on devices
- Simple responsive Web app provides device control on mobile
- Python API to interact with device at a low level
}

%description %_description

%package -n python3-%{srcname}
Requires: firewalld-filesystem
Requires: glyphicons-halflings-fonts
Requires: %{py3_dist pysignals}
Requires(post): firewalld-filesystem

Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p 1 -n %{srcname}-%{version}

# This project does not need future since
# pysignals is no longer bundled.
sed -i "/future/d" requirements.txt

install -pm 0644 %{SOURCE1} .

# Dont build examples, add to docs instead
mv ouimeaux/examples examples
rm examples/__init__.py

# Remove python shebang from __init__.py
sed -i -e '/^#!\//, 1d' ouimeaux/__init__.py

# fix python shebang and non-executable-script errors
find \( -name device.py -or -name service.py -or -name watch.py \) -type f -exec chmod +x {} \; -exec sed -i 's\^#!/usr/bin/env python$\#!%{python3}\' {} \;

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# remove non-ttf fonts and link the ttf font to the packaged file with the same name
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/server/static/fonts/glyphicons-halflings-regular.*
ln -sf /usr/share/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf %{buildroot}%{python3_sitelib}/%{srcname}/server/static/fonts/glyphicons-halflings-regular.ttf

# Install firewalld config
mkdir -p %{buildroot}%{fw_services}
install -pm 0644 %{SOURCE2} %{buildroot}%{fw_services}/

%post
%{?firewalld_reload}

%check
%{python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.md HISTORY.rst AUTHORS.rst CONTRIBUTING.rst README.firewall examples/
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/wemo
%{fw_services}/%{srcname}.xml

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.2-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.8.2-24
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.8.2-20
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.8.2-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-14
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-13
- replace webfts runtime requirement with glyphicons-halflings-fonts
- remove all non-ttf glyphicons fonts from package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-10
- ElementTree getchildren method deprecated. Use list instead.

* Mon Jun 22 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-9
- Patch3 was missing in last build

* Mon Jun 22 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-8
- rebundle jquery and update to latest 1.12.x

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-7
- unbundle statechange class from pysignals

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-6
- unbundle pysignals into separate pacakge

* Tue Jun 16 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-5
- patch for python 3.9 compatbility
- move runtime requirements into subpackage
- unbundle glyphicons-halflings
- bootstrap java files are ASL 2.0 license
- unbundle jquery

* Mon Jun 15 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-4
- Author updated releases page to match version in source, dropping git commit

* Mon May 25 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-3.git.6b6984b
- Define fw_services macro

* Mon May 25 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-2.git.6b6984b
- Add firewalld config and readme
- move examples to docs

* Sun May 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-1.git.6b6984b
- Initial package

