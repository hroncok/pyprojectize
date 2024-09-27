%global pypi_name backcall

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        %autorelease
Summary:        Specifications for callback functions passed in to an API

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/takluyver/backcall
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/takluyver/backcall/8eb45a77a40edad74b33086d05fd4d99d43d80b0/LICENSE
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%?python_enable_dependency_generator

%description
Specifications for callback functions passed in to an API.

If your code lets other people supply callback functions, it's important to
specify the function signature you expect, and check that functions support
that. Adding extra parameters later would break other peoples code unless
you're careful. Backcall helps with that.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Specifications for callback functions passed in to an API.

If your code lets other people supply callback functions, it's important to
specify the function signature you expect, and check that functions support
that. Adding extra parameters later would break other peoples code unless
you're careful. Backcall helps with that.


%prep
%autosetup -n %{pypi_name}-%{version}
cp -p %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -vv tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
