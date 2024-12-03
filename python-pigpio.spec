%global pypi_name pigpio

Name:           python-%{pypi_name}
Version:        1.78
Release:        %autorelease
Summary:        Raspberry Pi GPIO module

License:        Unlicense
URL:            http://abyz.co.uk/rpi/pigpio/python.html
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Raspberry Pi Python module to access the pigpio daemon.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Raspberry Pi Python module to access the pigpio daemon.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
%autochangelog
