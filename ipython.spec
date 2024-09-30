%if 0%{?epel}
# disable build of docs and tests for epel because of missing dependencies:
# - python3-ipykernel
# - python3-jupyter-client
# - python3-nbformat
# - python3-testpath
# tests and docs subpackages are also disabled
%bcond_with check
%bcond_with doc
%else
%bcond_without check
%bcond_without doc
%endif

Name:           ipython
Version:        8.27.0
Release:        %autorelease
Summary:        An enhanced interactive Python shell

# SPDX
# Source code is licensed under BSD-3-Clause except
# /IPython/testing/plugin/pytest_ipdoctest.py, which is MIT licensed
# Docs and examples are licensed under CC-BY-4.0
License:        BSD-3-Clause AND MIT AND CC-BY-4.0
URL:            http://ipython.org/
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-stack-data

%if %{with doc}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-ipykernel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
BuildRequires:  python3-typing-extensions
%endif

%if %{with check}
BuildRequires:  python3-Cython
BuildRequires:  python3-matplotlib
BuildRequires:  python3-matplotlib-inline
BuildRequires:  python3-pymongo
BuildRequires:  python3-tornado >= 4.0
BuildRequires:  python3-zmq
BuildRequires:  python3-zmq-tests
BuildRequires:  python3-nbformat
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-ipykernel
BuildRequires:  python3-jupyter-client
BuildRequires:  python3-testpath
# for frontend
BuildRequires:  python3-pygments
# for latex
BuildRequires: /usr/bin/dvipng
BuildRequires: tex(amsmath.sty)
BuildRequires: tex(amssymb.sty)
BuildRequires: tex(amsthm.sty)
BuildRequires: tex(bm.sty)
%endif

%global ipython_desc_base \
IPython provides a replacement for the interactive Python interpreter with\
extra functionality.\
\
Main features:\
 * Comprehensive object introspection.\
 * Input history, persistent across sessions.\
 * Caching of output results during a session with automatically generated\
   references.\
 * Readline based name completion.\
 * Extensible system of 'magic' commands for controlling the environment and\
   performing many tasks related either to IPython or the operating system.\
 * Configuration system with easy switching between different setups (simpler\
   than changing $PYTHONSTARTUP environment variables every time).\
 * Session logging and reloading.\
 * Extensible syntax processing for special purpose situations.\
 * Access to the system shell with user-extensible alias system.\
 * Easily embeddable in other Python programs.\
 * Integrated access to the pdb debugger and the Python profiler.

%description
%{ipython_desc_base}

%package -n python3-ipython
Summary:        An enhanced interactive Python shell
%py_provides    python3-ipython-console
Provides:       ipython3 = %{version}-%{release}
Provides:       ipython = %{version}-%{release}
Provides:       python3-ipython-console = %{version}-%{release}
Obsoletes:      python3-ipython-console < 5.3.0-1
Conflicts:      python2-ipython < 7

BuildRequires:  python3-backcall
BuildRequires:  python3-decorator
BuildRequires:  python3-jedi >= 0.10
BuildRequires:  python3-pexpect
BuildRequires:  python3-pickleshare
BuildRequires:  python3-prompt-toolkit >= 2
BuildRequires:  python3-traitlets >= 5.13.0
Requires:       (tex(amsmath.sty) if /usr/bin/dvipng)
Requires:       (tex(amssymb.sty) if /usr/bin/dvipng)
Requires:       (tex(amsthm.sty)  if /usr/bin/dvipng)
Requires:       (tex(bm.sty)      if /usr/bin/dvipng)

%description -n python3-ipython
%{ipython_desc_base}

This package provides IPython for in a terminal.

%pyproject_extras_subpkg -n python3-ipython notebook

%package -n python3-ipython-sphinx
Summary:        Sphinx directive to support embedded IPython code
Requires:       python3-ipython = %{version}-%{release}
BuildRequires:  python3-sphinx
Requires:       python3-sphinx

%description -n python3-ipython-sphinx
%{ipython_desc_base}

This package contains the ipython sphinx extension.

%if %{with check}
%package -n python3-ipython+test
Summary:        Tests for %{name}
Provides:       python3-ipython-tests = %{version}-%{release}
Obsoletes:      python3-ipython-tests < 8.7.0-2
%py_provides    python3-ipython-tests
Requires:       python3-ipykernel
Requires:       python3-ipython = %{version}-%{release}
Requires:       python3-jupyter-client
Requires:       python3-nbformat
Requires:       python3-zmq-tests
# For latex
Requires:       /usr/bin/dvipng
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)

%description -n python3-ipython+test
This package contains the tests of %{name}.
You can check this way, if ipython works on your platform.
%endif

%if %{with doc}
%package -n python3-ipython-doc
Summary:        Documentation for %{name}
%description -n python3-ipython-doc
This package contains the documentation of %{name}.
%endif


%prep
%autosetup -p1

# delete bundling libs
pushd IPython/external
ls -l
ls -l *

popd

# Remove shebangs
sed -i '1d' $(grep -lr '^#!/usr/' IPython)

find . -name '*.py' -print0 | xargs -0 sed -i '1s|^#!python|#!%{__python3}|'

# Drop upper bound on `pytest-asyncio`
# https://bugzilla.redhat.com/show_bug.cgi?id=2273582
sed -r -i 's/(pytest-asyncio).*"/\1"/' pyproject.toml

# Compatibility with pytest 8
sed -i "/pytest/s/<8//" pyproject.toml
sed -i "s/def setup(/def setup_method(/" IPython/core/tests/test_pylabtools.py
sed -i "s/def teardown(/def teardown_method(/" IPython/core/tests/test_pylabtools.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%if %{with doc}
pushd docs
PYTHONPATH=.. make html SPHINXBUILD='sphinx-build-3 -D intersphinx_timeout=1'
mkdir -p build/html/
rm -rf build/html/.buildinfo
popd
%endif


%install
%pyproject_install

# link the manpage to ipython3
mv %{buildroot}%{_mandir}/man1/ipython{,3}.1
ln -s ./ipython3.1 %{buildroot}%{_mandir}/man1/ipython.1


%if %{with check}
%check
# Ensure that the user's .pythonrc.py is not invoked during any tests.
export PYTHONSTARTUP=""
# Koji builders can be slow, especially on arms, we scale timeouts 4 times
export IPYTHON_TESTING_TIMEOUT_SCALE=4
# To prevent _pytest.pathlib.ImportPathMismatchError, we are
# testing directly in buildroot
pushd %{buildroot}%{python3_sitelib}/IPython
# test_pinfo_docstring_dynamic: https://github.com/ipython/ipython/issues/14457
# test_decorator_skip_with_breakpoint: https://github.com/ipython/ipython/issues/14458
%pytest -k "not test_pinfo_docstring_dynamic and not test_decorator_skip_with_breakpoint"
rm -rf .pytest_cache
popd
%else
rm -r %{buildroot}%{python3_sitelib}/IPython/*/tests
%endif

%files -n python3-ipython
%{_bindir}/ipython3
%{_bindir}/ipython
%{_mandir}/man1/ipython.*
%{_mandir}/man1/ipython3.*

%dir %{python3_sitelib}/IPython
%{python3_sitelib}/IPython/external
%{python3_sitelib}/IPython/__pycache__/
%{python3_sitelib}/IPython/*.py*
%{python3_sitelib}/IPython/py.typed
%dir %{python3_sitelib}/IPython/testing
%{python3_sitelib}/IPython/testing/__pycache__/
%{python3_sitelib}/IPython/testing/*.py*
%{python3_sitelib}/IPython/testing/plugin
%{python3_sitelib}/ipython-%{version}.dist-info/

%{python3_sitelib}/IPython/core/
%{python3_sitelib}/IPython/extensions/
%{python3_sitelib}/IPython/lib/
%{python3_sitelib}/IPython/terminal/
%{python3_sitelib}/IPython/utils/

# tests go into subpackage
%exclude %{python3_sitelib}/IPython/*/tests/


%files -n python3-ipython-sphinx
%{python3_sitelib}/IPython/sphinxext/

%if %{with check}
%files -n python3-ipython+test
%ghost %{python3_sitelib}/ipython-%{version}.dist-info/
%{python3_sitelib}/IPython/*/tests
%endif

%if %{with doc}
%files -n python3-ipython-doc
%doc docs/build/html
%endif


%changelog
%autochangelog
