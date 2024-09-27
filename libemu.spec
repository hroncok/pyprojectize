Name:           libemu
Version:        0.2.0
Summary:        The x86 shell-code detection and emulation
%global         baserelease     28
%if 0%{?rhel}
# Group needed for EPEL
Group:          Applications/System
%endif

# By default building without test cases as they contain realistic shell codes
# as seen by Metasploit and other exploits and some of them trigger the AV detection
# of the package.
# In case you need sctest with the original realistic test cases, please rebuild with
# rpmbuild --rebuild libemu.src.rpm --with testcases
%bcond_with	testcases



%global         gituser         DinoTools
%global         gitname         libemu
# Current version
%global         gitdate         20130410
%global         commit          ab48695b7113db692982a1839e3d6eb9e73e90a9
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})


# libemu package licensed with GPLv2+
# libdasm.c libdasm.h licensed as public domain do whatever - being bundled with libemu since at least 2006 effectively GPLv2+
# the code is removed during build and unbundled libdasm library is used instead.
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/DinoTools/libemu/
#               https://github.com/buffer/libemu
# Other information sources:
#    Original nepenthes site - is gone, but available from web archive
#               http://libemu.mwcollect.org -> https://web.archive.org/web/20090122230505/http://libemu.mwcollect.org
#               https://sourceforge.net/projects/nepenthes/files/libemu%20development/
#               http://downloads.sourceforge.net/project/nepenthes/libemu%20development/libemu/libemu-0.2.0.tar.gz
#    Original dionaea site - is gone, but available from web archive
#               http://libemu.carnivore.it/ -> https://web.archive.org/web/20150812195102/http://libemu.carnivore.it/
#    Debian libemu package
#               https://packages.debian.org/search?searchon=sourcenames&keywords=libemu
#               https://packages.debian.org/sid/libemu-dev
#    Git repositories/forks
#               https://github.com/DinoTools/libemu/
#               https://github.com/tpltnt/libemu
#               https://github.com/buffer/libemu
#               https://github.com/buffer/pylibemu
#               https://github.com/buffer/phoneyc
#               https://github.com/dzzie/SCDBG
#        Win32 Libemu shim for using Unicorn Engine as a backend
#               https://github.com/fireeye/unicorn-libemu-shim
#               https://github.com/gento/libemu
#    Paul Baecher
#               https://baecher.github.io/
#    Markus Koetter
#               https://www2.honeynet.org/2009/06/05/iteolih-is-this-worth-your-time/
#               https://www.honeynet.org/node/485
#    Articles
#               http://resources.infosecinstitute.com/shellcode-detection-emulation-libemu/
#               https://www.aldeid.com/wiki/Dionaea/Installation

# Version in Debian - 09bbeb583be41b96b9e8a5876a18ac698a77abfa
# http://http.debian.net/debian/pool/main/libe/libemu/libemu_0.2.0+git20120122.orig.tar.gz
#global         gitdate         20120122
#global         commit          09bbeb583be41b96b9e8a5876a18ac698a77abfa


# libemu currently doesn't work with python3
%bcond_with     python3
%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} >= 7 )
%bcond_with     python3
%endif

# py2 module allowed only for the EPEL7
%if ( 0%{?fedora} && 0%{?fedora} <= 30 ) || ( 0%{?rhel} && 0%{?rhel} <= 7 )
%bcond_without  python2
%else
%bcond_with     python2
%endif


# Exclude the private libemu in python sitearch dir
%global __provides_exclude_from ^(%{python2_sitearch}/.*\\.so$
%if 0%{?with_python3}
%global __provides_exclude_from ^(%{python2_sitearch}|%{python%{python3_pkgversion}_sitearch})/.*\\.so$
%endif


# This stanza is needed only for RHEL6
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitelib:  %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif



# Build source is tarball release=1 or git commit=0
%global         build_release    0

%if 0%{?build_release}  > 0
# Build from the targball release
Release:        %{baserelease}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%else
# Build from the git commit snapshot
# Not using the 0. on the beginning of release version as these are patches past version 0.2.0
# Next release should be probably 0.3.0
Release:        %{baserelease}.%{gitdate}git%{shortcommit}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# build_release
%endif


# Patches 1-5 taken from the Debian package - author David Martínez Moreno <ender@debian.org>
# and is licensed under the GPL version 2 or later

# Remove the hardcoded rpath from python binding
# https://github.com/DinoTools/libemu/issues/3
# https://github.com/DinoTools/libemu/pull/2
Patch1:         libemu-01_no_rpath_python.patch

# Allow installing to DESTDIR for the python binding
# https://github.com/DinoTools/libemu/issues/5
# https://github.com/DinoTools/libemu/pull/4
Patch2:         libemu-02_python_install_dir.patch


# Remove hardcoded rpath from configure.ac
# https://github.com/DinoTools/libemu/issues/6
# https://github.com/DinoTools/libemu/pull/7
Patch3:         libemu-03_remove_rpath_and_fix_ldflags.patch


# Comment out unused typedefs
# https://github.com/DinoTools/libemu/issues/8
# https://github.com/DinoTools/libemu/pull/9
Patch5:         libemu-05_unused_local_typedefs.patch

# Debian patches not relevant for Fedora -
# - recognizing GNU as OS not needed for Fedora build
# Patch4:       libemu-04_recognize_gnu.patch

# Fix warnings during the autreconf
# https://github.com/DinoTools/libemu/issues/10
# https://github.com/DinoTools/libemu/pull/11
Patch6:         libemu-06_autoreconf.patch

# Fix memory leak in emu_memory_free
# https://github.com/buffer/libemu/commit/9256d8dc460b15a1c05d19b2fd277939602145e1.patch
Patch7:         libemu-07_emu_memory_free.patch

# Add configure option for pkgconfigdir
# https://github.com/buffer/libemu/commit/48466d2d0d641c8b2067a366600cd2b6a52ef01b
Patch8:         libemu-08_pkgconfigdir.patch

# fix potential name collision of PAGE_SIZE in emu_memory.c by renaming to EMU_PAGE_SIZE
# https://github.com/DinoTools/libemu/issues/14
# https://github.com/DinoTools/libemu/pull/15
Patch9:         libemu-09_pagesize.patch

# fix single byte buffers causing floating point exception
# https://github.com/bwall/libemu/commit/d424e097b2a08fd0b837756192bc257344782009.patch
# https://github.com/buffer/libemu/pull/1
Patch10:        libemu-10_singlebyte.patch

# removed tautological condition
# https://github.com/tpltnt/libemu/commits/master
# https://github.com/tpltnt/libemu/commit/910f39fa0d9a18fc07ba2541c3757cc616d0ffeb.patch
Patch11:        libemu-11_tautology.patch

# fix potential null pointer dereferences
# https://github.com/DinoTools/libemu/issues/20
# https://github.com/DinoTools/libemu/pull/19
# From:
# https://github.com/tpltnt/libemu/commits/master
# https://github.com/tpltnt/libemu/commit/6c1a774e6d342912d646935432b426b4da6d3c93.patch
# https://github.com/tpltnt/libemu/commit/c3fb84dc99b01805c7f01d52527339dd58ceabbe.patch
# https://github.com/tpltnt/libemu/commit/5d88320054b642c6388a6af05cf397895b82e2d5.patch
# https://github.com/tpltnt/libemu/commit/b8c35bf2c3704fb8acc0501abc33be0a4d146c1c.patch
# https://github.com/tpltnt/libemu/commit/d41a3737ab62e9aaaabb791f8959c7cbd9d77a7a.patch
# https://github.com/tpltnt/libemu/commit/23117b2b9cff6346feb944611c05cc723820a3ba.patch
# https://github.com/tpltnt/libemu/commit/0267a6f003b5e08069d8e266826865f42f939025.patch
# https://github.com/tpltnt/libemu/commit/d15e16cee40898dd035537a47b5e97c404387b83.patch
# https://github.com/tpltnt/libemu/commit/56ff307ea36b938a11151bb22432b1ab561d71ea.patch
# https://github.com/tpltnt/libemu/commit/bdb14b443ff1b5294ecbc1ab7ba9b430b7ab2d50.patch
Patch12:        libemu-12_nullpointer.patch

# Unbundle the libdasm library and use the system-installed patch
# https://github.com/DinoTools/libemu/issues/24
# https://github.com/DinoTools/libemu/pull/25
Patch13:        libemu-13_unbundle_libdasm.patch

# Review found obsolete macros used
# https://github.com/DinoTools/libemu/issues/26
# https://github.com/DinoTools/libemu/pull/27
Patch14:        libemu-14_obsolete_m4.patch

# Parametrize python(2) binary used for building the extension
# https://github.com/DinoTools/libemu/pull/28
Patch15:        libemu-15_python2_build.patch

BuildRequires:  sed
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  git
BuildRequires:  gettext-devel
BuildRequires:  libdasm-devel

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif



%description
The libemu is a small library written in C offering basic x86 emulation and
shell-code detection using GetPC heuristics. Intended use is within network
intrusion/prevention detection and honeypots.



%package        devel
# ======================= devel package ==============================
Summary:        Development files for the libemu x86 emulator
%if 0%{?rhel} 
Group:          Development/Libraries
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if 0%{?with_python2}
%package        -n python2-libemu
# ======================= python2-libemu =============================
Summary:        Python2 binding to the libemu x86 emulator
%if 0%{?rhel} 
Group:          Development/Libraries
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python2-%{name}}

%description    -n python2-libemu
Python2 binding to the libemu x86 emulator.
#with_python2
%endif


%if 0%{?with_python3}
%package        -n python%{python3_pkgversion}-libemu
# ======================= python3-libemu =============================
Summary:        Python3 binding to the libemu x86 emulator
%if 0%{?rhel} 
Group:          Development/Libraries
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description    -n python%{python3_pkgversion}-libemu
Python3 binding to the libemu x86 emulator.

#with_python3
%endif



%prep
# ======================= prep =======================================


# Build from tarball release version
%if 0%{?build_release} > 0
%autosetup -p 1 -n %{gitname}-%{version} -S git

%else
# Build from git commit
%autosetup -p 1 -n %{gitname}-%{commit} -S git
%endif

# Unbundle the libdasm library - rest is in patch13
rm -f src/libdasm.c src/libdasm.h src/opcode_tables.h

git commit -q -a -m "unbundle libdasm"

# changes in macros in autoconf versions <= rhel6
%if ( 0%{?rhel} && 0%{?rhel} <= 6 )
sed -i 's|AC_CONFIG_MACRO_DIRS|AC_CONFIG_MACRO_DIR|;
    ' configure.ac

git commit -q -a -m "downgrade autoconf for rhel6"
%endif


%build
# ======================= build ======================================

# Create m4 directory if missing
[ -d m4 ] || mkdir m4


%if 0%{?with_testcases}
echo "Compiling with testcases"
export CFLAGS="%optflags -Wno-error=array-bounds"
%else
echo "Compiling without testcases"
export CFLAGS="%optflags -Wno-error=array-bounds -D_NO_TESTS"
%endif



autoreconf --verbose --install --force --warnings=all

# Disable suppression of the compilation warnings from the libtool
# LIBTOOLFLAGS=-no-suppress works only for compilation, but ends with error for linking
sed -i -e 's/\(^.*mode=compile $(CC).*\)\\/\1 -no-suppress\\/' src/Makefile.in


%if 0%{?with_python2} || 0%{?with_python3}
%configure --enable-python-bindings
#Build also for python3
cp -r bindings/python bindings/python3
%else
%configure
%endif


PYFLAGS=""
%if 0%{?with_python2}
PYFLAGS="PYTHON=%{__python2}"
%endif
%if 0%{?with_python3}
PYFLAGS="PYTHON=%{__python3}"
%endif
%make_build $PYFLAGS




%if 0%{?with_python2}
# re-rebuild with the Fedora hardening options
pushd bindings/python
%py2_build
popd
# with_python2
%endif

%if 0%{?with_python3}
pushd bindings/python3
%py3_build
popd
# with_python3
%endif

%install
# ======================= install ====================================
PYFLAGS=""
%if 0%{?with_python2}
PYFLAGS="PYTHON=%{__python2}"
%endif
%if 0%{?with_python3}
PYFLAGS="PYTHON=%{__python3}"
%endif
%make_install pkgconfigdir=%{_libdir}/pkgconfig $PYFLAGS


%if 0%{?with_python2}
# do the python2 install explicitly
pushd bindings/python
%py2_install
popd
%endif

%if 0%{?with_python3}
pushd bindings/python3
mkdir -p %{buildroot}/%{python3_sitearch}
%py3_install
popd
%endif

# No static building allowed for Fedora
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%if ( 0%{?rhel} && 0%{?rhel} <= 7 )
%ldconfig_scriptlets
%endif


%files
# ======================= files ======================================
%doc AUTHORS CHANGES README
%{_bindir}/sctest
%{_bindir}/scprofiler
%{_libdir}/%{name}.so.2*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3*


%if 0%{?with_python2}
%files -n python2-libemu
%{python2_sitearch}/%{name}.so
%{python2_sitearch}/%{name}-*.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-libemu
%{python3_sitearch}/%{name}.*.so
%{python3_sitearch}/%{name}-*.egg-info
# with_python3
%endif


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-28.20130410gitab48695
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-27.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-26.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-25.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-19.20130410gitab48695
- do not include the realistic shellcode tests to avoid AV trojan detections

* Fri Apr 2 2021 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-18.20130410gitab48695
- trying to rebuild for F33/F34
- do not treat the warnings about array-bounds as errors as the structs in emu_list are hitting this
- remove trailing spaces
- be more specific about the lib/python files to pack
- explicit adding BR to gcc and make

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16.20130410gitab48695
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-13.20130410gitab48695
- add back the Group tag for compatibility with EPEL

* Wed Oct 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-12.20130410gitab48695
- Remove Python 2

* Tue Oct 15 2019 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-11.20130410gitab48695
- Remove Python 2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10.20130410gitab48695.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-10.20130410gitab48695
- patch to calling python2 explicitly during build of the python binding
- fixes FTBS due to missing python binary as part of switching to python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9.20130410gitab48695
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-8.20130410gitab48695
- use ldconfig_scriptlets
- fix release version number in the changelog
- fix obsolete m4 macros
- Exclude the private libemu in python sitearch dir
- show all warnings to autoreconf
- use autosetup+git for troubleshooting the patches

* Mon Apr 02 2018 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-0.7.20130410gitab48695
- unbundle the libdasm library and use system-installed one
- disable the python3 build for now

* Mon Mar 26 2018 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-0.6.20130410gitab48695
- fix ldconfig requirement to align with the glibc provide

* Fri Mar 23 2018 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-0.5.20130410gitab48695
- added missing dependency to python3-devel
- use the python{python3_pkgversion}-devel/setuptools to enable EPEL7 build

* Thu Mar 22 2018 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-0.4.20130410gitab48695
- spec clean-up
- prepare for the python3 support
- include patches from buffer github repository

* Sun Mar 04 2018 Michal Ambroz <rebus at, seznam.cz> - 0.2.0-0.1.20130410gitab48695
- build for Fedora 27

