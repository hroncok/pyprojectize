%global srcname mirrors-countme
%global pkgname mirrors_countme

%if !0%{?fedora}%{?rhel} || 0%{?fedora} >= 38 || 0%{?rhel} >= 10
%bcond_without auto_buildrequires
%bcond_without poetry_compatible
%else
# Poetry in Fedora < 38, EL < 10 is too old
%bcond_with auto_buildrequires
%bcond_with poetry_compatible
%endif

# EL < 10 needs a non-default Python version and misses the hypothesis package
%if 0%{?rhel} && 0%{?rhel} < 10
%bcond_with tests
%global python3_pkgversion 3.11
%global __python3 %{_bindir}/python%{python3_pkgversion}
%if %{undefined pyproject_files}
%global pyproject_files %{_builddir}/%{name}-%{version}-%{release}.%{_arch}-pyproject-files
%endif
%else
%bcond_without tests
%endif

Name:    python-%{srcname}
Version: 0.1.4
Release: %autorelease
Summary: Parse access_log and count hosts accessing DNF mirrors
URL:     https://github.com/fedora-infra/mirrors-countme
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Source0: https://github.com/fedora-infra/mirrors-countme/releases/download/%{version}/%{pkgname}-%{version}.tar.gz
BuildArch: noarch
# Not quite sure what minimum sqlite version we need, but scripts use
# /usr/bin/sqlite3 and the python module is "sqlite3", so...
Requires: sqlite >= 3.0.0

%global _description %{expand:
A python module and scripts for parsing httpd access_log to find requests
including `countme=N`, parse the data included with those requests, and
compile weekly counts of DNF clients broken out by OS name, OS version,
system arch, etc.}

# This is for the toplevel metapackage.
%description %_description


# This section defines the python3-mirrors-countme subpackage.
%package -n python%{python3_pkgversion}-%{srcname}
Summary: %{summary}
BuildRequires: python%{python3_pkgversion}-devel
%if ! %{with auto_buildrequires}
%endif
%if %{with tests}
BuildRequires: glibc-langpack-en
BuildRequires: python%{python3_pkgversion}-hypothesis
BuildRequires: python%{python3_pkgversion}-pytest
BuildRequires: python%{python3_pkgversion}-pytest-cov
BuildRequires: python%{python3_pkgversion}-pytest-xdist
%endif

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
%autosetup -n %{pkgname}-%{version}

%if %{with auto_buildrequires}
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if %{with poetry_compatible}
%pyproject_wheel
%else
%py3_build
%endif

%install
%if %{with poetry_compatible}
%pyproject_install
%pyproject_save_files %{pkgname}
%else
%py3_install

pushd %{buildroot}
find "./%{python3_sitelib}/%{pkgname}"* -type d | while read d; do
    echo "%dir ${d#./}"
done > %{pyproject_files}
find "./%{python3_sitelib}/%{pkgname}"* -type f | while read f; do
    echo "${f#./}"
done >> %{pyproject_files}
popd
%endif

for script in update-rawdb update-totals sqlite2csv split-totals-db; do
    install -m0755 "scripts/countme-${script}.sh" "%{buildroot}%{_bindir}/"
done

install -m0755 "scripts/countme-rezip" "%{buildroot}%{_bindir}/"

%check
%pyproject_check_import

%if %{with tests}
PYTHONPATH="%{buildroot}%{python3_sitelib}" %{python3} -m pytest -v -n auto
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/countme-delete-totals
%{_bindir}/countme-parse-access-log
%{_bindir}/countme-totals
%{_bindir}/countme-trim-raw
%{_bindir}/countme-update-rawdb.sh
%{_bindir}/countme-update-totals.sh
%{_bindir}/countme-sqlite2csv.sh
%{_bindir}/countme-split-totals-db.sh
%{_bindir}/countme-rezip

%changelog
%autochangelog
