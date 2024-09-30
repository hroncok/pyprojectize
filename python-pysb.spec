# Documentation cannot be built on epel7, python-numpydoc is missing
%bcond doc 0%{?fedora}

# Use the same directory of the main package for subpackage licence and doc
%global _docdir_fmt %{name}

%global forgeurl https://github.com/pysb/pysb

Name:           python-pysb
Version:        1.16.0
Release:        %autorelease
Summary:        Rule-based modeling of biochemical systems as Python programs
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pysb.org/
%forgemeta
# https://github.com/pysb/pysb/issues/555
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  python3-devel
%if %{with doc}
# For building documentation
BuildRequires:  dvipng
BuildRequires:  python3-sphinx
BuildRequires:  tex(latex)
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3-ipython-sphinx
%endif

%global _description %{expand:
PySB is a framework for building mathematical models of biochemical
systems as Python programs. PySB abstracts the complex process of
creating equations describing interactions among multiple proteins or
other biomolecules into a simple and intuitive domain specific
programming language, which is internally translated into BioNetGen or
Kappa rules and from there into systems of equations. PySB makes it
straightforward to divide models into modules and to call libraries of
reusable elements (macros) that encode standard biochemical actions.
These features promote model transparency, reuse and accuracy. PySB
also interoperates with standard scientific Python libraries such as
NumPy, SciPy and SymPy enabling model simulation and analysis.}

%description %_description

%package -n python3-pysb
Summary: %summary
Requires:       bionetgen
Requires:       bionetgen-perl
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-matplotlib
Requires:       python3-sympy
Requires:       python3-pygraphviz
Requires:       python3-networkx

%description -n python3-pysb %_description

%if %{with doc}
%package doc
Summary:        HTML documentation for %{name}
Requires:       python3-pysb = %{version}-%{release}
BuildRequires:  python3-mock
Provides:       bundled(jquery)
Obsoletes:      %{name}-docs <= 1.0.1

%description doc
This package contains HTML documentation for %{name}.
%endif

%prep
%autosetup -n pysb-%{version} -p1
# https://github.com/pysb/pysb/issues/100
sed -i -e "s|/usr/local/share/BioNetGen|%{perl_vendorlib}/BioNetGen|" \
       -e "s|'c:/Program Files/BioNetGen',||" \
    pysb/bng.py
sed -i -s "1 s|/usr/bin/env python|%{python3}|" pysb/examples/*.py pysb/tools/*.py

# Remove upper bound on sympy version,
# drop requirement on pynose.
sed -r -i "s/'(sympy>=1.6),<1.12'/'\1'/; /'pynose'/d" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build documentation
%if %{with doc}
make -C doc html
rm doc/_build/html/.buildinfo
%endif

%install
%pyproject_install
chmod +x %{buildroot}/%{python3_sitelib}/pysb/examples/run_*.py
chmod +x %{buildroot}/%{python3_sitelib}/pysb/tools/[a-z]*.py

%files -n python3-pysb
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/pysb/
%{python3_sitelib}/pysb-%{version}.dist-info
%{_bindir}/pysb_export

%if %{with doc}
%files doc
%license LICENSE.txt
%doc doc/_build/html
%endif

%changelog
%autochangelog
