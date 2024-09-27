Name:           isrcsubmit
Version:        2.1.0
Release:        18%{?dist}
Summary:        Script to submit ISRCs from disc to MusicBrainz

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://jonnyjd.github.io/musicbrainz-isrcsubmit/
Source0:        http://isrcsubmit.jonnyjd.net/downloads/%{name}-%{version}.tar.gz
Patch0:         %{name}-2.0.1-no-setup-requires.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-libdiscid
BuildRequires:  python3-musicbrainzngs
BuildRequires:  python3-sphinx
Requires:       python3-libdiscid
Requires:       python3-musicbrainzngs
Requires:       python3-keyring
# https://bugzilla.redhat.com/show_bug.cgi?id=1831460
%{?python_disable_dependency_generator}

%description
This python script extracts ISRCs from audio cds and submits them to
MusicBrainz. Features: read and submit ISRCs from disc, search for
releases with the TOC of the disc, submit discIds / TOCs, display
release information from MusicBrainz, duplicate ISRC detection (local
and on server), keyring support for login information.


%prep
%autosetup
# Fix build with setuptools 62.1
# https://github.com/JonnyJD/musicbrainz-isrcsubmit/issues/140
sed -i "100i packages=[]," setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
# sys.stdin.encoding can be None in mock, hence override with PYTHONIOENCODING
export PYTHONIOENCODING=UTF-8
%{__python3} -Wall setup.py test


%files
%license COPYING
%doc AUTHORS CHANGES.markdown README.rst
%{_bindir}/isrcsubmit.py
%{python3_sitelib}/%{name}-%{version}*
%{_mandir}/man1/isrcsubmit.1*
%{_mandir}/man5/isrcsubmit-config.5*


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Lumír Balhar <lbalhar@redhat.com> - 2.1.0-11
- Fix compatibility with the latest setuptools

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 David King <amigadave@amigadave.com> - 2.1.0-6
- BuildRequire python3-setuptools explicitly

* Tue May 05 2020 David King <amigadave@amigadave.com> - 2.1.0-5
- Fix failure to install (#1759754)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 David King <amigadave@amigadave.com> - 2.1.0-1
- Update to 2.1.0 (#1680207)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-8
- Drop Python 2 build support

* Fri May 26 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-7
- Run tests with -Wall
- Drop obsolete build conditionals

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-5
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-3
- Use Python 3 on F-23+

* Mon Jun 29 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-2
- Do not try to download any packages during build

* Tue Jun 16 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-1
- Update to 2.0.1

* Sun Apr 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.0-2
- Add man page, fix and run test suite (#1210941)

* Sat Apr 11 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.0-1
- First build
