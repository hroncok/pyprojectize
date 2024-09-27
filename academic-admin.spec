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
BuildRequires:  python3-setuptools
BuildRequires:  python3-toml
BuildRequires:  python3-requests
BuildRequires:  python3-bibtexparser

Provides:       %srcname

%description
An admin tool for the Academic website builder.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n academic-admin
%doc README.md
%license LICENSE.md
%{python3_sitelib}/academic-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/academic/
%{_bindir}/*

%changelog
%autochangelog
