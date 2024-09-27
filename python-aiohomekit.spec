%global pypi_name aiohomekit

Name:           python-%{pypi_name}
Version:        0.2.60
Release:        15%{?dist}
Summary:        Python HomeKit client

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/Jc2k/aiohomekit
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This library implements the HomeKit protocol for controlling Homekit
accessories.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library implements the HomeKit protocol for controlling Homekit
accessories.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{_bindir}/aiohomekitctl
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.60-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.60-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.60-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.60-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.60-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.60-1
- Update to latest upstream release 0.2.60 (#1905103)

* Fri Nov 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.57-1
- Update to latest upstream release 0.2.57 (#1896737)

* Sun Nov 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.55-1
- Update to latest upstream release 0.2.55 (#1895136)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.54-1
- Update to latest upstream release 0.2.54 (#1882732)

* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.52-1
- Update to latest upstream release 0.2.52 (#1878686)

* Sat Aug 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.51-1
- Update to latest upstream release 0.2.51

* Mon Aug 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.50-1
- LICENSE file is now present (rhbz#1871908)

* Mon Aug 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.49-1
- Initial package for Fedora
