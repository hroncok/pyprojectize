%global srcname minidb

Name:           python-%{srcname}
Version:        2.0.8
Release:        %autorelease
Summary:        Simple python object store

License:        ISC
URL:            https://github.com/thp/minidb
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
minidb 2 makes it easy to store Python objects in a SQLite 3 database and
work with the data in an easy way with concise syntax.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
minidb 2 makes it easy to store Python objects in a SQLite 3 database and
work with the data in an easy way with concise syntax.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -v test

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}.py*
%{python3_sitelib}/%{srcname}*.egg-info
%{python3_sitelib}/__pycache__/*

%changelog
%autochangelog

