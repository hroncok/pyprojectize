%global srcname pyopencl

Name:           python-%{srcname}
Version:        2024.1
Release:        %autorelease
Summary:        Python wrapper for OpenCL

# https://bugzilla.redhat.com/show_bug.cgi?id=1219819#c16
# Boost (boost):
# pyopencl/cl/pyopencl-bessel-j.cl
# pyopencl/cl/pyopencl-bessel-y.cl
# pyopencl/cl/pyopencl-eval-tbl.cl
# GPLv2 (cephes):
# pyopencl/cl/pyopencl-airy.cl
# ASL 2.0 (ranluxcl), will be removed in 2018.x:
# pyopencl/cl/pyopencl-ranluxcl.cl
# ASL 2.0:
# pyopencl/scan.py
# BSD (random123):
# pyopencl/cl/pyopencl-random123/array.h
# pyopencl/cl/pyopencl-random123/openclfeatures.h
# pyopencl/cl/pyopencl-random123/philox.cl
# pyopencl/cl/pyopencl-random123/threefry.cl
# BSD:
# pyopencl/bitonic_sort.py
# pyopencl/bitonic_sort_templates.py

# Automatically converted from old format: MIT and Boost and ASL 2.0 and GPLv2 and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND BSL-1.0 AND Apache-2.0 AND GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            https://mathema.tician.de/software/pyopencl
Source0:        %{pypi_source}
Patch1:         0001-disable-executing-git-submodule.patch
# Have not asked upstream, but they want to enforce CFLAGS/LDFLAGS
Patch2:         0002-don-t-hack-distutils-with-C-LDFLAGS.patch

# pyopencl/cl/pyopencl-bessel-[j,y].cl and
# pyopencl/cl/pyopencl-eval-tbl.cl contain snippets taken from boost
# and cephes. pyopencl/cl/pyopencl-airy.cl contains code taken from
# cephes.
Provides:       bundled(boost-math)
Provides:       bundled(cephes) = 2.8
# pyopencl/cl/pyopencl-ranluxcl.cl contains a modified version of the
# ranluxcl library
Provides:       bundled(ranluxcl) = 1.3.1
# ./pyopencl/compyte/*
Provides:       bundled(compyte)

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  opencl-headers
BuildRequires:  ocl-icd-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(gl)

%description
PyOpenCL makes it possible to access GPUs and other massively\
parallel compute devices from Python. Specifically, PyOpenCL\
provides Pythonic access to the OpenCL parallel computation\
API in a manner similar to the sister project `PyCUDA`.

%package -n python3-%{srcname}
Summary:        Python 3 wrapper for OpenCL
BuildRequires:  python3-devel
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(zombie-imp)
Recommends:     python3dist(Mako)

%description -n python3-%{srcname}
Python 3 version of python-pyopencl.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vrf *.egg-info
rm -vf examples/download-examples-from-wiki.py

# generate html docs
#sphinx-build doc/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%generate_buildrequires
%pyproject_buildrequires

%build
%{__python3} configure.py --cl-enable-gl --cl-pretend-version=1.2
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

find %{buildroot}%{python3_sitearch}/%{srcname} -name '*.so' -exec chmod 755 {} \+

%files -n python3-%{srcname} -f %{pyproject_files}
%doc examples

%changelog
%autochangelog
