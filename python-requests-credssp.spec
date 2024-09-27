%global srcname requests_credssp
%global gh_owner jborean93
%global gh_name requests-credssp


%if 0%{?fedora}
# escaping for EPEL.
%endif

Name:       python-%{gh_name}
Version:    2.0.0
Release:    9%{?dist}
Summary:    Allows for HTTPS CredSSP authentication using the requests library

License:    MIT
URL:        https://github.com/jborean93/requests-credssp
Source0:    https://github.com/%{gh_owner}/%{gh_name}/archive/v%{version}.tar.gz#/%{gh_name}-%{version}.tar.gz
BuildArch:  noarch

%if 0%{?fedora}
%else
BuildRequires:  pyOpenSSL
%endif

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-cryptography
BuildRequires:  python3-requests
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-pyasn1
BuildRequires:  python3-ntlm-auth
BuildRequires:  python3-spnego
%description
This package allows for HTTPS CredSSP authentication using the requests
library. CredSSP is a Microsoft authentication that allows your credentials
to be delegated to a server giving you double hop authentication.

%package -n python3-%{gh_name}
Requires:  python3-cryptography
Requires:  python3-requests
Requires:  python3-pyOpenSSL
Requires:  python3-pyasn1
Requires:  python3-ntlm-auth
Summary:  Python 3 credssp library
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{gh_name}
This package allows for HTTPS CredSSP authentication using the requests
library. CredSSP is a Microsoft authentication that allows your credentials
to be delegated to a server giving you double hop authentication.

%prep
%autosetup -n %{gh_name}-%{version}
# Remove bundled egg-info, it's not there yet but just in case it gets added upstream
rm -rf %{gh_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{pytest} -k "not test_invalid_auth_mechanism"

%files -n python3-%{gh_name}
%license LICENSE
%doc CHANGELOG.md README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0 (closes rhbz#2055219)

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0 (closes rhbz#2016658)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Subpackage python2-requests-credssp has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon May 21 2018 James Hogarth <james.hogarth@gmail.com> - 1.0.0-1
- Initial package
