%global pkgname django-reversion
Name:           python-django-reversion
Version:        4.0.0
Release:        12%{?dist}
Summary:        Version control extension for the Django web framework

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/etianen/django-reversion
Source0:        https://github.com/etianen/django-reversion/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
Provides:       %{pkgname} = %{version}-%{release}
Obsoletes:      %{pkgname} < 1.6.2-1

%description
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

Features:
* Roll back to any point in a model's history - an unlimited undo facility!
* Recover deleted models - never lose data again!
* Admin integration for maximum usability.
* Group related changes into revisions that can be rolled back in a single
  transaction.
* Automatically save a new version whenever your model changes using Django's
  flexible signalling framework.
* Automate your revision management with easy-to-use middleware.

Reversion can be easily added to your existing Django project with a minimum
of code changes.

%package -n python3-%{pkgname}
Summary:        Version control extension for the Django web framework
BuildRequires:  python3-devel
Requires:       python3-django

Obsoletes:   python-%{pkgname} < 2.0.13-1
Obsoletes:   python2-%{pkgname} < 2.0.13-1

%description -n python3-%{pkgname}
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

Features:
* Roll back to any point in a model's history - an unlimited undo facility!
* Recover deleted models - never lose data again!
* Admin integration for maximum usability.
* Group related changes into revisions that can be rolled back in a single
  transaction.
* Automatically save a new version whenever your model changes using Django's
  flexible signalling framework.
* Automate your revision management with easy-to-use middleware.

Reversion can be easily added to your existing Django project with a minimum
of code changes.


%prep
%autosetup -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install

# Language files; not under /usr/share, need to be handled manually
(cd $RPM_BUILD_ROOT && find . -name 'django*.mo') | %{__sed} -e 's|^.||' | %{__sed} -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:' \
  >> %{name}.lang


find $RPM_BUILD_ROOT -name "*.po" | xargs rm -f


%files -n python3-%{pkgname} -f %{name}.lang
%doc README.rst
%license LICENSE
%dir %{python3_sitelib}/reversion
%{python3_sitelib}/reversion/*.py*
%{python3_sitelib}/reversion/__pycache__
%{python3_sitelib}/reversion/management/
%{python3_sitelib}/reversion/templates/
%{python3_sitelib}/reversion/migrations/
%{python3_sitelib}/django_reversion-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.0-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0.0-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.0.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Matthias Runge <mrunge@redhat.com> - 4.0.0-1
- update to 4.0.0 (rhbz#1603189)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.13-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.13-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.13-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.13-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.13-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Matthias Runge <mrunge@redhat.com> - 2.0.13-1
- update to 2.0.13
- drop Python2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuild for Python 3.6

* Sun Jul 31 2016 Petr Viktorin <pviktori@redhat.com> - 2.0.0-3
- Fix Python sitelib directories

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 13 2016 Matthias Runge <mrunge@redhat.com> - 2.0.0-1
- update to 2.0 (rhbz#1103194)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 02 2014 Matthias Runge <mrunge@redhat.com> - 1.8.0-1
- update to 1.8.0 (rhbz#1027767)

* Tue Aug 13 2013 Matthias Runge <mrunge@redhat.com> - 1.7.1-1
- update to 1.7.1 (rhbz#979597)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Matthias Runge <mrunge@redhat.com> - 1.7-1
- update to upstream version 1.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Matthias Runge <mrunge@redhat.com> - 1-6.5-1
- update to upstream version 1.6.5 (rhbz#886552)

* Wed Oct 31 2012 Matthias Runge <mrunge@redhat.com> - 1.6.4-1
- update to upstream version 1.6.4

* Mon Aug 06 2012 Matthias Runge <mrunge@matthias-runge.de> - 1.6.2-1
- updated to upstream release 1.6.2
- package renamed to python-django-reversion

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012 Luca Botti <lucabotti@fedoraproject.orf> 1.6.0-1
- Updated to 1.6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 14 2010 Luca Botti <lucabotti@fedoraproject.org> 1.3.2-2
- Fixed locale handling

* Fri Nov 12 2010 Luca Botti <lucabotti@fedoraproject.org> 1.3.2-1
- Update to 1.3.2

* Tue Sep 29 2009 Luca Botti <lucabotti@fedoraproject.org> 1.1.2-2
- Fixed Spec File

* Fri Aug 21 2009 Luca Botti <lucabotti@fedoraproject.org> 1.1.2-1
- Update to 1.1.2 upstream release

* Fri Jul 17 2009 Tim Niemueller <timn@fedoraproject.org> 1.1.1
- Initial RPM release
