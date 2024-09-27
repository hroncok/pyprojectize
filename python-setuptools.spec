%global srcname setuptools

# used when bootstrapping new Python versions
%bcond bootstrap 0

# Similar to what we have in pythonX.Y.spec files.
# If enabled, provides unversioned executables and other stuff.
# Disable it if you build this package in an alternative stack.
%bcond main_python 1

# The original RHEL N+1 content set is defined by (build)dependencies
# of the packages in Fedora ELN. Hence we disable tests and documentation here
# to prevent pulling many unwanted packages in.
# We intentionally keep this enabled on EPEL.
%bcond tests %[%{without bootstrap} && (%{defined fedora} || %{defined epel})]

%global python_wheel_name %{srcname}-%{version}-py3-none-any.whl

Name:           python-setuptools
# When updating, update the bundled libraries versions bellow!
Version:        69.2.0
Release:        %autorelease
Summary:        Easily build and distribute Python packages
# setuptools is MIT
# platformdirs is MIT
# more-itertools is MIT
# ordered-set is MIT
# packaging is BSD-2-Clause OR Apache-2.0
# importlib-metadata is Apache-2.0
# importlib-resources is Apache-2.0
# jaraco.text is MIT
# typing-extensions is Python-2.0.1
# zipp is MIT
# nspektr is MIT
# tomli is MIT
# the setuptools logo is MIT
License:        MIT AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0) AND Python-2.0.1
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{srcname} %{version}}

# Some test deps are optional and either not desired or not available in Fedora, thus this patch removes them.
Patch:          Remove-optional-or-unpackaged-test-deps.patch

# The `setup.py install` deprecation notice might be confusing for RPM packagers
# adjust it, but only when $RPM_BUILD_ROOT is set
Patch:          Adjust-the-setup.py-install-deprecation-message.patch

# Python 3.13 compatibility patches, merged upstream
Patch:          https://github.com/pypa/setuptools/pull/4356.patch
Patch:          https://github.com/pypa/setuptools/pull/4357.patch

# Security fix for CVE-2024-6345
# Remote code execution via download functions in the package_index module
# Tracking bug: https://bugzilla.redhat.com/show_bug.cgi?id=2297771
# Upstream solution: https://github.com/pypa/setuptools/pull/4332
# Patch simplified because upstream doesn't support SVN anymore.
Patch:          CVE-2024-6345.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
BuildRequires:  gcc
%endif

# python3 bootstrap: this is built before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
# The minimal version is for bundled provides verification script to accept multiple files as input
BuildRequires:  python3-rpm-generators >= 12-8

%if %{without bootstrap}
BuildRequires:  pyproject-rpm-macros >= 0-44
# Not to use the pre-generated egg-info, we use setuptools from previous build to generate it
%endif

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.

# Virtual provides for the packages bundled by setuptools.
# Bundled packages are defined in multiple files. Generate the list with:
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%%{python3_pkgversion}dist' */_vendor/vendored.txt
%global bundled %{expand:
Provides: bundled(python%{python3_pkgversion}dist(importlib-metadata)) = 6
Provides: bundled(python%{python3_pkgversion}dist(importlib-resources)) = 5.10.2
Provides: bundled(python%{python3_pkgversion}dist(jaraco-text)) = 3.7
Provides: bundled(python%{python3_pkgversion}dist(more-itertools)) = 8.8
Provides: bundled(python%{python3_pkgversion}dist(ordered-set)) = 3.1.1
Provides: bundled(python%{python3_pkgversion}dist(packaging)) = 23.1
Provides: bundled(python%{python3_pkgversion}dist(platformdirs)) = 2.6.2
Provides: bundled(python%{python3_pkgversion}dist(tomli)) = 2.0.1
Provides: bundled(python%{python3_pkgversion}dist(typing-extensions)) = 4.0.1
Provides: bundled(python%{python3_pkgversion}dist(typing-extensions)) = 4.4
Provides: bundled(python%{python3_pkgversion}dist(zipp)) = 3.7
}

%package -n python%{python3_pkgversion}-setuptools
Summary:        Easily build and distribute Python 3 packages
%{bundled}

# For users who might see ModuleNotFoundError: No module named 'pkg_resoureces'
# NB: Those are two different provides: one contains underscore, the other hyphen
%py_provides    python%{python3_pkgversion}-pkg_resources
%py_provides    python%{python3_pkgversion}-pkg-resources

%description -n python%{python3_pkgversion}-setuptools
Setuptools is a collection of enhancements to the Python 3 distutils that allow
you to more easily build and distribute Python 3 packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.

%if %{without bootstrap}
%package -n     %{python_wheel_pkg_prefix}-%{srcname}-wheel
Summary:        The setuptools wheel
%{bundled}

%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of setuptools to use with venv.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}
%if %{without bootstrap}
# If we don't have setuptools installed yet, we use the pre-generated .egg-info
# See https://github.com/pypa/setuptools/pull/2543
# And https://github.com/pypa/setuptools/issues/2550
# WARNING: We cannot remove this folder since Python 3.11.1,
#          see https://github.com/pypa/setuptools/issues/3761
#rm -r %%{srcname}.egg-info
%endif

# Strip shbang
find setuptools pkg_resources -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f setuptools/*.exe
# Don't ship these
rm -r docs/conf.py

%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x testing}
%endif

%build
%if %{with bootstrap}
%pyproject_wheel
%else
%pyproject_wheel
%endif


%install
%if %{with bootstrap}
# The setup.py install command tries to import distutils
# but the distutils-precedence.pth file is not yet respected
# and Python 3.12+ no longer has distutils in the standard library.
ln -s setuptools/_distutils distutils
PYTHONPATH=$PWD %pyproject_install
unlink distutils
%else
%pyproject_install
%pyproject_save_files setuptools pkg_resources _distutils_hack
%endif

# https://github.com/pypa/setuptools/issues/2709
rm -rf %{buildroot}%{python3_sitelib}/pkg_resources/tests/
%if %{without bootstrap}
sed -i '/\/pkg_resources\/tests\b/d' %{pyproject_files}

# Install the wheel for the python-setuptools-wheel package
mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}
%endif


%check
# Verify bundled provides are up to date
%{_rpmconfigdir}/pythonbundles.py */_vendor/vendored.txt --namespace 'python%{python3_pkgversion}dist' --compare-with '%{bundled}'

# Regression test, the tests are not supposed to be installed
test ! -d %{buildroot}%{python3_sitelib}/pkg_resources/tests
test ! -d %{buildroot}%{python3_sitelib}/setuptools/tests

%if %{without bootstrap}
# Regression test, the wheel should not be larger than 900 kB
# https://bugzilla.redhat.com/show_bug.cgi?id=1914481#c3
test $(stat --format %%s %{_pyproject_wheeldir}/%{python_wheel_name}) -lt 900000

%pyproject_check_import
%endif

%if %{with tests}
# https://github.com/pypa/setuptools/discussions/2607
rm pyproject.toml

# Upstream tests
# --ignore=setuptools/tests/test_integration.py
# --ignore=setuptools/tests/integration/
# --ignore=setuptools/tests/config/test_apply_pyprojecttoml.py
# -k "not test_pip_upgrade_from_source"
#   the tests require internet connection
# --ignore=setuptools/tests/test_editable_install.py
#   the tests require pip-run which we don't have in Fedora
PRE_BUILT_SETUPTOOLS_WHEEL=%{_pyproject_wheeldir}/%{python_wheel_name} \
PYTHONPATH=$(pwd) %pytest \
 --ignore=setuptools/tests/test_integration.py \
 --ignore=setuptools/tests/integration/ \
 --ignore=setuptools/tests/test_editable_install.py \
 --ignore=setuptools/tests/config/test_apply_pyprojecttoml.py \
 --ignore=tools/finalize.py \
 -k "not test_pip_upgrade_from_source and not test_setup_requires_honors_fetch_params"
%endif # with tests


%files -n python%{python3_pkgversion}-setuptools %{?!with_bootstrap:-f\ %{pyproject_files}}
%license LICENSE
%doc docs/* NEWS.rst README.rst
%{python3_sitelib}/distutils-precedence.pth
%if %{with bootstrap}
%{python3_sitelib}/setuptools-%{version}.dist-info/
%{python3_sitelib}/pkg_resources/
%{python3_sitelib}/setuptools/
%{python3_sitelib}/_distutils_hack/
%endif

%if %{without bootstrap}
%files -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
%license LICENSE
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}
%endif


%changelog
%autochangelog
