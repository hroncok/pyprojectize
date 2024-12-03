%bcond_without tests

%global pypi_name wcwidth

Name:           python-%{pypi_name}
Version:        0.2.13
Release:        %autorelease
Summary:        Measures number of Terminal column cells of wide-character codes

# part of the code is under HPND-Markus-Kuhn
License:        MIT AND HPND-Markus-Kuhn
URL:            https://github.com/jquast/wcwidth
Source0:        %pypi_source
BuildArch:      noarch

%description
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name}
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%prep
%setup -q -n %{pypi_name}-%{version}
# skip coverage checks
sed -i -e 's|--cov[^[:space:]]*||g' tox.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%if %{with tests}
%check
%pyproject_check_import

%pytest -v
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
