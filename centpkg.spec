# Explicitly define on RHEL8 to avoid an unnecessary dependency on python36
%if %{defined el8}
%global __python3 %{_libexecdir}/platform-python
%endif

Name:           centpkg
Version:        0.8.11
Release:        1%{?dist}
Summary:        CentOS utility for working with dist-git
License:        GPL-2.0-or-later
URL:            https://git.centos.org/centos/centpkg
Source0:        %{url}/archive/%{version}/centpkg-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# runtime requirements for test suite
BuildRequires:  python3-cryptography
BuildRequires:  python3-GitPython
BuildRequires:  python3-gitlab
BuildRequires:  python3-pycurl
BuildRequires:  python3-rpkg >= 1.6.5

# /etc/koji.conf.d/stream.conf was previously part of streamkoji
Conflicts:      streamkoji < 1.1-3


%description
Provides the centpkg command for working with dist-git.


%package sig
Summary:        CentOS SIG utility for working with dist-git
Requires:       %{name} = %{version}-%{release}


%description sig
Provides the centpkg-sig command for working with dist-git.


%prep
%autosetup -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%{python3} doc/centpkg_man_page.py > centpkg.1


%install
%pyproject_install
%pyproject_save_files %{name}
install -D -p -m 0644 src/stream.conf      %{buildroot}%{_sysconfdir}/koji.conf.d/stream.conf
install -D -p -m 0644 src/centpkg.conf     %{buildroot}%{_sysconfdir}/rpkg/centpkg.conf
install -D -p -m 0644 src/centpkg-sig.conf %{buildroot}%{_sysconfdir}/rpkg/centpkg-sig.conf
install -D -p -m 0644 src/centpkg.bash     %{buildroot}%{_datadir}/bash-completion/completions/centpkg
install -D -p -m 0644 centpkg.1            %{buildroot}%{_mandir}/man1/centpkg.1


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m unittest discover --verbose


%files -f %{pyproject_files}
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/koji.conf.d/stream.conf
%config(noreplace) %{_sysconfdir}/rpkg/centpkg.conf
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/centpkg
%{_mandir}/man1/centpkg.1*


%files sig
%{_bindir}/%{name}-sig
%config(noreplace) %{_sysconfdir}/rpkg/centpkg-sig.conf


%changelog
* Fri Sep 20 2024 Troy Dawson <tdawson@redhat.com> - 0.8.11-1
- determine_rhel_state: Fix missing phase check
- Fix detection of releases in Maintenance Phase
- Handle maintenance releases better

* Wed Sep 18 2024 Troy Dawson <tdawson@redhat.com> - 0.8.10-1
- Handle packages that don't sync to RHEL

* Fri Sep 13 2024 Troy Dawson <tdawson@redhat.com> - 0.8.9-1
- Fix detection of exception phase (CS-2523)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Troy Dawson <tdawson@redhat.com> - 0.8.8-1
- Tweak autodetection of repo name. (CS-2340)

* Thu Jun 27 2024 Troy Dawson <tdawson@redhat.com> - 0.8.7-1
- Fix autodetection of repo name with SSH remote (CS-2302)

* Fri Jun 21 2024 Troy Dawson <tdawson@redhat.com> - 0.8.6-1
- Fix cloning of the SIG repositories

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.8.3-3
- Rebuilt for Python 3.13

* Tue Apr 23 2024 Troy Dawson <tdawson@redhat.com> - 0.8.3-2
- Warn (not Fail) on possible fork when pushing (Issue: 93)

* Fri Mar 15 2024 Troy Dawson <tdawson@redhat.com> - 0.8.3-1
- Update branch detection for c10s

* Wed Feb 21 2024 Troy Dawson <tdawson@redhat.com> - 0.8.2-1
- Update centpkg to accept java branches (CS-1956)
- Set rhel-target to latest for c10s (CS-1971)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.8.1-3
- Add patch for Python 3.12 compatibility, resolves rhbz#2238954

* Thu Sep 07 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.8.1-2
- Sync dependencies
- Enable test suite
- Switch to SPDX license identifier

* Thu Sep 07 2023 Troy Dawson <tdawson@redhat.com> - 0.8.1-1
- Add the --rhel-target none option (Issue: 79)

* Mon Aug 28 2023 Troy Dawson <tdawson@redhat.com> - 0.8.0-1
- Update stabilization phase detection (CS-1726)
- Correctly clone tests/* (CS-1725)
- Added current-state option (CS-1551)
- Fix exit codes and error messages (Issue: 81)

* Tue Aug 15 2023 Troy Dawson <tdawson@redhat.com> - 0.7.4-4
- Correctly clone full path rpms (Issue: 80)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Troy Dawson <tdawson@redhat.com> - 0.7.4-2
- 0.7.4 requires python3-gitlab

* Mon Jul 10 2023 Troy Dawson <tdawson@redhat.com> - 0.7.4-1
- Check package spelling (CS-767)
- Add StreamLookasideCache specific get_download_url method
- Exit with message if unable to look for file

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.7.3-2
- Rebuilt for Python 3.12

* Wed May 03 2023 Troy Dawson <tdawson@redhat.com> - 0.7.1-3
- Fix determine_active_y_version bug
- Better user output when determine_active_y_version fails
- Skip rhel-target when doing scratch builds

* Wed Mar 01 2023 Troy Dawson <tdawson@redhat.com> - 0.7.1-2
- Latest upstream (Fixes confusing output)

* Wed Mar 01 2023 Troy Dawson <tdawson@redhat.com> - 0.7.1-1
- Latest upstream

* Tue Feb 28 2023 Troy Dawson <tdawson@redhat.com> - 0.7.0-1
- Latest upstream - adds --rhel-target feature

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Troy Dawson <tdawson@redhat.com> - 0.6.9-1
- Latest upstream

* Tue Nov 01 2022 Troy Dawson <tdawson@redhat.com> - 0.6.8-1
- Latest upstream

* Thu Sep 08 2022 Troy Dawson <tdawson@redhat.com> - 0.6.7-2
- centpkg 0.6.7 requires rpkg 1.65 or greater

* Thu Sep 08 2022 Troy Dawson <tdawson@redhat.com> - 0.6.7-1
- Latest upstream

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.6.6-5
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Carl George <carl@george.computer> - 0.6.6-3
- Backport upstream patch for "name 'header' is not defined" error

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Mohan Boddu <mboddu@bhujji.com> - 0.6.6-1
- Latest upstream

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.5-2
- Rebuilt for Python 3.10

* Tue May 25 2021 Carl George <carl@george.computer> - 0.6.5-1
- Latest upstream

* Wed Apr 28 2021 Carl George <carl@george.computer> - 0.6.4-1
- Latest upstream

* Fri Apr 16 2021 Carl George <carl@george.computer> - 0.6.3-1
- Latest upstream

* Tue Apr 13 2021 Carl George <carl@george.computer> - 0.6.2-1
- Latest upstream
- Add stream koji profile

* Thu Apr 08 2021 Carl George <carl@george.computer> - 0.6.1-1
- Latest upstream
- Add bash completion support
- Add manpage support

* Tue Mar 30 2021 Carl George <carl@george.computer> - 0.5.1-3
- Fix epel7/python2 compatibility

* Thu Mar 25 2021 Carl George <carl@george.computer> - 0.5.1-2
- Add missing el7 requirements

* Thu Mar 25 2021 Carl George <carl@george.computer> - 0.5.1-1
- Latest version

* Thu Feb 25 2021 mkonecny@redhat.com 0.5.0-1
- Add centpkg-sig command

* Mon Nov 28 2016 brian@bstinson.com 0.4.6-1
- Tracking updates to rpkg (thanks pavlix)
- Fix the URL building code in the sources method

* Sat Jan 31 2015 Brian Stinson bstinson@ksu.edu - 0.4.4-1
- New version correcting the anonymous pull URLs

* Sun Dec 14 2014 Brian Stinson bstinson@ksu.edu - 0.4.3-1
- Use the authenticated git url for centpkg pulls

* Sun Dec 14 2014 Brian Stinson bstinson@ksu.edu - 0.4.2-1
- Fix the koji config path in centpkg.conf

* Sun Dec 14 2014 Brian Stinson bstinson@ksu.edu - 0.4.1-1
- Fix a disttag regression and add a "patch" version number

* Sat Nov 23 2014 Brian Stinson bstinson@ksu.edu - 0.2-1
- The srpm workflow to the CBS works now

* Sat Jul 05 2014 Brian Stinson bstinson@ksu.edu - 0.1-2
- Update readme and add exception checking when running toplevel commands

* Sat Jul 05 2014 Brian Stinson bstinson@ksu.edu - 0.1-1
- Local builds and mockbuilds work
