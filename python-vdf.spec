%bcond_without tests

%global pypi_name vdf

Name:       python-%{pypi_name}
Version:    3.4
Release:    %autorelease
Summary:    Package for working with Valve's text and binary KeyValue format
BuildArch:  noarch

License:    MIT
URL:        https://github.com/ValvePython/vdf
Source0:    %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires: python3-devel
%if %{with tests}
BuildRequires: python3dist(pytest-cov) >= 2.7.0
BuildRequires: python3dist(pytest)
%endif

%global _description %{expand:
Pure python module for (de)serialization to and from VDF that works just like
json.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%if %{with tests}
%check
%{python3} -m pytest -v \
    %dnl # https://github.com/ValvePython/vdf/issues/33
    --ignore=tests/test_binary_vdf.py
%endif


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}*.dist-info


%changelog
%autochangelog
