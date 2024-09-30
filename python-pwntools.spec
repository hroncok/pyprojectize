Name:           python-pwntools
Version:        4.12.0
Release:        3%{?dist}
Summary:        A CTF framework and exploit development library
URL:            https://github.com/Gallopsled/pwntools/
VCS:            https://github.com/Gallopsled/pwntools/

# ./LICENSE-pwntools.txt - base project of pwntools is licensed as MIT
# ./pwnlib/data/includes/LICENSE.txt
#    - header files from FreeBSD licensed with BSD 2-clause license
#    - header files from dietlibc licensed with GPLv2 or later
# ./pwnlib/data/useragents/LICENSE.txt - script `download-useragents.py licensed with BSD 2-clause license
License:        MIT AND BSD-2-Clause AND GPL-2.0-or-later

%global srcname pwntools


# Source0:      https://github.com/Gallopsled/%%{srcname}/archive/%%{srcname}-%%{version}.tar.gz
Source0:        https://github.com/Gallopsled/%{srcname}/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

# some modules for the pwn command do have python2 shabeng even though imported from python3 lib
Patch0:         https://github.com/Gallopsled/pwntools/pull/2301.patch#/%{name}-4.11.1-shabeng.patch

# Regular expressions matching binary need to be escaped in python 3.12
Patch1:         https://github.com/Gallopsled/pwntools/pull/2302.patch#/%{name}-4.11.1-python3.12.patch

# fix pwn libcdb file [something]
# libcdb failing on binaries not containing /bin/sh
Patch2:         https://github.com/Gallopsled/pwntools/pull/2307.patch#/%{name}-4.11.1-binsh_search.patch

# Unicorn package currently doesn't build on s390x platform, but it is used ony for resolving plt.
# Other functionality of pwntools should be still working
Patch3:         python-pwntools-4.11.1-weak-unicorn.patch


BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
# Waiting on pwntools to support newer sphinx shipped by Fedora.
# BuildRequires:  python%%{python3_pkgversion}-sphinx

# Build requirements for %%check
BuildRequires:  python%{python3_pkgversion}-capstone
BuildRequires:  python%{python3_pkgversion}-mako
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-paramiko
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-pyelftools
BuildRequires:  python%{python3_pkgversion}-pygments
BuildRequires:  python%{python3_pkgversion}-pyserial
BuildRequires:  python%{python3_pkgversion}-pysocks
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-sortedcontainers
BuildRequires:  python%{python3_pkgversion}-wheel

# some packages missing on EPEL
%if (0%{?fedora})
BuildRequires:  python%{python3_pkgversion}-intervaltree
BuildRequires:  python%{python3_pkgversion}-colored-traceback
BuildRequires:  python%{python3_pkgversion}-ROPGadget
BuildRequires:  python%{python3_pkgversion}-rpyc

# Omiting the unicorn on purpose for now as it creates unwanted src.rpm build dependency on s390x for some reason
# %%ifnarch s390x s390
# BuildRequires:  python%%{python3_pkgversion}-unicorn
# %%endif
%endif



# Unicorn python3 module currently not available on s390x architecture F39/F40
# limited functionality will be available
#%%if ( 0%%{?fedora} && 0%%{?fedora} >= 39 )
#%%global __requires_exclude ^python.*unicorn.*
#%%endif

# Some packages are missing in EPEL9/8
# limited functionality will be available
%if 0%{?rhel}
%global __requires_exclude python%{python3_pkgversion}-unicorn,python%{python3_pkgversion}-intervaltree,python%{python3_pkgversion}-colored-traceback,python%{python3_pkgversion}-ROPGadget,python%{python3_pkgversion}-rpyc
%endif


%description
Pwntools is a CTF framework and exploit development library. Written
in Python, it is designed for rapid prototyping and development, and
intended to make exploit writing as simple as possible.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       binutils

# As we have ignored the requirement of unicorn, lets at least recommend it
# Recommends only supported on fedora and rhel8+
# %%if (0%%{?fedora}) || ( 0%%{?rhel} && 0%%{?rhel} >= 8 )
Recommends:      python%{python3_pkgversion}-unicorn
# %%endif

%description -n python%{python3_pkgversion}-%{srcname}
Pwntools is a CTF framework and exploit development library. Written
in Python, it is designed for rapid prototyping and development, and
intended to make exploit writing as simple as possible.

# Waiting on pwntools to support newer sphinx shipped by Fedora.
# %%package doc
# Summary:        pwntools documentation
#
# %%description doc
# Documentation for pwntools.

%prep
%autosetup -n %{srcname}-%{version} -p1

#wrong permission
chmod -x docs/requirements.txt

# Generate buildrequres is failing to generate viable deps:
# - s390x due to missing (optional) python3 unicorn module
# - epel due to missing python3 modules colored-traceback, intervaltree, rpyc, unicorn
# generate_buildrequires
# pyproject_buildrequires


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
# Waiting on pwntools to support newer sphinx shipped by Fedora.
# # Generate html documentation.
# PYTHONPATH=${PWD} sphinx-build-2 docs/source html
# # Remove the sphinx-build leftovers.
# rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files pwn pwnlib

mv %{buildroot}%{_bindir}/checksec %{buildroot}%{_bindir}/checksec-pwntools

# setuptools < 60 installs pwntools-doc to sitelib
# setuptools >= 60 changes the installation location
# remove pwntools-doc from both locations
rm -rf %{buildroot}%{python3_sitelib}/pwntools-doc
rm -rf %{buildroot}%{_prefix}/pwntools-doc


%check
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"
%py3_check_import pwn pwnlib
%{__python3} -c "from pwn import *; sh=process('bash'); sh.sendline(b'echo hello | md5sum'); x=sh.read(); assert (x == b'b1946ac92492d2347c6235b4d2611184  -\n');"


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md CONTRIBUTING.md README.md TESTING.md docs/requirements.txt
%license LICENSE-pwntools.txt
%{_bindir}/asm
%{_bindir}/checksec-pwntools
%{_bindir}/common
%{_bindir}/constgrep
%{_bindir}/cyclic
%{_bindir}/debug
%{_bindir}/disablenx
%{_bindir}/disasm
%{_bindir}/elfdiff
%{_bindir}/elfpatch
%{_bindir}/errno
%{_bindir}/hex
%{_bindir}/libcdb
%{_bindir}/main
%{_bindir}/phd
%{_bindir}/pwn
%{_bindir}/pwnstrip
%{_bindir}/scramble
%{_bindir}/shellcraft
%{_bindir}/template
%{_bindir}/unhex
%{_bindir}/update
%{_bindir}/version

# Waiting on pwntools to support newer sphinx shipped by Fedora.
# %%files doc
# %%doc html
# %%license LICENSE-pwntools.txt

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.12.0-2
- Rebuilt for Python 3.13

* Sun Jun 02 2024 W. Michael Petullo <mike@flyn.org> - 4.12.0-1
- Update to 4.12.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Michal Ambroz <rebus _AT seznam.cz> - 4.11.1-5
- Weak dependency for unicorn engine

* Sat Nov 25 2023 Michal Ambroz <rebus _AT seznam.cz> - 4.11.1-4
- Fix pwn libcdb file

* Tue Nov 21 2023 Michal Ambroz <rebus _AT seznam.cz> - 4.11.1-3
- Tweak build requirements needed for the tests to run
- Prepare for the EPEL builds

* Mon Nov 20 2023 Michal Ambroz <rebus _AT seznam.cz> - 4.11.1-1
- New upstream version 4.11.1
- change license references to new SPDX format
- patch python 3.12 regex
- patch unnecessary shabeng in librery modules
- add basic check

* Mon Sep 25 2023 W. Michael Petullo <mike@flyn.org> - 4.11.0-2
- Deal with requirements.txt, which moved.

* Mon Sep 25 2023 W. Michael Petullo <mike@flyn.org> - 4.11.0-1
- New upstream version

* Sat Sep 09 2023 W. Michael Petullo <mike@flyn.org> - 4.9.0-5
- Fix BZ #2238038; rename to checksec-pwntools to remove conflict with checksec package

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.9.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Jonathan Wright <jonathan@almalinux.org> - 4.9.0-1
- Update to 4.9.0 rhbz#1902526
- Fix changelog from 4.8.0-4 missing > after email

* Fri Dec 02 2022 W. Michael Petullo <mike@flyn.org> - 4.8.0-4
- Fix BZ #2149766; backport patch that fixes compatibility with Python 3.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.8.0-2
- Rebuilt for Python 3.11

* Fri May 13 2022 W. Michael Petullo <mike@flyn.org> - 4.8.0-1
- New upstream version

* Fri Mar 04 2022 Karolina Surmao <ksurma@redhat.com> - 4.7.0-3
- Fix python-pwntools build with setuptools >= 60

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 W. Michael Petullo <mike@flyn.org> - 4.7.0-1
- New upstream version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.3.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 W. Michael Petullo <mike@flyn.org> - 4.3.0-2
- Fix BZ #1892888; something did not like setup.py's 'unicorn>=1.0.2rc1,<1.0.2rc4'

* Fri Nov 06 2020 W. Michael Petullo <mike@flyn.org> - 4.3.0-1
- New upstream version

* Thu Oct 08 2020 W. Michael Petullo <mike@flyn.org> - 4.2.1-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.9

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 4.1.0-1
- New upstream version

* Thu Dec 19 2019 W. Michael Petullo <mike@flyn.org> - 4.0.0-0.1.b0
- New upstream version
- Migrate to Python 3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 W. Michael Petullo <mike@flyn.org> - 3.12.2-1
- New upstream version
- Adjust requires.txt

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 W. Michael Petullo <mike@flyn.org> - 3.12.1-1
- New upstream version
- Drop python2-pypandoc requirement

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 W. Michael Petullo <mike@flyn.org> - 3.12.0-1
- Initial package
