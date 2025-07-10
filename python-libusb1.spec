Name:           python-libusb1
Version:        3.1.0
Release:        5%{?dist}
Summary:        Pure-python wrapper for libusb-1.0

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/vpelletier/python-libusb1
Source0:        %{pypi_source libusb1}
Source1:        https://github.com/vpelletier/%{name}/releases/download/%{version}/libusb1-%{version}.tar.gz.asc

#https://github.com/vpelletier/python-libusb1/blob/5bc97a163ee1ca98ca6bfc11045f5c4ab94ec654/KEYS
#Wed Jan 05 2022, exported the upstream gpg key using the command:
#gpg2 --armor --export --export-options export-minimal 983AE8B73B9115987A923845CAC936914257B0C1 > gpgkey-python-libusb1.gpg
Source2:        gpgkey-python-libusb1.gpg

#Fixes test errors on Python 3.13, not sure if the problem is fixed in runtime
#Upstream report https://github.com/vpelletier/python-libusb1/issues/103
Patch0:         https://patch-diff.githubusercontent.com/raw/vpelletier/python-libusb1/pull/104.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-wheel
BuildRequires:  libusb1-devel

BuildRequires:  gnupg2

Requires:       libusb1

%global _description %{expand:
Pure-python wrapper for libusb-1.0.

Supports all transfer types, both in synchronous and asynchronous mode.}

%description %_description


%package -n python3-libusb1
Summary: %{summary}

%description -n python3-libusb1 %_description


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n libusb1-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l libusb1 usb1

%check
%pyproject_check_import

%{python3} setup.py test

%files -n python3-libusb1 -f %{pyproject_files}
%doc README.rst PKG-INFO

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-5
- convert license to SPDX

* Tue Sep 03 2024 Jonny Heggheim <hegjon@gmail.com> - 3.1.0-4
- Fixed test failure on Python 3.13

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.13

* Tue May 07 2024 Antoine Damhet <antoine.damhet@gmail.com> - 3.1.0-1
- Update to version 3.1.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Jonny Heggheim <hegjon@gmail.com> - 3.0.0-3
- Rebuilt for Python 3.10
- Use the correct build dependency libusb1-devel

* Mon May 23 2022 Jonny Heggheim <hegjon@gmail.com> - 3.0.0-2
- Stop using deprecated zero-argument pypi_source macro

* Fri Feb 25 2022 Jonny Heggheim <hegjon@gmail.com> - 3.0.0-1
- Updated to version 3.0.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Jonny Heggheim <hegjon@gmail.com> - 2.0.1-2
- Verify the signature of the source tarball

* Fri Nov 26 2021 Jonny Heggheim <hegjon@gmail.com> - 2.0.1-1
- Updated to 2.0.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.2-2
- Rebuilt for Python 3.10

* Fri Apr 02 2021 Jonny Heggheim <hegjon@gmail.com> - 1.9.2-1
- Updated to 1.9.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 2020 Jonny Heggheim <hegjon@gmail.com> - 1.9.1-1
- Updated to 1.9.1

* Sun Nov 29 2020 Jonny Heggheim <hegjon@gmail.com> - 1.8.1-1
- Updated to 1.8.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jonny Heggheim <hegjon@gmail.com> - 1.8-1
- Updated to 1.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Jonny Heggheim <hegjon@gmail.com> - 1.6.4-4
- Removed Python2 sub-package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-2
- Rebuilt for Python 3.7

* Tue Mar 20 2018 Jonny Heggheim <hegjon@gmail.com> - 1.6.4-1
- Inital version
