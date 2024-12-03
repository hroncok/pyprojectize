%if 0%{?rhel}
%bcond_with docs
%else
%bcond_without docs
%endif
%bcond_without tests

%global pypi_name drgn

%global _description %{expand:
drgn (pronounced "dragon") is a debugger with an emphasis on programmability.
drgn exposes the types and variables in a program for easy, expressive
scripting in Python.}

Name:           python-%{pypi_name}
Version:        0.0.27
Release:        %autorelease
Summary:        Programmable debugger

License:        LGPL-2.1-or-later
URL:            https://github.com/osandov/drgn
Source0:        %{pypi_source}

BuildRequires:  python3-devel
%if %{with docs}
BuildRequires:  sed
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-docs
%endif
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  bzip2-devel
BuildRequires:  elfutils-devel
BuildRequires:  libkdumpfile-devel
BuildRequires:  zlib-devel
BuildRequires:  xz-devel
# These are needed when building from git snapshots
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description %{_description}

%package -n     %{pypi_name}
Summary:        %{summary}

%description -n %{pypi_name} %{_description}

%if %{with docs}
%package -n %{pypi_name}-doc
Summary:        %{pypi_name} documentation
BuildArch:      noarch
Requires:       python3-docs

%description -n %{pypi_name}-doc %{_description}

This package contains additional documentation for %{pypi_name}.
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -p1
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif
# Ensure version is always set, even when building from git snapshots
if [ ! -f drgn/internal/version.py ]; then
  echo '__version__ = "%{version}"' > drgn/internal/version.py
fi

%generate_buildrequires
%pyproject_buildrequires

%build
# verbose build
export V=1
%pyproject_wheel

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name} _%{pypi_name}
mkdir -p %{buildroot}%{_datadir}/drgn
cp -PR contrib tools %{buildroot}%{_datadir}/drgn

%if %{with tests}
%check
%pyproject_check_import

%pytest
%endif

%files -n %{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/drgn
%{_datadir}/drgn

%if %{with docs}
%files -n %{pypi_name}-doc
%license COPYING
%license LICENSES
%doc html
%endif

%changelog
%autochangelog
