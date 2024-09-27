%global pypi_name testfixtures

Name:           python-%{pypi_name}
Version:        8.3.0
Release:        1%{?dist}
Summary:        Collection of helpers and mock objects for unit tests

License:        MIT
URL:            https://github.com/Simplistix/testfixtures
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%%check
# Upstream has a different idea about how Open Source works
# and is hostile against everything that doesn't match that idea.
# Thus, the only thing that matters is that tests work in their CI

%files -n python3-%{pypi_name}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.egg-info/

%changelog
* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 8.3.0-1
- Update to latest upstream version (closes rhbz#2278108)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.1.0-2
- Rebuilt for Python 3.13

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 8.1.0-1
- Update to latest upstream version 8.1.0 (closes rhbz#2264566)

* Fri Feb 02 2024 Karolina Surma <ksurma@redhat.com> - 7.2.2-4
- Don't build require test dependencies, since tests are not run

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Fabian Affolter <mail@fabian-affolter.ch> - 7.2.2-1
- Update to latest upstream release 7.2.2 (closes rhbz#2139114)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 6.18.5-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 6.18.5-2
- Rebuilt for Python 3.11

* Thu Mar 03 2022 Fabian Affolter <mail@fabian-affolter.ch> - 6.18.5-1
- Update to latest upstream release 6.18.5 (closes rhbz#2059579)

* Fri Feb 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 6.18.4-1
- Update to latest upstream release 6.18.4 (closes rhbz#2058548)
- No longer run tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Fabian Affolter <mail@fabian-affolter.ch> - 6.18.3-1
- Update to latest upstream release 6.18.3 (closes rhbz#2008817)

* Tue Sep 21 2021 Fabian Affolter <mail@fabian-affolter.ch> - 6.18.2-1
- Update to latest upstream release 6.18.2 (closes rhbz#2006200)

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 6.18.1-1
- Update to latest upstream release 6.18.1 (rhbz#1908262)

* Mon Aug 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 6.18.0-1
- Update to latest upstream release 6.18.0 (#1908262)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.17.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.17.0-1
- Update to latest upstream release 6.17.1 (#1908262)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.17.0-1
- Update to latest upstream release 6.17.0 (#1908262)

* Wed Dec 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.16.0-1
- Update to latest upstream release 6.16.0 (#1886668)

* Fri Oct 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.15.0-1
- Update to latest upstream release 6.15.0 (#1886668)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.14.2-1
- Update to latest upstream release 6.14.2 (#1875959)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> -6.14.1-3
- Add python3-setuptools as BR

* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.14.1-2
- Remove *.egg in prep section

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.14.1-1
- Exclude the failing tests for now
- Update to latest upstream release 6.14.1

* Sat Apr 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.14.0-1
- Update to latest upstream release 6.14.0

* Wed Feb 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.13.0-1
- Update to latest upstream release 6.13.0

* Mon Feb 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.12.0-1
- Update to latest upstream release 6.12.0

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.10.3-1
- Update to latest upstream release 6.10.3

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.8.2-2
- Fix license, URL and naming (rhbz#1708161)

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.8.2-1
- New spec file for re-review

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.14.3-5
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Miro Hrončok <mhroncok@redhat.com> - 4.14.3-4
- Fix pytohn2-django requires https://fedoraproject.org/wiki/Changes/Django20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Björn Esser <besser82@fedoraproject.org> - 4.14.3-1
- New upstream release (rhbz#1450930)

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 4.13.5-1
- Initial import (rhbz#1445824)

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 4.13.5-0.2
- Fix E: python-bytecode-wrong-magic-value

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 4.13.5-0.1
- Initial rpm-release (rhbz#1445824)
