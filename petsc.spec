# Broken package_note links in rules and variables files
# Disabling this functionality
%undefine _package_note_file

# Disable LTO
# undefined-non-weak-symbol libpetsc.so.3.*_glibcxx_assert_fail
%undefine _ld_as_needed
%global _lto_cflags %{nil}

# Testing libpetsc ?
%bcond_without check
#

# Python binding and its testing
%bcond_without python
# Python tests need Cython
# Python tests need epydoc (no longer available)
%bcond_with pycheck
%global pymodule_name petsc4py
%global pymodule_version %{version}
#

## Debug builds ?
%bcond_with debug
#

## Fix Epoch in EPEL9
%if 0%{?el9}
%global epoch 1
%else
%global epoch 0
%endif

%bcond_without mpich
%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%bcond_without arch64
%else
%bcond_with arch64
%endif

%bcond_without blas
%if %{with arch64}
%bcond_without blas64
%endif

%global blaslib flexiblas
%global blasvar %{nil}

#
## PETSC looks incompatible with serial MUMPS
%bcond_without mumps_serial
#
## Sundials needs mpi ?
%bcond_with sundials_serial
#
%bcond_without superlu
#

## Suitesparse
## This version of PETSc needs the 5.6.0 at least
%bcond_with suitesparse
%bcond_with suitesparse64
#

## SuperLUDIST needs parmetis
%bcond_without superludist >= 6.3.0
%bcond_with cgns
%bcond_without hdf5
%bcond_with superlumt
#

## Tetgen
%bcond_with tetgen
#

## Metis
%bcond_without metis
%bcond_without metis64
#

# 'scalapack' is required by 'MUMPS'
%if %{with openmpi}
%bcond_without mpi
# PETSC-3.* is incompatible with Sundials 3+
%bcond_with sundials
%bcond_without scalapack
%bcond_without mumps
%bcond_without ptscotch
%bcond_without hypre
%endif

%if %{with mpich}
%bcond_without mpi
# PETSC-3.* is incompatible with Sundials 3+
%bcond_with sundials
%bcond_without scalapack
%bcond_without mumps
%bcond_without ptscotch
%bcond_without hypre
%endif

%global petsc_build_options \\\
 %if %{with debug} \
 CFLAGS="-O0 -g -Wl,-z,now -fPIC" CXXFLAGS="-O0 -g -Wl,-z,now -fPIC" FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules" COPTFLAGS="-O0 -g -Wl,-z,now" \\\
  CXXOPTFLAGS="-O0 -g -Wl,-z,now" FOPTFLAGS="-O0 -g -Wl,-z,now -I%{_libdir}/gfortran/modules" LDFLAGS="$LDFLAGS -fPIC" \\\
  FCFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules" \\\
 %else \
 CFLAGS="$CFLAGS -O3 -fPIC" CXXFLAGS="$CXXFLAGS -O3 -fPIC" FFLAGS="$FFLAGS -O3 -fPIC" LDFLAGS="$LDFLAGS -fPIC" \\\
  COPTFLAGS="$CFLAGS -O3" CXXOPTFLAGS="$CXXFLAGS -O3" FOPTFLAGS="$FFLAGS -O3" \\\
  FCFLAGS="$FFLAGS -O3 -fPIC" \\\
 %endif \
 --CC_LINKER_FLAGS="$LDFLAGS" \\\
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran" \\\
 --with-default-arch=0 --with-make=1 \\\
 --with-cmake-exec=%{_bindir}/cmake --with-ctest-exec=%{_bindir}/ctest \\\
 --with-single-library=1 \\\
 --with-precision=double \\\
 --with-petsc-arch=%{_arch} \\\
 --with-clanguage=C \\\
 --with-shared-libraries=1 \\\
 --with-fortran-interfaces=1 \\\
 --with-windows-graphics=0 \\\
 --CC=gcc \\\
 --FC=gfortran \\\
 --CXX=g++ \\\
 --with-shared-ld=ld \\\
 --with-pic=1 \\\
 --with-clib-autodetect=0 \\\
 --with-fortranlib-autodetect=0 \\\
 --with-threadsafety=0 --with-log=1 \\\
 --with-mkl_sparse=0 \\\
 --with-mkl_sparse_optimize=0 \\\
 --with-mkl_cpardiso=0 \\\
 --with-mkl_pardiso=0 \\\
 --with-python=0 \\\
 --with-cxxlib-autodetect=1 \\\
 %if %{with debug} \
  --with-debugging=1 \\\
 %else \
  --with-debugging=0 \\\
 %endif \
 %if %{with mumps_serial} \
  --with-mumps-serial=1 \\\
 %endif \
  --with-mpi=0 \\\
 %if %{with hdf5} \
  --with-hdf5=1 \\\
  --with-hdf5-include= \\\
  --with-hdf5-lib="-lhdf5 -lhdf5_hl" \\\
 %endif \
 %if %{with cgns} \
  --with-cgns=0 \\\
 %endif \
  --with-x=1 \\\
  --with-openmp=0 \\\
  --with-hwloc=0 \\\
  --with-ssl=0 \\\
 %if %{with sundials_serial} \
  --with-sundials=1 \\\
  --with-sundials-include=%{_includedir} \\\
  --with-sundials-lib="-lsundials_nvecserial -lsundials_cvode" \\\
 %endif \
 %ifarch %{valgrind_arches} \
  --with-valgrind=1 \\\
 %endif \
  --with-pthread=1

%global petsc_mpibuild_options \\\
 %if %{with debug} \
 CFLAGS="-O0 -g -Wl,-z,now -fPIC" CXXFLAGS="-O0 -g -Wl,-z,now -fPIC" FFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}" COPTFLAGS="-O0 -g -Wl,-z,now" \\\
  CXXOPTFLAGS="-O0 -g -Wl,-z,now" FOPTFLAGS="-O0 -g -Wl,-z,now -I${MPI_FORTRAN_MOD_DIR}" LDFLAGS="$LDFLAGS -fPIC" \\\
  FCFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}" \\\
 %else \
 CFLAGS="$CFLAGS -O3 -fPIC" CXXFLAGS="$CXXFLAGS -O3 -fPIC" FFLAGS="$FFLAGS -O3 -fPIC" LDFLAGS="$LDFLAGS -fPIC" \\\
  COPTFLAGS="$CFLAGS -O3" CXXOPTFLAGS="$CXXFLAGS -O3" FOPTFLAGS="$FFLAGS -O3" \\\
  FCFLAGS="$FFLAGS -O3 -fPIC" \\\
 %endif \
  --CC_LINKER_FLAGS="$LDFLAGS" \\\
  --with-default-arch=0 --with-make=1 \\\
  --with-cmake-exec=%{_bindir}/cmake --with-ctest-exec=%{_bindir}/ctest \\\
  --with-single-library=1 \\\
  --with-precision=double \\\
  --with-petsc-arch=%{_arch} \\\
  --with-clanguage=C \\\
  --with-shared-libraries=1 \\\
  --with-fortran-interfaces=1 \\\
  --with-windows-graphics=0 \\\
  --with-cc=${MPI_BIN}/mpicc \\\
  --with-cxx=${MPI_BIN}/mpicxx \\\
  --with-fc=${MPI_BIN}/mpif90 \\\
  --with-shared-ld=ld \\\
  --with-pic=1 \\\
  --with-clib-autodetect=0 \\\
  --with-fortranlib-autodetect=0 \\\
  --with-mkl_sparse=0 \\\
  --with-mkl_sparse_optimize=0 \\\
  --with-mkl_cpardiso=0 \\\
  --with-mkl_pardiso=0 \\\
 %if %{with python} \
  --with-python=1 \\\
  --with-python-exec=%{__python3} \\\
  --with-petsc4py=1 \\\
  --with-petsc4py-test-np="`/usr/bin/getconf _NPROCESSORS_ONLN`" \\\
 %endif \
  --with-cxxlib-autodetect=1 \\\
  --with-threadsafety=0 --with-log=1 \\\
 %if %{with debug} \
  --with-debugging=1 \\\
    --with-mpiexec="${MPI_BIN}/mpiexec -n `/usr/bin/getconf _NPROCESSORS_ONLN` --mca btl_base_warn_component_unused 0 --mca orte_base_help_aggregate 0" \\\
 %else \
  --with-debugging=0 \\\
    --with-mpiexec="${MPI_BIN}/mpiexec -n `/usr/bin/getconf _NPROCESSORS_ONLN` --mca btl_base_warn_component_unused 0" \\\
 %endif \
 %if %{with scalapack} \
  --with-scalapack=1 \\\
  --with-scalapack-lib="-L$MPI_LIB -lscalapack" \\\
  --with-scalapck-include="" \\\
 %endif \
 %if %{with mpi} \
  --with-mpi=1 \\\
 %endif \
 %if %{with cgns} \
  --with-cgns=1 \\\
  --with-cgns-include=%{_includedir} \\\
  --with-cgns-lib=-lcgns \\\
 %endif \
 %if %{with hdf5} \
  --with-hdf5=1 \\\
  --with-hdf5-include= \\\
  --with-hdf5-lib="-L$MPI_LIB -lhdf5 -lhdf5_hl" \\\
 %endif \
 %if %{with ptscotch} \
  --with-ptscotch=1 \\\
  %if 0%{?rhel} \
  --with-ptscotch-include=$MPI_INCLUDE \\\
  %else \
  --with-ptscotch-include=$MPI_INCLUDE/scotch \\\
  %endif \
  --with-ptscotch-lib="-L$MPI_LIB -lptscotch -lscotch -lptscotcherr -lscotcherr" \\\
 %endif \
 %if %{with mumps} \
  --with-mumps=1 \\\
 %endif \
 %if %{with sundials} \
  --with-sundials=1 \\\
  --with-sundials-include=$MPI_INCLUDE \\\
  --with-sundials-lib=-lsundials_nvecparallel \\\
 %endif \
 %if %{with superludist} \
  --with-superlu_dist=1 \\\
  --with-superlu_dist-include=$MPI_INCLUDE/superlu_dist \\\
  --with-superlu_dist-lib=-lsuperlu_dist \\\
 %endif \
  --with-x=1 \\\
  --with-openmp=0 \\\
  --with-hwloc=0 \\\
  --with-ssl=0 \\\
 %if %{with hypre} \
  --with-hypre=1 \\\
  --with-hypre-include=$MPI_INCLUDE/hypre \\\
  --with-hypre-lib="-L$MPI_LIB -lHYPRE" \\\
 %endif \
 %if %{with fftw} \
  --with-fftw=1 \\\
  --with-fftw-include= \\\
  --with-fftw-lib="-L$MPI_LIB -lfftw3_mpi -lfftw3" \\\
 %endif \
 %ifarch %{valgrind_arches} \
  --with-valgrind=1 \\\
 %endif \
  --with-pthread=1
  
%global mpichversion %(rpm -qi mpich | awk -F': ' '/Version/ {print $2}')
%global openmpiversion %(rpm -qi openmpi | awk -F': ' '/Version/ {print $2}')
%global majorver 3
%global releasever 3.20

Name:    petsc
Summary: Portable Extensible Toolkit for Scientific Computation
Version: %{releasever}.6
Release: %autorelease
License: BSD-2-Clause
URL:     https://petsc.org/
Source0: https://web.cels.anl.gov/projects/%{name}/download/release-snapshots/%{name}-with-docs-%{version}.tar.gz

# These files have been generated by Cython-3.0.6
# PETSC-3.20+ needs Cython-3.0.0, these files are used in EPEL9
Source1: %{name}-3.20-PETSc_cython3.0.6.c
Source2: %{name}-3.20-PETSc_cython3.0.6.h
Source3: %{name}-3.20-PETSc_api_cython3.0.6.h

## Remove rpath flags
Patch0:  %{name}-3.11-no-rpath.patch

## Rename library name for 64-bit integer package
Patch1:  %{name}-lib64.patch
Patch3:  %{name}-3.19.4-fix_mumps_includes.patch
Patch4:  %{name}-3.19.4-fix_metis64.patch
Patch6:  %{name}-3.14.1-fix_pkgconfig_file.patch
Patch7:  %{name}-3.17.0-avoid_fake_MKL_detection.patch

Patch100: no-xdrlib.patch
Patch101: no-parse_makefile.patch

%if %{with superlu}
BuildRequires: SuperLU-devel >= 5.2.0
%endif
%if %{with superlumt}
BuildRequires: SuperLUMT-devel
%endif
%if %{with mumps_serial}
BuildRequires: MUMPS-devel
%endif
%if %{with metis}
BuildRequires: metis-devel >= 5.1.0
%endif
%if %{with suitesparse}
BuildRequires: suitesparse-devel >= 5.6.0
%endif
%if %{with blas}
BuildRequires: %{blaslib}-devel
%endif
BuildRequires: chrpath
BuildRequires: gcc, gcc-c++, cmake
BuildRequires: gcc-gfortran
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: python3-devel
BuildRequires: pcre2-devel
%if %{with hdf5}
BuildRequires: hdf5-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-devel
%endif
BuildRequires: tcsh
%if %{with tetgen}
BuildRequires: tetgen-devel
%endif
BuildRequires: xorg-x11-server-Xvfb
%ifarch %{valgrind_arches}
BuildRequires: valgrind-devel
%endif

%description
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package devel
Summary:    Portable Extensible Toolkit for Scientific Computation (developer files)
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
%description devel
Portable Extensible Toolkit for Scientific Computation (developer files).

%package doc
Summary:    Portable Extensible Toolkit for Scientific Computation (documentation files)
BuildRequires: python3-sphinx
BuildArch:  noarch
%description doc
Portable Extensible Toolkit for Scientific Computation.
PDF and HTML documentation files.

%if %{with arch64}
%package -n petsc64
Summary: Portable Extensible Toolkit for Scientific Computation (64bit INTEGER)
%if %{with metis64}
BuildRequires: metis64-devel >= 5.1.0
%endif

%description -n petsc64
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations (64bit INTEGER).

%package -n petsc64-devel
Requires:   %{name}64%{?_isa} = %{version}-%{release}
Requires:   gcc-gfortran%{?_isa}
Summary:    Portable Extensible Toolkit for Scientific Computation (64bit INTEGER)

%description -n petsc64-devel
Portable Extensible Toolkit for Scientific Computation (developer files)
(64bit INTEGER).
%endif

#############################################################################
#########
%if %{with openmpi}
%package openmpi
Summary:    Portable Extensible Toolkit for Scientific Computation (OpenMPI)
BuildRequires: openmpi-devel
%if %{with hdf5}
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with ptscotch}
BuildRequires: ptscotch-openmpi-devel
%endif
%if %{with scalapack}
BuildRequires: scalapack-openmpi-devel
%if 0%{?rhel}
BuildRequires: blacs-openmpi-devel
%endif
%endif
%if %{with mumps}
BuildRequires: MUMPS-openmpi-devel
%endif
%if %{with sundials}
BuildRequires: sundials-openmpi-devel
%endif
%if %{with superludist}
BuildRequires: superlu_dist-openmpi-devel >= 6.3.0
%endif
%if %{with fftw}
BuildRequires: fftw-devel
BuildRequires: fftw-openmpi-devel
%endif
%if %{with hypre}
BuildRequires: hypre-openmpi-devel
%endif

%description openmpi
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package openmpi-devel
Summary:    Portable Extensible Toolkit for Scientific Computation (OpenMPI)
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:   openmpi-devel%{?_isa} = %{epoch}:%{openmpiversion}
Requires:   hdf5-openmpi-devel%{?_isa}
%description openmpi-devel
Portable Extensible Toolkit for Scientific Computation (developer files).

%if %{with python}
%package -n     python3-%{name}-openmpi
Summary:        Python3 bindings for OpenMPI PETSc

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  python3-numpy
%if 0%{?rhel}
BuildRequires:  python3-pip
%else
BuildRequires:  python3-Cython
%endif
Requires:       petsc-openmpi%{?_isa}
Requires:       hdf5-openmpi%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-openmpi%{?_isa}
Requires:       openmpi%{?_isa} = %{epoch}:%{openmpiversion}
Requires:       MUMPS-openmpi%{?_isa}

Obsoletes:      %{pymodule_name}-openmpi < 0:3.14.0-3
Obsoletes:      python3-%{pymodule_name}-openmpi < 0:3.14.0-3
Provides:       python3-%{pymodule_name}-openmpi = 0:%{pymodule_version}-%{release}
Provides:       python-%{pymodule_name}-openmpi = 0:%{pymodule_version}-%{release}
Provides:       %{pymodule_name}-openmpi = 0:%{pymodule_version}-%{release}

%description -n python3-%{name}-openmpi
This package provides Python3 bindings for OpenMPI PETSc,
the Portable, Extensible Toolkit for Scientific Computation.
%endif
%endif
######
###############################################################################
######
%if %{with mpich}
%package mpich
Summary:    Portable Extensible Toolkit for Scientific Computation (MPICH)
BuildRequires: mpich-devel
%if %{with hdf5}
BuildRequires: hdf5-mpich-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-mpich-devel
%endif
%if %{with ptscotch}
BuildRequires: ptscotch-mpich-devel
%endif
%if %{with scalapack}
BuildRequires: scalapack-mpich-devel
%if 0%{?rhel}
BuildRequires: blacs-mpich-devel
%endif
%endif
%if %{with mumps}
BuildRequires: MUMPS-mpich-devel
%endif
%if %{with sundials}
BuildRequires: sundials-mpich-devel
%endif
%if %{with superludist}
BuildRequires: superlu_dist-mpich-devel >= 6.3.0
%endif
%if %{with hypre}
BuildRequires: hypre-mpich-devel
%endif
%if %{with fftw}
BuildRequires: fftw-devel
BuildRequires: fftw-mpich-devel
%endif
Requires:   mpich%{?_isa} = 0:%{mpichversion}

%description mpich
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package mpich-devel
Summary:    Portable Extensible Toolkit for Scientific Computation (MPICH)
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:   mpich-devel%{?_isa} = 0:%{mpichversion}
Requires:   hdf5-mpich-devel%{?_isa}
%description mpich-devel
Portable Extensible Toolkit for Scientific Computation (developer files).

%if %{with python}
%package -n     python3-%{name}-mpich
Summary:        Python3 bindings for MPICH PETSc

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  scalapack-mpich-devel
BuildRequires:  ptscotch-mpich-devel
BuildRequires:  python3-numpy
%if 0%{?rhel}
BuildRequires:  python3-pip
%else
BuildRequires:  python3-Cython
%endif
Requires:       petsc-mpich%{?_isa}
Requires:       hdf5-mpich%{?_isa}
Requires:       scalapack-mpich%{?_isa}
Requires:       ptscotch-mpich%{?_isa}
Requires:       mpich%{?_isa} = 0:%{mpichversion}
Requires:       MUMPS-mpich%{?_isa}

Obsoletes:      %{pymodule_name}-mpich < 0:3.14.0-3
Obsoletes:      python3-%{pymodule_name}-mpich < 0:3.14.0-3
Provides:       python3-%{pymodule_name}-mpich = 0:%{pymodule_version}-%{release}
Provides:       python-%{pymodule_name}-mpich = 0:%{pymodule_version}-%{release}
Provides:       %{pymodule_name}-mpich = 0:%{pymodule_version}-%{release}

%description -n python3-%{name}-mpich
This package provides Python3 bindings for MPICH PETSc,
the Portable, Extensible Toolkit for Scientific Computation.
%endif
%endif
######
#############################################################################

%prep
%setup -qc

%if %{with python}
rm -rf %{name}-%{version}/src/binding/petsc4py/src/*.egg-info

%if 0%{?fedora}
for i in `find . -name 'setup.py' -o -name 'configure' -o -name '*.py'`; do
%py3_shebang_fix $i
done
%endif
%endif

pushd %{name}-%{version}
%patch -P 7 -p1 -b .backup
%patch -P 100 -p1
%patch -P 101 -p1
popd

# Remove pregenerated Cython C sources
pushd %{name}-%{version}
rm -vf $(grep -rl '/\* Generated by Cython')
popd

%if %{with arch64}
cp -a %{name}-%{version} build64
pushd build64
%patch -P 1 -p0
%if %{with metis64}
%patch -P 4 -p1 -b .metis64
%endif
popd
%endif

pushd %{name}-%{version}
%patch -P 0 -p0 -b .backup
%patch -P 6 -p1 -b .backup
popd

%if %{with openmpi}
cp -a %{name}-%{version} buildopenmpi_dir
%if 0%{?rhel}
cp %{SOURCE1} buildopenmpi_dir/src/binding/petsc4py/src/petsc4py/PETSc.c
cp %{SOURCE2} buildopenmpi_dir/src/binding/petsc4py/src/petsc4py/PETSc.h
cp %{SOURCE3} buildopenmpi_dir/src/binding/petsc4py/src/petsc4py/PETSc_api.h
%endif
%endif

%if %{with mpich}
cp -a %{name}-%{version} buildmpich_dir
%if 0%{?rhel}
cp %{SOURCE1} buildmpich_dir/src/binding/petsc4py/src/petsc4py/PETSc.c
cp %{SOURCE2} buildmpich_dir/src/binding/petsc4py/src/petsc4py/PETSc.h
cp %{SOURCE3} buildmpich_dir/src/binding/petsc4py/src/petsc4py/PETSc_api.h
%endif
%endif

# Do NOT move up this patch
pushd %{name}-%{version}
%patch -P 3 -p1 -b .backup
popd

%generate_buildrequires
%pyproject_buildrequires

%build
pushd %{name}-%{version}
%configure --with-cc=gcc --with-cxx=g++ --with-fc=gfortran \
 %{petsc_build_options} \
 --with-64-bit-indices=0 \
%if %{with blas}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar} --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar} --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
%if %{with metis}
 --with-metis=1 \
%endif
%if %{with tetgen}
 --with-tetgen=1 \
 --with-tetgen-lib=-ltetgen \
%endif
%if %{with superlu}
 --with-superlu=1 \
 --with-superlu-include=%{_includedir}/SuperLU \
 --with-superlu-lib=-lsuperlu \
%endif
%if %{with suitesparse}
 --with-suitesparse=1 \
 --with-suitesparse-include=%{_includedir}/suitesparse \
 --with-suitesparse-lib="-lumfpack -lklu -lcholmod -lamd"
%endif
#cat config.log && exit 1
##

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/%{name}-%{version} PETSC_ARCH=%{_arch} all
popd

%if %{with arch64}
pushd build64
%configure --with-cc=gcc --with-cxx=g++ --with-fc=gfortran \
 %{petsc_build_options} \
 --with-64-bit-indices=1 \
%if %{with metis64}
 --with-metis=1 \
%endif
%if %{with blas64}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar}64 --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar}64 --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
%if %{with suitesparse64}
 --with-suitesparse=1 \
 --with-suitesparse-include=%{_includedir}/suitesparse \
 --with-suitesparse-lib="-lumfpack64 -lklu64 -lcholmod64 -lamd64"
%endif
##

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/build64 PETSC_ARCH=%{_arch} all
popd
%endif

%if %{with openmpi}
cd buildopenmpi_dir

%{_openmpi_load}
export CC=mpicc
export CXX=mpic++
export FC=mpifort
%configure --with-cc=mpicc --with-cxx=mpic++ --with-fc=mpifort \
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran -lmpi_mpifh" \
 --LIBS=" -lmpi -lmpi_mpifh" \
 %{petsc_mpibuild_options} \
%if %{with metis}
 --with-metis=1 \
%endif
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 --with-64-bit-indices=0 \
%endif
%if %{with blas}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar} --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar} --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
#cat config.log
#exit 1

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/buildopenmpi_dir PETSC_ARCH=%{_arch} all
 
%if %{with python}
pushd src/binding/petsc4py
export PETSC_ARCH=%{_arch}
export PETSC_DIR=../../../
%py3_build
unset PETSC_ARCH
unset PETSC_DIR
popd
%endif

%{_openmpi_unload}
cd ..
%endif

%if %{with mpich}
cd buildmpich_dir

%{_mpich_load}
export CC=mpicc
export CXX=mpic++
export FC=mpifort
%configure --with-cc=mpicc --with-cxx=mpic++ --with-fc=mpifort \
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran -lfmpich -lmpichf90" \
 --LIBS=" -lmpich -lfmpich -lmpichf90" \
 %{petsc_mpibuild_options} \
%if %{with metis}
 --with-metis=1 \
%endif
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 --with-64-bit-indices=0 \
%endif
%if %{with blas}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar} --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar} --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
#cat config.log
#exit 1

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/buildmpich_dir PETSC_ARCH=%{_arch} all

%if %{with python}
pushd src/binding/petsc4py
export PETSC_ARCH=%{_arch}
export PETSC_DIR=../../../
%py3_build
unset PETSC_ARCH
unset PETSC_DIR
popd
%endif

%{_mpich_unload}
cd ..
%endif

%install
pushd %{name}-%{version}
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_fmoddir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* %{buildroot}%{_libdir}
ln -sf libpetsc.so.%{version} %{buildroot}%{_libdir}/libpetsc.so
ln -sf libpetsc.so.%{version} %{buildroot}%{_libdir}/libpetsc.so.%{releasever}
ln -sf libpetsc.so.%{version} %{buildroot}%{_libdir}/libpetsc.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}%{_includedir}/%{name}/
install -pm 644 %{_arch}/include/*.mod %{buildroot}%{_fmoddir}/%{name}/
cp -a include/* %{buildroot}%{_includedir}/%{name}/

cp -a %{_arch}/lib/pkgconfig %{buildroot}%{_libdir}/
sed -e 's|${prefix}/lib|${prefix}/%{_lib}|g' -i %{buildroot}%{_libdir}/pkgconfig/PETSc.pc
ln -fs %{_libdir}/pkgconfig/PETSc.pc %{buildroot}%{_libdir}/pkgconfig/petsc.pc

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}%{_libdir}/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}%{_libdir}/%{name}/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}%{_libdir}/%{name}/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}%{_libdir}/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/%{name}-%{version}|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/%{name}-%{version}/%{_arch}/|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/%{name} -I%{_fmoddir}/%{name}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}/conf/rules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscrules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
popd

%if %{with arch64}
pushd build64
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}/%{name}64
mkdir -p %{buildroot}%{_fmoddir}/%{name}64
mkdir -p %{buildroot}%{_libdir}/%{name}64/conf
mkdir -p %{buildroot}%{_libdir}/pkgconfig

install -pm 755 %{_arch}/lib/libpetsc64.* %{buildroot}%{_libdir}
ln -sf libpetsc64.so.%{version} %{buildroot}%{_libdir}/libpetsc64.so
ln -sf libpetsc64.so.%{version} %{buildroot}%{_libdir}/libpetsc64.so.%{releasever}
ln -sf libpetsc64.so.%{version} %{buildroot}%{_libdir}/libpetsc64.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}%{_includedir}/%{name}64/
install -pm 644 %{_arch}/include/*.mod %{buildroot}%{_fmoddir}/%{name}64/
cp -a include/* %{buildroot}%{_includedir}/%{name}64/

cp -p %{_arch}/lib/pkgconfig/PETSc.pc %{buildroot}%{_libdir}/pkgconfig/PETSc64.pc
cp -p %{_arch}/lib/pkgconfig/PETSc.pc %{buildroot}%{_libdir}/pkgconfig/petsc64.pc
sed -e 's|${prefix}/lib|${prefix}/%{_lib}|g' -i %{buildroot}%{_libdir}/pkgconfig/PETSc64.pc
sed -e 's|${prefix}/lib|${prefix}/%{_lib}|g' -i %{buildroot}%{_libdir}/pkgconfig/petsc64.pc

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}%{_libdir}/%{name}64/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}%{_libdir}/%{name}64/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}%{_libdir}/%{name}64/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}%{_libdir}/%{name}64/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/build64|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/build64/%{_arch}/|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include/|-I%{_includedir}/%{name}64 -I%{_fmoddir}/%{name}64|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/rules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscrules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
popd
%endif

%if %{with openmpi}
pushd buildopenmpi_dir
%{_openmpi_load}
mkdir -p %{buildroot}$MPI_LIB %{buildroot}$MPI_INCLUDE/%{name}
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}
mkdir -p %{buildroot}$MPI_LIB/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* %{buildroot}$MPI_LIB
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{releasever}
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}$MPI_INCLUDE/%{name}/
install -pm 644 %{_arch}/include/*.mod %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}/
cp -a include/* %{buildroot}$MPI_INCLUDE/%{name}/

cp -a %{_arch}/lib/pkgconfig %{buildroot}$MPI_LIB/
sed -e 's|-I${includedir}/petsc|-I%{_includedir}/openmpi-%{_arch}/petsc|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-L${libdir}|-L%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|ldflag_rpath=-L|ldflag_rpath=-L%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-lpetsc|-lpetsc -lhdf5|' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|${prefix}/lib|${prefix}/%{_lib}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
ln -fs $MPI_LIB/pkgconfig/PETSc.pc %{buildroot}$MPI_LIB/pkgconfig/petsc.pc

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}$MPI_LIB/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/buildopenmpi_dir|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/buildopenmpi_dir/%{_arch}/|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/openmpi-%{_arch}/%{name} -I%{_fmoddir}/openmpi/%{name}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/rules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscrules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables

%if %{with python}
pushd src/binding/petsc4py
export PETSC_ARCH=%{_arch}
export PETSC_DIR=../../../
%py3_install -- --verbose
unset PETSC_ARCH
unset PETSC_DIR
popd

# Install petsc4py files into MPI directories
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/openmpi
%endif

mkdir -p %{buildroot}$MPI_PYTHON3_SITEARCH
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name} %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info

chrpath -r %{_libdir}/openmpi/lib %{buildroot}$MPI_PYTHON3_SITEARCH/%{pymodule_name}/lib/%{_arch}/*.so
%endif
%{_openmpi_unload}
cd ..
%endif

%if %{with mpich}
cd buildmpich_dir
%{_mpich_load}
mkdir -p %{buildroot}$MPI_LIB %{buildroot}$MPI_INCLUDE/%{name}
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}
mkdir -p %{buildroot}$MPI_LIB/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* %{buildroot}$MPI_LIB
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{releasever}
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}$MPI_INCLUDE/%{name}/
install -pm 644 %{_arch}/include/*.mod %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}/
cp -a include/* %{buildroot}$MPI_INCLUDE/%{name}/

cp -a %{_arch}/lib/pkgconfig %{buildroot}$MPI_LIB/
sed -e 's|-I${includedir}/petsc|-I%{_includedir}/mpich-%{_arch}/petsc|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-L${libdir}|-L%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|ldflag_rpath=-L|ldflag_rpath=-L%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-lpetsc|-lpetsc -lhdf5|' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|${prefix}/lib|${prefix}/%{_lib}/mpich/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
ln -fs $MPI_LIB/pkgconfig/PETSc.pc %{buildroot}$MPI_LIB/pkgconfig/petsc.pc

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}$MPI_LIB/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/buildmpich_dir|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/buildmpich_dir/%{_arch}/|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/mpich-%{_arch}/%{name} -I%{_fmoddir}/mpich/%{name}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/rules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscrules
sed -e 's|${PETSC_DIR}|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables

%if %{with python}
pushd src/binding/petsc4py
export PETSC_ARCH=%{_arch}
export PETSC_DIR=../../../
%py3_install -- --verbose
unset PETSC_ARCH
unset PETSC_DIR
popd

# Install petsc4py files into MPI directories
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/mpich
%endif

mkdir -p %{buildroot}$MPI_PYTHON3_SITEARCH
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name} %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info

chrpath -r %{_libdir}/mpich/lib %{buildroot}$MPI_PYTHON3_SITEARCH/%{pymodule_name}/lib/%{_arch}/*.so
%endif
%{_mpich_unload}
cd ..
%endif

# Move html documentation in _pkgdocdir
pushd %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_pkgdocdir}/headers
for i in `find . -name "*.h.html" -type f -print`; do
    mv $i %{buildroot}%{_pkgdocdir}/headers
done
for i in `find . -name "*.html" -type f -print`; do
    mv $i %{buildroot}%{_pkgdocdir}/headers
done
find . -name "Makefile" -type f -print | xargs /bin/rm -f
popd
cp -a %{name}-%{version}/docs/* %{buildroot}%{_pkgdocdir}
#

%check

%if %{with openmpi}
%{_openmpi_load}
%if %{with check}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
export PETSC_DIR=%{_builddir}/%{name}-%{version}/buildopenmpi_dir
export PETSC_ARCH=%{_arch}
export MPI_INTERFACE_HOSTNAME=localhost
export OMPI_MCA_btl_base_warn_component_unused=0
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/buildopenmpi_dir/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildopenmpi_dir V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/buildopenmpi_dir/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildopenmpi_dir V=1
%endif
%endif

%if %{with python}
%if %{with pycheck}
pushd buildopenmpi_dir/src/binding/petsc4py
export PETSC_ARCH=%{_arch}
export PETSC_DIR=../../../
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/openmpi
%endif
export PYTHONPATH=%{buildroot}$MPI_PYTHON3_SITEARCH
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%{__python3} setup.py test
unset PETSC_ARCH
unset PETSC_DIR
popd
%endif
%endif
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
%if %{with check}
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/buildmpich_dir/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/buildmpich_dir
export PETSC_ARCH=%{_arch}
export MPI_INTERFACE_HOSTNAME=localhost
export OMPI_MCA_btl_base_warn_component_unused=0
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/buildmpich_dir/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildmpich_dir V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/buildmpich_dir/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildmpich_dir V=1
%endif
%endif

%if %{with python}
%if %{with pycheck}
pushd buildmpich_dir/src/binding/petsc4py
export PETSC_ARCH=%{_arch}
export PETSC_DIR=../../../
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/mpich
%endif
export PYTHONPATH=%{buildroot}$MPI_PYTHON3_SITEARCH
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%{__python3} setup.py test
unset PETSC_ARCH
unset PETSC_DIR
popd
%endif
%endif
%{_mpich_unload}
%endif

%if %{with check}
export LD_LIBRARY_PATH=%{_libdir}:%{_builddir}/%{name}-%{version}/%{name}-%{version}/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/%{name}-%{version}
export PETSC_ARCH=%{_arch}
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/%{name}-%{version}/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C %{name}-%{version} V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/%{name}-%{version}/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C %{name}-%{version} V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/%{name}-%{version}/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS'
%endif

%if %{with arch64}
export LD_LIBRARY_PATH=%{_libdir}:%{_builddir}/%{name}-%{version}/build64/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/build64
export PETSC_ARCH=%{_arch}
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/build64/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
## 'make test' needs to link against -lpetsc
## Crude fix:
ln -s %{_builddir}/%{name}-%{version}/build64/%{_arch}/lib/libpetsc64.so %{_builddir}/%{name}-%{version}/build64/%{_arch}/lib/libpetsc.so

%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C build64 V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/build64/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C build64 V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/build64/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS'
%endif
%endif
%endif

%files
%license %{name}-%{version}/LICENSE
%{_libdir}/libpetsc.so.3
%{_libdir}/libpetsc.so.%{releasever}
%{_libdir}/libpetsc.so.%{version}

%files devel
%{_libdir}/pkgconfig/PETSc.pc
%{_libdir}/pkgconfig/petsc.pc
%{_libdir}/%{name}/
%{_libdir}/libpetsc.so
%{_includedir}/%{name}/
%{_fmoddir}/%{name}/

%files doc
%license %{name}-%{version}/LICENSE
%{_pkgdocdir}/

%if %{with arch64}
%files -n petsc64
%license build64/LICENSE
%{_libdir}/libpetsc64.so.3
%{_libdir}/libpetsc64.so.%{releasever}
%{_libdir}/libpetsc64.so.%{version}

%files -n petsc64-devel
%{_libdir}/pkgconfig/PETSc64.pc
%{_libdir}/pkgconfig/petsc64.pc
%{_libdir}/%{name}64/
%{_libdir}/libpetsc64.so
%{_includedir}/%{name}64/
%{_fmoddir}/%{name}64/
%endif

%if %{with openmpi}
%files openmpi
%license buildopenmpi_dir/LICENSE
%{_libdir}/openmpi/lib/libpetsc.so.3
%{_libdir}/openmpi/lib/libpetsc.so.%{releasever}
%{_libdir}/openmpi/lib/libpetsc.so.%{version}

%files openmpi-devel
%{_libdir}/openmpi/lib/libpetsc.so
%{_libdir}/openmpi/lib/%{name}/
%{_libdir}/openmpi/lib/pkgconfig/PETSc.pc
%{_libdir}/openmpi/lib/pkgconfig/petsc.pc
%{_includedir}/openmpi-%{_arch}/%{name}/
%{_fmoddir}/openmpi/%{name}/

%if %{with python}
%files -n python3-%{name}-openmpi
%{python3_sitearch}/openmpi/%{pymodule_name}/
%{python3_sitearch}/openmpi/%{pymodule_name}-%{pymodule_version}.dist-info
%endif
%endif

%if %{with mpich}
%files mpich
%license buildmpich_dir/LICENSE
%{_libdir}/mpich/lib/libpetsc.so.3
%{_libdir}/mpich/lib/libpetsc.so.%{releasever}
%{_libdir}/mpich/lib/libpetsc.so.%{version}

%files mpich-devel
%{_libdir}/mpich/lib/libpetsc.so
%{_libdir}/mpich/lib/%{name}/
%{_libdir}/mpich/lib/pkgconfig/PETSc.pc
%{_libdir}/mpich/lib/pkgconfig/petsc.pc
%{_includedir}/mpich-%{_arch}/%{name}/
%{_fmoddir}/mpich/%{name}/

%if %{with python}
%files -n python3-%{name}-mpich
%{python3_sitearch}/mpich/%{pymodule_name}/
%{python3_sitearch}/mpich/%{pymodule_name}-%{pymodule_version}.dist-info
%endif
%endif

%changelog
%autochangelog
