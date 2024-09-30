%global python3_pkgversion 38
%global srcname requests_ntlm

Name:           python%{python3_pkgversion}-%{srcname}-epel
Version:        1.1.0
Release:        2%{?dist}
Summary:        NTLM module for python requests

License:        ISC
URL:            https://pypi.python.org/pypi/requests_ntlm
Source0:        https://github.com/requests/requests-ntlm/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
This package allows Python clients running on any operating system to provide
NTLM authentication to a supporting server.}

%description %{_description}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python3.8dist(setuptools)
BuildRequires:  python3.8dist(requests) >= 2
BuildRequires:  python3.8dist(ntlm-auth) >= 1.0.2
BuildRequires:  python3.8dist(cryptography) >= 1.3
BuildRequires:  python3.8dist(pytest)
#BuildRequires:  python3.8dist(flask)

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n requests-ntlm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
#python3 -m tests.test_server &
#python3 -m pytest --ignore=tests/functional/test_functional.py --ignore=tests/test_server.py -vv

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CONTRIBUTORS.rst README.rst

%changelog
* Thu Jul 21 2022 Maxwell G <gotmax@e.email> - 1.1.0-2
- Rebuild to fix bug in epel-rpm-macros' Python dependency generator

* Tue Jul 05 2022 Orion Poplawski - 1.1.0-1
- Build for EPEL9
