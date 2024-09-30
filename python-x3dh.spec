Name:           python-x3dh
Version:        1.0.4
Release:        1%{?dist}
Summary:        Python implementation of the X3DH key agreement protocol

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-cryptography
BuildRequires:  python3-xeddsa
# For tests
# "nacl" is also a runtime requirement
BuildRequires:  python3-pynacl
#BuildRequires:  python3-pytest

%description
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.



%package     -n python3-x3dh
Summary:        Python implementation of the X3DH key agreement protocol
Requires:       python3-pynacl

%description -n python3-x3dh
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.



%prep
%autosetup -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files x3dh



%files -n python3-x3dh -f %{pyproject_files}
%license LICENSE
%doc README.md
# For noarch packages: sitelib



%changelog
* Thu Sep 19 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.13

* Mon May 20 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- Fix typo in %%changelog
- Remove patch and tests suite

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.5.9~beta-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9~beta-10
- Add explicit build dependancy on python3-setuptools (RHBZ#2142043)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.5.9~beta-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9~beta-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.9~beta-5
- Rebuilt for Python 3.10

* Sat Apr 17 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9~beta-4
- Package Review RHBZ#1916510:
  - Short the Summary
  - Add nacl python module as build requirement and runtime requirement
  - Use %%pytest to run tests suite

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9~beta-3
- Package Review RHBZ#1916510:
  - Add more explicit description
  - Remove %%{srcname} variable truely used once
  - Fix the Version tag to match upstream version
  - Use %%{python3_version} in %%files section

* Mon Jan 18 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9-2
- Add Patch0 to fix installation package
  Backport from upstream commit: a38d9ecf

* Thu Dec 10 2020 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.9-1
- Initial package
