# main package is archful to run tests everywhere but produces noarch packages
%global debug_package %{nil}
%bcond_without check
%global pname mrcfile

%global desc \
mrcfile is a Python implementation of the MRC2014 file format, which is used in\
structural biology to store image and volume data.\
\
It allows MRC files to be created and opened easily using a very simple API,\
which exposes the file's header and data as numpy arrays. The code runs in\
Python 2 and 3 and is fully unit-tested.\
\
This library aims to allow users and developers to read and write\
standard-compliant MRC files in Python as easily as possible, and with no\
dependencies on any compiled libraries except numpy. You can use it\
interactively to inspect files, correct headers and so on, or in scripts and\
larger software packages to provide basic MRC file I/O functions.

Name: python-%{pname}
Version: 1.5.3
Release: %autorelease
Summary: MRC2014 file format used in structural biology to store image and volume data
License: BSD-3-Clause
URL: https://github.com/ccpem/%{pname}
Source: https://github.com/ccpem/%{pname}/archive/v%{version}/%{pname}-%{version}.tar.gz

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{with check}
BuildRequires: python3-numpy
%endif
%{?python_provide:%python_provide python3-%{pname}}
BuildArch: noarch

%description -n python3-%{pname}
%{desc}

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
PYTHONDONTWRITEBYTECODE=1 \
PATH=%{buildroot}/usr/bin:${PATH} \
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} \
python3 -m unittest tests
%endif

%files -n python3-%{pname}
%license LICENSE.txt
%doc CHANGELOG.txt README.rst
%{_bindir}/mrcfile-header
%{_bindir}/mrcfile-validate
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pname}

%changelog
%autochangelog
