Name:           soundconverter
Version:        4.0.5
Release:        4%{?dist}
Summary:        Simple sound converter application for GNOME
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only

URL:            http://soundconverter.org
Source0:        http://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:         %{name}-appdata.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-base
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib

Requires:       python3-gobject-base
Requires:       gtk3
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-ugly-free


%description
SoundConverter is the leading audio file converter for the GNOME Desktop. It
reads anything GStreamer can read (Ogg Vorbis, AAC, MP3, FLAC, WAV, AVI, MPEG,
MOV, M4A, AC3, DTS, ALAC, MPC, Shorten, APE, SID, MOD, XM, S3M, etc...), and
writes to Opus, Ogg Vorbis, FLAC, WAV, AAC, and MP3 files, or use any GNOME
Audio Profile.

SoundConverter aims to be simple to use, and very fast. Thanks to its
multithreaded design, it will use as many cores as possible to speed up the
conversion. It can also extract the audio from videos.

%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

mkdir -p %{buildroot}/usr/share/locale
mv build/mo/* %{buildroot}/usr/share/locale/
%find_lang %{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --add-category X-OutputGeneration \
  --delete-original \
  build/share/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

rm -f %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled


%files -f %{name}.lang
%license COPYING
%doc AUTHORS CHANGELOG
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.soundconverter.gschema.xml
%{_docdir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}.dist-info


%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.5-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0.5-2
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Richard Shaw <hobbes1069@gmail.com> - 4.0.5-1
- Update to 4.0.5.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Richard Shaw <hobbes1069@gmail.com> - 4.0.4-1
- Update to 4.0.4.

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.0.3-6
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.3-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Richard Shaw <hobbes1069@gmail.com> - 4.0.3-1
- Update to 4.0.3.

* Mon Oct 04 2021 Adam Williamson <awilliam@redhat.com> - 4.0.1-5
- Backport PR #54 to fix crasher bug #1988116

* Mon Oct 04 2021 Adam Williamson <awilliam@redhat.com> - 4.0.1-4
- Backport fixes for https://bugs.launchpad.net/soundconverter/+bug/1945838

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.1-2
- Rebuilt for Python 3.10

* Sat May 15 2021 Richard Shaw <hobbes1069@gmail.com> - 4.0.1-1
- Update to 4.0.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Richard Shaw <hobbes1069@gmail.com> - 4.0.0-1
- Update to 4.0.0.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Leigh Scott <leigh123linux@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Fri Apr 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- Update to 3.0.0
- Update spec file
- Validate appdata

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.6-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.6-5
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Pranav Kant <pranvk@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.5-2
- Merge post-2.1.5 fix for drag'n'drop (lp:1419259).

* Sat Jan 31 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5 (fix for URI creation when doing drag'n'drop,
   encoding of VBR mp3, updated translations).

* Mon Sep  1 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (a few more bug-fixes).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  1 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3 (a few more bug-fixes).

* Fri Jan  3 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.2-3
- Merge upstream pull request: Pass on error in another location.

* Wed Dec 25 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.2-2
- Merge upstream pull request: Replacing messy characters replaced also "/".

* Tue Nov 26 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2.

* Wed Oct  9 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.1-6
- Merge fixes for lp:1213244, lp:1205828 (GStreamer error handling and
  cancelled codec installation).

* Mon Oct  7 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.1-5
- Require pygtk2-libglade (#1015971).
- Add a few BR for existing dependencies.

* Fri Sep 27 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.1-4
- Merge and install AppData file.

* Tue Aug 27 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.1-3
- Update scriptlet sections with current recipes.
- Drop the minimum errata version for gstreamer-plugins-good for F15/16/17.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1.

* Tue Apr  2 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.0-1
- Upgrade to 2.1.0. This merges most of the patches since 2.0.4, but some
  parts have been rewritten/reconstructed and need to be checked for
  regression.

* Mon Mar  4 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-24
- Fix a corner-case traceback upon cancelling tag reading.

* Sat Mar  2 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-23
- Fix set_row_progress "could not find tree path" (#915419).

* Tue Feb 26 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-22
- Merge new code from master for progress-per-file indication.

* Mon Feb 25 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-21
- Ignore aborted tasks in task_finished.
- Log correct number of tasks in queue.
- Reset progress-per-file indicators at (re)start of conversion.
- Fix missing progress-per-file indicators for Ogg, so at least
  if the file is done that gets displayed.

* Sun Feb 24 2013 Michael Schwendt <mschwendt@fedoraproject.org>
- 2.0.4-20
- Restart tag reading after GStreamer plug-in installation.
- 2.0.4-19
- Make "Cancel" also end the wait-for-tagreaders loop, since the async
  events for plugin installation are problematic.

* Fri Feb 22 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-18
- Merge upstream fix for batch mode running into non-URI files
  (lp #1128080).

* Mon Feb 18 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-17
- Add more fixes for success/failure of GStreamer plug-in installation,
  which makes it possible to fix the idle callback race between reading of
  tags and start of conversion.
- Merge all applied patches into a single file to avoid incremental
  patching in places where 2.0.5-pre currently differs a lot but fails.

* Sun Feb 17 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-16
- Fix tracebacks upon successfully installing a missing GStreamer plugin.

* Wed Feb 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-15
- Fix "Remove" to use gtk.TreeModelSort.convert_path_to_child_path

* Wed Feb 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-14
- Disable "Remove" temporarily, since it's completely broken.
- Fix GtkWarning about drag-data-received.

* Wed Feb 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-13
- Disable "GNOME Audio Profile" encoder, if no audio profiles are found
  (#910613).
- If GStreamer plug-in installation is aborted, don't add the file to
  the converter task queue.

* Sun Feb 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-12
- Forward exceptions from TagReader callback to main converter loop.
- Fedora >= 19: Drop ancient "fedora" vendor prefix and X-Fedora category
  from desktop file.

* Sun Feb 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-11
- Pull the TagReader patch, since it's problematic for unknown file types.

* Sun Feb 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-10
- Change GStreamer pipeline usage of audioresample and audioconvert,
  so conversion from FLAC and AIFF works.

* Sun Feb 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-9
- Fix aborted task queue.
- Fix race condition between tags_read() and converter.start() (#909681).
- Fix gstreamer.py show_error tracebacks.

* Mon Dec 10 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-8
- Merge fix for accessing files in filesystem root dir (lp #1087901).

* Sat Dec  1 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-7
- Patch further to also fix the last used folder for the "Add Folder" button.
- Patch for gnome bz #683708 and lp #1063724 GtkFileChooser problem.

* Sat Dec  1 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-4
- Work around folder choose issue (lp #1063724) where the folder is reset
  to the last-used-folder because nothing is selected/highlighted.

* Mon Nov 12 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-2
- Catch IOError when logging to stderr, which prevents crash
  in "no space left on device" condition (#874466).

* Thu Oct 18 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-1
- Updated to 2.0.4 (merged patches, further fixes and updated translations).

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.3-5
- Fix another last-used-folder "None" crash. (#836338)

* Thu May 10 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.3-4
- Apply newer post-2.0.3 batch mode fixes from upstream scm.
  This should also fix WAV batch encoding.

* Sat May  5 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.3-3
- Fix FLAC batch encoding (lp 995862).
- Fix -m and -s (lp 988262).
- Apply post-2.0.3 batch mode fixes from upstream scm. This involves
  copying the new batch.py file manually (temporarily).

* Tue Apr 24 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.3-2
- Update to 2.0.3 (stability/progress fixes and updated translations).

* Fri Apr 13 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.2-2
- Add more documentation files.

* Sun Mar 18 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 (31k diff, one bug-fix, mostly i18n/spelling fixes).

* Thu Feb  2 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (11k diff).

* Fri Jan 27 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0-1
- Update to 2.0 release (includes fix for #784413 / lp 921515).

* Fri Jan 13 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0-0.3.rc5
- Update to 2.0-rc5.

* Wed Jan  4 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0-0.2.rc4
- Rediff bad audio profiles patch (lp 911791).

* Wed Jan  4 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0-0.1.rc4
- Patch GNOME Audio Profile preferences crash (lp 911759).
- Explicitly install to libdir=/usr/lib since this is still a noarch package.
- Upgrade to 2.0-rc4 and drop merged/obsolete patches.

* Sat Dec 10 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-11
- Reenable FLAC to Ogg Vorbis conversion and require at least the
  first build of the gstreamer-plugins-good package that contains
  the backported fix.

* Sun Oct  9 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-10
- Ignore bad audio profiles (#744596) and multiple ones with no description.
- Remove %%defattr line.

* Fri Aug 19 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-9
- Enhance the previous patch, and consider the case when preferences
  are changed after creating a list of input files. Also remove rejected
  FLAC files from an internal filelist, so readding them will display the
  warning dialog again.

* Fri Aug 19 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-8
- Block conversion of FLAC to Ogg Vorbis due to GStreamer stream
  corruption (GNOME bz 651615).
- Make "Clear" button really clear internal filelist (lp 784918).

* Mon Jul  4 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-7
- Add (currently redundant) dependency on gnome-python2-gnomevfs, which
  is required by gnome-python2-gnome already, but Soundconverter imports
  the gnomevfs module directly.

* Mon Jul  4 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-6
- Add dependency on gnome-python2-canvas, which is a missing dep
  somewhere and causes a crash on non-GNOME installations (#718791).
  Probably related to the similar issue mentioned on March 22nd.

* Sat Jul  2 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-5
- Fix crash in markup_escape (calling glib markup_escape_text)
  caused by file names with invalid encodings (#718334).

* Tue Jun 21 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-4
- Fix crash when GNOME Audio Profile description changes translation (#714454).

* Tue Mar 22 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-3
- Add dependency on gnome-python2-bonobo, which is a missing dep of
  gnome-python2-gnome (#689836) and causes a crash if not installed,
  e.g. on LXDE #688780.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan  9 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.4-1
- Upgrade to 1.5.4.

* Thu Dec 16 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-8
- Add direct dependency on notify-python.

* Mon Nov 29 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-7
- Fix command-line FLAC compression default in order to avoid crash.

* Fri Nov 26 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-6
- Fix command-line options -m and -s, which have never worked,
  and -t which was broken by changes after 1.4.4.

* Wed Nov 24 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-5
- Fix command-line batch mode (#656526). Also skip conversion if input
  file name is same as output file name (as that would not have worked
  so far and would have emptied/deleted the input file instead).

* Wed Nov 17 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-4
- Fix target folder for artist/album creation when the source files are
  stored in subdirectories (#654045).

* Tue Nov 16 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-3
- Remove urllib.quote call for target folder URI, so e.g. space characters
  don't lead to creating a new unescaped target folder.

* Thu Oct 28 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-2
- Patch po files for combobox "AssertionError: model:4 widgets:5" (#647336)

* Thu Jun 17 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.3-1
- Upgrade to 1.5.3.

* Tue Jun 15 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-2
- Fix ZeroDivisionError in progress calculation.

* Tue Jun 15 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-1
- Upgrade to 1.5.2.

* Wed May 12 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4.4-2
- Update .desktop file patch.
- Minor spec adjustments in explicit deps and files section.

* Sat Jan 23 2010 Xavier Lamien <laxathom@fedoraproject.org> - 1.4.4-1
- Update release.

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.2-4
- Update desktop file according to F-12 FedoraStudio feature

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 25 2008 Denis Leroy <denis@poolshark.org> - 1.3.2-1
- Update to upstream 1.3.2
- Fixed gnome-python2 BR

* Tue May 13 2008 Denis Leroy <denis@poolshark.org> - 1.2.0-1
- Update to upstream 1.2.0

* Fri Jan 11 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-1
- Update to upstream 0.9.8, bugfix release

* Thu Aug 16 2007 Denis Leroy <denis@poolshark.org> - 0.9.7-1
- Update to 0.9.7
- Updated License tag
- Added patch to fix desktop file

* Sun Apr 29 2007 Denis Leroy <denis@poolshark.org> - 0.9.6-1
- Update to 0.9.6
- Removed some icon-related hacks, fixed upstream

* Thu Mar  1 2007 Denis Leroy <denis@poolshark.org> - 0.9.4-1
- Update to 0.9.4
- Removed taglib patch, is upstream
- Moved desktop icon into /usr/share/icons/

* Wed Nov  8 2006 Denis Leroy <denis@poolshark.org> - 0.9.3-2
- Added patch to detect missing id3v2mux gst plugin

* Thu Oct 19 2006 Denis Leroy <denis@poolshark.org> - 0.9.3-1
- Update to 0.9.3

* Tue Oct 17 2006 Denis Leroy <denis@poolshark.org> - 0.9.2-1
- Update to 0.9.2

* Fri Sep  8 2006 Denis Leroy <denis@poolshark.org> - 0.9.1-3
- Fixed desktop install

* Fri Sep  8 2006 Denis Leroy <denis@poolshark.org> - 0.9.1-2
- Added intltool BRs

* Fri Sep  8 2006 Denis Leroy <denis@poolshark.org> - 0.9.1-1
- Update to 0.9.1
- Uses gstreamer 1.0
- Some cleanup, use upstream configure and desktop

* Mon Sep  4 2006 Denis Leroy <denis@poolshark.org> - 0.8.3-2
- FE6 Rebuild

* Sun Feb 12 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.3-1
- Upstream update
- Updated to use gstreamer08

* Tue Nov 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.1-2
- Added gnome-python2-gconf to Requires (#173290)

* Mon Nov 14 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.1-1
- Upstream update

* Sun Oct  2 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.0-1
- Initial RPM release
