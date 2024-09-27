# Created by pyp2rpm-3.3.2

%global srcname flask-caching

Name:           python-%{srcname}
Version:        2.3.0
Release:        %autorelease
Summary:        Adds caching support to your Flask application

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sh4nks/flask-caching
Source0:        https://github.com/sh4nks/%{srcname}/archive/v.%{version}/%{srcname}-v.%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(asgiref)
BuildRequires:  python3dist(cachelib)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(pylibmc)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-xprocess)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(redis)
BuildRequires:  redis
BuildRequires:  python3dist(sphinx)

%description
Flask-Caching Adds easy cache support to Flask

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(flask)
%description -n python3-%{srcname}
Flask-Caching Adds easy cache support to Flask

%package -n python-%{srcname}-doc
Summary:        Flask-Caching documentation
%description -n python-%{srcname}-doc
Documentation for Flask-Caching

%prep
%autosetup -n %{srcname}-v.%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Patch out too tight cachilib upper pin
sed -i 's/cachelib >= 0.9.0, < 0.10.0"/cachelib >= 0.9.0"/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build

%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
redis-server &
%pytest
kill %1

%files -n python3-%{srcname}
%license LICENSE docs/license.rst
%doc README.rst
%{python3_sitelib}/flask_caching
%{python3_sitelib}/Flask_Caching-%{version}.dist-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE docs/license.rst

%changelog
%autochangelog
