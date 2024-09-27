Name:           python-omemo
Version:        1.0.4
Release:        1%{?dist}
Summary:        Python implementation of the OMEMO Encryption protocol

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-cryptography
BuildRequires:  python3-setuptools
BuildRequires:  python3-x3dh
#BuildRequires:  python3-pytest
# For tests
#BuildRequires:  python3-pynacl

%description
This python library offers an open implementation of the OMEMO
Multi-End Message and Object Encryption protocol.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.



%package     -n python3-omemo
Summary:        Python implementation of the OMEMO Encryption protocol
Requires:       python3-doubleratchet

%description -n  python3-omemo
This python library offers an open implementation of the OMEMO
Multi-End Message and Object Encryption protocol.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.



%prep
%autosetup -n %{name}-%{version}


%build
%py3_build


%install
%py3_install


%check
# tests requires python-omemo-backend-signal, that introduce cyclic
# dependancy: Disabling.



%files -n python3-omemo
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/omemo/
%{python3_sitelib}/OMEMO-%{version}-py%{python3_version}.egg-info/



%changelog
* Thu Sep 19 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.13

* Sun Jun 2 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0~beta-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0~beta-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0~beta-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.14.0~beta-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0~beta-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0~beta-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.14.0~beta-2
- Rebuilt for Python 3.11

* Sun Apr 24 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.14.0~beta-1
- Update to 0.14.0~beta

* Wed Mar 9 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.13.0~beta-1
- Update to 0.13.0~beta

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0~beta-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0~beta-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.0~beta-2
- Rebuilt for Python 3.10

* Mon Mar 29 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.12.0~beta-1
- Package Review RHBZ#1926523:
  - Update to 0.12.0
  - Shorten the Summary
  - Disable tests with pytest to avoid cyclic dependancy

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.11.0~beta-3
- Package Review RHBZ#1926523:
  - Fix the Version tag to match upstream version
  - Use %%{python3_version} in %%files section

* Mon Feb 08 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.11.0-2
- Add requirement not added automaticaly in python3 subpackage

* Mon Feb 08 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.11.0-1
- Initial package
