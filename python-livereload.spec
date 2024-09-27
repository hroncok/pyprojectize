%global pypi_name livereload

Name:           python-%{pypi_name}
Version:        2.6.3
Release:        15%{?dist}
Summary:        Utility for starting a server in a directory

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/lepture/python-livereload
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
LiveReload provides a command line utility, livereload, for starting a server
in a directory. By default, it will listen to port 35729, the common port for
LiveReload browser extensions. LiveReload is designed for web developers who
know Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-tornado
BuildRequires:  python3-certifi
BuildRequires:  python3-django
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
LiveReload provides a command line utility, livereload, for starting a server
in a directory. By default, it will listen to port 35729, the common port for
LiveReload browser extensions. LiveReload is designed for web developers who
know Python.

%package -n %{pypi_name}
Summary:        Command-Line tool for %{name}

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n %{pypi_name}
Command-line tool to live reload content.

%package docs
Summary:        Documentation for %{name}

%description docs
LiveReload documentation and examples.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

#%%check
#%%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst CHANGES.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%files docs
%doc docs example
%license LICENSE

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.3-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.6.3-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.6.3-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.6.3-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 23 2020 Fabian Affolter <mail@fabian-affolter.ch> -2.6.3-1
- Update to latest upstream release 2.6.3 (rhbz#1871363)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Fabian Affolter <mail@fabian-affolter.ch> -2.6.2-1
- Enable tests
- Update to latest upstream release 2.6.2 (rhbz#1844763)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-6
- Disable tests

* Tue Sep 10 2019 Neal Gompa <ngompa13@gmail.com> - 2.6.1-5
- Ensure that livereload package depends on matching version of Python module

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-2
- Rename subpackage (rhbz#1731638)

* Tue Jun 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-1
- Update to latest upstream release 2.6.1
- Add command-line sub-package
- Remove obsolete comments
- Enable tests
- Use upstream source

* Fri Jun 21 2019 Orion Poplawski <orion@nwra.com> - 2.5.2-5
- Drop BR on backports_abc - not needed

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.2-3
- Subpackage python2-livereload has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 2.5.2-1
- Update to v2.5.2
- BZ#1574127
- Skip failing tests
  https://github.com/lepture/python-livereload/issues/171

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-7
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Feb 17 2018 williamjmorenor@gmail.com - 2.5.1-5
- Run test only with python3 because missing python2-django
  See: https://fedoraproject.org/wiki/Changes/Django20
- Update description

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 William Moreno <williamjmorenor@gmail.com> - 2.5.1-1
- Update to v2.5.1
- Fix review issues

* Sat Dec 17 2016 William Moreno <williamjmorenor@gmail.com> - 2.5.0-1
- Update to v2.5.0
- Fix depencies names
- Update license from MIT to BSD


* Fri Feb 19 2016 William Moreno <williamjmorenor@gmail.com> - 2.4.1-2
- Provides python2-subpackage

* Fri Feb 12 2016 William Moreno <williamjmorenor@gmail.com> - 2.4.1-1
- v2.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 2.4.0-11
- https://fedoraproject.org/wiki/FAD_Python_3_Porting_2015

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 11 2015 Fedora <williamjmorenor at gmail.com> - 2.4.0-9
- Update Python Macros

* Thu Jul 09 2015 Fedora William Moreno Reyes <williamjmorenor at @gmail.com> - 2.4.0-8
- Do not build docs

* Thu Jul 09 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 2.4.0-7
- Not use compresed manpage

* Wed Jul 08 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 2.4.0-6
- Initial Import of #1230968
