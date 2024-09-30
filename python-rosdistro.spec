%global srcname rosdistro

Name:           python-%{srcname}
Version:        0.9.1
Release:        4%{?dist}
Summary:        File format for managing ROS Distributions

# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            http://www.ros.org/wiki/rosdistro
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
The rosdistro tool allows you to get access to the full dependency tree and
the version control system information of all packages and repositories. To
increase performance, the rosdistro tool will automatically look for a cache
file on your local disk. If no cache file is found locally, it will try to
download the latest cache file from the server. The cache files are only used
to improve performance, and are not needed to get correct results. rosdistro
will automatically go to Github to find any dependencies that are not part
of the cache file. Note that operation without a cache file can be very slow,
depending on your own internet connection and the response times of Github.
The rosdistro tool will always write the latest dependency information to a
local cache file, to speed up performance for the next query.


%package doc
Summary:        HTML documentation for '%{name}'
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-catkin-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' python module


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        File format for managing ROS Distributions
BuildRequires:  git
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-rospkg
Obsoletes:      python2-%{srcname} < 0.7.4-4

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-rospkg
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The rosdistro tool allows you to get access to the full dependency tree and
the version control system information of all packages and repositories. To
increase performance, the rosdistro tool will automatically look for a cache
file on your local disk. If no cache file is found locally, it will try to
download the latest cache file from the server. The cache files are only used
to improve performance, and are not needed to get correct results. rosdistro
will automatically go to Github to find any dependencies that are not part
of the cache file. Note that operation without a cache file can be very slow,
depending on your own internet connection and the response times of Github.
The rosdistro tool will always write the latest dependency information to a
local cache file, to speed up performance for the next query.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Drop unsupported syntax in older setuptools
sed -i "s/mock; python_version < '3.3'//" setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

PYTHONPATH=$PWD/src \
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
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  %{__python3} -m pytest \
  -k 'not test_manifest_providers' \
  test


%files doc
%license LICENSE.txt
%doc doc/_build/html

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%{_bindir}/rosdistro_build_cache
%{_bindir}/rosdistro_freeze_source
%{_bindir}/rosdistro_migrate_to_rep_141
%{_bindir}/rosdistro_migrate_to_rep_143
%{_bindir}/rosdistro_reformat
%{_bindir}/python%{python3_pkgversion}-rosdistro_build_cache
%{_bindir}/python%{python3_pkgversion}-rosdistro_freeze_source
%{_bindir}/python%{python3_pkgversion}-rosdistro_migrate_to_rep_141
%{_bindir}/python%{python3_pkgversion}-rosdistro_migrate_to_rep_143
%{_bindir}/python%{python3_pkgversion}-rosdistro_reformat


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.13

* Fri May 03 2024 Scott K Logan <logans@cottsay.net> - 0.9.1-1
- Update to 0.9.1 (rhbz#2278971)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Scott K Logan <logans@cottsay.net> - 0.9.0-1
- Update to 0.9.0 (rhbz#2095797)
- Re-enable test_get_index_from_http_with_query_parameters

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 0.8.3-5
- Apply upstream patch to use yaml safe_load (rhbz#2046910)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Scott K Logan <logans@cottsay.net> - 0.8.3-1
- Update to 0.8.3 (rhbz#1883374)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Scott K Logan <logans@cottsay.net> - 0.8.2-1
- Update to 0.8.2 (rhbz#1838293)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Scott K Logan <logans@cottsay.net> - 0.8.1-1
- Update to 0.8.1 (rhbz#1824379)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.8.0-1
- Update to 0.8.0 (rhbz#1782354)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Scott K Logan <logans@cottsay.net> - 0.7.5-1
- Update to 0.7.5 (rhbz#1761003)

* Sat Sep 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-4
- Subpackage python2-rosdistro has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Scott K Logan <logans@cottsay.net> - 0.7.4-1
- Update to 0.7.4 (rhbz#1702421)

* Wed Mar 27 2019 Scott K Logan <logans@cottsay.net> - 0.7.3-1
- Update to 0.7.3 (rhbz#1693483)
- Switch to Python 3 Sphinx
- Handle automatic dependency generation (f30+)
- Make doc subpackage a weaker dependency

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Scott K Logan <logans@cottsay.net> - 0.7.2-1
- Update to 0.7.2 (rhbz#1668955)

* Fri Jan 11 2019 Scott K Logan <logans@cottsay.net> - 0.7.1-1
- Update to 0.7.1

* Tue Nov 06 2018 Scott K Logan <logans@cottsay.net> - 0.7.0-1
- Update to 0.7.0
- Conditional python2 package
- Use python3_pkgversion
- Create a separate 'doc' package

* Fri Sep 14 2018 Scott K Logan <logans@cottsay.net> - 0.6.9-1
- Update to 0.6.9 (rhbz#1525745)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-5
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 0.6.2-1
- Update to release 0.6.2 (rhbz#1425644)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Rich Mattes <richmattes@gmail.com> - 0.5.0-1
- Update to release 0.5.0 (rhbz#1388280)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.7-4
- Rebuild for Python 3.6

* Tue Sep 27 2016 Rich Mattes <richmattes@gmail.com> - 0.4.7-3
- Remove python-argparse requirement

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 03 2016 Rich Mattes <richmattes@gmail.com> - 0.4.7-1
- Update to release 0.4.7 (rhbz#1304921)

* Wed Feb 10 2016 Rich Mattes <richmattes@gmail.com> - 0.4.4-1
- Update to release 0.4.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Rich Mattes <richmattes@gmail.com> - 0.4.2-1
- Update to release 0.4.2 (#1207455)

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 0.4.1-1
- Update to release 0.4.1

* Mon Dec 15 2014 Scott K Logan <logans@cottsay.net> - 0.4.0-1
- Update to release 0.4.0

* Sat Oct 25 2014 Scott K Logan <logans@cottsay.net> - 0.3.7-1
- Update to release 0.3.7
- Remove argparse patch (fixed upstream)
- Fix sphinx dependency in el6
- Add check section
- Add python3 package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Scott K Logan <logans@cottsay.net> - 0.3.5-1
- Update to release 0.3.5
- Remove argparse from python dependency list
- Added missing install requirements
- Remove patch for setuptools (merged upstream)

* Tue Apr 08 2014 Rich Mattes <richmattes@gmail.com> - 0.3.4-2
- Depend on setuptools instead of distribute

* Sat Feb 08 2014 Rich Mattes <richmattes@gmail.com> - 0.3.4-1
- Update to release 0.3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-3.20130602git6e83551
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Rich Mattes <richmattes@gmail.com> - 0.2.8-2.20130602git6e83551
- Update BuildRequires to python2-devel
- Remove cleanup of buildroot in install

* Sun Jun 02 2013 Rich Mattes <richmattes@gmail.com> - 0.2.8-1.20130602git6e83551
- Initial package
