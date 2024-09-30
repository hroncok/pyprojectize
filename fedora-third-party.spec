Name:		fedora-third-party
Version:	0.10
Release:	10%{dist}
Summary:	Tool for handling third-party RPM and Flatpak repositories in Fedora

License:	MIT
URL:		https://pagure.io/fedora-third-party
Source0:	fedora-third-party-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	systemd
BuildRequires:	polkit
BuildRequires:	python3-click
BuildRequires:	python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:	python3-pytest
BuildRequires:	golang-github-cpuguy83-md2man

Requires: python3-click
Requires: python3-gobject-base

%description
fedora-third-party is a tool for handling third-party RPM and Flatpak
repositories in Fedora.  It is used to handle the user changing their opt-in
status for these repositories, and enables/disables RPM repositories and
adds/removes Flatpak repositories as necessary.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

go-md2man -in doc/%{name}.1.md -out doc/%{name}.1


%check
%pytest


%install
%pyproject_install
%pyproject_save_files -l 'fedora_third_party*'

# This script is just for use under pkexec, move it out of bindir to avoid confusion
mkdir -p %{buildroot}%{_prefix}/lib/%{name}
mv %{buildroot}%{_bindir}/fedora-third-party-opt-out %{buildroot}%{_prefix}/lib/%{name}/fedora-third-party-opt-out

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_prefix}/lib/%{name}/conf.d

install -m0644 -D doc/%{name}.1 -t %{buildroot}%{_mandir}/man1
install -m0644 -D systemd/fedora-third-party-refresh.service -t %{buildroot}%{_unitdir}
install -m0644 -D polkit/org.fedoraproject.thirdparty.policy -t %{buildroot}%{_datadir}/polkit-1/actions
install -m0644 -D polkit/org.fedoraproject.thirdparty.rules -t %{buildroot}%{_datadir}/polkit-1/rules.d


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/polkit-1/rules.d/*.rules
%{_localstatedir}/lib/%{name}
%{_prefix}/lib/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/*.service


%post
%systemd_post fedora-third-party-refresh.service

%preun
%systemd_preun fedora-third-party-refresh.service

%postun
%systemd_postun_with_restart fedora-third-party-refresh.service

%dnl This enables/adds any newly added repositories/remotes
%transfiletriggerin -- %{_prefix}/lib/%{name}/conf.d
fedora-third-party refresh

%dnl This could potentially be used to remove Flatpak repositories (not currently implemented)
%transfiletriggerpostun -- %{_prefix}/lib/%{name}/conf.d
fedora-third-party refresh || :


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.10-9
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.10-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10-2
- Rebuilt for Python 3.11

* Wed Apr 06 2022 Owen W. Taylor <otaylor@fishsoup.net> - 0.10-1
- Version 0.10 (Owen W. Taylor)
- cli.py: add a logging handler to prettify warning messages (Owen W. Taylor)
- Gracefully handle failures when running 'flatpak' (Owen W. Taylor)
- test_repository.py: increase test coverage a bit (Owen W. Taylor)
- tests/test_cli.py: factor out repeated long commands (Owen W. Taylor)
- Add tools/test.sh that invokes flake8 and pytest, fix flake8 warnings (Owen W. Taylor)
- Fix upgrades by treating un-added Flatpak repositories as "unseen" (Owen W. Taylor)
- Fix listing remotes when some have no options at all. (Owen W. Taylor)

* Thu Mar 31 2022 Owen W. Taylor <otaylor@fishsoup.net> - 0.9.1-1
- Add missing [Build]Requires on python3-gobject-base (Owen W. Taylor)

* Thu Mar 31 2022 Owen W. Taylor <otaylor@fishsoup.net> - 0.9-1
- Version 0.9 (Owen W. Taylor)
- fedora-third-party.1.md: Remove incorrect statement (Owen W. Taylor)
- Enable/disable Flatpak repositories rather than adding/removing them (Owen W. Taylor)
- Pass title, comment, description to 'flatpak remote-add' on the command line (Owen W. Taylor)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.8-1
- Version 0.8 (Owen W. Taylor)
- Stop calling chcon to propagate selinux context to editor config files (Owen W. Taylor)

* Fri Oct 15 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.8-1
- Drop a chcon call that was making problems for selinux confinement

* Tue Oct 5 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.7-1
- Don't show repositories that are modified to remove the filter in
  the output of `fedora-third-party list.

* Mon Aug 16 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.6-1
- Don't write /var/lib/fedora-third-party/state on refresh if no changes
  Resolves: rhbz#1994830

* Mon Aug 16 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.5-1
- Remove dependency on 'dnf config-manager'
- Make fedora-third-party-refresh.service only run on rpm-ostree systems

* Wed Aug 11 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.4-1
- Add a special 'fedora-third-party-opt-out' script to go from unset => disabled
  without a polkit auth dialog.

* Wed Aug 11 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.3-1
- Add --config-only options to the enable/disable subcommands
- Allow detecting whether the config has been explicitly set, or whether no
  decision has been made yet.

* Tue Aug 10 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.2-1
- Fix spec file, add polkit configuration and a --list subcommand

* Fri Jul 30 2021 Owen W. Taylor <otaylor@fishsoup.net> - 0.1-1
- Initial version
