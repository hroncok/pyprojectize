%global srcname rosinstall_generator

Name:           python-%{srcname}
Version:        0.1.23
Release:        8%{?dist}
Summary:        Generates rosinstall files

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://wiki.ros.org/%{srcname}
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
The rosinstall_generator generates rosinstall files containing information
about repositories with ROS packages/stacks.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.1.28
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-rosdistro >= 0.7.3
BuildRequires:  python%{python3_pkgversion}-rospkg
BuildRequires:  python%{python3_pkgversion}-yaml
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.1.28
Requires:       python%{python3_pkgversion}-rosdistro >= 0.7.3
Requires:       python%{python3_pkgversion}-rospkg
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-yaml
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The rosinstall_generator generates rosinstall files containing information
about repositories with ROS packages/stacks.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_bindir}/%{srcname}-%{python3_version}
ln -s %{srcname}-%{python3_version} %{buildroot}%{_bindir}/%{srcname}


%check
%pytest test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-%{python3_version}


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.23-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.1.23-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.1.23-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Scott K Logan <logans@cottsay.net> - 0.1.23-1
- Update to 0.1.23 (rhbz#2174298)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.22-7
- Rebuilt for Python 3.11

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 0.1.22-6
- Apply upstream patch to use yaml safe_loader
- Resolves: rhbz#2046911

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.22-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Scott K Logan <logans@cottsay.net> - 0.1.22-1
- Update to 0.1.22 (rhbz#1854209)

* Thu Jun 25 2020 Scott K Logan <logans@cottsay.net> - 0.1.21-1
- Update to 0.1.21 (rhbz#1850826)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.19-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.1.19-1
- Update to 0.1.19 (rhbz#1823982)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.1.18-1
- Update to 0.1.18 (rhbz#1742963)

* Fri Sep 13 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.16-4
- Drop python2 sub package
- https://bugzilla.redhat.com/show_bug.cgi?id=1740996

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.16-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Scott K Logan <logans@cottsay.net> - 0.1.16-1
- Update to 0.1.16

* Fri Mar 15 2019 Scott K Logan <logans@cottsay.net> - 0.1.15-1
- Update to 0.1.15
- Add checks
- Handle automatic dependency generation
- Use version macros

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.14-2
- Rebuilt for Python 3.7

* Sun Mar 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.14-1
- Update to latest upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Rich Mattes <richmattes@gmail.com> - 0.1.13-2
- Add runtime requirements

* Wed Dec 21 2016 Rich Mattes <richmattes@gmail.com> - 0.1.13-1
- Update to release 0.1.13

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.11-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 19 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.11-3
- Build python3 package also

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 04 2015 Scott K Logan <logans@cottsay.net> - 0.1.11-1
- Update to release 0.1.11
- Update to latest packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 30 2014 Rich Mattes <richmattes@gmail.com> - 0.1.10-1
- Update to release 0.1.10
- Update to fedora github guidelines for source url

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Scott K Logan <logans@cottsay.net> 0.1.9-1
- Update to latest upstream release

* Thu Feb 20 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.1.8-1
- Update to latest upstream release
- rhbz 1066906

* Sat Feb 08 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.1.7-1
- Updated as per comments in rhbz 1062843
-  Initial rpm build
