%global srcname locket

Name:           python-%{srcname}
Version:        1.0.0
Release:        11%{?dist}
Summary:        File-based locks for Python for Linux and Windows

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mwilliamson/%{srcname}.py/
Source0:        https://github.com/mwilliamson/%{srcname}.py/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Locket implements a lock that can be used by multiple processes provided they
use the same path.

Locks largely behave as (non-reentrant) Lock instances from the threading
module in the standard library. Specifically, their behaviour is:

 * Locks are uniquely identified by the file being locked, both in the same
   process and across different processes.
 * Locks are either in a locked or unlocked state.
 * When the lock is unlocked, calling acquire() returns immediately and
   changes the lock state to locked.
 * When the lock is locked, calling acquire() will block until the lock state
   changes to unlocked, or until the timeout expires.
 * If a process holds a lock, any thread in that process can call release()
   to change the state to unlocked.
 * Behaviour of locks after fork is undefined.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        File-based locks for Python for Linux and Windows
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-spur
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Locket implements a lock that can be used by multiple processes provided they
use the same path.

Locks largely behave as (non-reentrant) Lock instances from the threading
module in the standard library. Specifically, their behaviour is:

 * Locks are uniquely identified by the file being locked, both in the same
   process and across different processes.
 * Locks are either in a locked or unlocked state.
 * When the lock is unlocked, calling acquire() returns immediately and
   changes the lock state to locked.
 * When the lock is locked, calling acquire() will block until the lock state
   changes to unlocked, or until the timeout expires.
 * If a process holds a lock, any thread in that process can call release()
   to change the state to unlocked.
 * Behaviour of locks after fork is undefined.


%prep
%setup -q -n %{srcname}.py-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}*


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.11

* Fri Apr 22 2022 Orion Poplawski <orion@nwra.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.0-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Orion Poplawski <orion@nwra.com> - 0.2.0-11
- Fix python2 conditional

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 7 2018 Orion Poplawski <orion@nwra.com> - 0.2.0-10
- Drop Python 2 package for Fedora 30+ (bugz #1634974)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.2-2
- Use python2 names where possible

* Wed Apr 6 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.2-1
- Initial package
