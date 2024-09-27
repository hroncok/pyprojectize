%global srcname osrf_pycommon
%global pkgname osrf-pycommon

Name:           python-%{pkgname}
Version:        2.1.4
Release:        6%{?dist}
Summary:        Commonly needed Python modules used by software developed at OSRF

# The entire source code is ASL 2.0 except parts of osrf_pycommon/terminal_color/windows.py which is BSD
# Automatically converted from old format: ASL 2.0 and BSD - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-BSD
URL:            http://osrf-pycommon.readthedocs.org/
Source0:        https://github.com/osrf/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Don't attempt to query a webserver for intersphinx inventory
Patch0:         osrf_pycommon-2.0.0-intersphinx.patch

BuildArch:      noarch

%description
osrf_pycommon is a python package which contains commonly used Python
boilerplate code and patterns. Things like ANSI terminal coloring, capturing
colored output from programs using sub-process, or even a simple logging system
which provides some nice functionality over the built-in Python logging system.

The functionality provided here should be generic enough to be reused in
arbitrary scenarios and should avoid bringing in dependencies which are not
part of the standard Python library. Where possible Windows and Linux/OS X
should be supported, and where it cannot it should be gracefully degrading.


%package doc
Summary:        API Documentation for the osrf_pycommon Python modules
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation generated from osrf_pycommon sources to be used in
developing software which uses osrf_pycommon.


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  python%{python3_pkgversion}-importlib-metadata
%endif
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{pkgname}
osrf_pycommon is a python package which contains commonly used Python
boilerplate code and patterns. Things like ANSI terminal coloring, capturing
colored output from programs using sub-process, or even a simple logging system
which provides some nice functionality over the built-in Python logging system.

The functionality provided here should be generic enough to be reused in
arbitrary scenarios and should avoid bringing in dependencies which are not
part of the standard Python library. Where possible Windows and Linux/OS X
should be supported, and where it cannot it should be gracefully degrading.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Don't install the package.xml
sed -i "\\|'share/' + package_name, \\['package.xml'\\]|d" setup.py

# Don't install the resource marker
sed -i "\\|('share/ament_index/resource_index/packages',|$!{
  N
  \\|('share/ament_index/resource_index/packages',\n *\\['resource/' + package_name\\])|d
  }" setup.py


%build
%py3_build

%make_build -C docs html man SPHINXBUILD=sphinx-build-%{python3_version}
rm docs/_build/html/.buildinfo


%install
%py3_install

install -p -m0644 -D docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1


%check
%pytest tests -k 'not test_code_format'


%files doc
%license LICENSE
%doc docs/_build/html

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc CHANGELOG.rst README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_mandir}/man1/%{srcname}.1.gz


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.4-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Scott K Logan <logans@cottsay.net> - 2.1.4-1
- Update to 2.1.4 (rhbz#2233722)

* Fri Jul 21 2023 Scott K Logan <logans@cottsay.net> - 2.1.3-1
- Update to 2.1.3 (rhbz#2222415)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.1.2-2
- Rebuilt for Python 3.12

* Tue May 09 2023 Soctt K Logan <logans@cottsay.net> - 2.1.2-1
- Update to 2.1.2 (rhbz#2170020)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 16 2022 Scott K Logan <logans@cottsay.net> - 2.1.0-1
- Update to 2.1.0 (rhbz#2054780)
- Switch from nose to pytest
- Drop Python 2 from spec file as it isn't supported upstream anymore

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.11

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 2.0.0-1
- Update to release 2.0.0
- Resolves: rhbz#1987089
- Resolves: rhbz#2026340

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.10

* Thu Feb 04 2021 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Update to 0.2.1 (rhbz#1905288)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.10-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Scott K Logan <logans@cottsay.net> - 0.1.10-1
- Update to 0.1.10 (rhbz#1833518)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.1.9-1
- Update to 0.1.9 (rhbz#1762208)

* Mon Sep 30 2019 Scott K Logan <logans@cottsay.net> - 0.1.8-1
- Update to 0.1.8 (rhbz#1753048)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Scott K Logan <logans@cottsay.net> - 0.1.7-1
- Update to 0.1.7
- Use Python 3 Sphinx

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Scott K Logan <logans@cottsay.net> - 0.1.6-2
- Remove Python 2 subpackage from f30+ (rhbz#1666189)

* Thu Nov 15 2018 Scott K Logan <logans@cottsay.net> - 0.1.6-1
- Update to 0.1.6

* Fri Sep 14 2018 Scott K Logan <logans@cottsay.net> - 0.1.5-1
- Update to 0.1.5 (rhbz#1593273)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.7

* Sun May 27 2018 Rich Mates <richmattes@gmail.com> - 0.1.4-1
- Update to release 0.1.4 (rhbz#1459873)
- Remove upstream flake8 compatibility patch (rhbz#1377139)

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.2-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Rich Mattes <richmattes@gmail.com> - 0.1.2-3
- Fix FTBFS by adding upstream patch to use flake8 command line (rhbz#1377139)
- Use 'python3-flake8' for python 3 tests

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 18 2016 Scott K Logan <logans@cottsay.net> - 0.1.2-1
- Initial package
