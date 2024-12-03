%global sysname sgtk_menu

Name:           sgtk-menu
Version:        1.4.1
Release:        15%{?dist}
Summary:        GTK launcher for sway & other WMs

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/nwg-piotr/sgtk-menu
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
This project is an attempt to create a launcher, that behaves decently on sway,
but also works on other window managers. It may or may not work on some DEs - I
don't care much about it. For what I managed to test so far, see the
Compatibility chart.


%prep
%autosetup -n %{name}-%{version}

# Remove shebang from Python libraries
for lib in sgtk_menu/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{sysname}


%check
%pyproject_check_import


%files -f %{pyproject_files}
%doc README.md examples/
%{_bindir}/%{name}
%{_bindir}/sgtk-bar
%{_bindir}/sgtk-dmenu
%{_bindir}/sgtk-grid


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.1-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.1-13
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.1-10
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.1-7
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-3
- Packaging fixes

* Wed Feb 26 2020 Bob Hepple <bob.hepple@gmail.com> - 1.3.1-1.fc31.wef
- Initial version of the package
