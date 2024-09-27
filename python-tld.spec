%global pypi_name tld
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.13
Release:        7%{?dist}
Summary:        Extract the top level domain from the URL given

License:        MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later
URL:            https://github.com/barseghyanartur/tld
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Extract the top level domain (TLD) from the URL given. List of TLD names is
taken from Mozilla.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-setuptools

%if %{with network}
BuildRequires: python3-coverage
BuildRequires: python3-factory-boy
BuildRequires: python3-faker
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-runner
BuildRequires: python3-tox
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Extract the top level domain (TLD) from the URL given. List of TLD names is
taken from Mozilla.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx

%description -n %{name}-doc
Documentation for %{name}.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%if %{with network}
%check
# Don't test the CLI part
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v --pyargs tld.tests \
 -k "not test_1_update_tld_names_command and not test_1_update_tld_names_mozilla_command and not test_18_update_tld_names_cli" 
%endif

%files -n python3-%{pypi_name}
%doc CHANGELOG.rst CREDITS.rst README.rst
%license LICENSE_GPL2.0.txt LICENSE_LGPL_2.1.txt LICENSE_MPL_1.1.txt
%{_bindir}/update-tld-names
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/
%exclude %{python3_sitelib}/%{pypi_name}/tests/

%files -n %{name}-doc
%doc html
%license LICENSE_GPL2.0.txt LICENSE_LGPL_2.1.txt LICENSE_MPL_1.1.txt

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.13-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.13-2
- Rebuilt for Python 3.12

* Mon Mar 27 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.13-1
- Update to v0.13
- Fix license tag (says "LGPLv2 only", should be "LGPLv2 or later")
- Convert license tag to SPDX

* Sun Feb 19 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.7-1
- Update to latest upstream release 0.12.7 (closes rhbz#2166763)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.12.6-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.6-1
- Update to latest upstream release 0.12.6 (rhbz#1968202)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.5-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.45-1
- Update to latest upstream release 0.12.5 (#1912040)

* Sun Jan 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.4-1
- Update to latest upstream release 0.12.4 (#1912040)

* Fri Nov 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.3-1
- Update to latest upstream release 0.12.3 (#1902105)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Artur Iwicki <fedora@svgames.pl> - 0.12.2-1
- Update to latest upstream release 0.12.2

* Wed Apr 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.1-1
- Update to latest upstream release 0.12.1

* Fri Apr 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12-2
- Add docs sub package
- Enable tests
- Add missing license file

* Fri Apr 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12-1
- Update to latest upstream release 0.12

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.11-1
- Update to latest upstream release 0.11.11

* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.10-1
- Update to latest upstream release 0.11.10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Update to latest upstream release 0.9.3
- Add documentation

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.9-9
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.7.9-7
- Update license tag
- https://github.com/barseghyanartur/tld/issues/46 
- https://bugzilla.redhat.com/show_bug.cgi?id=1577466

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.9-6
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Jan Beran <jberan@redhat.com> - 0.7.9-5
- Fix of python3-tld requires both Python 2 and Python 3 (rhbz #1546814)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 williamjmorenor@gmail.com - 0.7.9-3
- Fix python2 subpackage requeriments

* Sat Jan 06 2018 williamjmorenor@gmail.com - 0.7.9-2
- Initial import BZ#1529024

* Mon Dec 25 2017 williamjmorenor@gmail.com - 0.7.9-1
- Initial packaging

