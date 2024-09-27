# -*-Mode: rpm-spec -*-

# Use 0 for release and 1 for git
%global   git 0
Version:  0.1.3
%global   forgeurl https://github.com/nwg-piotr/nwg-wrapper
%if %{?git}
%global   commit b186a827404eb2c5e4d757bf122d5d74521b7dcd
%global   date 20220703
%endif
%forgemeta

%global sys_name nwg_wrapper

Name:    nwg-wrapper
Summary: A GTK3 wrapper to display text on the desktop for wlroots
Release: 9%{?dist}

License: MIT
URL:      %{forgeurl}
Source0:  %{forgesource}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3-gobject
Requires: gtk-layer-shell
Requires: gtk3
Recommends: python3-i3ipc
Recommends: wlr-randr

%description

nwg-wrapper is a GTK3-based wrapper to display a script output, or a
text file content on the desktop in sway or other wlroots-based
compositors.

%prep
%forgesetup -a

%build
%py3_build

%install
%py3_install
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{sys_name}/
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.3-8
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.3-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Bob Hepple <bob.hepple@gmail.com> - 0.1.3-2
- rebuild in response to RHBZ#2104366
* Mon Nov 28 2022 Bob Hepple <bob.hepple@gmail.com> - 0.1.3-1
- rebuild in response to RHBZ#2104366
* Wed Jul 06 2022 Bob Hepple <bob.hepple@gmail.com> - 0.1.2-1.20220703gitb186a82
- initial version
