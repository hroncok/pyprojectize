Name:           btrfs-sxbackup
Version:        0.6.11
Release:        26%{?dist}
Summary:        Incremental btrfs snapshot backups with push/pull support via SSH
License:        GPL-2.0-only
URL:            https://github.com/masc3d/btrfs-sxbackup
Source0:        https://github.com/masc3d/btrfs-sxbackup/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Add a manpage. The manpage was sent upstream but rejected, because they want
# to avoid maintaining multiple documentations and generate the manpage from the
# existing documentation instead. Keep the manpage until upstream has found a
# solution. Also see https://github.com/masc3d/btrfs-sxbackup/issues/26.
Patch0:         btrfs-sxbackup-manpages.patch
# Fix missing test suite from setup.py.
Patch1:         btrfs-sxbackup-tests.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Btrfs snapshot backup utility with push/pull support via SSH, retention, Email
notifications, compression of transferred data, and syslog logging.


%prep
%autosetup -p 1 -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
install -d %{buildroot}/%{_mandir}/man1
install -p -m644 man/* %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_sysconfdir}
install -p -m644 etc/btrfs-sxbackup.conf %{buildroot}/%{_sysconfdir}


%check
%{__python3} setup.py test


%files
%doc README.rst
%license LICENSE
%{_bindir}/btrfs-sxbackup
%{python3_sitelib}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/btrfs-sxbackup.conf


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.11-25
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.11-21
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.11-18
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.11-15
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.6.11-12
- Explicitly BR python3-setuptools (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.11-11
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.11-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.11-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.11-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 Till Hofmann <till.hofmann@posteo.de> - 0.6.11-1
- Update to 0.6.11

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-2
- Rebuild for Python 3.6

* Sat Aug 27 2016 Till Hofmann <till.hofmann@posteo.de> - 0.6.10-1
- Update to 0.6.10

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 10 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.9-2
- Add default config file

* Tue Jun 28 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.9-1
- Update to 0.6.9

* Mon Jun 20 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.8-1
- Update to 0.6.8

* Wed Jun 15 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.7-1
- Update to 0.6.7

* Mon Jun 06 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.6-2
- Change license to GPLv2+, add license file

* Sat Jun 04 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.6-1
- Update to 0.6.6

* Fri Jan 01 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.9-3
- Patch setup.py to run unit tests correctly

* Fri Jan 01 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.9-2
- Add manpages

* Sat Dec 05 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.9-1
- Update to newest upstream release

* Tue Nov  3 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.8-1
- Initial package
