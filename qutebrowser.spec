%global srcname qutebrowser

Name:		%{srcname}
Version:	3.2.0
Release:	%autorelease
Summary:	A keyboard-driven, vim-like browser based on PyQt5 and QtWebEngine
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		http://www.qutebrowser.org
Source0:	https://github.com/%{srcname}/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	asciidoc
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
Requires:	qt6-qtbase
Requires:	qt6-qtdeclarative
Requires:	python3-pyqt6
Requires:	python3-jinja2
Requires:	python3-PyYAML
Requires:	(qt6-qtwebengine and python3-pyqt6-webengine)
Recommends:	qt6-qtwebengine-devtools
Recommends:	python3-pygments
Recommends:	python3-adblock

%description
qutebrowser is a keyboard-focused browser with a minimal GUI. It’s based on
Python, PyQt5 and QtWebEngine and free software, licensed under the GPL.
It was inspired by other browsers/addons like dwb and Vimperator/Pentadactyl.


%prep
%autosetup -p 1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
# Compile the man page
a2x -f manpage doc/qutebrowser.1.asciidoc

# Find all *.py files and if their first line is exactly '#!/usr/bin/env python3'
# then replace it with '#!/usr/bin/python3' (if it's the 1st line).
find . -type f -iname "*.py" -exec sed -i '1s_^#!/usr/bin/env python3$_#!/usr/bin/python3_' {} +

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}

# Install desktop and appdata files
desktop-file-install \
	--add-category="Network" \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	misc/org.%{srcname}.%{srcname}.desktop

install -Dm644 misc/org.qutebrowser.qutebrowser.appdata.xml -t %{buildroot}%{_datadir}/metainfo

# Install man page
install -Dm644 doc/%{srcname}.1 -t %{buildroot}%{_mandir}/man1

# Install icons
install -Dm644 qutebrowser/icons/qutebrowser.svg \
	-t "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps"
for i in 16 24 32 48 64 128 256 512; do
	install -Dm644 "qutebrowser/icons/qutebrowser-${i}x${i}.png" \
		"%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/qutebrowser.png"
done

# Set __main__.py as executable
chmod 755 %{buildroot}%{python3_sitelib}/%{srcname}/__main__.py

# Remove zero-length files:
# https://fedoraproject.org/wiki/Packaging_tricks#Zero_length_files
find %{buildroot} -size 0 -delete

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{pyproject_files}
%doc README.asciidoc doc/changelog.asciidoc doc
%{_bindir}/%{srcname}
%{_datadir}/applications/org.%{srcname}.%{srcname}.desktop
%{_mandir}/man1/%{srcname}.1*
%{_datadir}/icons/hicolor/scalable/apps/%{srcname}.svg
%{_datadir}/icons/hicolor/16x16/apps/%{srcname}.png
%{_datadir}/icons/hicolor/24x24/apps/%{srcname}.png
%{_datadir}/icons/hicolor/32x32/apps/%{srcname}.png
%{_datadir}/icons/hicolor/48x48/apps/%{srcname}.png
%{_datadir}/icons/hicolor/64x64/apps/%{srcname}.png
%{_datadir}/icons/hicolor/128x128/apps/%{srcname}.png
%{_datadir}/icons/hicolor/256x256/apps/%{srcname}.png
%{_datadir}/icons/hicolor/512x512/apps/%{srcname}.png
%{_datadir}/metainfo/org.qutebrowser.qutebrowser.appdata.xml

%changelog
%autochangelog
