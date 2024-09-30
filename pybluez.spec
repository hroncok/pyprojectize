Name:           pybluez
Version:        0.23
Release:        17%{?dist}
Summary:        Python API for the BlueZ bluetooth stack 

License:        GPL-2.0-only
URL:            https://github.com/pybluez/pybluez/wiki
Source0:        https://github.com/pybluez/pybluez/archive/%{version}.tar.gz
Patch0:         pybluez-py310.patch
Patch1:         no-2to3.patch
Patch2:         427.patch

BuildRequires:  bluez-libs-devel gcc
BuildRequires:  python3-devel
                   
%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create Bluetooth
applications.

%package -n     python3-bluez
Summary:        A Python interface to bluez for Python 3
Requires:       python3-gattlib

%description -n python3-bluez
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create Bluetooth
applications.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
# This file shouldn't be executable - it's going into %doc
chmod a-x examples/bluezchat/bluezchat.py
%pyproject_install
%pyproject_save_files '*'

%files -n python3-bluez -f %{pyproject_files}
%{!?_licensedir:%global license %%doc}
%license COPYING

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.23-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.23-12
- Rebuilt for Python 3.12

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.23-11
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.23-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.23-6
- Patch to define  PY_SSIZE_T_CLEAN macro.

* Tue Nov 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.23-5
- Don't use 2to3 in setup.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.23-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.23-1
- 0.23, revert to main upstram.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.22-20
- BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.22-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.22-17
- Drop Python 2 support.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.22-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.22-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.22-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.22-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Dec 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.22-8
- Require gattlib, BZ 1523930.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.22-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.22-1
- Update to 0.22

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Jul  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.21-1
- Update to 0.21
- Update SPEC, URL and Source, use %%license
- Build python3 bindings too

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Apr 14 2010 Will Woods <wwoods@redhat.com> - 0.18-1
- Bugfix update from upstream (includes btmodule patch)

* Wed Oct 08 2009 Paulo Roma <roma@lcg.ufrj.br> - 0.16-2
- Applied btmodule patch.

* Tue Jul 28 2009 Will Woods <wwoods@redhat.com> - 0.16-1
- New (bugfix) release from upstream

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.15-3
- Rebuild for Python 2.6

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.15-2
- Rebuild

* Wed Jun 4 2008 Will Woods <wwoods@redhat.com> - 0.15-1
- New upstream version

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-4
- Autorebuild for GCC 4.3

* Fri Dec 29 2006 - Will Woods <wwoods@redhat.com> - 0.9.1-3
- Clean up spec file some more after further comments in bug #218678

* Fri Dec 15 2006 - Will Woods <wwoods@redhat.com> - 0.9.1-2
- Clean up spec file according to comments in bug #218678

* Wed Dec 6 2006 - Will Woods <wwoods@redhat.com> - 0.9.1-1
- Initial packaging attempt.
