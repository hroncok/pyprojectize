%global pypi_name asysocks

Name:           python-%{pypi_name}
Version:        0.1.7
Release:        %autorelease
Summary:        Socks5/Socks4 client and server library

License:        MIT
URL:            https://github.com/skelsec/asysocks
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/skelsec/asysocks/master/LICENSE
BuildArch:      noarch

%description
A Python Socks5/Socks4 client and server library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
A Python Socks5/Socks4 client and server library.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE
sed -i -e '/^#!\//, 1d' asysocks/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/asysock*

%changelog
%autochangelog

