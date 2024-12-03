# Disable Python 2
%bcond_with python2
# Enable Python 3
%bcond_without python3

%global commit 9b9fddf596a77e6b7e0407f0e45d02ca3a5ba5e1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-stomper
Version:        0.4.3
Release:        23%{?dist}
Summary:        A python client implementation of the STOMP protocol
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.io/project/stomper

Source0:        https://pypi.io/packages/source/s/stomper/stomper-%{version}.tar.gz

# Python 3.12 compatibility for tests
Patch:          https://github.com/oisinmulvihill/stomper/pull/15.patch

BuildArch:      noarch

%description
This is a python client implementation of the STOMP protocol. The client is
attempting to be transport layer neutral. This module provides functions to
create and parse STOMP messages in a programatic fashion.

%if %{with python2}
%package -n python2-stomper
Summary:        A python client implementation of the STOMP protocol

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
BuildRequires:  python2-future
%if %{undefined __pythondist_requires}
Requires:       python2-future
%endif

%description -n python2-stomper
This is a python client implementation of the STOMP protocol. The client is
attempting to be transport layer neutral. This module provides functions to
create and parse STOMP messages in a programatic fashion.
%endif

%if %{with python3}
%package -n python3-stomper
Summary:        A python client implementation of the STOMP protocol

BuildRequires:  python3-devel
BuildRequires:  python3-nose

%description -n python3-stomper
This is a python client implementation of the STOMP protocol. The client is
attempting to be transport layer neutral. This module provides functions to
create and parse STOMP messages in a programatic fashion.
%endif

%prep
%autosetup -n stomper-%{version} -p1
# Drop unneeded dependency on python3-future
# https://github.com/oisinmulvihill/stomper/issues/16
sed -i "s/'future'//" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with python2}
%{py2_build}
%endif
%if %{with python3}
%{pyproject_wheel}
%endif

%install
%if %{with python2}
%{py2_install}
%endif
%if %{with python3}
%{pyproject_install}
%pyproject_save_files 'stomper*'
%endif

%check
%pyproject_check_import

%if %{with python2}
PYTHONPATH=. nosetests-%{python2_version} -q
%endif
%if %{with python3}
PYTHONPATH=. nosetests-%{python3_version} -q
%endif

%if %{with python2}
%files -n python2-stomper
%doc README.rst
%{python2_sitelib}/stomper*
%endif

%if %{with python3}
%files -n python3-stomper -f %{pyproject_files}
%doc README.rst
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.3-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.3-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.4.3-17
- Rebuilt for Python 3.12

* Thu Jun 15 2023 Petr Viktorin <pviktori@redhat.com> - 0.4.3-16
- Python 3.12 compatibility for tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.3-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 0.4.3-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-4
- Rebuilt for Python 3.8

* Fri Aug 02 2019 mprahl <mprahl@redhat.com> - 0.4.3-3
- Stop building Python 2 packages for F31+

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 0.4.3-1
- Update to 0.4.3. Fixes bug #1697989

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-9
- Enable python dependency generator

* Tue Dec 18 2018 Ralph Bean <rbean@redhat.com> - 0.4.1-8
- Complete py3 conditionals in preparation for a epel7 update.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuild for Python 3.6

* Fri Jul 29 2016 Kevin Fenzi <kevin@scrye.com> - 0.4.1-1
- Update to 0.4.1. Fixes bug #1355749

* Mon Jul 11 2016 Ralph Bean <rbean@redhat.com> - 0.4.0-2
- Explicit py2 and py3 subpackages.
- Patch implicit encoding in setup.py.

* Mon Jul 11 2016 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- new version
- New dep on python-future

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Ralph Bean <rbean@redhat.com> - 0.3.0-1
- new version

* Mon Sep 15 2014 Ralph Bean <rbean@redhat.com> - 0.2.9-1
- New upstream supporting STOMP-1.1.
- Use github tarball, https://github.com/oisinmulvihill/stomper/issues/8
- Use python2 macros.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Luke Macken <lmacken@redhat.com> - 0.2.8-1
- Update to 0.2.8 (#949150)
- Update the URLs
- Modernize the specfile

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 21 2010 Luke Macken <lmacken@redhat.com> - 0.2.4-1
- Update to 0.2.4 (#639565)

* Tue Sep 07 2010 Luke Macken <lmacken@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Sep 03 2009 Luke Macken <lmacken@redhat.com> - 0.2.2-9
- Require python-uuid when using Python2.4 only
- Run the test suite in %%check

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Silas Sewell <silas at sewell ch> - 0.2.2-7
- Remove Python version dependency

* Sun Mar 29 2009 Silas Sewell <silas at sewell ch> - 0.2.2-6
- Fix dependencies

* Thu Mar 26 2009 Silas Sewell <silas at sewell ch> - 0.2.2-5
- Update package name to conform to Fedora naming standards
- Change define to global

* Fri Mar 20 2009 Silas Sewell <silas at sewell ch> - 0.2.2-4
- Update upstream package to remove hidden files

* Thu Mar 05 2009 Silas Sewell <silas at sewell ch> - 0.2.2-3
- Manually remove hidden files

* Wed Dec 17 2008 Silas Sewell <silas at sewell ch> - 0.2.2-2
- Increase Python requirements to 2.5 because stomper uses uuid

* Wed Dec 17 2008 Silas Sewell <silas at sewell ch> - 0.2.2-1
- Initial package
