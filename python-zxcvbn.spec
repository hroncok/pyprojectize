%global srcname zxcvbn-python

Name: python-zxcvbn
Summary: Realistic password strength estimator python module
Version: 4.4.28
Release: 14%{?dist}
License: MIT
URL: https://github.com/dwolfhub/zxcvbn-python
Source: https://github.com/dwolfhub/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: pytest

%global _description %{expand:
A realistic password strength estimator.

This is a Python implementation of the library created by the team at Dropbox.
The original library was written for JavaScript.

Accepts user data to be added to the dictionaries that are tested against
(name, birthdate, etc).  Gives a score to the password, from 0 (terrible)
to 4 (great). It provides feedback on the password and ways to improve it
and returns time estimates on how long it would take to guess the password
in different situations.}
%description %_description

%package -n python3-zxcvbn
Summary: Realistic password strength estimator python3 module

%description -n python3-zxcvbn %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pyproject_check_import
%pytest

%install
%pyproject_install
%pyproject_save_files -l zxcvbn

%files -n python3-zxcvbn -f %{pyproject_files}
%doc README.rst
%{_bindir}/zxcvbn

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.4.28-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.4.28-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.4.28-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.28-3
- Rebuilt for Python 3.10

* Sun May 30 2021 Paul Wouters <paul.wouters@aiven.io> - 4.4.28-2
- Resolves: rhbz#1965144 Package review issues

* Thu May 27 2021 Paul Wouters <paul.wouters@aiven.io> - 4.4.28-1
- Initial package
