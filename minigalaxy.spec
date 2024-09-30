%global forgeurl https://github.com/sharkwouter/minigalaxy
%global tag %{version}

Name:           minigalaxy
Version:        1.3.0
%forgemeta
Release:        %autorelease
Summary:        GOG client for Linux that lets you download and play your GOG Linux games
BuildArch:      noarch

# CC-BY-3.0:    Logo image (data/minigalaxy.png)
License:        GPL-3.0-or-later and CC-BY-3.0
URL:            https://sharkwouter.github.io/minigalaxy
Source0:        %{forgesource}

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel >= 3.30

BuildRequires:  python3dist(requests)

Requires:       hicolor-icon-theme
Requires:       python3-requests
Requires:       unzip
Requires:       webkit2gtk3

Recommends:     dosbox
Recommends:     gamemode
Recommends:     innoextract
Recommends:     mangohud
Recommends:     wine
Recommends:     wine-dxvk

Suggests:       scummvm

%description
A simple GOG client for Linux that lets you download and play your GOG Linux
games.


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{pyproject_files}
%license THIRD-PARTY-LICENSES.md
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml


%changelog
%autochangelog
