%global pypi_name aioasuswrt

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        %autorelease
Summary:        Python API wrapper for Asuswrt devices

License:        MIT
URL:            https://github.com/kennedyshead/aioasuswrt
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python API wrapper for Asuswrt devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest-runner)

%description -n python3-%{pypi_name}
Python API wrapper for Asuswrt devices.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog

