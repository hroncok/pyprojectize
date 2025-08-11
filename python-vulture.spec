%global pypi_name vulture
%global common_desc \
Vulture finds unused classes, functions and variables in your code. \
This helps you cleanup and find errors in your programs. If you run it \
on both your library and test suite you can find untested code. \
Due to Python’s dynamic nature, static code analyzers like vulture \
are likely to miss some dead code. Also, code that is only called \
implicitly may be reported as unused. Nonetheless, vulture can be a \
very helpful tool for higher code quality.

Name:           python-%{pypi_name}
Version:        2.12
Release:        1%{?dist}
Summary:        Find dead code

License:        MIT
URL:            https://github.com/jendrikseipp/vulture
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n	python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(pint)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
%description -n	python3-%{pypi_name}
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i '1{/^#!/d}' vulture/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
mv %{buildroot}%{_bindir}/%{pypi_name} %{buildroot}%{_bindir}/%{pypi_name}-%{python3_version}
ln -s %{_bindir}/vulture-%{python3_version} %{buildroot}/%{_bindir}/vulture-3
ln -s %{_bindir}/vulture-%{python3_version} %{buildroot}/%{_bindir}/vulture

%check
%pyproject_check_import
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-3
%{_bindir}/%{pypi_name}-%{python3_version}

%changelog
* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 2.12-1
- Update to latest upstream release (closes rhbz#2159155)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.6-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Python Maint <python-maint@redhat.com> - 2.6-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.6-1
- Update to latest upstream release 2.6 (closes rhbz#2127853)

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.5-1
- Update to latest upstream release 2.5 (closes rhbz#2088613)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Miro Hrončok <mhroncok@redhat.com> - 2.3-5
- BuildRequire all runtime deps, toml was only brought in transitively trough pytest

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-1
- Update to latest upstream release 2.3 (#1916895)

* Sat Jan 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-1
- Update to latest upstream release 2.2 (#1916895)

* Fri Nov 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1-1
- Update to latest upstream release 2.1 (#1754617)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Yatin Karel <ykarel@redhat.com> - 1.0-1
- Drop python2 sub package (Resolves #1740990)
- Update to 1.0 (Resolves #1586070)
- Disable tests temporary (Resolves #1716536)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.27-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Yatin Karel <ykarel@redhat.com> - 0.27-2
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Yatin Karel <ykarel@redhat.com> - 0.27-1
- Update to 0.27 (#1586070)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.26-1
- Update to 0.26 (#1485917)

* Wed Aug 16 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.25-1
- Update to 0.25 (#1472024)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Yatin Karel <ykarel@redhat.com> - 0.16-1
- Sync with upstream release 0.16

* Wed Jul 05 2017 Yatin Karel <ykarel@redhat.com> - 0.14-3
- Fix Changelog release

* Wed Jul 05 2017 Yatin Karel <ykarel@redhat.com> - 0.14-2
- Use versioned package, python2-setuptools(not python-setuptools)

* Tue Jun 20 2017 Yatin Karel <ykarel@redhat.com> - 0.14-1
- Initial package import

