%global pypi_name microfs

Name:           python-%{pypi_name}
Version:        1.3.1

# no tests in sdist, no tags on github
%global commit 2fdfb2525889bf19f1f2d49c546f525855654fbc
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Release:        %autorelease
Summary:        CLI and Python module to work with BBC micro:bit filesystem

License:        MIT
URL:            https://github.com/ntoll/microfs
Source0:        %{url}/archive/%{commit}/%{pypi_name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pyserial
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%?python_enable_dependency_generator

%description
A simple command line tool and module for interacting with the limited file
system provided by MicroPython on the BBC micro:bit.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Provides:       %{pypi_name} == %{version}-%{release}
Provides:       ufs == %{version}-%{release}

%description -n python3-%{pypi_name}
A simple command line tool and module for interacting with the limited file
system provided by MicroPython on the BBC micro:bit.

%prep
%autosetup -n %{pypi_name}-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -vv tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/ufs
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
