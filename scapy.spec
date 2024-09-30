Name:           scapy
Version:        2.5.0
Release:        9%{?dist}
Summary:        Interactive packet manipulation tool and network scanner

%global         gituser         secdev
%global         gitname         scapy
%global         commit          9473f77d8b548c8e478e52838bdd4c12f5d4f4ff
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

License:        GPL-2.0-only
URL:            https://scapy.net/
#was            http://www.secdev.org/projects/scapy/
VCS:            https://github.com/secdev/scapy
#               https://github.com/secdev/scapy/releases
#               https://bitbucket.org/secdev/scapy/pull-request/80
#               https://scapy.readthedocs.io/en/latest/introduction.html
Source0:        %{vcs}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%global         common_desc %{expand:
Scapy is a powerful interactive packet manipulation program built on top
of the Python interpreter. It can be used to forge or decode packets of
a wide number of protocols, send them over the wire, capture them, match
requests and replies, and much more.}


# By default build with python3 subpackage
%bcond_without     python3

# Build also the python2 package on releases up to fc31 and rhel8
%if (0%{?fedora} && 0%{?fedora} <= 31 ) || ( 0%{?rhel} && 0%{?rhel} <= 8 )
%bcond_without     python2
%else
%bcond_with        python2
%endif

# By default build the documentation only on Fedora due to cc-by-nc-sa license
%if 0%{?fedora}
%bcond_without     doc
%else
%bcond_with        doc
%endif




BuildArch:      noarch

BuildRequires:  make
BuildRequires:  sed

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with doc}
BuildRequires:  python2-tox
%endif
%endif

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with doc}
BuildRequires:  python%{python3_pkgversion}-tox
%endif
%endif

# Recommends only supported on fedora and rhel8+
%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
Recommends:     tcpdump
# Using database of manufactures /usr/share/wireshark/manuf
Recommends:     wireshark-cli
%endif

%description %{common_desc}

%if %{with python2}
%package -n python2-%{name}
Summary:        Interactive packet manipulation tool and network scanner


%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 ) 
Recommends:     python2-pyx
Recommends:     python2-matplotlib
Recommends:     ipython2
%endif

%description -n python2-%{name}
%{common_desc}

%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{name}
Summary:        Interactive packet manipulation tool and network scanner

Provides:       %{name} = %{version}-%{release}

%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 ) 
Recommends:     PyX
Recommends:     python%{python3_pkgversion}-matplotlib
Recommends:     ipython3
%endif

%description -n python%{python3_pkgversion}-%{name}
%{common_desc}
%endif

%if %{with doc}
%package doc
Summary:        Interactive packet manipulation tool and network scanner
License:        CC-BY-NC-SA-2.5

BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme

%description doc
%{common_desc}
%endif



%prep
%autosetup -p 1 -n %{name}-%{version}

# Remove shebang
# https://github.com/secdev/scapy/pull/2332
SHEBANGS=$(find ./scapy -name '*.py' -print | xargs grep -l -e '^#!.*env python')
for FILE in $SHEBANGS ; do
    sed -i.orig -e 1d "${FILE}"
    touch -r "${FILE}.orig" "${FILE}"
    rm "${FILE}.orig"
done



%generate_buildrequires
%pyproject_buildrequires



%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%pyproject_wheel
%endif

%if %{with doc}
make -C doc/scapy html BUILDDIR=_build_doc SPHINXBUILD=sphinx-build-%python3_version

rm -f doc/scapy/_build_doc/html/.buildinfo
rm -f doc/scapy/_build_doc/html/_static/_dummy
%endif



%install
install -dp -m0755 %{buildroot}%{_mandir}/man1
install -Dp -m0644 doc/scapy.1* %{buildroot}%{_mandir}/man1/

%if %{with python2}
%py2_install
rm -f %{buildroot}%{python2_sitelib}/*egg-info/requires.txt


# Rename the executables
mv -f %{buildroot}%{_bindir}/scapy   %{buildroot}%{_bindir}/scapy2

%if ! %{with python3}
# Link the default to the py2 version of executables if py3 not built
ln -s %{_bindir}/scapy2   %{buildroot}%{_bindir}/scapy
%endif
%endif

%if %{with python3}
%pyproject_install
rm -f %{buildroot}%{python3_sitelib}/*egg-info/requires.txt

# Rename the executables
mv -f %{buildroot}%{_bindir}/scapy   %{buildroot}%{_bindir}/scapy3

# Link the default to the python3 version of executables
ln -s %{_bindir}/scapy3   %{buildroot}%{_bindir}/scapy
%endif



# check
# TODO: Need to fix/remove slow/failed test
# cd test/
# ./run_tests_py2 || true
# ./run_tests_py3 || true



%if %{with python2}
%files -n python2-%{name}
%license LICENSE
%if ! %{with python3}
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%endif
%{_bindir}/scapy2
%{python2_sitelib}/scapy/
%{python2_sitelib}/scapy-*.egg-info
%exclude %{python2_sitelib}/test/
%endif



%if %{with python3}
%files -n python%{python3_pkgversion}-%{name}
%license LICENSE
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%{_bindir}/scapy3
%{python3_sitelib}/scapy/
%{python3_sitelib}/scapy-*.dist-info
%exclude %{python3_sitelib}/test/
%endif


%if %{with doc}
%files doc
%doc doc/scapy/_build_doc/html
%endif


%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.5.0-8
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.5.0-7
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.5.0-3
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Jonathan Wright <jonathan@almalinux.org> - 2.5.0-1
- Update to 2.5.0 rhbz#2156396

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.5-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.5-2
- Rebuilt for Python 3.10

* Tue Apr 20 2021 Michal Ambroz <rebus _AT seznam.cz> - 2.4.5-1
- bump to 2.4.5 release

* Fri Mar 12 2021 Michal Ambroz <rebus _AT seznam.cz> - 2.4.4-1
- bump to 2.4.4 release

* Thu Mar 11 2021 W. Michael Petullo <mike@flyn.org> - 2.4.3-8
- Patch to fix loading libc.a; see https://bugs.python.org/issue42580

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Michal Ambroz <rebus _AT seznam.cz> - 2.4.3-3
- remove colliding manpage from python2 package
- add license files
- add doc subpackage
- remove shebangs

* Sun Oct 06 2019 Michal Ambroz <rebus _AT seznam.cz> - 2.4.3-2
- change to recommended python build dependencies for EPEL7 - thanks Miro Hroncok

* Thu Sep 26 2019 Michal Ambroz <rebus _AT seznam.cz> - 2.4.3-1
- bump to 2.4.3 release
- change the python2 to conditional build to be able to keep one spec for all
- add Recommends for dependencies, except for EPEL7

* Fri Sep 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-8
- Subpackage python2-scapy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.7

* Mon Apr 30 2018 Michal Ambroz <rebus _AT seznam.cz> - 2.4.0-2
- disable the test for now - there is too many failing (network) tests

* Mon Apr 30 2018 Michal Ambroz <rebus _AT seznam.cz> - 2.4.0-1
- bump to 2.4.0 release

* Fri Mar 9 2018 Michal Ambroz <rebus _AT seznam.cz> - 2.4.0-0.rc5.1
- bump to upstream 2.4.0 release candidate 5
- enable separate python3 and python2 build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Michal Ambroz <rebus _AT seznam.cz> - 2.3.3-1
- bump to upstream 2.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Sven Lankes <athmane@fedoraproject.org> - 2.3.1-1
- update to latest upstream release (2.3.1)
- Update to 2.3.1
- Remove upstreamed patch
- Some spec fixes
- Thanks to Athmane Madjoudj for the patch

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.2.0-5
- Fix psdump()/pdfdump()

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Sven Lankes <sven@lank.es> - 2.2.0-1
- Update to Scapy 2.2.0
- Fixes rhbz #788659 - thanks to Thiébaud Weksteen

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 2.0.0.10-1
- Update to Scapy 2.0.0.10.

* Sun Dec 07 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 2.0.0.9-2
- Update for Scapy 2.0.0.9.

* Tue Jan 22 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-4
- Switch to using rm macro.

* Mon Jan 21 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-2
- Spec file cleanup.

* Fri Jan 18 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-1
- Initial packaging for Fedora.

