%global pypi_name steam

Name:       python-%{pypi_name}
Version:    1.4.4
Release:    %autorelease
Summary:    Python package for interacting with Steam
BuildArch:  noarch

License:    MIT
URL:        https://github.com/ValvePython/steam

# Tests works only woth GitHub sources
Source0:    %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3-pyyaml >= 5.4

BuildRequires: python3dist(cachetools) >= 3.0.0
BuildRequires: python3dist(gevent-eventemitter) >= 2.1
BuildRequires: python3dist(gevent) >= 1.3.0
BuildRequires: python3dist(mock)
BuildRequires: python3dist(protobuf) >= 3.0.0
BuildRequires: python3dist(pycryptodomex) >= 3.7.0
BuildRequires: python3dist(pytest-cov)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(requests) >= 2.9.1
BuildRequires: python3dist(vcrpy)
BuildRequires: python3dist(vdf) >= 3.3

# For client
Requires:   python3dist(gevent-eventemitter) >= 2.1
Requires:   python3dist(gevent) >= 1.3.0
Requires:   python3dist(protobuf) >= 3.0.0

%global _description %{expand:
A python module for interacting with various parts of Steam.

Features

  - SteamClient - communication with the steam network based on gevent.
  - CDNClient - access to Steam content depots
  - WebAuth - authentication for access to store.steampowered.com and
    steamcommunity.com
  - WebAPI - simple API for Steam's Web API with automatic population of
    interfaces
  - SteamAuthenticator - enable/disable/manage two factor authentication for
    Steam accounts
  - SteamID - convert between the various ID representations with ease
  - Master Server Query Protocol - query masters servers directly or via
    SteamClient}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{python3} -m pytest -v


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst CHANGES.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-*.egg-info


%changelog
%autochangelog
