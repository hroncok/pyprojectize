%global srcname getmac

Name:           python-%{srcname}
Version:        0.9.5
Release:        1%{?dist}
Summary:        Python module to get the MAC address of local network interfaces and LAN hosts

License:        MIT
URL:            https://github.com/GhostofGoes/getmac
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-getmac}

%description -n python3-%{srcname}
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
sed -i '1{/^#!\//d}' getmac/__main__.py
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/
/usr/bin/getmac

%changelog
* Mon Jul 22 2024 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.5-1
- Update to 0.9.5 fixes rhbz#2179157

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.2-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.2-3
- Rebuilt for Python 3.12

* Sun Feb 12 2023 Henrik Boeving <hargonix@gmail.com> - 0.9.2-2
- Upstream no longer ships manpages

* Sun Feb 12 2023 Henrik Boeving <hargonix@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Henrik Boeving <hargonix@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.10

* Tue May 25 2021 Henrik Boeving <hargonix@gmail.com> - 0.8.2-2
- Update to 0.8.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Henrik Boeving <hargonix@gmail.com> - 0.6.0-1
- initial packaging
