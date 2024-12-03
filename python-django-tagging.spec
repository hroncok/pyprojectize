%global pkgname django-tagging
Name:           python-django-tagging
Version:        0.5.0
Release:        1%{?dist}
Summary:        A generic tagging application for Django projects

License:        MIT
URL:            https://github.com/Fantomas42/django-tagging/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
A generic tagging application for Django projects, which allows association\
of a number of tags with any Model instance and makes retrieval of tags\
simple.\

%description %_description


%package -n python3-django-tagging
Summary:        A generic tagging application for Django projects
Requires:       python3-django
BuildRequires:  python3-devel

%description -n python3-django-tagging
A generic tagging application for Django projects, which allows association
of a number of tags with any Model instance and makes retrieval of tags
simple.


%prep
%autosetup -n %{pkgname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tagging


%check
%pyproject_check_import


%files -n python3-django-tagging -f %{pyproject_files}
%doc CHANGELOG.txt LICENSE.txt README.rst docs/*


%changelog
* Mon Sep 16 2024 Matthias Runge <mrunge@redhat.com> - 0.5.0-1
- rebase to 0.5.0 (rhbz#2312410)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.6-24
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.6-20
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.6-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.6-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-5
- Drop python2 subpackage (#1632341)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Matthias Runge <mrunge@redhat.com> - 0.4.6-1
- rebase to 0.4.6
- fix python2 requires, python2-django1.11

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.5-5
- Python 2 binary package renamed to python2-django-tagging
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-2
- Rebuild for Python 3.6

* Mon Sep 26 2016 Matthias Runge <mrunge@redhat.com> - 0.4.5-1
- upgrade to 0.4.5 (rhbz#1379180)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 31 2016 Matthias Runge <mrunge@redhat.com> - 0.3.6-5
- fix spec file for centos7 (py3)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jakub Dorňák <jdornak@redhat.com> - 0.3.6-1
- rebase to version 0.3.6

* Wed Dec 10 2014 Jakub Dorňák <jdornak@redhat.com> - 0.3.4-2
- renamed get_query_set to get_queryset

* Wed Dec 10 2014 Jakub Dorňák <jdornak@redhat.com> - 0.3.4-1
- rebase to version 0.3.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Dec 23 2013 Jakub Dorňák <jdornak@redhat.com> - 0.3.1-11
- use builtin next(i) instead of i.next() for compatibility with Py3

* Thu Dec  5 2013 Jakub Dorňák <jdornak@redhat.com> - 0.3.1-10
- fixed use of types which are not available in Py3

* Sun Dec  1 2013 Jakub Dorňák <jdornak@redhat.com> - 0.3.1-9
- added python3 subpackage

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 06 2012 Matthias Runge <mrunge@redhat.com> - 0.3.1-6
- correct wrong obsoletes
- requires python-django

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 03 2012 Matthias Runge <mrunge@matthias-runge.de> 0.3.1-4
- package rename to python-django-tagging

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Matthias Runge <mrunge@matthias-runge.de> - 0.3.1-2
- add dist-tag
* Sun Jun 26 2011 Matthias Runge <mrunge@matthias-runge.de> - 0.3.1-1
- update to version 0.3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4.20080217svnr154
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3-3.20080217svnr154
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2.20080217svnr154
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.3-1.20080217svnr154
- Add Requires: Django

* Wed Feb 18 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.3-0.20080217svnr154
- Initial RPM release
