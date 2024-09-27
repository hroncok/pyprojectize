%global with_tests 1

Name: autowrap
Summary: Generates Python Extension modules from [Cython] PXD files
Version: 0.22.11
Release: 10%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://pypi.org/project/autowrap/
Source0: https://github.com/OpenMS/autowrap/archive/refs/tags/release/%{version}/%{name}-release-%{version}.tar.gz
BuildArch: noarch

## For testing
BuildRequires: boost-devel
BuildRequires: gcc
BuildRequires: gcc-c++

%description
This module uses the Cython "header" .pxd files to automatically generate
Cython input (.pyx) files. It does so by parsing the header files and possibly
annotations in the header files to generate correct Cython code.

%package -n python%{python3_pkgversion}-autowrap
Summary: Generates Python3 Extension modules from [Cython] PXD files
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pytest
BuildRequires: python%{python3_pkgversion}-Cython
Obsoletes: python2-autowrap < 0:%{version}-%{release}
%if 0%{?rhel}
Obsoletes: python34-autowrap < 0:%{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-autowrap
%{summary}.

%prep
%setup -qc

##Remove bundled files
rm -rf %{name}-release-%{version}/autowrap/data_files/boost

%generate_buildrequires
%pyproject_buildrequires

%build
pushd %{name}-release-%{version}
%pyproject_wheel
popd

%install

pushd %{name}-release-%{version}
%pyproject_install

mkdir exe && pushd exe
for i in python%{python3_version}-autowrap autowrap-%{python3_version} autowrap-v%{version}-%{python3_version}; do
  touch -r $RPM_BUILD_ROOT%{_bindir}/autowrap $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/autowrap $RPM_BUILD_ROOT%{_bindir}/$i
done
popd
popd

%if 0%{?with_tests}
%check
pushd %{name}-release-%{version}
export CPPFLAGS="-I%{_includedir}/boost"
export CXXFLAGS="-I%{_includedir}/boost"
py.test-%{python3_version} -v tests
popd
%endif

%files -n python%{python3_pkgversion}-autowrap
%license %{name}-release-%{version}/LICENSE
%{_bindir}/autowrap
%{_bindir}/autowrap-%{python3_version}
%{_bindir}/python%{python3_version}-autowrap
%{_bindir}/autowrap-v%{version}-%{python3_version}
%{python3_sitelib}/autowrap/
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/*.dist-info

%changelog
* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.22.11-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.22.11-8
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Lumír Balhar <lbalhar@redhat.com> - 0.22.11-7
- Fix requirement for noarch package

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.22.11-3
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.22.11-1
- Release 0.22.11

* Sun Oct 30 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.22.10-1
- Release 0.22.10

* Fri Oct 21 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.22.9-1
- Release 0.22.9

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.22.8-2
- Rebuilt for Python 3.11

* Fri Apr 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.22.8-1
- Release 0.22.8

* Sat Feb 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.22.7-1
- Release 0.22.7

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 15 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.22.6-1
- Release 0.22.6

* Thu Jan 13 2022 Antonio Trande <sagitter@fedoraproject.org> - 0.22.5-1
- Release 0.22.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.22.3-2
- Rebuilt for Python 3.10

* Mon May 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.22.3-1
- Release 0.22.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.22.0-3
- Rebuilt for Python 3.9

* Sat May 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.22.0-2
- Rebuild for EPEL8-playground

* Fri May 01 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.22.0-1
- Release 0.22.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.19.1-1
- Release 0.19.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.19.0-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.19.0-3
- Unversioned commands point to Python3
- Obsolete Python2 version
- Obsolete Python34 version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.19.0-1
- Release 0.19.0

* Sat Sep 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.17.0-4
- Deprecate python2 on fedora 30+
- Prepare SPEC file for python3 migration on epel7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-2
- Rebuilt for Python 3.7

* Sat May 26 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.17.0-1
- Update to 0.17.0

* Thu May 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.16.0-1
- Update to 0.16.0

* Wed Feb 21 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.14.0-5.20170807git31dbeb
- Reorganize Python2 dependencies

* Wed Feb 21 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.14.0-4.20170807git31dbeb
- Explicit Python2 dependencies on fedora

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.14.0-3.20170807git31dbeb
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2.20170807git31dbeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.14.0-1.20170807git31dbeb
- Update to 0.14.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3.20170519git97b2f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.11.0-2.20170519git97b2f5
- Rebuilt for Boost 1.64

* Fri Jun 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.11.0-1.20170519git97b2f5
- Update to 0.11.0

* Sun Apr 23 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.10.0-1.20170412git669ea3
- Update to 0.10.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3.20161226gitee9a4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.2-2.20161226gitee9a4e
- Rebuilt for Boost 1.63

* Mon Dec 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.9.2-1.20161226gitee9a4e
- Update to 0.9.2

* Sat Dec 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.8.0-3.20130921git3f4808
- Exclude tests.test_main.test* (upstream bug #56)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2.20160921git3f4808
- Rebuild for Python 3.6

* Tue Nov 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.8.0-1.20130921git3f4808
- Update to 0.8.0

* Wed Aug 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.7.2-4.20130710git03c5d3
- Rebuild for Python-3.5.2

* Sat Aug 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.7.2-3.20130710git03c5d3
- Build Python3.4 version on epel7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2.20160710git03c5d3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.7.2-1.20130710git03c5d3
- Update to 0.7.2 (commit #03c5d3)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5.20151201gitbd06ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.7.1-4.20151201gitbd06ff
- Renamed Python2 package

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-3.20151201gitbd06ff
- Rebuilt for Boost 1.60

* Thu Dec 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.7.1-2.20151201gitbd06ff
- SPEC file adapted to recent guidelines for Python

* Thu Nov 26 2015 Antonio Trande <sagitter@fedoraproject.org> 0.7.1-1.20151201gitbd06ff
- Update to 0.7.1
- autowrap-? renamed as autowrap?

* Thu Nov 26 2015 Antonio Trande <sagitter@fedoraproject.org> 0.7.0-1.20151124gitd5e233
- Update to 0.7.0

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.6.1-11.20150209gitd0e9a5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 10 2015 Antonio Trande <sagitter@fedoraproject.org> 0.6.1-10.20150209gitd0e9a5
- Rebuilt for Python3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-9.20150209gitd0e9a5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 27 2015 Antonio Trande <sagitter@fedoraproject.org> 0.6.1-8.20150209gitd0e9a5
- Avoid executable conflicts

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.1-7.20150209gitd0e9a5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6.20150209gitd0e9a5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.6.1-5.20150209gitd0e9a5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4.20150209gitd0e9a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Antonio Trande <sagitter@fedoraproject.org> 0.6.1-3.20150209gitd0e9a5
- Adapted to EPEL6/7
- Built on F23

* Mon Feb 09 2015 Antonio Trande <sagitter@fedoraproject.org> 0.6.1-2.20150209gitd0e9a5
- Added missing pytest BR package
- Used %%license

* Mon Feb 09 2015 Antonio Trande <sagitter@fedoraproject.org> 0.6.1-1.20150209gitd0e9a5
- Update to 0.6.1

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.5.0-5.20140603git1753b9
- Rebuild for boost 1.57.0

* Thu Jul 31 2014 Antonio Trande <sagitter@fedoraproject.org> 0.5.0-4.20140603git1753b9
- Package is now noarch

* Wed Jul 30 2014 Antonio Trande <sagitter@fedoraproject.org> 0.5.0-3.20140603git1753b9
- Fixed BuildRequires and Requires for python3 sub-package
- Removed TODO and CONCEPT files as user documentation

* Wed Jun 11 2014 Antonio Trande <sagitter@fedoraproject.org> 0.5.0-2.20140603git1753b9
- Fixed nosetests command according to new default python3 stack on Fedora 21+

* Thu Jun 05 2014 Antonio Trande <sagitter@fedoraproject.org> 0.5.0-1.20140603git1753b9
- Release 0.5.0

* Mon Jun 02 2014 Antonio Trande <sagitter@fedoraproject.org> 0.4.0-4.20140602gitebde9f
- Update to a new commit (fixed all license headers)

* Mon Jun 02 2014 Antonio Trande <sagitter@fedoraproject.org> 0.4.0-3.20140321git26e901
- Removed conditional macros for EPEL
- Fixed Source0

* Sun Jun 01 2014 Antonio Trande <sagitter@fedoraproject.org> 0.4.0-2.20140321git26e901
- Fixed License
- Fixed Requires package for python2/python3
- Excluded 'tests' directories by packaging
- Performing building operations to packaging independent Python3 module
- Disabled generation of the useless debuginfo package

* Fri May 30 2014 Antonio Trande <sagitter@fedoraproject.org> 0.4.0-1.20140321git26e901
- Initial build
- Fixed Version tag
