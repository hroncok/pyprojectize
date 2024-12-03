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
BuildRequires:  python3-pytest

%description -n python3-%{srcname}
minidb 2 makes it easy to store Python objects in a SQLite 3 database and
work with the data in an easy way with concise syntax.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

%pytest -v test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

