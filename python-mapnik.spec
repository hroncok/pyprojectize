%global srcname mapnik

%global commitdate 20240614
%global commit 248003c9da0de1ec7996cebd007c982f9875f2a3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global testcommit 41c4ceeb0be4e5e699cdd50bd808054a826c922b
%global visualcommit 7dfd4568d6181da8be3543c8b7522b596a79b774

%global mapnik_version 4.0.0

Name:           python-%{srcname}
Version:        3.0.23^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Python bindings for Mapnik

License:        LGPL-2.1-only
URL:            https://github.com/mapnik/python-mapnik
Source0:        https://github.com/mapnik/python-mapnik/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        https://github.com/mapnik/test-data/archive/%{testcommit}/test-data-%{testcommit}.tar.gz
Source2:        https://github.com/mapnik/test-data-visual/archive/%{visualcommit}/test-data-visual-%{visualcommit}.tar.gz
# Stop setup.py trying to fiddle with compiler flags
Patch:          python-mapnik-flags.patch
# Allow more variation in comparisons
Patch:          python-mapnik-precision.patch
# Use pkg-config instead of mapnik-config
Patch:          python-mapnik-pkgconfig.patch
# Fix for mapnik 4.0.0 compatiblity
Patch:          python-mapnik-mapnik4.patch
# Update test results for https://github.com/mapnik/mapnik/pull/4468
Patch:          python-mapnik-split-bbox.patch

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch:    ppc ppc64 s390 s390x

BuildRequires:  gcc-c++
BuildRequires:  sqlite-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-PyPDF2
BuildRequires:  python3-pybind11 pybind11-devel
BuildRequires:  python3-pytest

BuildRequires:  mapnik-devel >= %{mapnik_version}
BuildRequires:  mapnik-static >= %{mapnik_version}
BuildRequires:  mapnik-utils >= %{mapnik_version}

BuildRequires:  git-core
BuildRequires:  boost-devel boost-python3-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  postgresql-test-rpm-macros postgis

%description
%{summary}.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -S git -p 1 -n %{name}-%{commit}
tar --directory=test/data --strip-components=1 --gunzip --extract --file=%{SOURCE1} 
tar --directory=test/data-visual --strip-components=1 --gunzip --extract --file=%{SOURCE2} 


%build
export PYCAIRO=true
%py3_build


%install
%py3_install


%check
# start a postgres instance for the tests to use
PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
createdb template_postgis
psql -c "CREATE EXTENSION postgis" template_postgis
# run the tests
PGHOST="$PWD" LANG="C.UTF-8" %pytest test/python_tests


%files -n python3-%{srcname}
%doc README.md AUTHORS.md CHANGELOG.md CONTRIBUTING.md
%license COPYING
%{python3_sitearch}/*


%changelog
%autochangelog
