Name:           python-pefile
Version:        2024.8.26
Release:        %autorelease
Summary:        Python module for working with Portable Executable files
License:        MIT
URL:            https://github.com/erocarrera/pefile


%global srcname pefile

%global common_desc pefile is a multi-platform Python module to read and work with Portable\
Executable (aka PE) files. Most of the information in the PE Header is \
accessible, as well as all the sections, section's information and data.\
pefile requires some basic understanding of the layout of a PE file. Armed \
with it it's possible to explore nearly every single feature of the file.\
Some of the tasks that pefile makes possible are:\
* Modifying and writing back to the PE image\
* Header Inspection\
* Sections analysis\
* Retrieving data\
* Warnings for suspicious and malformed values\
* Packer detection with PEiD’s signatures\
* PEiD signature generation\


# Source tarball contains 60+ MB of potentially malicious EXE files as tests
#Source0:        https://github.com/erocarrera/%%{srcname}/archive/v%%{version}.tar.gz#/%%{srcname}-%%{version}.tar.gz

# Release tarball contains only the functionality
Source0:        https://github.com/erocarrera/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

# For the patch
# BuildRequires: git-core

%description
%{common_desc}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname}
%{common_desc}


%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' pefile.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

%check
%pyproject_check_import

%py3_check_import pefile peutils ordlookup
# regression tests in this package are based on binary blob of exe files - commercial and malware
# at this point (2019-09-20) not suitable to be in Fedora.
# More info on:
# https://github.com/erocarrera/pefile/issues/171
# https://github.com/erocarrera/pefile/issues/82#issuecomment-192018385
# %%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
# TODO ... README missing in the 2024.8.26 release, should check with next version
#%%doc README*

%changelog
%autochangelog