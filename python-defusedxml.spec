%global pypi_name    defusedxml
%global base_version 0.7.1
#global prerel       ...
%global upstream_version %{base_version}%{?prerel}
Name:           python-%{pypi_name}
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        %autorelease
Summary:        XML bomb protection for Python stdlib modules
# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            https://github.com/tiran/defusedxml
Source0:        %{pypi_source %{pypi_name} %{upstream_version}}

# Drop deprecated unittest.makeSuite()
# From https://github.com/tiran/defusedxml/commit/4e6cea5f5b
# (This no longer skips lxml tests when lxml is not installed.)
Patch:          drop-makeSuite.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-lxml

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pypi_name}
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module. This is the python%{python3_pkgversion} build.


%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%{python3} tests.py


%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.txt README.html CHANGES.txt


%changelog
%autochangelog
