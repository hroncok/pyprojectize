%global srcname more-executors
%global srcname_py more_executors

Summary: A library of composable Python executors and futures
Name: python-%{srcname}
Version: 2.11.4
Release: %autorelease
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
BuildArch: noarch
URL: https://github.com/rohanpm/%{srcname}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

%{?python_enable_dependency_generator}

%description
This library is intended for use with the concurrent.futures module.
It includes a collection of Executor implementations in order to extend
the behavior of Future objects.

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

# dependencies for test suite
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pyhamcrest)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(mypy)

%{?python_provide:%python_provide python3-%{srcname}}

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.egg-info prometheus}

%description -n python3-%{srcname}
This library is intended for use with the concurrent.futures module.
It includes a collection of Executor implementations in order to extend
the behavior of Future objects.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -v

%files -n python3-%{srcname}
%doc README.md
%license LICENSE

%{python3_sitelib}/%{srcname_py}*.egg-info/
%{python3_sitelib}/%{srcname_py}/

%changelog
%autochangelog
