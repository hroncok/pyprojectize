%global pkgname nmrglue
%global pkgsum Python module for processing NMR data

Name:		python-%{pkgname}
Version:	0.9
Release:	%autorelease
Summary:	%{pkgsum}

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/jjhelmus/%{pkgname}
Source0:	https://github.com/jjhelmus/%{pkgname}/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
# these are required for tests
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy

%description
nmrglue is a module for working with NMR data in Python. When used with the 
numpy, scipy, and matplotlib packages nmrglue provides a robust interpreted 
environment for processing, analyzing, and inspecting NMR data.

%package -n python3-%{pkgname}
Summary:	%{pkgsum}
Requires:	python3-numpy
Requires:	python3-scipy

%description -n python3-%{pkgname}
nmrglue is a module for working with NMR data in Python. When used with the 
numpy, scipy, and matplotlib packages nmrglue provides a robust interpreted 
environment for processing, analyzing, and inspecting NMR data.

%prep
%autosetup -n %{pkgname}-%{version}

# disable tests bundling
sed -i '/nmrglue.fileio.tests/d' setup.py
sed -i '/package_data/d' setup.py
sed -i '/fileio\/tests\/data\//d' setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

%check
%pyproject_check_import


pushd nmrglue/fileio/tests

#python3 tests
PYTHONPATH="%{buildroot}%{python3_sitelib}" %{__python3} test_pipe.py

popd

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst TODO.txt

%changelog
%autochangelog
