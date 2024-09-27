%global pypi_name adafruit-pureio

Name:           python-%{pypi_name}
Version:        1.1.10
Release:        7%{?dist}
Summary:        Python access to Linux IO including I2C and SPI

License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PureIO
Source0:        %{pypi_source Adafruit_PureIO}
BuildArch:      noarch

%description
Pure Python (i.e. no native extensions) access to Linux IO
including I2C and SPI. Drop in replacement for smbus and
spidev modules.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools-scm)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pure Python (i.e. no native extensions) access to Linux IO
including I2C and SPI. Drop in replacement for smbus and
spidev modules.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for adafruit-pureio

BuildRequires:  python3dist(sphinx)

%description -n python-%{pypi_name}-doc
Documentation for adafruit-pureio.

%prep
%autosetup -n Adafruit_PureIO-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%ifarch %{arm} %{arm64}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/Adafruit_PureIO
%{python3_sitelib}/Adafruit_PureIO-%{version}.dist-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.10-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1.10-2
- Rebuilt for Python 3.12

* Sat Feb 18 2023 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.10-1
- Update to latest upstream release 1.1.10 (closes rhbz#2168356)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.9-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.9-1
- Update to latest upstream release 1.1.9 (rhbz#1971707)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.8-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.8-1
- Update to latest upstream release 1.1.8 (#1905102)

* Mon Oct 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.7-1
- Initial package for Fedora
