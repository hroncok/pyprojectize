%global srcname     qutepart
%global sum         Code editor widget
%global desc_common \
Qutepart is a code editor widget for PyQt. Features: \
    - Syntax highlighting for 196 languages. \
    - Smart indentation for many languages. \
    - Line numbers. \
    - Bookmarks. \
    - Advanced edit operations. \
    - Matching braces highlighting. \
    - Autocompletion based on document content. \
    - Marking too long lines with red line. \
    - Rectangular selection and copy-paste. \
    - Linter marks support.

# issue#69, tests for vim abort with python 3.7, maybe too slow?
%bcond_with     test_vim

Name:           python-%{srcname}
Version:        3.3.3
Release:        11%{?dist}
Summary:        %{sum}

# LGPL 2.1 >> 2.0 (explicitly allows dynamic linking)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/andreikop/%{srcname}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# https://github.com/andreikop/qutepart/issues/96
# Handle PEP623, forced on python3.12
Patch0:         qutepart-3.3.3-pep623.patch

BuildRequires:  gcc
BuildRequires:  pcre-devel

BuildRequires:  python3-qt5
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

BuildRequires:  xorg-x11-server-Xvfb

%description
%{desc_common}

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       pcre
Requires:       python3-qt5
Provides:       python-%{srcname}
Obsoletes:      python2-%{srcname} < 3.2.0

%description -n python3-%{srcname}
%{desc_common}


%prep
%setup -q -n %{srcname}-%{version}
%patch -P0 -p1
# disable PyQt5 mocking for sphinx
sed -i -r 's,(MOCK_MODULES = \[).*\],\1],' doc/source/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd doc
sphinx-build-3 source html
# E: non-standard-executable-perm
#find -name \*.so |xargs chmod 0755
# W: hidden-file-or-dir
rm -r html/.buildinfo html/.doctrees

%install
%pyproject_install
%pyproject_save_files -l '%{srcname}*'


%check
# let's find all modules and don't crash after execution
pushd tests
rm -f test_all.py
%if !%{with test_vim}
# FIXME (core dumped)
rm test_vim.py
%endif
# FIXME we saw crashes with python3 = 3.9, rhbz#1793009
%if 0%{?python3_version_nodots} > 38
true Skipping tests due to strange crashes! Python: %{python3_version_nodots} / %{?python3_pkgversion}
%else
# test_all.py: Look for all tests. Using test_* instead of
# test_*.py finds modules (test_syntax and test_indenter).
# Do some fake X
xvfb-run -s '-screen :0 1024x768x16'\
 %{__python3} -m unittest -vvv test_*
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md ChangeLog todo.txt
%doc doc/html/


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.3-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.3-9
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.3-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.3-4
- Workaround for Python 3.12 PEP632 change

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 3.3.3-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.3.3-1
- Update to 3.3.3 (#2117236)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Raphael Groner <raphgro@fedoraproject.org> - 3.3.2-1
- new version, rhbz#2023637
- fix crash with python 3.10, rhbz#2019640 

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1 (#1823013)

* Wed Mar 18 2020 Raphael Groner <projects.rg@smart.ms> - 3.3.0-3
- use correct build conditional, rhbz#1793009

* Wed Mar 18 2020 Raphael Groner <projects.rg@smart.ms> - 3.3.0-2
- rebuilt

* Mon Mar 16 2020 Raphael Groner <projects.rg@smart.ms> - 3.3.0-1
- new version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Raphael Groner <projects.rg@smart.ms> - 3.2.0-1
- new version
- fix execution of tests, avoid random freezes

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Raphael Groner <projects.rg@smart.ms> - 3.1-5
- add BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Raphael Groner <projects.rg@smart.ms> - 3.1-1
- new version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Raphael Groner <projects.rg@smart.ms> - 3.0.1-5
- explicitly set screen depth for tests: qt dropped support for depth 8

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.1-1
- new version

* Mon May 02 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.0-2
- rebuild for new python3-qt5

* Thu Apr 21 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.0-1
- bump to v3.0.0, now python3 only, rhbz#1328450

* Wed Mar 02 2016 Raphael Groner <projects.rg@smart.ms> - 2.2.3-1.20160229gitfdc29c7
- use upstream master as post-release

* Sun Feb 28 2016 Raphael Groner <projects.rg@smart.ms> - 2.2.3-1
- new version
- use main version for python3, get rid of py3 patches
- obsolete python2 package in Fedora 24+

* Sat Feb 27 2016 Raphael Groner <projects.rg@smart.ms> - 2.2.2-6
- rebuild to validate dependencies (bug with librsvg-2.so.2)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Raphael Groner <projects.rg@smart.ms> - 2.2.2-3
- add subpackages for python versioning
- experimental python3 support

* Mon Oct 19 2015 Raphael Groner <projects.rg@smart.ms> - 2.2.2-2
- take over from Jairo Llopis
- cleanup generally
- use LGPLv2 with "or later"
- add more documentation files
- execute tests
- fix permissions
- use new python macros
- use virtual provides of python2 module

* Fri Aug 28 2015 Jairo Llopis <yajo.sk8@gmail.com> 2.2.2-1
- New upstream version.

* Wed Aug 26 2015 Jairo Llopis <yajo.sk8@gmail.com> 2.2.0-7
- Fix some permissions.
- Remove Spanish descriptions, for easier maintenance.

* Mon May 4 2015 Jairo Llopis <yajo.sk8@gmail.com> 2.2.0-6
- Fix license macro in SPEC.
- Fix a couple of redundancies in SPEC.

* Thu Apr 30 2015 Jairo Llopis <yajo.sk8@gmail.com> 2.2.0-5
- New upstream version.
- Clear SPEC redundancies.
- Force usage of Python 2 macros in SPEC.

* Fri Feb 6 2015 Jairo Llopis <yajo.sk8@gmail.com> 2.1.0-4
- New upstream version.
- Update descriptions and dependencies to match upstream SPEC.
- Remove support for Fedora < 20.

* Mon Jul 7 2014 Jairo Llopis <yajo.sk8@gmail.com> 1.3.0-3
- New upstream version.
- Fix typo.

* Fri Oct 25 2013 Jairo Llopis <yajo.sk8@gmail.com> 1.1.0-2
- Fix comments.
- Fix translation.
- Fix CFLAGS when building.
- Fix license.

* Sun Sep 8 2013 Jairo Llopis <yajo.sk8@gmail.com>  1.1.0-1
- Initial release.
