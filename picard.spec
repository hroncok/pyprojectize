%global forgeurl    https://github.com/musicbrainz/picard/
%global commit      311b42c964ddb7ca57617fe7204fdfb4cdc920ac

Name:           picard
Version:        2.12.1
Release:        %autorelease
Summary:        MusicBrainz-based audio tagger
License:        GPL-2.0-or-later

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        picard.rpmlintrc
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       hicolor-icon-theme
Requires:       python3-qt5
Requires:       python3-dateutil
Requires:       python3-libdiscid
Requires:       python3-mutagen >= 1.37
Requires:       python3-markdown
Requires:       qt5-qtmultimedia
Recommends:     rsgain

%if 0%{?rhel}
ExcludeArch:    ppc64
%endif

%description
Picard is an audio tagging application using data from the MusicBrainz
database. The tagger is album or release oriented, rather than
track-oriented.

%prep
%forgesetup
%autosetup -n %{archivename}

%build
%{__python3} setup.py config
%py3_build

%install
%py3_install

desktop-file-install \
  --delete-original --remove-category="Application"   \
  --dir=%{buildroot}%{_datadir}/applications      \
  %{buildroot}%{_datadir}/applications/*

%find_lang %{name}
%find_lang %{name}-attributes
%find_lang %{name}-constants
%find_lang %{name}-countries

%check

%files -f %{name}.lang -f %{name}-attributes.lang -f %{name}-constants.lang -f %{name}-countries.lang
%doc AUTHORS.txt
%license COPYING.txt
%{_bindir}/picard
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.*
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml
%{python3_sitearch}/*egg-info
%{python3_sitearch}/picard/

%changelog
%autochangelog
