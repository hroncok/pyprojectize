%if 0%{?fedora} || 0%{?rhel}
%bcond_without pyproject
%else
%bcond_with pyproject
%global __python3 /usr/bin/python3.11
%global python3_version 3.11
%endif

%global pypi_name aioquic

# as_needed flag breaks links to Python  
%undefine _ld_as_needed

Name:           python-%{pypi_name}
Version:        0.9.22
Release:        %autorelease
Summary:        %{pypi_name} is a library for the QUIC network protocol in Python
License:        BSD-3-Clause
URL:            https://github.com/aiortc/%{pypi_name}
Source0:        %{pypi_source}


%description
It features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.

QUIC was standardised in RFC 9000 and HTTP/3 in RFC 9114.
%{pypi_name} is regularly tested for interoperability against other
QUIC implementations.

It provides Python Decoder and Encoder objects
to read or write HTTP/3 headers compressed with QPACK.


%package -n python3-%{pypi_name}
Summary: %{pypi_name} is a library for the QUIC network protocol in Python
BuildRequires:  gcc
BuildRequires:  openssl-devel
%if %{with pyproject}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%else
BuildRequires:  python%{python3_version}-devel
BuildRequires:  python%{python3_version}-setuptools
BuildRequires:  python%{python3_version}-wheel
BuildRequires:  python%{python3_version}-pylsqpack
BuildRequires:  python%{python3_version}-pytest
Recommends:     python%{python3_version}-uvloop
%py_provides    python%{python3_version}-%{pypi_name}
%endif


%description -n python3-%{pypi_name}
It features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.

QUIC was standardised in RFC 9000 and HTTP/3 in RFC 9114.
%{pypi_name} is regularly tested for interoperability against other
QUIC implementations.

It provides Python Decoder and Encoder objects
to read or write HTTP/3 headers compressed with QPACK.


%prep
%autosetup -n %{pypi_name}-%{version}

rm -rf %{pypi_name}.egg-info
%if %{with pyproject}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
# Be sure Python lib is linked
export LDFLAGS="%{__global_ldflags} %(pkg-config --libs python3-embed)"
%if %{with pyproject}
%pyproject_wheel
%else
%pyproject_wheel
%endif


%check
%pyproject_check_import
%pytest


%install
%if %{with pyproject}
%pyproject_install
%pyproject_save_files %{pypi_name}
%else
%pyproject_install
%endif


%if %{with pyproject}
%files -n python3-%{pypi_name} -f %{pyproject_files}
%else
%files -n python3-%{pypi_name}
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}*.dist-info/
%license LICENSE
%endif
%doc README.rst


%changelog
%autochangelog
