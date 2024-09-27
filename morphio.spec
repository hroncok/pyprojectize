# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/BlueBrain/MorphIO

%global _description %{expand:
MorphIO is a library for reading and writing neuron morphology files. It
supports the following formats:

- SWC
- ASC (aka. neurolucida)
- H5 v1
- H5 v2 is not supported anymore

It provides 3 C++ classes that are the starting point of every morphology
analysis:

- Soma: contains the information related to the soma.
- Section: a section is the succession of points between two bifurcations. To
  the bare minimum the Section object will contain the section type, the
  position and diameter of each point.
- Morphology: the morphology object contains general information about the
  loaded cell but also provides accessors to the different sections.

One important concept is that MorphIO is split into a read-only part and a
read/write one.
}

%global pretty_name MorphIO

# cpp tests
%bcond_without tests
# python tests
%bcond_without pytests

Name:           morphio
Version:        3.3.9
Release:        %autorelease
Summary:        A python and C++ library for reading and writing neuronal morphologies
%forgemeta
# The entire source is Apache-2.0 except the following, which is BSD-3-Clause:
#   - CMake/CodeCoverage.cmake
# The “effective license” remains Apache-2.0.
License:        Apache-2.0 AND BSD-3-Clause
URL:            %forgeurl
Source0:        %forgesource

# Patches
# https://github.com/sanjayankur31/MorphIO/tree/fedora-3.3.2
# Some sent upstream: https://github.com/BlueBrain/MorphIO/pull/293
# Do not let cmake use $FLAGS env var
Patch:          stop-them-using-a-random-env-var.patch
# Remove more hard-coded compiler flags
Patch:          remove-upstreams-flags.patch
# Add install target for the compiled python module
Patch:          install-python-shared-object.patch
# Stop setup.py from running the cmake build, we’ll run it ourselves
Patch:          stop-setup.py-from-cmake-build.patch
# Some Python tests are failing because “expected” results are float32 and then
# promoted back to float64 for comparison with the actual results. We are not
# sure why upstream is not experiencing this.
Patch:          pytest-float32.patch
# use LIB_INSTALL_DIR which is defined by %%cmake
Patch:          use-lib_install_dir.patch
# Allow use of external ghc_filesystem
Patch:          allow_use_of_external_ghc_filesystem.patch
# Above patch fails with:
#CMake Error at src/CMakeLists.txt:64 (target_include_directories):
#  Error evaluating generator expression:
#
#    $<TARGET_PROPERTY:ghc_filesystem,INTERFACE_INCLUDE_DIRECTORIES>
#
#  Target "ghc_filesystem" not found.
# So let's circumvent CMake foo for ghc_filesystem
Patch:          dont_use_cmake_for_finding_ghc_filesystem.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  hdf5-devel
BuildRequires:  boost-devel
%if %{with tests}
BuildRequires:  cmake(Catch2) < 3
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Our choice: the make backend works fine too
BuildRequires:  ninja-build
BuildRequires:  lcov

# Header-only libraries; -static required by guidelines for tracking
BuildRequires:  cmake(gsl-lite)
BuildRequires:  gsl-lite-static
BuildRequires:  cmake(highfive)
BuildRequires:  highfive-static
BuildRequires:  lexertl14-devel
BuildRequires:  lexertl14-static
BuildRequires:  cmake(ghc_filesystem)
BuildRequires:  gulrak-filesystem-static
# We cannot currently figure out how to unbundle this:
BuildRequires:  cmake(pybind11)
BuildRequires:  pybind11-static

%description %_description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

# A gsl header is included from the public morphio/types.h header.
Requires:       gsl-lite-devel%{?_isa}
Requires:       gsl-lite-static
# A HighFive header is included from the public morphio/morphology.h header.
Requires:       highfive-devel%{?_isa}
Requires:       highfive-static
# Note that packages using this -devel package should ideally also BR
# gsl-lite-static and highfive-static for header-only library tracking.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n python3-%{name}
Summary:        Python bindings for %{name}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm
%if %{with pytests}
# tests/requirements-tests.txt
BuildRequires:  %{py3_dist h5py} >= 2.9.0
BuildRequires:  %{py3_dist pytest} >= 6.0
BuildRequires:  %{py3_dist numpy} >= 1.14.2
BuildRequires:  %{py3_dist requests} >= 2.25.1
%endif

# Note that this package does not depend at all on the base package (it does
# not link against the shared library).

%description -n python3-%{name}
This package includes the Python 3 bindings for %{name}.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
This package provides documentation for %{name}


%prep
%autosetup -n %{pretty_name}-%{version} -p1

# Unbundle gsl-lite
rm -rvf 3rdparty/GSL_LITE
sed -r -i '/GSL_LITE/d' MANIFEST.in
sed -r -i '/director.*\(.*(gsl-lite|GSL_LITE).*\)/d' 3rdparty/CMakeLists.txt
sed -r -i \
    -e '/TARGET_PROPERTY:gsl-lite,INTERFACE_INCLUDE_DIRECTORIES/d' \
    -e 's/PUBLIC[[:blank:]]+gsl-lite[[:blank:]]+(PRIVATE)/\1/' \
    src/CMakeLists.txt
# Update includes. Note that this affects the public API headers.
#
# The grep-then-sed pattern means we only modify those files that need it,
# preserving the mtimes on the others.
grep -ErIl '#[[:blank:]]*include[[:blank:]]+["<]gsl/gsl[">]' . |
  xargs -r sed -r -i \
      's@(#[[:blank:]]*include[[:blank:]]+["<]gsl/gsl)([">])@\1-lite\.hpp\2@'

# Unbundle lexertl
rm -rvf '3rdparty/lexertl'
ln -s '%{_includedir}/lexertl' '3rdparty/'

# Some of these could make it into the installed package:
find . -type f -name .gitignore -print -delete


%generate_buildrequires
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%cmake \
    -DEXTERNAL_PYBIND11:BOOL=TRUE \
    -DEXTERNAL_HIGHFIVE:BOOL=TRUE \
    -DEXTERNAL_GHC_FILESYSTEM:BOOL=TRUE \
    -DMORPHIO_USE_DOUBLE:BOOL=TRUE \
    -DBUILD_BINDINGS:BOOL=TRUE \
    -DMorphIO_CXX_WARNINGS:BOOL=FALSE \
    -DMORPHIO_TESTS:BOOL=%{?with_tests:TRUE}%{?!with_tests:FALSE} \
    -DEXTERNAL_CATCH2:BOOL=TRUE \
    -DMORPHIO_ENABLE_COVERAGE:BOOL=TRUE \
    -DMORPHIO_USE_DOUBLE:BOOL=TRUE \
    -DMORPHIO_VERSION_STRING:STRING="%{version}" \
    -GNinja \
    -Wno-dev
%cmake_build

# Build pure python bits
%pyproject_wheel


%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%cmake_install
# Install pure python bits
%pyproject_install

# Move module to sitearch so that the binding can be correctly imported.
if [ '%{python3_sitelib}' != '%{python3_sitearch}' ]
then
  mv -v %{buildroot}%{python3_sitelib}/%{name}/* \
        %{buildroot}%{python3_sitearch}/%{name}
  mv -v %{buildroot}%{python3_sitelib}/%{name}*egg-info \
        %{buildroot}%{python3_sitearch}/
fi


%check
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%if %{with tests}
# From ci/cpp_test.sh
%ctest -VV
%endif
%if %{with pytests}
# We will change directories so that the “un-built” package is not imported
xdir="$(basename "${PWD}")"
# From ci/python_test.sh
cd ..
# Fetches from the Internet:
k='not test_v2'
# Still fails in 3.3.6
# TODO: Is this a real problem? The answer is only slightly outside tolerances.
#
# >               assert_array_almost_equal(neuron.markers[0].points,
#                                           np.array([[81.58, -77.98, -20.32]], dtype=np.float32))
# E               AssertionError:
# E               Arrays are not almost equal to 6 decimals
# E
# E               Mismatched elements: 2 / 3 (66.7%)
# E               Max absolute difference: 3.35693359e-06
# E               Max relative difference: 4.30486464e-08
# E                x: array([[ 81.58, -77.98, -20.32]])
# E                y: array([[ 81.58, -77.98, -20.32]], dtype=float32)
k="${k} and not test_neurolucida_markers"
# Still fails to 3.3.6
# TODO: Is this a real problem? The answer is only slightly outside tolerances.
#
# >       assert_array_equal(m.markers[0].points, np.array([[  -0.97    , -141.169998,   84.769997]],
#                                                          dtype=np.float32))
# E       AssertionError:
# E       Arrays are not equal
# E
# E       Mismatched elements: 3 / 3 (100%)
# E       Max absolute difference: 3.35693359e-06
# E       Max relative difference: 3.96004922e-08
# E        x: array([[  -0.97, -141.17,   84.77]])
# E        y: array([[  -0.97, -141.17,   84.77]], dtype=float32)
k="${k} and not test_marker_with_string"
# In the same vein as above, failing since 3.3.6
k="${k} and not test_mitochondria"
k="${k} and not test_mitochondria_read"
# TODO: pytest segfaults while writing a temporary file..
k="${k} and not test_dendritic_spine_round_trip_empty_postsynaptic_density"
%pytest "${xdir}/tests" -k "${k}" -v
%endif


%files
%license LICENSE.txt
%{_libdir}/libmorphio.so.0.0.0


%files devel
%{_includedir}/%{name}
%{_libdir}/libmorphio.so
%{_libdir}/cmake/%{pretty_name}


%files -n python3-%{name}
%license LICENSE.txt
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-%{version}.dist-info


%files doc
%license LICENSE.txt
%doc AUTHORS.txt CHANGELOG.md CONTRIBUTING.md README.rst examples

%changelog
%autochangelog
