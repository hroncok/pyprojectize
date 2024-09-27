%global pypi_name Nik4

Name:		nik4
Version:	1.7.0
Release:	%autorelease
Summary:	Command-line interface to a Mapnik rendering toolkit

License:	WTFPL
URL:		https://github.com/Zverik/Nik4
Source0:	https://files.pythonhosted.org/packages/source/N/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	python3-mapnik

BuildRequires:	python3-devel

%description
Nik4 is a mapnik-to-image exporting script.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

mv %{buildroot}/%{_bindir}/nik4.py %{buildroot}/%{_bindir}/nik4

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{python3_sitelib}/*

%changelog
%autochangelog
