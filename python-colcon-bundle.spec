%global srcname colcon-bundle

Name:           python-%{srcname}
Version:        0.1.3
Release:        8%{?dist}
Summary:        Plugin to bundle built software for the colcon command line tool

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This package is a plugin to colcon-core. It provides functionality to bundle a
built workspace. A bundle is a portable environment which can be moved to a
different linux system and executed as if the contents of the bundle was
installed locally.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.15
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-jinja2 >= 2.9.0
BuildRequires:  python%{python3_pkgversion}-pytest

%if !0%{?rhel} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
%endif

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-bash >= 0.4.2
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.15
Requires:       python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.1
Requires:       python%{python3_pkgversion}-distro >= 1.2.0
Requires:       python%{python3_pkgversion}-jinja2 >= 2.9.0
Requires:       python%{python3_pkgversion}-setuptools >= 30.3.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This package is a plugin to colcon-core. It provides functionality to bundle a
built workspace. A bundle is a portable environment which can be moved to a
different linux system and executed as if the contents of the bundle was
installed locally.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colcon_bundle


%check
%{__python3} -m pytest \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc NOTICE README.md


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.3-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.3-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Scott K Logan <logans@cottsay.net> - 0.1.3-1
- Update to 0.1.3 (rhbz#2196633)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Scott K Logan <logans@cottsay.net> - 0.1.0-2
- Add some patches from upstream (rhbz#1908156)

* Tue Dec 15 2020 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Update to 0.1.0 (rhbz#1907692)

* Wed Sep 02 2020 Scott K Logan <logans@cottsay.net> - 0.0.24-1
- Update to 0.0.24

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Scott K Logan <logans@cottsay.net> - 0.0.23-1
- Update to 0.0.23 (rhbz#1855921)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.0.20-1
- Update to 0.0.20 (rhbz#1818496)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Scott K Logan <logans@cottsay.net> - 0.0.18-1
- Update to 0.0.18 (rhbz#1742142)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.15-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Scott K Logan <logans@cottsay.net> - 0.0.15-1
- Update to 0.0.15 (rhbz#1722296)
- Ignore a test due to known Python 3.8 incompatibility (rhbz#1721930)

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.0.13-1
- Update to 0.0.13
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Mon Feb 04 2019 Scott K Logan <logans@cottsay.net> - 0.0.10-1
- Update to 0.0.10

* Mon Nov 26 2018 Scott K Logan <logans@cottsay.net> - 0.0.8-1
- Update to 0.0.8

* Wed Nov 21 2018 Scott K Logan <logans@cottsay.net> - 0.0.6-1
- Update to 0.0.6

* Thu Nov 01 2018 Scott K Logan <logans@cottsay.net> - 0.0.5-1
- Update to 0.0.5

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.0.4-1
- Initial package
