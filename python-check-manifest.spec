%global pypi_name check-manifest

Name:           python-%{pypi_name}
Version:        0.48
Release:        13%{?dist}
Summary:        Check MANIFEST.in in a Python source package

License:        MIT
URL:            https://github.com/mgedmin/check-manifest
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch:          Replace-deprecated-mock-with-unittest.mock.patch
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  gpg

%description
Check MANIFEST.in in a Python source package for completeness to avoid the
upload of broken packages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-tomli
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-build
BuildRequires:  python3-wheel
 
%description -n python3-%{pypi_name}
Check MANIFEST.in in a Python source package for completeness to avoid the
upload of broken packages.

%package -n     %{pypi_name}
Summary:        CLI tool to check MANIFEST.in files

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{pypi_name}
Command-line tool to check MANIFEST.in files.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' check_manifest.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l check_manifest

%check
%pytest -v tests.py -k "not vcs and not git and not sdist"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGES.rst

%files -n %{pypi_name}
%{_bindir}/check-manifest

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.48-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Maxwell G <maxwell@gtmx.me> - 0.48-9
- Remove python3-mock test dependency

* Mon Oct 30 2023 Miro Hrončok <mhroncok@redhat.com> - 0.48-8
- Remove unused build dependency on python3-pep517
- The python3-build package replaced it in 0.45

* Wed Aug 02 2023 Sandro Mani <manisandro@gmail.com> - 0.48-7
- BR: python3-tomli (#2142070)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.48-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.48-2
- Rebuilt for Python 3.11

* Fri Mar 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.48-1
- Update to latest upstream release 0.48 (closes rhbz#2063514)

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.47-1
- Update to latest upstream release 0.47 (closes rhbz#1893382)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.45-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.45-1
- Update to latest upstream release 0.45 (#1893382)

* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.44-1
- Update to latest upstream release 0.44 (#1884888)

* Thu Sep 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.43-1
- Update to latest upstream release 0.43 (#1881152)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.42-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.42-1
- Update to latest upstream release 0.42 (rhbz#1830740)

* Sat Apr 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.41-1
- Fix build issue (rhbz#1818596)
- Update to latest upstream release 0.41

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.40-2
- Adjust BR (rhbz#1790080)

* Wed Jan 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.40-1
- Initial package for Fedora
