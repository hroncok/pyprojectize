%bcond check 1

Name:           solaar
Version:        1.1.13
Release:        3%{?dist}
Summary:        Device manager for a wide range of Logitech devices
URL:            https://github.com/pwr/Solaar
Source:         %{url}/archive/%{version}/Solaar-%{version}.tar.gz

# Fedora-specific patches
Patch:          0002-Install-alternative-udev-rules-for-wayland-compatibi.patch
Patch:          0003-Install-autostart-desktop-file.patch
Patch:          solaar-use-system-hid-parser.patch

BuildArch:      noarch
License:        GPL-2.0-or-later

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
%if %{with check}
BuildRequires:  gtk3
BuildRequires:  python3-dbus
BuildRequires:  python3-evdev
BuildRequires:  python3-psutil
BuildRequires:  python3-gobject-base
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-pyudev
BuildRequires:  python3-pyyaml
%endif

Requires:       hicolor-icon-theme
Requires:       solaar-udev
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)
Recommends:     gtk3
Recommends:     libappindicator-gtk3
Recommends:     python3-gobject-base
Recommends:     python3-hid-parser

%description
Solaar is a device manager for Logitech's Unifying Receiver peripherals. It is
able to pair/unpair devices to the receiver and, for most devices, read battery
status.

gtk3 is recommended.  Without it, you can run solaar commands to view the
configuration of the devices and pair/unpair peripherals but you cannot use the
graphical interface.


%package doc
Summary:        Developer documentation for Solaar
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
This package provides documentation for Solaar, a device manager for
Logitech's Unifying Receiver peripherals.


%package udev
Summary:        Udev rules for Logitech receivers
BuildArch:      noarch

%description udev
This package contains udev rules which grant users permission to access various
connected Logitech wireless receivers.  This includes Unifying receivers,
various types of Nano receivers and some other types which can be used by
Solaar.


%prep
%autosetup -p1 -n Solaar-%{version}
rm docs/.gitignore
rm -rv lib/hid_parser


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
tools/po-compile.sh


%install
%pyproject_install

install -pm755 tools/hidconsole %{buildroot}%{_bindir}

# Remove pointless shebangs
sed -i -e '1d' %{buildroot}/%{python3_sitelib}/solaar/{gtk,tasks}.py

# Fix shebang line
sed -i -e '1s,^#!.*$,#!/usr/bin/python3,' %{buildroot}/%{_bindir}/hidconsole

desktop-file-validate %{buildroot}/%{_datadir}/applications/solaar.desktop

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/solaar.desktop

%find_lang %{name}

%check
%pytest

%posttrans udev
# This is needed to apply permissions to existing devices when the package is
# installed.
# Skip triggering udevd when it is note accessible, e.g. containers or
# rpm-ostree-based systems.
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm trigger --subsystem-match=hidraw --action=add
fi

%files -f %{name}.lang
%license LICENSE.txt
%doc CHANGELOG.md COPYRIGHT Release_Notes.md share/README
%{_bindir}/solaar
%{_bindir}/hidconsole
%{python3_sitelib}/hidapi
%{python3_sitelib}/keysyms
%{python3_sitelib}/logitech_receiver
%{python3_sitelib}/solaar
%{python3_sitelib}/solaar-%{version}*.dist-info
%{_datadir}/applications/solaar.desktop
%{_datadir}/icons/hicolor/32x32/apps/solaar-light_*.png
%{_datadir}/icons/hicolor/scalable/apps/solaar.svg
%{_datadir}/icons/hicolor/scalable/apps/solaar-attention.svg
%{_datadir}/icons/hicolor/scalable/apps/solaar-init.svg
%{_datadir}/icons/hicolor/scalable/apps/solaar-symbolic.svg
%{_metainfodir}/io.github.pwr_solaar.solaar.metainfo.xml
%config(noreplace) %{_sysconfdir}/xdg/autostart/solaar.desktop


%files doc
%doc docs/*


%files udev
%license LICENSE.txt
%{_udevrulesdir}/42-logitech-unify-permissions.rules


%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.13-2
- Rebuilt for Python 3.13

* Sun May 12 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.1.13-1
- update to 1.1.13

* Sat May 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.1.12-1
- update to 1.1.12 (#2276196)
- run tests and include test dependencies

* Wed Mar 06 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.1.11-1
- update to 1.1.11 (#2263677)
- drop obsolete patch
- use SPDX license identifier
- drop ancient Obsoletes/Provides

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.1.10-1
- update to 1.1.10 (#2239784)
- drop obsolete patch

* Fri Jul 28 2023 Carl George <carl@george.computer> - 1.1.9-4
- Use alternative udev rules for wayland compatibility

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.9-2
- Rebuilt for Python 3.12

* Fri Apr 21 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.1.9-1
- update to 1.1.9 (#2184776)
- add weak dependency on libappindicator-gtk3, required to show tray icon (#2181248)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.1.8-1
- update to 1.1.8 (#2152380)
- add weak dependency on hid-parser, required to recognize some devices

* Sun Nov 06 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.1.7-2
- drop unnecessary dependency

* Fri Nov 04 2022 Mark E. Fuller <fuller@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7 (#2137568)

* Tue Sep 20 2022 Mark E. Fuller <fuller@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5 (#2126961)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.1.4-1
- update to 1.1.4 (#2103752)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.11

* Thu May 05 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.1.3-1
- update to 1.1.3 (#2078519)
- fix rule processing under Wayland (#2070753, #2071252)

* Sun Mar 27 2022 Dominik Mierzejewski <rpm@greysector.net> - 1.1.2-1
- update to 1.1.2 (#2068769)
- patch to lower evdev version requirement
- add explicit build dependency on setuptools
- sort build dependencies

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Dominik Mierzejewski <rpm@greysector.net> - 1.1.1-1
- update to 1.1.1 (#2035614)

* Tue Nov 30 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.1.0-1
- update to 1.1.0 (#2026986)
- fix exceptions when adding devices (#2008448, #2015360)
- fix exception when applying settings fails (#2020706, #2022320)

* Mon Oct 11 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.0.7-1
- update to 1.0.7 (#2009721)
- fix exception when disabling "MX Keys" (#2003483)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.6-2
- Rebuilt for Python 3.10

* Tue May 11 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.0.6-1
- update to 1.0.6 (#1953333)
- improve handling of unavailable devices on startup or resume (#1921575, #1912132, #1942301, #1946104)
- add a conditional weak dependency on appindicator extension for gnome-shell

* Sun Mar 21 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.0.5-1
- update to 1.0.5 (#1933413)
- drop obsolete patch
- drop redundant explicit Requires: on pyudev
- python3-gobject is optional (for GUI only), move to Recommends:
- fix unknown battery status regression

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.0.4-3
- build and include translations (https://github.com/pwr-Solaar/Solaar/issues/1049)

* Sun Nov 08 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.4-2
- improve handling of receiver disconnections (#1891242, #1891655, #1891717)

* Sat Oct 24 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.4-1
- update to 1.0.4 release (#1890613)
- drop obsolete patch

* Sun Aug 16 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.3-1
- update to 1.0.3 release (#1860667)
- backport patch to fix exception with missing locale (#1811313)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.2-1
- update to 1.0.2 release
- fix install path for udev rules in setup.py

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-0.3.rc1
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.2-0.2.rc1.20200322git563ef0d
- Don't trigger udev if socket is not accessible (#1764565, patch by Stefano Figura)

* Tue Mar 24 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.0.2-0.1.rc1.20200322git563ef0d
- update to 1.0.2-rc1 + two recent commits
- drop obsolete patches

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.0.1-1
- update to 1.0.1
- preserve timestamps
- fix wrong version in setup.py
- add missing requires for unowned icons directory

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11.gitf0fc63e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-10.20180813gitf0fc63e
- Add optional gtk3 dependency.
- Document optional gtk3 dependency.
- Add patch for better output when gtk3 is not installed.

* Tue Aug 14 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-9.20180813gitf0fc63e
- Install the hidconsole executable.
- Fix permissions on the udev rules file.

* Mon Aug 13 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-8.20180813gitf0fc63e
- Update to latest git head.
- Drop upstreamed patch.

* Fri Jul 27 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-7.20180720git59b7285
- Include a subpackage containing the udev rules, and have it obsolete/provide
  unifying-receiver-udev.
- Add build dependency on systemd (for %%_udevrulesdir).
- Add %%posttranstrigger on the udev subpackage to auto-activate the rules.
- Drop solaar-cli executable.  It just spits out a warning to use solaar.

* Fri Jul 20 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-6.20180720git59b7285
- Update to new git snapshot.
- Use forge macros to simplify things.
- Convert to python3 and modern python macros.
- Add patch for python3.7 compatibility.
- Better way to fix shebang lines.

* Fri Jul 20 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.2-5.20150528gitcf27328
- Use versioned python macros.
- Remove icon-cache scriptlets which are not needed in Fedora.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.2-4.20150528gitcf27328.9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 0.9.2-4.20150528gitcf27328.7
- Remove unnecessary Group: tags

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 06 2016 Richard Fearn <richardfearn@gmail.com> - 0.9.2-4.20150528gitcf27328.4
- Add missing dependency on python-gobject (bug #1355869)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4.20150528gitcf27328.3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4.20150528gitcf27328.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4.20150528gitcf27328.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Eric Smith <brouhaha@fedoraproject.org> 0.9.2-4.20150528gitcf27328
- Update to upstream git snapshot

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 24 2013 Eric Smith <brouhaha@fedoraproject.org> 0.9.2-2
- Changed files line for .egg-info to be less dependent on Python version,
  to build for EL6 which uses Python 2.6.

* Thu Jul 25 2013 Eric Smith <brouhaha@fedoraproject.org> 0.9.2-1
- Updated to latest upstream.

* Fri Jul 19 2013 Eric Smith <eric@brouhaha.com> 0.9.1-2
- Added scriptlets to update icon caches.
- Added BuildRequires for desktop-file-utils.

* Sun Jul 14 2013 Eric Smith <eric@brouhaha.com> 0.9.1-1
- Updated to latest upstream.
- Consistently use "solaar" rather than name macro.
- Removed extraneous dependency on pygtk2.
- Moved documentation into subpackage.

* Sun Apr 28 2013 Eric Smith <eric@brouhaha.com> 0.8.7-1
- initial version
