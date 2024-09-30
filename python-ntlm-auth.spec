%global srcname ntlm-auth

Name:           python-%{srcname}
Version:        1.5.0
Release:        15%{?dist}
Summary:        Python 3 compatible NTLM library (requires md4, thus legacy OpenSSL settings)

License:        MIT
URL:            https://pypi.python.org/pypi/ntlm-auth
Source:         https://github.com/jborean93/ntlm-auth/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# For tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist cryptography}

%global _description %{expand:
This package allows Python clients running on any operating system to provide
NTLM authentication to a supporting server.

With OpenSSL 3 or above, the legacy OpenSSL provider needs to be set in
order to support md4 in Python.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-ntlm3 < 1.0.3-1
Provides:       python3-ntlm3 = %{version}-%{release}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ntlm_auth

%check
# see https://github.com/jborean93/ntlm-auth/issues/22
cat > openssl.cnf << EOF
openssl_conf = openssl_init

[openssl_init]
providers = provider_sect

[provider_sect]
default = default_sect
legacy = legacy_sect

[default_sect]
activate = 1

[legacy_sect]
activate = 1
EOF
export OPENSSL_CONF=${PWD}/openssl.cnf

%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.md README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.0-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.5.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Maxwell G <gotmax@e.email> - 1.5.0-8
- Fix license (the project was relicensed to MIT 5 years ago)
- Tweak description

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.5.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Joel Capitao <jcapitao@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Subpackage python2-ntlm-auth has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 James Hogarth <james.hogarth@gmail.com> = 1.1.0-1
* Upstream update to 1.1.0
* Mon Oct 10 2016 James Hogarth <james.hogarth@gmail.com> - 1.0.2-1
- Initial package.
