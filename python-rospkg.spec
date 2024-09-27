%global srcname rospkg

Name:           python-%{srcname}
Version:        1.5.1
Release:        4%{?dist}
Summary:        Utilities for ROS package, stack, and distribution information

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://ros.org/wiki/rospkg
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
The ROS packaging system simplifies development and distribution of code
libraries. It enables you to easily specify dependencies between code
libraries, easily interact with those libraries from the command-line, and
release your code for others to use.


%package doc
Summary:        Documentation for %{name}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-catkin-sphinx
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-distro
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Obsoletes:      python2-%{srcname} < 1.1.10-3

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-distro
Requires:       python%{python3_pkgversion}-PyYAML
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The ROS packaging system simplifies development and distribution of code
libraries. It enables you to easily specify dependencies between code
libraries, easily interact with those libraries from the command-line, and
release your code for others to use.


%prep
%autosetup -p1 -n %{srcname}-%{version}

find test -type f | xargs sed -i '1{s@^#!/usr/bin/env python@#!%{__python3}@}'


%build
%py3_build

%make_build -C doc html man SPHINXBUILD=sphinx-build-%{python3_version}
rm doc/_build/html/.buildinfo


%install
%py3_install

# backwards compatibility symbolic links
pushd %{buildroot}%{_bindir}
for i in *; do
  ln -s ./$i python3-$i
done
popd
install -p -m0644 -D doc/man/rosversion.1 %{buildroot}%{_mandir}/man1/rosversion.1


%check
%if 0%{?rhel}
export LANG=en_US.UTF-8
%endif

%pytest


%files doc
%doc doc/_build/html

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/rosversion
%{_bindir}/python3-rosversion
%{_mandir}/man1/rosversion.1.*


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.1-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.13

* Fri May 03 2024 Scott K Logan <logans@cottsay.net> - 1.5.1-1
- Update to 1.5.1 (rhbz#2276182)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Scott K Logan <logans@cottsay.net> - 1.5.0-1
- Update to 1.5.0 (rhbz#2180332)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.11

* Fri May 27 2022 Scott K Logan <logans@cottsay.net> - 1.4.0-2
- Switch from nose to pytest

* Sat Apr 23 2022 Rich Mattes <richmattes@gmail.com> - 1.4.0-1
- Update to release 1.4.0 (rhbz#2058818)

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 1.3.0-4
- Apply upstream patch to use yaml safe_load function

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.10

* Fri Apr 16 2021 Scott K Logan <logans@cottsay.net> - 1.3.0-1
- Update to 1.3.0 (rhbz#1945454)

* Thu Feb 04 2021 Scott K Logan <logans@cottsay.net> - 1.2.10-1
- Update to 1.2.10 (rhbz#1897763)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Scott K Logan <logans@cottsay.net> - 1.2.8-1
- Update to 1.2.8 (rhbz#1849858)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Scott K Logan <logans@cottsay.net> - 1.2.6-1
- Update to 1.2.6 (rhbz#1831400)

* Mon Apr 20 2020 Scott K Logan <logans@cottsay.net> - 1.2.4-2
- Add upstream patch for distro dependency

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 1.2.4-1
- Update to 1.2.4 (rhbz#1775451)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.10-3
- Subpackage python2-rospkg has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.10-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Scott K Logan <logans@cottsay.net> - 1.1.10-1
- Update to 1.1.10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Scott K Logan <logans@cottsay.net> - 1.1.9-1
- Update to 1.1.9 (rhbz#1700773)

* Fri Apr 12 2019 Scott K Logan <logans@cottsay.net> - 1.1.8-1
- Update to 1.1.8 (rhbz#1699085)
- Switch to Python 3 Sphinx
- Create a separate 'doc' package
- Handle automatic dependency generation (f30+)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.7-2
- Drop explicit locale setting for python3, use C.UTF-8 for python2
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Thu Sep 13 2018 Scott K Logan <logans@cottsay.net> - 1.1.7-1
- Update to 1.1.7 (rhbz#1441445)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 1.1.0-1
- Update to release 1.1.0 (rhbz#1425997)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Rich Mattes <richmattes@gmail.com> - 1.0.41-1
- Update to release 1.0.41 (rhbz#1329031)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.40-2
- Rebuild for Python 3.6

* Mon Sep 26 2016 Rich Mattes <richmattes@gmail.com> - 1.0.40-1
- Update to release 1.0.40 (rhbz#1329031)
- Remove dependencies on python-argparse

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.38-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Rich Mattes <richmattes@gmail.com> - 1.0.38-3
- Add additional architectures to uname test (rhbz#1290136)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 Rich Mattes <richmattes@gmail.com> - 1.0.38-1
- Update to release 1.0.38 (rhbz#1270086)

* Sun Oct 18 2015 Rich Mattes <richmattes@gmail.com> - 1.0.37-1
- Update to release 1.0.37 (rhbz#1270086)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 1.0.35-1
- Update to release 1.0.35
- Remove Fedora 12 spec conditionals

* Tue Dec 30 2014 Rich Mattes <richmattes@gmail.com> - 1.0.33-1
- Update to release 1.0.33
- Remove upstreamed patch

* Sat Oct 25 2014 Scott K Logan <logans@cottsay.net> - 1.0.31-1
- Update to release 1.0.31
- Fix test failure on PPC
- Remove argparse patch (fixed upstream)
- Fix sphinx and nose dependencies in el6
- Add python3 package

* Tue Jul 15 2014 Scott K Logan <logans@cottsay.net> - 1.0.29-1
- Update to release 1.0.29
- Fix test failure on ARM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Rich Mattes <richmattes@gmail.com> - 1.0.28-1
- Update to release 1.0.28
- Remove argparse from python dependency list (rhbz#1088448)
- Add requirement on python-argparse
- Add check section
- Add html documentation

* Fri Apr 04 2014 Scott K Logan <logans@cottsay.net> - 1.0.27-1
- Update to release 1.0.27
- Added PyYAML BuildRequires and Requires

* Sat Feb 08 2014 Rich Mattes <richmattes@gmail.com> - 1.0.26-1
- Update to release 1.0.26

* Mon Aug 19 2013 Rich Mattes <richmattes@gmail.com> - 1.0.21-1
- Update to release 1.0.21
- Update to github sourceurl guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20-2.20130318git0a4448e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Rich Mattes <richmattes@gmail.com> - 1.0.20-1.20130318git0a4448e
- Update to release 1.0.20

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Rich Mattes <richmattes@gmail.com> - 1.0.18-1
- Update to version 1.0.18

* Fri Oct 26 2012 Rich Mattes <richmattes@gmail.com> - 1.0.10-1
- Update to version 1.0.10

* Sat Sep 22 2012 Rich Mattes <richmattes@gmail.com> - 1.0.6-2
- Moved build to build section
- Finer-grained filenames in files section

* Sat Jun 16 2012 Rich Mattes <richmattes@gmail.com> - 1.0.6-1
- Update to version 1.0.6

* Sat Jun 02 2012 Rich Mattes <richmattes@gmail.com> - 1.0.3-1
- Update to version 1.0.3

* Wed Apr 25 2012 Rich Mattes <richmattes@gmail.com> - 1.0.2-1
- Initial package
