%global srcname colcon-output

Name:           python-%{srcname}
Version:        0.2.13
Release:        8%{?dist}
Summary:        Extension for colcon to customize the output in various ways

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to customize the output in various ways.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.8
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to customize the output in various ways.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l colcon_output


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.13-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.13-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.13-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Scott K Logan <logans@cottsay.net> - 0.2.13-1
- Update to 0.2.13 (rhbz#2170313)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.12-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.12-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.12-1
- Update to 0.2.12 (rhbz#1885436)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Scott K Logan <logans@cottsay.net> - 0.2.11-1
- Update to 0.2.11 (rhbz#1849121)

* Fri Jun 12 2020 Scott K Logan <logans@cottsay.net> - 0.2.10-1
- Update to 0.2.10 (rhbz#1846604)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.9-1
- Update to 0.2.9 (rhbz#1783666)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Scott K Logan <logans@cottsay.net> - 0.2.6-1
- Update to 0.2.6 (rhbz#1757563)

* Tue Aug 27 2019 Scott K Logan <logans@cottsay.net> - 0.2.5-1
- Update to 0.2.5 (rhbz#1744679)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Scott K Logan <logans@cottsay.net> - 0.2.4-1
- Update to 0.2.4

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.3-2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.3-1
- Initial package
