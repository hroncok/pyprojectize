%global pkgname django-ajax-selects

Name:           python-django-ajax-selects
Version:        2.2.0
Release:        10%{?dist}
Summary:        Enables editing of ForeignKey, ManyToMany and simple text fields

# Automatically converted from old format: MIT or GPL+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT OR GPL-1.0-or-later
URL:            https://github.com/crucialfelix/django-ajax-selects
Source:         http://pypi.python.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
Enables editing of ForeignKey, ManyToMany and simple text fields using the\
Autocomplete - jQuery plugin.\
django-ajax-selects will work in any normal form as well as in the admin.\
The user is presented with a text field. They type a search term or a few\
letters of a name they are looking for, an ajax request is sent to the server,\
a search channel returns possible results. Results are displayed as a drop\
down menu. When an item is selected it is added to a display area just below\
the text field.

%description %_description

%package -n python3-django-ajax-selects
Summary:        Intelligent schema migrations for Django apps


Requires:       python3-django

Obsoletes:      python2-django-ajax-selects < 1.3.4-14
Obsoletes:      python-django-ajax-selects < 1.3.4-14

%description -n python3-django-ajax-selects %_description

%prep
%setup -q -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-django-ajax-selects
%license ajax_select/LICENSE.txt
%doc README.md CHANGELOG.md
%{python3_sitelib}/ajax_select
%{python3_sitelib}/django_ajax_selects-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Luis Bazan <lbazan@fedoraproject.org> - 2.2.0-1
- New upstream version

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.8.0-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.8.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.8.0-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.7.1-1
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.7

* Thu Apr 19 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.7.0-2
- fix Documents

* Thu Apr 19 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.7.0-1
- New Upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-14
- Removed Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20
- Removed Groups
- Added %%python_provide for python3 subpackage
- Use modern %%py3_ macros and %%license

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.4-13
- Python 2 binary package renamed to python2-django-ajax-selects
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.4-5
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Apr 10 2014 Luis Bazan <lbazan@fedoraporject.org> - 1.3.4-2
- add compatibility with python3

* Thu Apr 10 2014 Luis Bazan <lbazan@fedoraporject.org> - 1.3.4-1
- New Upstream version

* Tue Feb 04 2014 Luis Bazan <lbazan@fedoraproject.org> - 1.3.3-1
- New upstream version

* Mon Sep 16 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.5-3
- correct django-ajax-selects obs_ver once more, since there's an even
  newer build in F17

* Tue Sep 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.2.5-2
- correct django-ajax-selects obs_ver

* Tue Aug 13 2013 Luis Bazan <lbazan@fedoraproject.org> - 1.2.5-1
- New Upstream Version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Domingo Becker <domingobecker@gmail.com> - 1.2.4-1
- Update to new upstream version.
- Removed first line.
- Fixed BuildRequires to make it more readable.
- Removed python-django as required for build.
- Fixed dependency python-devel to python2-devel.
- Fixed docs in files section.
- Fixed "installed but unpackaged" error for egg-info in files section.

* Tue May 29 2012 Domingo Becker <domingobecker@gmail.com> - 1.1.4-5
- Removed BuildRoot, clean, defattr and rm -rf buildroot.

* Sat May 26 2012 Domingo Becker <domingobecker@gmail.com> - 1.1.4-4
- Package rename to python-django-ajax-selects. Please read
  https://fedoraproject.org/wiki/User:Bkabrda/Django_rename

* Sat Nov 20 2010 Domingo Becker <domingobecker@gmail.com> - 1.1.4-3
- Fixed License tag.
- Updated tarball to upstream one.

* Mon Nov 08 2010 Domingo Becker <domingobecker@gmail.com> - 1.1.4-2
- Fixed some rpmlint warnings.

* Mon Sep 27 2010 Domingo Becker <domingobecker@gmail.com> - 1.1.4-1
- Initial RPM release

