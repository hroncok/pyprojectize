%global srcname colcon-bash

Name:           python-%{srcname}
Version:        0.5.0
Release:        4%{?dist}
Summary:        Extension for colcon to provide Bash scripts

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to provide Bash scripts.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.12.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide Bash scripts.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colcon_bash


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Scott K Logan <logans@cottsay.net> - 0.5.0-1
- Update to 0.5.0 (rhbz#2240871)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.2-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.4.2-1
- Update to 0.4.2 (rhbz#1800836)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Scott K Logan <logans@cottsay.net> - 0.4.1-1
- Update to 0.4.1 (rhbz#1757634)

* Thu Aug 29 2019 Scott K Logan <logans@cottsay.net> - 0.4.0-1
- Update to 0.4.0 (rhbz#1747247)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.3.2-2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7

* Fri Mar 01 2019 Scott K Logan <logans@cottsay.net> - 0.3.2-1
- Update to 0.3.2
- Handle automatic dependency generation (f30+)

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.3.1-1
- Initial package
