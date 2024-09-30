Summary:        Secure HTTP request signing using the HTTP Signature draft specification
Name:           python-httpsig-cffi
Version:        15.0.0
Release:        24%{?dist}
License:        MIT
URL:            https://github.com/hawkowl/httpsig_cffi
Source0:        https://files.pythonhosted.org/packages/source/h/httpsig-cffi/httpsig_cffi-%{version}.tar.gz
Patch0:         0001-Fix-cryptography-deprecation-warnings-1.patch
BuildArch:      noarch 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(six)
%description
Sign HTTP requests with secure signatures according to the IETF HTTP
Signatures specification (Draft 3_). This is a fork of the fork of the
original module that was made to fully support both RSA and HMAC
schemes as well as unit test both schemes to prove they work. This
particular fork moves from PyCrypto to Cryptography, which provides
PyPy support.

%package -n     python3-httpsig-cffi
Summary:        %{summary}
Requires:       python3dist(cryptography)
Requires:       python3dist(requests)
Requires:       python3dist(six)
%description -n python3-httpsig-cffi
Sign HTTP requests with secure signatures according to the IETF HTTP
Signatures specification (Draft 3_). This is a fork of the fork of the
original module that was made to fully support both RSA and HMAC
schemes as well as unit test both schemes to prove they work. This
particular fork moves from PyCrypto to Cryptography, which provides
PyPy support.

%prep
%autosetup -p1 -n httpsig_cffi-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files httpsig_cffi
rm -rf %{buildroot}%{python3_sitelib}/httpsig_cffi/tests

%check
%{__python3} setup.py test

%files -n python3-httpsig-cffi -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 15.0.0-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 15.0.0-19
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Terje Rosten <terje.rosten@ntnu.no> - 15.0.0-16
- Add patch to fix 3.11 issue (rhbz#2098970)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 15.0.0-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 15.0.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-2
- Rebuilt for Python 3.7

* Wed Jun 06 2018 Terje Rosten <terje.rosten@ntnu.no> - 15.0.0-1
- Initial package
