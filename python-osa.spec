%global pypi_name osa

Name:           python-%{pypi_name}
Version:        0.2.3
Release:        %autorelease
Summary:        A small python SOAP client library

License:        LGPL-3.0-or-later
URL:            https://pypi.org/project/osa
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
A small python library to consume SOAP services. It can process
a WSDL documents and then use types and methods defined in that
document.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}

Requires:  python3

%description -n python3-%{pypi_name}
A small python library to consume SOAP services. It can process
a WSDL documents and then use types and methods defined in that
document.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf *.egg-info

%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
# No License, see https://github.com/baserge/osa/issues/1
%doc README
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/osa-%{version}-py?.*.egg-info


%changelog
%autochangelog
