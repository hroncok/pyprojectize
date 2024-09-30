%global pypi_name mechanicalsoup

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        3%{?dist}
Summary:        Python library for automating interaction with websites

License:        MIT
URL:            https://mechanicalsoup.readthedocs.io
Source0:        https://github.com/MechanicalSoup/MechanicalSoup/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
MechanicalSoup automatically stores and sends cookies, follows redirects,
and can follow links and submit forms. It doesn't do JavaScript.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-httpbin)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-mock)
BuildRequires:  python3dist(six)

%description -n python3-%{pypi_name}
MechanicalSoup automatically stores and sends cookies, follows redirects,
and can follow links and submit forms. It doesn't do JavaScript.

%prep
%autosetup -n MechanicalSoup-%{version}
rm -rf %{pypi_name}.egg-info
# No linting
sed -i -e 's/--flake8//g' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.13

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream version 1.3.0 (closes rhbz#2219697)
- Fix rhbz#2219756, rhbz#2261581 and rhbz#2232585

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 18 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Update to latest upstream release 1.2.0 (closes rhbz#2127659)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.10

* Sun May 30 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Update to latest upstream release 1.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream release 1.0.0 (#1913059)

* Sat Sep 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Initial package for Fedora
