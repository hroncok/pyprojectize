%global pypi_name hstspreload

Name:           python-%{pypi_name}
Version:        2024.9.1
Release:        %autorelease
Summary:        Chromium HSTS Preload list

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sethmlarson/hstspreload
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Chromium HSTS Preload list as a Python package. The package provides a
single function: in_hsts_preload() which takes an IDNA-encoded host and
returns either True or False regarding whether that host should be only
accessed via HTTPS.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Chromium HSTS Preload list as a Python package. The package provides a
single function: in_hsts_preload() which takes an IDNA-encoded host and
returns either True or False regarding whether that host should be only
accessed via HTTPS.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog

