# Disable debuginfo since there are no binaries
%global debug_package %{nil}

%global enable_doc 1

%global nagios_bindir %{_libdir}/nagios/plugins
%global arc_spooldir %{_localstatedir}/spool/arc
%global pkg_spooldir %{arc_spooldir}/nagios
%global pkg_sysconfdir %{_sysconfdir}/arc/nagios

Name:		nordugrid-arc-nagios-plugins
Version:	2.0.1
Release:	5%{?dist}
Summary:	Nagios plugins for ARC

License:	Apache-2.0
URL:		https://www.nordugrid.org
Source0:	https://download.nordugrid.org/packages/%{name}/releases/%{version}/src/%{name}-%{version}.tar.gz

%if %{?fedora}%{!?fedora:0}
#		Don't add dependency on EPEL since it can use either
#		nordugrid-arc-client or nordugrid-arcN-client
Requires:	nordugrid-arc-client >= 1.0.0
%endif
Requires:	python%{python3_pkgversion}-cryptography
Requires:	python%{python3_pkgversion}-jinja2
Requires:	python%{python3_pkgversion}-ldap3
Requires:	nagios-common
Requires:	glue-schema >= 2.0.8
BuildRequires:	make
BuildRequires:	python%{python3_pkgversion}-devel
%if %{enable_doc}
BuildRequires:	/usr/bin/sphinx-build
%endif

%description
This package provides the Nagios plugins for testing ARC computing element.

%if %{enable_doc}
%package doc
Summary:	HTML documentation for the ARC Nagios plugins
BuildArch:	noarch

%description doc
HTML documentation for the ARC Nagios plugins.
%endif

%package egi
Summary:	EGI configuration and dependencies for the ARC Nagios plugins
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description egi
EGI configuration and dependencies for the ARC Nagios plugins.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{enable_doc}
make -C doc html
rm -f doc/_build/html/.buildinfo
%endif

%install
%pyproject_install
%pyproject_save_files -l arcnagios

install -m755 -d %{buildroot}%{pkg_spooldir}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%dir %{pkg_sysconfdir}
%dir %{pkg_sysconfdir}/20-dist.d
%config(noreplace) %{pkg_sysconfdir}/20-dist.ini
%config(noreplace) %{pkg_sysconfdir}/20-dist.d/default.xrsl.j2
%{nagios_bindir}/check_arcce_clean
%{nagios_bindir}/check_arcce_monitor
%{nagios_bindir}/check_arcce_submit
%{nagios_bindir}/check_aris
%{nagios_bindir}/check_egiis
%{nagios_bindir}/check_arcservice
%{nagios_bindir}/check_gridstorage
%dir %{arc_spooldir}
%attr(-,nagios,nagios) %{pkg_spooldir}
%doc AUTHORS README.rst
%doc doc/arcnagios.ini.example
%doc doc/services.cfg.example

%if %{enable_doc}
%files doc
%doc doc/_build/html
%license LICENSE NOTICE
%endif

%files egi
%dir %{pkg_sysconfdir}/60-egi.d
%config(noreplace) %{pkg_sysconfdir}/60-egi.ini
%config(noreplace) %{pkg_sysconfdir}/60-egi.d/arcce_igtf.py*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.1-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.0.1-1
- Version 2.0.1

* Wed Nov 01 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.0.1~rc1-1
- Version 2.0.1 rc1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.0.0-12
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.0.0-1
- Version 2.0.0

* Thu Oct 03 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.0.0~rc2-1
- Version 2.0.0 rc2
- This version uses python 3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.9.1-9
- Update sphinx BR

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.9.1-7
- Fix python shebangs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.9.1-1
- Updated to release 1.9.1.

* Wed May 31 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.9.0-1
- Updated to release 1.9.0.
- EPEL 5 End-Of-Life specfile clean-up

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.8.4-6
- Remove runtime requirement for python-argparse

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.8.4-3
- Make arcce_igtf.py non-executable

* Thu Oct 22 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.8.4-2
- Specfile clean-up for Fedora review submission

* Fri Sep 11 2015 Petter Urkedal <urkedal@nbi.dk> - 1.8.4-1
- Updated to release 1.8.4.

* Mon Jul 06 2015 Anders Waananen <waananen@nbi.dk> - 1.8.3-2
- Drop doc subpackage for el5 due to missing dependencies

* Thu Jul 02 2015 Petter Urkedal <urkedal@nbi.dk> - 1.8.3-1
- Updated to release 1.8.3.

* Fri Mar 27 2015 Petter Urkedal <urkedal@nbi.dk> - 1.8.2-1
- Updated to release 1.8.2.

* Thu Jan 15 2015 Petter Urkedal <urkedal@nbi.dk> - 1.8.2-0.rc2
- Updated to release candidate 1.8.2rc2.

* Fri Jan 09 2015 Petter Urkedal <urkedal@nbi.dk> - 1.8.2-0.rc1
- Updated to release candidate 1.8.2rc1.

* Fri Aug 15 2014 Anders Waananen <waananen@nbi.dk> - 1.8.1-1
- Updated to release 1.8.1.

* Fri Jun 27 2014 Petter Urkedal <urkedal@nbi.dk> - 1.8.1-0.rc1
- Updated to release candidate 1.8.1rc1.

* Wed Apr 30 2014 Petter Urkedal <urkedal@nbi.dk> - 1.8.0-1
- Updated to release 1.8.0.

* Tue Oct 22 2013 Petter Urkedal <urkedal@nbi.dk> - 1.7.1-1
- Updated to release 1.7.1.

* Fri Aug 16 2013 Petter Urkedal <urkedal@nbi.dk> - 1.7.0-1
- Updated to release 1.7.0.

* Fri Jul 05 2013 Petter Urkedal <urkedal@nbi.dk> - 1.6.1-0.rc1
- Updated to release candidate 1.6.1rc1.

* Fri Apr 19 2013 Petter Urkedal <urkedal@nbi.dk> - 1.6.0-1
- Updated to release 1.6.0.

* Sat Apr 06 2013 Petter Urkedal <urkedal@nbi.dk> - 1.6.0-0.rc1
- Updated to release candidate 1.6.0rc1.

* Mon Feb 18 2013 Petter Urkedal <urkedal@nbi.dk> - 1.5.0-1
- Updated to release 1.5.0.

* Fri Feb 01 2013 Petter Urkedal <urkedal@nbi.dk> - 1.5.0-0.rc3
- Updated to release candidate 1.5.0rc3.

* Mon Jan 28 2013 Petter Urkedal <urkedal@nbi.dk> - 1.5.0-0.rc2
- Updated to release candidate 1.5.0rc2.

* Fri Jan 11 2013 Petter Urkedal <urkedal@nbi.dk> - 1.5.0-0.rc1
- Updated to release candidate 1.5.0rc1.

* Thu Dec 20 2012 Petter Urkedal <urkedal@nbi.dk> - 1.4.0-0.rc4
- Updated to release candidate 1.4.0rc4.

* Tue Nov 27 2012 Petter Urkedal <urkedal@nbi.dk> - 1.4.0-0.rc1
- Updated to release candidate 1.4.0rc1.

* Mon Oct 29 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.11-1
- Updated to release 1.3.11.

* Wed Sep 26 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.10-1
- Updated to release 1.3.10.

* Fri Sep 07 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.9-1
- Updated to release 1.3.9.

* Mon Apr 23 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.8-1
- Updated to release 1.3.8.

* Tue Apr 03 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.7-1
- Updated to release 1.3.7.

* Mon Apr 02 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.6-1
- Updated to release 1.3.6.

* Thu Feb 02 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.5-1
- Updated to release 1.3.5.

* Thu Feb 02 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.4-1
- Updated to release 1.3.4.

* Thu Feb 02 2012 Petter Urkedal <urkedal@nbi.dk> - 1.3.3-1
- Updated to release 1.3.3.

* Wed Dec 21 2011 Petter Urkedal <urkedal@nbi.dk> - 1.3.2-1
- Updated to release 1.3.2.

* Mon Dec 19 2011 Petter Urkedal <urkedal@nbi.dk> - 1.3.1-1
- Updated to release 1.3.1.

* Thu Dec 08 2011 Petter Urkedal <urkedal@nbi.dk> - 1.3.0-1
- Updated to release 1.3.0.

* Wed Nov 23 2011 Petter Urkedal <urkedal@nbi.dk> - 1.2.0-1
- Updated to release 1.2.0.

* Mon Nov 14 2011 Petter Urkedal <urkedal@nbi.dk>
- Change README to README.rst.
- Add documentation subpackage.

* Fri Nov 04 2011 Petter Urkedal <urkedal@nbi.dk> - 1.1.0-1
- Updated to release 1.1.0.

* Thu Nov 03 2011 Petter Urkedal <urkedal@nbi.dk>
- Install default configuration file.

* Wed Oct 26 2011 Petter Urkedal <urkedal@nbi.dk> - 1.0.2-1
- Updated to release 1.0.2.

* Thu Oct 20 2011 Petter Urkedal <urkedal@nbi.dk> - 1.0.1-1
- Updated to release 1.0.1.

* Tue Oct 18 2011 Petter Urkedal <urkedal@nbi.dk>
- Add argparse and nordugrid-arc-python dependencies.
- Install README and LICENSE.

* Fri Oct 14 2011 Petter Urkedal <urkedal@nbi.dk> - 1.0-1
- Updated to release 1.0.
- Almost complete rewrite for the new probes.

* Fri Sep 30 2011 Anders Waananen <waananen@nbi.dk> - 0.9-1
- New package name and ownership

* Thu Jun 30 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.4-1
- Fix flags to stat

* Thu Nov 18 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.3-1
- Implement changes proposed by Emir

* Mon Oct 11 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2-1
- Remove Requires (per WLCG practice)

* Thu Sep 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-1
- Initial packaging
