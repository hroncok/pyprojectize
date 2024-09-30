
%if 0%{?fedora} || 0%{?rhel} >= 8
%{!?python3_pkgversion: %global python3_pkgversion 3}
%else
%{!?python3_pkgversion: %global python3_pkgversion 34}
%endif

%global modname arrow

Name:               python-%{modname}
Version:            1.2.3
Release:            %autorelease
Summary:            Better dates and times for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:            Apache-2.0
URL:                https://pypi.io/project/arrow
Source0:            %pypi_source arrow
# This lets us drop a hard to port dep for py3 on epel7.
Patch0:             python-arrow-remove-simplejson-test.patch

BuildArch:          noarch

%description
Arrow is a Python library that offers a sensible, human-friendly approach to
creating, manipulating, formatting and converting dates, times, and timestamps.

It implements and updates the datetime type, plugging gaps in functionality,
and provides an intelligent module API that supports many common creation
scenarios.

Simply put, it helps you work with dates and times with fewer imports and a lot
less code.

%package -n         python%{python3_pkgversion}-%{modname}
Summary:            Better dates and times for Python

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-chai
BuildRequires:      python%{python3_pkgversion}-dateutil
BuildRequires:      python%{python3_pkgversion}-pytz
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-pytest-mock
BuildRequires:      python%{python3_pkgversion}-pytest-cov
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-simplejson
BuildRequires:      python%{python3_pkgversion}-dateparser

Requires:           python%{python3_pkgversion}-dateutil
Requires:           python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{modname}
Arrow is a Python library that offers a sensible, human-friendly approach to
creating, manipulating, formatting and converting dates, times, and timestamps.

It implements and updates the datetime type, plugging gaps in functionality,
and provides an intelligent module API that supports many common creation
scenarios.

Simply put, it helps you work with dates and times with fewer imports and a lot
less code.

%prep
%setup -q -n %{modname}-%{version}

# Don't enforce a certain coverage when we build the RPM, that's an upstream's
# problem
sed -i -e "s|--cov-fail-under=100 ||" tox.ini

#%patch0 -p1


# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l %{modname}

%check
pytest-%{python3_version} tests

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst

%changelog
%autochangelog
