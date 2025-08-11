%global __cmake_in_source_build 1
Name:		dolfin
Version:	2019.1.0.post0
%global fenics_version 2019.1
Release:        %autorelease
Summary:        FEniCS computational backend and problem solving environment

License:        LGPL-3.0-or-later
URL:            https://fenicsproject.org/
Source0:        https://bitbucket.org/fenics-project/dolfin/downloads/dolfin-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/dolfin/downloads/dolfin-%{version}.tar.gz.asc
Source2:        3083BE4C722232E28AD0828CBED06106DD22BAB3.gpg

Patch:          0001-pkgconfig-drop-irrelevant-part-from-Libs-and-Cflags.patch
Patch:          0001-Add-missing-include-for-compatiblity-with-gcc-13.patch

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  pkgconf
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  petsc-devel
BuildRequires:  sundials-devel
BuildRequires:  scotch-devel
# ptscotch-mpich-devel?
BuildRequires:  %{blaslib}-devel
BuildRequires:  hdf5-devel
# hdf5-mpich-devel?
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(fenics-ffc) >= %{fenics_version}
BuildRequires:  python3dist(fenics-ufl) >= %{fenics_version}
BuildRequires:  python3dist(fenics-dijitso) >= %{fenics_version}
# go cmake go
BuildRequires:  chrpath
BuildRequires:  make

# check-buildroot flags the python .so, but it should be fine after rpath removal.
# It seems that the original path to the library is stored in some comment.
%global __arch_install_post /usr/lib/rpm/check-buildroot || :

#BuildRequires:  mpich-devel
#BuildRequires:  openmpi-devel

%global _description %{expand:
DOLFIN is the computational backend of FEniCS and implements the
FEniCS Problem Solving Environment.}

%description %_description

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}%{?isa}
# dolfin headers include headers from other projects
Requires:       boost-devel
Requires:       eigen3-devel

%description devel
%{summary}.

%package -n python3-dolfin
Summary:        Python wrapper for the FEniCS dolfin environment
# The jit compiles and links to the dolfin library
Requires:       %{name}-devel = %{version}-%{release}%{?isa}

%description -n python3-dolfin %_description

%package doc
Summary:        Documentation and demos for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%autosetup -p1

# Let's just specify an exact version of a dependency, yay!
sed -i -r 's|pybind11==|pybind11>=|' python/setup.py

# Drop obsolete bundled crap that doesn't support FlexiBLAS
rm cmake/modules/FindBLAS.cmake

cat >>python/CMakeLists.txt <<EOF
set(CMAKE_CXX_FLAGS "\${CMAKE_CXX_FLAGS} -I$PWD")
EOF

# https://bugzilla.redhat.com/show_bug.cgi?id=1843103
sed -r -i 's/#include </#include <algorithm>\n\0/' \
  dolfin/geometry/IntersectionConstruction.cpp \
  dolfin/mesh/MeshFunction.h

sed -r -i 's|boost/detail/endian.hpp|boost/endian/arithmetic.hpp|' \
  dolfin/io/VTKFile.cpp \
  dolfin/io/VTKWriter.cpp

%generate_buildrequires
%pyproject_buildrequires

%build
# %%_mpich_load
mkdir -p build && cd build
CFLAGS="%{optflags} -Wno-unused-variable -DH5_USE_110_API" CXXFLAGS="%{optflags} -DH5_USE_110_API" %cmake .. \
  %{cmake_blas_flags} \
  -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=off \
  -Wno-dev
%make_build

# The flags defined in the pkg-config file are used at runtime.
# For some reason, the contents are not injected properly.
# https://fenicsproject.discourse.group/t/cant-define-expression-through-c-returns-fatal-error-ufc-h-no-such-file-or-directory/5472/19
# https://bugzilla.redhat.com/show_bug.cgi?id=2118536
ffc_path="$(python3 -c 'import ffc; print(ffc.get_include_path())')"
eigen_options="$(pkgconf --cflags eigen3)"
sed -r -i "s|Cflags:.*|\\0 -I${ffc_path} ${eigen_options}|" \
    dolfin.pc

# "temporary install" so the python build can find the stuff it needs
%make_install

cd ../python
export VERBOSE=1 CMAKE_PREFIX_PATH=%{buildroot}/usr/share/dolfin/cmake CMAKE_SKIP_INSTALL_RPATH=yes CMAKE_SKIP_RPATH=yes
%pyproject_wheel

%install
cd build
%make_install

cd ../python
%pyproject_install
%pyproject_save_files dolfin dolfin_utils fenics

sed -r -i '1 {s|#!/usr/bin/env python.*|#!%{__python3}|}' \
    %{buildroot}%{_bindir}/dolfin-order \
    %{buildroot}%{_bindir}/dolfin-plot \
    %{buildroot}%{_bindir}/dolfin-convert

# this file is just pointless
rm %{buildroot}/usr/share/dolfin/dolfin.conf

# there's even an option for this, except it seems to have no effect
chrpath %{buildroot}%{python3_sitearch}/dolfin/*.so
chrpath --delete %{buildroot}%{python3_sitearch}/dolfin/*.so

%check
%pyproject_check_import
ctest -V %{?_smp_mflags}

%files
%license COPYING COPYING.LESSER AUTHORS
%doc README.rst
%{_bindir}/dolfin-version
%{_bindir}/fenics-version
%{_libdir}/libdolfin.so.%{fenics_version}
%{_libdir}/libdolfin.so.%{fenics_version}.*
%dir /usr/share/dolfin
%dir /usr/share/dolfin/data
/usr/share/dolfin/data/README

%files devel
/usr/include/dolfin.h
/usr/include/dolfin/
%{_libdir}/libdolfin.so
%{_libdir}/pkgconfig/dolfin.pc
/usr/share/dolfin/cmake/

%files doc
%{_bindir}/dolfin-get-demos
/usr/share/dolfin/demo/

%files -n python3-dolfin -f %{pyproject_files}
%{_bindir}/dolfin-convert
%{_bindir}/dolfin-order
%{_bindir}/dolfin-plot

%changelog
%autochangelog
