%global srcname colcon-ros

Name:           python-%{srcname}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Extension for colcon to support ROS packages

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to support ROS packages.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.4.14
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.7.0
BuildRequires:  python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.4.14
Requires:       python%{python3_pkgversion}-colcon-cmake >= 0.2.6
Requires:       python%{python3_pkgversion}-colcon-core >= 0.7.0
Requires:       python%{python3_pkgversion}-colcon-pkg-config
Requires:       python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.4
Requires:       python%{python3_pkgversion}-colcon-recursive-crawl
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       dpkg-dev
%else
Requires:       dpkg-dev
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support ROS packages.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colcon_ros


%check
%pytest -m 'not linter' test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Scott K Logan <logans@cottsay.net> - 0.5.0-1
- Update to 0.5.0 (rhbz#2294187)
- Switch to SPDX license identifier

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Scott K Logan <logans@cottsay.net> - 0.4.1-1
- Update to 0.4.1 (rhbz#2240876)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.23-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.23-2
- Rebuilt for Python 3.11

* Sat May 07 2022 Scott K Logan <logans@cottsay.net> - 0.3.23-1
- Update to 0.3.23 (rhbz#2074335)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Scott K Logan <logans@cottsay.net> - 0.3.22-1
- Update to 0.3.22 (rhbz#2035230)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.21-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Scott K Logan <logans@cottsay.net> - 0.3.21-1
- Update to 0.3.21 (rhbz#1889066)

* Wed Sep 30 2020 Scott K Logan <logans@cottsay.net> - 0.3.20-1
- Update to 0.3.20 (rhbz#1881838)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Scott K Logan <logans@cottsay.net> - 0.3.19-1
- Update to 0.3.19 (rhbz#1858472)

* Fri Jun 12 2020 Scott K Logan <logans@cottsay.net> - 0.3.18-1
- Update to 0.3.18 (rhbz#1846603)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-2
- Rebuilt for Python 3.9

* Mon Apr 13 2020 Scott K Logan <logans@cottsay.net> - 0.3.17-1
- Update to 0.3.17 (rhbz#1775856)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Scott K Logan <logans@cottsay.net> - 0.3.13-1
- Update to 0.3.13

* Thu Aug 29 2019 Scott K Logan <logans@cottsay.net> - 0.3.12-1
- Update to 0.3.12 (rhbz#1747250)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.11-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Scott K Logan <logans@cottsay.net> - 0.3.11-1
- Update to 0.3.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.3.10-1
- Update to 0.3.10
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7

* Fri Mar 01 2019 Scott K Logan <logans@cottsay.net> - 0.3.8-1
- Update to 0.3.8
- Handle automatic dependency generation (f30+)

* Mon Feb 04 2019 Scott K Logan <logans@cottsay.net> - 0.3.7-1
- Update to 0.3.7

* Wed Dec 26 2018 Scott K Logan <logans@cottsay.net> - 0.3.6-1
- Update to 0.3.6

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.3.5-1
- Initial package
