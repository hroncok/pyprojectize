Name: ServiceReport
Version: 2.2.4
Release: 3%{?dist}
Summary: A tool to validate and repair First Failure Data Capture (FFDC) configuration

License: GPL-2.0-or-later
URL: https://github.com/linux-ras/ServiceReport
Source0: https://github.com/linux-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel python3-setuptools
BuildRequires: systemd-rpm-macros

%description
ServiceReport is a python based tool that investigates the incorrect
First Failure Data Capture (FFDC) configuration and optionally repairs
the incorrect configuration

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%post
%systemd_post servicereport.service

%preun
%systemd_preun servicereport.service

%postun
%systemd_postun servicereport.service

%files
%doc README.md
%license COPYING
%{_mandir}/man8/*
%{_bindir}/servicereport
%{_unitdir}/servicereport.service
%{python3_sitelib}/servicereportpkg
%{python3_sitelib}/ServiceReport*.egg-info

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.4-2
- Rebuilt for Python 3.13

* Wed Feb 28 2024 Than Ngo <than@redhat.com> - 2.2.4-1
- bz#2266558, update to 2.2.4

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.3-3
- Rebuilt for Python 3.12

* Mon Jun 12 2023 Than Ngo <than@redhat.com> - 2.2.3-2
- migrated to SPDX license

* Wed Mar 29 2023 Than Ngo <than@redhat.com> - 2.2.3-1
- Fixed #1978490, update to 2.2.3

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.2-8
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.2-5
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Vasant Hegde <hegdevasant@linux.ibm.com> - 2.2.2-3
- Initial Fedora version

* Thu Jul 02 2020 Sourbh Jain <sourabhjain@linux.ibm.com> 2.2.2-2
- Update data files of the project

* Thu May 14 2020 Sourabh Jain <sourabhjain@linux.ibm.com> 2.2.2-1
- Update crashkernel memory reservation limit
- Remove rpm postscript
- Add servicereport.spec file
- Move systemd service file to a generic location
- Run service only once at boot time without repair action
- fix initrd repair function
- [fadump] No boolean return from check_* function
- [fadump] indent the code with spaces instead of tabs
- Fix the option_string for --plugin option
- [fadump] update the logic to extract the FADump mem reservation
- Add irqbalance daemon check
- Add irqbalance package check
- Fix the system platform string extraction from /proc/cpuinfo
- Fix powerpc-ibm-utils package name
- Fix typo in README.md

* Fri Nov 15 2019 Sourabh Jain <sourabhjain@linux.ibm.com> 2.2.1-1
- First Open source release
- Initial Commit of Open Source release
