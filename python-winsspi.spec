%global pypi_name winsspi

Name:           python-%{pypi_name}
Version:        0.0.9
Release:        16%{?dist}
Summary:        Windows SSPI library in Python

License:        MIT
URL:            https://github.com/skelsec/winsspi
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Windows SSPI wrapper in pure Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Windows SSPI wrapper in pure Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' winsspi/common/defines.py
sed -i "s|\r||g" README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.9-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.9-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.9-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.9-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.9-2
- Rebuilt for Python 3.9

* Wed Apr 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.9-1
- Update to latest upstream release 0.0.9 (rhbz#1821092)

* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.8-1
- Update to latest upstream release 0.0.8 (rhbz#1821092)

* Mon Mar 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Use LICENSE file shipped in source tarball
- Update to latest upstream release 0.0.7 (rhbz#1814977)

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- Update to latest upstream release 0.0.5 (rhbz#1814977)

* Tue Jan 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-2
- Fix ownership

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-1
- Initial package for Fedora
