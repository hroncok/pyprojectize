%global pypi_name chirpstack-api

Name:           python-%{pypi_name}
Version:        3.9.4
Release:        13%{?dist}
Summary:        Chirpstack Python API

License:        MIT
URL:            https://github.com/brocaar/chirpstack-api
Source0:        %{pypi_source}
BuildArch:      noarch

%description
ChirpStack gRPC API message and service wrappers for Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
ChirpStack gRPC API message and service wrappers for Python.

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
%{python3_sitelib}/chirpstack_api
%{python3_sitelib}/chirpstack_api-%{version}.dist-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.9.4-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.9.4-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.9.4-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.9.4-2
- Rebuilt for Python 3.10

* Mon Mar 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.4-1
- Update to latest upstream release 3.9.4 (#1933686)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.3-1
- Update to latest upstream release 3.9.3 (#1909963)

* Thu Dec 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.2-1
- Update to latest upstream release 3.9.2 (#1909963)

* Tue Dec 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.9.1-1
- Update to latest upstream release 3.9.1

* Fri Dec 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.8.1-1
- Update to latest upstream release 3.8.1

* Tue Sep 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.7-1
- Initial package for Fedora
