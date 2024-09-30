%global pypi_name convertdate

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        9%{?dist}
Summary:        Python module to convert date formats and calculating holidays

License:        MIT
URL:            https://github.com/fitnr/convertdate
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Converts between Gregorian dates and other calendar systems. Calendars 
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic, ISO, 
Julian, Mayan and Persian.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz
BuildRequires:  python3-ephem
BuildRequires:  python3-pymeeus

%description -n python3-%{pypi_name}
Converts between Gregorian dates and other calendar systems. Calendars 
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic, ISO, 
Julian, Mayan and Persian.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests -k "not testPersian"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc HISTORY.rst README.md
%{_bindir}/censusgeocode

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.4.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Update to latest upstream release 2.4.0 (closes rhbz#2043954)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.2-1
- Update to latest upstream release 2.3.2 (rhbz#1929762)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 2.3.1-2
- Rebuilt for Python 3.10

* Wed Feb 17 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.1-1
- Update to latest upstream release 2.3.1 (#1929762)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-1
- Update to latest upstream release 2.3.0 (#1895601)

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.2-1
- Update to latest upstream release 2.2.2 (#1880240)

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-7
- Enable dependency generator

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-5
- Add python3-setuptools as BR

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-2
- Add additional requirements manually (rhbz#1792034)

* Tue Oct 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release 2.2.0

* Thu Sep 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-2
- Update summary (rhbz#1748938)

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Initial package for Fedora
