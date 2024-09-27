Name:           arandr
Version:        0.1.11
Release:        %autorelease
Summary:        Simple GTK+ XRandR GUI

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://christian.amsuess.com/tools/arandr/
Source0:        https://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz
Patch0:         0001-Make-ARandR-appear-in-XFCE-Settings-Manager.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  gettext
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils
Requires:       python3
Requires:       python3-gobject
Requires:       xrandr

%description
ARandR is designed to provide a simple visual front end for XRandR 1.2/1.3.
Relative monitor positions are shown graphically and can be changed in a
drag-and-drop way.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/arandr.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc README TODO ChangeLog NEWS
%license COPYING
%{_bindir}/arandr
%{_bindir}/unxrandr
%{python3_sitelib}/screenlayout/
%{python3_sitelib}/arandr-%{version}-py*.egg-info
%{_mandir}/man1/arandr.1.*
%{_mandir}/man1/unxrandr.1.*
%{_datadir}/applications/arandr.desktop


%changelog
%autochangelog
