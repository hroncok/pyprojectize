%global pypi_name msldap

Name:           python-%{pypi_name}
Version:        0.3.26
Release:        13%{?dist}
Summary:        Python library to play with MS LDAP

License:        MIT
URL:            https://github.com/skelsec/msldap
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python library to play with MS LDAP.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Python library to play with MS LDAP.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/msldap*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.26-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.26-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.26-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.26-2
- Rebuilt for Python 3.10

* Sat Feb 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.26-1
- Update to latest upstream release 0.3.26 (#1933380)

* Thu Feb 11 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.25-1
- Update to latest upstream release 0.3.25 (#1926507)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.24-1
- Update to latest upstream release 0.3.24 (#1914691)

* Fri Jan 15 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.23-1
- Update to latest upstream release 0.3.23 (#1914691)

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.22-1
- Update to latest upstream release 0.3.22 (#1893531)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.21-1
- Update to latest upstream release 0.3.21 (#1893531)

* Mon Nov 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.20-1
- Update to latest upstream release 0.3.20 (#1893531)

* Fri Oct 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.17-1
- Update to latest upstream release 0.3.17 (#1893066)

* Thu Oct 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.16-1
- Update to latest upstream release 0.3.16 (#1885156)

* Mon Oct 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.15-1
- Update to latest upstream release 0.3.15 (#1885156)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.14-1
- Update to latest upstream release 0.3.14 (#1882046)

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.13-1
- Update to latest upstream release 0.3.13 (#1879299)

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.12-1
- Update to latest upstream release 0.3.12 (#1876056)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.11-1
- Update to latest upstream release 0.3.11 (#1851635)

* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.10-1
- Update to latest upstream release 0.3.10 (#1851635)

* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.9-1
- Update to latest upstream release 0.3.9 (#1849548)

* Thu Jun 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.8-1
- Update to latest upstream release 0.3.8 (#1833839)

* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-1
- Update to latest upstream release 0.3.6 (#1833839)

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Update to latest upstream release 0.3.5 (#1833839)

* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Update to latest upstream release 0.3.4 (#1833839)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.14-3
- Rebuilt for Python 3.9

* Thu May 14 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.14-2
- include a patch to work with newer prompt_toolkit

* Tue Apr 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.14-1
- Update to latest upstream release 0.2.14 (#1825710)

* Wed Apr 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.13-1
- Update to latest upstream release 0.2.13 (#1815002)

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.12-1
- Update to latest upstream release 0.2.12 (#1815002)

* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.11-1
- Update to latest upstream release 0.2.11 (#1815002)

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.10-1
- LICENSE file is no in the source tarball
- Update to latest upstream release 0.2.10 (#1815002)

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Update to latest upstream release 0.2.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-2
- Fix requirement (#1790355)

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-1
- Initial package
