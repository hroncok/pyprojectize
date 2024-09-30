Name:          zezere
Version:       0.5.2
Release:       7%{?dist}
Summary:       A provisioning service for Fedora IoT
License:       MIT
URL:           https://github.com/fedora-iot/zezere
Source0:       https://github.com/fedora-iot/zezere/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: systemd

%description
Zezere is a provisioning service for Fedora IoT. It can be used for deploying
Fedora IoT to devices without needing a physical console.

%package ignition
Summary: Ignition client for Zezere
Requires: python3-setuptools
Requires: ignition

%description ignition
An Ignition client for Zezere managed systems.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l zezere

install zezere_ignition/__init__.py %{buildroot}/usr/bin/zezere-ignition
chmod +x %{buildroot}/usr/bin/zezere-ignition
mkdir -p %{buildroot}%{_unitdir}
install zezere_ignition/zezere_ignition* %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sharedstatedir}/zezere
mkdir -p %{buildroot}%{_sysconfdir}/issue.d/
ln -s /run/zezere-ignition-banner %{buildroot}%{_sysconfdir}/issue.d/zezere_ignition.issue

%files -f %{pyproject_files}
%{_sharedstatedir}/zezere
%{_bindir}/zezere-manage

%files ignition
%{_bindir}/zezere-ignition
%{_sysconfdir}/issue.d/zezere_ignition.issue
%{_unitdir}/*

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.2-6
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5-11
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5-8
- Rebuilt for Python 3.10

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Adam Williamson <awilliam@redhat.com> - 0.5-5
- Backport patch to show all unclaimed devices to admins in web UI
- Also include the fixtures in the package as they're necessary

* Mon Jul 13 2020 Adam Williamson <awilliam@redhat.com> - 0.5-4
- Install the HTML template files (#1855927)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5-3
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5-2
- Update to 0.5

* Wed Apr 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4-2
- Fix ignition keys fragment merging (rhbz 1820614)

* Tue Apr  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.4-1
- Update to 0.4

* Fri Mar 20 2020 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.3-2
- Backport /usr/lib/zezere-ignition-url patch

* Tue Mar 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3-1
- Update to 0.3

* Fri Feb 21 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.2-2
- new upstream release: 0.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec  5 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-2
- Review fixes and updates

* Thu Dec  5 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-1
- Initial package
