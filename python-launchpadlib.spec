%global pypi_name launchpadlib
Name:           python-%{pypi_name}
Version:        2.0.0
Release:        %autorelease
Summary:        Script Launchpad through its web services interfaces

License:        LGPL-3.0-only
URL:            https://launchpad.net/launchpadlib 
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Launchpadlib is an open-source Python library that lets you treat the HTTP
resources published by Launchpad's web service as Python objects responding
to a standard set of commands. With launchpadlib you can integrate your
applications into Launchpad without knowing a lot about HTTP client
programming.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(httplib2)
BuildRequires:  python3dist(keyring)
BuildRequires:  python3dist(lazr-restfulclient) >= 0.9.19
BuildRequires:  python3dist(lazr-uri)
BuildRequires:  python3dist(testresources)
BuildRequires:  python3dist(wadllib)

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license COPYING.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
