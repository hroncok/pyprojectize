Name:           wxGlade
Version:        1.0.5
Release:        7%{?dist}
Summary:        A wxWidgets/wxPython/wxPerl GUI designer
License:        MIT
URL:            http://wxglade.sourceforge.net
Source0:        https://downloads.sourceforge.net/project/wxglade/wxglade/%{version}/%{name}-%{version}.zip
Source1:        wxglade.desktop
Source2:        wxglade.png
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
Requires:       python3-wxpython4

%description
wxGlade is a GUI designer written in Python with the popular GUI
toolkit wxPython, that helps you create wxWidgets/wxPython user
interfaces. At the moment it can generate Python, C++, Perl and XRC
(wxWidgets' XML resources) code.

Starting from version 0.7.0, wxGlade requires wxPython >= 2.8 and Python >= 2.4
and <= 2.7.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Let's handle licenses by ourselves.
rm -frv %{buildroot}%{_docdir}/wxglade/LICENSE.txt

# Install desktop related entries
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
install -pm 755 -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -pm 644 %{S:2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%{_docdir}/wxglade/
%license LICENSE.txt
%{_bindir}/wxglade*
%{_datadir}/icons/hicolor/*x*/apps/*
%{_datadir}/applications/*
%{_datadir}/wxglade
%{python3_sitelib}/wxglade/
%{python3_sitelib}/%{name}-%{version}.dist-info

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.5-6
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 14 2023 Sérgio Basto <sergio@serjux.com> - 1.0.5-4
- Rebuild for wxGTK update seems fixes the problem

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.5-2
- Rebuilt for Python 3.12

* Wed Apr 26 2023 Scott Talbert <swt@techie.net> - 1.0.5-1
- Update to new upstream release 1.0.5 (#2183890)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 Scott Talbert <swt@techie.net> - 1.0.4-5
- Fix startup script on Python 3.10+ (#2136512)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Sérgio Basto <sergio@serjux.com> - 1.0.4-1
- Update wxGlade to 1.0.4 (#2036474)

* Sun Nov 14 2021 Sérgio Basto <sergio@serjux.com> - 1.0.3-1
- Update wxGlade to 1.0.3 (#2023018)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.10

* Sat May 08 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (#1958537)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Scott Talbert <swt@techie.net> - 1.0.1-1
- Update to new upstream release 1.0.1 (#1911834)

* Mon Dec 21 2020 Scott Talbert <swt@techie.net> - 1.0.0-1
- Update to new upstream release 1.0.0 (#1846938)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Scott Talbert <swt@techie.net> - 0.9.4-3
- Update to new upstream release 0.9.5 (#1794942)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Scott Talbert <swt@techie.net> - 0.9.4-1
- Update to new upstream release 0.9.4 (#1747087)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Scott Talbert <swt@techie.net> - 0.9.3-1
- New upstream release 0.9.3

* Fri Mar 22 2019 Scott Talbert <swt@techie.net> - 0.9.2-1
- New upstream release 0.9.2

* Thu Feb 07 2019 Scott Talbert <swt@techie.net> - 0.9.1-1
- New upstream release 0.9.1

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Scott Talbert <swt@techie.net> - 0.9.0-1
- New upstream release 0.9.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-2
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Scott Talbert <swt@techie.net> - 0.8.3-1
- New upstream release 0.8.3 (#1514291)
- Switch to Python 3 and wxPython 4 (#1549045)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-5
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 12 2016 Sérgio Basto <sergio@serjux.com> - 0.7.2-1
- Update wxGlade to 0.7.2 .
- Fix URL of Source0 .
- Better document dir handling .

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 21 2015 Christopher Meng <rpm@cicku.me> - 0.7.0-1
- Update to 0.7.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 11 2013 Christopher Meng <rpm@cicku.me> - 0.6.8-1
- New version(BZ#1006631) with major cleanup/rewrite.
- Fix unversioned docdir issue(BZ#993886).
- Fix old version bug(BZ#948782).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.6.3tip20100625-6
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.3tip20100625-2
- recompiling .py files against Python 2.7 (rhbz#623417)

* Fri Jun  25 2010 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3tip20100625-1
- update to tip20100625

* Sun Jun  6 2010 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3tip20091130-2
- update source

* Mon Nov 30 2009 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3tip20091130-1
- update to tip version

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 24 2008 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3-2
- update to 0.6.3

* Sat Nov 24 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.6.1-1
- update to 0.6.1
- remove docs path patch, add a docs symlink instead

* Thu Jul 19 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-6
- 248795 , patch for launch help docs correctly

* Mon Apr 16 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-5
- update to fix EVR problem

* Sun Apr 15 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-2
- file permissions with install command

* Sun Apr 15 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-1
- update to 0.5
- launch script with quoted $@
- name to wxGlade

* Tue Feb 27 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-3
- Desktop entry do not need version number
- remove some comments

* Sun Feb 25 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-2
- install icon to hicolor directory
- change name to wxglade
- BuildRequires desktop-file-utils
- remove Application category in desktop file
- remove some macro redefination

* Fri Feb 16 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-2
- Add missing icons

* Fri Feb 16 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-1
- update to 0.4.1

* Wed Oct 27 2004 Alberto Griggio <agriggio@users.sf.net> 0.3.5-1
- Updated to version 0.3.5

* Wed Mar 10 2004 Alberto Griggio <agriggio@users.sf.net> 0.3.4-1
- Updated to version 0.3.4

* Wed Mar 10 2004 Alberto Griggio <albgrig@tiscalinet.it> 0.3.2-1
- Updated to version 0.3.2

* Tue Sep 02 2003 Alberto Griggio <albgrig@tiscalinet.it> 0.3.1-1
- Updated to version 0.3.1

* Fri Aug 29 2003 Robin Dunn <robind@alldunn.com> 0.3-5
- Initial version
