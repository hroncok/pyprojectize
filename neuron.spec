# This is a serial build of NEURON
%global _description %{expand:
NEURON is a simulation environment for modeling individual neurons and networks
of neurons. It provides tools for conveniently building, managing, and using
models in a way that is numerically sound and computationally efficient. It is
particularly well-suited to problems that are closely linked to experimental
data, especially those that involve cells with complex anatomical and
biophysical properties.

Please install the %{name}-devel package to compile nmodl files, and please
install the MPI specific sub-packages for MPICH and OpenMPI builds.
}

%global tarname nrn

# fails somehow, disabled by default
%bcond_with metis

# Music support
%bcond_with music

%bcond_without mpich
%bcond_without openmpi

Name:       neuron
Version:    8.2.2
Release:    %autorelease
Summary:    A flexible and powerful simulator of neurons and networks

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        http://www.neuron.yale.edu/neuron/
Source0:    https://github.com/neuronsimulator/%{tarname}/archive/%{version}/%{name}-%{version}.tar.gz

# they bundle HPC coding conventions as a git submodule
%global conv_git_commit  5d4bcd2d410e67bdc1d23d3280c08ee5c9df943b
%global conv_short_commit %(c=%{conv_git_commit}; echo ${c:0:7})
Source1:    https://github.com/BlueBrain/hpc-coding-conventions/archive/%{conv_git_commit}/hpc-coding-conventions-%{conv_short_commit}.tar.gz

%global rxd_tests_commit 2a08564a45fac78f259d23203d737db924c224c8
%global rxd_short_commit %(c=%{rxd_tests_commit}; echo ${c:0:7})
Source2:    https://github.com/neuronsimulator/rxdtestdata/archive/%{rxd_tests_commit}/rxdtestdata-%{rxd_short_commit}.tar.gz


Patch0:     0001-Unbundle-Random123.patch
# libstdc++ bundled is from 1988: seems heavily modified. Headers from there
# are not present in the current version
# https://github.com/neuronsimulator/nrn/issues/145

# Use system copy of Catch
Patch1:     0002-Unbundle-catch.patch
# We install the python bits ourselves
Patch2:     0003-Disable-python-build-and-install.patch
# Set soversions for all shared objects
Patch3:     0004-Set-soversions-for-libs.patch
# Set the right path for libdir
# Upstreamable
Patch4:     0005-Correct-librxdmath-path-for-64bit.patch
# stop build scripts from generating version during build
Patch5:     0006-Do-not-generate-version-info-at-buildtime.patch
# Remove rpaths
Patch6:     0007-Remove-rpaths.patch
# do not download data git submodule
Patch7:     0008-Dont-download-testdata-submodule.patch
# place help file in correct location
Patch8:     0009-Add-help-file-as-package-data.patch
# tries to create /usr/x86_64 etc dirs
Patch9:     0010-Remove-unneeded-symlinks.patch
# remove build time flags from the nrnmech makefile---it should not use these
Patch10:    0011-Strip-build-flags-from-nrnmech_makefile.patch

# Random123 does not build on these, so neither can NEURON
# https://github.com/neuronsimulator/nrn/issues/114
ExcludeArch:    mips64r2 mips32r2
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bison-devel
BuildRequires:  cmake
BuildRequires:  catch-devel
# Needs to be packaged separately
# BuildRequires:  coreneuron-devel
BuildRequires:  flex
BuildRequires:  (flex-devel or libfl-devel)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
# the cmake build requires iv with cmake too
BuildRequires:  iv-devel >= 0.1
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libtool
%if %{with metis}
BuildRequires:  metis-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  Random123-devel

# Bundles sundials. WIP
# https://github.com/neuronsimulator/nrn/issues/113
# BuildRequires:  sundials-devel
Provides: bundled(sundials) = 2.0.1

%description %_description

%package devel
Summary:    Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires:  ncurses-devel
Requires:  readline-devel
Requires:  gcc-c++
Requires:  libtool
Requires:  libX11-devel
Requires:  libXext-devel
Requires:  iv-devel

%description devel
Headers and development shared libraries for the %{name} package

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

%description doc
Documentation for %{name}

%package -n python3-%{name}
Summary:   Python3 interface to %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

%description -n python3-%{name} %_description

%if %{with mpich}
%package mpich
Summary:   %{name} built with MPICH support
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-mpich

Requires:       mpich
Requires:       python3-mpi4py-mpich


%description mpich %_description

%package mpich-devel
Summary:    Development files for %{name}
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
Headers and development shared libraries for the %{name} package

%package -n python3-%{name}-mpich
Summary:    Python3 interface to %{name}-mpich
Requires:  %{name}-mpich%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-mpich %_description
%endif

%if %{with openmpi}
%package openmpi
Summary:   %{name} built with OpenMPI support
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-openmpi

Requires:       openmpi
Requires:       python3-mpi4py-openmpi


%description openmpi %_description

%package openmpi-devel
Summary:    Development files for %{name}
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
Headers and development shared libraries for the %{name} package

%package -n python3-%{name}-openmpi
Summary:    Python3 interface to %{name}-openmpi
Requires:  %{name}-openmpi%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-openmpi %_description
%endif

%prep
%autosetup -n %{tarname}-%{version} -S git

# Remove executable perms from source files
find src -type f -executable ! -name '*.sh' -exec chmod -x {} +

# remove shebangs: check again each release
pushd share/lib/auditscripts/
for f in *
do
sed -i -e "/^#!\/bin\/sh.*/ d" $f
done
popd

# Remove bundled Random123
rm -rf src/Random123
rm -rf src/readline

# extract coding convention tar
# can probably use setup macro etc.
pushd external/coding-conventions
cp %SOURCE1 .
tar -xvf hpc-coding-conventions*.tar.gz --strip-components=1
rm -f hpc-coding-conventions*.tar.gz
popd

# extract rxdtestdata tar
pushd test/rxd/testdata
cp %SOURCE2 .
tar -xvf rxdtestdata*.tar.gz --strip-components=1
rm -f rxdtestdata*.tar.gz
popd

# Create version file ourselves
# To create this, we run the git2version.sh script in a checked out copy of neuron
export TIMESTAMP=$(date +%Y-%m-%d)
cat > src/nrnoc/nrnversion.h << EOF
#define GIT_DATE "$TIMESTAMP"
#define GIT_BRANCH "master"
#define GIT_CHANGESET "f0ca745418e942ad4763bdc47459c409f0b11512"
#define GIT_DESCRIBE "8.0.2 (Fedora %{fedora})"
EOF

# Stop system from using hard coded flags
sed -i '/CompilerFlagsHelpers/ d' cmake/ReleaseDebugAutoFlags.cmake

# Setting SETUPTOOLS_USE_DISTUTILS=stdlib does not work on Python 3.12
# https://github.com/neuronsimulator/nrn/issues/2263
#
# We change each occurrence to SETUPTOOLS_USE_DISTUTILS=local (the default).
# The find-then-modify pattern keeps us from discarding mtimes on any sources
# that do not need modification.
find . -type f -name 'CMakeLists.txt' -exec gawk \
    '/export SETUPTOOLS_USE_DISTUTILS=stdlib/ { print FILENAME; nextfile }' \
    '{}' '+' |
  xargs -r -t sed -r -i 's/(export SETUPTOOLS_USE_DISTUTILS=)stdlib/\1local/'

%build
# Not yet to be used
# export SUNDIALS_SYSTEM_INSTALL="yes"
%global do_build %{expand:
echo
echo "*** BUILDING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
%set_build_flags
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
        -DNRN_ENABLE_SHARED=ON \\\
        -DNRN_ENABLE_INTERVIEWS=ON \\\
        -DNRN_ENABLE_PYTHON=ON \\\
        -DNRN_ENABLE_PYTHON_DYNAMIC=OFF \\\
        -DNRN_ENABLE_THREADS=ON \\\
        -DNRN_ENABLE_MEMACS=ON \\\
        -DNRN_ENABLE_RX3D=ON \\\
        -DNRN_ENABLE_CORENEURON=OFF \\\
        -DNRN_ENABLE_TESTS=OFF \\\
        -DNRN_ENABLE_REL_RPATH=OFF \\\
        -DNRN_ENABLE_MODULE_INSTALL=ON \\\
        -DNRN_ENABLE_INTERNAL_READLINE=OFF \\\
        -DNRN_ENABLE_MPI=$MPI_YES \\\
        -DNEURON_CMAKE_FORMAT:BOOL=OFF \\\
        -DMPI_INCLUDE_PATH=$MPI_INCLUDE \\\
        -DMPI_LIBRARY=$MPI_LIBFILE \\\
%if "%{_lib}" == "lib64" \
        -DLIB_SUFFIX=64 -B $MY_CMAKE_BUILDDIR && \
%else                      \
        -DLIB_SUFFIX="" -B $MY_CMAKE_BUILDDIR && \
%endif
%__cmake --build $MY_CMAKE_BUILDDIR %{_smp_mflags} \

%if %{with music}
pushd $MY_CMAKE_BUILDDIR/src/neuronmusic
%__cmake --build %{_smp_mflags}
%{py3_build}
popd
%endif
}


# Serial version
export MPI_COMPILER=serial
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_INCLUDE=%{_includedir}
export MPI_LIB="%{_libdir}"
export MPI_LIBFILE=""
export MPI_YES=OFF
# Python 3
export MPI_COMPILE_TYPE=""
export MPI_SITEARCH="%{python3_sitearch}"
export MY_CMAKE_BUILDDIR="%_vpath_builddir"
%{do_build}

# MPICH
%if %{with mpich}
%{_mpich_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-mpich"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-mpich"
export MPI_LIBFILE="$MPI_LIB/libmpi.so"
%{do_build}
%{_mpich_unload}
%endif

# OpenMPI
%if %{with openmpi}
%{_openmpi_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-openmpi"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-openmpi"
export MPI_LIBFILE="$MPI_LIB/libmpi.so"
%{do_build}
%{_openmpi_unload}
%endif

%install
# Install everything

%global do_install %{expand:
echo
echo "*** INSTALLING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
DESTDIR=%{buildroot} %__cmake --install $MY_CMAKE_BUILDDIR

%if %{with music}
pushd $MY_CMAKE_BUILDDIR/src/neuronmusic
%{py3_install}
popd
%endif

# Python bits from the post install hook
# It requires the libraries before to be installed, not just built, so it must
# be done here. The only alternative is a different package that requires this,
# but this is simpler
RPM_LD_FLAGS="%{?__global_ldflags} -L$RPM_BUILD_ROOT/$MPI_LIB"
pushd $MY_CMAKE_BUILDDIR/src/nrnpython/
%{py3_build}
%{py3_install "--install-lib" "$MPI_PYTHON3_SITEARCH"}
popd

# set up second symlink for shared objects
pushd $RPM_BUILD_ROOT/$MPI_LIB/
    ln -sv ./libnrniv.so.0.0.0 libnrniv.so.0
    ln -sv ./librxdmath.so.0.0.0 librxdmath.so.0
popd
}

%global do_post_install_tweaks %{expand:
# Remove installed libfiles
rm -rfv $RPM_BUILD_ROOT/$MPI_HOME/lib/python/neuron/
# Post install clean up: remove stray object files
# Must be done at end, otherwise it deletes object files required for other builds
find . $RPM_BUILD_ROOT/$MPI_LIB/ -name "*.o" -exec rm -f '{}' \\;
# Remove libtool archives
find . $RPM_BUILD_ROOT/$MPI_LIB/ -name "*.la" -exec rm -f '{}' \\;
# Remove installed copy of libtool
# Remove iv header provided by iv package
rm -rf $RPM_BUILD_ROOT/$MPI_HOME/include/ivstream.h
# Delete installed libtool
rm -fv $RPM_BUILD_ROOT/$MPI_HOME/share/%{tarname}/libtool

# remove package note flag from nrnmech_makefile
pushd $RPM_BUILD_ROOT/$MPI_BIN/
    sed -i "s|-Wl,-dT,.*\.ld||" nrnmech_makefile
popd
# Only needed for MPI builds
if [ x"$MPI_SUFFIX" != "x" ]
then
# Do not install demo files for MPI packages
rm -rf $RPM_BUILD_ROOT/$MPI_HOME/share/%{tarname}/demo
# Renaming MPI bits
pushd $RPM_BUILD_ROOT/$MPI_BIN/
# Rename file references to use MPI_SUFFIX before renaming them
sed -i "s/nrniv\"/nrniv$MPI_SUFFIX\"/g" nrngui
sed -i -e "s/nrniv\"/nrniv$MPI_SUFFIX\"/g" -e "s/nrnmech_makefile/nrnmech_makefile$MPI_SUFFIX/g" -e "s/nocmodl/nocmodl$MPI_SUFFIX/g" nrnivmodl
sed -i -e "s/nocmodl/nocmodl$MPI_SUFFIX/g" nrnmech_makefile
sed -i -e "s/nocmodl/nocmodl$MPI_SUFFIX/g" mkthreadsafe

# Rename files to include $MPI_SUFFIX
for f in modlunit neurondemo nrngui nrniv sortspike mkthreadsafe nocmodl nrnivmodl nrnmech_makefile
do
    mv -v "$f"{,$MPI_SUFFIX}
done
mv -v nrnpyenv{,$MPI_SUFFIX}.sh
mv -v set_nrnpyenv{,$MPI_SUFFIX}.sh
popd
fi
}

# Serial
export MPI_LIB="%{_libdir}"
export MPI_COMPILE_TYPE=""
export MPI_PYTHON3_SITEARCH=%{python3_sitearch}
export MY_CMAKE_BUILDDIR="%_vpath_builddir"
export MPI_HOME="%{_prefix}"
export MPI_BIN="%{_bindir}"
export MPI_SUFFIX=""
%do_install
%do_post_install_tweaks
# Remove duplicate files. These are installed in the correct python locations already
# rm -rf $RPM_BUILD_ROOT/%%{_datadir}/%%{tarname}/lib/python/%%{name}



# mpich
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-mpich"
%do_install
%do_post_install_tweaks
%{_mpich_unload}
%endif

# OpenMPI
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
export MY_CMAKE_BUILDDIR="%_vpath_builddir""-openmpi"
%do_install
%do_post_install_tweaks
%{_openmpi_unload}
%endif

# The makefiles do not have shebangs
%files
%license Copyright
%{_bindir}/modlunit
%{_bindir}/neurondemo
%{_bindir}/nrngui
%{_bindir}/nrniv
%{_bindir}/sortspike
# Not needed but I'll include them for completeness anyway
%{_bindir}/nrnpyenv.sh
%{_bindir}/set_nrnpyenv.sh
# Libs
%{_libdir}/libnrniv.so.0.0.0
%{_libdir}/libnrniv.so.0
%{_libdir}/librxdmath.so.0.0.0
%{_libdir}/librxdmath.so.0
# other hoc files and data
%dir %{_datadir}/%{tarname}
%{_datadir}/%{tarname}/lib

# Python bits
%files -n python3-%{name}
# The libraries are here
%{python3_sitearch}/%{name}
# Egg info
%{python3_sitearch}/NEURON-*-py%{python3_version}.egg-info

%files devel
%license Copyright
%doc README.md
%{_bindir}/mkthreadsafe
%{_bindir}/nocmodl
%{_bindir}/nrnivmodl
%{_bindir}/nrnmech_makefile
# Headers
%{_includedir}/*.h
%{_includedir}/nrncvode/
# Shared objects
%{_libdir}/libnrniv.so
%{_libdir}/librxdmath.so
# required by neuron
# https://github.com/neuronsimulator/nrn/issues/719#issuecomment-677501890
%{_datadir}/%{tarname}/nrnmain.cpp

%files doc
%license Copyright
%{_datadir}/%{tarname}/demo

%if %{with mpich}
%files mpich
%license Copyright
%{_libdir}/mpich/bin/modlunit_mpich
%{_libdir}/mpich/bin/neurondemo_mpich
%{_libdir}/mpich/bin/nrngui_mpich
%{_libdir}/mpich/bin/nrniv_mpich
%{_libdir}/mpich/bin/sortspike_mpich
# Not needed but I'll include them for completeness anyway
%{_libdir}/mpich/bin/nrnpyenv_mpich.sh
%{_libdir}/mpich/bin/set_nrnpyenv_mpich.sh
# Libs
%{_libdir}/mpich/lib/libnrniv.so.0.0.0
%{_libdir}/mpich/lib/libnrniv.so.0
%{_libdir}/mpich/lib/librxdmath.so.0.0.0
%{_libdir}/mpich/lib/librxdmath.so.0
#
%dir %{_libdir}/mpich/share/%{tarname}
%{_libdir}/mpich/share/%{tarname}/lib

# Python bits
%files -n python3-%{name}-mpich
# The libraries are here
%{python3_sitearch}/mpich/%{name}
# Egg info
%{python3_sitearch}/mpich/NEURON-*-py%{python3_version}.egg-info

%files mpich-devel
%license Copyright
%doc README.md
%{_libdir}/mpich/bin/mkthreadsafe_mpich
%{_libdir}/mpich/bin/nocmodl_mpich
%{_libdir}/mpich/bin/nrnivmodl_mpich
%{_libdir}/mpich/bin/nrnmech_makefile_mpich
# Headers
%{_libdir}/mpich/include/*.h
%{_libdir}/mpich/include/nrncvode/
# Shared objects
%{_libdir}/mpich/lib/libnrniv.so
%{_libdir}/mpich/lib/librxdmath.so
# required by neuron
# https://github.com/neuronsimulator/nrn/issues/719#issuecomment-677501890
%{_libdir}/mpich/share/%{tarname}/nrnmain.cpp
%endif

%if %{with openmpi}
%files openmpi
%license Copyright
%{_libdir}/openmpi/bin/modlunit_openmpi
%{_libdir}/openmpi/bin/neurondemo_openmpi
%{_libdir}/openmpi/bin/nrngui_openmpi
%{_libdir}/openmpi/bin/nrniv_openmpi
%{_libdir}/openmpi/bin/sortspike_openmpi
# Not needed but I'll include them for completeness anyway
%{_libdir}/openmpi/bin/nrnpyenv_openmpi.sh
%{_libdir}/openmpi/bin/set_nrnpyenv_openmpi.sh
# Libs
%{_libdir}/openmpi/lib/libnrniv.so.0.0.0
%{_libdir}/openmpi/lib/libnrniv.so.0
%{_libdir}/openmpi/lib/librxdmath.so.0.0.0
%{_libdir}/openmpi/lib/librxdmath.so.0
#
%dir %{_libdir}/openmpi/share/%{tarname}
%{_libdir}/openmpi/share/%{tarname}/lib

# Python bits
%files -n python3-%{name}-openmpi
# The libraries are here
%{python3_sitearch}/openmpi/%{name}
# Egg info
%{python3_sitearch}/openmpi/NEURON-*-py%{python3_version}.egg-info

%files openmpi-devel
%license Copyright
%doc README.md
%{_libdir}/openmpi/bin/mkthreadsafe_openmpi
%{_libdir}/openmpi/bin/nocmodl_openmpi
%{_libdir}/openmpi/bin/nrnivmodl_openmpi
%{_libdir}/openmpi/bin/nrnmech_makefile_openmpi
# Headers
%{_libdir}/openmpi/include/*.h
%{_libdir}/openmpi/include/nrncvode/
# Shared objects
%{_libdir}/openmpi/lib/libnrniv.so
%{_libdir}/openmpi/lib/librxdmath.so
# required by neuron
# https://github.com/neuronsimulator/nrn/issues/719#issuecomment-677501890
%{_libdir}/openmpi/share/%{tarname}/nrnmain.cpp
%endif

%changelog
%autochangelog
