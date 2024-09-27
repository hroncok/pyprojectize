# spec file for package battray
#

Name:           battray
Version:        2.3
Release:        29%{?dist}
Summary:        Tool for displaying a laptop's battery status in the system traiy
License:        MIT
URL:            http://arp242.net/code/battray/
Source0:        https://github.com/Carpetsmoker/battray/archive/version-%{version}/%{name}-version-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-notify2

%description
Battray is a fairly simple tray icon to show a laptop’s battery status. It’s 
simple, easy, fairly environment-independent, and ‘just works’ without tons of
{Gnome,KDE,..} dependencies.

One can also configure it to play annoying sounds if your battery is getting 
low, dim the screen when you switch from AC to battery, etc.

%prep
%setup -q -n %{name}-version-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check

%install
%pyproject_install

%files
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc README.markdown
%license LICENSE

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3-28
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3-24
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3-21
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 22 2021 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-5
- fixed notification issue as per BZ #2001311
- moved to bzipped2 archive (minor)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3-16
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3-13
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3-10
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3-6
- Rebuilt for Python 3.7



* Sat May 12 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-5
- fixed packaging issues as per BZ #1573695 comment #11

* Thu May 3 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-4
- fixed packaging issues as per BZ #1573695 comment #6
- kept removed Requires: python3-gobject (still does not seem to need it). 

* Wed May 2 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-3
- fixed packaging issues as per BZ #1573695 comment #4
- removed Requires: python3-gobject (does not seem to need it. try for now 
  without it.) 

* Wed May 2 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3=2
- fixed packaging issues as per BZ #1573695 comment #2

* Tue May 1 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-1
- initial packaging of 2.3 version


