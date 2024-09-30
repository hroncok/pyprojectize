%global libname btchip
%global srcname %{libname}-python

Name:     python-%{libname}
Version:  0.1.32
Release:  15%{?dist}
Summary:  Python communication library for Ledger Hardware Wallet products

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:  Apache-2.0
URL:      https://github.com/LedgerHQ/btchip-python
Source0:  %{pypi_source}
Source1:  https://raw.githubusercontent.com/LedgerHQ/udev-rules/765b7fdf57b20fd9326cedf48ee52e905024ab4f/20-hw1.rules
Source2:  https://raw.githubusercontent.com/LedgerHQ/btchip-python/3a941ed1a257a8ad519a473e361cda16fb4f36fd/LICENSE

BuildArch:     noarch
BuildRequires: systemd

%global _description %{expand:
btchip-python is a python API for communicating primarily with the
Ledger HW.1 hardware bitcoin wallet. This library also adds compatibility
to Electrum in order to use the "Nano", "Nano S", and other Ledger-based
hardware wallets.}

%description %_description

%package -n python3-%{libname}
Summary: %{summary}
BuildRequires: python3-devel
Requires: python3-hidapi hidapi >= 0.7.99
Requires: python3-mnemonic python-%{libname}-common

%description -n python3-%{libname} %_description


%package -n python-%{libname}-common
Summary: udev rules for Ledger devices

%description -n python-%{libname}-common
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf btchip_python.egg-info
cp %{SOURCE2} .

# Adjust version contstraint to comply with PEP-440
# https://peps.python.org/pep-0440/
# This makes package compatible with python-packaging>=22.0.0
sed -i 's/1.6.12-4build1/1.6.12/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files btchip
mkdir -p %{buildroot}%{_udevrulesdir}
install -m644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/20-ledger.rules


%check
# Tests try to contact PyPi


%files -n python3-%{libname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n python-%{libname}-common
%{_udevrulesdir}/20-ledger.rules


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.32-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.32-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.32-9
- Rebuilt for Python 3.12

* Wed Feb 01 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.1.32-8
- Adjust version constraint to make it compatible with new packaging>=22.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.32-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.32-2
- Rebuilt for Python 3.10

* Thu Apr 01 2021 Jonny Heggheim <hegjon@gmail.com> - 0.1.32-1
- Update to 0.1.32

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 2020 Jonny Heggheim <hegjon@gmail.com> - 0.1.31-2
- Updated udev-rules

* Wed Dec 09 2020 Jonny Heggheim <hegjon@gmail.com> - 0.1.31-1
- Update to 0.1.31

* Wed Dec 09 2020 Jonny Heggheim <hegjon@gmail.com> - 0.1.30-1
- Update to 0.1.30

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.28-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.28-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.28-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Michael Goodwin <xenithorb@fedoraproject.org> - v0.1.28-1
- Update to 0.1.28

* Mon Oct 01 2018 Jonny Heggheim <hegjon@gmail.com> - 0.1.26-4
- Removed Python 2 sub-package
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.26-2
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Michael Goodwin <xenithorb@fedoraproject.org> - v0.1.26-1
- Update to 0.1.26 (0.1.25 was a same-day release)

* Thu Feb 22 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.24-1
- Update to 0.1.24

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.21-4
- Fix ${sum} mistake in common package

* Mon Oct 16 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.21-3
- Add python-mnemonic dependency for BIP39 support during dongle setup
- New sub-package: python3-btchip (upstream added py3 support) (#1499686)
- New sub-package: python-btchip-common - current for the btchip udev rules
    - Add udev rules (20-hw1.rules) for automatic device recognition

* Wed Oct 04 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.21-2
- Update to 0.1.21

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.20-1
- Update to 0.1.20

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 4 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.18-3
- Final finishing touches after package review

* Tue Jan 3 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.18-2
- Improve SPEC for most recent python packaging guidelines

* Sun Jan 1 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.1.18-1
- Initial packaging of btchip-python for Fedora
