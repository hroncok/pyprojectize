%global pypi_name adb-shell

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        12%{?dist}
Summary:        Python implementation for ADB shell and file sync

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/JeffLIrion/adb_shell
Source0:        %{pypi_source adb_shell}
BuildArch:      noarch

%description
Python package implements ADB shell and FileSync functionality.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Python package implements ADB shell and FileSync functionality.

%prep
%autosetup -n adb_shell-%{version}
rm -rf %{pypi_name}.egg-info
# Conflict with crypto
sed -i -e 's/pycryptodome/pycryptodomex/g' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files adb_shell

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.2-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 22 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream release 0.4.2 (closes rhbz#2016651)

* Wed Oct 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream release 0.4.1 (closes rhbz#2013903)

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Update to latest upstream release 0.4.0 (closes rhbz#1929542)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.3-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Update to latest upstream release 0.3.3 (#1929542)

* Mon May 31 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-1
- Update to latest upstream release 0.3.2 (#1929542)

* Wed Feb 17 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream release 0.3.1 (#1929542)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-1
- Update to new upstream release 0.2.3 (#1883034)

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to new upstream release 0.2.2 (#1871369)

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Update to new upstream release 0.2.1 (#1858210)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Update to latest upstream release 0.2.0 (#1858210)

* Wed Jun 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.7-1
- Add license file
- Update to latest upstream release 0.1.7

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-1
- Update to latest upstream release 0.1.4

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Initial package for Fedora
