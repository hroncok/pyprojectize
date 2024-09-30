%global pypi_name hatasmota

Name:           python-%{pypi_name}
Version:        0.7.3
Release:        %autorelease
Summary:        Python module to help parse and construct Tasmota MQTT messages

License:        MIT
URL:            https://github.com/emontnemery/hatasmota
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python module to help parse and construct Tasmota MQTT messages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Python module to help parse and construct Tasmota MQTT messages.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/HATasmota-%{version}.dist-info/

%changelog
%autochangelog
