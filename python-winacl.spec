%global pypi_name winacl

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        13%{?dist}
Summary:        Python ACL/ACE/Security Descriptor manipulation library

License:        MIT
URL:            https://github.com/skelsec/winacl
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Platform independent library for interfacing windows security descriptors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Platform independent library for interfacing windows security descriptors.

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

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.1-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.1-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.10

* Sat Feb 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Update to latest upstream release 0.1.1 (#1933379)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Update to latest upstream release 0.1.0 (#1893024)

* Thu Oct 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Update to latest upstream release 0.0.7 (#1890357)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.6-1
- Update to latest upstream release 0.0.6 (rhbz#1847137)

* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- Update to latest upstream release 0.0.5 (rhbz#1840959)

* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Add license file
- Update to latest upstream release 0.0.4 (rhbz#1840959)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.2-1
- Initial package for Fedora
