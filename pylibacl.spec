Name:           pylibacl
Summary:        POSIX.1e ACLs library wrapper for Python
Version:        0.6.0
Release:        10%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pylibacl.k1024.org
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/downloads/%{name}-%{version}.tar.gz.asc
Source2:        https://k1024.org/files/key.asc

BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  python3-devel
BuildRequires:  gnupg2
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Python extension module for POSIX ACLs. It allows to query, list,
add and remove ACLs from files and directories.}

%description %_description

%package -n python3-%{name}
Summary: %{summary}

Provides:  py3libacl = %{version}-%{release}
Obsoletes: py3libacl < 0.5.4

%description -n python3-%{name} %_description

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# the module is just a C extension => need to add the installed destination to
# PYTHONPATH, otherwise it won't be found
export PYTHONPATH=%{buildroot}%{python3_sitearch}:$PYTHONPATH
# One test crashes on s390x: https://github.com/iustin/pylibacl/issues/20
python3 -m pytest tests -v \
%ifarch s390x
  -k 'not TestAclExtensions and not test_acl_init_copy_ext_invalid'
%endif

%files -n python3-%{name}
%{python3_sitearch}/posix1e.cpython-%{python3_version_nodots}*
%{python3_sitearch}/*egg-info
%license COPYING
%doc README.md NEWS


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.6.0-1
- Updated to 0.6.0
- Removed broken test exclusion on i686 and armv7hl - fixed upstream - https://github.com/iustin/pylibacl/issues/13
- Added new broken test excludion on s390x - https://github.com/iustin/pylibacl/issues/20

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.4-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.4-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.5.4-4
- Add BuildRequire python3-setuptools in addition to python3-devel
  (see https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.5.4-1
- Update to 0.5.4
- Add GPG signature verification
- Drop Python 2 subpackage - https://fedoraproject.org/wiki/Changes/F31_Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.2-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 02 2016 Yclept Nemo <pscjtwjdjtAhnbjm/dpn> - 0.5.2-1
- updated to 0.5.2
- phase out python-libacl (it's been a while...)
- run checks
- python3 subpackage
- remove outdated macros
- (original change date Mon Jan 12 2015)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.5.1-2
- fix wrong licence tag - starting from 0.4 it should be LGPLv2+ instead of GPLv2+

* Tue Jun 26 2012 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.5.1-1
- updated to 0.5.1
- fix bugs found with cpycheck (bug 800126)
- adjust minimal required Python version to 2.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 06 2010 Kevin Fenzi <kevin@tummy.com> - 0.5.0-1
- Update to 0.5.0
- Fix egg-info

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.2-5
- Rebuild for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.2-4
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.2-3
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.2-2
- added compatibility with Python Eggs forced in F9

* Mon Aug 27 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.2-1
- upgraded to 0.2.2

* Sun Aug 26 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.1-7
 - Updated License tag

* Wed Apr 25 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-6
 - added Provides/Obsoletes tags

* Sat Apr 21 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-5
 - removed redundant after name change "exclude" tag
 - comments cleanup

* Wed Apr 18 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-4
 - applied suggestions from Kevin Fenzi
 - name changed from python-libacl to pylibacl
 - corrected path to the source file

* Fri Apr 6 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-3
 - fixed path to a source package

* Thu Apr 5 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-2
 - added python-devel in BuildRequires
 - added Provides section
 - modified to Fedora Extras requirements

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
