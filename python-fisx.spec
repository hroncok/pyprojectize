Name:           python-fisx
Version:        1.3.2
Release:        %autorelease
Summary:        Calculate X-ray fluorescence intensities

# This is SPDX
License:        MIT
URL:            https://github.com/vasole/fisx
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  %py3_dist cython
BuildRequires:  %py3_dist numpy

%global _description %{expand:
Calculate expected x-ray fluorescence intensities. The library accounts
for secondary and tertiary excitation, K, L and M shell emission lines
and de-excitation cascade effects.}

%description %_description

%package     -n python3-fisx
Summary: %summary

%description -n python3-fisx %_description

%prep
%autosetup -n fisx-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fisx

%check
%pyproject_check_import
PYTHONPATH=%{buildroot}%{python3_sitearch} %python3 -m fisx.tests.testAll

%files -n python3-fisx -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
