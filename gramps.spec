Name:           gramps
Version:        5.2.3
Release:        2%{?dist}
Summary:        Genealogical Research and Analysis Management Programming System

License: GPL-2.0-or-later
URL:            https://gramps-project.org/
Source0:        https://github.com/gramps-project/gramps/archive/v%{version}/gramps-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-gobject
BuildRequires:  intltool
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:  libappstream-glib

Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-gobject
Requires:       gtk3
Requires:       pango
Requires:       librsvg2
Requires:       xdg-utils
Requires:       rcs
Requires:	graphviz
Requires:	osm-gps-map-gobject
Requires:       python%{python3_pkgversion}-pyicu
Requires:	gtkspell3
Requires:	libgexiv2
Requires:       python%{python3_pkgversion}-bsddb3

Requires:	gnu-free-serif-fonts
Requires:	gnu-free-mono-fonts
Requires:	gnu-free-fonts-common
Requires:	gnu-free-sans-fonts
Requires:	hicolor-icon-theme

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

# the script starts with -O, the macros add -sP.  execve(2) treats everything
# after the interpreter as a single argument, so the flags need to be combined
sed -i -e '1s| \+-||2g' ${RPM_BUILD_ROOT}%{_bindir}/gramps

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/locale
cp -pr build/mo/* ${RPM_BUILD_ROOT}%{_datadir}/locale/

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/mime/packages
cp -p build/data/org.gramps_project.Gramps.xml ${RPM_BUILD_ROOT}%{_datadir}/mime/packages/
mkdir -p ${RPM_BUILD_ROOT}%{_metainfodir}/
cp -p build/data/org.gramps_project.Gramps.metainfo.xml ${RPM_BUILD_ROOT}%{_metainfodir}/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
cp -p build/data/man/gramps.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/gramps.1.gz
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/doc/gramps/

echo -n %{_datadir} > $RPM_BUILD_ROOT%{python3_sitelib}/gramps/gen/utils/resource-path

# fix the app id to match flathub
appstream-util modify $RPM_BUILD_ROOT%{_metainfodir}/org.gramps_project.Gramps.metainfo.xml \
  id org.gramps_project.Gramps
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_metainfodir}/org.gramps_project.Gramps.metainfo.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/c.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/d.png 

%find_lang %{name}

desktop-file-install --delete-original  \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications   	\
  build/data/org.gramps_project.Gramps.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS COPYING FAQ NEWS TODO example/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.gramps_project.Gramps.desktop
%{_datadir}/mime/packages/org.gramps_project.Gramps.xml
%{_datadir}/icons/hicolor/*/apps/org.gramps_project.Gramps.*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_mandir}/man1/%{name}.1.gz
%{_metainfodir}/org.gramps_project.Gramps.metainfo.xml
%{python3_sitelib}/gramps*egg-info
%{python3_sitelib}/gramps/__init*
%{python3_sitelib}/gramps/__main*
%{python3_sitelib}/gramps/grampsapp*
%{python3_sitelib}/gramps/gui
%{python3_sitelib}/gramps/test
%{python3_sitelib}/gramps/version*
%{python3_sitelib}/gramps/__pycache__
%dir %{python3_sitelib}/gramps/
%{python3_sitelib}/gramps/cli
%{python3_sitelib}/gramps/gen
%{python3_sitelib}/gramps/plugins

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.2.3-1
- 5.2.3

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.2.2-2
- Rebuilt for Python 3.13

* Mon Apr 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.2.2-1
- 5.2.2

* Mon Mar 25 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.2.1-1
- 5.2.1

* Thu Mar 07 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.2.0-2
- Restore duplicate license file for use by GUI

* Fri Feb 23 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.2.0-1
- 5.2.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.1.6-2
- Python 3.12

* Thu Jun 29 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.1.6-1
- 5.1.6

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 5.1.5-6
- Rebuilt for Python 3.12

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.1.5-5
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.1.5-2
- Rebuilt for Python 3.11

* Sun Feb 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.1.5-1
- 5.1.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 5.1.4-2
- Fix icon handling.

* Tue Jul 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 5.1.4-1
- 5.1.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.3-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 5.1.3-1
- 5.1.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.1.2-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 5.1.2-1
- 5.1.2

* Mon Sep 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.1.1-1
- 5.1.1

* Thu Aug 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.1.0-1
- 5.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-2
- Rebuilt for Python 3.8

* Thu Aug 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.0.2-1
- 5.0.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.0.1-1
- 5.0.1

* Wed Jul 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.0.0-1
- 5.0.0
- Webapp dropped by upstream.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.8-2
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 4.2.8-1
- 4.2.8

* Thu Feb 08 2018 Gwyn Ciesla <limburgher@gmail.com> - 4.2.7-1
- 4.2.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Gwyn Ciesla <limburgher@gmail.com> - 4.2.6-2
- Fix python3-django Requires, spec cleanup.

* Tue Aug 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 4.2.6-1
- 4.2.6

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Jon Ciesla <limburgher@gmail.com> - 4.2.5-3
- Fix file/directory ownership issues, BZ 1413404.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.5-2
- Rebuild for Python 3.6

* Fri Dec 16 2016 Jon Ciesla <limburgher@gmail.com> - 4.2.5-1
- 4.2.5

* Mon Sep 05 2016 Jon Ciesla <limburgher@gmail.com> - 4.2.4-1
- 4.2.4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Jon Ciesla <limburgher@gmail.com> - 4.2.3-1
- 4.2.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Jon Ciesla <limburgher@gmail.com> - 4.2.2-1
- 4.2.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 26 2015 Jon Ciesla <limburgher@gmail.com> - 4.2.1-1
- 4.2.1

* Fri Sep 04 2015 Jon Ciesla <limburgher@gmail.com> - 4.2.0-1
- 4.2.0

* Mon Jul 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.1.3-3
- Fix F23FTBFS (RHBZ#1239545).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Jon Ciesla <limburgher@gmail.com> - 4.1.3-1
- 4.1.3

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 4.1.2-2
- Use better AppData screenshots

* Wed Mar 04 2015 Jon Ciesla <limburgher@gmail.com> - 4.1.2-1
- Upstream maintenance release.
- Include examples per Paul Franklin.

* Mon Nov 03 2014 Jon Ciesla <limburgher@gmail.com> - 4.1.1-1
- Upstream maintenance release.

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-4
- update/fix icon/mime scriptlets, deps

* Fri Sep 19 2014 Richard Hughes <richard@hughsie.com> 4.1.0-3
- Actually install the AppData file

* Wed Jul 16 2014 Bastien Nocera <bnocera@redhat.com> 4.1.0-2
- Update run-time dependencies for GTK+ 3.x
- Switch to Python 3

* Mon Jun 23 2014 Jiri Kastner <jkastner at redhat dot com> - 4.1.0-1
- update to 4.1.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Jon Ciesla <limburgher@gmail.com> - 4.0.3-1
- Upstream maintenance release.

* Wed Nov 13 2013 Jon Ciesla <limburgher@gmail.com> - 4.0.2-1
- Latest upstream, BZ 1029930.
- 6807 patch upstreamed.

* Fri Aug 23 2013 Jon Ciesla <limburgher@gmail.com> - 4.0.1-6
- Migrate from python-osmgpsmap to osm-gps-map-gobject
- and pygobject3, BZ 1000058.

* Tue Aug 20 2013 Jon Ciesla <limburgher@gmail.com> - 4.0.1-5
- Change webapp Requires to python-django14.

* Tue Aug 13 2013 Jon Ciesla <limburgher@gmail.com> - 4.0.1-4
- Ship webapp as subpackage, BZ 983418.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Jon Ciesla <limburgher@gmail.com> - 4.0.1-1
- Add gtkspell3 dependency, BZ 983064
- Add libgexiv2-python2 dependency, BZ 983071
- Patch for AttributeError, BZ 982250.

* Mon Jul 08 2013 Jon Ciesla <limburgher@gmail.com> - 4.0.1-1
- 4.0.1.

* Thu May 30 2013 Jon Ciesla <limburgher@gmail.com> - 4.0.0-1
- 4.0.0.

* Thu May 30 2013 Jon Ciesla <limburgher@gmail.com> - 3.4.5-2
- Add Requires for pyicu.

* Thu May 30 2013 Jon Ciesla <limburgher@gmail.com> - 3.4.5-1
- The .We have also developed a tomato which can eject itself when
- an accident is imminent., a maintenance and bug fix release.
- The important change:
-  Problem after upgrading to 3.4.4 from 3.3.1
-
- Other changes are on reports:
-
-  Ability to keep custom filename on output
-  Book report: Sub reports forget/overwrite their settings when
-  trying to re-configure them
-  End of Line Report options window . changing Output Format cause
-  change active tab to .report options.
-  Various updated translations: de, es, fr, nb, nl, pl, sk

* Tue Mar 26 2013 Jon Ciesla <limburgher@gmail.com> - 3.4.3-1
- Version 3.4.3 has been released, the ““Whenever life gets you down, Mrs.
- Brown”“, a maintenance (“bug fix”) release.
- * Sorting of names, places etc. uses the International Components for
- * Unicode (ICU) libraries which resolves many bugs particularly on MS
- * Windows, and ensures that sorting is the same for all platforms.
- * Addon checking and download works again.
- * A large number of fixes to Narrative Web. In particular, media objects attached to events and sources are now output.
- * Many other bug fixes.
- * Various updated translations: da, de, es, fr, it, nb, nl, pt_BR, pt_PT, sv, uk.

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 3.4.2-3
- Drop desktop vendor tag.

* Sun Nov 18 2012 Robert Scheck <robert@fedoraproject.org> - 3.4.2-2
- Version 3.4.2 -- The "We're all individuals!" bug fix release.
- * Some fixes on NarrativeWeb and book reports
- * Improvement on database path interface and user's preferences
- * Consistency on Name display and regex support
- * Some platform-specific fixes for Windows system environment
- * Better support for media links on Gedcom file format
- * Fix possible incorrect family relations on Gedcom file format
- * Various fixes on citation records
- * Fix and improve places handling on Geography views
- * Fix on command line arguments
- * Consistency on PDF file format
- * New language: Greek
- * Various updated translations
- Corrected bogus historical date information in %%changelog entries

* Mon Sep 03 2012 Robert Scheck <robert@fedoraproject.org> - 3.4.1-1
- Version 3.4.1 -- The "A tiger? In Africa?!" bug fix release.
- * Error in export to xml of family order in 3.4.0, now fixed
- * Bug fixes
- * Translation updates

* Sat Aug 04 2012 Jon Ciesla <limburgher@gmail.com> - 3.4.0-1
- Version 3.4.0 -- The "always look on the bright side of life" feature release.
- * Lots of changes and bug fixes to every part of Gramps, including XML
-   import/export, image handling, gedom handling, Gramplets, date handling,
-   citations, reports, more!
- * Some platform-specific fixes (Windows, OSX, Linux)
- * What's new (and what to do before you upgrade):  http://goo.gl/K3RDV
- * Roadmap:  http://goo.gl/GJhjH
- * Many translation updates

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Jeffrey Ollie <jeff@ocjtech.us> - 3.3.2-1
- Version 3.3.2 -- "The Knights who say 'Ni'" bug fix release.
- * Expressive error when trying to load familytree with downgraded Berkeley db
- * Fix in the image offset calculation (MediaRef Editor)
- * Improved focus and bug fixes on Editors
- * Enhancements on ODT file format
- * Improved synchronization on gramplets
- * Export, filtering and database log improvements
- * Call of living proxy is more accurate when using NarrativeWeb report
- * Fixes on Check and Repair, Sort Events and Clipboard tools
- * Fix automate version
- * Fixes on PedigreeView (database state and mouse events)
- * Various fixes and improvements on merge code
- * Minor fixes on report interface and output
- * Various fixes on Narrative and Web Calendar reports
- * Minor issues on Gedcom handling
- * Cleanup
- * Add Japanese holidays (reports)
- * Add a Relationship calculator for Catalan
- * More than 50 bug fixes and improvements
- * Translations update : ca, cs, de, es, fr, hr, hu, it, nb, nl, nn, pl, sv, zh 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct  3 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.3.1-1
- Version 3.3.1 -- "The Tenth Anniversary Edition" bug fix release.
-
-     translation updates:  ca, cs, de, fr, hr, it, nb, nl, pl, pt_br, sk, sl, sv, uk, zh_cn
-     new languages in this release:  ja (Japanese), vi (Vietnamese)
-     36 bugs closed since v3.3.0:  http://www.gramps-project.org/bugs/roadmap_page.php?version_id=27
-     79 translation commits since v3.3.0
-     189 code commits since v3.3.0
-     ten years since v0.1.1 was first released:  http://www.gramps-project.org/wiki/index.php?title=Previous_releases
-     "Thank you!" to Donald Allingham, The Gramps Developers, translators, and our every day users

* Fri Sep  9 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.3.0-1
- Update to 3.3.0
- Drop conditionals for building on old versions of Fedora
-
- Version 3.3.0 -- the "Prelude to the next version" new feature
- release.  Note this version contains many new features, including:
-
- * many translation updates: Chinese, Croatian, Czech, Dutch, French,
-   German, Italian, Irish, Norwegian, Polish, Portuguese, Russian,
-   Serbian, Slovenian, Swedish, Ukrainian, and more!
- * new "person name" dialog and workflow with better (or new!) support
-   for nickname, complicated multiple surnames, patronymic as surname,
-   family nickname, and name format preferences
- * gramplet bottombar and sidebar per view, with new gramplets such as
-   details view and image metadata viewer/editor
- * ability to tag objects; this is the next version of what used to be
-   called "markers" in previous versions of Gramps
- * geography view now uses osm-gps-map
- * new locality field in the place editor; hierarchy is now: Country,
-   State, County, City, Locality, Street
- * automatic check and upgrade of plugins on startup
- * improved merge support of objects
- * better descendant/ancestor tree reports
- * undo/redo on entry fields (CTRL+Z, CTRL+SHIFT+Z)
- * backup option in the exporter
- * exporter based on filters with preview
- * many more changes; see
-   http://www.gramps-project.org/wiki/index.php?title=Gramps_3.3_Wiki_Manual_-_What%27s_new%3F

* Mon May  2 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.6-1
- Version 3.2.6 -- the "So far, so good." bug fix release.
- * fix memory leaks
- * fix corrupted reports
- * fix crash in cramplets
- * fix gedcom import and export
- * import speed improvements
- * NarrativeWeb fixes
- * prevent corrupting databases
- * many translation updates
- * other changes; see the changelog and the 3.2.6 roadmap: http://www.gramps-project.org/bugs/roadmap_page.php?version_id=23

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.5-2
- Removed dependencies on ImageMagik and python-reportlab
- Added dependency on python-enchant

* Thu Nov 18 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.5-1
- Version 3.2.5 -- the "I intend to live forever" bug fix release.
-
- Highlights of fixes in this release include:
-
- * fix Gramps so it again runs with Python 2.5
- * write all notes and sources to gedcom files
- * cli fixes
- * GeneWeb and LegacyGedcom fixes
- * NarrativeWeb fixes
- * memory leak fixes
- * various other small fixes
- * many translation updates

* Tue Oct 12 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.4-2
- Due to a missing .css file, we've chosen to re-release Gramps 3.2.4.
- This will only affect those who use NarrativeWeb.

* Sun Oct 10 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.4-1
- Version 3.2.4 -- the "Tententen" bug fix release.
- * fix a crash on newer distro's after an export is finished
- * styled notes cleanup and consistency improvement (nar web behaves
-   like the pdf/html output of reports)
- * newlines in styled notes are written as newlines so users can make
-   simple lists
- * many NarrativeWeb fixes
- * gedcom output fixes
- * non latin character fixes (mainly for windows)
- * recursive filter fixes
- * undo fixes
- * many translation updates
-
- Thanks to all who participated.  Looking at the Changelog file, I see
- 120+ code/translation commits and another 35+ commits just for
- translation updates.
-
- There were 17 distinct people who committed code.  (My scripts don't
- take into account checkins made on behalf of people without write
- access to svn, sorry!)  Thanks to everyone, but I personally want to
- highlight the numerous contributions -- in alphabetical order -- by
- Benny Malengier, Doug Blank, Espen Berg, Jérôme Rapinat, Mirko
- Leonhäuser, Nick Hall, Peter Landgren, Rob Healey, and Serge Noiraud.

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 3.2.3-3
- recompiling .py files against Python 2.7 (rhbz#623313)

* Wed Aug 11 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.3-2
- Rebuild for Python 2.7

* Mon May 17 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.3-1%{?dist}
- Version 3.2.3 -- the "I used to eat there. Really good noodles." release.
- * Bug fixes:
- -> several GLADE fixes
- -> several GEDCOM fixes (both export and import)
- -> several crash fixes
- -> encoding fix (Windows only)
- -> privacy/living fixes
- -> updates to NarrativeWeb and the css stylsheets
- * Translation updates: bg, ca, de, es, fr, he, nb, nl, pl, sk, sv

* Sun Apr 25 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.2-1
- Version 3.2.2 -- the "Mea navis aëricumbens anguillis abundat" release.
- * This release is a quick fix to a problem introduced by NarrativeWeb
- in the previous release.
- * Also includes a few small fixes and translation updates to hr and it.
- * See the release notes from the 3.2.1 release for the full list of
- changes and translation updates.

* Thu Apr 22 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.1-1
- Version 3.2.1 -- the "One of those men is my father" release.
- * Many bug fixes:
- -> fixed missing icons
- -> load/reload plugins must unload old plugins
- -> import/export fixes (date ranges, underscore, latitude/longitude)
- -> narrative web crash fixes and many updates, html notes, css updates
- -> geoview fixes and updates
- -> unicode error in soundex
- -> fixed crash on data entry
- * Translation updates: bg, ca, de, es, fr, he, hr, it, nb, nl, sk, sv

* Sat Apr  3 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.0-1
- Update to final release

* Fri Mar 12 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.2.0-0.1.beta2
- Update to 3.2.0 beta 2

* Wed Dec  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.1.3-1
- Update to 3.1.3

* Fri Aug 21 2009 Warren Togami <wtogami@redhat.com> - 3.1.2-1
- 3.1.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Warren Togami <wtogami@redhat.com> - 3.1.1-3
- frefont -> gnu-free* automatic detected for Fedora 11+
  Turns out gramps used them during PDF chart generation.

* Tue Mar 24 2009 Warren Togami <wtogami@redhat.com> - 3.1.1-2
- freefont was split into multiple packages gnu-free-*, however it seems that 
  gramps works fine without any of them?  Remove freefont req to fix broken
  dep for now.

* Tue Mar 10 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.1.1-1
- Version 3.1.1 -- the "Spam, bacon, sausage and spam" release:
- * The release of 3.1.1 is primarily to fix a crash bug that needed to be addressed immediately:
- * -> bug #2792, crash with the message "need more than 6 values to unpack"
- * Several other small fixes snuck into the release over the last 2 days between 3.1.0 and 3.1.1:
- * -> add a warning when installing from .tar.gz
- * -> bug #2121 - graphviz reports were generated off-page
- * -> various gramplet fixes
- * -> several text typo fixes and translation updates (de, fr)
- * -> bug #2772 - name display format
- * -> bug #2789 - fix for HTTP 404 in NarrativeWeb due to bad relative path

* Sat Mar  7 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.1.0-1
- Update to 3.1.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.4-1
- Update to 3.0.4

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.3-1
- Rebuild for Python 2.6

* Thu Nov 20 2008 Russell Harrison <rharrison@fedoraproject.org> - 3.0.3-0
- Update to 3.0.3.
- Changed build arguments to "--enable-packager-mode" from "--disable-schemas-install --disable-scrollkeeper --disable-mime-install".
- Removed scrollkeeper commands and dependencies.
- Removed GCONF schema commands as schema files are no longer created by the build. pre and preun sections are no longer needed.
- Help files are now stored on the gramps wiki instead of created durring the build.
- Changed gnome-python2 dependency to gnome-python2-gnome for F10 and above per bug #460006
- Included a patch to allow gramps to work with BerkeleyDB 4.7 in F10

* Mon Jan 14 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.2.10-1
- Update to 2.2.10.

* Sun Oct 28 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.9-1
- Update to 2.2.9.
- Update gtk icon scriptlet.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.8-5
- Update license tag.

* Sun Jun 10 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.8-4
- Drop requires on yelp.

* Sat Jun  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.8-3
- Remove depreciated desktop file categories, and add category on gtk.

* Sat Jun  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.8-2
- Add requires on yelp. (#243399)

* Mon May 28 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.8-1
- Update to 2.2.8.

* Fri May 18 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.7-1
- Update to 2.2.7.

* Mon Jan 29 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.6-1
- Update to 2.2.6.

* Sun Jan 28 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.2.5-1
- Update to 2.2.5.

* Wed Dec 27 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.2.4-3
- Add requires on gnome-python2-gtkspell & freefont.

* Tue Dec 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.2.4-2
- Add gramp.png to files.

* Tue Dec 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.2.4-1
- Update to 2.2.4.

* Fri Dec  8 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.2.3-2
- Rebuild against new python.

* Mon Nov 27 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3.
- Add scalable mimetype icons to files section.

* Sat Nov  4 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2.
- Add scriptlet for gtk+ icon cache.
- Disable scrollkeeper & mime-install in configure.
- Simplify files since we are no longer ghosting *.pyo files.
- Drop X-Fedora desktop category.
- Add BR on gnome-doc-utils.

* Wed Sep  6 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0.11-5
- Don't ghost *.pyo files.

* Sat Sep  2 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0.11-4
- Rebuild for FC6.
- Remove requires on python, it's no longer needed.
- Use --disable-schemas-install to config.
- Add BR for perl(XML::Parser).

* Mon May  1 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.11-3
- Update to 2.0.11.
- Drop INSTALL, README & ChangeLog documentation.
- Ghost .pyo files.

* Sat Mar 11 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.10-3
- Remove Utility category from desktop file.
- Update scriptlets.

* Tue Feb 28 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.10-2
- Update to 2.0.10.

* Thu Feb 16 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.9-6
- Remove unnecessary BR (gnome-python2-gnomevfs, pygtk2, gnome-python2, GConf2). 

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.9-5
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sat Jan 28 2006 Brian Pepple <bdpepple@ameritech.net> - 2.0.9-4
- Add require for shared-mime-info.
- Remove mime.cache.
- Use python-abi.

* Wed Dec 14 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.9-3
- Add requires for gnome-python2-gnomeprint.

* Tue Dec 13 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.9-2
- Make noarch. (#170974)
- Update to 2.0.9.

* Wed Sep  7 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.8-2
- Update to 2.0.8.

* Wed Aug 17 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.6-3
- Specify ver for python-reportlab.

* Mon Aug 15 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.6-2
- Update to 2.0.6.
- Bump minimum ver for python.
- Add requires for python-reportlab & graphviz for reports.

* Wed Jul  6 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.5-1
- Update to 2.0.5.

* Wed Jun 29 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.4-1
- Update to 2.0.4.

* Sat Jun 18 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.3-1
- Update to 2.0.3.
- Add dist tag.

* Sat May 21 2005 Brian Pepple <bdpepple@ameritech.net> - 2.0.0-1
- Update to 2.0.0.
- Add mime info.
- Use more macros.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Feb 06 2005 Phillip Compton <pcompton[AT]proteinmedia.com - 1.0.10-1
- 1.0.10.

* Sun Nov 28 2004 Phillip Compton <pcompton[AT]proteinmedia.com - 1.0.8-3
- Version bump.

* Sat Nov 13 2004 Phillip Compton <pcompton[AT]proteinmedia.com - 1.0.8-0.fdr.2
- Spec cleanup.

* Sat Nov 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com - 1.0.8-0.fdr.1
- 1.0.8.

* Wed Aug 18 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.7-0.fdr.1
- Update to 1.0.7.

* Sat Jul 31 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.5-0.fdr.1
- Update to 1.0.5.

* Wed Jul 21 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.4-0.fdr.1
- Update to 1.0.4.

* Thu Apr 22 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.3-0.fdr.1
- Update to 1.0.3.

* Tue Apr 20 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2-0.fdr.2
- Dropped unneccessary BuildReqs.
- Removed Requires(foo,bar) notation.

* Tue Apr 13 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.2-0.fdr.1
- Update to 1.0.2.
- Using upstream desktop entry.

* Sat Feb 28 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.0.1.0-0.fdr.1
- Update to 1.0.1.

* Mon Jan 12 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.98.0-0.fdr.1
- Update to 0.98.0.

* Sat Nov 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.95-0.fdr.5
- dropped smp_mflags.

* Fri Nov 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.95-0.fdr.4
- Req gnome-python2.

* Mon Nov 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.95-0.fdr.3
- BuildReq gnome-python2.

* Mon Nov 10 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.95-0.fdr.2
- Modifications to desktop entry.
- Reqs ImageMagick and rcs.

* Fri Oct 10 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.95-0.fdr.1
- Initial RPM release.
