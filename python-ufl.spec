%global srcname ufl

Name:           python-%{srcname}
Version:        2019.1.0
Release:        22%{?dist}
Summary:        Compiler for finite element variational forms

License:        LGPL-3.0-or-later
URL:            http://www.fenicsproject.org
Source0:        https://bitbucket.org/fenics-project/ufl/downloads/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
The Unified Form Language (UFL) is a domain specific language for declaration
of finite element discretizations of variational forms. More precisely, it
defines a flexible interface for choosing finite element spaces and defining
expressions for weak forms in a notation close to mathematical notation.

%package -n python3-%{srcname}
Summary:        %{summery}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The Unified Form Language (UFL) is a domain specific language for declaration
of finite element discretizations of variational forms. More precisely, it
defines a flexible interface for choosing finite element spaces and defining
expressions for weak forms in a notation close to mathematical notation.

%package        demo
Summary:        Demo files for %{name}
Requires:       python3-%{srcname} = %{version}-%{release}

%description    demo
The %{name}-demo package contains demo files for %{name}.

%package        test
Summary:        Test files for %{name}
Requires:       python3-%{srcname} = %{version}-%{release}
Requires:       python3-nose

%description    test
The %{name}-test package contains test files for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
# Fix permissions
chmod +x test/test_*.py
# Fix typo
sed -i -e 's|#!/use/bin/env|#!/usr/bin/env|g' test/test_measures.py

%build
%py3_build

%install
%py3_install
mkdir %{buildroot}%{python3_sitelib}/%{srcname}/demo/
install -Dp -m 0644 demo/* %{buildroot}%{python3_sitelib}/%{srcname}/demo/
mkdir %{buildroot}%{python3_sitelib}/%{srcname}/test/
cp -R test/* %{buildroot}%{python3_sitelib}/%{srcname}/test/
chmod +x %{buildroot}%{python3_sitelib}/%{srcname}/demo/clean.sh

%files -n python3-%{srcname}
%doc AUTHORS ChangeLog.rst README.rst
%license COPYING COPYING.LESSER
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/*ufl*.egg-info
%exclude %{python3_sitelib}/%{srcname}/demo/
%exclude %{python3_sitelib}/%{srcname}/test/

%files demo
%doc COPYING.LESSER
%{python3_sitelib}/%{srcname}/demo/

%files test
%doc COPYING.LESSER
%{python3_sitelib}/%{srcname}/test/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2019.1.0-21
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2019.1.0-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2019.1.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2019.1.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2019.1.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2019.1.0-7
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2019.1.0-1
- Update to latest upstream release 2019.1.0 (rhbz#1655269)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Kalev Lember <klember@redhat.com> - 1.6.0-2
- Fix broken dependencies for demo and test subpackages

* Sun Nov 15 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Cleanup
- Update to latest upstream release 1.6.0 (rhbz#1181552)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 01 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to latest upstream release 1.5.0 (rhbz#1181552)

* Thu Aug 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-2
- Remove duplicate files
- Fix typo

* Thu Jul 31 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update python macros
- Update source URL
- Update to latest upstream release 1.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-4
- License file added to subpackages
- Removed check section
- Other minor changes

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-3
- License issue fixed
- Test subpackage
- Demo subpackage

* Sun Mar 25 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-2
- Minor changes

* Sun Mar 04 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Updated to new upstream version 1.0.0

* Sat Mar 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1-0.1.pre
- Initial package
