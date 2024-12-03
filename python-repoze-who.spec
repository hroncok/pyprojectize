%global modname repoze.who

Name:           python-repoze-who
Version:        3.0.0
Release:        3%{?dist}
Summary:        An identification and authentication framework for WSGI

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/r/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pytest
BuildRequires:      python3-coverage
BuildRequires:      python3-zope-interface
BuildRequires:      python3-webob
BuildRequires:      python3dist(legacy-cgi)


%global _description\
repoze.who is an identification and authentication framework for arbitrary WSGI\
applications.  It acts as WSGI middleware.\
\
repoze.who is inspired by Zope 2's Pluggable Authentication Service (PAS) (but\
repoze.who is not dependent on Zope in any way; it is useful for any WSGI\
application).  It provides no facility for authorization (ensuring whether a\
user can or cannot perform the operation implied by the request).  This is\
considered to be the domain of the WSGI application.\


%description %_description

%package -n python3-repoze-who
Summary:        An identification and authentication framework for WSGI

%description -n python3-repoze-who
repoze.who is an identification and authentication framework for arbitrary WSGI
applications.  It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service (PAS) (but
repoze.who is not dependent on Zope in any way; it is useful for any WSGI
application).  It provides no facility for authorization (ensuring whether a
user can or cannot perform the operation implied by the request).  This is
considered to be the domain of the WSGI application.

%prep
%setup -q -n %{modname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l repoze

%check
%pyproject_check_import

#PYTHONPATH=$(pwd) %%{__python3} setup.py test
%pytest -k "not test_crypt_check"


%files -n python3-repoze-who -f %{pyproject_files}
%doc README.rst CHANGES.rst CONTRIBUTORS.txt
%license COPYRIGHT.txt


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.0.0-1
- Update to upstream
- Disable crypt check. Crypt module has been removed from python3.13,
  repoze-who works well without it and therefore this test is useless
- Use pytest instead of setup.py test

* Fri Jun 14 2024 Python Maint <python-maint@redhat.com> - 2.4.1-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.4.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.1-2
- Rebuilt for Python 3.11

* Tue Feb 01 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4.1-1
- Update to upstream.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4-6
- Switch from deprecated nose to pytest

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4-1
- Update to upstream

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3-3
- Rebuilt for Python 3.9

* Sun May 10 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3-2
- Fix compatibility with zope-interface >= 5 (bz#1825462)

* Thu Apr 16 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3-1
- Update to upstream
- Update URLs to https
- Marked COPYRIGHT and LICENSE files as licenses

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1-18
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-17
- Subpackage python2-repoze-who has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1-15
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1-12
- Python 2 binary package renamed to python2-repoze-who
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Luke Macken <lmacken@redhat.com> - 2.1-1
- Update to 2.1
- Add a python3 subpackage
- Remove setuptools patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.18-4
- Add missing BR: python-coverage

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue May 04 2010 Luke Macken <lmacken@redhat.com> - 1.0.18-2
- Run the test suite in %%check

* Mon Apr 26 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.0.18-1
- Update to the latest upstream release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 06 2009 Luke Macken <lmacken@redhat.com> - 1.0.13-1
- Update to the latest upstream release.

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0.7-1
- Initial package
