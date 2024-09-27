Name:           nfoview
Version:        1.28.1
Release:        12%{?dist}
Summary:        Viewer for NFO files

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://otsaloma.io/nfoview/
Source0:        https://github.com/otsaloma/nfoview/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib

Requires:       shared-mime-info
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       terminus-fonts

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a
text editor are preset font and encoding settings, automatic window
size and clickable hyperlinks.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
desktop-file-install                                        \
    --add-category="TextTools;"                             \
    --remove-category="Viewer;"                             \
    --delete-original                                       \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{buildroot}%{_datadir}/applications/io.otsaloma.nfoview.desktop
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.otsaloma.nfoview.appdata.xml

%files -f %{name}.lang
%doc AUTHORS.md NEWS.md README.md
%license COPYING
%{_mandir}/man*/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/io.otsaloma.nfoview.appdata.xml
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.dist-info
%{_datadir}/applications/io.otsaloma.nfoview.desktop
%{_datadir}/icons/hicolor/*/apps/io.otsaloma.nfoview*

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.1-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 1.28.1-10
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.28.1-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.28.1-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.28.1-1
- Update to latest upstream release 1.28.1 (closes rhbz#2011649)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.28-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.28-2
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.27.1-1
- remove conditional for Fedora 11
- Update to latest upstream release 1.28 (rhbz#1829183)

* Wed Apr 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.27.1-1
- Update to latest upstream release 1.27.1 (rhbz#1822994)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.27-5
- Update URL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.27-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.27-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.27-1
- Update to latest upstream release 1.27 (rhbz#1742648)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.26.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.26.1-3
- Update to latest upstream release 1.26.1 (rhbz#1718557)

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.26-3
- Update specfile

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.26-1
- Update to new upstream version 1.26

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.24-2
- Rebuilt for Python 3.7

* Sun May 20 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.24-1
- Update to new upstream version 1.24 (rhbz#1570794)

* Thu Mar 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.23-2
- appdata.xml was move inside the source

* Fri Feb 16 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.23-1
- Update to new upstream version 1.23 (rhbz#1504377)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.22-1
- Update to new upstream version 1.22 (rhbz#1433547)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.21-2
- Rebuild for Python 3.6

* Tue Nov 01 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.21-1
- Update to new upstream version 1.21 (rhbz#1389960)

* Wed Aug 03 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.20-1
- Update to new upstream version 1.20 (rhbz#1359444)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.19-1
- Update to new upstream version 1.19 (rhbz#1336067)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.18-1
- Update to new upstream version 1.18 (rhbz#1301311)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Oct 15 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.17-1
- Update to new upstream version 1.17 (rhbz#1270576)

* Sat Aug 01 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.16-1
- Update to new upstream version 1.16 (rhbz#1243832)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.15.1-1
- Update to new upstream version 1.15.1 (rhbz#1170996)

* Wed Oct 08 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.15-1
- Update to new upstream version 1.15 (rhbz#1150496)

* Sun Jun 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-1
- Update to new upstream version 1.14

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Sep 23 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.13.1-1
- Update to new upstream version 1.13.1

* Wed Jul 31 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.13-1
- Update to new upstream version 1.13

* Tue Apr 16 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.12.1-1
- Update to new upstream version 1.12.1

* Tue Apr 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-1
- Update to new upstream version 1.12

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.11-1
- Update to new upstream version 1.11

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.10-5
- Rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Conrad Meyer <konrad@tylerc.org> - 1.10-2
- Add missing Requires on python3-gobject (#765643)

* Sun Nov 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-1
- Update BRs update
- Update to new upstream version 1.10

* Thu Jun 02 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.5-1
- Update to new upstream version 1.9.5

* Wed Apr 06 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.4-1
- Update to new upstream version 1.9.4

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.3-1
- Update to new upstream version 1.9.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.2-1
- Update to new upstream version 1.9.2

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 26 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.9.1-1
- Update to 1.9.1
- Require shared-mime-info

* Sun Oct 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.8-1
- Update to new upstream version 1.8
- The icons need now hicolor-icon-theme

* Tue Sep 29 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-1
- Update to new upstream version 1.7

* Thu Sep 17 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-1
- Update to new upstream version 1.6

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.5-3
- Use bzipped upstream tarball

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.5-1
- Update to 1.5
- Fix conditional comparison that caused broken deps in Fedora 9

* Sat May 02 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-3
- Small changes around the desktop file

* Sat Apr 25 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-2
- Remove PKG-INFO from doc
- Fix requiements
- Add update-desktop-database
- Fix category for the .desktop file
- Add patch for German translation

* Sun Apr 19 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1
- Initial package for Fedora
