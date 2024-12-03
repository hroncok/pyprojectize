%global pypi_name op1repacker

%global common_description %{expand:
OP-1 Firmware Repacker is the tool for unpacking and repacking OP-1 synthesizer
firmware. This allows you to access and modify the files within the firmware as
well as repacking the files into a valid installable firmware file. Ready made
mods are also included in the tool. Lastly it is also possible to analyze
unpacked firmware to get information such as build version, build time and
date, bootloader version etc.}

Name:           python-%{pypi_name}
Version:        0.2.6
Release:        13%{?dist}
Summary:        Tool for unpacking, modding and repacking OP-1 firmware

License:        MIT
URL:            https://github.com/op1hacks/op1repacker
# PyPI tarball is missing a few files so use GitHub instead
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel

%description
%{common_description}

%package -n     %{pypi_name}
Summary:        %{summary}

%description -n %{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python3|d" -i %{pypi_name}/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n %{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/op1repacker

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.6-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.6-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.6-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.6-1
- Initial package.
