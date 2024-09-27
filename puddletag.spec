Summary:        Feature rich, easy to use tag editor
Name:           puddletag
Version:        2.4.0
Release:        3%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://docs.puddletag.net/
Source0:        https://github.com/puddletag/puddletag/archive/refs/tags/%{version}.tar.gz
Patch0:         puddletag-2.4.0-req.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Buildrequires:  desktop-file-utils
Requires:       PyQt5
Requires:       python3-pyparsing >= 1.5.5
Requires:       python3-acoustid
Requires:       python3-mutagen
Requires:       python3-configobj
Requires:       python3-Levenshtein
%description
Puddletag is an audio tag editor.

Unlike most taggers, it uses a spreadsheet-like layout so that all the
tags you want to edit by hand are visible and easily editable.

The usual tag editor features are supported like extracting tag
information from filenames, renaming files based on their tags by
using patterns (that you define, not crappy, uneditable ones).

Then there are Functions, which can do things like replace text, trim,
change the case of tags, etc. Actions can automate repetitive
tasks. You can import your QuodLibet library, lookup tags using
AcoustID, MusicBrainz, FreeDB or Amazon (though it is only good for
cover art) and more.

Supported formats: ID3v1, ID3v2 (mp3), MP4 (mp4, m4a, etc.),
VorbisComments (ogg, flac), Musepack (mpc), Monkeys Audio (.ape) and
WavPack (wv).

%prep
%autosetup -p1

%build
%{py3_build}

%install
%{py3_install}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
find %{buildroot} -name exampletags\* -delete
chmod 0644 %{buildroot}%{python3_sitelib}/puddlestuff/data/{menus,shortcuts}

%files
%license copyright
%doc NEWS THANKS TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/puddlestuff/
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.4.0-1
- 2.4.0

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.13

* Mon May 06 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.3.0-3
- Fix pyparsing 3.1.2 issue (rbbz#2277510)

* Mon Mar 18 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.3.0-2
- Levenshtein has changed name, however package name is fixed

* Wed Mar 06 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.3.0-1
- 2.3.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-2
- Rebuilt for pyparsing-3.0.9

* Sat Jul 09 2022 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-1
- 2.2.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.1-4
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Terje Rosten <terje.rosten@ntnu.no> - 2.1.1-3
- Use upstream patch to resolve bug below

* Wed Jun 01 2022 Terje Rosten <terje.rosten@ntnu.no> - 2.1.1-2
- Try to fix rhbz#2084341

* Sat Feb 05 2022 Terje Rosten <terje.rosten@ntnu.no> - 2.1.1-1
- 2.1.1

* Tue Feb 01 2022 Terje Rosten <terje.rosten@ntnu.no> - 2.1.0-1
- 2.1.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.0.1-1
- Update to puddletag 2.0.1 with Python 3 support

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-7
- Use correct python macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-4
- Prefer python2-* style deps

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-1
- 1.2.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.1.1-1
- 1.1.1

* Sun Sep 20 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.0.5-3
- Add patch from upstream to fix bz#1256225

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.0.5-1
- 1.0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-1
- 1.0.3

* Mon Nov 18 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.0.2-1
- 1.0.2

* Mon Aug 05 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.0.2-0.1.rc1
- 1.0.2RC1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-3
- Fix req (bz #895788)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1

* Thu Aug 23 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.0.0-1
- 1.0.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.10.6-2
- Fix typo in xdg-open patch

* Tue Jun 14 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.10.6-1
- 0.10.6

* Mon Mar 28 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.10.3-1
- 0.10.3

* Sun Mar 13 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.10.0-1
- 0.10.0

* Mon Feb 28 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.9.12-1
- 0.9.12

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.9.11-2
- add dep on quodlibet
- add xdg-open patch

* Mon Dec 27 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.11-1
- 0.9.11
- fix license
- add comment about py reqs
- add slash to dir in files
- fix typo in description
- remove buildroot tag
- remove define of python macro
- remove python req
- fix sed expression

* Mon Dec  6 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.7-1
- 0.9.7

* Thu Oct 21 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-1
- initial build
