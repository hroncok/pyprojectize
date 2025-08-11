%global srcname colcon-notification

Name:           python-%{srcname}
Version:        0.3.0
Release:        3%{?dist}
Summary:        Extension for colcon to provide status notifications

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Taken from sources - disables install of data files per platform
Patch0:         %{name}-0.2.8-data-files.patch

BuildArch:      noarch

%description
An extension for colcon-core to provide status notifications.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.7
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.7
Requires:       python%{python3_pkgversion}-notify2
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide status notifications.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
BUILD_DEBIAN_PACKAGE=1 \
    %pyproject_wheel


%install
BUILD_DEBIAN_PACKAGE=1 \
    %pyproject_install
%pyproject_save_files -l colcon_notification


%check
%pyproject_check_import
%pytest -m 'not linter' test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.13

* Fri Mar 22 2024 Scott K Logan <logans@cottsay.net> - 0.3.0-1
- Update to 0.3.0 (rhbz#2269536)
- Switch to SPDX license identifier

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.15-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Scott K Logan <logans@cottsay.net> - 0.2.15-1
- Update to 0.2.15 (rhbz#2155375)

* Wed Aug 31 2022 Scott K Logan <logans@cottsay.net> - 0.2.14-1
- Update to 0.2.14 (rhbz#2123069)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.13-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.13-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.13-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Scott K Logan <logans@cottsay.net> - 0.2.13-1
- Update to 0.2.13 (rhbz#1824385)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.12-1
- Update to 0.2.12 (rhbz#1775866)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Scott K Logan <logans@cottsay.net> - 0.2.10-1
- Update to 0.2.10

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Scott K Logan <logans@cottsay.net> - 0.2.9-1
- Update to 0.2.9

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.2.8-2
- Set BUILD_DEBIAN_PACKAGE to relax setuptools requirement

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.2.8-1
- Update to 0.2.8 (rhbz#1718092)

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.7-2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Mon Mar 18 2019 Scott K Logan <logans@cottsay.net> - 0.2.7-1
- Update to 0.2.7
- Handle automatic dependency generation (f30+)

* Mon Jan 14 2019 Scott K Logan <logans@cottsay.net> - 0.2.6-1
- Update to 0.2.6

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.5-1
- Initial package
