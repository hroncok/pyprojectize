%global srcname Traits
%global modname traits
%global commit ac5d0296def6a389f932add5fbcab2eef6e7334e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Circular test deps with traitsui
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        6.4.3
Release:        4%{?dist}
Summary:        Explicitly typed attributes for Python
# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
License:        BSD-3-Clause AND CC-BY-3.0
URL:            http://docs.enthought.com/traits/
#Source0:        https://github.com/enthought/traits/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz
Source0:        https://github.com/enthought/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
# Upstream fix for Python 3.13
Patch:          https://github.com/enthought/traits/pull/1767.patch
BuildRequires:  gcc
BuildRequires:  xorg-x11-server-Xvfb

%description
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object
attributes, traits also have several additional characteristics:

* Initialization: A trait can be assigned a default value.
* Validation: A trait attribute's type can be explicitly declared.
* Delegation: The value of a trait attribute can be contained either
  in another object.
* Notification: Setting the value of a trait attribute can trigger
  notification of other parts of the program.
* Visualization: User interfaces that permit the interactive
  modification of a trait's value can be automatically constructed
  using the trait's definition.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-sphinx
%if %{without bootstrap}
BuildRequires:  python%{python3_pkgversion}-traitsui
%endif
Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-six
Provides:       python%{python3_pkgversion}-%{modname} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object
attributes, traits also have several additional characteristics:

* Initialization: A trait can be assigned a default value.
* Validation: A trait attribute's type can be explicitly declared.
* Delegation: The value of a trait attribute can be contained either
  in another object.
* Notification: Setting the value of a trait attribute can trigger
  notification of other parts of the program.
* Visualization: User interfaces that permit the interactive
  modification of a trait's value can be automatically constructed
  using the trait's definition.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1
# we already have a bit another flags
sed -i -e '/extra_compile_args=/d' setup.py

%build
%py3_build

%install
%py3_install

%check
pushd build/lib.%{python3_platform}-*
  export PYTHONPATH=%{buildroot}%{python3_sitearch}
  xvfb-run %__python3 -s -m unittest discover -v
popd

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst examples/tutorials README.rst
%{python3_sitearch}/%{modname}*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Python Maint <python-maint@redhat.com> - 6.4.3-3
- Rebuilt for Python 3.13

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 6.4.3-2
- Bootstrap for Python 3.13

* Tue Jan 30 2024 Orion Poplawski <orion@nwra.com> - 6.4.3-1
- Update to 6.4.3
- Fix and use SPDX license

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Orion Poplawski <orion@nwra.com> - 6.4.2-1
- Disable bootstrap

* Sun Aug 13 2023 Orion Poplawski <orion@nwra.com> - 6.4.2-1
- Update to 6.4.2
- Bootstrap build for Python 3.12 (FTBFS #2226136)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 20 2023 Python Maint <python-maint@redhat.com> - 6.4.1-4
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 6.4.1-3
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 13 2022 Orion Poplawski <orion@nwra.com> - 6.4.1-1
- Update to 6.4.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Python Maint <python-maint@redhat.com> - 6.3.2-5
- Rebuilt for Python 3.11

* Wed Jun 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 6.3.2-4
- Fix FTBFS with setuptools >= 62.1
Resolves: rhbz#2097086

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.3.2-3
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Orion Poplawski <orion@nwra.com> - 6.3.2-1
- Update to 6.3.2

* Thu Oct 14 2021 Orion Poplawski <orion@nwra.com> - 6.3.1-1
- Update to 6.3.1

* Sun Oct 10 2021 Orion Poplawski <orion@nwra.com> - 6.3.0-1
- Update to 6.3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.2.0-4
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.2.0-3
- Bootstrap for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Orion Poplawski <orion@nwra.com> - 6.2.0-1
- Update to 6.2.0

* Tue Aug 04 02:12:00 GMT 2020 Orion Poplawski <orion@nwra.com> - 6.1.1-1
- Update to 6.1.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Orion Poplawski <orion@nwra.com> - 6.1.0-1
- Update to 6.1.0

* Sat May 30 2020 Orion Poplawski <orion@nwra.com> - 6.0.0-3
- Add bootstrap config

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Orion Poplawski <orion@nwra.com> - 6.0.0-1
- Update to 6.0.0
- Use unittest instead of nose and run under Xvfb

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Orion Poplawski <orion@nwra.com> - 5.2.0-1
- Update to 5.2.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Orion Poplawski <orion@nwra.com> - 5.1.2-1
- Update to 5.1.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Orion Poplawski <orion@nwra.com> - 5.1.1-1
- Update to 5.1.1

* Mon Apr 15 2019 Orion Poplawski <orion@nwra.com> - 5.1.0-1
- Update to 5.1.0

* Tue Feb  5 2019 Orion Poplawski <orion@nwra.com> - 5.0.0-1
- Update to 5.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-2
- Subpackage python2-Traits has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 4.6.0-1
- Update to 4.6.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-18.gitac5d029
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-17.gitac5d029
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-16.gitac5d029
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-15.gitac5d029
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-14.gitac5d029
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-13.gitac5d029
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-12.gitac5d029
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-11.gitac5d029
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 2 2016 Orion Poplawski <orion@cora.nwra.com> - 4.5.0-10.gitac5d029
- Provide python2/3-traits

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-9.gitac5d029
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 4.5.0-8.gitac5d029
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 4.5.0-7.gitac5d029
- Update to snapshot
- Add python3 subpackage

* Mon Aug 10 2015 Orion Poplawski <orion@cora.nwra.com> - 4.5.0-5
- Modernize spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Orion Poplawski <orion@cora.nwra.com> - 4.5.0-1
- Update to 4.5.0

* Thu Jan 30 2014 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0

* Tue Aug 06 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-3
- Drop BR on python-setupdocs, no longer used

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0
- Add python lib provides filter
- Add Provides: python-traits
- Drop line-ending fix, no longer needed
- Add %%check
- Drop %%defattr

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 6 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-1
- Update to 4.2.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Rakesh Pandit <rakesh@fedoraproject.org> 3.5.0-1
- Updated to 3.5.0

* Fri Aug 13 2010 Chen Lei <supercyper@163.com> 3.4.0-1
- Update spec to match latest guidelines w.r.t %%clean
- Fix timestamps for example files
- Remove BR:numpy

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jan 31 2010 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-1
- Updated to 3.2.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-2
- Fixed missing setupdocs BR

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Updated

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.2-2
- Fixed permissions for ctraits.so and _speedups.so
- Fixed license after confirming from upstream

* Sun Dec 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.2-1
- Initial package
