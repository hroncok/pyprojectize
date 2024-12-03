%global pypi_name django-tastypie
%global sum A flexible and capable API layer for Django
Name:           python-%{pypi_name}
Version:        0.14.7
Release:        %autorelease
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/toastdriven/django-tastypie/

# Release version doesn't include tests
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
# Let's keep Requires and BuildRequires sorted alphabetically
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%description
Tastypie is an webservice API framework for Django. It provides a convenient, 
yet powerful and highly customizable, abstraction for creating REST-style 
interfaces.

%package doc
Summary: Documentation for %{name}

Requires: python3-%{pypi_name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%package -n python3-%{pypi_name}
Summary:        %{sum}

Requires:       python3-dateutil
Requires:       python3-django
Requires:       python3-mimeparse

Obsoletes:      %{pypi_name} < 0.9.11-3
Obsoletes:      python-%{pypi_name} <= 0.13.3-8
Obsoletes:      python2-%{pypi_name} <= 0.13.3-8

%description -n python3-%{pypi_name}
Tastypie is an webservice API framework for Django. It provides a convenient, 
yet powerful and highly customizable, abstraction for creating REST-style 
interfaces.

%prep 
%setup -q -n %{pypi_name}-%{version}


%build
# (re)generate the documentation
#pushd docs
sphinx-build-3 docs docs/_build/html
#make html
#popd
rm -rf docs/_build/html/.??*

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'django_tastypie*' tastypie

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS LICENSE

%files doc
%doc docs/_build/html

%changelog
%autochangelog
