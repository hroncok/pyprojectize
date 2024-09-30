%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.

# We do not generate docs, due to the missing dependencies
%bcond_without doc_pdf

%global pypi_name pyunicorn
%global forgeurl https://github.com/pik-copan/pyunicorn
%global commit master
%global upstream_version 0.7.0a1

%global _description %{expand:
pyunicorn (Unified Complex Network and RecurreNce analysis toolbox)
is a fully object-oriented Python package for the advanced
analysis and modeling of complex networks. Above the standard measures
of complex network theory such as degree, betweenness and clustering 
coefficient it provides some uncommon but interesting statistics like 
Newman's random walk betweenness. pyunicorn features novel node-weighted
(node splitting invariant) network statistics as well as measures 
designed for analyzing networks of interacting/interdependent networks.}

Name:           python-%{pypi_name}

%forgemeta

# Set version to preliminary version defined in setup.cfg
Version:        0.7.0~a1
Release:        %{autorelease}
Summary:        Unified complex network and recurrence analysis toolbox

# The entire source code is BSD except the following files:
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/__init__.py
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/compat.py
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/progressbar.py
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/widgets.py
# Automatically converted from old format: BSD and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.pik-potsdam.de/~donges/pyunicorn/
Source0:        %{forgesource}

# patch intended for skipping two tests due to the failed attempts on i686
#Patch0:         0001-Skip-test.patch

# patch removes two badges that are in svg format
# it resolves problems with building docs
#Patch1:         0002-Remove-badges-in-README.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  Cython

BuildRequires:  python3-igraph
BuildRequires:  numpy
BuildRequires:  python3-networkx
BuildRequires:  python3-basemap
BuildRequires:  python3-scipy

Requires:  matplotlib

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-cartopy
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation and examples for %{name}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{commit}
for lib in $(find . -name "*.py"); do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
# Disable coverage and fix pytest command (has no option '-n')
sed -i -e 's/-n auto //' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# We run this in %%install, since Sphinx imports __version__ from pyunicorn.
# So, that needs to be installed first.
%if %{with doc_pdf}
%{py3_test_envvars} %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%{py3_test_envvars} %make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst examples/
%license LICENSE.txt

%files doc
%doc README.rst
%license LICENSE.txt
%if %{with doc_pdf}
%doc docs/build/latex/%{pypi_name}.pdf
%endif

%changelog
%autochangelog
