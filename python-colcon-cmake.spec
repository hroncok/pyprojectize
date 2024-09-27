%global srcname colcon-cmake

Name:           python-%{srcname}
Version:        0.2.28
Release:        4%{?dist}
Summary:        Extension for colcon to support CMake packages

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to support CMake projects.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.5.6
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.5.6
Requires:       python%{python3_pkgversion}-colcon-library-path
Requires:       python%{python3_pkgversion}-colcon-test-result >= 0.3.3
Requires:       python%{python3_pkgversion}-packaging
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support CMake projects.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_cmake/
%{python3_sitelib}/colcon_cmake-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.28-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.28-2
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Scott K Logan <logans@cottsay.net> - 0.2.28-1
- Update to 0.2.28 (rhbz#2242421)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.27-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 31 2022 Scott K Logan <logans@cottsay.net> - 0.2.27-1
- Update to 0.2.27 (rhbz#2123074)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.26-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.26-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Scott K Logan <logans@cottsay.net> - 0.2.26-1
- Update to 0.2.26 (rhbz#1881836)

* Sun Aug 16 2020 Scott K Logan <logans@cottsay.net> - 0.2.25-1
- Update to 0.2.25 (rhbz#1868888)

* Wed Jul 29 2020 Scott K Logan <logans@cottsay.net> - 0.2.24-1
- Update to 0.2.24 (rhbz#1860172)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Scott K Logan <logans@cottsay.net> - 0.2.23-1
- Update to 0.2.23 (rhbz#1849942)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.22-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Scott K Logan <logans@cottsay.net> - 0.2.22-1
- Update to 0.2.22 (rhbz#1827879)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.21-1
- Update to 0.2.21 (rhbz#1775860)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.2.16-1
- Update to 0.2.16 (rhbz#1762084)

* Fri Oct 11 2019 Scott K Logan <logans@cottsay.net> - 0.2.15-1
- Update to 0.2.15

* Tue Oct 01 2019 Scott K Logan <logans@cottsay.net> - 0.2.14-1
- Update to 0.2.14 (rhbz#1757562)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.13-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Scott K Logan <logans@cottsay.net> - 0.2.13-1
- Update to 0.2.13 (rhbz#1719546)

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.2.12-1
- Update to 0.2.12 (rhbz#1718091)

* Mon May 20 2019 Scott K Logan <logans@cottsay.net> - 0.2.11-1
- Update to 0.2.11

* Sat May 18 2019 Scott K Logan <logans@cottsay.net> - 0.2.10-1
- Update to 0.2.10

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.9-1
- Update to 0.2.9
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Mon Feb 11 2019 Scott K Logan <logans@cottsay.net> - 0.2.8-1
- Update to 0.2.8

* Fri Feb 08 2019 Scott K Logan <logans@cottsay.net> - 0.2.7-1
- Update to 0.2.7

* Mon Feb 04 2019 Scott K Logan <logans@cottsay.net> - 0.2.6-1
- Update to 0.2.6

* Wed Dec 26 2018 Scott K Logan <logans@cottsay.net> - 0.2.5-1
- Update to 0.2.5

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.4-2
- Fix python3_other requires

* Fri Oct 26 2018 Scott K Logan <logans@cottsay.net> - 0.2.4-1
- Initial package
