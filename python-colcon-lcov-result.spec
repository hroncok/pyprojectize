%global srcname colcon-lcov-result

Name:           python-%{srcname}
Version:        0.5.2
Release:        8%{?dist}
Summary:        Extension for colcon to provide test results using LCOV

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to provide aggregate coverage results using LCOV.

LCOV is a graphical front-end for GCC's coverage testing tool gcov, producing
the following coverage metrics:
- Statement coverage
- Function coverage
- Branch coverage


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.5.6
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     binutils
Recommends:     gcc
Recommends:     lcov
%else
Requires:       binutils
Requires:       gcc
Requires:       lcov
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide aggregate coverage results using LCOV.

LCOV is a graphical front-end for GCC's coverage testing tool gcov, producing
the following coverage metrics:
- Statement coverage
- Function coverage
- Branch coverage


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colcon_lcov_result


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.2-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.2-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Scott K Logan <logans@cottsay.net> - 0.5.2-1
- Update to 0.5.2 (rhbz#2179716)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Scott K Logan <logans@cottsay.net> - 0.5.0-8
- Add dependency on command line tools (gcov/lcov/genhtml/c++flit)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Scott K Logan <logans@cottsay.net> - 0.5.0-1
- Update to 0.5.0 (rhbz#1906396)

* Wed Sep 30 2020 Scott K Logan <logans@cottsay.net> - 0.4.1-1
- Update to 0.4.1 (rhbz#1881545)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Scott K Logan <logans@cottsay.net> - 0.4.0-1
- Initial package (rhbz#1833741)
