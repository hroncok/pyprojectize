%global srcname django-timezone-field

Name:           python-%{srcname}
Version:        4.2.1
Release:        %autorelease
Summary:        Django app providing database and form fields for pytz timezone objects

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mfogel/django-timezone-field
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%package     -n python3-%{srcname}+rest_framework
Summary:        %{summary}
Provides:       python3dist(%{srcname}[rest_framework]) = %{version}
Provides:       python%{python3_version}dist(%{srcname}[rest_framework]) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(djangorestframework) >= 3

%description -n python3-%{srcname}+rest_framework %{_description}

"rest_framework" extras. Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/django_timezone_field-*.dist-info/
%{python3_sitelib}/timezone_field/

%files -n python3-%{srcname}+rest_framework
%{?python_extras_subpkg:%ghost %{python3_sitelib}/django_timezone_field-*.dist-info/}

%changelog
%autochangelog