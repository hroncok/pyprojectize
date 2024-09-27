Name:           vorta
Version:        0.9.1
Release:        2%{?dist}
Summary:        A GUI for Borg Backup
License:        GPL-3.0-only AND BSD-2-Clause AND OFL-1.1
# src/vorta/qt_single_application.py if BSD-2-Clause
# src/vorta/assets/icons are OFL-1.1
URL:            https://vorta.borgbase.com/
Source0:        https://github.com/borgbase/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       borgbackup
Requires:       hicolor-icon-theme
Requires:       qt5-qtsvg

BuildArch:      noarch

# https://github.com/borgbase/vorta/commit/0cc15e3d3d647bae1782f2c21eafacbf2c8073c6
# should be upstream in > 0.9.1
Patch:          fix-appdata.xml.patch

%description
Vorta is a backup client for macOS and Linux desktops.
It integrates the mighty BorgBackup with your desktop environment
to protect your data from disk failure, ransomware and theft

%prep
%autosetup -p1
# https://github.com/borgbase/vorta/issues/1690
sed -i 's/platformdirs >=2.6.0/platformdirs >=2.3.0/g' setup.cfg

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
# all tests require a GUI (pyqt5) to complete
# so they won't work in mock

%install
%pyproject_install
%pyproject_save_files %{name}
#%%pyproject_install
install -D -p -m 644 src/vorta/assets/icons/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.borgbase.Vorta.svg
install -D -p -m 644 package/icon-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/com.borgbase.Vorta-symbolic.svg
install -D -p src/vorta/assets/metadata/com.borgbase.Vorta.desktop -t %{buildroot}%{_datadir}/applications/
install -D -p src/vorta/assets/metadata/com.borgbase.Vorta.appdata.xml -t %{buildroot}/%{_metainfodir}/

desktop-file-validate %{buildroot}/%{_datadir}/applications/com.borgbase.Vorta.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files -f %{pyproject_files}
%doc README.md CONTRIBUTORS.md
%license LICENSE.txt
%{_bindir}/vorta
%{_datadir}/applications/com.borgbase.Vorta.desktop
%{_metainfodir}/com.borgbase.Vorta.appdata.xml
%{_datadir}/icons/hicolor/*/apps/com.borgbase.Vorta*.svg


%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 jonathanspw <jonathan@almalinux.org> - 0.9.1-1
- update to 0.9.1 rhbz#2257791

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.8.12-6
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Python Maint <python-maint@redhat.com> - 0.8.12-3
- Rebuilt for Python 3.12

* Mon Apr 10 2023 Jonathan Wright <jonathan@almalinux.org> - 0.8.12-2
- Override minimum platformdirs version

* Mon Apr 10 2023 Jonathan Wright <jonathan@almalinux.org> - 0.8.12-1
- Update to 0.8.12

* Sun Apr 09 2023 Jonathan Wright <jonathan@almalinux.org> - 0.8.11-1
- Update to 0.8.11 rhbz#2185461

* Mon Jan 23 2023 Jonathan Wright <jonathan@almalinux.org> - 0.8.10-2
- Add requires qt5-qtsvg rhbz#2162072

* Sun Jan 22 2023 Jonathan Wright <jonathan@almalinux.org> - 0.8.10-1
- Update to 0.8.10 rhbz#2163001

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Jonathan Wright <jonathan@almalinux.org> - 0.8.9-1
- Update to 0.8.9 rhbz#2140355

* Mon Aug 22 2022 Jonathan Wright <jonathan@almalinux.org> - 0.8.7-1
- Initial package build
- Thanks to luminoso for his work in COPR
- rhbz#2120883
