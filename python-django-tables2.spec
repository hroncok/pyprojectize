%global srcname django-tables2

Name:           python-django-tables2
Version:        2.4.0
Release:        %autorelease
Summary:        Table framework for Django

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jieter/django-tables2
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
django-tables2 simplifies the task of turning sets of data into HTML tables.
It has native support for pagination and sorting. It does for HTML tables
what django.forms does for HTML forms.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Obsoletes:      python-%{srcname} < 1.2.3-5
Obsoletes:      python2-%{srcname} < 1.2.3-5

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info/

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files django_tables2

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog