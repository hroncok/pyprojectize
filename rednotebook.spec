Name: rednotebook
Version: 2.29.6
Release: 7%{?dist}
Summary: Daily journal with calendar, templates and keyword searching
License: GPL-2.0-or-later

URL: http://rednotebook.sourceforge.net

Source0: https://github.com/jendrikseipp/rednotebook/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: gettext
BuildRequires: python3-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: python-setuptools
%else
BuildRequires: python3-setuptools
%endif
BuildRequires: desktop-file-utils

Requires: python3-PyYAML
%if 0%{?fedora} >= 37
Requires: webkit2gtk4.1
%else
Requires: webkitgtk4
%endif
Requires: python3-chardet
Requires: python3-enchant
Requires: hicolor-icon-theme
Requires: gtksourceview4

%description
RedNotebook is a modern desktop journal. It lets you format, tag and
search your entries. You can also add pictures, links and customizable
templates, spell check your notes, and export to plain text, HTML,
Latex or PDF.

%prep
%autosetup

%build
%py3_build

%install
%py3_install
desktop-file-install                                    \
    --add-category="Calendar"                           \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}/%{_datadir}/appdata/
mv %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
# Be careful to not list locales twice
%dir %{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}/*.py*
%{python3_sitelib}/%{name}/external/
%{python3_sitelib}/%{name}/files/
%{python3_sitelib}/%{name}/gui/
%{python3_sitelib}/%{name}/images/
%{python3_sitelib}/%{name}/util/
%{python3_sitelib}/%{name}*.egg-info
%{python3_sitelib}/%{name}/__pycache__

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.29.6-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.29.6-2
- Rebuilt for Python 3.12

* Mon May 01 2023 Phil Wyett <philip.wyett@kathenas.org> - 2.29.6-1
- New upstream version 2.29.6.

* Wed Apr 19 2023 Phil Wyett <philip.wyett@kathenas.org> - 2.29.5-1
- New upstream version 2.29.5.

* Wed Apr 12 2023 Phil Wyett <philip.wyett@kathenas.org> - 2.29.4-1
- New upstream version 2.29.4.
- Use SPDX license identifier.
- Requires webkit2gtk4.1 where able.
- Little spec file rework.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Phil Wyett <philip.wyett@kathenas.org> - 2.29.3-1
- New upstream version 2.29.3

* Thu Jan 12 2023 Phil Wyett <philip.wyett@kathenas.org> - 2.29.1-1
- New upstream version 2.29.1

* Sat Dec 31 2022 Phil Wyett <philip.wyett@kathenas.org> - 2.29-1
- New upstream version 2.29

* Thu Dec 29 2022 Phil Wyett <philip.wyett@kathenas.org> - 2.28.1-1
- New upstream version 2.28.1

* Wed Dec 28 2022 Phil Wyett <philip.wyett@kathenas.org> - 2.28-1
- New upstream version 2.28

* Mon Dec 19 2022 Phil Wyett <philip.wyett@kathenas.org> - 2.27.2-1
- New upstream version 2.27.2

* Sun Nov 20 2022 Phil Wyett <philip.wyett@kathenas.org> - 2.27.1-1
- New upstream version 2.27.1

* Wed Sep 28 2022 Phil Wyett <philip.wyett@kathenas.org> - 2.26-1
- New upstream version 2.26

* Thu Sep 22 2022 Phil Wyett <philip.wyett@kathenas.org> - 2.25-1
- New upstream version 2.25

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.24-3
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.24-2
- Add missing requirement (closes rhbz#2058475)

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.24-1
- Update to latest upstream release 2.24

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.22-2
- Rebuilt for Python 3.10

* Fri May 28 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.22-1
- Update to new upstream version 2.22

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.21-1
- Update to new upstream version 2.21

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.20-1
- Update to new upstream release 2.20

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.19-1
- Update to latest upstream release 2.19

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.18-2
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.18-1
- Update to latest upstream release 2.18

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.17-1
- Update to latest upstream release 2.17

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.16-1
- Update to latest upstream release 2.16

* Sat Jan 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.15-2
- Update requirements (rhbz#1768788)

* Thu Dec 12 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.15-1
- Update to latest upstream release 2.15

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.11.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.11.1-1
- Update to latest upstream release 2.11.1

* Mon Mar 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.9-1
- Update to latest upstream release 2.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.8-1
- Update to latest upstream release 2.8

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.5-1
- Update to latest upstream release 2.5

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4-2
- Rebuilt for Python 3.7

* Sat Mar 17 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.4-1
- Update to latest upstream release 2.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-1
- Update to latest upstream release 2.3
- Fix requirements (rhbz#1498766, rhbz#1501182)
- Move to Python 3 (rhbz#1375797, rhbz#1482931)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-2
- Update docs

* Tue Jan 17 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-1
- Update to new upstream version 1.14 (rhbz#1403474)

* Tue Aug 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.13-1
- Update to new upstream version 1.13

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 16 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-1
- Update to new upstream version 1.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Mike DePaulo <mikedep333@fedoraproject.org> - 1.11-1
- Update to new upstream version 1.11
- Update Summary to that of 0.7.0+
- Update Description to latest

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.0-1
- Update to new upstream version 1.9.0

* Fri Oct 17 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.8.0-1
- Update to new upstream version 1.8.0

* Sat Nov 16 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.3-1
- Update to new upstream version 1.7.3

* Wed Jul 31 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.2-1
- Update to new upstream version 1.7.2

* Sat Jun 08 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.1-1
- Update to new upstream version 1.7.1

* Fri Mar 01 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Update to new upstream version 1.7.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.6-1
- Update to new upstream version 1.6.6

* Sun Jan 06 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.5-1
- Update to new upstream version 1.6.5

* Tue Dec 25 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.4-1
- Update to new upstream version 1.6.4

* Sat Dec 08 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.3-1
- Update to new upstream version 1.6.3

* Mon Nov 19 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.2-1
- Update to new upstream version 1.6.2

* Thu Nov 15 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-1
- Update to new upstream version 1.6.1

* Thu Nov 01 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Update to new upstream version 1.6.0

* Tue Aug 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-2
- Fix Requires

* Mon Aug 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to new upstream version 1.5.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to new upstream version 1.4.0

* Fri Feb 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to new upstream version 1.3.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 08 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-2
- Spec file synced with master branch

* Thu Oct 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Tue Aug 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.8-1
- Update to new upstream version 1.1.8
- List locales correctly tagged as %%lang

* Fri Jul 15 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.7-1
- Update to new upstream version 1.1.7

* Mon May 16 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.5-1
- Update to new upstream version 1.1.5

* Sun Mar 27 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Sun Mar 06 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-1
- Update to new upstream version 1.1.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.2-1
- Update to new upstream version 1.1.2

* Sun Aug 29 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to new upstream version 1.1.1

* Sat Aug 14 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Update to new upstream version 1.1.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 26 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to new upstream version 1.0.0

* Tue May 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.5-2
- Require python-chardet

* Tue May 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5

* Wed Feb 24 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Mon Feb 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Sun Jan 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1
- Require pywebkitgtk for new print preview
- Use desktop-file-install

* Fri Dec 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Thu Nov 19 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.9-2
- Update the URL after a request from the upstream maintainer

* Wed Nov 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.9-1
- Update to new upstream version 0.8.9

* Mon Nov 16 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.8-1
- Update to new upstream version 0.8.8

* Tue Sep 29 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.7-1
- Update to new upstream version 0.8.7

* Thu Sep 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6.1-1
- Update to 0.8.6.1, fixes #523880

* Thu Sep 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6-2
- Fix libglade error with GTK 2.16.6 (#523880)

* Fri Sep 04 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6-1
- Updated to new upstream version 0.8.6

* Fri Aug 14 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.5-1
- Update to new upstream version 0.8.5 (fixes #518778)

* Fri Aug 14 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.4-1
- Update to new upstream version 0.8.4

* Fri Aug 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.3-1
- Updated to new upstream version 0.8.3

* Wed Jul 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-1
- Update to new upstream version 0.8.2

* Sat Jul 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-1
- Update to new upstream version 0.8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update BR python
- Icon cache update added
- Update to new upstream version 0.8.0

* Wed Jul 15 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.6-1
- Update to new upstream version 0.7.6

* Mon Jul 06 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-1
- Remove the shebang stuff, upstream changed this
- Update to new upstream version 0.7.5

* Mon Jun 29 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.4-1
- Move the removing of the shebang to prep section
- Update to new upstream version 0.7.4

* Tue May 26 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-1
- Update to new upstream version 0.7.2

* Wed May 06 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Update to new upstream version 0.7.1

* Wed May 06 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.9-1
- Update to new upstream version 0.6.9

* Sun May 03 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.8-1
- Update to new upstream version 0.6.8

* Tue Apr 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.7-1
- Update to new upstream version 0.6.7

* Tue Apr 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.6-1
- Update to new upstream version 0.6.6

* Fri Apr 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.5-1
- Update to new upstream version 0.6.5

* Wed Mar 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Add hicolor-icon-theme as a requirement
- Add icons directory
- Update to new upstream version 0.6.2

* Sat Mar 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Update to new upstream version 0.6.1
- Rename docs, add License file

* Thu Feb 12 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.5-1
- Update to new upstream version 0.5.5

* Sat Jan 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Update to new upstream version 0.5.2

* Sat Jan 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Initial package for Fedora
