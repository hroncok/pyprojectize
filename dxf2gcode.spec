%{?python_enable_dependency_generator}
%global date 20240509
%global vdate %(x=%{date}; echo "${x:0:4}-${x:4:2}-${x:6:2}")
%global py_setup st-setup.py


Name:           dxf2gcode
Version:        %{date}
Release:        4%{?dist}
Summary:        2D drawings to CNC machine compatible G-Code converter
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
Url:            https://sourceforge.net/p/dxf2gcode/wiki/Home/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}-%{version}.zip

BuildArch:      noarch

BuildRequires:  /usr/bin/git
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  qt5-linguist
BuildRequires:  /usr/bin/pyuic5
BuildRequires:  /usr/bin/pyrcc5
BuildRequires:  python3dist(pyopengl)
BuildRequires:  python3dist(pyqt5)
BuildRequires:  python3dist(configobj)

Requires:       /usr/bin/pdftops
Requires:       /usr/bin/pstoedit
Requires:       hicolor-icon-theme


%description
%{name} is a tool for converting 2D (DXF, PDF, PS) drawings to CNC machine
compatible GCode. It has the following features:
    - Integration in EMC2,
    - Fully adjustable Postprocessor,
    - G0 moves reduction by route optimization,
    - Import of DXF and PDF,
    - Improved accuracy for splines import by Line and Arc's,
    - Mill parameter specification by layers,
    - Drag knife and lathe support,
    - Breaks a.k.a Tabs support,
    - AutoCAD Blocks and Inserts,
    - Multiple tools,
    - Multiple language support: English, German, French, Russian,
    - 3D viewer.


%prep
%autosetup -S git


%generate_buildrequires
%pyproject_buildrequires


%build
# regenerate *images5_rc.py and *ui5.py files
python3 ./make_py_uic.py 5
# regenerate translation files
lrelease-qt5 i18n/*.ts
%pyproject_wheel


%install
%pyproject_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%license COPYING
%doc README.txt
%{_bindir}/%{name}
%{python3_sitelib}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/i18n
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/*.appdata.xml


%changelog
* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 20240509-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240509-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 20240509-2
- Rebuilt for Python 3.13 (fixes RHBZ#2291513)

* Thu May 09 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20240509-1
- Update to the latest available version, fixes (rhbz#2277765)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Python Maint <python-maint@redhat.com> - 20191025-12
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 20191025-9
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20191025-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20191025-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20191025-1
- Update to the latest available version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 20190103-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20190103-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20190103-2
- Enable python dependency generator

* Thu Jan 03 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20190103-1
- Update to the latest available version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170925-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 20170925-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170925-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20170925-2
- Remove obsolete scriptlets

* Mon Sep 25 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20170925-1
- Update to the lastest available version.

* Thu Sep 14 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20170915-1
- Drop upstream patches,
- Use tarball generated by python3 st-setup.py sdist

* Tue Sep 12 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20170503-2
- Add upstream fixes.

* Wed Sep 06 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20170503-1
- Initial RPM release.
