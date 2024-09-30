# For pre-release
%global git_tag %{version}

# Filter auto-generated deps from bundled shell script (which depends on busybox only)
%global __requires_exclude_from ^%{python3_sitelib}/gns3server/compute/docker/resources/.*$

Name:           gns3-server
Version:        2.2.49
Release:        2%{?dist}
Summary:        Graphical Network Simulator 3

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://gns3.com
Source0:        https://github.com/GNS3/gns3-server/archive/v%{git_tag}/%{name}-%{git_tag}.tar.gz
Source1:        gns3.service
Patch0:         0001-changing-busybox-udhcpc-script-path.patch

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: python3-sphinx
BuildRequires: make

Requires(post): edk2-ovmf
Recommends: docker busybox
Recommends: qemu-kvm
Requires: ubridge >= 0.9.14
Requires: cpulimit



%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple
workstations to powerful routers.

This is the server package which provides an HTTP REST API for the client (GUI).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
%description doc
%{name}-doc package contains documentation.


%prep
%autosetup -S git -n %{name}-%{git_tag}

# Relax requirements
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r 's/distro>=1.9.*/distro>=1.5.0/' requirements.txt
sed -i -r 's/psutil>=6.0.0/psutil>=5.8.0/' requirements.txt
sed -i -r 's/aiofiles>=24.1.0,<25.0/aiofiles>=0.7/' requirements.txt
sed -i -r 's/aiohttp>=3.9.5,<3.10/aiohttp>=3.9.3/' requirements.txt
sed -i -r 's/Jinja2>=3.1.4,<3.2/jinja2>=2.11.3/' requirements.txt
sed -i -r 's/jsonschema>=4.23,<4.24/jsonschema>=3.2.0/' requirements.txt
sed -i -r 's/py-cpuinfo>=9.0.0,<10.0/py-cpuinfo>=8.0.0/' requirements.txt
sed -i -r 's/async-timeout>=4.0.3,<4.1/async-timeout>=4.0.2/' requirements.txt
sed -i -r 's/sentry-sdk.*//g' requirements.txt
sed -i -r 's/truststore.*//g' requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l gns3server

# Remove shebang
find %{buildroot}/%{python3_sitelib}/ -name '*.py' -print \
   -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;
# Remove empty file
rm -f %{buildroot}/%{python3_sitelib}/gns3server/symbols/.gitkeep

# Build the doc1834283s
%{make_build} -C docs html
/bin/rm -f docs/_build/html/.buildinfo

## Systemd service part
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
mkdir -p  %{buildroot}%{_sharedstatedir}/gns3

# Don't bundle OVMF_CODE.fd OVMF_VARS.fd with the package
rm -fv %{buildroot}/%{python3_sitelib}/gns3server/disks/OVMF_CODE.fd
rm -fv %{buildroot}/%{python3_sitelib}/gns3server/disks/OVMF_VARS.fd

%check


%files -f %{pyproject_files}
%doc README.md AUTHORS CHANGELOG
%{_bindir}/gns3server
%{_bindir}/gns3vmnet
%{_bindir}/gns3loopback
%{_unitdir}/gns3.service
%dir %attr(0755,gns3,gns3) %{_sharedstatedir}/gns3

%files doc
%license LICENSE
%doc docs/_build/html

%pre
getent group gns3 >/dev/null || groupadd -r gns3
getent passwd gns3 >/dev/null || \
       useradd -r -g gns3 -d /var/lib/gns3 -s /sbin/nologin \
               -c "gns3 server" gns3
exit 0

%post
[ -d "/var/lib/gns3" ] && chown -R gns3:gns3 %{_sharedstatedir}/gns3
%systemd_post gns3.service

# Replace bundled OVMF_CODE.fd OVMF_VARS.fd with Fedora ones
cp -fp %{_datadir}/edk2/ovmf/OVMF_CODE.fd %{python3_sitelib}/gns3server/disks/OVMF_CODE.fd
cp -fp %{_datadir}/edk2/ovmf/OVMF_VARS.fd %{python3_sitelib}/gns3server/disks/OVMF_VARS.fd

%preun
%systemd_preun gns3.service

%postun
%systemd_postun_with_restart gns3.service

%changelog
* Mon Aug 26 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.49-2
- lower aiohttp requirements

* Thu Aug  8 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.49-1
- Update to 2.2.49

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.48.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.48.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.48.1-1
- Update to 2.2.48.1

* Wed Jul 10 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.48-1
- Update to 2.2.48

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.47-2
- Rebuilt for Python 3.13

* Wed May 15 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.47-1
- Update to 2.2.47

* Mon Feb 26 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.46-2
- /usr/sbin/busybox copied in ~/.local/share/GNS3 at runtime

* Mon Feb 26 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.46-1
- Update to 2.2.46

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.45-1
- Update to 2.2.45

* Tue Nov  7 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.44.1-1
- Update to 2.2.44.1

* Mon Nov  6 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.44-1
- Update to 2.2.44

* Tue Sep 19 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.43-2
- Backported importlib_resources fix
- lower distro and jinja2 requirements
- cpulimit required for gns3server/compute/qemu/qemu_vm.py

* Tue Sep 19 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.43-1
- Update to 2.2.43

* Thu Aug 10 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.42-1
- Update to 2.2.42

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.41-1
- Update to 2.2.41
- Replace bundled OVMF_CODE.fd OVMF_VARS.fd with Fedora ones

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.2.40.1-2
- Rebuilt for Python 3.12

* Sat Jun 10 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.40.1-1
- Update to 2.2.40.1

* Tue Jun 06 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.40-1
- Update to 2.2.40

* Mon May 15 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.39-1
- Update to 2.2.39

* Mon Apr 24 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.2.38-2
- Relax importlib-resources requirement
  https://src.fedoraproject.org/rpms/gns3-server/pull-request/3

* Tue Feb 28 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.38-1
- Update to 2.2.38

* Sat Feb 18 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.37-4
- backport python3.11 fix

* Fri Feb 17 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.37-3
- Update relaxed requirements

* Fri Feb 17 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.37-2
- Update relaxed requirements

* Tue Jan 31 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.37-1
- Update to 2.2.37

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.34-1
- Update to 2.2.34
- backport python3.11 fix - rhbz#2134944

* Thu Jul 21 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.33.1-3
- Drop busybox at build time

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.33.1-1
- Update to 2.2.33.1

* Tue Jun 21 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.33-1
- Update to 2.2.33

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.32-3
- Rebuilt for Python 3.11

* Sun May 15 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.32-2
- lower distro requirement

* Thu May 05 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.32-1
- Update to 2.2.32

* Tue Mar 15 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.31-2
- Update relaxed requirements

* Fri Mar 04 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.31-1
- Update to 2.2.31

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.29-1
- Update to 2.2.29

* Thu Dec 16 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.28-1
- Update to 2.2.28

* Fri Dec 03 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.27-1
- Update to 2.2.7

* Thu Nov 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.26-1
- Update to 2.2.26

* Wed Sep 15 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.25-1
- Update to 2.2.25

* Thu Aug 26 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.24-1
- Update to 2.2.24

* Sat Aug 07 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.23-1
- Update to 2.2.23

* Sat Jul 31 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.22-1
- Update to 2.2.22

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.21-2
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.21-1
- Update to 2.2.21

* Mon Apr 12 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.20-2
- Rework enforced dependencies

* Fri Apr 09 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.20-1
- Update to 2.2.20

* Mon Mar 08 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.19-1
- Update to 2.2.19

* Thu Mar 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.18-1
- Update to 2.2.18

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.17-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.17-1
- Update to 2.2.17

* Mon Nov 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.16-1
- Update to 2.2.16

* Wed Oct 07 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.15-1
- Update to 2.2.15

* Fri Sep 25 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.14-1
- Update to 2.2.14

* Wed Aug 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.12-1
- Update to 2.2.12

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.11-1
- Update to 2.2.11

* Tue Jun 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.10-1
- Update to 2.2.10

* Fri Jun 05 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.9-1
- Update to 2.2.9
- Fix docker image IP - rhbz#1834283

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.7-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7-1
- Update to 2.2.7

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.6-1
- Update to 2.2.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Fri Jan 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.20-2
- Add back a modern requires exclusion

* Thu Jan 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.20-1
- Update to 2.1.20
- Drop aiohttp bundle
- Fix optional dependencies with recommends - rhbz#1763762
- Don't distribute fedora busybox with the package.

* Sun Sep 15 2019 Othman Madjoudj <athmane@fedoraproject.org> - 2.1.16-7
- Add back Docker support (rhbz #1570826)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Athmane Madjoudj <athmane@fedoraproject.org>  - 2.1.16-3
- Add a patch to disable the broken embedded shell (rhbz #1690958)

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-2
- Fix typo in reqs
- Relax strict reqs

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-1
- Update to 2.1.16
- Fix broken deps (rhbz #1690958)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.11-1
- Update to 2.1.11 (rhbz #1581507)
- Drop unsued patch

* Wed Jul 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.8-2
- Add patch to fix py37 build (GH #1370)

* Mon Jul 16 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8 (rhbz #1581507)

* Mon Jul 16 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-4
- Rebuilt without bundled aiohttp

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.5-3
- Rebuilt for Python 3.7

* Tue Apr 24 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-3
- Fix issues reported by rpmlint

* Sat Apr 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-2
- Add option to bundle aiohttp since it gets broken very often

* Sat Apr 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5 (rhbz #1569276)

* Sun Mar 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.4-2
- Make sure to pull ubridge >= 0.9.14

* Sun Mar 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (rhbz #1554316)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3 (rhbz #1536429)

* Thu Jan 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2 (rhbz #1532422)

* Wed Jan 10 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.1-2
- Build docs with Python 3

* Sat Dec 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1 (rhbz #1528826)
- Remove non-needed workarounds

* Mon Nov 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 final
- Pick older libs as a temp bugs workaround

* Sat Nov 04 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc3
- Update to 2.1.0 RC3
- Relax version requirements

* Sun Oct 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc1
- Update to 2.1.0 RC1 which support recent aiohttp lib.

* Sun Jul 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-7
- Fix the reqs in prepration for 2.1 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-5
- Correct python3-aiohttp-cors version dep

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-4
- Bump release number for copr update

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-3
- Remove patch for aiohttp >= 2 since gns3 was instable
- Use the exact deps version as recommended by upstream

* Sat Jul 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-2
- Add a patch to support aiohttp >= 2

* Sat Jul 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Sat May 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-2
- Some spec fixes due to major version change

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Apr 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-3
- Add temporary workaround for py egg

* Fri Apr 14 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-2
- Remove some workarounds

* Fri Apr 14 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Sat Apr 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.3-2
- Add versioned deps

* Fri Feb 10 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.2-3
- Remove docker BR (not available in all arches)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-2
- Rebuild for Python 3.6

* Sun Sep 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2
- Remove upstreamed patches

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-4
- Fix typo in egg dir
- Build/ship the doc
- update BR

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org>  - 1.5.0-3
- Spec cleanup
- Add patch to move vmnet to gns3 namespace.
- Merge service sub pkg (too small)

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-2
- Minor spec fixes
- Provide a systemd service

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-1
- Initial spec 
