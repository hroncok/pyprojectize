Name: slingshot
Version:  0.9
Release:  25%{?dist}
Summary: A Newtonian strategy game

License: GPL-2.0-or-later        
URL: https://github.com/ryanakca/slingshot
Source0: https://github.com/ryanakca/slingshot/archive/%{version}/slingshot-%{version}.tar.gz
Source1: slingshot.desktop
Source2: slingshot.appdata.xml
# Port to Python 3
Patch0: 243aef95dde390f97f1e0abbbdb646b3e5b97f7d.patch
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: python3-devel
Requires: gnu-free-sans-fonts
Requires: hicolor-icon-theme
Requires: python3-pygame

%description
Slingshot is a two dimensional, turn based simulation-strategy game 
set in the gravity fields of several planets. It is a highly 
addictive game, and never the same from round to round due to its 
randomly generated playing fields.

%prep
%setup -q
%patch -P0 -p1

rm -f src/slingshot/data/FreeSansBold.ttf

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

rm -rf $RPM_BUILD_ROOT/slingshot
rm -rf $RPM_BUILD_ROOT/home
rm -rf $RPM_BUILD_ROOT/builddir

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mv src/slingshot/data/icon64x64.png src/slingshot/data/slingshot.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 src/slingshot/data/slingshot.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

#install appdata
mkdir -p $RPM_BUILD_ROOT/%{_metainfodir}
install -p -m 664 %{SOURCE2} $RPM_BUILD_ROOT/%{_metainfodir}
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_metainfodir}/*.appdata.xml

#Link to font
ln -s %{_datadir}/fonts/gnu-free/FreeSansBold.ttf $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/data/FreeSansBold.ttf

%files -f %{pyproject_files}
%{_bindir}/slingshot
%doc README
%license LICENSE
%{_datadir}/applications/slingshot.desktop
%{_datadir}/icons/hicolor/64x64/apps/slingshot.png
%{_datadir}/pixmaps/slingshot.xpm
%{_metainfodir}/slingshot.appdata.xml

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9-24
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9-21
- Rebuilt for Python 3.12

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.9-20
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9-17
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9-12
- Patch to convert to Python 3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9-6
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 02 2016 Jon Ciesla <limburgher@gmail.com> - 0.9-1
- New upstream, BZ 1295114

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.1p-11
- Fix URL, BZ 1023983.
- Add appdata file, BZ 1023986.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.1p-9
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Jon Ciesla <limb@jcomserv.net> - 0.8.1p-5
- Fix for crash, BZ 652244.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Jon Ciesla <limb@jcomserv.net> - 0.8.1p-3
- Update for freefont->gnu-free-fonts rename/split.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1p-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 06 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.1p-1
- create.
