%global python3_pkgversion 38
%global srcname ntlm-auth

Name:           python%{python3_pkgversion}-%{srcname}-epel
Version:        1.5.0
Release:        2%{?dist}
Summary:        Python 3 compatible NTLM library

License:        LGPLv3+
URL:            https://pypi.python.org/pypi/ntlm-auth
Source:         https://github.com/jborean93/ntlm-auth/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python3.8dist(setuptools)
# For tests
BuildRequires:  python3.8dist(pytest)
BuildRequires:  python3.8dist(requests)
BuildRequires:  python3.8dist(cryptography)

%global _description %{expand:
This package allows Python clients running on any operating system to provide
NTLM authentication to a supporting server.}

%description %{_description}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%python3 -m pytest -vv

%files -n python%{python3_pkgversion}-%{srcname}
%doc CHANGES.md README.md
%license LICENSE
%{python3_sitelib}/ntlm_auth-*.egg-info/
%{python3_sitelib}/ntlm_auth/

%changelog
* Thu Jul 21 2022 Maxwell G <gotmax@e.email> - 1.5.0-2
- Rebuild to fix bug in epel-rpm-macros' Python dependency generator

* Tue Jun 28 2022 Orion Poplawski <orion@nwra.com> - 1.5.0-1
- Build for EPEL8 Python 3.8
