%global pypi_name AWSIoTPythonSDK

Name:           python-%{pypi_name}
Version:        1.4.9
Release:        15%{?dist}
Summary:        SDK for connecting to AWS IoT using Python

# ASL 2.0: main library
# EPL-1.0: core/protocol/paho
# Automatically converted from old format: ASL 2.0 and EPL-1.0 - review is highly recommended.
License:        Apache-2.0 AND EPL-1.0
URL:            https://github.com/aws/aws-iot-device-sdk-python
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The AWS IoT Device SDK for Python allows developers to write Python script to
use their devices to access the AWS IoT platform through MQTT or MQTT over the
WebSocket protocol. By connecting their devices to AWS IoT, users can securely
work with the message broker, rules, and the device shadow (sometimes referred
to as a thing shadow) provided by AWS IoT and with other AWS services like AWS
Lambda, Amazon Kinesis, Amazon S3, and more.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
The AWS IoT Device SDK for Python allows developers to write Python script to
use their devices to access the AWS IoT platform through MQTT or MQTT over the
WebSocket protocol. By connecting their devices to AWS IoT, users can securely
work with the message broker, rules, and the device shadow (sometimes referred
to as a thing shadow) provided by AWS IoT and with other AWS services like AWS
Lambda, Amazon Kinesis, Amazon S3, and more.

%prep
%autosetup -n aws-iot-device-sdk-python-%{version}
chmod -x {LICENSE.txt,README.rst,samples/*/*.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst samples/

%changelog
* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.9-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.9-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.9-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.9-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.9-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.9-1
- Update to latest upstream release 1.4.9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.8-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.8-2
- Update license details

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.8-1
- Fix prep section
- Fix source URL (rhbz#1787304)
- Update to latest upstream release 1.4.8

* Thu Jan 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.7-1
- Initial package for Fedora
