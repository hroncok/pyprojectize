%global pypi_name pyspiflash

Name:           python-%{pypi_name}
Version:        0.6.3
Release:        16%{?dist}
Summary:        Python SPI data flash device drivers

License:        MIT
URL:            https://github.com/eblot/pyspiflash
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
SPI flash devices, also known as DataFlash are commonly found in embedded
products, to store firmware, microcode or configuration parameters.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
#BuildRequires:  python3-pyftdi

%description -n python3-%{pypi_name}
SPI flash devices, also known as DataFlash are commonly found in embedded
products, to store firmware, microcode or configuration parameters.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l spiflash

# Not running tests as they try to create a device
#%check
#PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} i2cflash/tests/serialeeprom.py

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst spiflash/AUTHORS

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.3-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.3-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.3-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.3-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.3-1
- Update to latest upstream release 0.2.2 (rhbz#1833300)

* Fri Apr 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Update to latest upstream release 0.6.2 (rhbz#1822562)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Update to latest upstream release 0.6.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Initial package for Fedora
