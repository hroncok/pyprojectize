%bcond_without tests

%global pretty_name openant
%global extract_name ant

%global _description %{expand:
A python library to download and upload files from ANT-FS 
compliant devices (Garmin products).Any compliant ANT-FS 
device should in theory work, but those specific devices 
have been reported as working: Garmin Forerunner 60,
Garmin Forerunner 405CX, Garmin Forerunner 310XT, Garmin 
Forerunner 610, Garmin Forerunner 910XT, Garmin FR70, 
Garmin Swim}

Name:           python-%{pretty_name}
Version:        1.3.1
Release:        5%{?dist}
Summary:        A python library to communicate with ANT-FS compliant devices

License:        MIT
URL:            https://github.com/Tigge/openant
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz
Source2:        ant-usb-sticks.rules

BuildArch:      noarch

# For udev-rules	
BuildRequires:  systemd

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pyusb}
BuildRequires:  %{py3_dist pytest}

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%{!?_udevrulesdir: %global _udevrulesdir %{_sysconfdir}/udev/rules.d}

%pyproject_install
mkdir -pm 755 %{buildroot}/%{_udevrulesdir}	
install -pm 644 %{SOURCE2} %{buildroot}/%{_udevrulesdir}

%check
%{pytest}

%post
%udev_rules_update

%postun
%udev_rules_update

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}.dist-info
%{python3_sitelib}/%{extract_name}
%{python3_sitelib}/%{pretty_name}
%{_bindir}/openant
%config(noreplace) %{_udevrulesdir}/*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 6 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 1.3.1-1
- Update to 1.3.1

* Thu Nov 16 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 1.3.0-1
- Update to 1.3.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.12

* Wed Feb 1 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.2.1-1
- Update to 1.2.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.4-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4-4
- Rebuilt for Python 3.10

* Sun Mar 28 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-3
- Added macro for udev rules update

* Sat Mar 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-2
- Cosmetic changes

* Fri Feb 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-1
- Added comment for patch
- Fixed Unowned Directories

* Mon Feb 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4-1
- Initial package
