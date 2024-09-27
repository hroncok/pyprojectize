%global pypi_name aiolifx

Name:           python-%{pypi_name}
Version:        0.8.9
Release:        %autorelease
Summary:        Python API for local communication with LIFX devices

License:        MIT
URL:            http://github.com/frawau/aiolifx
Source0:        %{pypi_source}
BuildArch:      noarch

%description
aiolifx is a Python library to control Lifx LED light bulbs 
over your LAN.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiolifx is a Python library to control Lifx LED light bulbs 
over your LAN.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# https://github.com/frawau/aiolifx/pull/37
sed -i -e '/^#!\//, 1d' aiolifx/{__main__.py,aiolifx.py,update-products.py}
# Remove script to maintain parts of the source
rm -rf aiolifx/update-products.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog

