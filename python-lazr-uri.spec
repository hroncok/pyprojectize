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

BuildRequires:  python3-devel

%description -n python3-lazr-uri  %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l lazr

%check
%pyproject_check_import
%{__python3} setup.py test

%files -n python3-lazr-uri -f %{pyproject_files}
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth

%changelog
%autochangelog
