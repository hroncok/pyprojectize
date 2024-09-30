%global pypi_name pyhaversion
%global pkg_name haversion

Name:           python-%{pkg_name}
Version:        23.1.0
Release:        %autorelease
Summary:        Python module to get the version number of Home Assistant

License:        MIT
URL:            https://github.com/ludeeus/pyhaversion
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python module to get the version number of Home Assistant.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(async-timeout)
BuildRequires:  python3dist(awesomeversion)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(semantic-version)
BuildRequires:  python3dist(aresponses)
%py_provides    python3-%{pypi_name}

%description -n python3-%{pkg_name}
A Python module to get the version number of Home Assistant.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e 's/main/%{version}/g' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests -k "not test_stable_version and not test_etag" 

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

