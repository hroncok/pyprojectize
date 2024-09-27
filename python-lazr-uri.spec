%global pypi_name lazr.uri
Name:           python-lazr-uri
Version:        1.0.6
Release:        %autorelease
Summary:        Parsing and dealing with URIs

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.uri
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
The lazr.uri package includes code for parsing and dealing with URIs.}

%description %_description

%package -n     python3-lazr-uri
Summary:        %{summary}
%{?python_provide:%python_provide python3-lazr-uri}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-lazr-uri  %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-lazr-uri
%license COPYING.txt
%doc README.rst
%{python3_sitelib}/lazr/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
