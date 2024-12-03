# tests disabled in RHEL
%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

%global srcname factory_boy
%global desc factory_boy is a fixtures replacement based on thoughtbot's factory_girl\
<http://github.com/thoughtbot/factory_girl>.\
\
Its features include:\
\
- Straightforward syntax\
- Support for multiple build strategies (saved/unsaved instances, attribute\
  dicts, stubbed objects)\
- Powerful helpers for common cases (sequences, sub-factories, reverse\
  dependencies, circular factories, ...)\
- Multiple factories per class support, including inheritance\
- Support for various ORMs (currently Django, Mogo, SQLAlchemy)\

Name: python-factory-boy
Version: 3.3.1
Release: 1%{?dist}
Summary: A versatile test fixtures replacement based on thoughtbot's factory_girl
License: MIT
URL: https://github.com/rbarrois/factory_boy
Source0: https://github.com/rbarrois/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
%if %{with tests}
BuildRequires: python3-pytest
BuildRequires: python3-faker >= 0.7.0
BuildRequires: python3-sqlalchemy
BuildRequires: python3-sqlalchemy-utils
BuildRequires: python3-coverage
BuildRequires: python3-flake8
BuildRequires: python3-isort
BuildRequires: python3-pillow
BuildRequires: tox
BuildRequires: python3-django
BuildRequires: python3-flask
BuildRequires: python3-flask-sqlalchemy
%endif

%description
%desc

%package -n python3-factory-boy
Summary: A versatile test fixtures replacement based on thoughtbot's factory_girl
Suggests: %{name}-doc = %{version}-%{release}

%description -n python3-factory-boy
%desc

%package doc
Summary: API documentation for %{name}

%description doc
Documentation for the %{name} API

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Clean the doc dir
rm -f docs/Makefile
rm -rf docs/_static
find examples -type f -print0 | xargs -0 chmod 0644

%install
%pyproject_install
%pyproject_save_files -l factory

%if %{with tests}
%check
%pyproject_check_import

SKIP_MONGOENGINE=1 %pytest
%endif

%files -n python3-factory-boy -f %{pyproject_files}

%files doc
%doc README.rst CODE_OF_CONDUCT.md CONTRIBUTING.rst CREDITS docs examples
%license LICENSE

%changelog
* Wed Sep 04 2024 Juan Orti Alcaine <jortialc@redhat.com> - 3.3.1-1
- Version 3.3.1 (RHBZ#2306033)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 3.3.0-5
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.0-4
- Bootstrap for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 22 2023 Juan Orti Alcaine <jortialc@redhat.com> - 3.3.0-1
- Version 3.3.0 (#2223915)
- Fix tests

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 3.2.1-8
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.2.1-7
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.2.1-4
- Rebuilt for Python 3.11

* Sat Mar 26 2022 Juan Orti Alcaine <jortialc@redhat.com> - 3.2.1-3
- Disable tests in RHEL

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Juan Orti Alcaine <jortialc@redhat.com> - 3.2.1-1
- Version 3.2.1 (#2017474)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Juan Orti Alcaine <jortialc@redhat.com> - 3.2.0-1
- Version 3.2.0 (#1911225)

* Thu Oct 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 3.1.0-1
- Version 3.1.0 (RHBZ#1884820)
- BR: python3-setuptools

* Fri Aug 14 2020 Juan Orti Alcaine <jortialc@redhat.com> - 3.0.1-1
- Version 3.0.1 (RHBZ#1868502)

* Thu Aug 13 2020 Juan Orti Alcaine <jortialc@redhat.com> - 3.0.0-1
- Version 3.0.0
- Include documentation in text format as sphinx fails to build

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.12.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.12.0-1
- Version 2.12.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.1-5
- Drop python2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-2
- Rebuilt for Python 3.7

* Wed May 16 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.11.1-1
- Version 2.11.1

* Tue Mar 13 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.10.0-1
- Version 2.10.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.9.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Aug 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.9.2-1
- Version 2.9.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.8.1-2
- Python3 changes

* Sun Feb 26 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.8.1-1
- Version 2.8.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 06 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.7.0-2
- Add BuildRequires: python-sphinx_rtd_theme

* Thu Jun 23 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.7.0-1
- Version 2.7.0

* Wed Feb 24 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.6.1-1
- Version 2.6.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.6.0-3
- Add python-faker dependency
- Use python_provide macro

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 21 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.6.0-1
- New version 2.6.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.5.2-1
- New version 2.5.2

* Tue Dec 23 2014 Juan Orti <jorti@fedoraproject.org> - 2.4.1-4
- Use parallel make

* Mon Dec 15 2014 Juan Orti <jorti@fedoraproject.org> - 2.4.1-3
- Update to commit 392db861e585f12038f18f41e467ecfcab9d39b0
- Drop patch factory_boy-2.4.1-disable_broken_tests.patch

* Wed Dec 10 2014 Juan Orti <jorti@fedoraproject.org> - 2.4.1-2
- Rename python3 subpackage to python3-factory-boy
- Move manpage to doc subpackage and to section 3
- Fit summary and description in 80 characters width lines
- Remove .buildinfo files
- Run tests
- Add patch to disable broken tests
- Change Source0 to GitHub
- Add documentation in plain text format

* Wed Dec 03 2014 Juan Orti <jorti@fedoraproject.org> - 2.4.1-1
- Update to version 2.4.1
- Spec file cleanup

* Sat May 24 2014 Didier Fabert <didier.fabert@gmail.com> 2.3.1-1
- Initial RPM release
