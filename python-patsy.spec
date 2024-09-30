%bcond_without check

%global srcname patsy

%global _description %{expand:
A Python package for describing statistical models and for building 
design matrices. It is closely inspired by and compatible with 
the 'formula' mini-language used in R and S.}

Name: python-%{srcname}
Version: 0.5.6
Release: %autorelease
Summary: Describing statistical models in Python using symbolic formulas
# All code is under BSD except patsy.compat that is under Python
# See LICENSE.txt for details
License: BSD-2-Clause AND PSF-2.0

URL: https://github.com/pydata/patsy
Source0:  %{pypi_source} 
Patch0: patsy-intersphinx.patch
Patch1: patsy-error-doc.patch
# https://github.com/pydata/patsy/issues/143
Patch2: patsy-print-doc.patch
#Patch3: patsy-python39.patch
# The contour routine emits a warning with numpy 1.9
Patch4: patsy-warn-doc.patch
Patch5: patsy-doc-conf.patch

BuildArch: noarch
BuildRequires: make
BuildRequires: python3-devel

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%if %{with check}
BuildRequires: %{py3_dist pytest}
#BuildRequires: python3-numpy
%endif
# For the docs
BuildRequires: python3-sphinx
BuildRequires: python3-ipython-sphinx
BuildRequires: python3-pandas
BuildRequires: python3-docs
BuildRequires: python3-numpy-doc
BuildRequires: texlive-latex
BuildRequires: texlive-ucs texlive-amscls
# This should be required by python3-ipython-sphinx
BuildRequires: python3-matplotlib 
# For splines
BuildRequires: python3-scipy  

# For splines
Recommends: %{py3_dist scipy}


%description -n python3-%{srcname} %_description

%package -n python3-%{srcname}-doc
Summary: Documentation for python3-%{srcname}, includes full API docs
BuildArch: noarch

%description -n python3-%{srcname}-doc
This package contains the full API documentation for python3-%{srcname}.


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

pushd doc
  export PYTHONPATH=`readlink -f ../build/lib`
  make html SPHINXBUILD=sphinx-build-%{python3_version}
popd

%install
%pyproject_install

%check
%if %{with check}
%pytest -v --deselect "patsy/eval.py::test_EvalEnvironment_eq"
%endif

%files -n python3-%{srcname}
%doc README.md TODO
%license LICENSE.txt
%{python3_sitelib}/patsy*

%files -n python3-%{srcname}-doc
%doc README.md TODO doc/_build/html
%license LICENSE.txt

%changelog
%autochangelog
