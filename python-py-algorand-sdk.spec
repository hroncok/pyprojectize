%global pypi_name py-algorand-sdk
Name:           python-%{pypi_name}
Version:        2.6.1
Release:        2%{?dist}
Summary:        Algorand Python SDK
License:        MIT

URL:            https://github.com/algorand/py-algorand-sdk
Source0:        https://github.com/algorand/py-algorand-sdk/archive/v%{version}/py-algorand-sdk-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/algorand/py-algorand-sdk/develop/LICENSE

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pynacl
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-msgpack


%description
A python library for interacting with the Algorand network.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A python library for interacting with the Algorand network.

%prep
%setup -q -n %{pypi_name}-%{version}


%build
%py3_build

cp %{SOURCE1} .

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/algosdk
%{python3_sitelib}/py_algorand_sdk-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.6.1-1
- 2.6.1

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.13

* Wed Jun 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-1
- 2.6.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-1
- 2.5.0

* Thu Aug 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-1
- 2.4.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0-1
- 2.3.0

* Mon May 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.2.0-1
- 2.2.0

* Thu Mar 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.1.2-1
- 2.1.2

* Mon Mar 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.1.1-1
- 2.1.1

* Wed Mar 15 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-1
- 2.1.0

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-1
- 2.0.0

* Mon Dec 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.20.2-1
- 1.20.2

* Thu Nov 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.20.1-1
- 1.20.1

* Wed Nov 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.20.0-1
- 1.20.0

* Wed Oct 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.19.0-1
- 1.19.0

* Mon Sep 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.18.0-1
- 1.18.0

* Thu Aug 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.16.1-1
- 1.16.1

* Mon Jul 25 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.16.0-1
- 1.16.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.15.0-1
- 1.15.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.13.1-2
- Rebuilt for Python 3.11

* Thu May 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.13.1-1
- 1.13.1

* Mon May 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.13.0-1
- 1.13.0

* Thu Apr 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12.0-1
- 1.12.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.8.0-1
- 1.8.0

* Wed Aug 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.7.0-1
- 1.7.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-1
- 1.6.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.10

* Thu Apr 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-1
- 1.5.0

* Tue Mar 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- Initial package.

