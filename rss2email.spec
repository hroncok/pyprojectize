Name:           rss2email
Version:        3.14
Release:        10%{?dist}
Summary:        Deliver news from RSS feeds to your SMTP server as text or HTML mail

# Automatically converted from old format: GPLv2+ or GPLv3+ - review is highly recommended.
License:        GPL-2.0-or-later OR GPL-3.0-or-later
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
# Migration tool (rss2email 2.x to rss2email 3.x) from https://github.com/emillon/rss2email-debian
Source1:        r2e-migrate
Source2:        r2e-migrate.1
Source3:        README.migrate
Patch1:         rss2email-3.14-remove-special-bytes.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-feedparser >= 6.0.5
BuildRequires:  python3-html2text >= 2018.1.9
Recommends:     python3-beautifulsoup4
Recommends:     esmtp
# r2e-migrate
Requires:       python3-pyxdg

%description
%{name} lets you subscribe to a list of XML news feeds (RSS or Atom). It can
parse them regularly with the help of cron and send new items to you by email.

An HTML mail will be send in the default configuration to the local SMTP server.
See the manual page r2e for details on how to set up %{name}.

%package zsh-completion
Summary:        zsh-completion files for rss2email
BuildArch:      noarch
Supplements:    (rss2email and zsh)
Requires:       zsh
Requires:       rss2email

%description zsh-completion
This package provides %{summary}.

%prep
%autosetup -p1

cp -p %{SOURCE3} .


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}

install -D -m 644 -p completion/r2e.zsh %{buildroot}%{_datadir}/zsh/functions/Completion/Unix/_r2e

install -D -m 644 -p r2e.1 %{buildroot}%{_mandir}/man1/r2e.1

install -D -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/r2e-migrate
install -D -m 644 -p %{SOURCE2} %{buildroot}%{_mandir}/man1/r2e-migrate.1


%check
PATH="${PATH}:%{buildroot}%{_bindir}" PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} ./test/test.py


%files -f %{pyproject_files}
%license COPYING
%doc AUTHORS CHANGELOG README.rst README.migrate
%{_bindir}/r2e
%{_bindir}/r2e-migrate
%{_mandir}/man1/r2e.1*
%{_mandir}/man1/r2e-migrate.1*

%files zsh-completion
%{_datadir}/zsh/functions/Completion/Unix/_r2e

%changelog
* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.14-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 David Kaufmann <astra@ionic.at> - 3.14-8
- Remove special characters from Testcase

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.14-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.14-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 27 2022 David Kaufmann <astra@ionic.at> - 3.14-1
- Update to 3.14

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 David Kaufmann <astra@ionic.at> - 3.13.1-1
- Update to 3.13.1

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.12.3-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.12.3-2
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.12.3-1
- Update to 3.12.3 (#1941090)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 David Kaufmann <astra@ionic.at> - 3.12.2-2
- Update to feedparser 6

* Tue Sep 01 2020 David Kaufmann <astra@ionic.at> - 3.12.2-1
- Update to 3.12.2
- Reference files by tag instead of commit

* Fri Aug 07 2020 David Kaufmann <astra@ionic.at> - 3.12.1-1
- Update to 3.12.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.11-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 David Kaufmann <astra@ionic.at> - 3.11-2
- Clean up spec file a bit
- Get rid of over-globbing
- Add zsh-completion subpackage

* Mon Oct 28 2019 David Kaufmann <astra@ionic.at> - 3.11-1.20191028gitb4eae44
- Add new `user-agent` attribute for configuring email User-Agent

* Mon Sep 23 2019 David Kaufmann <astra@ionic.at> - 3.10-2.20190909git9c2d407
- Enable tests
- Use automatically generated dependencies for python packages for f30+

* Mon Sep 09 2019 David Kaufmann <astra@ionic.at> - 3.10-1.20190909git9c2d407
- Update to latest git version

* Mon Aug 12 2019 David Kaufmann <astra@ionic.at> - 3.9-3.20190812git4708c4b
- Include package review recommendations

* Mon Aug 12 2019 David Kaufmann <astra@ionic.at> - 3.9-2.20190812git4708c4b
- Update to latest git version
- Fix python version name for EPEL7

* Thu Dec 28 2017 Filip Szymański <fszymanski@fedoraproject.org> - 3.9-1.20171228gite21e803
- Update to 3.9
- Major spec file cleanup

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.71-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.71-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.71-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar  4 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.71-5
- Add a few patches from Debian package:
  0003-Setup-the-correct-version-number-in-rss2email.py.patch
  0006-Prefer-utf8-in-CHARSET_LIST.patch
  0008-Fix-encoding-of-From-and-To-headers.patch.diff
- Merge a few updates for the manual page.
- Minor spec clean-up to remove superfluous items.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 11 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.71-1
- Upgrade to 2.71.
- Fix bad tarball permissions.
- Increase minimum version in python-feedparser and python-html2text
  dependencies to match what upstream wants for this release.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.70-1
- Upgrade to 2.70.
- Update r2e wrapper script.
- Patch config.py loader (now first look in current dir like upstream,
  but if not found look for $HOME/.rss2email/config.py).
- Include config.py.example also in the documentation directory.
- Various minor spec file adjustments.

* Sun Jul 04 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.66-1
- update to 2.66, which now is shipped in a tarball

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.65-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.65-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.65-1
- update to 2.65
- recreate rss2email-use-configpy-from-homedir.patch

* Sun Oct 26 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.64-1
- update to 2.64
- drop rss2email-warn-if-problems-with-local-mta.patch, something similar now
  upstream

* Fri Jul 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.63-1
- update to 2.63 (GPLv3 now)

* Sat Jan 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.62-1
- Update to 2.62

* Fri Dec 14 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.61-1
- Update to 2.61

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Sun Mar 25 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.60-3
- Use sed instead of dos2unix
- Some small fixes from review bug #233715
- Apply one patch from Debian that should warn if there are problems with
  local delivery via sendmail

* Sat Mar 24 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.60-2
- Seperate package for html2text, as it might be useful for other stuff
  as well
- update r2e and make it possible to manage different feed files (optional,
  use r2e option "--feedext foo" to use it)
- add some common used, but-no-so-well documented configuration parameters
  to config.py template and give a hint where to find docs what they do

* Fri Mar 23 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 2.60-1
- Initial package
