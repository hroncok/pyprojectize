%global pkgname webpy
%global srcname web.py

Name:           python-%{pkgname}
Version:        0.62
Release:        13%{dist}
Summary:        A simple web framework for Python

# The entire source code is Public Domain save for the following exceptions:
#   web/debugerror.py (Modified BSD)
#     This is from django
#     See http://code.djangoproject.com/browser/django/trunk/LICENSE
#   web/httpserver.py (Modified BSD)
#     This is from WSGIUtils/lib/wsgiutils/wsgiServer.py
#     See http://www.xfree86.org/3.3.6/COPYRIGHT2.html#5
# Automatically converted from old format: Public Domain and BSD - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD

URL:            http://webpy.org/
Source0:        https://github.com/%{pkgname}/%{pkgname}/archive/%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
web.py is a web framework for python that is as simple as it is\
powerful. web.py is in the public domain; you can use it for whatever\
purpose with absolutely no restrictions.

%description %_description

%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-cheroot

Requires:       python3-cheroot


%description -n python3-%{pkgname}
%_description


%prep
%autosetup -n %{pkgname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%check
pytest -k 'not test_routing' tests

%files -n python3-%{pkgname}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/web
%{python3_sitelib}/%{srcname}-%{version}.dist-info


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.62-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.62-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Python Maint <python-maint@redhat.com> - 0.62-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.62-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Matthias Runge <mrunge@redhat.com> - 0.62-1
- update to 0.62 (rhbz#1895901)
- skip ApplicationTest.test_routing for now

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.61-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Paweł Marciniak <sunwire+webpy@gmail.com> - 0.61-2
- Fix small mistake in the changelog

* Sat Jul 25 2020 Paweł Marciniak <sunwire+webpy@gmail.com> - 0.61-1
- update to 0.61-1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.50-3
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Matthias Runge <mrunge@redhat.com> - 0.50-1
- add tests and also fix dist

* Mon Mar 23 2020 Matthias Runge <mrunge@redhat.com> - 0.50-1
- update to 0.50-1, (rhbz#1756261)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.dev0-20170819gitb725a4f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.40.dev0-20170818gitb725a4f
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.40.dev0-20170817gitb725a4f
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.dev0-20170816gitb725a4f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.dev0-20170815gitb725a4f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.40.dev0-20170814gitb725a4f
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.dev0-20170813gitb725a4f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.40.dev0-20170812gitb725a4f
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.dev0-20170811gitb725a4f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.40.dev0-20170810gitb725a4f
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Oct 16 2017 Jan Beran <jberan@redhat.com> - 0.40.dev0-20170809gitb725a4f
- new version from the latest commit 0.40.dev0-20170809gitb725a4f
- modernized specfile with Python 3 subpackage

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.37-11
- Python 2 binary package renamed to python2-webpy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.37-1
- update to 0.37
- minor spec cleanup

* Wed Mar 14 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.36-2
- unbundle cherrypy-code

* Wed Jan 25 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.36-1
- rebase to 0.36

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.32-3
- Strip shebang from non-scripts
- Update license information
- Enable unit tests

* Thu Jul 02 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.32-2
- Added python-devel BuildRequires
- Updated with multiple licensing annotations

* Wed Jul 01 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.32-1
- Rebase to 0.32

* Mon Jun 01 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.31-1
- Initial package
