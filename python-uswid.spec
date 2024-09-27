%global srcname uswid

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Python module for working with Firmware SBoMs

License:        LGPL-2.1-or-later
URL:            https://github.com/hughsie/python-uswid
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

%global _description %{expand:
Software Identification (SWID) tags provide an extensible XML-based structure to
identify and describe individual software components, patches, and installation
bundles. XML SWID tag representations can be too large for devices with network
and storage constraints.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-cbor2
BuildRequires:  python3-lxml
BuildRequires:  python3-pefile
BuildRequires:  python3-wheel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' %{srcname}/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
#%{python3} setup.py test
%pytest

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}.dist-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/uswid

%changelog
%autochangelog
