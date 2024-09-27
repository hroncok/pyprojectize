%global pypi_name reflink
%global pypi_version 0.2.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python wrapper around the reflink system calls
License:        MIT
URL:            https://gitlab.com/rubdos/pyreflink
Source0:        %{pypi_source}

BuildRequires:  btrfs-progs
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Python wrapper around the reflink system calls.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cffi)
%description -n python3-%{pypi_name}
 Python reflink :alt: Documentation Status

%package -n python-%{pypi_name}-doc
Summary:        reflink documentation
%description -n python-%{pypi_name}-doc
Documentation for reflink

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# Cannot test as we cannot use loop filesystems in a systemd-nspawnd container
#%check
#%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst docs/readme.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Aug 23 2024 Neel Chauhan <neel@neelc.org> - 0.2.2-1
- Initial package.
