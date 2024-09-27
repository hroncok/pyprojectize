%global pypi_name wadllib
Name:           python-%{pypi_name}
Version:        1.3.6
Release:        %autorelease
Summary:        Navigate HTTP resources using WADL files as guides

License:        LGPL-3.0-only
URL:            https://launchpad.net/wadllib
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
A Python library to navigate HTTP resources using WADL files as guides.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(lazr-uri)

# doctests use the cgi module removed from Python 3.13
# https://bugs.launchpad.net/wadllib/+bug/2069619
BuildRequires:  (python3dist(legacy-cgi) if python3 >= 3.13)

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license COPYING.txt
# README is installed in sitelib and used at runtime
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
