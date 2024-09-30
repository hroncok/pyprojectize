%global pypi_name minidump

Name:           python-%{pypi_name}
Version:        0.0.21
Release:        %autorelease
Summary:        Python library to parse and read Microsoft minidump file format

License:        MIT
URL:            https://github.com/skelsec/minidump
Source0:        %pypi_source
BuildArch:      noarch

%description
A Python library to parse and read Microsoft minidump file format. Can create
minidumps on Windows machines using the windows API (implemented with ctypes).

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
A Python library to parse and read Microsoft minidump file format. Can create
minidumps on Windows machines using the windows API (implemented with ctypes).

%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}
Command line tools for the Microsoft minidump file format.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs
sed -i -e '/^#!\//, 1d' %{pypi_name}/{*.py,*/*.py}
# Fix line endings
sed -i "s|\r||g" README.md

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.dist-info

%files -n %{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/%{pypi_name}

%changelog
%autochangelog

