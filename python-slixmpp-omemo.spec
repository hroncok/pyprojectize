# set upstream name variable
%global srcname slixmpp_omemo


Name:           python-slixmpp-omemo
Version:        0.9.1
Release:        3%{?dist}
Summary:        OMEMO plugin for Slixmpp

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://codeberg.org/poezio/slixmpp-omemo
Source0:        https://codeberg.org/poezio/slixmpp-omemo/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-slixmpp
BuildRequires:  python3-omemo
# for tests
#BuildRequires:  python3-pytest

%description
This library provides an interface between python-omemo and
python-slixmpp.



%package     -n python3-slixmpp-omemo
Summary:        OMEMO plugin for Slixmpp

%description -n python3-slixmpp-omemo
This library provides an interface between python-omemo and
python-slixmpp.



%prep
%autosetup -n slixmpp-omemo
# Remove shebang in 3 non-executable files
find ./%{srcname}/ -type f '(' -name __init__.py -o -name stanza.py -o -name version.py ')' -ls -exec sed -i 's@#!/usr/bin/env python3@@' '{}' \;


%build
%py3_build


%install
%py3_install


%check
# no tests to run with pytest: Disabling.



%files -n python3-slixmpp-omemo
%license LICENSE
%doc CONTRIBUTING.rst ChangeLog README.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/



%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 22 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1
- Update URL and SourcesURL tags
- Remove python3-omemo-backend-signal as BuildRequires

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0
- Update SourcesURL
- Fix %%autosetup in %%prep section

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 24 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-3
- Rebuilt for Python 3.10

* Fri Apr 2 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.4.0-2
- Package Review RHBZ#1928004:
  - Remove shebang in non-executable scripts in %%prep section

* Thu Feb 11 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.4.0-1
- Initial package
