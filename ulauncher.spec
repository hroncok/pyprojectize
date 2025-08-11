Name:           ulauncher
Version:        5.15.7
Release:        %{autorelease}
Summary:        Linux Application Launcher
BuildArch:      noarch

License:        GPL-3.0-or-later
URL:            https://github.com/Ulauncher/Ulauncher
Source0:        %{url}/releases/download/%{version}/%{name}_%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2293346
Patch:          https://github.com/Ulauncher/Ulauncher/commit/08b52d2.patch#/support-gir1.2-webkit2-4.1.patch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  keybinder3-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-devel >= 3.30
BuildRequires:  python3-inotify
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-pyxdg
BuildRequires:  python3-websocket-client
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3dist(requests)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme
Requires:       keybinder3
Requires:       webkit2gtk4.1
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-inotify
Requires:       python3-Levenshtein
Requires:       python3-pyxdg
Requires:       python3-websocket-client
Requires:       wmctrl

Recommends:     libappindicator-gtk3

%description
Ulauncher is a fast application launcher for Linux. It's is written in Python,
using GTK+.


%prep
%autosetup -n %{name} -p1
# Newer version patch: https://github.com/Ulauncher/Ulauncher/issues/1194
sed -i "s|version=''|version='%{version}'|g" setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{name}


%check
%pyproject_check_import
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service


%files -f %{pyproject_files}
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-toggle
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%dir %{_datadir}/icons/breeze/
%dir %{_datadir}/icons/elementary/
%dir %{_datadir}/icons/gnome/
%dir %{_datadir}/icons/ubuntu-mono-dark/
%dir %{_datadir}/icons/ubuntu-mono-light/
%{_datadir}/icons/breeze/apps/48/%{name}-indicator.svg
%{_datadir}/icons/elementary/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}-indicator.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/icons/ubuntu-mono-*/scalable/apps/%{name}-indicator.svg
%{_userunitdir}/%{name}.service


%changelog
%autochangelog
