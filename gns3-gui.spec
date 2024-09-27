# Pre-release
#%%global git_tag 2.1.0rc3

%global git_tag %{version}

Name:           gns3-gui
Version:        2.2.49
Release:        1%{?dist}
Summary:        GNS3 graphical user interface

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://gns3.com
Source0:        https://github.com/GNS3/%{name}/archive/v%{git_tag}/%{name}-%{git_tag}.tar.gz
Source3:        %{name}.appdata.xml

BuildArch:      noarch

BuildRequires:  python3-devel 
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires: telnet 
Requires: socat
Requires: python3-jsonschema 
Requires: python3-psutil 
Requires: python3-qt5

%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

This package contains the client graphical user interface.

%prep
%autosetup -n %{name}-%{git_tag}

# Relax strict reqs
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r 's/sentry-sdk.*//g' requirements.txt
sed -i -r 's/truststore.*//g' requirements.txt
# Lower psutil>=5.8.0
sed -i -r 's/psutil>=6.0.0/psutil>=5.8.0/' requirements.txt
sed -i -r 's/distro>=1.9.*/distro>=1.5.0/' requirements.txt
sed -i -r 's/jsonschema>=4.23,<4.24/jsonschema>=3.2.0/' requirements.txt

# Disable update alerts
sed -i 's/"check_for_update": True,/"check_for_update": False,/' gns3/settings.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install

# Remove shebang
for lib in `find %{buildroot}/%{python3_sitelib}/ -name '*.py'`; do
 echo $lib
 sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done

# Remove empty files
find %{buildroot}/%{python3_sitelib}/ -name '.keep' -type f -delete

# Remove exec perm
find %{buildroot}/%{python3_sitelib}/ -type f -exec chmod -x {} \;

# AppData
mkdir -p %{buildroot}/%{_datadir}/appdata/
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/appdata/


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/gns3*.desktop


%files 
%license LICENSE
%doc README.md AUTHORS CHANGELOG
%{python3_sitelib}/gns3/
%{python3_sitelib}/gns3_gui*.dist-info/
%{_bindir}/gns3
%{_datadir}/applications/gns3*.desktop
%{_datadir}/icons/hicolor/*/apps/*gns3*
%{_datadir}/icons/hicolor/*/mimetypes/*-gns3*
%{_datadir}/mime/packages/gns3-gui.xml
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Thu Aug  8 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.49-1
- Update to 2.2.49

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.48.1-3
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

* Mon Feb 26 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.46-1
- Update to 2.2.46

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.45-1
- Update to 2.2.45

* Tue Nov  7 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.44.1-1
- Update to 2.2.44.1

* Mon Nov  6 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.44-1
- Update to 2.2.44

* Mon Sep 25 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.43-2
- Backported importlib_resources fix
- lower distro and setuptools requirements
- Removed cpulimit required for gns3server/compute/qemu/qemu_vm.py
- gns3-net-converter removed from requirements in 2.0.0 beta3
- python3-raven removed from requirements in 2.2.9

* Tue Sep 19 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.43-1
- Update to 2.2.43

* Wed Sep  6 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.42-2
- Fixed jsonschema requirement

* Thu Aug 10 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.42-1
- Update to 2.2.42

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.41-1
- Update to 2.2.41
- Removed sending stats

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.40.1-2
- Rebuilt for Python 3.12

* Sat Jun 10 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.40.1-1
- Update to 2.2.40.1

* Tue Jun 06 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.40-1
- Update to 2.2.40

* Sun May 21 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.39-2
- gns3/utils/get_resource.py requires setuptools(pkg_resources)

* Mon May 15 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.39-1
- Update to 2.2.39

* Tue Feb 28 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.38-1
- Update to 2.2.38

* Tue Jan 31 2023 Alexey Kurov <nucleo@fedoraproject.org> - 2.2.37-1
- Update to 2.2.37

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.34-1
- Update to 2.2.34

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.33.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.33.1-2
- Lower distro requirement

* Mon Jun 27 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.33.1-1
- Update to 2.2.33.1

* Tue Jun 21 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.33-1
- Update to 2.2.33

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.32-2
- Rebuilt for Python 3.11

* Thu May 05 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.32-1
- Update to 2.2.32

* Tue Mar 15 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.31-2
- Relax requirements

* Fri Mar 04 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.31-1
- Update to 2.2.31

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.2.29-1
- Update to 2.2.29

* Thu Dec 16 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.28-1
- Update to 2.2.28

* Fri Dec 03 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.27-1
- Update to 2.2.27

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

* Fri Apr 23 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.20-2
- lower psutil requirements

* Fri Apr 09 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.20-1
- Update to 2.2.20

* Mon Mar 08 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.19-1
- Update to 2.2.19

* Thu Mar 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.2.18-1
- Update to 2.2.18

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

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.7-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7-1
- Update to 2.2.7

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.6-1
- Update to 2.2.6
- Drop duplicate desktop entry

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Thu Jan 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.20-1
- Update to 2.1.20

* Wed Sep 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.1.16-5
- drop dep on python3-sip

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-2
- Relax strict reqs

* Sat Apr 27 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.16-1
- Update to 2.1.16 (rhbz #1668653 #1668654)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.11-2
- Add missing PyQt dep

* Sat Nov 17 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.112.1.11-11
- Update to 2.1.11 (rhbz #1581506)

* Wed Jul 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8 (rhbz #1581506)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.5-2
- Rebuilt for Python 3.7

* Sat Apr 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5 (rhbz #1569275)

* Sun Mar 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (rhbz #1554315)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3 (rhbz #1536428)

* Thu Jan 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2 (rhbz #1532421)
- Disable anonymous data collection

* Sat Dec 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1 (rhbz #1528825)

* Mon Nov 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 final

* Sat Nov 04 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc3
- Update to 2.1.0-0.rc3

* Sun Oct 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.1.0-0.rc1
- Update to 2.1.0 RC1
- Fix appdata

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-2
- Disable update alert

* Sat Jul 15 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Sat May 13 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-2
- Update files section

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Fri Apr 14 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Sat Apr 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-2
- Rebuild for Python 3.6

* Sun Sep 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Fri Aug 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-2
- Fix appdata

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1
- Fix the url

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-2
- Minor spec fixes
- Provide AppData

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-1
- Initial spec 
