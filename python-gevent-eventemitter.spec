%global pypi_name gevent-eventemitter
%global modname eventemitter
%global eggname gevent_%{modname}

Name:       python-%{pypi_name}
Version:    2.1
Release:    %autorelease
Summary:    EventEmitter using gevent
BuildArch:  noarch

# https://github.com/rossengeorgiev/gevent-eventemitter/pull/3
License:    MIT

URL:        https://github.com/rossengeorgiev/gevent-eventemitter

# Tests works only woth GitHub sources
Source0:    %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3dist(coverage) >= 4.0.3
BuildRequires: python3dist(gevent) >= 1.3
BuildRequires: python3dist(pytest-cov) >= 2.5.1
BuildRequires: python3dist(pytest) >= 3.2.1

%global _description %{expand:
This module implements EventEmitter with gevent.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pyproject_check_import

%{python3} -m pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%dnl %license LICENSE
%doc README.rst


%changelog
%autochangelog
