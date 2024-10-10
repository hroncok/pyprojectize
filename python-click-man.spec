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

%description
Automatically produces UNIX-style manual pages for Python applications that
use Click for option handling.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
# pkg_resources is used for entrypoint handling
Requires:       python3dist(setuptools)
 

%description -n python3-%{pypi_name}
Automatically produces UNIX-style manual pages for Python applications that
use Click for option handling.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l click_man


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/click-man


%changelog
%autochangelog
