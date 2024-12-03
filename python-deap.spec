# Building of HTML docs fails in Python 3.12
# Disable as a temporary measure
%bcond_without docs

Name:           python-deap
Version:        1.4.1

Release:        %autorelease
Summary:        Distributed Evolutionary Algorithms in Python

License:        LGPL-3.0-only
URL:            https://github.com/deap
Source:         https://github.com/deap/deap/archive/%{version}/deap-%{version}.tar.gz

Patch:          0001-Use-float-instead-of-np.float.patch
Patch:          0002-setup-fix-git-invocation-for-exlinks-add-override.patch
Patch:          0001-Fix-use-of-unknown-escape-seqeuences.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  python3-devel
BuildRequires:  python3-pypandoc
BuildRequires:  python3-pytest
BuildRequires:  python3-nose
BuildRequires:  python3-numpy

# documentation
%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  texlive-scheme-basic
BuildRequires:  tex(ucs.sty)
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  python3-numpy
BuildRequires:  python3-matplotlib
%endif

%global _description %{expand:
DEAP is a novel evolutionary computation framework for rapid prototyping and
testing of ideas that implements a number of genetic optimization algorithms
behind a common interface.}

%description %_description

%package -n     python3-deap
Requires:       python3-numpy
BuildRequires:  python3-nose
Summary:        %{summary}

%description -n python3-deap %_description

%if %{with docs}
%package -n python-deap-doc
Summary:        Documentation for deap
BuildArch:      noarch
%description -n python-deap-doc
%{summary}.
%endif

%prep
%autosetup -n deap-%{version} -p1
sed -i 's/\["git", "rev-parse", "HEAD"\]/["echo", "deap-%{version}-%{release}"]/' \
    doc/conf.py

%if %{with docs}
# https://bugzilla.redhat.com/show_bug.cgi?id=1644771
sed -i -r "s|'matplotlib.sphinxext.only_directives',||" doc/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
%if %{with docs}
GITHUB_COMMIT=%{version} \
  PYTHONPATH=build/lib.%{python3_platform}-%{python3_version} \
  sphinx-build-3 doc build/html

# remove the sphinx-build leftovers
rm -rf build/html/.{doctrees,buildinfo}
%endif

%global _docdir_fmt %{name}

%install
%pyproject_install
%pyproject_save_files -l deap

%check
%pyproject_check_import

OPTIONS=(
  # Fails with: AssertionError: CMA algorithm did not converged properly.
  --deselect=tests/test_algorithms.py::test_cma
)

%pytest tests/
PYTHONPATH=%{buildroot}%{python3_sitearch} pytest -v "${OPTIONS[@]}"

%files -n python3-deap -f %{pyproject_files}
%doc README.md

%if %{with docs}
%files -n python-deap-doc
%license LICENSE.txt
%doc build/html
%endif

%changelog
%autochangelog
