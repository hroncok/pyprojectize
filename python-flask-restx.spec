# what it's called on pypi
%global srcname flask-restx
# what it's imported as
%global libname flask_restx

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Framework for fast, easy and documented API development with Flask
License:        BSD-3-Clause
URL:            https://github.com/python-restx/flask-restx
Source0:        %{pypi_source %srcname}
Patch0:         0001-Use-importlib.resources.patch
BuildArch:      noarch

%global _description %{expand:
Flask-RESTX is an extension for Flask that adds support for quickly
building REST APIs. It encourages best practices with minimal setup.
If you are familiar with Flask, Flask-RESTX should be easy to pick up.
It provides a coherent collection of decorators and tools to describe your API
and expose its documentation properly using Swagger.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:       python3-flask-restplus = %{version}-%{release}
# Using < or <= would obsolete ourselves
Obsoletes:      python3-flask-restplus = 0.13.0
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{libname}.egg-info
rm -f %{libname}/static/files/.npmignore

%build
%py3_build

%install
%py3_install

# Upstream requires pinned dependencies versions
#%%check
#%%tox

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{libname}-*.egg-info/


%changelog
%autochangelog
