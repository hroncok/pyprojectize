%bcond_with mpich
%bcond_with openmpi

# Issue filed about warnings while compiling NEURON mod files:
# https://github.com/NeuralEnsemble/PyNN/issues/707


# Exclude privately used libnrnmech from provides
%global __provides_exclude ^libnrnmech\\.so.*$
%global __requires_exclude ^libnrnmech\\.so.*$

%global _description %{expand:
PyNN (pronounced 'pine') is a simulator-independent language for building
neuronal network models.

In other words, you can write the code for a model once, using the PyNN API and
the Python programming language, and then run it without modification on any
simulator that PyNN supports (currently NEURON, NEST and Brian) and on a number
of neuromorphic hardware systems.

The PyNN API aims to support modelling at a high-level of abstraction
(populations of neurons, layers, columns and the connections between them)
while still allowing access to the details of individual neurons and synapses
when required. PyNN provides a library of standard neuron, synapse and synaptic
plasticity models, which have been verified to work the same on the different
supported simulators. PyNN also provides a set of commonly-used connectivity
algorithms (e.g. all-to-all, random, distance-dependent, small-world) but makes
it easy to provide your own connectivity in a simulator-independent way.

Even if you don’t wish to run simulations on multiple simulators, you may
benefit from writing your simulation code using PyNN’s powerful, high-level
interface. In this case, you can use any neuron or synapse model supported by
your simulator, and are not restricted to the standard models.

Documentation: http://neuralensemble.org/docs/PyNN/
Mailing list: https://groups.google.com/forum/?fromgroups#!forum/neuralensemble

This package supports the NEURON, NEST, and Brian simulators.}

%global forgeurl https://github.com/NeuralEnsemble/PyNN

Name:           python-pynn
Version:        0.12.3

%global tag %{version}
%forgemeta

Release:        %autorelease
Summary:        A package for simulator-independent specification of neuronal network models


# SPDX
License:        CECILL-2.0
URL:            http://neuralensemble.org/PyNN/
Source:         %forgesource

# Random123 does not build on these, so neither can NEURON, so nothing that
# depends on NEURON supports them either
# https://github.com/neuronsimulator/nrn/issues/114
#
# python-pyedflib does not support s390x, so the complete dep tree needs to also exclude it
# https://src.fedoraproject.org/rpms/python-pyedflib/blob/rawhide/f/python-pyedflib.spec
#
# python-pynn: Build hangs on i686
# https://bugzilla.redhat.com/show_bug.cgi?id=2155635
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    mips64r2 mips32r2 s390x %{ix86}

# For extensions
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  ncurses-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  readline-devel

BuildRequires:  python3-brian2
BuildRequires:  python3-cheetah
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist lazyarray}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist morphio}
BuildRequires:  %{py3_dist neo}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist libneuroml}
BuildRequires:  python3-nest >= 3.7
BuildRequires:  nest-devel >= 3.7
BuildRequires:  nest >= 3.7
BuildRequires:  libneurosim-devel
BuildRequires:  python3-neuron
BuildRequires:  neuron-devel
BuildRequires:  %{py3_dist quantities}

BuildRequires:  %{py3_dist pytest}

%if %{with mpich}
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  python3-nest-mpich >= 3.7
BuildRequires:  nest-mpich >= 3.7
BuildRequires:  python3-neuron-mpich
BuildRequires:  rpm-mpi-hooks
BuildRequires:  mpich
BuildRequires:  mpich-devel
%endif

%if %{with openmpi}
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3-nest-openmpi >= 3.7
BuildRequires:  nest-openmpi >= 3.7
BuildRequires:  python3-neuron-openmpi
BuildRequires:  rpm-mpi-hooks
BuildRequires:  openmpi
BuildRequires:  openmpi-devel
%endif

Obsoletes:      python3-pynn-devel < 0:0.12.3-1

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-pynn
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-pynn %_description

%package doc
Summary:        %{summary}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%forgeautosetup
rm -rfv PyNN-%{version}/pyNN.egg-info

# we install NEST libraries in standard directories, and that's where NEST expects to find extensions also
sed -i 's|\${NEST_LIBDIR}/nest|\${NEST_LIBDIR}|' pyNN/nest/extensions/CMakeLists.txt

%build
# TODO: investigate using pyproject macros, or other new non setup.py tools
%py3_build

pushd ./build/lib/pyNN/neuron/nmodl/ || exit 1
    nrnivmodl .
popd
# The tests however, look for these here, so we also build them
pushd pyNN/neuron/nmodl || exit 1
    nrnivmodl .
popd

# NEST extensions: we build and install them ourselves
pushd ./build/lib/pyNN/nest/extensions/ || exit 1
    %cmake -Dwith-nest=%{_bindir}/nest-config
    %cmake_build
popd


%install
%py3_install

# Includes compiled arch specific files but installs in /lib
# Manually move to arch specific folder
%if "%{python3_sitelib}" != "%{python3_sitearch}"
mkdir -p 0644 $RPM_BUILD_ROOT/%{python3_sitearch}/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/pyNN $RPM_BUILD_ROOT/%{python3_sitearch}/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/PyNN-%{version}-py%{python3_version}.egg-info $RPM_BUILD_ROOT/%{python3_sitearch}/
%endif

# NEST extensions
pushd ./build/lib/pyNN/nest/extensions/ || exit 1
    %cmake_install
popd

# remove temporary build files
rm -rf $RPM_BUILD_ROOT%{python3_sitearch}/pyNN/nest/extensions/redhat-linux-build/
rm -rf $RPM_BUILD_ROOT%{python3_sitearch}/pyNN/nest/_build

%check
# skip pyNN.nest because it looks for nest extensions outside the buildroot
%py3_check_import pyNN pyNN.neuron pyNN.brian2

%pytest test/unittests -k "not test_partitioning and not test_get"

%if %{with mpich}
%{_mpich_load}
export PYTHONPATH=$PYTHONPATH:$RPM_BUILD_ROOT/%{python3_sitearch}:$RPM_BUILD_ROOT/%{python3_sitelib}:$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH:$MPI_PYTHON3_SITEARCH
%py3_check_import pyNN pyNN.nest pyNN.neuron pyNN.brian2

%pytest test/unittests

unset PYTHONPATH
%{_mpich_unload}
%endif

%if %{with openmpi}
%{_openmpi_load}
export PYTHONPATH=$PYTHONPATH:$RPM_BUILD_ROOT/%{python3_sitearch}:$RPM_BUILD_ROOT/%{python3_sitelib}:$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH:$MPI_PYTHON3_SITEARCH
%py3_check_import pyNN pyNN.nest pyNN.neuron pyNN.brian2

%pytest test/unittests

unset PYTHONPATH
%{_openmpi_unload}
%endif

# These files are NEURON files that are required by PyNN to run bits using the NEURON backend
# The libnrnmech.so file, along with the .libs/libnrnmech.so symlink are both required
# So is the "special" script that loads these libraries
# We can remove some temporary compilation files, though:
find $RPM_BUILD_ROOT/%{python3_sitearch}/pyNN/neuron/nmodl/*/ -name "*.c" -o -name "*.mod" -delete


%files -n python3-pynn
%license LICENSE
%doc README.rst AUTHORS changelog
%{_libdir}/*pynn*so
%{python3_sitearch}/pyNN
%{python3_sitearch}/PyNN-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%doc examples


%changelog
%autochangelog
