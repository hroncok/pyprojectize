Name: solarwolf
Version:  1.6.0
Release:  20%{?dist}.a4
Summary: A Python port of SolarFox

License: LGPL-2.0-or-later
URL: http://pygame.org/shredwheat/solarwolf
#Source0: http://pygame.org/shredwheat/solarwolf/solarwolf-%{version}.tar.gz
Source0: solarwolf-d19d830.tar.gz
Source1: solarwolf.desktop
#Patch0: solarwolf-path.patch
Patch1: solarwolf-1.6.0a4-python3.patch
BuildArchitectures: noarch
BuildRequires: desktop-file-utils python3-devel python3-setuptools
Requires: hicolor-icon-theme python3-pygame

%description
The point of the game is to scramble through 60 levels
collecting space boxes. Each level gets is harder than
the previous. Obstacles like bullets, mines, and asteroids
cover your every move. Beat the Skip timer and grab the
powerups for your only chance.

%prep
%setup -qn solarwolf-d19d830
#chmod 755 data/music
#chmod 644 data/music/*
#chmod 755 data/audio
#chmod 644 data/audio/*

#%patch0 -p0
%patch -P1 -p0
#%py3_shebang_fix .
#find . -type f -name '*.py' | xargs 2to3 -w

%build
%py3_build

%install
%py3_install
#mkdir -p  %{buildroot}%{_bindir}
#install -p -m 755 solarwolf.py %{buildroot}%{_bindir}/solarwolf

#mkdir -p  %{buildroot}%{_datadir}/solarwolf
#mkdir -p  %{buildroot}%{_datadir}/solarwolf/data
#cp -ra data/* %{buildroot}%{_datadir}/solarwolf/data

#mkdir -p  %{buildroot}%{_datadir}/solarwolf/code
#install -p -m 644 code/* %{buildroot}%{_datadir}/solarwolf/code

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 dist/solarwolf.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps


%files
%{_bindir}/solarwolf
#%{_datadir}/solarwolf/
%{python3_sitelib}/solarwolf/
%{python3_sitelib}/solarwolf-*.egg-info/
%license lgpl.txt
%doc README.rst
%{_datadir}/applications/solarwolf.desktop
%{_datadir}/icons/hicolor/64x64/apps/solarwolf.png

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-20.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.0-19.a4
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-18.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-17.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.0-16.a4
- Rebuilt for Python 3.12

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-15.a4
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-13.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.0-12.a4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-10.a4
- Don't own /usr/lib/python3.X/site-packages

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.0-8.a4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-5.a4
- BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4.a4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2.a4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-1.a4
- Rebuilt for Python 3.8

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-0.a4
- Python 3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.5-19
- Fix shebang handling.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5-16
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-15
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.5-8
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 21 2007 Jon Ciesla <limb@jcomserv.net> - 1.5-2
- Fixed Source URL.
- Switched from mv to cp for timestamps.
- Moved permission correction to prep.

* Fri Sep 14 2007 Jon Ciesla <limb@jcomserv.net> - 1.5-1
- create.
