%global py_name Screenkey
Name:		screenkey
Version:	1.5
Release:	10%{?dist}
Summary:	A screencast tool to display your keys
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://www.thregr.org/~wavexx/software/%{name}
Source0:	%{URL}/releases/%{name}-%{version}.tar.gz
Source1:        %{URL}/releases/%{name}-%{version}.tar.gz.asc
Source2:        https://www.thregr.org/~wavexx/files/wavexx.asc

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-babel
BuildRequires:	desktop-file-utils

BuildRequires: gnupg2

Requires:   python3-gobject
Requires:   python3-cairo
Requires:   slop

Recommends: fontawesome-fonts
Recommends: libappindicator-gtk3

%description
A screencast tool to display your keys, featuring:
* Several keyboard translation methods
* Key composition/input method support
* Configurable font/size/position
* Highlighting of recent keystrokes
* Improved backspace processing
* Normal/Emacs/Mac caps modes
* Multi-monitor support
* Dynamic recording control etc.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
%py3_build

%install
%py3_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc README.rst NEWS.rst
%license COPYING.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.thregr.%{name}.metainfo.xml
%{python3_sitelib}/%{py_name}/
%{python3_sitelib}/%{name}-%{version}-*.egg-info

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5-8
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5-5
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5-2
- Rebuilt for Python 3.11

* Sun Jan 30 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.5-1
- New upstream release 1.5

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.4-2
- Remove appstreamcli validation (koji doesn't have internet connection to verify)

* Thu Oct 14 2021 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.4-1
- Cleanup build requirements

* Thu Oct 14 2021 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.4-0
- New version 1.4
- Switches to babel for i18n

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.2-3
- Address Fedora review comments, v2.
- Fix BR typo of python3-gobject
- Add missing BR for intltool and gettext
- Add missing runtime dependency on slop
- Add fontawesome and appindicator recommendation
- Install locale files

* Fri Sep 11 2020 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.2-2
- Address Fedora review comments

* Fri Sep 11 2020 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.2-1
- Initial packaging
