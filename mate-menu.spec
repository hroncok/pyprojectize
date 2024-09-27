%global debug_package %{nil}
%global _name   mate_menu

Name:           mate-menu
Version:        20.04.3
Release:        18%{?dist}
Summary:        Advanced Menu for the MATE Desktop
# mate_menu/keybinding.py use MIT license and the rest is under GPLv2+
# Automatically converted from old format: GPLv2+ and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-MIT
BuildArch:      noarch
Url:            https://github.com/ubuntu-mate/%{name}
# downloading the tarball
# spectool -g mate-menu.spec
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         mate-menu_adjust-package-manager.patch
Patch2:         mate-menu_default-applications.patch

BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils

Requires:       mate-menus
Requires:       mozo
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       python3-xlib
Requires:       python3-setproctitle
Requires:       python3-unidecode
Requires:       beesu
Requires:       mate-panel


%description
An advanced menu for MATE. Supports filtering, favorites,
auto-session, and many other features.
This menu originated in the Linux Mint distribution and has
been ported to other distributions that ship the MATE Desktop
Environment.


%prep
%setup -q

%patch -P1 -p1 -b .adjust-package-manager
%patch -P2 -p1 -b .default-applications

# xdg-su isn't available in fedora
sed -i 's/xdg-su/beesu/g' %{_name}/execute.py

%build
%py3_build

%install
%py3_install

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{python3} %{buildroot}%{_usr}/lib/%{name}/*.py

# avoid rpmlint invalid-lc-messages-dir and incorrect-locale-subdir errors
rm -rf %{buildroot}%{_datadir}/locale/ber
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/es_419/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/nah/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/LC_MESSAGES/mate-menu.mo
rm -rf %{buildroot}%{_datadir}/locale/zh-Hans/

%find_lang %{name}


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_usr}/lib/%{name}/
%{python3_sitelib}/%{_name}/
%{python3_sitelib}/%{_name}-*-py3.*.egg-info/
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.mate.mate-menu*.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MateMenuApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateMenuAppletFactory.service
%{_mandir}/man1/mate-menu.1.*


%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 20.04.3-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 20.04.3-16
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 20.04.3-12
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 20.04.3-9
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20.04.3-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 20.04.3-4
- fix python pain
- fix rhbz (#1864117)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Wolfgang Ulbrich <fedora@raveit.de> - 20.04.3-1
- update to 20.04.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 19.04.0-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.04.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.04.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Wolfgang Ulbrich <fedora@raveit.de> - 19.04.0-1
- update to 19.04.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Wolfgang Ulbrich <fedora@raveit.de> - 18.04.3-2
- switch to python3

* Sat Nov 10 2018 Wolfgang Ulbrich <fedora@raveit.de> - 18.04.3-1
- update to 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.10.1-4
- Remove obsolete scriptlets

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17.10.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 17.10.1-1
- update to 17.10.1

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 16.10.1-5
- Update package-manager from yumex-dnf to dnfdragora

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 16.10.1-3
- remove depedency to beesu to avoid spam in maintainers mailbox

* Wed Oct 12 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 16.10.1-2
- add a note about licensing

* Thu Aug 04 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 16.10.1-1
- Initial package

