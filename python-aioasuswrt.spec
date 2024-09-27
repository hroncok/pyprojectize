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
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest-runner)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python API wrapper for Asuswrt devices.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog

