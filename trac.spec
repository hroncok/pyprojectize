Name:           trac
Version:        1.6
Release:        4%{?dist}
Summary:        Enhanced wiki and issue tracking system
License:        BSD-3-Clause
URL:            http://trac.edgewall.com/
Source0:        http://ftp.edgewall.com/pub/trac/Trac-%{version}.tar.gz
Source2:        trac.ini
Source3:        trac.ini-environment_sample
Source4:        %{name}-README.fedora
Source5:        trac.wsgi

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-jinja2
BuildRequires:  python3-markupsafe
BuildRequires:  make

# optional packages to ensure we run all Trac tests (if one of these are not
# installed the test would be skipped)
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  python3-textile
BuildRequires:  python3-subversion
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/svnadmin
# No geckodriver in Fedora, hence we skip the selenium tests
#  BuildRequires:  python3-selenium
#  BuildRequires:  /usr/bin/geckodriver
# No tidylib in Fedora either
#  BuildRequires:  python3-tidylib

%description
Trac is an integrated system for managing software projects, an
enhanced wiki, a flexible web-based issue tracker, and an interface to
the Subversion revision control system.  At the core of Trac lies an
integrated wiki and issue/bug database. Using wiki markup, all objects
managed by Trac can directly link to other issues/bug reports, code
changesets, documentation and files.  Around the core lies other
modules, providing additional features and tools to make software
development more streamlined and effective.

%prep
%setup -q -n Trac-%{version}

find contrib -type f -exec chmod -x '{}' \;
# don't package windows specific files
rm -f contrib/trac-post-commit-hook.cmd
cp -a %{SOURCE4} README.fedora


%build
%py3_build

%install
%py3_install

install -dm 755 $RPM_BUILD_ROOT%{_var}/www/cgi-bin

install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/trac/trac.ini
install -Dpm 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/trac/trac.ini-environment_sample
install -dpm 755 $RPM_BUILD_ROOT/etc/trac/{plugin,template}s.d

find sample-plugins/ -type f -name '*.py' -exec install -pm 644 '{}' $RPM_BUILD_ROOT/etc/trac/plugins.d \;

find sample-plugins/ -type f -name '*.ini*' -exec install -pm 644 '{}' $RPM_BUILD_ROOT/etc/trac/ \;

install -dm 755 $RPM_BUILD_ROOT%{_sbindir}
mv $RPM_BUILD_ROOT{%{_bindir}/tracd,%{_sbindir}/tracd}

#%%check
#PYTHONPATH=$(pwd) PYTHON=/usr/bin/python3 make test

%files
%license COPYING
%doc AUTHORS ChangeLog INSTALL* README* RELEASE* THANKS UPGRADE* contrib/
%{_bindir}/trac-admin
%{_sbindir}/tracd
%{python3_sitelib}/[Tt]rac*/
%dir /etc/trac
%config(noreplace) /etc/trac/*

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.6-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.6-1
- 1.6

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.5.4-3
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.4-2
- migrated to SPDX license

* Mon Feb 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.4-1
- 1.5.4

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.5.3-8
- Patch for soft_unicode->soft_str

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.3-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.5.3-4
- Use markupsafe.soft_unicode.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.3-2
- Rebuilt for Python 3.10

* Mon May 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.5.3-1
- 1.5.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-1
- Update to 1.5.2
- Switch to Python 3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-1
- 1.5.1.

* Wed Feb 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4-1
- 1.4
- Drop test dependencies to clean Python 2 requirements.

* Mon Jul 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.2.4-1
- 1.2.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.3-1
- 1.2.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.2-4
- use Python 2-specific macros to fix build in rawhide ("F29")

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-3
- Escape macros in %%changelog

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Sep 11 2017 Jon Ciesla <limburgher@gmail.com> - 1.2.2-1
- 1.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Jon Ciesla <limburgher@gmail.com> - 1.2-1
- 1.2

* Mon Sep 19 2016 Jon Ciesla <limburgher@gmail.com> - 1.0.13-1
- 1.0.13

* Tue Sep 06 2016 Jon Ciesla <limburgher@gmail.com> - 1.0.12-1
- 1.0.12

* Wed Apr 20 2016 Dave Johansen <davejohanesn@gmail.com> - 1.0.10-1
- Upstream update

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 03 2015 Jon Ciesla <limburgher@gmail.com> - 1.0.8-1
- 1.0.8
- Fix FTBFS, BZ 1240073.
- Patches upstreamed.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 13 2014 Felix Schwarz <fschwarz@fedoraproject.org> - 1.0.2-3
- add BuildRequires so most Trac tests are run during %%check
- add patch so git tests pass (upstream issue 11876)

* Sat Nov 08 2014 Felix Schwarz <fschwarz@fedoraproject.org> - 1.0.2-2
- add patch for upstream issue 11805

* Thu Oct 30 2014 Felix Schwarz <fschwarz@fedoraproject.org> - 1.0.2-1
- 1.0.2

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.1-6
- Replace python-setuptools-devel BR with python-setuptools

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Dan Horák <dan[at]danny.cz> - 1.0.1-4
- spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Luke Macken <lmacken@redhat.com> - 1.0.1-2
- Run the test suite

* Mon Feb 04 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.1-1
- 1.0.1, BZ 907068

* Wed Sep 12 2012 Jon Ciesla <limburgher@gmail.com> - 1.0-1
- 1.0, BZ 855519
- Pidfile patch upstreamed.

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Jon Ciesla <limburgher@gmail.com> - 0.12.3-3
- Drop httpd dep, BZ 232921.

* Fri May 04 2012 Jon Ciesla <limburgher@gmail.com> - 0.12.3-2
- Patch for pidfile open mode, BZ 818385.

* Thu Feb 09 2012 Jon Ciesla <limburgher@gmail.com> - 0.12.3-1
- Update to 0.12.3, BZ 788775.

* Mon Feb 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.12.2-8
- Only ship trac.wsgi in doc, updated README.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-6
- Rebuilt for glibc bug#747377

* Tue Jun 14 2011 Jon Ciesla <limb@jcomserv.net> - 0.12.2-5
- Added .wsgi file, BZ 701762.
- No longer ship mod_python trac.conf, deprecated.

* Sun Apr 03 2011 Jesse Keating <jkeating@redhat.com> - 0.12.2-1
- New upstream release mostly bugfixes
- http://trac.edgewall.org/browser//tags/trac-0.12.2/ChangeLog

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Jesse Keating <jkeating@redhat.com> - 0.12.1-3
- Update the trac-README.fedora content for global ini

* Fri Oct 15 2010 Jesse Keating <jkeating@redhat.com> - 0.12.1-2
- Fix README.fedora installation

* Tue Oct 12 2010 Jesse Keating <jkeating@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Mar 10 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 0.11.7-1
- New upstream release (including security fix)

* Sat Mar 06 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 0.11.6-3
- don't package Windows commit hook
- package now includes trac.test module

* Sun Jan 24 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 0.11.6-2
- add missing setuptools requirement
- removed python-sqlite requirement as Python 2.6 already contains a suitable
  module in the standard library
- removed dependencies on subversion and python-pygments as these are actually
  optional
- added README.fedora to explain which packages can be installed for 
  additional functionality

* Sat Dec 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 0.11.6-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Jesse Keating <jkeating@redhat.com> - 0.11.4-1
- New upstream release to fix bugs and minor enhancements.

* Tue Mar 31 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.11.3-4
- Fix unowned directory (#473989)

* Mon Mar 09 2009 Jesse Keating <jkeating@redhat.com> - 0.11.3-3
- Obsolete trac-webadmin, its now built in

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.3-1
- Trac 0.11.3 contains a number of bug fixes and minor enhancements.
- The following list contains only a few highlights:
- 
-  * Compatibility with Python 2.6 (#7876, #7458)
-  * PostgreSQL db backend improvement (#4987, #7600)
-  * Highlighting of search results is more robust (#7324, #7830)
-  * Unicode related fixes (#7672, #7959, #7845, #7935, #8024)
-  * Fixed Trac link rendering in ReST (#7712)
- 
- You can find a more detailed release note at:
- http://trac.edgewall.org/wiki/TracDev/ReleaseNotes/0.11

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.11.2.1-4
- Rebuild for Python 2.6

* Fri Nov 28 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.2.1-3
- Add dependency on python-pygments
- Rebuild for Python 2.6

* Tue Nov 18 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.2.1-2
- Upload new sources
- Add new files to CVS

* Tue Nov 18 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.11.2.1-0.1
- Update to 0.11.2.1

* Mon Jun 23 2008 Ryan B. Lynch <ryan.b.lynch@gmail.com> - 0.11-1
- Update to 0.11

* Sun Jun 22 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.5-1
- Update to 0.10.5

* Thu Jan  3 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.4-2
- Simplify files section so that it picks up the egg info files.

* Thu May  3 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.4-1
- Update to 0.10.4

* Mon Mar 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.3.1-2
- Switch requires back to python-sqlite

* Sat Mar 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.3.1-1
- Update to 0.10.3.1 to fix security bug

* Sun Jan  7 2007 Joost Soeterbroek <joost.soeterbroek@gmail.com> - 0.10.3-2
- change req: python-sqlite -> python-sqlite2

* Tue Jan  2 2007 Joost Soeterbroek <joost.soeterbroek@gmail.com> - 0.10.3
- upstream release 0.10.3 (#221162)

* Sat Dec  9 2006 Joost Soeterbroek <joost.soeterbroek@gmail.com> - 0.10.3
- rebuild for python 2.5, add python-devel to BR

* Tue Nov 28 2006 Joost Soeterbroek <joost.soeterbroek@gmail.com> - 0.10.2
- upstream release 0.10.2 (#217539)

* Sat Nov 11 2006 Joost Soeterbroek <joost.soeterbroek@gmail.com> - 0.10.1
- upstream release 0.10.1 (fixes CSRF vulnerability, bugzilla #215077)

* Thu Sep 28 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10
- upstream release 0.10 'Zengia'

* Wed Aug 30 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.6-3
- remove %%ghost for .pyo files; bugzilla #205439

* Wed Aug 30 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.6-2
- rebuild for Fedora Extras 6

* Thu Jul  6 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.6-1
- upstream release 0.9.6

* Tue Apr 18 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.5-1
- bug fix release 0.9.5

* Wed Feb 15 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.4-1
- 0.9.4
 * Deletion of reports has been fixed.
 * Various encoding issues with the timeline RSS feed have been fixed.
 * Fixed a memory leak when syncing with the repository.
 * Milestones in the roadmap are now ordered more intelligently.
 * Fixed bugs: 
   1064, 1150, 2006, 2253, 2324, 2330, 2408, 2430, 2431, 2459, 2544, 
   2459, 2481, 2485, 2536, 2544, 2553, 2580, 2583, 2606, 2613, 2621, 
   2664, 2666, 2680, 2706, 2707, 2735

* Mon Feb 13 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.3-5
- Rebuild for Fedora Extras 5

* Mon Jan 16 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.3-4
- updated trac.conf to allow for trac.*cgi 

* Mon Jan 16 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.3-3
- re-added tracd and trac.fcgi by user request.

* Tue Jan 10 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.3-2
- removed trac.fcgi (bugzilla #174546, comment #11)
- applied patch (bugzilla #174546, attachment id=123008)

* Mon Jan  9 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.3-1
- 0.9.3
- removed tracd (bugzilla #174546, comment #6)
- added trac.conf for httpd
- removed %%{python_sitelib}/trac/test.py
- removed comments

* Tue Dec  6 2005 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.2-2
- added /etc/init.d/tracd
- added /etc/sysconfig/tracd

* Tue Dec  6 2005 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.2-1
- 0.9.2
- fixes SQL Injection Vulnerability in ticket search module.
- fixes broken ticket email notifications.

* Sat Dec  3 2005 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9.1-1
- 0.9.1
- fixes SQL Injection Vulnerability

* Tue Nov 29 2005 Joost Soeterbroek <fedora@soeterbroek.com> - 0.9-1
- Rebuild for Fedora Extras

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9-1
- 0.9.

* Mon Jun 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.8.4-0.1
- 0.8.4.
- Move tracd to %%{_sbindir} and man page to section 8.

* Thu Jun 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.8.3-0.1
- 0.8.3.

* Wed Jun  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.8.2-0.1
- 0.8.2.

* Sun May 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.8.1-0.2
- Rebuild for FC4.

* Fri Apr  8 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.8.1-0.1
- First build.
