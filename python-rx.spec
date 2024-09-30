# what it's called on pypi
%global srcname Rx
# what it's imported as
%global libname rx
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%global _description \
Rx is a library for composing asynchronous and event-based programs using\
observable collections and LINQ-style query operators in Python.

%bcond_without tests


Name:           python-%{pkgname}
Version:        3.2.0
Release:        %autorelease
Summary:        Reactive Extensions (Rx) for Python
License:        MIT
URL:            https://github.com/ReactiveX/RxPY
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/ReactiveX/RxPY/pull/570
Patch0:         0001-Set-daemon-attribute-instead-of-using-setDaemon-meth.patch
# https://github.com/ReactiveX/RxPY/pull/575
Patch1:         0002-Remove-deprecated-loop-parameter.patch
# Python 3.11 compatibility: replace coroutine decorator with async keyword
Patch3:         https://github.com/ReactiveX/RxPY/commit/a4e84d8a488d6c7c75bdb09f6d6f08edcb2b23b0.patch

BuildArch:      noarch


%description %{_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-coverage
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-runner


%description -n python3-%{pkgname} %{_description}


%prep
%autosetup -n RxPY-%{version} -p 1
rm -rf %{eggname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%if %{with tests}
%check
%pytest --verbose
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst authors.txt changes.md
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}.dist-info


%changelog
%autochangelog
