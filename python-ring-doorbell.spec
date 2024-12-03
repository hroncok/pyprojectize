%global pypi_name ring-doorbell

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        %autorelease
Summary:        Python library to communicate with Ring Door Bells

# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            https://github.com/tchellomello/python-ring-doorbell
Source0:        %{url}/archive/%{version}/ring_doorbell-%{version}.tar.gz
BuildArch:      noarch

%description
Python library written that exposes the Ring.com devices as Python
objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-oauthlib)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests-mock)

%description -n python3-%{pypi_name}
Python library written that exposes the Ring.com devices as Python
objects.

%prep
%autosetup -n python-ring-doorbell-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ring_doorbell

%check
%pyproject_check_import

%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

