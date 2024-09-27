Name:           transifex-client
Version:        0.13.7
Release:        17%{?dist}
Summary:        Command line tool for Transifex translation management
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://transifex.org
Source:         %pypi_source
BuildArch:      noarch

BuildRequires: git
BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python3-six            
BuildRequires: python3-slugify            
BuildRequires: python3-urllib3
BuildRequires: python3-requests
BuildRequires: python3-pip
BuildRequires: python3-mock
BuildRequires: python3-requests
BuildRequires: python3-rpm-generators

Requires: python3-rpm-macros
Requires: python3-slugify
Requires: python3-requests
Requires: python3-six

# https://bugzilla.redhat.com/show_bug.cgi?id=1799082
Patch1: 0001-Remove-versioning.patch

%description
The Transifex Command-line Client is a command line tool that enables
you to easily manage your translations within a project without the
need of an elaborate UI system.

%prep
%autosetup -p1 -S git

%build
%py3_build

%install
%py3_install

%check            
%{__python3} setup.py test

%files
%doc LICENSE README.md
%{python3_sitelib}/*
%{_bindir}/*

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.13.7-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.13.7-15
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.13.7-12
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13.7-9
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13.7-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.7-3
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Bastien Nocera <bnocera@redhat.com> - 0.13.7-2
+ transifex-client-0.13.7-2
- Fix uninstallable package in Fedora 32 (#1799082)

* Tue Jan 28 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.13.7-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.6-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.13.6-2
- Fix requirements

* Wed Feb 13 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.13.6-1
- New upstream version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Tim Landscheidt <tim@tim-landscheidt.de> - 0.13.5-5
- Loosen requirements for python3-slugify and python3-urllib3 in
  requirements.txt (#1653103, #1654677).
- Add pinned version requirements from requirements.txt to
  BuildRequires/Requires.
- Add BuildRequires for python3-mock, python3-six, python3-slugify and
  python3-urllib3.
- Add Requires for python3-requests (#1653103).
- Add %check section.

* Thu Nov 22 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.5-4
- urllib3 1.2.4

* Thu Nov 22 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.5-3
- add Buildrequres

* Thu Nov 22 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.5-2
- add Buildrequres

* Wed Oct 17 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.5-1
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.4-1
- New upstream version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.3-5
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.3-4
- Fix dependency backports ssl create BZ #1592062

* Sat Jun 16 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.3-3
- Fix dependency backports ssl

* Tue May 29 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.3-2
- Update Python 3 dependency
- Fix Python 3 syntax

* Fri May 18 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.13.3-1
- New upstream version

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Nick Bebout <nb@fedoraproject.org> - 0.10-2
- Add patch to fix resource creation

* Wed Jan 15 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.10-1
- New Upstream version

* Mon Dec 02 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9.1-1
- New Upstream version

* Thu Oct 24 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9-7
- change python-backports-ssl to python-backports-ssl_match_hostname

* Thu Oct 24 2013 Eduardo Echeverria <echevemaster@gmail.com> - 0.9-6
- Use system wide python-backports-ssl

* Wed Oct 09 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9-5
- Fix BZ #1002546

* Mon Aug 26 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9-4
- remove dependency

* Thu Aug 15 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9-3
- add new dependency

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.9-1
- New Upstream Version

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 09 2012 Domingo Becker <domingobecker@gmail.com> - 0.7.3-1
- Update to new upstream version.

* Sat Feb 25 2012 Domingo Becker <domingobecker@gmail.com> - 0.7.2-1
- Update to new upstream version.

* Thu Feb 16 2012 Domingo Becker <domingobecker@gmail.com> - 0.7-1
- Update to new upstream version.

* Tue Jan 10 2012 Domingo Becker <domingobecker@gmail.com> - 0.6.1-1
- Update to new upstream version.

* Tue Dec 20 2011 Domingo Becker <domingobecker@gmail.com> - 0.6-1
- Update to new upstream version.

* Fri Jun 24 2011 Domingo Becker <domingobecker@gmail.com> - 0.5.2-1
- Update to new upstream version.

* Wed May 18 2011 Domingo Becker <domingobecker@gmail.com> - 0.5-1
- New upstream version.

* Mon Feb 21 2011 Paul W. Frields <stickster@gmail.com> - 0.4.2-0.3.226a185088efhg
- Add BR for python-setuptools

* Sat Feb 19 2011 Domingo Becker <domingobecker@gmail.com> - 0.4.2-0.2.226a185088efhg
- fixed some rpmlint warnings

* Thu Feb 17 2011 Paul W. Frields <stickster@gmail.com> - 0.4.2-0.1.226a185088efhg
- Initial packaging

