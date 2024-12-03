%global srcname catkin_lint

Name:           python-%{srcname}
Version:        1.6.22
Release:        8%{?dist}
Summary:        Check catkin packages for common errors

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/fkie/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/fkie/catkin_lint/pull/111
# https://github.com/fkie/catkin_lint/issues/110
# https://bugzilla.redhat.com/show_bug.cgi?id=2259550
# Handle ntpath.isabs change in Python 3.13
Patch:          0001-Handle-changed-ntpath.isabs-behaviour-in-Python-3.13.patch

BuildArch:      noarch

%description
catkin_lint checks package configurations for the catkin build system of ROS.
It runs a static analysis of the package.xml and CMakeLists.txt files in your
package, and it will detect and report a number of common problems.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-nose2
BuildRequires:  python%{python3_pkgversion}-rosdistro
BuildRequires:  python%{python3_pkgversion}-rospkg
BuildRequires:  python%{python3_pkgversion}-setuptools_scm

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-lxml
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-rosdep
Recommends:     python%{python3_pkgversion}-rosdistro
Recommends:     python%{python3_pkgversion}-rospkg
%endif

%description -n python%{python3_pkgversion}-%{srcname}
catkin_lint checks package configurations for the catkin build system of ROS.
It runs a static analysis of the package.xml and CMakeLists.txt files in your
package, and it will detect and report a number of common problems.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} \
  %pyproject_wheel
mv build/scripts-%{python3_version}/%{srcname} build/scripts-%{python3_version}/%{srcname}-%{python3_version}
ln -s %{srcname}-%{python3_version} build/scripts-%{python3_version}/%{srcname}-3
ln -s %{srcname}-%{python3_version} build/scripts-%{python3_version}/%{srcname}


%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} \
  %pyproject_install
%pyproject_save_files -l %{srcname}

install -p -D -m0644 shell/bash/%{srcname} %{buildroot}%{_sysconfdir}/bash_completion.d/%{srcname}


%check
%pyproject_check_import

%{__python3} -m nose2 test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc changelog.txt README.rst
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-3
%{_bindir}/%{srcname}-%{python3_version}
%{_datadir}/bash-completion/completions/%{srcname}
%{_datadir}/fish/vendor_completions.d/%{srcname}.fish
%{_sysconfdir}/bash_completion.d/%{srcname}


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.22-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Adam Williamson <awilliam@redhat.com> - 1.6.22-6
- Backport PR #111 to handle changed ntpath.isabs in Python 3.13 (#2259550)
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 1.6.22-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Scott K Logan <logans@cottsay.net> - 1.6.22-1
- Update to 1.6.22 (rhbz#2115320)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 01 2022 Scott K Logan <logans@cottsay.net> - 1.6.17-4
- Add upstream patch for Python 3.11 compatibility (rhbz#2098858, rhbz#2113616)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.17-2
- Rebuilt for Python 3.11

* Sat Apr 23 2022 Rich Mattes <richmattes@gmail.com> - 1.6.17-1
- Update to release 1.6.17 (rhbz#2064036)

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 1.6.16-1
- Update to release 1.6.16
- Resolves: rhbz#1976062

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.12-2
- Rebuilt for Python 3.10

* Thu Feb 04 2021 Scott K Logan <logans@cottsay.net> - 1.6.12-1
- Update to 1.6.12 (rhbz#1897466)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Scott K Logan <logans@cottsay.net> - 1.6.10-1
- Update to 1.6.10 (rhbz#1851568)

* Mon Jun 22 2020 Scott K Logan <logans@cottsay.net> - 1.6.9-1
- Update to 1.6.9 (rhbz#1847827)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.8-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 1.6.8-1
- Update to 1.6.8 (rhbz#1776382)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Scott K Logan <logans@cottsay.net> - 1.6.2-1
- Update to 1.6.2 (rhbz#1767353)

* Mon Sep 16 2019 Scott K Logan <logans@cottsay.net> - 1.6.1-1
- Update to 1.6.1 (rhbz#1748135)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Scott K Logan <logans@cottsay.net> - 1.6.0-1
- Update to 1.6.0
- Handle automatic dependency generation (f30+)

* Tue Feb 12 2019 Scott K Logan <logans@cottsay.net> - 1.5.6-1
- Update to 1.5.6

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.4-3
- Subpackage python2-catkin_lint has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Scott K Logan <logans@cottsay.net> - 1.5.4-1
- Update to 1.5.4
- Align spec with current python examples

* Mon Sep 17 2018 Scott K Logan <logans@cottsay.net> - 1.5.3-1
- Update to 1.5.3 (rhbz#1591523)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.21-2
- Rebuilt for Python 3.7

* Mon Jun 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.21-1
- Update to 1.4.21

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.20-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.20-1
- Update to latest release

* Sun Mar 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.19-1
- Update to latest release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.17-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.17-1
- Update to release 1.4.17 (rhbz#1509944)

* Wed Oct 25 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.16-1
- Update to release 1.4.16 (rhbz#1443069)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 1.4.13-1
- Update to release 1.4.13 (rhbz#1440346)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 16 2016 Scott K Logan <logans@cottsay.net> - 1.4.6-1
- Update to 1.4.6

* Thu Apr 07 2016 Scott K Logan <logans@cottsay.net> - 1.4.5-1
- Update to 1.4.5
- Update to latest packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 17 2015 Rich Mattes <richmattes@gmail.com> - 1.4.3-1
- Update to release 1.4.3 (rhbz#1240452)

* Sat Jul 04 2015 Scott K Logan <logans@cottsay.net> - 1.4.0-1
- Update to 1.4.0
- Update to latest packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 1.3.11-1
- Update to release 1.3.11 (rhbz#1175223)

* Tue Dec 02 2014 Scott K Logan <logans@cottsay.net> - 1.3.8-1
- Update to release 1.3.8
- Add python3 package
- Enable check section

* Wed Jul 16 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.7-1
- Update to latest upstream release

* Mon Jun 09 2014 Scott K Logan <logans@cottsay.net> - 1.3.6-1
- Update to release 1.3.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Scott K Logan <logans@cottsay.net> 1.3.5-1
- Update to release 1.3.5

* Tue Apr 15 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.4-1
- Correct requires

* Sat Apr 05 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.4-1
- Initial package build
