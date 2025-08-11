%global srcname netdisco

Name:           python-netdisco
Version:        3.0.0
Release:        10%{?dist}
Summary:        Python library to scan local network for services and devices

License:        MIT
URL:            https://github.com/home-assistant/netdisco
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-zeroconf
BuildRequires:  python3-requests
BuildRequires:  python3-pytest

%description
NetDisco is a Python 3 library to discover local devices and services. It
allows to scan on demand or offer a service that will scan the network in
the background in a set interval.

Current methods of scanning:
- mDNS (includes Chromecast, Homekit)
- uPnP
- Plex Media Server using Good Day Mate protocol
- Logitech Media Server discovery protocol
- Daikin discovery protocol
- Web OS discovery protocol

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-zeroconf
Requires:       python3-requests
%py_provides    python3-%{name}

%description -n python3-%{srcname}
NetDisco is a Python 3 library to discover local devices and services. It
allows to scan on demand or offer a service that will scan the network in
the background in a set interval.

Current methods of scanning:
- mDNS (includes Chromecast, Homekit)
- uPnP
- Plex Media Server using Good Day Mate protocol
- Logitech Media Server discovery protocol
- Daikin discovery protocol
- Web OS discovery protocol

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%{pytest} -v tests --ignore "tests/test_xboxone.py"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.0.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.11

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Update to latest upstream release 3.0.0 (closes rhbz#2009913)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.0-1
- Update to latest upstream release 2.9.0 (rhbz#1958196)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.8.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.8.2-1
- Update to latest upstream release 2.8.2 (rhbz#1852280)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.1-1
- Update to latest upstream release 2.7.1 (rhbz#1848247)

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-1
- Update to latest upstream release 2.7.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.0-2
- Remove requirement

* Wed Apr 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.0-1
- Update to latest upstream release 2.6.0

* Mon Mar 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.0-1
- Update to latest upstream release 2.5.0

* Mon Mar 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Update to latest upstream release 2.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release 2.2.0

* Wed Aug 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to latest upstream release 1.5.0

* Mon Jun 11 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream release 1.4.1

* Tue May 29 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-2
- Fix check

* Mon Mar 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Initial package
