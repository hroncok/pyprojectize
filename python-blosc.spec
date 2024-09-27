Name:           python-blosc
Summary:        Python wrapper for the Blosc high performance compressor
Version:        1.11.2
Release:        %autorelease
License:        BSD-3-Clause
URL:            https://github.com/Blosc/python-blosc
Source0:        https://github.com/Blosc/python-blosc/archive/v%{version}/blosc-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Blosc/python-blosc/f3c5e341a2504a03c225f4f1d9066ccdf4bd31dd/setup.py

BuildRequires:  gcc
BuildRequires:  blosc-devel >= 1.16.0
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-cpuinfo

%description
%{summary}.

%package -n python%{python3_pkgversion}-blosc
Summary:        Python wrapper for the blosc high performance compressor
Requires:       blosc%{_isa} >= 1.16.0

%{?python_provide:%python_provide python%{python3_pkgversion}-blosc}
%{?fedora:Recommends: python%{python3_pkgversion}-numpy}

%description -n python%{python3_pkgversion}-blosc
%{summary}.

%prep
%autosetup -p1

# Overwrite setup.py with the last version that does not use skbuild and cmake
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
export BLOSC_DIR=%{_libdir}/blosc CFLAGS="%{optflags}"
export DISABLE_BLOSC_AVX2=1
%pyproject_wheel

%install
%pyproject_install

%check
cd / # avoid interference with build dir
PYTHONPATH=%{buildroot}%{python3_sitearch} %__python3 -c 'import sys, blosc; sys.exit(blosc.test())'

%files -n python%{python3_pkgversion}-blosc
%{python3_sitearch}/blosc/
%{python3_sitearch}/blosc-%{version}*.dist-info
%license LICENSE.txt
%doc README.rst RELEASE_NOTES.rst

%changelog
%autochangelog
