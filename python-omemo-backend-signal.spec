Name:           python-omemo-backend-signal
Version:        0.3.1~beta
Release:        9%{?dist}
Summary:        A backend for python-omemo offering compatibility with libsignal

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version_no_tilde}.tar.gz
# For files and directories
%global srcname omemo_backend_signal
%global version_main %(c=%version; echo $c|cut -d~ -f1)

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-x3dh
BuildRequires:  python3-doubleratchet
BuildRequires:  python3-omemo
BuildRequires:  python3-cryptography
BuildRequires:  python3-protobuf
# For tests
#BuildRequires:  python3-pynacl

%description
This library implements a backend for python-omemo offering
compatibility with libsignal (C, Java, JavaScript).

OMEMO is Multi-End Message and Object Encryption protocol and it is an
extension of XMPP protocol.



%package     -n python3-omemo-backend-signal
Summary:        A backend for python-omemo offering compatibility with libsignal

%description -n python3-omemo-backend-signal
This library implements a backend for python-omemo offering
compatibility with libsignal (C, Java, JavaScript).

OMEMO is Multi-End Message and Object Encryption protocol and it is an
extension of XMPP protocol.



%prep
%autosetup -n %{name}-%{version_no_tilde}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# Tests suite has been removed by upstream



%files -n python3-omemo-backend-signal -f %{pyproject_files}
%license LICENSE
%doc README.md
# For noarch packages: sitelib



%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.1~beta-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1~beta-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 0.3.1~beta-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1~beta-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1~beta-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1~beta-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.3.1~beta-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1~beta-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 28 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.3.1~beta-1
- Update to 0.3.1~beta

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0~beta-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.3.0~beta-2
- Rebuilt for Python 3.11

* Sun Apr 24 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.3.0~beta-1
- Update to 0.3.0~beta
- Disabling tests suite which has been removed by upstream in this version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6~beta-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6~beta-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6~beta-3
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.2.6~beta-2
- Package Review RHBZ#1927580:
  - Use %%{python3_version} in %%files section

* Wed Feb 10 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.2.6~beta-1
- Initial package
