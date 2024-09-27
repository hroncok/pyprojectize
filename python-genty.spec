%global pypi_name genty
Name:           python-%{pypi_name}
Version:        1.3.2
Release:        %autorelease
Summary:        Allows you to run a test with multiple data sets
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/box/genty
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of input
Genty makes this a breeze.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(six)

%description -n python3-%{pypi_name}
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of input
Genty makes this a breeze.


%prep
%autosetup -n %{pypi_name}-%{version}

# Use mock from standard library:
sed -i 's/from mock/from unittest.mock/' test/test_genty.py


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
