Name:           python-yara
Version:        4.5.1
%global         baserelease     3
Summary:        Python binding for the YARA pattern matching tool
License:        Apache-2.0
URL:            https://github.com/VirusTotal/yara-python/
VCS:            https://github.com/VirusTotal/yara-python/
#               https://github.com/VirusTotal/yara-python/tags
#               https://github.com/VirusTotal/yara-python/releases/

# By default build from a release tarball.
# If you want to rebuild from a unversioned commit from git do that with
# rpmbuild --rebuild python-yara.src.dpm --without release
%bcond_without  release

%global         gituser         VirusTotal
%global         gitname         yara-python
%global         gitdate         20240525
%global         commit          2880de0358e1ec871093759d74309f4dc080d726
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})


%global         common_description %{expand:
Python binding for the YARA pattern matching tool.
YARA is a tool aimed at (but not limited to) helping malware researchers to
identify and classify malware samples. With YARA you can create descriptions
of malware families (or whatever you want to describe) based on textual or
binary patterns. Each description, a.k.a rule, consists of a set of strings
and a Boolean expression which determine its logic.}

# Build with python2 support for RHEL7
%if ( 0%{?rhel} && 0%{?rhel} <= 7 )
%bcond_without     python2
%endif

%if 0%{?with_release}
Release:        %{baserelease}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        %{baserelease}.%{gitdate}git%{shortcommit}%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz#/%{name}-%{version}-git%{gitdate}-%{shortcommit}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  pkgconfig(yara)
BuildRequires:  libtool
BuildRequires:  yara-devel >= %{version}
# html doc generation
BuildRequires:  /usr/bin/sphinx-build

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest


%if 0%{?with_python2}  > 0
BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif


%description
%{common_description}


#====================================================================
%package -n python%{python3_pkgversion}-yara
Summary:        Python3 binding for the YARA pattern matching tool



%description -n python%{python3_pkgversion}-yara
%{common_description}

%if 0%{?with_python2}  > 0
%package -n python2-yara
Summary:        Python2 binding for the YARA pattern matching tool


%description -n python2-yara
%{common_description}
%endif

#====================================================================
%prep
%if 0%{?with_release}
# Build from git release version
%autosetup -n yara-python-%{version}

%else
# Build from git commit
%autosetup -n yara-python-%{commit}
%endif



#====================================================================
%generate_buildrequires
%pyproject_buildrequires
%build
%if 0%{?with_python2}  > 0
%py2_build "--dynamic-linking"
%endif

%pyproject_wheel -C--global-option='"--dynamic-linking"'



#====================================================================
%install
%if 0%{?with_python2}  > 0
%py2_install
%endif

%pyproject_install
%pyproject_save_files 'yara*'


#====================================================================
%check
# testModuleData is always failing for architecture armv7hl
# Remove once Fedora 36 is EOL
%ifarch armv7hl
EXCLUDE='not testModuleData'
%endif

%if ( 0%{?rhel} && 0%{?rhel} <= 7 )
export CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"
export PATH="%{buildroot}%{_bindir}:$PATH"
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_XDIST_AUTO_NUM_WORKERS=%{_smp_build_ncpus}}
pytest-3 -k "$EXCLUDE" tests.py -v
%else
%pytest -k "$EXCLUDE" tests.py -v
%endif


#====================================================================
%files -n python%{python3_pkgversion}-yara -f %{pyproject_files}
%license LICENSE
%doc README.rst

%if 0%{?with_python2}  > 0
%files -n python2-yara
%license LICENSE
%doc README.rst
%{python2_sitearch}/yara*
%endif

#====================================================================
%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.5.1-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Michal Ambroz <rebus _AT seznam.cz> - 4.5.1-1
- bump to 4.5.1

* Wed Feb 14 2024 Michal Ambroz <rebus _AT seznam.cz> - 4.5.0-1
- bump to 4.5.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 17 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4.4.0-1
- bump to 4.4.0

* Fri Aug 25 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4.3.1-4
- Fix rhbz#2226378 rhbz#2220571

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.12

* Wed Apr 26 2023 Michal Ambroz <rebus _AT seznam.cz> - 4.3.1-1
- bump to 4.3.1

* Thu Mar 30 2023 Michal Ambroz <rebus _AT seznam.cz> - 4.3.0-1
- bump to 4.3.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Michal Ambroz <rebus _AT seznam.cz> - 4.2.3-1
- Rebuilt for yara-4.2.3 - second service :)

* Tue Aug 09 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4.2.0-5
- Rebuilt for yara-4.2.3

* Mon Aug 08 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4.2.0-4
- Skip testModuleData again for F36, fixes rhbz#2116289

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.2.0-2
- Rebuilt for Python 3.11

* Fri May 27 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4.2.0-1
- Bump to 4.2.0 rhbz#2063287 fixes FTBFS rhbz#2064646
- Minor changes to spec, like using https for URL
- Simplify some of checks for different builds

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.1.3-2
- rebuild due to koji hickup

* Wed Nov 10 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.1.3-1
- bump the python-yara as well to 4.1.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.1.0-1
- bump the python-yara as well to 4.1.0

* Tue Apr 27 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.0.5-3
- rebuild for new version of yara 4.1.0

* Sun Apr 25 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.0.5-2
- rebuild for epel

* Sat Mar 13 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.0.5-1
- bump to version 4.0.5

* Wed Feb 10 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.0.4-1
- bump to version 4.0.4

* Thu Feb 04 2021 Michal Ambroz <rebus _AT seznam.cz> - 4.0.3-1
- bump to version 4.0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Michal Ambroz <rebus _AT seznam.cz> - 4.0.2-1
- bump to version 4.0.2

* Sat Jun 06 2020 Michal Ambroz <rebus _AT seznam.cz> - 4.0.1-1
- bump to version 4.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-2
- Rebuilt for Python 3.9

* Tue May 12 2020 Michal Ambroz <rebus _AT seznam.cz> - 4.0.0-1
- bump to version 4.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Michal Ambroz <rebus _AT seznam.cz> - 3.11.0-2
- fix the release number

* Mon Oct 14 2019 Michal Ambroz <rebus _AT seznam.cz> - 3.11.0-1
- bump to 3.11.0, omit py2 for f30+ and epel8+

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-2.2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Michal Ambroz <rebus _AT seznam.cz> - 3.9.0-2
- change dependency to sphinx based on the /usr/bin/sphinx-build

* Mon Mar 18 2019 Michal Ambroz <rebus _AT seznam.cz> - 3.9.0-1
- bump to 3.9.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.8.1-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 27 2018 Michal Ambroz <rebus _AT seznam.cz> - 3.8.1-2
- rebuild with yara 3.8.1 override

* Mon Aug 27 2018 Michal Ambroz <rebus _AT seznam.cz> - 3.8.1-1
- bump to 3.8.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-6
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Michal Ambroz <rebus _AT seznam.cz> - 3.7.0-5
- fix dependencies for building the epel7/epel6 packages

* Thu Mar 15 2018 Michal Ambroz <rebus _AT seznam.cz> - 3.7.0-4
- rebuild with yara 3.7.1 for supported platforms
- fix dependencies for building the epel packages

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.7.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Michal Ambroz <rebus _AT seznam.cz> - 3.7.0-1
- bump to yara 3.7.0 release version (#1511921)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Michal Ambroz <rebus _AT seznam.cz> - 3.6.3-2
- fix bogus dates in the changelog
- omit failing testCompileFile test for s390/ppc64

* Mon Jul 17 2017 Michal Ambroz <rebus _AT seznam.cz> - 3.6.3-1
- bump to upstream 3.6.3 release version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.5.0-9
- Rebuild for Python 3.6

* Wed Nov 23 2016 Dan Horák <dan[at]danny.cz> - 3.5.0-8
- fix the arch lists

* Tue Aug 16 2016 Michal Ambroz <rebus _AT seznam.cz> - 3.5.0-7
- adding test exclusions also for armv7hl and ppc64le

* Tue Aug 16 2016 Michal Ambroz <rebus _AT seznam.cz> - 3.5.0-6
- additionally testEntrypoint testIn testIntegerFunctions failing on s390/ppc64
- exclude those tests for build of s390/ppc64

* Tue Aug 16 2016 Michal Ambroz <rebus _AT seznam.cz> - 3.5.0-5
- testModuleData is failing on arm platform even for python 2.7
- exclude this test for build of arm

* Fri Aug 12 2016 Michal Ambroz <rebus _AT seznam.cz> - 3.5.0-4
- remove unnecessary ldconfig
- count with the python3 test values except the 2 known for failing

* Thu Aug 11 2016 Michal Ambroz <rebus _AT seznam.cz> - 3.5.0-3
- change python3 naming to allow epel7 python34 packages

* Thu Aug 04 2016 Michal Ambroz <rebus _AT seznam.cz> - 3.5.0-2
- cosmetics

* Thu Aug 04 2016 Michal Ambroz <rebus _AT seznam.cz> - 3.5.0-1
- with yara 3.5.0 the python yara binding is separate library
