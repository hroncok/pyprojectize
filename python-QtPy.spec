%global pypi_name QtPy
%global simple_name qtpy

Name:           python-%{pypi_name}
Version:        2.4.1
Release:        %autorelease
Summary:        Provides an abstraction layer on top of the various Qt bindings

# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://github.com/spyder-ide/%{simple_name}
Source0:        https://github.com/spyder-ide/%{simple_name}/archive/v%{version}/%{simple_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description

QtPy (pronounced ‘cutie pie’) is a small abstraction layer that lets you 
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout 
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import qt from 
qtpy instead of PyQt5.

%package -n     python3-%{pypi_name}
Summary:        Provides an abstraction layer on top of the various Qt bindings

%description -n python3-%{pypi_name}

QtPy (pronounced ‘cutie pie’) is a small abstraction layer that lets you 
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout 
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import qt from 
qtpy instead of PyQt5.

%prep
%autosetup -n %{simple_name}-%{version}

rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l qtpy

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/qtpy

%changelog
%autochangelog
