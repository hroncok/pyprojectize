%global srcname pretend

Name:           python-pretend
Version:        1.0.9
Release:        %autorelease
Summary:        A library for stubbing in Python

License:        BSD-3-Clause
URL:            https://github.com/alex/pretend
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest


%description
Pretend is a library to make stubbing with Python easier.


%package -n python3-pretend
Summary:        A library for stubbing in Python


%description -n python3-pretend
Pretend is a library to make stubbing with Python easier.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%pytest -v


%files -n python3-pretend
%doc README.rst
%license LICENSE.rst
%pycached %{python3_sitelib}/pretend.py
%{python3_sitelib}/pretend-%{version}-py%{python3_version}.egg-info/


%changelog
%autochangelog
