%bcond tests 1

Name:           python-crc32c
Version:        2.7.post1
Release:        %autorelease
Summary:        A python package implementing the crc32c algorithm in hardware and software

License:        LGPL-2.1-or-later
URL:            https://github.com/ICRAR/crc32c
Source:         %{url}/archive/refs/tags/v%{version}/crc32c-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This package implements the crc32c checksum algorithm. It automatically
chooses between a hardware-based implementation (using theCRC32C SSE
4.2 instruction of Intel CPUs, and the crc32* instructions on ARMv8
CPUs), or a software-based one when no hardware support can be found.}

%description %{_description}


%package -n python3-crc32c
Summary:        %{summary}

%description -n python3-crc32c %{_description}


%prep
%autosetup -n crc32c-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x testing}


%build
%py3_build


%install
%py3_install


%check
%py3_check_import crc32c

%if %{with tests}
%pytest
PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} run-tests.py
%endif


%files -n python3-crc32c
%doc CHANGELOG.md
%license LICENSE
%license LICENSE.google-crc32c
%license LICENSE.slice-by-8
%doc README.rst

%{python3_sitearch}/crc32c/
%{python3_sitearch}/crc32c-%{version}-*.egg-info

%changelog
%autochangelog
