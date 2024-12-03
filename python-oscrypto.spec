# main package is archful to run tests everywhere but produces noarch packages
%global debug_package %{nil}
%bcond_without check
%global pname oscrypto

%global desc %{expand:
Currently the following features are implemented. Many of these should only be
used for integration with existing/legacy systems.

* TLSv1.x socket wrappers
* Exporting OS trust roots
* Encryption/decryption
* Generating public/private key pairs
* Generating DH parameters
* Signing and verification
* Loading and normalizing DER and PEM formatted keys
* Key derivation
* Random byte generation
}

Name: python-%{pname}
Version: 1.3.0
Release: 8%{?dist}
Summary: Compiler-free Python crypto library backed by the OS
License: MIT
URL: https://github.com/wbond/oscrypto
Source0: %{url}/archive/%{version}/%{pname}-%{version}.tar.gz
# https://github.com/wbond/oscrypto/issues/74
Patch0: %{name}-py3.12.patch

%description %{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3-asn1crypto
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
%endif
BuildArch: noarch

%description -n python3-%{pname} %{desc}

%prep
%autosetup -p1 -n %{pname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
#%%py3_build
%pyproject_wheel

%install
#%%py3_install
%pyproject_install
%pyproject_save_files %{pname}

%if %{with check}
%check
%pyproject_check_import

# run only non-network tests
%pytest -k 'not TLSTests'
%endif

%files -n python3-%{pname} -f %{pyproject_files}
%license LICENSE
%doc readme.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Dominik Mierzejewski <dominik@greysector.net> 1.3.0-3
- fix build with python-3.12

* Thu Jun 29 2023 Dominik Mierzejewski <dominik@greysector.net> 1.3.0-2
- use pyproject macros and drop explicit BR: on setuptools
- improve description
- run only non-network tests

* Fri May 06 2022 Dominik Mierzejewski <dominik@greysector.net> 1.3.0-1
- initial build
