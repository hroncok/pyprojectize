Name:           python-straight-plugin
Version:        1.5.0
Release:        29%{?dist}
Summary:        Python plugin loader

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ironfroggy/straight.plugin/

Source0:        https://files.pythonhosted.org/packages/48/89/34ae6a87784d0b607af61c84a52c313c598f1d86ce5c1e9eb6da038fee5f/straight.plugin-%{version}.tar.gz

# Remove an unused import of imp.find_module
# The imp module was removed in Python 3.12
# Fixes https://bugzilla.redhat.com/2238632
# Rebased from https://github.com/ironfroggy/straight.plugin/pull/30
Patch:          Remove-the-import-of-imp.find_module.patch

BuildArch:      noarch

BuildRequires:  python3-devel



%global _description\
straight.plugin is a Python plugin loader inspired by twisted.plugin with two\
important distinctions:\
\
 - Fewer dependencies\
 - Python 3 compatible\
\
The system is used to allow multiple Python packages to provide plugins within\
a namespace package, where other packages will locate and utilize. The plugins\
themselves are modules in a namespace package where the namespace identifies\
the plugins in it for some particular purpose or intent.\


%description %_description

%package -n     python3-straight-plugin
Summary:        Python plugin loader

%description -n python3-straight-plugin
straight.plugin is a Python plugin loader inspired by twisted.plugin with two
important distinctions:

 - Fewer dependencies
 - Python 3 compatible

The system is used to allow multiple Python packages to provide plugins within
a namespace package, where other packages will locate and utilize. The plugins
themselves are modules in a namespace package where the namespace identifies
the plugins in it for some particular purpose or intent.

%prep
%autosetup -p1 -n straight.plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

#%check
#%{__python3} tests.py

%files -n python3-straight-plugin
# For noarch packages: sitelib
%{python3_sitelib}/straight*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.0-29
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Paul Wouters <paul.wouters@aiven.io> - 1.5.0-27
- Resolves: rhbz#2244822 depends on 2to3 which will be removed from Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.0-26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-23
- Fix a ModuleNotFoundError when this package was imported on Python 3.12+
- Fixes: rhbz#2238632

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.0-21
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.0-18
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.0-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-7
- Subpackage python2-straight-plugin has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Kevin Fenzi <kevin@scrye.com> - 1.5.0-5
- Rebuild with previous fixes.

* Wed Jul 18 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.5.0-4
- Fix the python interpreter used to build the py2 package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.7

* Thu Apr 26 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.5.0-1
- Update to 1.5.0

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.0-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-11
- Python 2 binary package renamed to python2-straight-plugin
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-8
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Pierre-Yves Chibon - 1.4.0-1
- Update to 1.4.0
- Remove doc as they are not part of the sources anymore (reported upstream)
- Comment out the tests as they are apparently also not in the sources anymore
- Add python{,3}-setuptools as BR

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.1-0.10.20111110.git57ef11c
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-0.9.20111110.git57ef11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-0.8.20111110.git57ef11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.1.1-0.7.20111110git57ef11c
- Fix the import of python-importlib (Finally!!)

* Fri Nov 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.1.1-0.6.20111110git57ef11c
- Fix typo in the use if for python-importlib

* Fri Nov 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.1.1-0.5.20111110git57ef11c
- Add python-importlib as BR and R on EL6

* Fri Nov 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.1.1-0.4.20111110git57ef11c
- EL6 has no python3 /me should get glasses...
- Fix comment on how to generate the tarball properly (previous method didn't keep the timestamp)

* Thu Nov 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.1.1-0.3.20111110git57ef11c
- Fix the use of __python3 for the tests and the build
- Change python-devel to python2-devel on the BR

* Thu Nov 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.1.1-0.2.20111110git57ef11c
- Rename the package to remove the dot

* Thu Nov 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.1.1-0.1.20111110git57ef11c
- Initial packaging work for Fedora
