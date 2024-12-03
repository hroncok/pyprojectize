Name:           python-trezor
Version:        0.13.9
Release:        1%{?dist}
Summary:        Python library for communicating with TREZOR Hardware Wallet

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/trezor/python-trezor
Source0:        %{pypi_source trezor}

BuildArch:      noarch

BuildRequires:  pkgconfig(bash-completion)

%description
%{summary}.

%package -n python3-trezor
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       %{py3_dist hidapi}
Requires:       trezor-common >= 2.3.6

#Unit tests
BuildRequires:  python3-pytest
BuildRequires:  python3-typing-extensions
BuildRequires:  python3-requests
BuildRequires:  %{py3_dist construct-classes}

%description -n python3-trezor
%{summary}.


%prep
%autosetup -n trezor-%{version}
rm -rf trezor.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l trezorlib

install -Dpm 644 bash_completion.d/trezorctl.sh %{buildroot}%{bash_completions_dir}/trezorctl


%check
%pyproject_check_import

#Missing dependency on stellar_sdk
%{pytest} \
  tests/test_btc.py \
  tests/test_cosi.py \
  tests/test_protobuf_encoding.py \
  tests/test_protobuf_misc.py \
  tests/test_tools.py \
  tests/test_transport.py


%files -n python3-trezor -f %{pyproject_files}
%doc AUTHORS
%doc CHANGELOG.md
%doc README.md
%{_bindir}/trezorctl
%{bash_completions_dir}/trezorctl


%changelog
* Mon Sep 02 2024 Jonny Heggheim <hegjon@gmail.com> - 0.13.9-1
- Updated to version 0.13.9

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.13.8-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.13.8-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 28 2023 Jonny Heggheim <hegjon@gmail.com> - 0.13.8-1
- Updated to version 0.13.8

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.13.6-2
- Rebuilt for Python 3.12

* Sat Apr 29 2023 Jonny Heggheim <hegjon@gmail.com> - 0.13.6-1
- Updated to version 0.13.6

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Jonny Heggheim <hegjon@gmail.com> - 0.13.5-1
- Updated to version 0.13.5

* Mon Dec 05 2022 Jonny Heggheim <hegjon@gmail.com> - 0.13.4-2
- Enabled dependency on simple-rlp, it is now included in Fedora

* Mon Nov 21 2022 Jonny Heggheim <hegjon@gmail.com> - 0.13.4-1
- Updated to version 0.13.4

* Thu Jul 28 2022 Jonny Heggheim <hegjon@gmail.com> - 0.13.3-3
- Remove simple-rlp requirement that have a license that is not allowed in
  Fedora

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jonny Heggheim <hegjon@gmail.com> - 0.13.3-1
- Updated to version 0.13.3

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Jonny Heggheim <hegjon@gmail.com> - 0.13.0-1
- Updated to version 0.13.0

* Thu Dec 02 2021 Jonny Heggheim <hegjon@gmail.com> - 0.12.4-1
- Updated to version 0.12.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.2-4
- Rebuilt for Python 3.10

* Fri Apr 02 2021 Jonny Heggheim <hegjon@gmail.com> - 0.12.2-3
- Require trezor-common and enable unit tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Jonny Heggheim <hegjon@gmail.com> - 0.12.2-1
- Updated to version 0.12.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jonny Heggheim <hegjon@gmail.com> - 0.12.0-2
- Will install with any version of python-hidapi

* Thu Jun 04 2020 Jonny Heggheim <hegjon@gmail.com> - 0.12.0-1
- Updated to version 0.12.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.5-1
- Updated to version 0.11.5

* Mon Sep 23 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.4-3
- Use hashlib instead of pyblake2

* Fri Sep 20 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.4-2
- Disable dependency for python3-construct for Fedora 30 and lower.

* Mon Sep 09 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.4-1
- Updated to version 0.11.4

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.2-2
- Added missing requires on python3-construct

* Tue Apr 02 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.2-1
- Updated to version 0.11.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.1-1
- Updated to version 0.11.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Jonny Heggheim <hegjon@gmail.com> - 0.10.2-1
- Updated to version 0.10.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Jonny Heggheim <hegjon@gmail.com> - 0.9.1-2
- Added missing requires on python3-libusb1

* Tue Mar 06 2018 Jonny Heggheim <hegjon@gmail.com> - 0.9.1-1
- Updated to version 0.9.1
- Removed Python2 subpackage since Python2 is not longer supported upstream
- Dropped patches for protobuf2
- License is only LGPLv3, since bundled file with BSD license is replaced

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.16-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Jan Beran <jberan@redhat.com> - 0.7.16-4
- Python 3 subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.16-2
- Added patches for Fedora 25 to work with protobuffer2

* Thu Jul 06 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.16-1
- new version

* Mon Jun 19 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.15-3
- Added missing python2-requests requires

* Mon Jun 19 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.15-2
- Included correct requires for python2-trezor

* Mon Jun 19 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.15-1
- new version

* Wed May 03 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.13-1
- new version

* Tue Apr 11 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.12-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.8-2
- Include udev-rules

* Sun Nov 27 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.8-1
- new version

* Fri Nov 25 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.7-2
- added bundled(python-protobuf-json)
- included BSD in the license

* Thu Nov 24 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.7-1
- new version

* Thu Nov 17 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.6-1
- initial package
