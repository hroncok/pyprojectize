%global srcname colcon-mixin

Name:           python-%{srcname}
Version:        0.2.3
Release:        8%{?dist}
Summary:        Extension for colcon to read CLI mixins from files

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to fetch and manage CLI mixins from repositories.

For an example repository containing mixins see colcon-mixin-repository.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.7.0
Requires:       python%{python3_pkgversion}-PyYAML
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to fetch and manage CLI mixins from repositories.

For an example repository containing mixins see colcon-mixin-repository.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colcon_mixin


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.3-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Scott K Logan <logans@cottsay.net> - 0.2.3-1
- Update to 0.2.3 (rhbz#2166745)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.11

* Thu Feb 10 2022 Scott K Logan <logans@cottsay.net> - 0.2.2-1
- Update to 0.2.2 (rhbz#2053360)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Update to 0.2.1 (rhbz#2035233)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Update to 0.2.0 (rhbz#1858470)

* Mon Jun 29 2020 Scott K Logan <logans@cottsay.net> - 0.1.10-1
- Update to 0.1.10 (rhbz#1850897)

* Fri Jun 12 2020 Scott K Logan <logans@cottsay.net> - 0.1.9-1
- Update to 0.1.9 (rhbz#1846602)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Scott K Logan <logans@cottsay.net> - 0.1.8-1
- Update to 0.1.8 (rhbz#1825080)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.1.7-1
- Update to 0.1.7 (rhbz#1775861)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.1.5-1
- Update to 0.1.5
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7

* Mon Mar 18 2019 Scott K Logan <logans@cottsay.net> - 0.1.4-1
- Update to 0.1.4
- Handle automatic dependency generation (f30+)

* Thu Jan 17 2019 Scott K Logan <logans@cottsay.net> - 0.1.3-1
- Update to 0.1.3

* Mon Jan 14 2019 Scott K Logan <logans@cottsay.net> - 0.1.2-1
- Update to 0.1.2

* Fri Nov 09 2018 Scott K Logan <logans@cottsay.net> - 0.1.1-2
- Fix source package description

* Fri Nov 09 2018 Scott K Logan <logans@cottsay.net> - 0.1.1-1
- Initial package
