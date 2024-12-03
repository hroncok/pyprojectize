%global mod_name Flask-OpenID

Name:           python-flask-openid
Version:        1.3.0
Release:        %autorelease
Summary:        OpenID support for Flask

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/mitsuhiko/flask-openid/
Source0:        %{pypi_source %{mod_name}}
# https://github.com/pallets-eco/flask-openid/pull/71
Patch01:        71.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-openid

%global _description\
Flask-OpenID is an extension to flask that allows you to add openid\
based authentication to your website in a matter of minutes.

%description %_description

%package -n python3-flask-openid
Summary:        OpenID support for Flask
Requires:       python3-openid

%description -n python3-flask-openid
Flask-OpenID is an extension to flask that allows you to add openid
based authentication to your website in a matter of minutes.

This package includes the python 3 version of the module.


%prep
%autosetup -n %{mod_name}-%{version} -p1
rm -f docs/_themes/.git
rm -f docs/_themes/.gitignore
rm -f docs/.DS_Store
rm -f docs/_static/.DS_Store
rm -f docs/_static/._.DS_Store
rm -f docs/._.DS_Store


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_openid

%check
%pyproject_check_import

%files -n python3-flask-openid -f %{pyproject_files}
%doc docs README.rst LICENSE PKG-INFO

%changelog
%autochangelog
