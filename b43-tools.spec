%global git_commit 2fe10ea6690df9a068cb21cde537236bae784a14
%global git_date 20220704

Name:		b43-tools
Version:	019
Release:	%autorelease -s %{git_date}git%{sub %git_commit 0 7}
Summary:	Tools for the Broadcom 43xx series WLAN chip
# assembler — GPLv2
# debug — GPLv3
# disassembler — GPLv2
# ssb_sprom — GPLv2+
License:	GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
URL:		https://bues.ch/cgit/%{name}.git
VCS:		git:https://git.bues.ch/git/%{name}.git
Source0:	%{url}/snapshot/b43-tools-%{git_commit}.tar.xz
Patch1:		0001-b43-tools-fix-format-security-errors.patch
Patch2:		0002-Use-2to3-to-convert-to-Python3.patch
Patch3:		0003-Explicitly-use-python3.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	flex-static
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	python3-devel


%description
Tools for the Broadcom 43xx series WLAN chip.


%prep
%autosetup -p1 -n %{name}-%{git_commit}
install -p -m 0644 assembler/COPYING COPYING.assembler
install -p -m 0644 assembler/README README.assembler
install -p -m 0644 debug/COPYING COPYING.debug
install -p -m 0644 debug/README README.debug
install -p -m 0644 disassembler/COPYING COPYING.disassembler
install -p -m 0644 ssb_sprom/README README.ssb_sprom
install -p -m 0644 ssb_sprom/COPYING COPYING.ssb_sprom

# For py3_build/py3_install macros
sed 's/py_modules=/version="%{version}", py_modules=/' debug/install.py > debug/setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
CFLAGS="%{optflags}" %{make_build} -C assembler
CFLAGS="%{optflags}" %{make_build} -C disassembler
CFLAGS="%{optflags}" %{make_build} -C ssb_sprom
cd debug
%pyproject_wheel


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm.bin %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-dasm %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-fwconv %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 ssb_sprom/ssb-sprom %{buildroot}%{_bindir}
cd debug
%pyproject_install
%pyproject_save_files '*'


%files -f %{pyproject_files}
%doc README.*
%license COPYING.*
%{_bindir}/b43-asm
%{_bindir}/b43-asm.bin
%{_bindir}/b43-beautifier
%{_bindir}/b43-dasm
%{_bindir}/b43-fwdump
%{_bindir}/b43-ivaldump
%{_bindir}/brcm80211-fwconv
%{_bindir}/brcm80211-ivaldump
%{_bindir}/ssb-sprom


%changelog
%autochangelog
