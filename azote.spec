# -*-Mode: rpm-spec -*-

Name:      azote
Version:   1.13.0
Release:   %autorelease
BuildArch: noarch
Summary:   Wallpaper and color manager for Sway, i3 and some other WMs

# GPLv3: main program
# BSD: colorthief.py
License:   GPL-3.0-only and BSD-1-Clause

URL:       https://github.com/nwg-piotr/azote
Source0:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: python3
BuildRequires: python3-devel

Requires: python3-pillow
Requires: python3-gobject
Requires: ((feh and xrandr) if Xserver)
Requires: ((swaybg and wlr-randr) if wayfire)
Requires: python3-cairo

Recommends: python3-send2trash
Recommends: ImageMagick
Recommends: ((maim and slop) if Xserver)

Provides: bundled(python3-colorthief) = 0.2.1

%description
Azote is a GTK+3 - based picture browser and background setter, as the
front-end to the swaybg (sway/Wayland) and feh (X windows) commands. It
also includes several color management tools.

The program is confirmed to work on sway, i3, Openbox, Fluxbox and dwm
window managers, on Arch Linux, Void Linux, Debian and Fedora.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}
#desktop-file-edit --set-icon %{_datadir}/pixmaps/%{name}.svg dist/%{name}.desktop
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/applications dist/%{name}.desktop
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/%{name} dist/*.png dist/*.svg
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/pixmaps dist/azote.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
for lib in %{buildroot}%{python3_sitelib}/%{name}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%files -f %{pyproject_files}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%doc README.md


%changelog
%autochangelog
