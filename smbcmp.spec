#
# spec file for package smbcmp
#

Name:		smbcmp
Version:	0.1
Release:	19%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Summary:	Small curses utility to diff, compare and debug SMB network traces
URL:		https://github.com/smbcmp/smbcmp
Group:		Development/Tools/Debuggers
Source0:	https://github.com/smbcmp/smbcmp/archive/v0.1/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3 >= 3.4
BuildRequires:	python3-setuptools
Requires:	wireshark-cli

%description
Small curses utility to diff, compare and debug SMB network traces.

%package gui
Summary:	GUI version of smbcmp
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python3-wxpython4

%description gui
smbcmp is a debug tool to diff and compare network captures aimed
towards SMB traffic. This is the GUI version of smbcmp based on the
wxWidget toolkit.

%prep
%autosetup -p1

%build
# Workaround as there is no -lboost_python3
sed -i 's|curses||' setup.py
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/smbcmp/
%{python3_sitelib}/smbcmp*egg-info*

%files gui
%{_bindir}/%{name}-gui

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-19
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1-17
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1-14
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1-11
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Guenther Deschner <gdeschner@redhat.com> - 0.1-3
- Add missing dist tag

* Wed Oct 02 2019 Guenther Deschner <gdeschner@redhat.com> - 0.1-2
- Initial package
