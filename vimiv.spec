Name:       vimiv
Version:    0.9.1
Release:    28%{?dist}
Summary:    An image viewer with vim-like keybindings

License:    MIT
URL:        http://karlch.github.io/%{name}
Source0:    https://github.com/karlch/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-gobject

Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gexiv2

%description
Vimiv is an image viewer with vim-like keybindings. It is written in python3
using the Gtk3 toolkit. Some of the features are:

- Thumbnail mode
- Simple library browser
- Basic image editing
- Command line with tab completion

%prep
%setup -q


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

install -p -Dm644 config/vimivrc $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/vimivrc
install -p -Dm644 config/keys.conf $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/keys.conf

install -p -Dm644 man/vimiv.1 $RPM_BUILD_ROOT/%{_mandir}/man1/vimiv.1
install -p -Dm644 man/vimivrc.5 $RPM_BUILD_ROOT/%{_mandir}/man5/vimivrc.5


install -p -Dm644 %{name}.appdata.xml $RPM_BUILD_ROOT/%{_datadir}/metainfo/%{name}.appdata.xml

appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/%{name}.appdata.xml

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop

for i in 16 32 64 128 256 512; do
    install -p -Dm644 icons/%{name}_${i}x${i}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

install -p -Dm644 icons/%{name}.svg $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files -f %{pyproject_files}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}/
%doc readme.md

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.1-27
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.9.1-24
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.1-21
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.1-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-15
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-12
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-9
- Include gcc as BR
- Organise BRs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-5
- Remove obsolete scriptlets

* Sun Dec 10 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-4
- Remove tests - Xvfb seems to require root access and X

* Sun Dec 10 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-3
- Add tests and other corrections based on rhbz #1517006
- update-desktop-database
- preserve timestamps

* Fri Nov 24 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-2
- Update requires
- Fix permissions

* Fri Nov 17 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-1
- Update to latest upstream release
- Not noarch now

* Tue Nov 07 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8-2
- Add appdata file
- correct folder permissions

* Tue Nov 07 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8-1
- Initial rpmbuild
- TODO: add appstream data file?
