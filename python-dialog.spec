Name:           python-dialog
Version:        3.5.3
Release:        %autorelease
Summary:        Python interface to the Unix dialog utility

License:        LGPL-2.1-or-later
URL:            http://pythondialog.sourceforge.net
# Upstream releases two tarballs from the same sources
Source0:        %{pypi_source pythondialog}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A Python interface to the Unix dialog utility, designed to provide an
easy, pythonic, and as complete as possible way to use the dialog
features from Python code.}

%description %_description

%package -n python3-dialog
Requires:       dialog
Summary:        %{summary}

%description -n python3-dialog %_description

%prep
%autosetup -n pythondialog-%{version}

find examples -name '*.py' -print -exec sed -r -i 's|(.!)\s+/usr/bin/env python.*|\1%{__python3}|' {} \;

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dialog

%check
%pyproject_check_import
%py3_check_import dialog

%files -n python3-dialog -f %{pyproject_files}
%doc README.rst examples/

%changelog
%autochangelog
