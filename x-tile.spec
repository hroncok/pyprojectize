Name:           x-tile
Version:        3.3
Release:        15%{?dist}
Summary:        A GTK application to tile windows in different ways

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.giuspen.com/x-tile/
Source0:        https://github.com/giuspen/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# Fix build with setuptools >= 61.0
Patch0:         %{name}-3.3-setuptools.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
Requires:       %{py3_dist pygobject}
Requires:       %{py3_dist pycairo}
Requires:       gtk3
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
X-tile is an application that allows you to select a number of windows and tile
them in different ways.  X-tile works on any X desktop (GNOME, KDE, XFCE,
LXDE...).
The main features are: many tiling geometries, undo tiling, invert tiling order,
optional system tray docking and menu, filter to avoid listing some windows,
filter to check some windows by default, command line interface.


%prep
%autosetup

# Remove bundled egg-info
rm -rf *.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
mkdir -p build/scripts-%{python3_version}/
%pyproject_wheel


%install
%pyproject_install
install -Dpm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%files -f %{name}.lang
%license license
%{_bindir}/%{name}
%{python3_sitelib}/X_Tile.dist-info
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3-13
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.3-10
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3-7
- Fix build with setuptools >= 61.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3-1
- Update to 3.3

* Mon Sep 07 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2-1
- Update to 3.2

* Mon Aug 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1-1
- Initial RPM release, from previously retired package (with contribution of
  Vlastimil Holer)
