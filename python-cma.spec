%global srcname cma
Name:           python-cma
Version:        4.0.0
Release:        %autorelease
Summary:        Covariance Matrix Adaptation Evolution Strategy numerical optimizer

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://cma.gforge.inria.fr/cmaes_sourcecode_page.html
Source0:         %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-numpy

%global _description %{expand:
A stochastic numerical optimization algorithm for difficult (non-convex,
ill-conditioned, multi-modal, rugged, noisy) optimization problems in continuous
search spaces, implemented in Python.}

%description %_description

%package -n     python3-cma
Summary:        %{summary}

%description -n python3-cma %_description

%prep
%autosetup -n cma-%{version}
#Fix line-endings
sed -i 's/\r//' README.txt
#Remove unneeded shebang
sed -i '1d' cma/{bbobbenchmarks.py,purecma.py,test.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-cma
%doc README.txt
%license LICENSE
%{python3_sitelib}/cma/
%{python3_sitelib}/cma-*.dist-info/

%changelog
%autochangelog
