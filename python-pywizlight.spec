%global pypi_name pywizlight

Name:           python-%{pypi_name}
Version:        0.5.14
Release:        9%{?dist}
Summary:        Python connector for WiZ light devices

License:        MIT
URL:            https://github.com/sbidy/pywizlight
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python connector for WiZ light devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python connector for WiZ light devices.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/wizlight
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.14-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.14-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.14-1
- Update to latest upstream release 0.5.14 (closes rhbz#2095142)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.13-2
- Rebuilt for Python 3.11

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.13-1
- Update to latest upstream release 0.5.13 (closes rhbz#2057390)

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.12-1
- Update to latest upstream release 0.5.12 (closes rhbz#2051126)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.16-1
- Update to latest upstream release 0.4.16 (closes rhbz#2023978)

* Sat Oct 23 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.12-1
- Update to latest upstream release 0.4.12 (closes rhbz#2016689)

* Fri Oct 22 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.10-1
- Update to latest upstream release 0.4.10 (closes rhbz#2016662)

* Fri Oct 22 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.9-1
- Update to latest upstream release 0.4.9 (closes rhbz#2016662)

* Wed Oct 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.8-1
- Update to latest upstream release 0.4.8 (closes rhbz#2015294)

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.7-1
- Update to latest upstream release 0.4.7 (rhbz#1927463)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.5-2
- Rebuilt for Python 3.10

* Thu Feb 11 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.5-1
- Update to latest upstream release 0.4.5 (#1927463)

* Fri Feb 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.4-1
- Update to latest upstream release 0.4.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream release 0.4.1 (#1910904)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.8-1
- Update to latest upstream release 0.3.8 (#1910904)

* Sat Dec 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.7-1
- Update to latest upstream release 0.3.7 (#1910904)

* Sat Dec 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-1
- Update to new upstream version 0.3.6 (#1908355)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Update to new upstream version 0.3.5

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Update to new upstream version 0.3.4 (#1884993)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Initial package for Fedora
