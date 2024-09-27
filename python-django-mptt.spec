%global srcname django-mptt

Summary:    Utilities for implementing Modified Preorder Tree Traversal
Name:       python-%{srcname}
Version:    0.12.0
Release:    13%{?dist}
License:    MIT
URL:        https://github.com/django-mptt/django-mptt
Source:     %{pypi_source}
BuildArch:  noarch

%global _description\
Utilities for implementing Modified Preorder Tree Traversal (MPTT)\
with your Django Model classes and working with trees of Model instances.\

%description %_description

%package -n python3-%{srcname}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Obsoletes: python2-django-mptt < 0.9.0-2
Obsoletes: python-django-mptt < 0.9.0-2

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info/

# remove unnecessary language ressources:
rm mptt/locale/*/LC_MESSAGES/django.po


%build
%py3_build


%install
%py3_install


%find_lang django

%check

# tests require django-js-asset
#cd tests
#sh runtests.sh


%files -n python3-django-mptt -f django.lang
%license LICENSE
%doc README.rst NOTES
%{python3_sitelib}/django_mptt-*.egg-info/
%{python3_sitelib}/mptt/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.12.0-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.12.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.12.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.10

* Fri Mar 26 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.7

* Tue Mar 20 2018 Matthias Runge <mrunge@redhat.com> - 0.9.0-4
- fix file ownership (static missing)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Matthias Runge <mrunge@redhat.com> - 0.9.0-2
- drop Python2 subpackage for https://fedoraproject.org/wiki/Changes/Django20
- Fix Python3 package building (rhbz#1539851)

* Fri Jan 26 2018 Matthias Runge <mrunge@redhat.com> - 0.9.0-1
- upgrade to 0.9.0
- fix python2/python2-django requirements

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.6-5
- Python 2 binary package renamed to python2-django-mptt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.6-2
- Rebuild for Python 3.6

* Wed Dec 21 2016 Jakub Dorňák <jakub.dornak@misli.cz> - 0.8.6-1
- update to 0.8.6

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul  7 2015 Jakub Dorňák <jdornak@redhat.com> - 0.7.4-1
- update to 0.7.4
- move license and docs to the right place

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Nov 25 2013 Jakub Dorňák <jdornak@redhat.com> - 0.6.0-2
- added python3 subpackage

* Mon Aug 19 2013 Matthias Runge <mrunge@redhat.com> - 0.6.0-1
- update to 0.6.0
- fix ftbfs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.5.4-1
- update to version 0.5.4 from upstream

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.5.2-3
- fix double included language files
- fix license

* Tue Mar 27 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.5.2-1
- renamed to python-django-mptt
- update to version 0.5.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 29 2010 Dave Riches <dcr226@fedorapeople.org> - 0.4.2-2
- removed redundant comments from spec


* Sun Nov 28 2010 Clint Savage <herlo@fedorapeople.org> - 0.4.2-1
- Updated the package to 0.4.2 and removed a couple unneeded lines from the spec

* Thu Oct 21 2010 Dave Riches <dcr226@fedorapeople.org> - 0.4.1-1
- Packaged for Fedora

