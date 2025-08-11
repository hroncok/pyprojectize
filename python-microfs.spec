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

%description
A simple command line tool and module for interacting with the limited file
system provided by MicroPython on the BBC micro:bit.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Provides:       %{pypi_name} == %{version}-%{release}
Provides:       ufs == %{version}-%{release}

%description -n python3-%{pypi_name}
A simple command line tool and module for interacting with the limited file
system provided by MicroPython on the BBC micro:bit.

%prep
%autosetup -n %{pypi_name}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%{__python3} -m pytest -vv tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/ufs

%changelog
%autochangelog
