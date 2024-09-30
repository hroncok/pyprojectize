%global srcname colcon-python-setup-py

Name:           python-%{srcname}
Version:        0.2.8
Release:        9%{?dist}
Summary:        Extension for colcon to support Python packages with a setup.py file

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to identify packages with a setup.py file by
introspecting the arguments to the setup() function call of setuptools.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.6.1
Requires:       python%{python3_pkgversion}-setuptools
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to identify packages with a setup.py file by
introspecting the arguments to the setup() function call of setuptools.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colcon_python_setup_py


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.8-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.8-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.8-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Scott K Logan <logans@cottsay.net> - 0.2.8-1
- Update to 0.2.8 (rhbz#2128557)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.7-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.7-1
- Update to 0.2.7 (rhbz#1885438)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Scott K Logan <logans@cottsay.net> - 0.2.6-1
- Update to 0.2.6 (rhbz#1858473)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.2.5-1
- Update to 0.2.5 (rhbz#1789467)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Scott K Logan <logans@cottsay.net> - 0.2.2-1
- Update to 0.2.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.1-2
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Sat Oct 27 2018 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Initial package
