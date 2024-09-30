%global pypi_name hvac
%global __python3 /usr/bin/python3.8
%global python3_pkgversion 38

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.11.2
Release:        2%{?dist}
Summary:        HashiCorp Vault API client for Python

License:        ASL 2.0
URL:            https://github.com/hvac/hvac
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros

%description
This package provides a Python API client for HashiCorp Vault.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?el8}
# Lower dependency to requests 2.20+ for EL8
sed -e "s/requests>=2.21.0/requests>=2.20.0/" -i setup.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
* Thu Jul 21 2022 Maxwell G <gotmax@e.email> - 0.11.2-2
- Rebuild to fix bug in epel-rpm-macros' Python dependency generator

%autochangelog
