%bcond_without tests

Name:           python-pycparser
Summary:        C parser and AST generator written in Python
Version:        2.20
Release:        %autorelease
License:        BSD-3-Clause
URL:            http://github.com/eliben/pycparser
Source0:        %{url}/archive/release_v%{version}.tar.gz
Source1:        pycparser-0.91.1-remove-relative-sys-path.py

# This is Fedora-specific; I don't think we should request upstream to
# remove embedded libraries from their distribution, when we can remove
# them during packaging.
# It also ensures that pycparser uses the same YACC __tabversion__ as ply
# package to prevent "yacc table file version is out of date" problem.
Patch100:       pycparser-unbundle-ply.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-ply

# for unit tests
%if %{with tests}
BuildRequires:  cpp
%endif

%description
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.

%package -n python3-pycparser
Summary:        %{summary}

%description -n python3-pycparser
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.

%prep
%autosetup -p1 -n pycparser-release_v%{version}

# remove embedded copy of ply
rm -r pycparser/ply

# Remove relative sys.path from the examples
%{python3} %{SOURCE1} examples

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd build/lib/pycparser
%{python3} _build_tables.py
popd

%install
%pyproject_install
%pyproject_save_files -l pycparser

%check
%pyproject_check_import

%if %{with tests}
%{python3} tests/all_tests.py
%endif
 
%files -n python3-pycparser -f %{pyproject_files}
%doc examples

%changelog
%autochangelog
