Name:           TurboGears2
Version:        2.4.3
Release:        18%{?dist}
Summary:        Next generation front-to-back web development megaframework

License:        MIT
URL:            http://www.turbogears.org
Source0:        https://files.pythonhosted.org/packages/source/T/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-backlash
BuildRequires:  python3-chameleon
BuildRequires:  python3-crank >= 0.8.0
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-formencode
BuildRequires:  python3-genshi >= 0.5.1
BuildRequires:  python3-jinja2
BuildRequires:  python3-kajiki >= 0.2.2
BuildRequires:  python3-mako
BuildRequires:  python3-repoze-tm2 >= 1.0-0.4.a4
BuildRequires:  python3-repoze-who
BuildRequires:  python3-repoze-who-plugins-sa >= 1.0.1
BuildRequires:  python3-tw2-forms
BuildRequires:  python3-webtest
BuildRequires:  python3-zope-sqlalchemy >= 0.4

%global _description \
TurboGears brings together a best of breed python tools to create a flexible,\
full featured, and easy to use web framework.\
\
TurboGears 2 provides and integrated and well tested set of tools for\
everything you need to build dynamic, database driven applications.  It\
provides a full range of tools for front end javascript develeopment, back\
database development and everything in between:\
\
 * dynamic javascript powered widgets ToscaWidgets\
 * automatic JSON generation from your controllers\
 * powerful, designer friendly XHTML basted templating (Genshi)\
 * object or route based URL dispatching\
 * powerful Object Relational Mappers (SQLAlchemy)\

%description %{_description}

%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}

Requires:       python3-backlash
Requires:       python3-chameleon
Requires:       python3-crank >= 0.8.0
Requires:       python3-decorator
Requires:       python3-formencode
Requires:       python3-genshi >= 0.5.1
Requires:       python3-jinja2
Requires:       python3-kajiki > 0.2.2
Requires:       python3-mako
Requires:       python3-markupsafe
Requires:       python3-paste-deploy
Requires:       python3-repoze-lru
Requires:       python3-repoze-tm2 >= 1.0-0.a4
Requires:       python3-repoze-who
Requires:       python3-repoze-who-plugins-sa >= 1.0.1
Requires:       python3-tw2-forms
Requires:       python3-webob >= 1.2
Requires:       python3-zope-sqlalchemy >= 0.4

%description -n python3-%{name} %{_description}

%prep
%autosetup -n %{name}-%{version}


%build
%py3_build

%install
%py3_install
rm -fr %{buildroot}%{python3_sitelib}/tests

# Tests cannot be included because some test dependencies
# are not available in Fedora repositories
#%check
#PYTHONPATH=$(pwd) %{__python3} setup.py test

%files -n python3-%{name}
%doc README.rst
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/tg/

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4.3-17
- Rebuild for python 3.13

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 2.4.3-16
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.4.3-12
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 2.4.3-9
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.3-6
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-3
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4.3-2
- Removed dependencies not really needed for current version:
  beaker, routes, simplegeneric

* Sun Mar 01 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3 (#1763576)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4.2-1
- Update to upstream.

* Thu Sep 12 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4.1-2
- Removed dependencies unused in current version (routes and simplegeneric).

* Tue Sep 03 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4.1-1
- Update to upstream.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.4.0-1
- Update to upstream.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.12-2
- Drop python2 subpackage (#1643378)

* Tue Jul 24 2018 Clement Verna <cverna@fedoraproject.org> - 2.3.12-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.11-5
- Rebuilt for Python 3.7

* Fri May 04 2018 Lumír Balhar <lbalhar@redhat.com> - 2.3.11-4
- Renamed dependencies
- Removed test BuildRequires
- Python 3 subpackage

* Mon Feb 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.11-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Clement Verna <cverna@tutanota.com> - 2.3.11-1
- Latest upstream
- Drop ming patch

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Ralph Bean <rbean@redhat.com> - 2.3.6-1
- Latest upstream.
- Drop chameleon patch.
- Disable test suite for now.  The latest from upstream isn't passing out of
  the box.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-0.6.git6da6959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-0.5.git6da6959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.0-0.4.git
- Replace dep on python-setuptools-devel with dep on python-setuptools

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-0.3.git6da6959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  8 2013 Luke Macken <lmacken@redhat.com> - 2.3.0-0.1.git6da6959
- Update to the latest 2.3 snapshot.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Ralph Bean <rbean@redhat.com> - 2.1.4-3
- Patch webob version requirement to allow python-webob-1.1.1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Luke Macken <lmacken@redhat.com> - 2.1.4-1
- Update to 2.1.4
- Get the test suite up and running again
- Add a tarball with some missing templates needed to run the tests
- Patch out the chameleon.genshi tests

* Thu Aug 25 2011 Luke Macken <lmacken@redhat.com> - 2.1.2-1
- Update to 2.1.2
- Update our requirements

* Wed Aug 17 2011 Nils Philippsen <nils@redhat.com>
- Update to 2.1.1 (#663117)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Luke Macken <lmacken@redhat.com> - 2.1-1
- Update to 2.1 final
- Patch out the kajiki requirement & tests until it's packaged

* Mon Oct 18 2010 Luke Macken <lmacken@redhat.com> - 2.1-0.4.rc1
- Add a patch to fix a helpers import issue
- This brings our package up to speed with the latest RC1 release

* Tue Sep 28 2010 Luke Macken <lmacken@redhat.com> - 2.1-0.3.rc1.dev1048
- Pre-RC1 development snapshot
- Remove strict Pylons<0.9.7 requirement
- Get the test suite running
- Pull in python-chameleon for the test suite
- Require python-simplegeneric
- Update the description

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.1-0.2.b2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 05 2010 Luke Macken <lmacken@redhat.com> - 2.1-0.1.b2
- Update to 2.1b2

* Mon Jan 11 2010 Luke Macken <lmacken@redhat.com> - 2.0.3-4
- Fix the source URL

* Mon Sep 14 2009 Luke Macken <lmacken@redhat.com> - 2.0.3-3
- Tweak our python-wsgiref conditional for EL5

* Tue Sep 01 2009 Luke Macken <lmacken@redhat.com> - 2.0.3-2
- Remove the SQLAlchemy requirement, as python-zope-sqlalchemy
  is now set to include the appropriate version

* Wed Aug 12 2009 Luke Macken <lmacken@redhat.com> - 2.0.3-1
- 2.0.3

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> 2.0.1-1
- 2.0.1
- Bump our ToscaWigdets requirement to 0.9.4
- Remove TurboGears2-custom-content-type.patch, which is upstream

* Sat Jun 06 2009 Luke Macken <lmacken@redhat.com> 2.0-4
- Require the new python-sqlalchemy0.5 package

* Thu Jun 04 2009 Luke Macken <lmacken@redhat.com> 2.0-3
- Add a patch to fix custom content types.
  http://trac.turbogears.org/ticket/2280

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> 2.0-2
- Conditionally include wsgiref

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> 2.0-1
- Update to 2.0 final.
- Add python-repoze-what-pylons and python-webflash to the BuildRequires
- Disable the test suite until we package chameleon.genshi

* Tue Oct 28 2008 Luke Macken <lmacken@redhat.com> 1.9.7.0.3.b1dev.r5627
- Update to a svn snapshot to support tgext.authorization instead of
  tg.ext.repoze.who

* Mon Oct 27 2008 Luke Macken <lmacken@redhat.com> 1.9.7-0.2.b1
- Update to 1.9.7b1

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> 1.9.7-0.1.a5dev.r5564
- Initial packaging of TurboGears2 for Fedora.
