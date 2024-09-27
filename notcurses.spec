Name:          notcurses
Version:       3.0.9
Release:       %autorelease
Summary:       Character graphics and TUI library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           https://nick-black.com/dankwiki/index.php/Notcurses
Source0:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/notcurses_%{version}+dfsg.1.orig.tar.xz
Source1:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/notcurses_%{version}+dfsg.1.orig.tar.xz.asc
Source2:       https://nick-black.com/dankamongmen.gpg
# Add compatibility with FFMPEG 7
Patch1:        0001-Add-compatibility-with-FFMPEG-7.0.patch

BuildRequires: gnupg2
BuildRequires: cmake
BuildRequires: doctest-devel
BuildRequires: gcc-c++
BuildRequires: gpm-devel
BuildRequires: libdeflate-devel
BuildRequires: libqrcodegen-devel
BuildRequires: libunistring-devel
BuildRequires: ffmpeg-free-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pandoc
BuildRequires: python3-cffi
BuildRequires: python3-devel
BuildRequires: python3-pypandoc
BuildRequires: pkgconfig(ncurses)
# for en_US.UTF-8 locale (we just want *some* UTF-8 one)
BuildRequires: glibc-langpack-en

%description
Notcurses facilitates the creation of modern TUI programs,
making full use of Unicode and 24-bit TrueColor. It presents
an API similar to that of Curses, and rides atop Terminfo.
This package includes C and C++ shared libraries.

%package devel
Summary:       Development files for the Notcurses library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the notcurses library.

%package static
Summary:       Static library for the Notcurses library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description static
A statically-linked version of the notcurses library.

%package utils
Summary:       Binaries from the Notcurses project
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description utils
Binaries from Notcurses, and multimedia content used thereby.

%package -n python3-%{name}
Summary:       Python wrappers for notcurses
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python wrappers and a demonstration script for the notcurses library.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%define __cmake_in_source_build 1

%generate_buildrequires
%pyproject_buildrequires

%build
# fedora requires -fPIC for static libraries
%cmake -DUSE_QRCODEGEN=on -DDFSG_BUILD=on -DUSE_GPM=on \
 -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build
cd cffi
CFLAGS="-I../include -L../" %pyproject_wheel

%check
#ctest -V %{?_smp_mflags}

%install
%cmake_install
cd cffi
%pyproject_install

%files
%doc CONTRIBUTING.md doc/CURSES.md doc/HACKING.md doc/HISTORY.md INSTALL.md doc/OTHERS.md README.md USAGE.md NEWS.md TERMINALS.md
%license COPYRIGHT
%{_libdir}/libnotcurses-core.so.%{version}
%{_libdir}/libnotcurses-core.so.3
%{_libdir}/libnotcurses-ffi.so.%{version}
%{_libdir}/libnotcurses-ffi.so.3
%{_libdir}/libnotcurses.so.%{version}
%{_libdir}/libnotcurses.so.3
%{_libdir}/libnotcurses++.so.3
%{_libdir}/libnotcurses++.so.%{version}

%files devel
%{_includedir}/notcurses/
%{_includedir}/ncpp/
%{_libdir}/libnotcurses-core.so
%{_libdir}/libnotcurses-ffi.so
%{_libdir}/libnotcurses.so
%{_libdir}/libnotcurses++.so
%{_libdir}/cmake/Notcurses
%{_libdir}/cmake/Notcurses++
%{_libdir}/cmake/NotcursesCore
%{_libdir}/pkgconfig/notcurses-core.pc
%{_libdir}/pkgconfig/notcurses-ffi.pc
%{_libdir}/pkgconfig/notcurses.pc
%{_libdir}/pkgconfig/notcurses++.pc
%{_mandir}/man3/*.3*

%files static
%{_libdir}/libnotcurses-core.a
%{_libdir}/libnotcurses.a
%{_libdir}/libnotcurses++.a

%files utils
# Don't use a wildcard, lest we pull in notcurses-*pydemo.1.
%{_bindir}/ncls
%{_bindir}/ncneofetch
%{_bindir}/ncplayer
%{_bindir}/nctetris
%{_bindir}/notcurses-demo
%{_bindir}/notcurses-info
%{_bindir}/notcurses-input
%{_bindir}/notcurses-tester
%{_bindir}/tfman
%{_mandir}/man1/ncls.1*
%{_mandir}/man1/ncneofetch.1*
%{_mandir}/man1/ncplayer.1*
%{_mandir}/man1/nctetris.1*
%{_mandir}/man1/notcurses-demo.1*
%{_mandir}/man1/notcurses-info.1*
%{_mandir}/man1/notcurses-input.1*
%{_mandir}/man1/notcurses-tester.1*
%{_mandir}/man1/tfman.1*
%{_datadir}/%{name}

%files -n python3-%{name}
%{_bindir}/notcurses-pydemo
%{_bindir}/ncdirect-pydemo
%{_mandir}/man1/notcurses-pydemo.1*
%{_mandir}/man1/ncdirect-pydemo.1*
%{python3_sitearch}/*egg-info/
%{python3_sitearch}/notcurses/
%attr(0755, -, -) %{python3_sitearch}/notcurses/notcurses.py
%{python3_sitearch}/*.so

%changelog
%autochangelog
