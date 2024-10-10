%global modname chai

Name:               python-%{modname}
Version:            1.1.2
Release:            32%{?dist}
Summary:            Easy to use mocking/stub/spy framework

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/chai
Source0:            http://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

%description
Chai provides a very easy to use api for mocking/stubbing your python
objects, patterned after the `Mocha <http://mocha.rubyforge.org/>`_ library
for Ruby.

%package -n         python%{python3_pkgversion}-%{modname}
Summary:            Easy to use mocking/stub framework

BuildRequires:      python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{modname}
Chai provides a very easy to use api for mocking/stubbing your python
objects, patterned after the `Mocha <http://mocha.rubyforge.org/>`_ library
for Ruby.

%prep
%setup -q -n %{modname}-%{version}

# Remove py2-only files.  They make our tests fail on py3.
rm chai/python2.py

# Remove py2-only file for the py3 tests.
rm tests/comparator_py2.py

# Replace unittest aliases removed in Python 3.12
sed -i \
    -e 's|assertEquals(|assertEqual(|' \
    -e 's|assertNotEquals(|assertNotEqual(|' \
    -e 's|assert_true(|assertTrue(|' \
    -e 's|assert_equals(|assertEqual(|' \
$(find tests -type f)

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l %{modname}

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.2-32
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.2-30
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.2-26
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.2-23
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1.1.2-20
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-15
- Subpackage python2-chai has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-10
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Kevin Fenzi <kevin@scrye.com> - 1.1.2-6
- Update to 1.1.2. Fixes bug #1463021

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuild for Python 3.6

* Wed Jul 27 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-4
- Explicit python2 subpackage.

* Wed Jul 27 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-3
- Get python34 working for EPEL7.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- new version

* Wed Oct 15 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0.0
- Update to 1.0.0

* Wed Jul 09 2014 Ralph Bean <rbean@redhat.com> - 0.4.8-2
- Modernize with_python3 macro definition.

* Wed Jul 02 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.8-1
- Update to 0.4.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Jan 08 2014 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.7-1
- Update to 0.4.7

* Wed Dec 04 2013 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.6-1
- Update to 0.4.6

* Sun Nov 03 2013 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.5-1
- Update to 0.4.5
- Upstream ships LICENSE file
- Re-activate the tests

* Tue Oct 29 2013 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.4-1
- initial package for Fedora
