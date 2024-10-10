%global modname fedmsg_meta_fedora_infrastructure

Name:               python-fedmsg-meta-fedora-infrastructure
Version:            0.31.0
Release:            14%{?dist}
Summary:            Metadata providers for Fedora Infrastructure's fedmsg deployment

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:            LicenseRef-Callaway-LGPLv2+
URL:                http://pypi.python.org/pypi/%{modname}
Source0:            http://pypi.python.org/packages/source/f/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-fedmsg
BuildRequires:      python3-fedora
BuildRequires:      python3-dateutil
BuildRequires:      python3-pytz
BuildRequires:      python3-nose
BuildRequires:      python3-pbr
BuildRequires:      python3-fasjson-client

%description
fedmsg <http://fedmsg.com> is a set of tools for knitting together
services and webapps into a realtime messaging net.  This package contains
metadata provider plugins for the primary deployment of that system:
Fedora Infrastructure <http://fedoraproject.org/wiki/Infrastructure>.

%package -n python3-fedmsg-meta-fedora-infrastructure
Summary:        Common object storage frontend

Requires:           python3-fedmsg
Requires:           python3-fedora
Requires:           python3-dateutil
Requires:           python3-pytz
Requires:           python3-fasjson-client

%description -n python3-fedmsg-meta-fedora-infrastructure
fedmsg <http://fedmsg.com> is a set of tools for knitting together
services and webapps into a realtime messaging net.  This package contains
metadata provider plugins for the primary deployment of that system:
Fedora Infrastructure <http://fedoraproject.org/wiki/Infrastructure>.

%prep
%autosetup -n %{modname}-%{version}
#-S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
FEDMSG_META_NO_NETWORK=True %{__python3} setup.py test

%files -n python3-fedmsg-meta-fedora-infrastructure -f %{pyproject_files}
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.31.0-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Maxwell G <maxwell@gtmx.me> - 0.31.0-12
- Remove unused python3-mock test dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.31.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.31.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.31.0-2
- Rebuilt for Python 3.10

* Tue Mar 23 2021 Stephen Coady <scoady@redhat.com> - 0.31.0-1
- Upgrade to 0.31.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.30.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.30.0-1
- Upgrade to 0.30.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.29.0-1
- Upgrade to 0.29.0

* Wed Aug 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.28.0-3
- Subpackage python2-fedmsg-meta-fedora-infrastructure has been removed
  See https://bugzilla.redhat.com/show_bug.cgi?id=1739922

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.28.0-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.28.0-1
- Upgrade to 0.28.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.27.0-1
- Upgrade to 0.27.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26.0-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.26.0-1
- Update to 0.26.0

* Tue May 29 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.25.0-2
- Fix the Requires in el6

* Fri May 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.25.0-1
- Update to 0.25.0

* Tue Apr 10 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.24.1-1
- Update to 0.24.1

* Mon Apr 09 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.24.0-1
- Update to 0.24.0

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.23.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.23.1-1
- Update to 0.23.1

* Tue Dec 19 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.23.0-1
- Update to 0.23.0

* Wed Oct 04 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.22.0-2
- Adjust the py2 BR and R to be on python2-fedmsg-core

* Mon Oct 02 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.22.0-1
- Update to 0.22.0

* Tue Sep 12 2017 Jeremy Cline <jeremy@jcline.org> - 0.21.0-2
- Depend on python2-fedmsg and python3-fedmsg

* Thu Aug 24 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.21.0-1
- Update to 0.21.0

* Wed Aug 16 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.20.0-2
- Just a release bump

* Wed Aug 16 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.20.0-1
- Update to 0.20.0

* Fri Aug 11 2017 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.19.0-2
- Add patch of PR#430

* Wed Aug 09 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.19.0-1
- Update to 0.19.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 0.18.0-1
- Updates to 0.18.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.17.8-1
- Update to 0.17.8

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.7-2
- Rebuild for Python 3.6

* Fri Dec 16 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.17.7-1
- Update to 0.17.7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 14 2016 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 0.17.6-1
- new version

* Fri Jul 08 2016 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 0.17.5-1
- new version

* Thu Apr 28 2016 Ralph Bean <rbean@redhat.com> - 0.17.4-1
- new version

* Thu Apr 28 2016 Ralph Bean <rbean@redhat.com> - 0.17.3-2
- Enable python3 subpackage.

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 0.17.3-1
- new version

* Fri Mar 11 2016 Ralph Bean <rbean@redhat.com> - 0.15.11-1
- new version

* Wed Mar 02 2016 Ralph Bean <rbean@redhat.com> - 0.15.10-1
- new version

* Tue Mar 01 2016 Ralph Bean <rbean@redhat.com> - 0.15.9-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Ralph Bean <rbean@redhat.com> - 0.15.8-1
- new version

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.15.7-1
- new version

* Wed Dec 16 2015 Ralph Bean <rbean@redhat.com> - 0.15.6-1
- new version

* Tue Nov 17 2015 Ralph Bean <rbean@redhat.com> - 0.15.5-7
- Remove those manual requires/obsoletes, since the epel macros should work
  now.

* Mon Nov 16 2015 Ralph Bean <rbean@redhat.com> - 0.15.5-6
- Fix broken Requires on pytz.

* Mon Nov 16 2015 Ralph Bean <rbean@redhat.com> - 0.15.5-5
- Add an Obsoletes to go with that Provides.

* Mon Nov 16 2015 Ralph Bean <rbean@redhat.com> - 0.15.5-4
- Fiddle with Provides statement.

* Mon Nov 16 2015 Ralph Bean <rbean@redhat.com> - 0.15.5-3
- Explicit provides for EPEL.

* Sun Nov 15 2015 Ralph Bean <rbean@redhat.com> - 0.15.5-2
- Added stubs for python3 subpackage and modernized python macros.

* Sun Nov 15 2015 Ralph Bean <rbean@redhat.com> - 0.15.5-1
- new version

* Mon Oct 12 2015 Ralph Bean <rbean@redhat.com> - 0.15.4-1
- new version

* Fri Oct 09 2015 Ralph Bean <rbean@redhat.com> - 0.15.3-1
- new version

* Wed Sep 23 2015 Ralph Bean <rbean@redhat.com> - 0.15.2-1
- new version

* Wed Aug 26 2015 Ralph Bean <rbean@redhat.com> - 0.15.1-1
- new version

* Wed Aug 19 2015 Ralph Bean <rbean@redhat.com> - 0.15.0-1
- new version

* Fri Jul 10 2015 Ralph Bean <rbean@redhat.com> - 0.5.11-1
- new version

* Wed Jul 08 2015 Ralph Bean <rbean@redhat.com> - 0.5.10-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Ralph Bean <rbean@redhat.com> - 0.5.9-1
- new version

* Thu Jun 11 2015 Ralph Bean <rbean@redhat.com> - 0.5.8-1
- new version

* Tue Jun 02 2015 Ralph Bean <rbean@redhat.com> - 0.5.7-1
- new version

* Mon Jun 01 2015 Ralph Bean <rbean@redhat.com> - 0.5.6-1
- new version

* Tue May 12 2015 Ralph Bean <rbean@redhat.com> - 0.5.5-1
- new version

* Tue May 05 2015 Ralph Bean <rbean@redhat.com> - 0.5.3-1
- new version

* Tue Apr 28 2015 Ralph Bean <rbean@redhat.com> - 0.5.2-1
- new version

* Thu Apr 23 2015 Ralph Bean <rbean@redhat.com> - 0.5.1-1
- new version

* Thu Apr 23 2015 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- new version

* Tue Mar 31 2015 Ralph Bean <rbean@redhat.com> - 0.4.11-1
- new version

* Mon Mar 30 2015 Ralph Bean <rbean@redhat.com> - 0.4.10-1
- new version

* Mon Mar 30 2015 Ralph Bean <rbean@redhat.com> - 0.4.9-1
- new version

* Mon Mar 30 2015 Ralph Bean <rbean@redhat.com> - 0.4.8-1
- new version

* Tue Mar 24 2015 Ralph Bean <rbean@redhat.com> - 0.4.7-1
- new version

* Fri Mar 20 2015 Ralph Bean <rbean@redhat.com> - 0.4.6-1
- new version

* Tue Mar 17 2015 Ralph Bean <rbean@redhat.com> - 0.4.5-1
- new version

* Mon Mar 16 2015 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- new version

* Tue Feb 24 2015 Ralph Bean <rbean@redhat.com> - 0.4.3-1
- new version

* Tue Feb 24 2015 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- new version

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- new version

* Tue Feb 10 2015 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- new version

* Tue Feb 10 2015 Ralph Bean <rbean@redhat.com> - 0.3.12-2
- Disable tests for now since they require the latest fedmsg.

* Wed Jan 28 2015 Ralph Bean <rbean@redhat.com> - 0.3.12-1
- Handle new sigul messages.

* Mon Jan 26 2015 Ralph Bean <rbean@redhat.com> - 0.3.11-1
- Bugfix for new pkgdb messages.

* Thu Jan 15 2015 Ralph Bean <rbean@redhat.com> - 0.3.10-1
- Handle a new message from the-new-hotness.
- Change the way usernames are returned from pkgdb messages.

* Fri Dec 12 2014 Ralph Bean <rbean@redhat.com> - 0.3.8-1
- Fixes to anitya messages (new distro.delete message).

* Sat Dec 06 2014 Ralph Bean <rbean@redhat.com> - 0.3.7-1
- New mirrormanager2 processor.
- Bugfix to the fedimg processor.
- Be able to distinguish between some prod and stg messages.

* Fri Nov 21 2014 Ralph Bean <rbean@redhat.com> - 0.3.6-1
- Latest upstream with some bugfixes.
- Disable network test with patch.

* Thu Oct 09 2014 Ralph Bean <rbean@redhat.com> - 0.3.5-1
- Further fixes to anitya.

* Wed Oct 08 2014 Ralph Bean <rbean@redhat.com> - 0.3.4-1
- Fixes to pkgdb and anitya processors.

* Fri Oct 03 2014 Ralph Bean <rbean@redhat.com> - 0.3.3-1
- New koschei and anitya processors.

* Mon Sep 29 2014 Ralph Bean <rbean@redhat.com> - 0.3.2-1
- Latest upstream.
- Handle different types of legacy messages.
- git messages now return the full patch via a call to msg2long_form.
- future-proofing against new types of bugzilla messages.

* Thu Aug 28 2014 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- Latest upstream with the new conglomerator api.
- Also, fixes to copr messages.
- New threading lock put around fas cache regeneration.
- Bump up the BR version on fedmsg.

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 0.2.19-1
- Latest upstream with jenkins and pkgdb fixes.
- Remove patches.

* Wed Aug 13 2014 Ralph Bean <rbean@redhat.com> - 0.2.18-3
- Upstream patches to fix further problems with the jenkins processor.

* Sun Aug 10 2014 Ralph Bean <rbean@redhat.com> - 0.2.18-2
- Patch out time-sensitive test.

* Sat Aug 09 2014 Ralph Bean <rbean@redhat.com> - 0.2.18-1
- Fix test suite.

* Sat Aug 09 2014 Ralph Bean <rbean@redhat.com> - 0.2.17-1
- Bugfixes to jenkins messages.

* Sat Aug 09 2014 Ralph Bean <rbean@redhat.com> - 0.2.16-1
- Remove patch.
- Handle fedora college messages.

* Fri Jul 11 2014 Ralph Bean <rbean@redhat.com> - 0.2.15-2
- Patch to handle github edge case.

* Thu Jul 10 2014 Ralph Bean <rbean@redhat.com> - 0.2.15-1
- New kerneltest processor
- Fixes to pkgdb, coprs, elections, github, and releng.

* Thu Jun 19 2014 Ralph Bean <rbean@redhat.com> - 0.2.14-1
- Updates to the github processor.
- New fedimg cloudy releng processor from David Gay.
- Switch to libravatar full-time.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Ralph Bean <rbean@redhat.com> - 0.2.13-1
- More fixes for pkgdb2.
- New fmn.web message processor.

* Fri May 16 2014 Ralph Bean <rbean@redhat.com> - 0.2.12-1
- Fixes for pkgdb.
- New icons for copr and meetbot.
- Fixes to supybot topic changes.

* Tue Mar 25 2014 Ralph Bean <rbean@redhat.com> - 0.2.11-1
- New github processor.
- New ftpsync processor.
- Require latest fedmsg to manage conflict between git and github procs.

* Thu Feb 27 2014 Ralph Bean <rbean@redhat.com> - 0.2.10-1
- Fixes to the icons for many processors.

* Fri Feb 21 2014 Ralph Bean <rbean@redhat.com> - 0.2.9-1
- Latest upstream with jenkins processor.
- Links are added to summershum processor.
- Bugfix to handle legacy bodhi messages in ancient datanommer history.

* Wed Feb 19 2014 Ralph Bean <rbean@redhat.com> - 0.2.8-1
- Latest upstream with summershum processor.

* Thu Feb 13 2014 Ralph Bean <rbean@redhat.com> - 0.2.7-1
- Bugfix to that last release.

* Thu Feb 13 2014 Ralph Bean <rbean@redhat.com> - 0.2.6-1
- Latest upstream.
- Handle secondary koji instances.
- Other bugfixes

* Fri Jan 10 2014 Ralph Bean <rbean@redhat.com> - 0.2.5-1
- Latest upstream.
- Compose processor supports epelbeta7
- Support for cnucnuweb.
- Support for koji scratch builds.

* Tue Nov 12 2013 Ralph Bean <rbean@redhat.com> - 0.2.4-1
- Latest upstream.
- Support new COPR messages.
- Make git icons square.
- Handle the new fedora badges login message.

* Tue Oct 22 2013 Ralph Bean <rbean@redhat.com> - 0.2.3-4
- Disable tests on el6 for now.

* Tue Oct 22 2013 Ralph Bean <rbean@redhat.com> - 0.2.3-3
- Fix conditional for el6 deps, rhbz #1022222.

* Thu Oct 17 2013 Ralph Bean <rbean@redhat.com> - 0.2.3-2
- Reenable the test suite now that fedmsg has caught up.
- Patch out the failing avatar test.
- Add dep on python-dateutil

* Tue Oct 01 2013 Ralph Bean <rbean@redhat.com> - 0.2.3-1
- Latest upstream with pkgdb2 and fedocal.

* Fri Sep 27 2013 Ralph Bean <rbean@redhat.com> - 0.2.2-1
- Latest upstream with new processor for nuancier.

* Wed Sep 04 2013 Ralph Bean <rbean@redhat.com> - 0.2.1-1
- Latest upstream with bugfixes and a few more message types.
- Temporarily disable the test suite while fedmsg catches up.

* Tue Aug 06 2013 Ralph Bean <rbean@redhat.com> - 0.1.9-2
- Remove old patches.

* Tue Aug 06 2013 Ralph Bean <rbean@redhat.com> - 0.1.9-1
- Added ansible processor.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Ralph Bean <rbean@redhat.com> - 0.1.8-1
- Add possibility of caching fas data for irc nicks.
- Fix the mediawiki subtitle.
- Use users username for badge links (instead of the integer id).

* Tue Jun 18 2013 Ralph Bean <rbean@redhat.com> - 0.1.7-1
- Added badges processors for fedbadges backend.

* Thu Jun 06 2013 Ralph Bean <rbean@redhat.com> - 0.1.6-2
- Removed an old unneeded patch.

* Thu Jun 06 2013 Ralph Bean <rbean@redhat.com> - 0.1.6-1
- Fix the planet processor name.
- Add mailman3 processor for the future.

* Mon May 13 2013 Ralph Bean <rbean@redhat.com> - 0.1.5-2
- Patch: don't declare tickets closed unless that value actually changes.

* Mon May 13 2013 Ralph Bean <rbean@redhat.com> - 0.1.5-1
- New upstream with new avatars and emails interfaces.
- New dep on python-fedora
- Temporarily remove test for avatars while python-fedora catches up.
- New processor for fedorahosted/trac messages.

* Wed Apr 24 2013 Ralph Bean <rbean@redhat.com> - 0.1.4-1
- Handle the latest tagger2 messages.

* Wed Apr 24 2013 Ralph Bean <rbean@redhat.com> - 0.1.3-1
- Docstrings for tests for self-documentation of the /topics/ doc.
- Cleanup some koji and compose messages.
- Random typo and bug fixes.

* Mon Mar 11 2013 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- More meetbot message types
- Handle secondary arch compose messages.
- Handle koji package list changes
- Give up on askbot deep linking.  It is hard.
- Use non-https cgit urls.
- Use non-https planet urls.
- Better debug of unhandled messages.

* Fri Feb 08 2013 Ralph Bean <rbean@redhat.com> - 0.1.0-1
- Fine tuning of some messages and links.
- Correct __name__ for KojiProcessor.

* Fri Feb 01 2013 Ralph Bean <rbean@redhat.com> - 0.0.9-1
- Support usernames and links for koji messages.
- Support new and old-style fas message bodies.

* Thu Jan 31 2013 Ralph Bean <rbean@redhat.com> - 0.0.8-1
- Latest upstream.  New planet and buildsys (koji) message types.

* Mon Jan 21 2013 Ralph Bean <rbean@redhat.com> - 0.0.7-1
- Latest upstream, yet more changes to git/scm messages.

* Sat Jan 19 2013 Ralph Bean <rbean@redhat.com> - 0.0.6-1
- Latest upstream, more changes to git/scm messages.

* Wed Jan 16 2013 Ralph Bean <rbean@redhat.com> - 0.0.5-1
- Latest upstream, changes to git/scm messages.

* Mon Jan 07 2013 Ralph Bean <rbean@redhat.com> - 0.0.4-1
- Latest upstream, now with pkgdb messages.

* Tue Nov 27 2012 Ralph Bean <rbean@redhat.com> - 0.0.3-1
- Initial package for Fedora
