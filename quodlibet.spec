Name:		quodlibet
Version:	4.6.0
Release:	7%{?dist}
Summary:	A music management program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://quodlibet.readthedocs.org/en/latest/
Source0:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/quodlibet-%{version}.tar.gz
Source1:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/quodlibet-%{version}.tar.gz.sig
Source2:	https://keys.openpgp.org/vks/v1/by-fingerprint/E0AA0F031DBD80FFBA57B06D5A62D0CAB6264964
Source3:	README.fedora

# https://github.com/quodlibet/quodlibet/pull/4361
Patch0:		0001-make-flake8-happy.patch

# https://github.com/quodlibet/quodlibet/pull/4358
Patch1:		0001-Fix-startup-on-Python-3.12.patch
Patch2:		0002-Fix-SoundCloud-browser-tests.patch

# https://github.com/quodlibet/quodlibet/pull/4363
Patch3:		0001-Add-missing-network-mark-to-test_click_add_station.patch

# https://github.com/quodlibet/quodlibet/pull/4563
Patch4:		0001-Squeezebox-plugins-Migrate-to-raw-socket-connection.patch

# https://github.com/quodlibet/quodlibet/pull/4566
Patch5:		0001-tests-Filter-out-unsupported-file-formats-properly.patch

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 3.5
# needed for py_byte_compile
BuildRequires:	python3-devel
# needed for tests
BuildRequires:	glibc-langpack-en
BuildRequires:	gnupg2
BuildRequires:	gstreamer1
BuildRequires:	gstreamer1-plugins-good
BuildRequires:	gtk3 >= 3.18
BuildRequires:	libmodplug
BuildRequires:	python3-feedparser
BuildRequires:	python3-gobject >= 3.18
BuildRequires:	python3-mutagen >= 1.14
BuildRequires:	python3-pytest
BuildRequires:	python3-pyvirtualdisplay
BuildRequires:	xine-lib

Requires:	exfalso = %{version}-%{release}
Requires:	gstreamer1
Requires:	gstreamer1-plugins-base
Requires:	gstreamer1-plugins-good
Requires:	python3-dbus

%description
Quod Libet is a music management program. It provides several different ways
to view your audio library, as well as support for Internet radio and
audio feeds. It has extremely flexible metadata tag editing and searching
capabilities.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.


%package -n exfalso
Summary: Tag editor for various music files

Requires:	adwaita-icon-theme
Requires:	gtk3 >= 3.18
Requires:	hicolor-icon-theme
Requires:	libsoup >= 2.44
Requires:	pkgconfig
Requires:	python3-gobject >= 3.18
Requires:	python3 >= 3.5
Requires:	python3-mutagen >= 1.14
Requires:	python3-feedparser

# for musicbrainz plugin
Requires:	python3-musicbrainzngs >= 0.6


%description -n exfalso
Ex Falso is a tag editor with the same tag editing interface as Quod Libet,
but it does not play files.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.


%package zsh-completion
Summary: zsh completion files for %{name}
Requires: quodlibet = %{version}-%{release}
Requires: zsh

%description zsh-completion
This package installs %{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1

install -pm 0644 %{S:3} .


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.QuodLibet.desktop
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.ExFalso.desktop

%find_lang quodlibet


%check
%pytest -m "not network and not quality"


%files
%doc README.fedora
%{_bindir}/quodlibet
%{_datadir}/applications/io.github.quodlibet.QuodLibet.desktop
%{_datadir}/bash-completion/completions/quodlibet
%{_datadir}/gnome-shell/search-providers/io.github.quodlibet.QuodLibet-search-provider.ini
%{_datadir}/icons/hicolor/*x*/apps/io.github.quodlibet.QuodLibet.png
%{_datadir}/appdata/io.github.quodlibet.QuodLibet.appdata.xml
%{_datadir}/dbus-1/services/net.sacredchao.QuodLibet.service
%{_mandir}/man1/quodlibet.1*


%files -n exfalso -f %{name}.lang
%license COPYING
%doc NEWS.rst README.rst
%{_bindir}/exfalso
%{_bindir}/operon
%{_datadir}/applications/io.github.quodlibet.ExFalso.desktop
%{_datadir}/bash-completion/completions/operon
%{_mandir}/man1/exfalso.1*
%{_mandir}/man1/operon.1*
%{_datadir}/icons/hicolor/*x*/apps/io.github.quodlibet.ExFalso.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/appdata/io.github.quodlibet.ExFalso.appdata.xml

%{python3_sitelib}/quodlibet-%{version}.dist-info
%{python3_sitelib}/quodlibet


%files zsh-completion
%{_datadir}/zsh/site-functions/_quodlibet


%changelog
* Wed Sep 04 2024 LuK1337 <priv.luk@gmail.com> - 4.6.0-7
- Fix failing tests on rawhide

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.6.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.6.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 26 2023 LuK1337 <priv.luk@gmail.com> - 4.6.0-1
- update to recent upstream version

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.5.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Johannes Lips <hannes@fedoraproject.org> - 4.5.0-4
- built without distutils for python 3.12

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.5.0-2
- Rebuilt for Python 3.11

* Wed Mar 30 2022 Johannes Lips <hannes@fedoraproject.org> - 4.5.0-1
- update to recent upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 01 2021 Johannes Lips <hannes@fedoraproject.org> - 4.5.0-0.1
- update to recent upstream git to fix bug #2008422

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.0-2
- Rebuilt for Python 3.10

* Mon Mar 01 2021 Johannes Lips <hannes@fedoraproject.org> - 4.4.0-1
- update to recent upstream release 4.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-3
- Rebuilt for Python 3.9

* Mon Apr 13 2020 Johannes Lips <hannes@fedoraproject.org> - 4.3.0-2
- fixed icon theme dependency - bug #1814119

* Mon Feb 24 2020 Johannes Lips <hannes@fedoraproject.org> - 4.3.0-1
- update to recent upstream release 4.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Björn Esser <besser82@fedoraproject.org> - 4.2.1-3
- Fix FTBFS

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Johannes Lips <hannes@fedoraproject.org> - 4.2.0-1
- update to recent upstream release 4.2.1

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-2
- Require python3-gobject instead of python2-gobject

* Fri Nov 23 2018 Johannes Lips <hannes@fedoraproject.org> - 4.2.0-1
- update to recent upstream release 4.2.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Johannes Lips <hannes@fedoraproject.org> - 4.1.0-3
- Rebuilt for Python 3.7 site-tag

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Johannes Lips <hannes@fedoraproject.org> - 4.1.0-1
- update to recent upstream release 4.1.0
- name changes to multiple files

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.2-2
- Remove obsolete scriptlets

* Thu Jan 18 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.2-1
- update to recent upstream release 4.0.2

* Sat Jan 13 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.1-1
- update to recent upstream release 4.0.1

* Wed Jan 03 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.0-2
- updated missing deps for bug #1461590

* Wed Jan 03 2018 Johannes Lips <hannes@fedoraproject.org> - 4.0.0-1
- transition to python3
- license changed to GPLv2+

* Fri Aug 11 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.23-1
- First version for Fedora Extras
