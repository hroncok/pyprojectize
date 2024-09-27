%global srcname ijson

Name:           python-%{srcname}
Version:        3.2.3
Release:        %autorelease
Summary:        Iterative JSON parser

License:        BSD-3-Clause
URL:            https://github.com/ICRAR/ijson
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  python3dist(setuptools)

%global _description %{expand:
Iterative JSON parser with standard Python iterator interfaces.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     yajl
Recommends:     python3dist(cffi)

# Test dependencies
BuildRequires:  python3dist(cffi)

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

# Disable tests for unsupported configurations.
sed -i "s/\['python', 'yajl', 'yajl2', 'yajl2_cffi', 'yajl2_c']/\['python', 'yajl2', 'yajl2_cffi']/" test/test_base.py

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:$PWD %{python3} -m unittest discover

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
