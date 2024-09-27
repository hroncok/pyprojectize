%global pypi_name click-man

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        %autorelease
Summary:        Generate man pages for click based CLI applications

License:        MIT
URL:            https://github.com/click-contrib/click-man
Source0:        %pypi_source
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Automatically produces UNIX-style manual pages for Python applications that
use Click for option handling.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
# pkg_resources is used for entrypoint handling
Requires:       python3dist(setuptools)
 

%description -n python3-%{pypi_name}
Automatically produces UNIX-style manual pages for Python applications that
use Click for option handling.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/click-man
%{python3_sitelib}/click_man
%{python3_sitelib}/click_man-%{version}-py%{python3_version}.egg-info


%changelog
%autochangelog
