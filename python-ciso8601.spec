%global pypi_name ciso8601

Name:           python-%{pypi_name}
Version:        2.3.1
Release:        5%{?dist}
Summary:        Fast ISO8601 date time parser

License:        MIT
URL:            https://github.com/closeio/ciso8601
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%description
ciso8601 converts ISO 8601 or RFC 3339 date time strings into Python
datetime objects. Since it's written as a C module, it is much faster
than other Python libraries.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
ciso8601 converts ISO 8601 or RFC 3339 date time strings into Python
datetime objects. Since it's written as a C module, it is much faster
than other Python libraries.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.1-1
- Update to latest upstream release 2.3.1 (closes rhbz#2155669)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release 2.2.0 (rhbz#1991039)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-2
- Enable debug output (rhbz#1875860)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Initial package for Fedora
