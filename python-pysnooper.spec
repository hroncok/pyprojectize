%global srcname PySnooper
Name:           python-pysnooper
Version:        1.2.1
Release:        %autorelease
Summary:        Poor man's debugger for Python

License:        MIT
URL:            https://github.com/cool-RR/pysnooper
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(six)

%global _description %{expand:
PySnooper is a replacement for debug print statements in code. After decorating
a function it automatically logs which lines were run and any changes to local
variables.

@pysnooper.snoop()
def func(...):
  ...
}

%description %_description

%package -n python3-pysnooper
Summary:        %{summary}
%{?python_provides python3-pysnooper}

%description -n python3-pysnooper %_description

%prep
%autosetup -n PySnooper-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pysnooper

%check
%pyproject_check_import
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m pytest -v tests/

%files -n python3-pysnooper -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
