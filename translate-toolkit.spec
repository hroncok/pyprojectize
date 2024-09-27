%global upstream_name translate_toolkit
Name:           translate-toolkit
Version:        3.13.3
Release:        1%{?dist}
Summary:        Tools to assist with translation and software localization
License:        GPL-2.0-or-later
URL:            http://toolkit.translatehouse.org/
Source0:        https://github.com/translate/translate/releases/download/%{version}/%{upstream_name}-%{version}.tar.gz
Source1:        pocommentclean.1
Source2:        pocompendium.1
Source3:        pocount.1
Source4:        pomigrate2.1
Source5:        popuretext.1
Source6:        poreencode.1
Source7:        posplit.1
Source8:        tmserver.1

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-aeidon
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-chardet
BuildRequires:  python3-enchant
BuildRequires:  python3-iniparse
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-lxml
BuildRequires:  python3-phply
BuildRequires:  python3-pycountry
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-simplejson
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
BuildRequires:  python3-vobject

Requires:       gettext
Requires:       python3-aeidon
Requires:       python3-beautifulsoup4
Requires:       python3-chardet
Requires:       python3-cheroot
Requires:       python3-enchant
Requires:       python3-iniparse
Requires:       python3-Levenshtein
Requires:       python3-lxml
Requires:       python3-phply
Requires:       python3-pycountry
Requires:       python3-ruamel-yaml
Requires:       python3-simplejson
Requires:       python3-six
Requires:       python3-vobject

%description
A set of tools for managing translation and software localization via Gettext
PO or XLIFF format files.

Including:
  * Convertors: convert from various formats to PO or XLIFF
  * Formats:
    * Core localization formats - XLIFF and Gettext PO
    * Other localization formats - TMX, TBX, Qt Linguist (.ts),
           Java .properties, Wordfast TM, OmegaT glossary
    * Compiled formats: Gettext MO, Qt .qm
    * Other formats - OpenDocument Format (ODF), text, HTML, CSV, INI,
            wiki (MediaWiki, DokuWiki), iCal
    * Specialised - OpenOffice.org GSI/SDF, PHP,
            Mozilla (.dtd, .properties, etc), Symbian,
            Innosetup, tikiwiki, subtitles
  * Tools: count, search, debug, segment and pretranslate localization
            files. Extract terminology. Pseudo-localize
  * Checkers: validate translations with over 45 checks

%package        docs
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
# added during F26 cycle
Obsoletes:      %{name}-devel < %{version}-%{release}

%description    docs
This package contains Translate Toolkit documentation, including API docs
for developers  wishing to build new tools for the toolkit or to use
the libraries in other localization tools.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
LANG=C.utf8
%py3_build
make html -C docs/

%install
LANG=C.utf8
%py3_install

# create manpages
mkdir -p %{buildroot}%{_mandir}/man1
for prog in %{buildroot}%{_bindir}/*; do
    progname=$(basename $prog)
    case ${progname} in
      build_tmdb|buildxpi.py|get_moz_enUS.py|l20n2po|po2l20n|pydiff)
        ;;
      pocommentclean|pocompendium|pocount|pomigrate2|popuretext|poreencode|posplit|tmserver)
        cp -p %{_sourcedir}/${progname}.1 %{buildroot}%{_mandir}/man1/
        ;;
      *)
        PYTHONPATH=. $prog --manpage >  %{buildroot}%{_mandir}/man1/${progname}.1 || :
        grep -q .SH %{buildroot}%{_mandir}/man1/${progname}.1 || rm -f %{buildroot}%{_mandir}/man1/${progname}.1
        ;;
    esac
done

%files
%doc docs/license.rst
%{_bindir}/*
%{_mandir}/man1/*
%{python3_sitelib}/translate*

%files docs
%doc docs/_build/html

%changelog
* Fri Aug 9 2024 Sudip Shil <sshil@redhat.com> - 3.13.3-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.13.3.html

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.12.2-2
- Rebuilt for Python 3.13

* Tue Feb 13 2024 Sudip Shil <sshil@redhat.com> - 3.12.2-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.12.2.html

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Python Maint <python-maint@redhat.com> - 3.9.2-2
- Rebuilt for Python 3.12

* Mon Jul  3 2023 Jens Petersen <petersen@redhat.com> - 3.9.2-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.9.2.html

* Wed Mar 29 2023 Sundeep Anand <suanand@redhat.com> - 3.8.4-2
- update license tag to as per SPDX identifiers

* Wed Feb 8 2023 Sundeep Anand <suanand@redhat.com> - 3.8.4-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.8.4.html

* Mon Jan 23 2023 Sundeep Anand <suanand@redhat.com> - 3.8.3-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.8.3.html

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sundeep Anand <suanand@redhat.com> - 3.8.1-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.8.1.html

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 3.6.2-2
- Rebuilt for Python 3.11

* Wed May 11 2022 Sundeep Anand <suanand@redhat.com> - 3.6.2-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.6.2.html

* Thu Apr 21 2022 Sundeep Anand <suanand@redhat.com> - 3.6.1-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.6.1.html

* Mon Feb 28 2022 Sundeep Anand <suanand@redhat.com> - 3.6.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.6.0.html

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Sundeep Anand <suanand@redhat.com> - 3.5.3-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.5.3.html

* Fri Jan 7 2022 Sundeep Anand <suanand@redhat.com> - 3.5.2-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.5.2.html

* Wed Nov 10 2021 Sundeep Anand <suanand@redhat.com> - 3.5.1-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.5.1.html

* Tue Nov 2 2021 Sundeep Anand <suanand@redhat.com> - 3.5.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.5.0.html

* Mon Sep 13 2021 Sundeep Anand <suanand@redhat.com> - 3.4.1-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.4.1.html

* Tue Aug 24 2021 Sundeep Anand <suanand@redhat.com> - 3.4.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.4.0.html

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.6-2
- Rebuilt for Python 3.10

* Wed May 12 2021 Sundeep Anand <suanand@redhat.com> - 3.3.6-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.3.6.html

* Wed Apr 28 2021 Sundeep Anand <suanand@redhat.com> - 3.3.5-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.3.5.html

* Thu Apr 8 2021 Sundeep Anand <suanand@redhat.com> - 3.3.4-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.3.4.html

* Wed Mar 3 2021 Sundeep Anand <suanand@redhat.com> - 3.3.3-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.3.3.html

* Fri Feb 12 2021 Sundeep Anand <suanand@redhat.com> - 3.3.2-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.3.2.html

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 5 2021 Sundeep Anand <suanand@redhat.com> - 3.3.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.3.0.html

* Fri Nov  6 2020 Sundeep Anand <suanand@redhat.com> - 3.2.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.2.0.html

* Thu Sep 24 2020 Sundeep Anand <suanand@redhat.com> - 3.1.1-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.1.1.html

* Tue Sep 22 2020 Sundeep Anand <suanand@redhat.com> - 3.1.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.1.0.html

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Sundeep Anand <suanand@redhat.com> - 3.0.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/3.0.0.html

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-2
- Rebuilt for Python 3.9

* Mon Apr 27 2020 Sundeep Anand <suanand@redhat.com> - 2.5.1-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/2.5.1.html

* Tue Feb 25 2020 Jens Petersen <petersen@redhat.com> - 2.5.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/2.5.0.html

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Jens Petersen <petersen@redhat.com> - 2.4.0-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/2.4.0.html

* Fri Jul  5 2019 Jens Petersen <petersen@redhat.com> - 2.3.1-2
- add dep on pycountry

* Fri Jul  5 2019 Jens Petersen <petersen@redhat.com> - 2.3.1-1
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/2.3.1.html

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul  7 2018 Jens Petersen <petersen@redhat.com> - 2.3.0-1
- update to 2.3.0
- http://docs.translatehouse.org/projects/translate-toolkit/en/latest/releases/2.3.0.html

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.5-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.5-2
- Escape macros in %%changelog

* Wed Sep 27 2017 Jens Petersen <petersen@redhat.com> - 2.2.5-1
- update to 2.2.5 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Jens Petersen <petersen@redhat.com> - 2.1.0-3
- drop the unnecessary dependency on gaupol (Piotr Drag)
- add some manpages from Debian

* Fri Apr 14 2017 Jens Petersen <petersen@redhat.com> - 2.1.0-2
- remove shebangs from non-executable .py files (rpmlint)
- don't move data files
- build with C.utf8 (build warnings)
- remove improper manpages (rpmgrill)

* Thu Apr 13 2017 Jens Petersen <petersen@redhat.com> - 2.1.0-1
- update to 2.1.0
- http://docs.translatehouse.org/projects/translate-toolkit/en/stable-2.1.0/releases/2.1.0.html
- require gaupol
- rename devel subpackage to docs and include all html
- no longer remove ical2po, po2ical, sub2po, po2sub
- require gettext not gettext-libs
- use github for source url

* Mon Feb 13 2017 Jens Petersen <petersen@redhat.com> - 2.0.0-4
- build with python3 for F26+ and python2 otherwise (for Levenshtein)

* Sat Feb 11 2017 Jens Petersen <petersen@fedoraproject.org> - 2.0.0-3
- in python3 ConfigParser is called configparser

* Sat Feb 11 2017 Jens Petersen <petersen@fedoraproject.org> - 2.0.0-2
- add new python-diff-match-patch dep
- clean up deps

* Sat Feb 11 2017 Jens Petersen <petersen@fedoraproject.org> - 2.0.0-1
- update to 2.0.0 stable release (#1130071)
- build with python3

* Wed Nov  2 2016 Jens Petersen <petersen@redhat.com> - 1.13.0-1
- update to 1.13.0
- make it build by using autosetup, py2_build, and py2_install macros

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Christopher Meng <rpm@cicku.me> - 1.11.0-1
- Update to 1.11.0
- Add dependency: python-BeautifulSoup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 13 2011 Dwayne Bailey <dwayne@translate.org.za> - 1.9.0-1
- Update to 1.9.0
   - Various improvements: see release notes
   - Bugfixes relevant to Pootle
      - Support for Xapian 1.2
      - Work around some changes introduced in Django 1.2.5/1.3
      - Improved support for .ts comment as context
      - Support for Java properties in UTF-8 encoding
- Drop patches: encoding_logging

* Thu Feb 10 2011 Dwayne Bailey <dwayne@translate.org.za> - 1.8.1-3
- Fix rhbz#676603

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.8.1-1
- Update to 1.8.1
   - File formats:
     - A rewrite and major improvement of the html format
     - New JSON format introduced
     - Support for Universal Terminology Exchange (UTX) format
     - Support for Java properties files encoded in UTF-8
     - Improvements to CSV format, and improved compatibility with Excel
       exports
     - Bug fixes to Qt ts
     - Support for XLIFF's state attributes (pocount now lists detailed state
       statistics)
     - Minor bug fixes for PHP format
   - Major performance improvements to quality checks
   - Other improvements:
     - Improvements to stability of Lucene text indexing (affecting Pootle)
     - Parameter for po2prop to ignore untranslated strings
     - Many improvements to pot2po including Qt ts support, improved
       handling of extra XML namespaces in XLIFF, and performance
       improvements.
- Refresh stoplist location patch

* Wed Aug 18 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.8.0-1
- Update to 1.8.0
   - Required for Pootle 2.1 and recommended for Pootle 2.0
   - File formats: Adobe Flex, Mac OS X strings, Haiku catkeys
   - Terminology: Improvements to poterminology and terminology suggestions
   - Other improvements: Improvements to indexing performance and reliability
     in Pootle
- Drop patches: zh lambda, moz2po output directory

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 22 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.7.0-3
- Depend on aeidon for subtitle support
- Backport r14946 to fix rhbz#603597 - moz2po output to directory

* Mon Jun 7 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.7.0-2
- Backport upstream r14600 to fix rhbz#600561

* Thu May 13 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.7.0-2
- Align spec with EL-5, fixing missing dependencies

* Thu May 13 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.7.0-1
- Update to 1.7.0
   - Support for Array constructs in the PHP converter
   - Detect the target language from the PO team header
   - Improvements in detecting languages for many other formats
   - Correctly migrate the header comments from the old PO file in pot2po
   - Handle certain malformed PO files better
   - Reliability improvements for Qt TS and XLIFF
   - Support for longer terminology entries
   - New plural information: Sinhala (si), Aragonese (an),
     Catalan (Valencia) (ca@valencia), Romansh (rm), Tatar (tt)
   - Some language specific customisations for Sinhala and Thai.
   - New: junitmsgfmt, runs msgfmt and provides junit-type output for use
     in continuous integration systems such as Hudson.
   - Reliability improvements for Lucene when Pootle is under Apache
   - Correctly use the header encoding when opening .mo files
   - Avoid adding an extra type comment line (#,) (bug 1400)
   - Support any delimiter (=, : or space) in po2prop as we do in prop2po
   - Better handling of non-default encodings for .rc files

* Fri Mar 19 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.6.0-1
- Update to 1.6.0
   - Improvements to quality tests for speed and accuracy
   - Improvements to language specific quality checks
   - Small improvements to the handling of incorrect PO files
   - Better support for the newer comment types in TS
   - Several small improvements and corrections to XLIFF and TS
   - Many API improvements and cleanups for the upcoming Pootle and Virtaal
   - Fix a bug when Virtaal opened files in paths with non-ASCII characters
   - The Toolkit now always creates headers for PO files
   - A better XML placeable with support for XML namespaces
   - A small bug with a single space unit as seen in abrt (bug 1370). This
     also fixes the resulting error in Virtaal.
- Drop patch for bug 1372

* Mon Feb 22 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.5.3-2
- Bug #1372: Decode fulesystem paths correctly

* Fri Feb 19 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.5.3-2
- Use python2-devel in BuildRequires

* Tue Feb 2 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.5.3-1
- Update to 1.5.3
   - Plural information for more languages
   - Cleaner language names (for the benefit of Pootle and Virtaal)
   - Skype support for prop2po and po2prop [by Filip Miletić]
   - Small improvement to Qt .ts support
   - Other small bugfixes
- Redo stoplist patch
- Drop gaupol and iniparse from BuildRequires

* Mon Jan 11 2010 Dwayne Bailey <dwayne@translate.org.za> - 1.5.2-1
- Update to 1.5.2
   - Initial support for '#' type comments in the PHP converters (#1298)
   - Reliability improvements for Pootle concerning Xapian and Python 2.4
   - A small fix affecting searching in Virtaal
   - Classify XML tags as editable placeables for Virtaal (#1287)
   - Correctly handle language codes with '@' in them (like ca@valencia)
   - Don't unnecessarily add empty 'note' nodes in XLIFF (#1319)
   - Allow for the translation of 'title' attributes in XML (#1294)
- Drop LRU patch

* Thu Nov 26 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.5.1-2
- Make lru.py exception handling work in Python 2.4

* Thu Nov 26 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.5.1-1
- Update to 1.5.1
   - Support for OmegaT glossary files
   - Fixes for the fast (but still experimental) C PO parser
   - Fixes for the LRU cache
   - Fixes for correct and faster language identification
- Remove backports introduced in 1.5.0-1

* Tue Nov 24 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.5.0-1
- Update to 1.5.0
  - The tmserver will now be multithreaded if cherrypy is installed
  - New faster PO parser for testing
  - Optionally preserve HTML comments in html2po. Bug #1183
  - Many reliability and API improvements for the upcoming versions of Pootle and Virtaal
- Move langmodels into /usr/share/translate-toolkit
- Remove backports introduced in 1.4.1-2
- Backports:
   - r13226, r13234 - fix and optimise language identification
   - r13225 - check for units based on source and target text

* Tue Nov 3 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.1-2
- Backport various fixes needed for Pootle 1.3
   - r12685 index speedup
   - r12686 id index
   - r12724 hassuggestion speedup
   - r12727 msgidcomment

* Thu Oct 15 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.1-2
- Retag

* Thu Oct 15 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.1-1
- Update to 1.4.1
   - Better support for printf (including numbered) variables (bug 1118)
   - Fixes for the upcoming Pootle, including combined searches (bug 1036)
   - subtle bug in tmserver handling of the percent sign (%%) (bug 1101)
   - obsolete messages seen as translatable (bug 1114)
- Drop patch bug#1114 - obsolete messages should not be translatable

* Mon Aug 24 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.0-2
- Upstream bug #1114 - obsolete messages should not be translatable

* Wed Aug 5 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.0-1
- Update to 1.4.0 final

* Fri Jul 31 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.0-0.5.rc2
- Fix tarball reference

* Fri Jul 31 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.0-0.4.rc2
- Update to 1.4.0 rc2
   - Some small fixes for XLIFF support
   - API documentation has been augmented with diagrams

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 24 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.0-0.2.rc1
- Update to 1.4.0 rc1

* Sat Jun 27 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.4.0-0.1.beta1
- Update to 1.4.0 beta1

* Fri Jun 12 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.3.0-3
- Remove old excludes for /usr/bin/*.py{o,c}

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.3.0-1
- Update to 1.3.0 final release

* Tue Feb 3 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.3.0-0.2.rc1
- Update to 1.3.0 rc1

* Thu Jan 22 2009 Dwayne Bailey <dwayne@translate.org.za> - 1.3.0-0.1.beta1
- Update to 1.3.0 beta1

* Sat Dec 6 2008 Dwayne Bailey <dwayne@translate.org.za> - 1.2.1-1
- Update to 1.2.1
- Refresh poterminology patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.0-4
- Rebuild for Python 2.6

* Mon Nov 17 2008 Dwayne Bailey <dwayne@translate.org.za> - 1.2.0-3
- Rebuild using %%{ix86} instead of i386

* Mon Nov 17 2008 Dwayne Bailey <dwayne@translate.org.za> - 1.2.0-2
- python-psyco is only available on i386
- Remove RHEL dependency on python-enchant

* Wed Nov 12 2008 Dwayne Bailey <dwayne@translate.org.za> - 1.2.0-1
- Update to 1.2.0
- Patch poterminology to read stoplist-en from /usr/share/
- Add devel package to include generated Translate Toolkit API documentation
- Add dependencies: python-iniparse, python-Levenshtein, python-lxml,
  python-psyco, python-vobject, gettext-libs
- Drop iCal support for RHEL

* Fri Jun 06 2008 Roozbeh Pournader <roozbeh@gmail.com> - 1.1.1-1
- update to 1.1.1

* Mon Jan 21 2008 Jens Petersen <petersen@redhat.com> - 1.0.1-1
- update license field to GPLv2+
- update to 1.0.1 with changes from Dwayne Bailey (#315021):

* Thu Dec 20 2007 Dwayne Bailey <dwayne@translate.org.za>
- Update spec to upstream 1.0.1
- Update patch for Python 2.5 ElementTree
- Cleanup the doc installation
- Create man pages
- Update description

* Sat May 05 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.11-1
- Update to upstream 0.11, adding HTML documentation

* Tue Jan 09 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.10.1-4
- Patch to use Python 2.5's built-in ElementTree

* Sat Dec 30 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.10.1-3
- Rebuild to fix dependency problem

* Sat Dec 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.10.1-2
- Rebuild for Python 2.5

* Thu Nov 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.10.1-1
- Update to upstream 0.10.1
- Cleanup based on latest Python packaging guidelines

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-2
- Rebuild to get into Rawhide

* Mon Feb 20 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-1
- Update to final 0.8

* Sun Feb 19 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.10.rc6
- Fix a typo in po2dtd that made po2moz fail

* Tue Feb 14 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.9.rc6
- Rebuild for Fedora Extras 5

* Tue Feb 07 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.8.rc6
- Require python-enchant for spellchecking support in pofilter

* Sat Feb 04 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.7.rc6
- Rebuild

* Sat Feb 04 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.6.rc6
- Update to 0.8rc6

* Sat Jan 21 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.5.rc5
- Use sed instead of dos2unix

* Mon Jan 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.4.rc5
- Own forgotten subdirectories

* Mon Jan 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.3.rc5
- Fix the jToolkit requirement

* Sun Jan 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.2.rc5
- Add %%{?dist} tag

* Sat Jan 07 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 0.8-0.1.rc5
- Initial packaging
