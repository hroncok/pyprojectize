%global pypi_name admesh

Name:           python-%{pypi_name}
Version:        0.98.9
Release:        %autorelease
Summary:        Python bindings for ADMesh, STL manipulation library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/admesh/python-admesh
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# https://github.com/admesh/python-admesh/issues/15
Source1:        %{url}/raw/v%{version}/test/utils.py

BuildRequires:  gcc

BuildRequires:  admesh-devel >= 0.98

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest-runner

%description
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.

%package -n     python3-%{pypi_name}
Summary:        Python 3 bindings for ADMesh, STL manipulation library
%{?python_provide:%python_provide python3-%{pypi_name}}

Obsoletes:      python2-%{pypi_name} < 0.98.8-2
Obsoletes:      python-%{pypi_name} < 0.98.8-2

%description -n python3-%{pypi_name}
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.


%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} test/

%build
%py3_build


%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-3 -v \
%ifarch ppc64
  -k "not test_saved_equals_original_binary" # likely a bug in admesh itself
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%attr(0755,root,root) %{python3_sitearch}/%{pypi_name}.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
