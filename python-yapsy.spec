%global srcname Yapsy
%global modname yapsy

Name:           python-%{modname}
Version:        1.12.2
Release:        %autorelease
Summary:        Simple plugin system for Python applications

# Automatically converted from old format: BSD and ISC and CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND ISC AND LicenseRef-Callaway-CC-BY-SA
URL:            http://yapsy.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/%{modname}/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/tibonihoo/yapsy/pull/11
# Should fix yapsy to work with Python 3.12
Patch:          11.patch

# prerequisit for PR 22
# https://github.com/tibonihoo/yapsy/pull/20
Patch1:         20.patch
# fixes regression introduced with py 3.12 changges in PR#11, for rhbz#2268608
# https://github.com/tibonihoo/yapsy/pull/22
Patch2:         22_pluginmgr.patch

BuildArch:      noarch

%global _description \
Yapsy’s main purpose is to offer a way to easily design a plugin system in\
Python. Yapsy only depends on Python’s standard library.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p2
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test || :

%files -n python3-%{modname}
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
%autochangelog
