Name:           printrun
Epoch:          1
Version:        2.0.0
%global prerel  rc8
%global uver    %{version}%{?prerel}
%global tag     %{name}-%{uver}
Release:        0.33.%{prerel}%{?dist}

Summary:        RepRap printer interface and tools
# Only AppData is FSFAP
# Automatically converted from old format: GPLv3+ and FSFAP - review is highly recommended.
License:        GPL-3.0-or-later AND FSFAP

URL:            https://github.com/kliment/Printrun
Source0:        https://github.com/kliment/Printrun/archive/%{tag}.tar.gz

# Fix a crashes on Python 3.10
Patch1:         %{url}/pull/1224.patch
Patch2:         %{url}/pull/1262.patch
Patch3:         %{url}/pull/1303.patch

BuildRequires:  gcc
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-pyserial
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/grep
BuildRequires:  /usr/bin/msgfmt
BuildRequires:  /usr/bin/sed

Requires:       pronterface = %{epoch}:%{version}-%{release}
Requires:       pronsole = %{epoch}:%{version}-%{release}
Requires:       plater = %{epoch}:%{version}-%{release}

%description
Printrun is a set of G-code sending applications for RepRap.
It consists of printcore (dumb G-code sender), pronsole (featured command line
G-code sender), pronterface (featured G-code sender with graphical user
interface), and a small collection of helpful scripts.
This package installs whole Printrun.

###############################################

%package        common
Summary:        Common files for Printrun
Requires:       python3-appdirs
Requires:       python3-lxml
Requires:       python3-numpy

Provides:       bundled(tatlin)

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

###############################################

%package     -n pronsole
Summary:        CLI interface for RepRap
Requires:       python3-pyserial
Requires:       %{name}-common = %{epoch}:%{version}-%{release}
# So that it just works
Requires:       3dprinter-udev-rules

BuildArch:      noarch

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer. It is a part of Printrun.

################################################

%package     -n pronterface
Summary:        GUI interface for RepRap
Requires:       python3-cairocffi
Requires:       python3-cffi
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       python3-pyglet
Requires:       python3-wxpython4
Requires:       simarrange
Requires:       pronsole = %{epoch}:%{version}-%{release}
# So that it just works
Requires:       3dprinter-udev-rules

BuildArch:      noarch

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer. It is a part of Printrun.

###############################################

%package     -n plater
Summary:        RepRap STL plater
Requires:       %{name}-common = %{epoch}:%{version}-%{release}
Requires:       python3-cairocffi
Requires:       python3-cffi
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       python3-pyglet
Requires:       python3-wxpython4
Requires:       simarrange
BuildArch:      noarch

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.

###############################################


%prep
%autosetup -p1 -n Printrun-%{tag}

# don't pin wxpython
sed -i 's/wxPython (== 4.1.0)/wxPython (>= 4)/' requirements.txt

# sed upstream's desktop files to remove .py extensions from Exec
sed -i 's/.py//' *.desktop

# remove useless shebangs
grep -ilrx printrun -e '#!/usr/bin/env python3' --include '*.py'| xargs sed -i '1s|^#!/usr/bin/env python3$||'

%generate_buildrequires
%pyproject_buildrequires

%build
# rebuild locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || :
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || :
done
cd ..

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

cd %{buildroot}%{_bindir}
for FILE in *.py; do
  mv -f $FILE ${FILE%.py}
done

cd -

%{find_lang} pronterface
%{find_lang} plater


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%doc README*
%license COPYING

%files common -f %{pyproject_files}
%{_bindir}/printcore*
%doc README*

%files -n pronsole
%{_bindir}/pronsole*
%{_datadir}/pixmaps/pronsole.png
%{_datadir}/applications/pronsole.desktop
%{_datadir}/metainfo/pronsole.appdata.xml
%doc README*
%license COPYING

%files -n pronterface -f pronterface.lang
%{_bindir}/pronterface*
%{_datadir}/pronterface/
%{_datadir}/pixmaps/pronterface.png
%{_datadir}/applications/pronterface.desktop
%{_datadir}/metainfo/pronterface.appdata.xml
# This file is needed by both pronterface and plater, so it is in both
# https://bugzilla.redhat.com/show_bug.cgi?id=1777737
%{_datadir}/pixmaps/plater.png
%doc README*
%license COPYING

%files -n plater -f plater.lang
%{_bindir}/plater*
%{_datadir}/applications/plater.desktop
%{_datadir}/pixmaps/plater.png
%{_datadir}/metainfo/plater.appdata.xml
%doc README*
%license COPYING

%changelog
* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1:2.0.0-0.33.rc8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.32.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:2.0.0-0.31.rc8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.30.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.29.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.28.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1:2.0.0-0.27.rc8
- Rebuilt for Python 3.12

* Thu Jan 26 2023 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.26.rc8
- Fix another crash on Python 3.10

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.25.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.24.rc8
- Fix another crash on Python 3.10

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.23.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:2.0.0-0.22.rc8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.21.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.20.rc8
- Update to 2.0.0rc8
- Fix a crash on Python 3.10
- Fixes rhbz#2022732

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.19.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:2.0.0-0.18.rc5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.17.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.16.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.15.rc5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.14.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.13.rc5
- Add missing plater.png to pronterface (#1777737)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.12.rc5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.11.rc5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.10.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.9.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.8.rc5
- Fix Python 3 compatibility when handling filename command line argument (#1654399)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-0.7.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.6.rc5
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.5.rc5
- Update to 2.0.0rc5
- Provide bundled tatlin (this is not new, rather forgotten before)

* Fri Mar 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.4.rc4
- Update to 2.0.0rc4

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.3.rc3
- Update to 2.0.0rc3

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.2.rc2
- Update to 2.0.0rc2

* Sat Mar 03 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.0-0.1.rc1
- Update to 2.0.0rc1
- Use Python 3 and wxPython 4
- raise epoch
- AppData license changed from CC0 to FSFAP

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2015.03.10-10
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.10-6
- Add a patch to always run on X11

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.10-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 25 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.10-4
- Require 3dprinter-udev-rules

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 05 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03.10-2
- Add patch to resolve GTK3 issues (by Scott Talbert) (#1231518)

* Fri Jun 19 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03.10-1
- Update to 2015.03.10
- Removed no longer needed simarrange patch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.08.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 29 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08.01-1
- Update to 2014.08.01 (minor upstream fix)
- Remove prontserve from the spec
- Remove Fedora <> 20 conditions
- pronterface and plater require python-psutil and numpy (#1171319)
- the slicer command is now in different file

* Sat Oct 25 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07.30-3
- Do not longer depend on skeinforge, as it appears nobody uses it

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.07.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07.30-1
- New version
- Remove merged patches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.01.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01.26-3
- Use PNG icons, so AppData works

* Mon Mar 17 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01.26-2
- Fix 1077126

* Wed Mar 05 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01.26-1
- New version
- Do not ship our own desktop and appdata files, now it's in tarball
- Add macros to simplify the version to gittag conversion
- Remove merged patches and rebased simmarange patch
- Build require pyserial
- sed upstream's desktop files to remove .py

* Fri Dec 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-8
- Make subpackages other than common noarch on F21+

* Fri Dec 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-7
- Add AppData

* Fri Nov 15 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-6
- Use system's simarrange in plater

* Wed Nov 13 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-5
- Finally, this seems like a proper fix for 438

* Sun Nov 10 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-4
- Go back to our workaround

* Sun Nov 10 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-3
- Bad upstream "proper" fix for 438

* Tue Oct 29 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-2
- Added patch to workaround upstream issue 438

* Sat Oct 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10.19-1
- New upstream release
- Switch to new versioning, drop commit hashes from version/release
- Upstream now has proper entrypoints, so entire %%install is redone

* Fri Sep 06 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-32.20130711gitb8f549b
- Fixed #1004973 (%%{name}-missing-plater-import.patch)
- In F <= 19 added backwards compatibility .py symlinks to bindir
- Added asterisk at the end of bindir content in %%files to also match those symlinkss

* Sun Aug 11 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-31.20130711gitb8f549b
- No longer have .py named scripts in bindir

* Sat Aug 10 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-30.20130711gitb8f549b
- Fix bad patch

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-29.20130711gitb8f549b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-28.20130711gitb8f549b
- New upstream tag release
- Corrected bogus date in %%changelog
- Flush patch no longer needed
- No longer NoArch
- BR added Cython

* Thu Jun 20 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-27.20130604git80e313d
- Added patch to solve upstream issue 402

* Tue Jun 18 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-26.20130604git80e313d
- Upstream released tag release 20130604
- Pyglet 1.2 issue fixed in upstream, removed patch
- Prepared spec for prontserve but do not produce the package yet (not all deps satisfied)

* Tue Jun 18 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-25.20130123git71e5da0
- When printrun is installed and plater not, don't crash when clicking Compose
- Require pyglet for plater for F18+

* Fri Jun 07 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-24.20130123git71e5da0
- Fixed Pyglet 1.2 issue (#868266)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-23.20130123git71e5da0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-22.20130123git71e5da0
- Pull request merged
- Updated to new commit
- Removed pacth (no longer needed)

* Wed Jan 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-21.20130113git5897fbc
- Handle UTF-8 encode better in patch

* Wed Jan 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-20.20130113git5897fbc
- Removing UTF-8 removal from patch

* Sat Jan 19 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-19.20130113git5897fbc
- Removed run-time deps, that are resolved automatically

* Sat Jan 19 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-18.20130113git5897fbc
- Added patch from my pull request

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-17.20130113git5897fbc
- New "version" (bugfix)

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-16.20130113git094dffa
- New upstream "version", where everything is GPLv3+
- pronsole.ico and gcoder.py now part of setup.py
- Skeinforge path changing moved from %%install to %%prep
- Commented macros in changelog
- Use skeinforge launchers in default settings
- Pronterface lang moved from common to pronterface, is not needed by pronsole any more

* Wed Jan 09 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-15.20121103git6fa4766
- Updated to respect new GitHub rule

* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-14.20121103git6fa47668f2
- Changed location of skeinforge from %%{_datadir}/%%{name}/
                                   to %%{python_sitelib}/%%{name}

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-13.20121103git6fa47668f2
- Do not download the desktop files from my GitHub

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-12.20121103git6fa47668f2
- Fixing a source mistake
- Redone, using setup.py now

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-11.20121103git6fa47668f2
- New upstream "version" (merge from experimetal)
- Commented macros in comments
- Playing a bit with attr

* Mon Oct 29 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-10-20120924gitb6935b93
- Switched generic names and names in desktop files
- Don't use rm, cp and ln -s macros

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-9-20120924gitb6935b93
- updated bash lounchers

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-8-20120924gitb6935b93
- ln -s skeinforge
- printrun requires exact version and release

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-7-20120924gitb6935b93
- New sources links

* Sat Sep 22 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-6-20120924gitb6935b93
- New commits, inlude the license

* Sat Sep 22 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-5-20120921gitdceaf26f
- launching scripts now pass the params

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-4-20120921gitdceaf26f
- Build gettext

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-3-20120921gitdceaf26f
- BuildRequires:  desktop-file-utils

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-2-20120921gitdceaf26f
- Language files correctly added

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-1-20120921gitdceaf26f
- New package
