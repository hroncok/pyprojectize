%global srcname virtualbmc

Name: python-%{srcname}
Version: 3.1.0
Release: 7%{?dist}
Summary: A virtual BMC for controlling virtual machines using IPMI commands
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://opendev.org/openstack/virtualbmc
Source0: https://tarballs.opendev.org/openstack/%{srcname}/%{srcname}-%{version}.tar.gz
Source1: 60-vbmcd.rules
Source2: vbmcd.service
Source3: vbmcd.sysusers
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: systemd-rpm-macros
BuildRequires: git
# Documentation
BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme
# Tests
BuildRequires: python3-stestr
BuildRequires: python3-libvirt
BuildRequires: python3-pyghmi
BuildRequires: python3-zmq
BuildRequires: python3-oslotest
BuildRequires: python3-autopage

%description
A virtual BMC for controlling virtual machines using IPMI commands.

%package -n python3-%{srcname}
Summary: A virtual BMC for controlling virtual machines using IPMI commands
Suggests: python3-%{srcname}-doc
Requires(pre): shadow-utils

%description -n python3-%{srcname}
A virtual BMC for controlling virtual machines using IPMI commands.

%package -n python3-%{srcname}-tests
Summary: VirtualBMC tests
Requires: python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-tests
Tests for VirtualBMC.

%package -n python3-%{srcname}-doc
Summary: VirtualBMC documentation

%description -n python3-%{srcname}-doc
Documentation for VirtualBMC.

%prep
%autosetup -n %{srcname}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
sphinx-build-3 -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/polkit-1/rules.d/60-vbmcd.rules
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/vbmcd.service
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/vbmcd.conf
install -d -m 750 %{buildroot}%{_sharedstatedir}/vbmcd

%check
PYTHON=%{__python3} stestr run

%pre -n python3-%{srcname}
%sysusers_create_compat %{SOURCE3}

%post -n python3-%{srcname}
%systemd_post vbmcd.service

%preun -n python3-%{srcname}
%systemd_preun vbmcd.service

%postun -n python3-%{srcname}
%systemd_postun_with_restart vbmcd.service

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/vbmcd
%{_bindir}/vbmc
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.dist-info
%exclude %{python3_sitelib}/%{srcname}/tests
%{_datadir}/polkit-1/rules.d/60-vbmcd.rules
%{_unitdir}/vbmcd.service
%{_sysusersdir}/vbmcd.conf
%dir %attr(750, vbmcd, vbmcd) %{_sharedstatedir}/vbmcd

%files -n python3-%{srcname}-tests
%license LICENSE
%{python3_sitelib}/%{srcname}/tests

%files -n python3-%{srcname}-doc
%license LICENSE
%doc AUTHORS README.rst HACKING.rst CONTRIBUTING.rst ChangeLog
%doc doc/build/html

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 3.1.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Juan Orti Alcaine <jortialc@redhat.com> - 3.1.0-2
- Remove BR python3-mock

* Fri Sep 22 2023 Juan Orti Alcaine <jortialc@redhat.com> - 3.1.0-1
- Version 3.1.0 (RHBZ#2240081)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 3.0.1-2
- Rebuilt for Python 3.12

* Thu Mar 16 2023 Juan Orti Alcaine <jortialc@redhat.com> - 3.0.1-1
- Version 3.0.1 (RHBZ#2176951)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Juan Orti Alcaine <jortialc@redhat.com> - 3.0.0-1
- Version 3.0.0 (#2137838)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Python Maint <python-maint@redhat.com> - 2.2.2-2
- Rebuilt for Python 3.11

* Sat Jun 18 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.2.2-1
- Version 2.2.2 (#2098114)

* Wed Mar 09 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.2.1-5
- Move polkit rule to /usr/share/polkit-1/rules.d

* Thu Jan 27 2022 Juan Orti Alcaine <jortialc@redhat.com> - 2.2.1-4
- BR: python3-autopage

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.2.1-2
- Create vbmcd user with systemd sysusers

* Fri Oct 22 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.2.1-1
- Version 2.2.1 (#1968102)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.10

* Sat Jun 05 2021 Juan Orti Alcaine <jortialc@redhat.com> - 2.2.0-1
- Version 2.2.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-1
- Version 2.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.6.0-1
- Version 1.6.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.5.0-5
- Fix polkit logging

* Sun Jul 14 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.5.0-4
- Fix tests for Fedora 30

* Sun Jul 14 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.5.0-3
- Include html docs
- Run tests

* Thu Jul 11 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.5.0-2
- Include polkit and service unit

* Wed Jul 10 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.5.0-1
- Build only for Python3
- Version 1.5.0

* Tue Feb 13 2018 Maxim Burgerhout <maxim@redhat.com> - 1.2.0-2
- First build for Fedora 27 copr

* Tue Aug 22 2017 Alfredo Moralejo <amoralej@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Tue Nov 15 2016 Lucas Alvares Gomes <lucasagomes@gmail.com> - 0.1.0-1
- Initial package.
