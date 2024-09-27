# set upstream name variable
%global srcname poezio_omemo


Name:           poezio-omemo
Version:        0.7.0
Release:        3%{?dist}
Summary:        OMEMO plugin for the Poezio XMPP client

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://codeberg.org/poezio/poezio-omemo
Source0:        https://codeberg.org/poezio/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
#BuildRequires:  python3-pytest

%description
This plugin provides OMEMO support for Poezio client.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.



%prep
%autosetup -n %{name}
# Remove shebang in 2 non-executable files
find ./%{srcname}/ -type f '(' -name __init__.py -o -name version.py ')' -ls -exec sed -i 's@#!/usr/bin/env python3@@' '{}' \;


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
# no tests to run with pytest



%files
%license LICENSE
%doc README.rst ChangeLog CONTRIBUTING.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/



%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0
- Update SourcesURL

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.0-9
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.11

* Tue Apr 26 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.10

* Thu May 20 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Apr 28 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.3.0-2
- Package Review RHBZ#1942312:
  - Remove shebang in non-executable scripts in %%prep section

* Tue Mar 23 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.3.0-1
- Initial package
