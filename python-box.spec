%global pypi_name box

Name:           python-%{pypi_name}
Version:        7.2.0
Release:        1%{?dist}
Summary:        Python dictionaries with advanced dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Box will automatically make otherwise inaccessible keys safe to
access as an attribute. You can always pass conversion_box=False
to Box to disable that behavior. Also, all new dict and lists
added to a Box or BoxList object are converted automatically.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(ruamel-yaml)
BuildRequires:  python3dist(toml)

Requires:       python3dist(msgpack)
Requires:       python3dist(ruamel-yaml)
Requires:       python3dist(toml)

%description -n python3-%{pypi_name}
Box will automatically make otherwise inaccessible keys safe to
access as an attribute. You can always pass conversion_box=False
to Box to disable that behavior. Also, all new dict and lists
added to a Box or BoxList object are converted automatically.

%prep
%autosetup -n Box-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -v test -k "not test_msgpack"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/python_box-%{version}.dist-info/

%changelog
* Tue Sep 17 2024 Fabian Affolter <mail@fabian-affolter.ch> - 7.2.0-1
- Update to latest upstream release (closes rhbz#2292117, closes rhbz#2193084)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 7.1.1-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 21 2023 David Moreau Simard <moi@dmsimard.com> - 7.1.1-2
- Update to latest upstream release 7.1.1 (closes rhbz#2220139)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 7.0.1-2
- Rebuilt for Python 3.12

* Tue May 23 2023 Fabian Affolter <mail@fabian-affolter.ch> - 6.1.0-1
- Update to latest upstream release 7.0.1 (closes rhbz#2165252)

* Sun May 07 2023 Maxwell G <maxwell@gtmx.me> - 6.1.0-3
- Remove buildtime dependency on deprecated pytest-runner

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Fabian Affolter <mail@fabian-affolter.ch> - 6.1.0-1
- Update to latest upstream release 6.1.0 (closes rhbz#2138674)

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 6.0.2-1
- Update to latest upstream release 6.0.2 (closes rhbz#2043812)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.4.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-2
- BuildRequire all runtime deps, toml was only brought in transitively trough pytest

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.4.0-1
- Update to latest upstream release 5.4.0 (rhbz#1993666)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.3.0-2
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.3.0-1
- Update to new upstream release 5.3.0 (#1928418)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.2.0-1
- Update to new upstream release 5.2.0 (#1892840)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.1-1
- Enable tests
1867812)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 David Moreau Simard <dmsimard@redhat.com> - 3.4.5-1
- Update to latest upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 5 2019 David Moreau Simard <dmsimard@redhat.com> - 3.4.1-1
- First version of the package
