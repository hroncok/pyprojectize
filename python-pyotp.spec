%global srcname pyotp

Name:           python-%{srcname}
Version:        2.9.0
Release:        %autorelease
Summary:        Python One Time Password library
BuildArch:      noarch

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/pyotp
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
PyOTP is a Python library for generating and verifying one-time passwords. It
can be used to implement two-factor (2FA) or multi-factor (MFA) authentication
methods in web applications and in other systems that require users to log in.


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
PyOTP is a Python library for generating and verifying one-time passwords. It
can be used to implement two-factor (2FA) or multi-factor (MFA) authentication
methods in web applications and in other systems that require users to log in.


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
%pyproject_check_import

%{__python3} test.py


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
