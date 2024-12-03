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

%description -n python3-%{pypi_name}
Chromium HSTS Preload list as a Python package. The package provides a
single function: in_hsts_preload() which takes an IDNA-encoded host and
returns either True or False regarding whether that host should be only
accessed via HTTPS.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

