%global pypi_name torchdata

%bcond_with gitcommit
%if %{with gitcommit}
%global pypi_version 0.7.1
# Fixes are still happening in after 0.7.1
# ex/
# commit 07903385443da2cab8ed90c46bd4e02412945100
# Author: Danylo Baibak <baibak@meta.com>
# Date:   Fri Jan 26 01:12:03 2024 -0800
#
#    Forward fix / Update dill_available API for torchdata (#1222)
#
# Since torchtext depends on torchdata that depends on torch..
# we need to use the commit
%global commit0 66f0b984d4c3b2f7d715d8eb4e4cac5101bf7f08
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240327
%else
%global pypi_version 0.8.0
%endif

%bcond_with test

Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif

Release:        %autorelease
Summary:        A PyTorch module for data loading

License:        BSD-3-Clause
URL:            https://github.com/pytorch/data
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/data-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/data-%{version}.tar.gz
%endif
# Do not use git submodules
# Do not use distutils
Patch0:         0001-Prepare-torchdata-setup-for-fedora.patch


# Limit to these because that is what torch is on
ExclusiveArch:  x86_64 aarch64
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(urllib3)

%description
torchdata is a library of common modular data loading primitives for
easily constructing data pipelines.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
torchdata is a library of common modular data loading primitives for
easily constructing data pipelines.

%prep
%if %{with gitcommit}
%autosetup -p1 -n data-%{commit0}
%else
%autosetup -p1 -n data-%{version}
%endif

rm -rf third_party/*

# pyproject_ is broken it is generate_buildrequires looks for
# python3-cmake and python3-ninja, revert to old py3_

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Testing has a circular dependency
# E   ModuleNotFoundError: No module named 'torchtext'
# We need torchdata to build torchtext :(
%if %{with test}
%check
%pytest
%endif

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
