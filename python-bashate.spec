%global pypi_name bashate

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        %autorelease
Summary:        A pep8 equivalent for bash scripts

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.org/project/%{pypi_name}/
Source0:        %{pypi_source}

BuildArch:      noarch

%description
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.

%package -n python3-%{pypi_name}
Summary:        A pep8 equivalent for bash scripts

BuildRequires:  python3-devel
BuildRequires:  python3dist(fixtures)
BuildRequires:  python3dist(pbr)
# deps for check
BuildRequires:  python3dist(autopage)
BuildRequires:  python3dist(stestr)

Requires:       python3dist(babel)
Requires:       python3dist(pbr)
Requires:       python3dist(setuptools)


%description -n python3-%{pypi_name}
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.


%package -n python-%{pypi_name}-doc
Summary: Documentation for bashate module

BuildRequires:  python3dist(openstackdocstheme)
BuildRequires:  python3dist(reno)
BuildRequires:  python3dist(sphinx)


%description -n python-%{pypi_name}-doc
Documentation for the bashate module

%prep
%autosetup -S git -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -rf {test-,}requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
#remove shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' bashate/bashate.py
# doc
sphinx-build-3 -b html -d build/doctrees  doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%pyproject_wheel

%install
%pyproject_install

%check
stestr --test-path ./bashate/tests run

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%exclude %{python3_sitelib}/%{pypi_name}/tests

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%changelog
%autochangelog
