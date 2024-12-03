%global srcname colcon-ros-bundle

Name:           python-%{srcname}
Version:        0.1.0
Release:        16%{?dist}
Summary:        Plugin for colcon to bundle ros applications

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Submitted upstream as colcon/colcon-ros-bundle#51
Patch0:         %{name}-0.1.0-unittest-mock.patch

BuildArch:      noarch

%description
This package is a plugin to colcon-core, that contains extensions for
colcon-bundle.

With this package you can use colcon bundle to create bundles of ROS
applications. A bundle is a portable environment that allows for execution of
the bundled application on a Linux host that does not have the application or
its dependencies installed in the root filesystem.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-bundle >= 0.0.18
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-rosdep >= 0.14.0

%if !0%{?rhel} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
%endif

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-bundle >= 0.0.18
Requires:       python%{python3_pkgversion}-colcon-ros >= 0.3.5
Requires:       python%{python3_pkgversion}-rosdep >= 0.14.0
Requires:       python%{python3_pkgversion}-setuptools >= 30.3.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This package is a plugin to colcon-core, that contains extensions for
colcon-bundle.

With this package you can use colcon bundle to create bundles of ROS
applications. A bundle is a portable environment that allows for execution of
the bundled application on a Linux host that does not have the application or
its dependencies installed in the root filesystem.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l colcon_ros_bundle


%check
%pyproject_check_import

%{__python3} -m pytest \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc NOTICE README.md


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.0-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.1.0-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.1.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Scott K Logan <logans@cottsay.net> - 0.1.0-8
- Drop dependency on standalone 'mock' package

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Update to 0.1.0 (rhbz#1908229)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.14-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.0.14-1
- Initial package
