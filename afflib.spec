Name:           afflib
Version:        3.7.20
Release:        %autorelease
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
Summary:        Library to support the Advanced Forensic Format

# Build also the python2 package
%global         with_python2    0
# Build also the python3 package
%global         with_python3    1

%global         gituser      sshock
%global         gitname      AFFLIBv3
%global         gitdate      20240324
%global         commit       95bf6cb9cf344ed6dccb8eb12bc159a17e616adb
%global         shortcommit %(c=%{commit}; echo ${c:0:7})

URL:            https://github.com/sshock/AFFLIBv3
VCS:            https://github.com/sshock/AFFLIBv3
#Source0:       %%{vcs}/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:        %{vcs}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz#/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

# GPLv2 FOSS incompatible with BSD with advertising
##BuildRequires:  fuse-devel
# GPLv2 FOSS incompatible with BSD with advertising
##BuildRequires:  readline-devel
#BuildRequires:   libedit-devel - good replacement for readline - not supported for now


%if 0%{?with_python2}
BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-Cython
%endif


%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-Cython
%endif



# Afflib format uses lzma-SDK 443
Provides: bundled(lzma) = 443



%description
AFF® is an open and extensible file format designed to store disk images and
associated metadata.
afflib is library for support of the Advanced Forensic Format (AFF).


%package -n     afftools
Summary:        Utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n afftools
The %{name}-utils package contains utilities for using %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

#====================================================================
%if 0%{?with_python2}
%package -n python2-pyaff
Summary:        Python2 binding for the AFFLIB
Group:          Development/Libraries

%description -n python2-pyaff
Python2 bindings for AFFLIB.
These bindings currently support a read-only file-like interface to AFFLIB and
basic metadata accessor functions. The binding is not currently complete.
# end with_python2
%endif



%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-pyaff
Summary:        Python3 binding for the AFFLIB
Group:          Development/Libraries



%description -n python%{python3_pkgversion}-pyaff
Python3 bindings for AFFLIB.
These bindings currently support a read-only file-like interface to AFFLIB and
basic metadata accessor functions. The binding is not currently complete.
# end with_python3
%endif




%prep
%autosetup -p1 -n AFFLIBv3-%{commit}
# prevent internal lzma to be built - testing
#rm -rf lzma443

#fix spurious permissions with lzma443
find lzma443 -type f -exec chmod 0644 {} ';'
chmod 0644 lib/base64.{h,cpp}

./bootstrap.sh

%generate_buildrequires
%pyproject_buildrequires

%build
%configure --enable-shared \
  --disable-static \
  --enable-python=no \
  --enable-s3=yes

# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

# Remove the cythonized files in order to regenerate them during build.
rm $(grep -rl '/\* Generated by Cython')

%make_build
cd pyaff
%global py_setup_args build_ext --include-dirs %{_builddir}/AFFLIBv3-%{commit}/include --library-dirs %{_builddir}/AFFLIBv3-%{commit}/lib/.libs
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%pyproject_wheel
%endif


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

cd pyaff
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%pyproject_install
%pyproject_save_files 'PyAFF*' 'pyaff*'
%endif


%ldconfig_scriptlets


%files
%doc AUTHORS BUGLIST.txt ChangeLog NEWS README
%doc doc/announce_2.2.txt
%license COPYING
%{_libdir}/*.so.*

%files -n afftools
%{_bindir}/aff*
%{_mandir}/man1/aff*.1.*

%files devel
%doc doc/crypto_design.txt doc/crypto_doc.txt
%{_includedir}/afflib/
%{_libdir}/*.so
%{_libdir}/pkgconfig/afflib.pc

%if 0%{?with_python2}
%files -n python2-pyaff
%license COPYING
%doc pyaff/README
%{python2_sitearch}/PyAFF*
%{python2_sitearch}/pyaff*
%endif


%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-pyaff -f %{pyproject_files}
%license COPYING
%doc pyaff/README
%endif



%changelog
%autochangelog
