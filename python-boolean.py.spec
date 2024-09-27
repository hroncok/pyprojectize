%global pypi_name boolean.py

Name:           python-%{pypi_name}
Version:        4.0
Release:        %autorelease
Summary:        Define boolean algebras, and create and parse boolean expressions

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/bastikr/boolean.py
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist pytest}

%global _description \
"boolean.py" is a small library implementing a boolean algebra. It defines\
two base elements, TRUE and FALSE, and a Symbol class that can take on one of\
these two values. Calculations are done in terms of AND, OR and NOT - other\
compositions like XOR and NAND are not implemented but can be emulated with\
AND or and NOT. Expressions are constructed from parsed strings or in Python.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
sphinx-build-%{python3_version} docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst html/
%{python3_sitelib}/boolean.py*.egg-info/
%{python3_sitelib}/boolean/

%changelog
%autochangelog
