#global commit 16191801a53eddae8ca9380a28988c3b5b263c5e
%{?gitcommit:%global gitcommitshort %(c=%{gitcommit}; echo ${c:0:7})}

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Summary:        HDF5 support in Python
Name:           python-tables
Version:        3.10.1
Release:        %autorelease
#Source0:        https://github.com/PyTables/PyTables/archive/%{commit}/PyTables-%{commit}.tar.gz
Source0:        https://github.com/PyTables/PyTables/archive/v%{version}/python-tables-%{version}.tar.gz

# sometimes it doesn't get updated
%global manual_version 3.3.0

%bcond tests 1

Source1:        https://github.com/PyTables/PyTables/releases/download/v%{manual_version}/pytablesmanual-%{manual_version}.pdf

# https://github.com/PyTables/PyTables/issues/735
Patch1:         0001-Skip-tests-that-fail-on-s390x.patch

Patch3:         0001-Skip-failing-test.patch

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://www.pytables.org

BuildRequires:  hdf5-devel >= 1.8
BuildRequires:  bzip2-devel
BuildRequires:  lzo-devel
BuildRequires:  blosc-devel
BuildRequires:  blosc2-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-blosc2
BuildRequires:  python%{python3_pkgversion}-Cython >= 0.13
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-numexpr >= 2.4
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-typing-extensions

ExcludeArch:    %{ix86}

%global _description %{expand:
PyTables is a package for managing hierarchical datasets and designed
to efficiently and easily cope with extremely large amounts of data.}

%description %_description

%package -n python%{python3_pkgversion}-tables
Summary:        %{summary}

Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-numexpr >= 2.4

%description -n python%{python3_pkgversion}-tables %_description

%package        doc
Summary:        Documentation for PyTables
BuildArch:      noarch

%description doc
The %{name}-doc package contains the documentation for %{name}.

%prep
%autosetup -p1 -n PyTables-%{version}
cp -a %{SOURCE1} pytablesmanual.pdf

# Make sure we are not using anything from the bundled blosc by mistake
find c-blosc -mindepth 1 -maxdepth 1 -name hdf5 -prune -o -exec rm -r {} +

# circumvent the broken attempt to detect library location
sed -r -i \
  '/def get_blosc2_directories\(\):/a \ \ \ \ return Path("%{_includedir}"),Path("%{_libdir}"),None' \
  setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
chmod -x examples/check_examples.sh
sed -i 's|bin/env |bin/|' utils/*

%pyproject_install
%pyproject_save_files tables

%check
%if %{with tests}
%ifarch %{ix86} s390x
skip=true
%else
skip=false
%endif

cd /
PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} -m tables.tests.test_all -v || $skip
%endif

%files -n python%{python3_pkgversion}-tables -f %{pyproject_files}
%license LICENSE.txt LICENSES
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{_bindir}/pt2to3
%{_bindir}/pttree

%files doc
%license LICENSE.txt LICENSES
%doc pytablesmanual.pdf
%doc [A-KM-Za-z]*.txt
%doc examples/

%changelog
%autochangelog
