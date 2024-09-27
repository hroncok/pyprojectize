%bcond_without check
%global pname mmtf-python

%global desc \
The Macromolecular Transmission Format (MMTF) is a new compact binary format to\
transmit and store biomolecular structures for fast 3D visualization and\
analysis.\
\
Bradley AR, Rose AS, Pavelka A, Valasatava Y, Duarte JM, Prlić A, Rose PW (2017)\
MMTF - an efficient file format for the transmission, visualization, and\
analysis of macromolecular structures. bioRxiv 122689. doi: 10.1101/122689\
\
Valasatava Y, Bradley AR, Rose AS, Duarte JM, Prlić A, Rose PW (2017) Towards an\
efficient compression of 3D coordinates of macromolecular structures. PLOS ONE\
12(3): e0174846. doi: 10.1371/journal.pone.01748464\
\
Rose AS, Bradley AR, Valasatava Y, Duarte JM, Prlić A, Rose PW (2016) Web-based\
molecular graphics for large complexes. In Proceedings of the 21st International\
Conference on Web3D Technology (Web3D '16). ACM, New York, NY, USA, 185-186.\
doi: 10.1145/2945292.2945324\


Name: python-mmtf
Version: 1.1.3
Release: %autorelease
Summary: A decoding library for the macromolecular transmission format (MMTF) 
License: Apache-2.0
URL: https://github.com/rcsb/mmtf-python
Source0: https://files.pythonhosted.org/packages/source/m/%{pname}/%{pname}-%{version}.tar.gz
BuildArch: noarch

%description
%{desc}

%package -n python3-mmtf
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{with check}
BuildRequires: python3-msgpack
BuildRequires: python3-pytest
BuildRequires: python3-numpy
%endif
%{?python_provide:%python_provide python3-mmtf}
Requires: python3-msgpack

%description -n python3-mmtf
%{desc}

%prep
%setup -q -n %{pname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%pytest mmtf/tests/codec_tests.py
%endif

%files -n python3-mmtf
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{python3_sitelib}/mmtf_python-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/mmtf

%changelog
%autochangelog
