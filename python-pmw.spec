# Turn off the brp-python-bytecompile script
%global srcname pmw

Name: python-pmw
Version: 2.1.1
Release: 9%{?dist}
Summary: Python powerwidgets
# Automatically converted from old format: MIT and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-MIT AND GPL-2.0-or-later
URL: http://pmw.sourceforge.net/
Source: http://downloads.sourceforge.net/pmw/Pmw-%{version}.tar.gz
BuildRequires: python3-devel
BuildRequires: dos2unix
BuildArch: noarch

# Fix identation errors, patch created by using 'autopep8-1.6.0'
Patch0: %{name}-fix_identation_error.patch

%description
Pmw is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It consists of a set of base classes and a
library of flexible and extensible megawidgets built on this
foundation. These megawidgets include notebooks, comboboxes, selection
widgets, paned widgets, scrolled widgets and dialog windows

%package -n python3-%{srcname}
Summary: Python powerwidgets
Requires: python3-tkinter

%description -n python3-%{srcname}
Pmw is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It consists of a set of base classes and a
library of flexible and extensible megawidgets built on this
foundation. These megawidgets include notebooks, comboboxes, selection
widgets, paned widgets, scrolled widgets and dialog windows.

%prep
%autosetup -n Pmw-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files Pmw

# file fixes
chmod 644 Pmw/Pmw_1_3_3/doc/*
chmod 644 Pmw/Pmw_2_1_1/doc/*

rm -rf %{buildroot}%{python3_sitelib}/Pmw/Pmw_1_3_3

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc Pmw/Pmw_2_1_1/doc

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.1-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-1
- Release 2.1.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-24
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-21
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-15
- Subpackage python2-pmw has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6
- Rebuild for Python 3.6

* Sat Jul 30 2016 Tim Fenn <tim.fenn@gmail.com> - 2.0.0-5
- fix python2 vs python3 packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Tim Fenn <tim.fenn@gmail.com> - 2.0.0-3
- more fixes for tkinter import

* Tue Jul 12 2016 Tim Fenn <tim.fenn@gmail.com> - 2.0.0-2
- fix for tkinter import

* Sun Apr 17 2016 Tim Fenn <tim.fenn@gmail.com> - 2.0.0-1
- update to 2.0.0
- add python3 module
- spec cleanups

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.2-17
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Tim Fenn <fenn@stanford.edu> - 1.3.2-8
- patch for unicode menus (Mamoru Tasaka), bug ID 500459

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.2-6
- Rebuild for Python 2.6

* Wed Oct 08 2008 Tim Fenn <fenn@stanford.edu> - 1.3.2-5
- remove python and python-devel from buildrequires/requires

* Sun Oct 05 2008 Tim Fenn <fenn@stanford.edu> - 1.3.2-4
- remove CFLAGS, minor fixes

* Thu Oct 02 2008 Tim Fenn <fenn@stanford.edu> - 1.3.2-3
- add doc to %%files, add egg-info, spec updates, change license

* Sun Sep 28 2008 Tim Fenn <fenn@stanford.edu> - 1.3.2-2
- fix build problems

* Fri Sep 12 2008 Tim Fenn <fenn@stanford.edu> - 1.3.2-1
- initial build
