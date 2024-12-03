%global pypi_name sphinx-removed-in

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        %autorelease
Summary:        versionremoved and removed-in directives for Sphinx
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/MrSenko/sphinx-removed-in
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# Drop the dependency on deprecated sphinx-testing
# From https://github.com/MrSenko/sphinx-removed-in/pull/9
Patch:          %{url}/commit/52457154d7.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest

%description
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sphinx_removed_in
# https://github.com/MrSenko/sphinx-removed-in/pull/10
rm -rf %{buildroot}%{python3_sitelib}/tests

%check
%pyproject_check_import

%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
