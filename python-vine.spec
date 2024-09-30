%global pypi_name vine

# Enable tests by default
%bcond_without tests

# docs depend on package sphinx_celery
# https://github.com/celery/sphinx_celery
%bcond_with docs

Name:           python-%{pypi_name}
Version:        5.1.0
Release:        %autorelease
Summary:        Promises, promises, promises

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/celery/vine
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with docs}
BuildRequires:  python3-sphinx
%endif


%description
%{summary}


%package -n     python3-%{pypi_name}
Summary:        Promises, promises, promises

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%endif


%description -n python3-%{pypi_name}
%{summary}

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        vine documentation
%description -n python-%{pypi_name}-doc
Documentation for vine
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Compatibility with pytest 8
# https://github.com/celery/vine/commit/cf9b3979173ff22a4a410c4da6cfdad878eced8c
sed -i "/def setup(self)/s/setup/setup_method/" t/unit/test_synchronization.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# docs depend on sphinx-celery
%if %{with docs}
# generate html docs

sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%if %{with tests}
%check
%pytest -xv --cov=vine --cov-report=xml --no-cov-on-fail
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc docs/templates/readme.txt README.rst

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%endif

%changelog
%autochangelog
