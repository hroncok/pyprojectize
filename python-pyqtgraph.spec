%global _python_bytecompile_extra 0
%global srcname pyqtgraph
%global py3_deps python3-PyQt5 python3-numpy python3-pyopengl
%bcond_without docs

Name:           python-%{srcname}
Version:        0.13.7
Release:        5%{?dist}
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
URL:            https://www.pyqtgraph.org/
Source0:        https://github.com/pyqtgraph/pyqtgraph/archive/refs/tags/pyqtgraph-%{version}.tar.gz
Patch0:         no-sphinx-qt-doc.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# For Docs
%if %{with docs}
BuildRequires:  make %{py3_dist pydata-sphinx-theme sphinx sphinx_design}
BuildRequires:  %{py3_dist sphinx_rtd_theme sphinxext-rediraffe}
BuildRequires:  %{py3_dist sphinx_autodoc_typehints}
%endif
# For Tests
BuildRequires:  %{py3_dist h5py pytest pytest-xvfb scipy six}
BuildRequires:  mesa-dri-drivers %{py3_deps}

%global _description %{expand:
PyQtGraph is a pure-python graphics and GUI library built on PyQt4 / PySide and
numpy. It is intended for use in mathematics / scientific /engineering
applications. Despite being written entirely in python, the library is very
fast due to its heavy leverage of numpy for number crunching and Qt\'s
GraphicsView framework for fast display.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       %{py3_deps}

%description -n python3-%{srcname} %_description

%if %{with docs}
%package doc
Summary:        Documentation for the %{srcname} library

%description doc
This package provides documentation for the %{srcname} library.
%endif

%prep
%autosetup -p1 -n %{srcname}-%{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with docs}
make -C doc html
%endif

%install
%pyproject_install
rm -rf %{buildroot}/%{python3_sitelib}/pyqtgraph/examples
rm -f doc/build/html/.buildinfo
rm -f doc/build/html/objects.inv

%check
# https://github.com/pyqtgraph/pyqtgraph/issues/1475 (test_reload)
# https://github.com/pyqtgraph/pyqtgraph/issues/2110 (test_PolyLineROI)
%pytest -k "not (test_reload or test_PolyLineROI)"

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGELOG README.md
%{python3_sitelib}/*

%if %{with docs}
%files doc
%doc pyqtgraph/examples doc/build/html
%endif

%changelog
* Thu Aug 01 2024 Scott Talbert <swt@techie.net> - 0.13.7-5
- Update License tag to use SPDX identifiers

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Scott Talbert <swt@techie.net> - 0.13.7-3
- Enable building without docs

* Wed Jun 26 2024 Scott Talbert <swt@techie.net> - 0.13.7-2
- Rebuilt for Python 3.13

* Wed May 01 2024 Scott Talbert <swt@techie.net> - 0.13.7-1
- Update to new upstream release 0.13.7 (#2277667)

* Tue Apr 23 2024 Scott Talbert <swt@techie.net> - 0.13.6-1
- Update to new upstream release 0.13.6 (#2276249)

* Fri Mar 08 2024 Scott Talbert <swt@techie.net> - 0.13.4-1
- Update to new upstream release 0.13.4 (#2268482)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Scott Talbert <swt@techie.net> - 0.13.3-3
- Rebuilt for Python 3.12

* Mon Jun 19 2023 Scott Talbert <swt@techie.net> - 0.13.3-2
- Fix a couple of test issues/warnings with numpy 1.24+

* Wed Apr 26 2023 Scott Talbert <swt@techie.net> - 0.13.3-1
- Update to new upstream release 0.13.3 (#2175373)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Scott Talbert <swt@techie.net> - 0.13.1-1
- Update to new upstream release 0.13.1 (#2130347)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.12.4-3
- Rebuilt for Python 3.11

* Wed Mar 23 2022 Scott Talbert <swt@techie.net> - 0.12.4-2
- Skip test_PolyLineROI because it fails on aarch64 and ppc64le

* Fri Mar 04 2022 Scott Talbert <swt@techie.net> - 0.12.4-1
- Update to new upstream release 0.12.4 (#2060987)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Scott Talbert <swt@techie.net> - 0.12.3-1
- Update to new upstream release 0.12.3 (#2012669)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Scott Talbert <swt@techie.net> - 0.12.2-2
- Update GLTextItem patch to upstreamed version

* Sat Jul 10 2021 Scott Talbert <swt@techie.net> - 0.12.2-1
- Update to new upstream release 0.12.2 (#1980258)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.1-2
- Rebuilt for Python 3.10

* Sat Apr 10 2021 Scott Talbert <swt@techie.net> - 0.12.1-1
- Update to new upstream release 0.12.1 (#1946852)

* Sat Mar 27 2021 Scott Talbert <swt@techie.net> - 0.12.0-3
- BR setuptools

* Fri Mar 26 2021 Scott Talbert <swt@techie.net> - 0.12.0-2
- Apply upstream patch for Python 3.10 fixes (#1901925)

* Thu Mar 25 2021 Scott Talbert <swt@techie.net> - 0.12.0-1
- Update to new upstream release 0.12.0 (#1943345)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 13:59:44 EST 2020 Scott Talbert <swt@techie.net> - 0.11.1-1
- Update to new upstream release 0.11.1 (#1909448)

* Thu Nov 26 10:00:39 EST 2020 Scott Talbert <swt@techie.net> - 0.11.0-1
- Update to new upstream release (#1901997)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Scott Talbert <swt@techie.net> - 0.10.0-13
- Fix FTBFS with Python 3.9 (#1792947)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Scott Talbert <swt@techie.net> - 0.10.0-8
- Disable writing bytecode when running tests to avoid packaging pycache files

* Thu Sep 13 2018 Scott Talbert <swt@techie.net> - 0.10.0-7
- Indicate that we don't want to bytecompile the extra python files

* Tue Sep 11 2018 Scott Talbert <swt@techie.net> - 0.10.0-6
- Remove Python 2 subpackage (appears to be unused)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-4
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Scott Talbert <swt@techie.net> - 0.10.0-3
- Disable additional tests that only fail under Koji, fixes FTBFS (#1556569)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jul 30 2017 Scott Talbert <swt@techie.net> - 0.10.0-1
- New upstream release 0.10.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-12
- Rebuild for Python 3.6

* Wed Jul 20 2016 Scott Talbert <swt@techie.net> - 0.9.10-11
- De-fuzz the disable-failing-tests patch to fix F25 FTBFS

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 01 2016 Scott Talbert <swt@techie.net> - 0.9.10-9
- Update dependency names

* Sat Feb 06 2016 Scott Talbert <swt@techie.net> - 0.9.10-8
- Cherry-pick a couple of upstream patches to fix test failures on F24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Scott Talbert <swt@techie.net> - 0.9.10-6
- Remove pytest path patch on F23+ - fixes FTBFS with Python 3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 07 2015 Scott Talbert <swt@techie.net> - 0.9.10-4
- Moved documentation to subpackage

* Tue Aug 04 2015 Scott Talbert <swt@techie.net> - 0.9.10-3
- Fix and run tests, move examples to docs, add docs

* Sun Aug 02 2015 Scott Talbert <swt@techie.net> - 0.9.10-2
- Build python2 package also; update to latest python packaging standards

* Fri Jul 31 2015 Scott Talbert <swt@techie.net> 0.9.10-1
- Initial packaging.
