%global pypi_name django-threadedcomments

Name:           python-%{pypi_name}
Version:        1.2
Release:        26%{?dist}
Summary:        A simple yet flexible threaded commenting system for Django

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/HonzaKral/%{pypi_name}
Source:         https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Django-threadedcomments is a Django application which allows for the
simple creation of a threaded commenting system. It is flexible as well,
partly due to its use of the same facilities that any other Django
application would use.

%package -n python3-%{pypi_name}
Summary:        %{summary} - Python 3 version

BuildRequires:  python3-devel
Requires:       python3-django

Obsoletes:      python-%{pypi_name} < 1.1-1
Obsoletes:      python2-%{pypi_name} < 1.1-1

%description -n python3-%{pypi_name}
Django-threadedcomments is a Django application which allows for the
simple creation of a threaded commenting system. It is flexible as well,
partly due to its use of the same facilities that any other Django
application would use.
This package provides Python 3 build of %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l threadedcomments

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst LICENSE.txt CHANGELOG.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2-24
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2-20
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.2-12
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.2-8
- Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.2-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1-1
- Update to version 1.1 and remove upstreamed patch
- Remove Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuild for Python 3.6

* Thu Sep 8 2016 Jan Beran <jberan@redhat.com> - 1.0.1-1
- update to version 1.0.1 + patch
- url and source update
- modernized specfile with Python 3 packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.0-7
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 16 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.0-5
- correct django-threadedcomments obs_ver once more, since there's an even
  newer build in F17

* Tue Sep 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.0-4
- correct django-threadedcomments obs_ver

* Wed Aug 14 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9.0-3
- remove doc that are not in directory

* Wed Aug 14 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9.0-2
- fix documents

* Wed Aug 14 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9.0-1
- New Upstream Version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 08 2013 Matthias Runge <mrunge@redhat.com> - 0.5.3-8
- change requirement to python-django14 (rhbz#950564)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Domingo Becker <domingobecker@gmail.com> - 0.5.3-5
- Added a more specific files section.
- Removed first line.
- Removed unnecessary BuildRequires python-django.
- Changed BuildRequires from python-devel to python2-devel.
- Fixed release number.

* Tue May 29 2012 Domingo Becker <domingobecker@gmail.com> - 0.5.3-4
- Removed BuildRoot, clean, defattr and rm -rf buildroot.

* Sun May 27 2012 Domingo Becker <domingobecker@gmail.com> - 0.5.3-3
- Package rename to python-django-threadedcomments. Please read
  https://fedoraproject.org/wiki/User:Bkabrda/Django_rename

* Mon Nov 08 2010 Domingo Becker <domingobecker@gmail.com> - 0.5.3-2
- new doc section excluding binary file ._pinax.txt from docs directory
- new description
- BuildRequires added Django.
- fixed changelog version of the previous one.

* Mon Sep 27 2010 Domingo Becker <domingobecker@gmail.com> - 0.5.3-1
- Initial RPM release


