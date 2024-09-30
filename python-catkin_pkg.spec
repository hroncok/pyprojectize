%global srcname catkin_pkg

Name:           python-%{srcname}
Version:        1.0.0
Release:        5%{?dist}
Summary:        Library for retrieving information about catkin packages

License:        BSD-3-Clause
URL:            https://github.com/ros-infrastructure/%{srcname}
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}


%package doc
Summary:        HTML documentation for %{name}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML API documentation for the Python module '%{srcname}'


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-docutils
Requires:       python%{python3_pkgversion}-pyparsing
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

PYTHONPATH=$PWD/build/lib \
  PYTHONDONTWRITEBYTECODE=1 \
  %make_build -C doc html SPHINXBUILD=sphinx-build-%{python3_version} SPHINXAPIDOC=sphinx-apidoc-%{python3_version}
rm doc/_build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files %{srcname}

# backwards compatibility symbolic links
pushd %{buildroot}%{_bindir}
for i in *; do
  ln -s ./$i python%{python3_pkgversion}-$i
done
popd


%check
%{__python3} -m pytest \
  --ignore=test/test_flake8.py \
  test


%files doc
%license LICENSE
%doc doc/_build/html

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{_bindir}/catkin_create_pkg
%{_bindir}/catkin_find_pkg
%{_bindir}/catkin_generate_changelog
%{_bindir}/catkin_package_version
%{_bindir}/catkin_prepare_release
%{_bindir}/catkin_tag_changelog
%{_bindir}/catkin_test_changelog
%{_bindir}/python%{python3_pkgversion}-catkin_create_pkg
%{_bindir}/python%{python3_pkgversion}-catkin_find_pkg
%{_bindir}/python%{python3_pkgversion}-catkin_generate_changelog
%{_bindir}/python%{python3_pkgversion}-catkin_package_version
%{_bindir}/python%{python3_pkgversion}-catkin_prepare_release
%{_bindir}/python%{python3_pkgversion}-catkin_tag_changelog
%{_bindir}/python%{python3_pkgversion}-catkin_test_changelog


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Scott K Logan <logans@cottsay.net> - 1.0.0-1
- Update to 1.0.0 (rhbz#2238988)
- Switch to SPDX license identifier

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.2-3
- Rebuilt for pyparsing-3.0.9

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.11

* Fri May 27 2022 Scott K Logan <logans@cottsay.net> - 0.5.2-1
- Update to 0.5.2 (rhbz#2090928)

* Tue May 10 2022 Scott K Logan <logans@cottsay.net> - 0.5.0-1
- Update to 0.5.0 (rhbz#2083893)

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 0.4.24-1
- Update to release 0.4.24
- Resolves: rhbz#2018262

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.23-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Scott K Logan <logans@cottsay.net> - 0.4.23-1
- Update to 0.4.23 (rhbz#1883763)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Scott K Logan <logans@cottsay.net> - 0.4.22-1
- Update to 0.4.22 (rhbz#1850827)

* Fri May 29 2020 Scott K Logan <logans@cottsay.net> - 0.4.20-1
- Update to 0.4.20 (rhbz#1835055)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.19-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Scott K Logan <logans@cottsay.net> - 0.4.19-1
- Update to 0.4.19 (rhbz#1824378)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.4.16-1
- Update to 0.4.16 (rhbz#1782360)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.4.14-1
- Update to 0.4.14 (rhbz#1762232)

* Sat Sep 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.13-3
- Subpackage python2-catkin_pkg has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.13-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Scott K Logan <logans@cottsay.net> - 0.4.13-1
- Update to 0.4.13

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Scott K Logan <logans@cottsay.net> - 0.4.12-1
- Update to 0.4.12 (rhbz#1702118)

* Mon Mar 25 2019 Scott K Logan <logans@cottsay.net> - 0.4.11-1
- Update to 0.4.11
- Switch to Python 3 Sphinx
- Handle automatic dependency generation (f30+)
- Make doc subpackage a weaker dependency

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Scott K Logan <logans@cottsay.net> - 0.4.10-2
- Add patch for argparse on Python 2.7

* Fri Jan 11 2019 Scott K Logan <logans@cottsay.net> - 0.4.10-1
- Update to 0.4.10
- Modernize spec
- Separate doc package

* Thu Sep 13 2018 Scott K Logan <logans@cottsay.net> - 0.4.8-1
- Update to 0.4.8 (rhbz#1597686)
- Add runtime requirement for pyparsing (rhbz#1628751)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-2
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.5-1
- Update to 0.4.5

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-3
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.3-2
- Fix build
- Add new bin scripts.

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.3-1
- Update to new upstream version

* Sat May 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.2-1
- Update to latest upstream release
- Tests fail. Disabling

* Sun Mar 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.1-2
- Add BR to fix tests

* Sun Mar 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.1-1
- Update to latest upstream release

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.9-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.9-2
- Remove patch, use sed instead to make it version independent

* Sun Dec 17 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.9-1
- Update to latest releas 0.3.9 (rhbz#1508241)

* Sat Dec 02 2017 Till Hofmann <thofmann@fedoraproject.org> - 0.3.8-2
- Add patch to remove argparse from the requirements

* Wed Oct 25 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.8-1
- Update to new release 0.3.8 (rhbz#1455183)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 0.3.1-1
- Update to release 0.3.1 (rhbz#1422069)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.10-6
- Rebuild for Python 3.6

* Tue Sep 27 2016 Rich Mattes <richmattes@gmail.com> - 0.2.10-5
- Remove argparse requirement

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 17 2015 Rich Mattes <richmattes@gmail.com> - 0.2.10-1
- Update to release 0.2.10 (rhbz#1250758)
- Remove upstreamed patches
- Fix spec file layout so spectool can parse it

* Tue Jun 30 2015 Scott K Logan <logans@cottsay.net> - 0.2.9-1
- Update to 0.2.9
- Switch to Github upstream to get docs
- Update to latest packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.7-1
- Update to 0.2.7

* Sat Oct 25 2014 Scott K Logan <logans@cottsay.net> - 0.2.6-1
- Update to 0.2.6

* Sat Oct 18 2014 Scott K Logan <logans@cottsay.net> - 0.2.5-1
- Update to 0.2.5
- Add python3 package
- Exclude tests which are not compatible with python 2.6

* Thu Jul 31 2014 Scott K Logan <logans@cottsay.net> - 0.2.4-1
- Update to 0.2.4
- Remove README.rst (not present in Pypi sources)

* Wed Jul 16 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.3-1
- Update to latest upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Scott K Logan <logans@cottsay.net> - 0.2.2-1
- Update to 0.2.2

* Thu Feb 06 2014 Scott K Logan <logans@cottsay.net> - 0.1.28-1
- Update to 0.1.28

* Thu Feb 06 2014 Scott K Logan <logans@cottsay.net> - 0.1.25-1
- Update to 0.1.25
- Added check section
- Added python-dateutil Requires/BuildRequires
- Added python-docutils Requires/BuildRequires
- Added python-nose BuildRequires
- Added python-mock BuildRequires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.1.18-1
- Update to 1.18
- https://bugzilla.redhat.com/show_bug.cgi?id=926034

* Sat Mar 16 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.1.10-1
- Initial rpm build



