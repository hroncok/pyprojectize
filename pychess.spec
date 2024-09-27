%bcond_without docs
%bcond_without tests

Name:           pychess
Version:        1.0.3
Release:        14%{?dist}
Summary:        Chess game for GNOME

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://pychess.github.io
Source0:        https://github.com/pychess/pychess/archive/%{version}/%{name}-%{version}.tar.gz
# PR#1897 Update metainfo to the latest spec
Patch0:         https://github.com/pychess/pychess/pull/1897.patch
# PR#1988 Remove unnecessary shebangs
Patch1:         https://github.com/pychess/pychess/pull/1898.patch
# PR#2005 Python 3.12: Use importlib instead of deprecated imp module
Patch2:         https://github.com/pychess/pychess/pull/2005.patch
# PR#2235 Python 3.13: Drop use of telnetlib
# https://github.com/pychess/pychess/pull/2235
Patch3:         0001-TimeSeal.py-make-IAC_WONT_ECHO-a-literal-as-telnetli.patch


BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(sqlalchemy) < 2
BuildRequires:  gtk3
BuildRequires:  librsvg2
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sed
%if %{with docs} || %{with tests}
BuildRequires:  gstreamer1
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(websockets)
%endif
%if %{with docs}
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-docs
Suggests:       %{name}-doc
%endif
%if %{with tests}
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  python3dist(coverage)
BuildRequires:  gtksourceview3
BuildRequires:  stockfish
%endif

Requires:       python3dist(psutil)
Requires:       python3dist(sqlalchemy) < 2
Requires:       python3dist(websockets)
# gnome-settings-daemon
Requires:       python3-gobject
Requires:       librsvg2
Requires:       hicolor-icon-theme
Requires:       python3-gstreamer1
# for editing .pgn files
Requires:       gtksourceview3

Recommends:     stockfish

%description
PyChess is a GTK+ chess game for Linux. It is designed to at the same time
be easy to use, beautiful to look at, and provide advanced functions for
advanced players.


%if %{with docs}
%package        doc
Summary:        Documentation for PyChess
Requires:       python3-docs

%description    doc
This package contains additional documentation for PyChess.
%endif


%prep
%autosetup -n %{name}-%{version} -p1

# disable update check
cat > lib/pychess/Utils/checkversion.py <<EOF
def isgit():
    return False

async def checkversion():
    return
EOF

%if %{with docs}
# Use local intersphinx inventory
# TODO: do the same for pgi-docs once that's packaged
sed -r \
    -e 's|https://docs.python.org/3\.4|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif

%build
%py3_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD}/lib sphinx-build-3 docs html
%endif


%install
%py3_install
# Remove Debian specific menu stuff
rm -r %{buildroot}%{_datadir}/menu

desktop-file-install --delete-original               \
        --dir=%{buildroot}%{_datadir}/applications   \
        --set-key=Exec --set-value=pychess           \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet                \
        %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%find_lang %{name}


%if %{with tests}
%check
# remove tests requiring network access
rm testing/remotegame.py
# run tests
pushd testing
PYTHONPATH=../lib PYCHESS_UNITTEST=true xvfb-run -a coverage run \
  --omit=../lib/pychess/external/* \
  --source ../lib \
  -m unittest discover \
  -p "*.py"
%endif


%files -f %{name}.lang
%doc README.md AUTHORS ARTISTS DOCUMENTERS TRANSLATORS
%doc utilities
%license LICENSE
%{python3_sitelib}/%{name}
%{python3_sitelib}/PyChess-%{version}-py%{python3_version}.egg-info
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/gtksourceview-3.0/language-specs/pgn.lang
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man?/*
%{_metainfodir}/*.metainfo.xml


%if %{with docs}
%files doc
%license LICENSE
%doc doc/*.dia
%doc html
%endif


%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Adam Williamson <awilliam@redhat.com> - 1.0.3-12
- Backport PR #2235 to fix with Python 3.13 (telnetlib removed)
- Rebuilt for Python 3.13

* Thu Mar 21 2024 Nils Philippsen <nils@tiptoe.de> - 1.0.3-11
- Require SQLAlchemy < 2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-7
- Apply upstream patch for python3.12 imp module removal

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.0.3-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 13 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.3-4
- Add missing Requires for sqlalchemy
  Fixes: RHBZ#2118059

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.11

* Tue Feb 15 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- Backport PR#1897 to update the bundled metainfo xml
- Backport PR#1898 to remove unnecessary shebangs
- Disable version update check
- Build and package the documentation
- Conditionally run the test suite
- Drop logic for retired versions and update macros
- Update project URL
- Update BuildRequires and add a Recommends for stockfish

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.4-23
- Rebuilt for Python 3.10

* Fri Feb 05 2021 Kalev Lember <klember@redhat.com> - 0.12.4-22
- Require hicolor-icon-theme instead of obsolete gnome-icon-theme

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.4-10
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.4-7
- Switch to Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-5
- Without python-gobject, pychess doesn't work properly

* Mon Jun 27 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-4
- For now also require gtksourceview3, since it at least checks for it

* Sun Jun 26 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-3
- No we should use gtksourceview2, because that's what pygtksourceview does

* Sun Jun 26 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-2
- We need gtksourceview3

* Sun Jun 26 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-1
- Update to 0.12.4
- Bugfix release. See: https://github.com/pychess/pychess/releases/tag/0.12.4
- Patch is no longer needed.

* Thu Mar 03 2016 Sérgio Basto <sergio@serjux.com> - 0.12.3-1
- Update to pychess-0.12.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.10.1-7
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> 0.10.1-4
- Remove vendor prefix from desktop file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Bruno Wolff III <bruno@wolff.to> 0.10.1-1
- Upstream 0.10.1 release
- Should only be bug fixes since beta2
- At some point the license changed to GPL3

* Sat Oct 29 2011 Bruno Wolff III <bruno@wolff.to> 0.10.1-0.1.beta2
- Pick up a few more bug fixes with the beta2 prerelease.

* Sat Sep 03 2011 Bruno Wolff III <bruno@wolff.to> - 0.10.rev2004-1
- Pickup lots of post 0.10 fixes (hopefully that fix reported bugs)

* Wed May 18 2011 Christopher Aillon <caillon@redhat.com> - 0.10-1
- Update to 0.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Michel Salim <salimma@fedoraproject.org> - 0.10-0.8.rc1
- Update to 0.10rc1
- Install PGN language spec in correct location
- Properly update icon cache

* Sun Aug 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.7.20100815hg
- update to new version (fixes bug #598062)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10-0.6.20100511hg
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.5.20100511hg
- new hg snapshot to fix #591165

* Tue May  4 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.4.20100504hg
- new hg snapshot to get it working again (#577570)

* Sun Feb 14 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.3.20100214svn
- update svnsnapshot to fix some fedora bugs
  (562895,565225,563330)

* Fri Feb  5 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.2.20100203svn
- add R: gnome-python2-rsvg (#551475)

* Wed Feb  3 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.1.20100203svn
- update to svn snapshot (the rest is currently non working)
- %%global and not %%define
- delete the patches, all upstream or solved upstream differently
- remove R python-sqlite2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8.2-2
- Rebuild for Python 2.6

* Tue Aug 26 2008 Michel Salim <salimma@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Mon Mar 17 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 0.8-2
- Bump release

* Thu Feb 21 2008 Sindre Pedersen Bjordal <foolish@guezz.net> - 0.8-1
- Final 0.8 release

* Mon Dec  3 2007 Michel Salim <michel.sylvan@gmail.com> - 0.8-0.1.beta2
- Update to 0.8beta2

* Sun Nov 11 2007 Michel Salim <michel.sylvan@gmail.com> - 0.8-0.1.beta1
- Update to 0.8beta1

* Thu Apr 19 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-1
- Update to 0.6.0 final

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.3.beta5
- Update description

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.2.beta5
- Fix permissions
- Fix quiet %%setup

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.1.beta5
- Initial build
