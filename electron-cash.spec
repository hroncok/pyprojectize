Name:           electron-cash
Version:        4.4.1
Release:        3%{?dist}
Summary:        A lightweight Bitcoin Cash client

License:        MIT
URL:            https://electroncash.org/
Source0:        https://github.com/Electron-Cash/Electron-Cash/releases/download/%{version}/electron_cash-%{version}.tar.gz
Source1:        https://github.com/Electron-Cash/keys-n-hashes/raw/master/sigs-and-sums/%{version}/win-linux/electron_cash-%{version}.tar.gz.asc
#Sun 15 Dec 2019, exported the upstream gpg key using the command:
#gpg2 --armor --export --export-options export-minimal D56C110F4555F371AEEFCB254FD06489EFF1DDE1 D465135F97D0047E18E99DC321810A542031C02C > gpgkey-electron-cash.gpg
Source2:        gpgkey-electron-cash.gpg

Patch0:         relax-protobuf-version.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

BuildRequires:  libappstream-glib
BuildRequires:  gnupg2

Requires:       qt5-qtbase
Requires:       qt5-qtsvg
Requires:       qt5-qtmultimedia

# Manually from contrib/requirements/requirements-binaries.txt
Requires:       python3-qt5
Requires:       python3-pycryptodomex
Requires:       python3-psutil
Requires:       python3-cryptography
Requires:       python3-zxing-cpp >= 2.0.0

Requires:       libsecp256k1 >= 0.20.9
Requires:       zbar
Requires:       tor

Provides:       bundled(google-noto-emoji-color-fonts)

Suggests:       python3-trezor >= 0.12

%description
Electron Cash is an easy to use Bitcoin Cash client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin block chain.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n electron_cash-%{version}

#pre-built bundled library
rm -v ./electroncash/*.so*

#pre-built tor binary
rm -v ./electroncash/tor/bin/tor

#budled libraries
rm -rfv ./packages/

%generate_buildrequires
%pyproject_buildrequires

%build
pyrcc5 icons.qrc -o electroncash_gui/qt/icons_rc.py
%{pyproject_wheel}

%install
%{pyproject_install}

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}%{_datadir}/applications/%{name}.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.electroncash.ElectronCash.appdata.xml

%files
%doc AUTHORS
%doc README.rst
%doc RELEASE-NOTES
%license LICENCE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scaleable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.electroncash.ElectronCash.appdata.xml
%{python3_sitelib}/electroncash/
%{python3_sitelib}/electroncash_gui/
%{python3_sitelib}/electroncash_plugins/
%{python3_sitelib}/Electron_Cash-%{version}.dist-info

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.4.1-2
- Rebuilt for Python 3.13

* Fri May 03 2024 Jonny Heggheim <hegjon@gmail.com> - 4.4.1-1
- Updated to version 4.4.1

* Thu Mar 07 2024 Jonny Heggheim <hegjon@gmail.com> - 4.4.0-3
- Relax python3-zxing-cpp requirements

* Wed Mar 06 2024 Jonny Heggheim <hegjon@gmail.com> - 4.4.0-2
- Add missing runtime requires

* Wed Mar 06 2024 Jonny Heggheim <hegjon@gmail.com> - 4.4.0-1
- Updated to version 4.4.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jonny Heggheim <hegjon@gmail.com> - 4.3.1-4
- Fix Python 3.12 build error

* Tue Jul 18 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.3.1-3
- Drop x86 support (leaf package)

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.12

* Sat May 20 2023 Jonny Heggheim <hegjon@gmail.com> - 4.3.1-1
- Updated to version 4.3.1

* Wed May 17 2023 Jonny Heggheim <hegjon@gmail.com> - 4.3.0-2
- Relaxed version for python3-protobuf

* Wed May 17 2023 Jonny Heggheim <hegjon@gmail.com> - 4.3.0-1
- Updated to version 4.3.0

* Tue Jan 24 2023 Jonny Heggheim <hegjon@gmail.com> - 4.2.14-1
- Updated to version 4.2.14

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Jonny Heggheim <hegjon@gmail.com> - 4.2.13-1
- Updated to version 4.2.13

* Mon Nov 14 2022 Jonny Heggheim <hegjon@gmail.com> - 4.2.12-1
- Updated to version 4.2.12

* Sat Aug 20 2022 Jonny Heggheim <hegjon@gmail.com> - 4.2.11-1
- Updated to version 4.2.11

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.2.10-3
- Rebuilt for Python 3.11

* Sun May 29 2022 Jonny Heggheim <hegjon@gmail.com> - 4.2.10-2
- Fix issue with missing support for ripemd in openssl 3

* Sun May 29 2022 Jonny Heggheim <hegjon@gmail.com> - 4.2.10-1
- Updated to version 4.2.10

* Wed May 11 2022 Jonny Heggheim <hegjon@gmail.com> - 4.2.9-1
- Updated to version 4.2.9

* Sat May 07 2022 Jonny Heggheim <hegjon@gmail.com> - 4.2.8-1
- Updated to version 4.2.8

* Sat Feb 26 2022 Jonny Heggheim <hegjon@gmail.com> - 4.2.7-1
- Updated to version 4.2.7

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Jonny Heggheim <hegjon@gmail.com> - 4.2.6-1
- Updated to version 4.2.6

* Fri Aug 20 2021 Jonny Heggheim <hegjon@gmail.com> - 4.2.5-1
- Updated to version 4.2.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Jonny Heggheim <hegjon@gmail.com> - 4.2.4-3
- Enable qdarkstyle dependency

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2.4-2
- Rebuilt for Python 3.10

* Fri Mar 05 2021 Jonny Heggheim <hegjon@gmail.com> - 4.2.4-1
- Updated to version 4.2.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Jonny Heggheim <hegjon@gmail.com> - 4.2.3-1
- Updated to version 4.2.3

* Thu Nov 19 2020 Jonny Heggheim <hegjon@gmail.com> - 4.2.2-1
- Updated to version 4.2.2

* Wed Nov 18 2020 Jonny Heggheim <hegjon@gmail.com> - 4.2.1-1
- Updated to version 4.2.1

* Thu Oct 22 2020 Jonny Heggheim <hegjon@gmail.com> - 4.2.0-1
- Updated to version 4.2.0

* Mon Sep 14 2020 Jonny Heggheim <hegjon@gmail.com> - 4.1.1-1
- Updated to version 4.1.1

* Fri Jul 31 2020 Jonny Heggheim <hegjon@gmail.com> - 4.1.0-2
- Added dependency on python-certifi

* Fri Jul 31 2020 Jonny Heggheim <hegjon@gmail.com> - 4.1.0-1
- Updated to version 4.1.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.15-1
- Updated to version 4.0.15

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.14-3
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.14-2
- Remove protobuf <3.9 constraint

* Wed Mar 25 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.14-1
- Updated to version 4.0.14

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.12-2
- Require a newer version of libsecp256k1

* Sat Dec 14 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.12-1
- Updated to version 4.0.12

* Tue Nov 19 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.11-1
- Updated to version 4.0.11

* Mon Sep 09 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.10-1
- Updated to version 4.0.10

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.9-3
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.9-2
- Remove locked version for python-dateutil

* Mon Aug 12 2019 Jonny Heggheim <hegjon@gmail.com>
- Updated to version 4.0.9

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.8-1
- Updated to version 4.0.8

* Tue Jun 25 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.7-3
- Added missing dependency on python3-qt5

* Mon Jun 24 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.7-2
- Added missing dependencies

* Fri Jun 21 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.7-1
- Updated to version 4.0.7

* Thu Jun 06 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.6-1
- Updated to version 4.0.6

* Mon May 27 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.5-1
- Updated to version 4.0.5

* Mon May 27 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.4-1
- Updated to version 4.0.4

* Wed May 22 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.3-1
- Updated to version 4.0.3

* Sat Apr 20 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.2-1
- Updated to version 4.0.2

* Thu Apr 04 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.1-1
- Updated to version 4.0.1

* Tue Apr 02 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.0-2
- Added dependency on libsecp256k1 because of CashShuffle

* Sat Mar 30 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.0-1
- Updated to version 4.0.0

* Mon Feb 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.6-2
- Disabled optional requires qdarkstyle that is not packed for Fedora

* Sun Feb 24 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.6-1
- Updated to version 3.3.6

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.5-3
- Add python3-pycryptodomex as requires

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.5-2
- Bumped the version requires for python3-trezor

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.5-1
- Updated to version 3.3.5

* Sat Dec 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.4-2
- Enable python dependency generator

* Sat Dec 29 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.4-1
- Updated to version 3.3.4

* Wed Nov 14 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.2-1
- Updated to version 3.3.2

* Sat Jul 21 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.1-1
- Updated to version 3.3.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3-1
- Updated to version 3.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2-2
- Rebuilt for Python 3.7

* Wed Apr 25 2018 Jonny Heggheim <hegjon@gmail.com> - 3.2-1
- Updated to version 3.2

* Tue Mar 20 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.6-2
- Added conflicts on older trezor since it does not work with newer version of
  electron-cash

* Sat Mar 17 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.6-1
- Updated to version 3.1.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.2-1
- Updated to version 3.1.2

* Sun Jan 07 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.1-1
- Updated to version 3.1.1

* Fri Jan 05 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1-1
- Updated to version 3.1

* Fri Dec 15 2017 Jonny Heggheim <hegjon@gmail.com> - 3.0-1
- Inital version
