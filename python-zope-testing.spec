%global modname zope.testing


Name:           python-zope-testing
Version:        5.0.1
Release:        9%{?dist}
Summary:        Zope Testing Framework
License:        ZPL-2.1
URL:            https://pypi.io/project/%{modname}
Source0:        https://pypi.io/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
# Upstream report: https://github.com/zopefoundation/zope.testing/issues/41
Patch:          0001-Fix-doctest-failure-with-Python-3.11.patch

BuildArch:      noarch

%description
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.


%package -n python%{python3_pkgversion}-zope-testing
Summary:        Zope Testing Framework

BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-zope-testing
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%prep
%autosetup -p1 -n %{modname}-%{version}

rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
# __init__.py* are not needed since .pth file is used
rm -f %{buildroot}%{python3_sitelib}/zope/__init__.py*

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-zope-testing
%doc CHANGES.rst README.rst src/zope/testing/*.txt
%license COPYRIGHT.txt LICENSE.txt
%{python3_sitelib}/zope/testing/
%exclude %{python3_sitelib}/zope/testing/*.txt
%{python3_sitelib}/%{modname}-*.dist-info
%{python3_sitelib}/%{modname}-*-nspkg.pth

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.0.1-8
- Rebuilt for Python 3.13

* Sun Apr 14 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.1-7
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.0.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Dan Radez <dradez@redhat.com> - 5.0.1-1
- update to 5.0.1 (rhbz#2155219)

* Mon Aug 29 2022 Dan Radez <dradez@redhat.com> - 4.10-1
- updating to 4.10 (rhbz#1912537)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.7-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 4.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7-2
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Lumír Balhar <lbalhar@redhat.com> - 4.7-1
- Update to 4.7 (#1460853)
- Removed unnecessary dependencies, fixed license files

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-11
- Subpackage python2-zope-testing has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Carl George <carl@george.computer> - 4.6.1-8
- EPEL compatibility

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Ralph Bean <rbean@redhat.com> - 4.6.1-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Ralph Bean <rbean@redhat.com> - 4.5.0-5
- Add an explicit python2 subpackage.
- Modernize python macros.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 4.5.0-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 4.1.3-1
- Latest upstream.
- Modernized python macros.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 4.1.2-1
- Latest upstream.
- Enabled python3 tests in the check section.
- Updated the with_python3 conditional.
- README and CHANGES renamed from .txt to .rst.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Ralph Bean <rbean@redhat.com> - 4.1.1-1
- Latest upstream release.
- Packaged a python3 subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Robin Lee <cheeselee@fedoraproject.org> - 3.10.3-1
- Update to 3.10.3 (ZTK 1.1.3)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.10.2-1
- Update to 3.10.2
- Move the documents to proper place
- Run the tests

* Tue Aug 31 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.10.0-2
- Requirement: python-zope-filesystem removed, python-zope-exceptions added
- Spec cleaned up

* Mon Aug 30 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.10.0-1
- Update to 3.10.0
- Rearrange documents

* Sat Jul 31 2010 David Malcolm <dmalcolm@redhat.com> - 3.9.5-5
- actually remove the requirement on python-zope-exceptions this time

* Fri Jul 30 2010 David Malcolm <dmalcolm@redhat.com> - 3.9.5-4
- add missing build-time requirement on python-setuptools

* Fri Jul 30 2010 David Malcolm <dmalcolm@redhat.com> - 3.9.5-3
- remove requirement on python-zope-exceptions for now (bug 619478)
- add missing zope-testrunner executable to %%files

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 17 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.9.5-1
- Update to 3.9.5
- Rearrange documents
- Requires: python-zope-interface and python-zope-exceptions added

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Conrad Meyer <konrad@tylerc.org> - 3.7.3-3
- Actually fix file conflict with python-zope-filesystem.

* Sat Jun 13 2009 Conrad Meyer <konrad@tylerc.org> - 3.7.3-2
- Fix file conflict with python-zope-filesystem.

* Wed Apr 22 2009 Conrad Meyer <konrad@tylerc.org> - 3.7.3-1
- Bump to 3.7.3.

* Sun Dec 14 2008 Conrad Meyer <konrad@tylerc.org> - 3.7.1-1
- Initial package.
