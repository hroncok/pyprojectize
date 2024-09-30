Name:       rig
Summary:    Monitor a system for events and trigger specific actions
Version:    1.1
Release:    10%{?dist}
Url:        https://github.com/TurboTurtle/rig
Source0:    %{url}/archive/%{name}-%{version}.tar.gz
License:    GPL-2.0-only
BuildArch:  noarch

BuildRequires: python3-devel
BuildRequires: python3dist(systemd-python)
BuildRequires: python3dist(psutil)

%description
Rig is a utility designed to watch or monitor specific system resources (e.g.
log files, journals, system activity, etc...) and then take specific action
when the trigger condition is met. Its primary aim is to assist in
troubleshooting and data collection for randomly occurring events.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/rig.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%pyproject_install
%pyproject_save_files -l rigging

%files -f %{pyproject_files}
%{_bindir}/rig
%{_mandir}/man1/*


%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1-2
- Rebuilt for Python 3.11

* Fri Apr 22 2022 Jake Hunsaker <jhunsake@redhat.com> - 1.1-1
- New upstream release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jake Hunsaker <jhunsake@redhat.com> - 1.0-1
- Version 1.0 release
