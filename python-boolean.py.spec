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

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
sphinx-build-%{python3_version} docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l boolean

%check
%pytest

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst README.rst html/

%changelog
%autochangelog
