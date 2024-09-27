%global srcname hugo-academic-cli

Name:           academic-admin
Version:        0.8.1
Release:        %autorelease
Summary:        Admin tool for the Academic website builder

License:        MIT
URL:            https://github.com/wowchemy/%{srcname}
Source0:        https://github.com/wowchemy/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         academic-admin-0.8.1-dependencies.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-toml
BuildRequires:  python3-requests
BuildRequires:  python3-bibtexparser

Provides:       %srcname

%description
An admin tool for the Academic website builder.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n academic-admin
%doc README.md
%license LICENSE.md
%{python3_sitelib}/academic-%{version}.dist-info/
%{python3_sitelib}/academic/
%{_bindir}/*

%changelog
%autochangelog
