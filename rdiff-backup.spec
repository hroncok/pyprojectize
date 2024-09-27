%global gittag 2.2.6

Version: %{gittag}
Summary: Convenient and transparent local/remote incremental mirror/backup
Name: rdiff-backup
Release: 7%{?dist}

URL: https://rdiff-backup.net/
Source0: https://github.com/%{name}/%{name}/releases/download/v%{gittag}/%{name}-%{version}.tar.gz

License: GPL-2.0-or-later
BuildRequires: python3-devel >= 3.6, librsync-devel >= 1.0.0
BuildRequires: python3-setuptools_scm
BuildRequires: gcc

#recommended runtime dependencies
Recommends: py3libacl
Recommends: python3-pyxattr
Recommends: python3-psutil

%description
rdiff-backup is a script, written in Python, that backs up one
directory to another and is intended to be run periodically (nightly
from cron for instance). The target directory ends up a copy of the
source directory, but extra reverse diffs are stored in the target
directory, so you can still recover files lost some time ago. The idea
is to combine the best features of a mirror and an incremental
backup. rdiff-backup can also operate in a bandwidth efficient manner
over a pipe, like rsync. Thus you can use rdiff-backup and ssh to
securely back a hard drive up to a remote location, and only the
differences from the previous backup will be transmitted.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Remove doc files so we package them with rpmbuild
rm -rf $RPM_BUILD_ROOT/usr/share/doc/*

%files
%defattr(-,root,root)
%{_bindir}/rdiff-backup
%{_bindir}/rdiff-backup-statistics
%{_bindir}/rdiff-backup-delete
%{_mandir}/man1/rdiff-backup*
%{python3_sitearch}/rdiff_backup/
%{python3_sitearch}/rdiff_backup.dist-info
%{python3_sitearch}/rdiffbackup/
%{_datadir}/bash-completion/completions/rdiff-backup
%doc CHANGELOG.adoc README.adoc
%doc docs/credits.adoc docs/DEVELOP.adoc docs/examples.adoc
%doc docs/FAQ.adoc docs/migration.adoc
%license COPYING

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.6-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 10 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.6-3
- Rebuild for pyinstall CVE-2023-49797 BZ2253844

* Sat Sep 09 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.6-2
- Final minor release v2.2.6 - Fedora/EPEL Release
- Fix release number in spec file.

* Fri Sep 08 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.6-1
- Final minor release v2.2.6 - COPR Release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.5-3
- Rebuilt for Python 3.12

* Sun May 07 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.5-2
- Minor Fix release v2.2.5 - Fedora/EPEL Release

* Sat May 06 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.5-1
- Minor Fix release v2.2.5 - COPR Release

* Wed Mar 08 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.4-2
- Small Fix Release v2.2.4 - Fedora/EPEL Release

* Tue Feb 28 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.4-1
- Small Fix Release v2.2.4 - COPR Release

* Sun Feb 19 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.3-2
- Fix release v2.2.3 - Fedora/EPEL Release

* Sun Feb 12 2023 Frank Crawford <frank@crawford.emu.id.au> - 2.2.3-1
- Fix release v2.2.3 - COPR Release
 
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.2.2-2
- Bugfix Oops release v2.2.2 - Fedora/EPEL Release

* Thu Dec 29 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.2.2-1
- Bugfix Oops release v2.2.2 - COPR Release

* Wed Dec 28 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.2.1-1
- Bugfix release v2.2.1 - COPR Release

* Wed Dec 28 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.2.0-3
- Patch to fix issue with function in debug mode

* Tue Dec 20 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.2.0-2
- Happy Holidays release v2.2.0 - Fedora Release

* Sun Dec 18 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.2.0-1
- Happy Holidays release v2.2.0 - COPR Release

* Mon Nov 21 2022 Frank Crawford <frank@crawford.emu.id.au> - 2.0.5-10
- SPDX license update

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.5-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Frank Crawford <frank@crawford.emu.id.au> 2.0.5-6
- Added patch for Python3.11 as per BZ#2021946

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.5-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Frank Crawford <frank@crawford.emu.id.au> 2.0.5-2
- Bump to separate from COPR build

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Frank Crawford <frank@crawford.emu.id.au> 2.0.5-1
- Last bug-fix before code cleanu-up

* Thu Jul 09 2020 Frank Crawford <frank@crawford.emu.id.au> 2.0.3-5
- Bumped due to a Koji build error

* Tue Jul 07 2020 Frank Crawford <frank@crawford.emu.id.au> 2.0.3-4
- Add requirement of python3-setuptools (Ref upstream issue #305)

* Sat Jun 27 2020 Frank Crawford <frank@crawford.emu.id.au> 2.0.3-3
- Add BuildRequire python3-setuptools in addition to python3-devel
  (see https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuilt for Python 3.9

* Sat May 23 2020 Frank Crawford <frank@crawford.emu.id.au> 2.0.3-1
- Version 2.0.3 - Bugfix release

* Sun Mar 15 2020 Frank Crawford <frank@crawford.emu.id.au> 2.0.0-1
- Version 2.0.0 - ready for the future

* Sun Mar  8 2020 Frank Crawford <frank@crawford.emu.id.au> 1.9.2rc0-1
- First release candidate towards 2.0.0

* Mon Feb 24 2020 Frank Crawford <frank@crawford.emu.id.au> 1.9.1b0-1
- Third beta before 2.0.0

* Sat Feb  1 2020 Frank Crawford <frank@crawford.emu.id.au> 1.9.0b0-1
- Second beta before 2.0.0
- Make pylibacl and pyxattr recommended rather than required

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Frank Crawford <frank@crawford.emu.id.au> 1.4.0b0-1
- First beta release before 2.0.0
- Updated to Python3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Kevin Fenzi <kevin@scrye.com> - 1.2.8-30
- Clean up useless conditional. Fixes bug #1663715

* Wed Jul 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.2.8-29
- Fix FTBFS by python2 versioning all python calls.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.8-26
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 24 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.8-25
- Adjust requires for pyxattr changes.

* Sat Dec 02 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.8-24
- Add patch to ignore ENODATA when removing acls (as one might remove already a later one). Fixes bug #1494236

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.8-20
- Add patch to better handle hardlinks. Fixes bug #1409435

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-19
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Kevin Fenzi <kevin@scrye.com> - 1.2.8-17
- Fix define vs global

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Kevin Fenzi <kevin@scrye.com> 1.2.8-15
- Include examples.html as a doc file. Fixes bug #1200751

* Sun Mar 01 2015 Robert Scheck <robert@fedoraproject.org> - 1.2.8-14
- Rebuild for librsync 1.0.0 (#1126712)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Kevin Fenzi <kevin@scrye.com> 1.2.8-11
- Add patch for unversioned docdirs
- Fix changelog entries
- Drop old f9 conditional

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Mar 20 2010 Kevin Fenzi <kevin@tummy.com> - 1.2.8-4
- Add patch for cosmetic popen warning. Fixes bug #528940

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.8-2
- Add conditional for egg info file (bug 490341)

* Thu Mar 26 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.8-1
- Update to 1.2.8

* Thu Mar 12 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.7-1
- Update to 1.2.7 (bug 486426)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.5-1
- Update to 1.2.5

* Thu Jan 01 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.4-1
- Update to 1.2.4

* Mon Dec 29 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.3-1
- Update to 1.2.3
- Also fixes bug 477507

* Mon Dec 15 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.2-1
- Update to 1.2.2 (bug 476539)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.1-3
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.1-2
- Rebuild for Python 2.6

* Mon Sep 08 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.1-1
- Update to 1.2.1

* Mon Aug 11 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.0-1
- Update to 1.2.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.5-7
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Kevin Fenzi <kevin@tummy.com> 1.0.5-6
- Add egginfo file.

* Mon Aug 13 2007 Kevin Fenzi <kevin@tummy.com> 1.0.5-5
- Remove python-abi Requires

* Mon Aug 13 2007 Kevin Fenzi <kevin@tummy.com> 1.0.5-4
- Update License

* Fri Jun 15 2007 Gavin Henry <ghenry@suretecsystems.com> 1.0.5-3
- Applied patch from Marcin Zajaczkowski <mszpak ATT wp DOTT pl>
  for addition of pylibacl, pyxattr in Requires section

* Sun Dec 17 2006 Kevin Fenzi <kevin@tummy.com> - 1.0.5-2
- Rebuild for python 2.5

* Tue Dec 5  2006 Gavin Henry <ghenry@suretecsystems.com> - 0:1.0.5-1 
- Update to latest version

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.0.4-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Kevin Fenzi <kevin@tummy.com> - 1.0.4-2
- Build for fc6
- No longer need to ghost pyo files (bug 205431)

* Fri Dec 9  2005 Gavin Henry <ghenry@suretecsystems.com> - 0:1.0.4-1 
- Update to latest version

* Fri Dec 9  2005 Gavin Henry <ghenry@suretecsystems.com> - 0:1.0.3-1 
- Update to latest version

* Wed Sep 14 2005 Gavin Henry <ghenry@suretecsystems.com> - 0:1.0.1-1
- New version

* Mon Aug 15 2005 Gavin Henry <ghenry@suretecsystems.com> - 0:1.0.0-1
- Latest version

* Wed May 11 2005 Bill Nottingham <notting@redhat.com> - 0:0.12.7-3
- rebuilt

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Jan 22 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.12.7-1
- Update to 0.12.7 which was released May 31st, 2004.
- Enhance spec with python-abi and arch-dependent sitelib paths.
- Update URL and Source.

* Sun Oct 05 2003 Ben Escoto <bescoto@stanford.edu> - 0:0.12.5-0.fdr.1
- Added epochs to python versions, more concise %%defines, %%ghost files

* Sat Aug 16 2003 Ben Escoto <bescoto@stanford.edu> - 0:0.12.3-0.fdr.4
- Implemented various suggestions of Fedora QA

* Sun Nov 4 2001 Ben Escoto <bescoto@stanford.edu>
- Initial RPM
