%global srcname flask-cors

Name:           python-%{srcname}
Version:        4.0.1
Release:        %autorelease
Summary:        Cross Origin Resource Sharing (CORS) support for Flask
License:        MIT
URL:            https://github.com/corydolphin/%{srcname}
Source0:        https://github.com/corydolphin/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%package -n python3-%{srcname}
Summary:        Cross Origin Resource Sharing (CORS) support for Flask


BuildRequires:  python3-devel
BuildRequires:  python3-flask
BuildRequires:  python3-pytest
BuildRequires:  python3-packaging
BuildRequires:  python3-six

%description -n python3-%{srcname}
Python3 flask_cors package.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python3_sitelib}/flask_cors/
%{python3_sitelib}/Flask_Cors*.dist-info/

%changelog
%autochangelog
