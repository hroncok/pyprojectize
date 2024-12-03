%global pypi_name pytest-xprocess

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        %autorelease
Summary:        Pytest plugin to manage external processes across test runs

License:        MIT
URL:            https://github.com/pytest-dev/pytest-xprocess/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools-scm)

%description
Experimental py.test <>_ plugin for managing processes across test runs.Usage
install via:: pip install pytest-xprocessThis will provide a xprocess fixture
which helps you to ensure that one ore more longer-running processes are
present for your tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).Additionally there are two new command
line...

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(psutil)
Requires:       python3dist(pytest)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Experimental py.test <>_ plugin for managing processes across test runs.Usage
install via:: pip install pytest-xprocessThis will provide a xprocess fixture
which helps you to ensure that one ore more longer-running processes are
present for your tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).Additionally there are two new command
line...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove executable bit from README
chmod -x README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l xprocess

%check
%pyproject_check_import

%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
