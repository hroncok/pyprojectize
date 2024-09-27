# MUSIC depends on MPI for communication, so a non-MPI version is not being
# built.
# https://github.com/INCF/MUSIC/issues/55

%global forgeurl https://github.com/INCF/MUSIC/

# For debugging
%bcond_without mpich
%bcond_without openmpi

%global lname music

%global _description %{expand:
MUSIC is an API allowing large scale neuron simulators using MPI internally to
exchange data during runtime.  MUSIC provides mechanisms to transfer massive
amounts of event information and continuous values from one parallel
application to another.  Special care has been taken to ensure that existing
simulators can be adapted to MUSIC.  In particular, MUSIC handles data transfer
between applications that use different time steps and different data
allocation strategies.

This is the MUSIC pilot implementation.

The two most important components built from this software distribution is the
music library `libmusic.a' and the music utility `music'.  A MUSIC-aware
simulator links against the C++ library and can be launched using mpirun
together with the music utility as described below.  MUSIC can also be used
from a C program using the API in music-c.h.

MUSIC is distributed under the GNU General Public License v3.}


Name:           MUSIC
Version:        1.2.1
Release:        %autorelease
Summary:        The MUltiSimulation Coordinator

%global tag %{version}
%forgemeta

License:        GPL-3.0-or-later
URL:            %forgeurl
Source0:        %forgesource

# MPI unavailable
ExcludeArch:    %{ix86}

# https://github.com/sanjayankur31/MUSIC/tree/fedora-1.2.1

Patch:         0001-Disable-sysguess.patch
Patch:         0002-Enable-tests-and-extras.patch
Patch:         0003-Make-python-bits-ourselves.patch
Patch:         0004-Make-bundled-rudeconfig-also-follow-all-flags.patch
Patch:         0005-Remove-src-flags.patch
#
# Bundled rudeconfig
Provides:       bundled(rudeconfig) = 5.0.5-1

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  patch
BuildRequires:  hwloc-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(looseversion)
BuildRequires:  python3dist(cython)
# Currently bundles a modified version of rudeconfig which cannot be unbundled
# until MUSIC upstream sends their changes upstream to rudeconfig.
# https://github.com/INCF/MUSIC/issues/56
# BuildRequires:  rudeconfig-devel

%description %_description

%package common
Summary:    Architecture independent test and example files for %{name}
BuildArch:  noarch

%description common %_description

%if %{with mpich}
%package mpich
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
Requires:       mpich

%description mpich %_description

%package mpich-devel
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
Requires:       mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
Development files for %{name} built with MPICH.

%package -n python3-%{name}-mpich
Summary:        Python3 support for %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-mpich
Requires:       python3-mpi4py-mpich
Requires:       mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-mpich %_description
%endif

%if %{with openmpi}
%package openmpi
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi

%description openmpi %_description

%package openmpi-devel
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
Development files for %{name} built with MPICH.

%package -n python3-%{name}-openmpi
Summary:        Python3 support for %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-openmpi
Requires:       python3-mpi4py-openmpi
Requires:       openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-openmpi %_description
%endif

%prep
%autosetup -c -n %{name}-%{version} -N
# Unable to use autosetup directly because we need three copies of the source
# in here now
# Apply patches
pushd %{name}-%{version}
%patch -p1 -P 0 1 2 3 4
# on Fedora, we have mpichversion, not mpich2version
sed -i 's|mpich2version|mpichversion|' configure.ac
popd

cp %{name}-%{version}/LICENSE .
cp %{name}-%{version}/README .

%if %{with mpich}
    cp -a %{name}-%{version} %{name}-%{version}-mpich
%endif

%if %{with openmpi}
    cp -a %{name}-%{version} %{name}-%{version}-openmpi
%endif

%generate_buildrequires
%pyproject_buildrequires

%build

%global do_build %{expand:
echo "** BUILDING $MPI_COMPILE_TYPE **"
pushd %{name}-%{version}$MPI_COMPILE_TYPE
./autogen.sh &&
%{set_build_flags}
MPI_CXXFLAGS="$CXXFLAGS $(pkg-config --cflags $MPI_VARIANT)"
MPI_CFLAGS="$CFLAGS $(pkg-config --cflags $MPI_VARIANT)"
MPI_LDFLAGS="$LDFLAGS $(pkg-config --libs $MPI_VARIANT | sed 's|-Lsystem/lib||')"
./configure LAUNCHSTYLE="_mpirun" SYSGUESS="$SYSGUESS" CXX=mpicxx CC=mpicc MPI_CXXFLAGS="$MPI_CXXFLAGS" MPI_CFLAGS="$MPI_CFLAGS" MPI_LDFLAGS="$MPI_LDFLAGS" PYTHON="$PYTHON_BIN" \\\
--disable-static \\\
--prefix=$MPI_HOME \\\
--libdir=$MPI_LIB \\\
--includedir=$MPI_INCLUDE \\\
--bindir=$MPI_BIN \\\
--mandir=$MPI_MAN

%make_build

# Make python bits ourselves
pushd pymusic
%{pyproject_wheel}
popd

popd
}


# Mpich
%if %{with mpich}
%{_mpich_load}
MPI_VARIANT="mpich"
SYSGUESS="mpich"

MPI_COMPILE_TYPE="-mpich"
PYTHON_VERSION=3
PYTHON_BIN="%{python3}"
%{do_build}

%{_mpich_unload}
%endif

# Openmpi
%if %{with openmpi}
%{_openmpi_load}
MPI_VARIANT="ompi-cxx"
SYSGUESS="openmpi"

MPI_COMPILE_TYPE="-openmpi"
PYTHON_VERSION=3
PYTHON_BIN="%{python3}"
%{do_build}
%{_openmpi_unload}
%endif

%install
%global do_install %{expand:
%make_install -C %{name}-%{version}$MPI_COMPILE_TYPE
mv $RPM_BUILD_ROOT/$MPI_HOME/lib/%{lname}-%{version}/* $RPM_BUILD_ROOT/$MPI_BIN/ -v && rm -vrf $RPM_BUILD_ROOT/$MPI_HOME/lib/%{lname}-%{version}
for f in contsink eventcounter eventgenerator eventlogger eventselect eventsink eventsource messagesource music viewevents waveconsumer waveproducer clocksource constsource contdelay eventdelay launchtest multiport musicrun test_ag
do
    if [ -e  "$RPM_BUILD_ROOT/$MPI_BIN/$f" ]; then
        echo "Renaming $f"
        mv "$RPM_BUILD_ROOT/$MPI_BIN/$f" "$RPM_BUILD_ROOT/$MPI_BIN/$f$MPI_SUFFIX" -v
    fi
done
# Delete script for tests
rm -f "$RPM_BUILD_ROOT/$MPI_BIN/music_tests.sh"

# Install python bits
pushd %{name}-%{version}$MPI_COMPILE_TYPE/pymusic
%{python3} setup.py install --skip-build --root $RPM_BUILD_ROOT --install-lib=$MPI_PYTHON3_SITEARCH
popd

# Move other files to correct location also
mv -v "$RPM_BUILD_ROOT/%{python3_sitearch}/%{lname}/config" "$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/%{lname}/"
mv -v "$RPM_BUILD_ROOT/%{python3_sitearch}/%{lname}/pymusic.so" "$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/%{lname}"
mv -v "$RPM_BUILD_ROOT/%{python3_sitearch}/%{lname}/pybuffer.so" "$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/%{lname}"
}


# Mpich
%if %{with mpich}
%{_mpich_load}
MPI_COMPILE_TYPE="-mpich"
%{do_install}
%{_mpich_unload}
%endif

# Openmpi
%if %{with openmpi}
%{_openmpi_load}
MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%{_openmpi_unload}
%endif

# Move arch independent examples and tests to datadir
%if %{with mpich} || %{with openmpi}
# Tests
install -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/%{lname}/
mv $RPM_BUILD_ROOT/%{_libdir}/mpich/share/%{lname}-%{version}/tests $RPM_BUILD_ROOT/%{_datadir}/%{lname}/ || exit 0

# Docs
install -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/doc/%{lname}/
mv $RPM_BUILD_ROOT/%{_libdir}/mpich/share/%{lname}-%{version}/examples $RPM_BUILD_ROOT/%{_datadir}/doc/%{lname}/ || exit 0

# Delete the folders
rm -vrf $RPM_BUILD_ROOT/%{_libdir}/mpich/share || exit 0
rm -vrff $RPM_BUILD_ROOT/%{_libdir}/openmpi/share || exit 0
%endif

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files common
%license LICENSE
%{_datadir}/%{lname}
%{_datadir}/doc/%{lname}


%if %{with mpich}
%files mpich
%license LICENSE
%doc README
%{_libdir}/mpich/bin/contsink_mpich
%{_libdir}/mpich/bin/eventcounter_mpich
%{_libdir}/mpich/bin/eventgenerator_mpich
%{_libdir}/mpich/bin/eventlogger_mpich
%{_libdir}/mpich/bin/eventselect_mpich
%{_libdir}/mpich/bin/eventsink_mpich
%{_libdir}/mpich/bin/eventsource_mpich
%{_libdir}/mpich/bin/messagesource_mpich
%{_libdir}/mpich/bin/music_mpich
%{_libdir}/mpich/bin/viewevents_mpich
%{_libdir}/mpich/bin/waveconsumer_mpich
%{_libdir}/mpich/bin/waveproducer_mpich
%{_libdir}/mpich/bin/constsource_mpich
%{_libdir}/mpich/bin/clocksource_mpich
%{_libdir}/mpich/bin/contdelay_mpich
%{_libdir}/mpich/bin/eventdelay_mpich
%{_libdir}/mpich/bin/launchtest_mpich
%{_libdir}/mpich/bin/multiport_mpich
%{_libdir}/mpich/bin/musicrun_mpich
%{_libdir}/mpich/bin/test_ag_mpich
%{_libdir}/mpich/bin/music_tests
%{_libdir}/mpich/lib/libmusic.so.1
%{_libdir}/mpich/lib/libmusic-c.so.1
%{_libdir}/mpich/lib/libmusic.so.1.0.0
%{_libdir}/mpich/lib/libmusic-c.so.1.0.2
%{_mandir}/mpich-%{_arch}/man1/*

%files mpich-devel
%license LICENSE
%doc README
%{_includedir}/mpich*/%{lname}
%{_includedir}/mpich*/%{lname}*.*
%{_includedir}/mpich*/predict_rank-c.h
%{_libdir}/mpich/lib/libmusic.so
%{_libdir}/mpich/lib/libmusic-c.so

%files -n python3-%{name}-mpich
%license LICENSE
%doc README
%{_libdir}/python%{python3_version}/site-packages/mpich/%{lname}
%{_libdir}/python%{python3_version}/site-packages/mpich/%{lname}-%{version}.dist-info
%endif

%if %{with openmpi}
%files openmpi
%license LICENSE
%doc README
%{_libdir}/openmpi/bin/contsink_openmpi
%{_libdir}/openmpi/bin/eventcounter_openmpi
%{_libdir}/openmpi/bin/eventgenerator_openmpi
%{_libdir}/openmpi/bin/eventlogger_openmpi
%{_libdir}/openmpi/bin/eventselect_openmpi
%{_libdir}/openmpi/bin/eventsink_openmpi
%{_libdir}/openmpi/bin/eventsource_openmpi
%{_libdir}/openmpi/bin/messagesource_openmpi
%{_libdir}/openmpi/bin/music_openmpi
%{_libdir}/openmpi/bin/viewevents_openmpi
%{_libdir}/openmpi/bin/waveconsumer_openmpi
%{_libdir}/openmpi/bin/waveproducer_openmpi
%{_libdir}/openmpi/bin/constsource_openmpi
%{_libdir}/openmpi/bin/clocksource_openmpi
%{_libdir}/openmpi/bin/contdelay_openmpi
%{_libdir}/openmpi/bin/eventdelay_openmpi
%{_libdir}/openmpi/bin/launchtest_openmpi
%{_libdir}/openmpi/bin/multiport_openmpi
%{_libdir}/openmpi/bin/musicrun_openmpi
%{_libdir}/openmpi/bin/test_ag_openmpi
%{_libdir}/openmpi/bin/music_tests
%{_libdir}/openmpi/lib/libmusic.so.1
%{_libdir}/openmpi/lib/libmusic-c.so.1
%{_libdir}/openmpi/lib/libmusic.so.1.0.0
%{_libdir}/openmpi/lib/libmusic-c.so.1.0.2
%{_mandir}/openmpi-%{_arch}/man1/*

%files openmpi-devel
%license LICENSE
%doc README
%{_includedir}/openmpi*/%{lname}
%{_includedir}/openmpi*/%{lname}*.*
%{_includedir}/openmpi*/predict_rank-c.h
%{_libdir}/openmpi/lib/libmusic.so
%{_libdir}/openmpi/lib/libmusic-c.so

%files -n python3-%{name}-openmpi
%license LICENSE
%doc README
%{_libdir}/python%{python3_version}/site-packages/openmpi/%{lname}
%{_libdir}/python%{python3_version}/site-packages/openmpi/%{lname}-%{version}.dist-info
%endif

%changelog
%autochangelog
