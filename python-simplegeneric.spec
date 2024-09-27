%global pypi_name simplegeneric

Name:           python-simplegeneric
Version:        0.8.1
Release:        %autorelease
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)

# Automatically converted from old format: Python or ZPLv2.1 - review is highly recommended.
License:        LicenseRef-Callaway-Python OR ZPL-2.1
URL:            https://pypi.org/project/simplegeneric/
Source0:        %{pypi_source %{pypi_name} %{version} zip}

BuildArch:      noarch


%description
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.


%package -n python3-%{pypi_name}
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)
# Automatically converted from old format: Python or ZPLv2.1 - review is highly recommended.
License:        LicenseRef-Callaway-Python OR ZPL-2.1
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.



%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=$(pwd) %{__python3} setup.py test


%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/__pycache__/simplegeneric.cpython*
%{python3_sitelib}/simplegeneric.py
%{python3_sitelib}/simplegeneric-%{version}-py%{python3_version}.egg-info/


%changelog
%autochangelog
