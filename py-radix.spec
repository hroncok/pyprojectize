Name: py-radix
Summary: Radix tree data structure for Python
Version: 0.10.0
Release: 12%{?dist}

URL: https://github.com/mjschultz/py-radix
Source0: https://github.com/mjschultz/py-radix/archive/v%{version}/%{name}-%{version}.tar.gz

# Define PY_SSIZE_T_CLEAN, use ssize_t as the index type (PEP 353)
# Fixes Python 3.10 failures, https://bugzilla.redhat.com/1899466
Patch1: https://github.com/mjschultz/py-radix/pull/55.patch#/py-radix-0.10.0-py_ssize_t_clean.patch
# Change away from deprecated assertEquals and assertNotEquals to assertEqual
# Fixes Python 3.12 failures, https://bugzilla.redhat.com/2175152
Patch2: https://github.com/mjschultz/py-radix/pull/44.patch#/py-radix-0.10.0-assertequal.patch
# Change incompatible pointer type from RadixNodeObject to PyObject
# Fixes Python 3.13 failures, https://bugzilla.redhat.com/2259528
Patch3: https://github.com/mjschultz/py-radix/pull/58.patch#/py-radix-0.10.0-pyobject-type.patch

License: BSD-4-Clause AND ISC
BuildRequires: gcc

%description
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%package -n python3-%{name}
Summary: Radix tree data structure for Python

BuildRequires: python3-devel
# Needed for tests
BuildRequires: python3-pytest


%description -n python3-%{name}
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%prep
%autosetup -p1
rm -f inet_ntop.c strlcpy.c
touch inet_ntop.c strlcpy.c

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -v

%files -n python3-%{name}
%doc README.rst
%license LICENSE
%{python3_sitearch}/py_radix*
%{python3_sitearch}/radix*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Robert Scheck <robert@fedoraproject.org> - 0.10.0-11
- Update license identifier to SPDX expression
- Add patch proposal to change incompatible pointer type (#2259528)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.10.0-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Kevin Fenzi <kevin@scrye.com> - 0.10.0-7
- Apply upstream patch to fix FTBFS. https://github.com/mjschultz/py-radix/pull/44

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.10.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.11

* Sat Apr 09 2022 Kevin Fenzi <kevin@scrye.com> - 0.10.0-1
- Update to 0.10.0.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.3-21
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-12
- Subpackage python2-py-radix has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-5
- Rebuild for Python 3.6

* Thu Jul 21 2016 Charalampos Stratakis <cstratak@redhat.com> 0.9.3-4
- Provide python 3 subpackage
- Renamed python 2 (sub)package
- Modernize SPEC

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 Kevin Fenzi <kevin@scrye.com> 0.9.3-1
- Update to 0.9.3
- Enable tests in check
- Point to new upstream site/repo

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Oct 23 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-6
- Add patch by Alexander Sabourenkov to fix memory leak (Debian #512830)

* Mon Oct 12 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-5
- remove inet_ntop.c and strlcpy.c for safety.  They're only used on
  Windows.

* Thu Oct  1 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-4
- more package cleanups during review
  - quiet setup, clean buildroot at install, drop python Requires,
    add dist tag.

* Thu Oct  1 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-2
- update for Fedora packaging guidelines

* Wed Jun 28 2006 Damien Miller <djm@mindrot.org>
- Build RPM
