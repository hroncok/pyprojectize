Name:    prunerepo
Version: 1.25
Summary: Remove old packages from rpm-md repository
Release: 7%{?dist}
Url: https://pagure.io/prunerepo

# Source is created by:
# git clone %%url && cd prunerepo
# tito build --tgz --tag %%name-%%version-%%release
Source0: %name-%version.tar.gz

License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: bash
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-rpm
BuildRequires: createrepo_c
BuildRequires: asciidoc
BuildRequires: findutils
BuildRequires: python3-dnf
BuildRequires: dnf-plugins-core
BuildRequires: coreutils
Requires: createrepo_c
Requires: dnf-plugins-core
Requires: python3-rpm
Requires: python3

%description
RPM packages that have newer version available in that same
repository are deleted from filesystem and the rpm-md metadata are
recreated afterwards. If there is a source rpm for a deleted rpm
(and they both share the same directory path), then the source rpm
will be deleted as well.

Support for specific repository structure (e.g. COPR) is also available
making it possible to additionally remove build logs and whole build
directories associated with a package.

After deletion of obsoleted packages, the command
"createrepo_c --database --update" is called
to recreate the repository metadata.

%prep
%setup -q

%check
tests/run.sh

%build
name="%{name}" version="%{version}" summary="%{summary}" %py3_build
a2x -d manpage -f manpage man/prunerepo.1.asciidoc

%install
name="%{name}" version="%{version}" summary="%{summary}" %py3_install

install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/prunerepo.1 %{buildroot}/%{_mandir}/man1/

%files
%license LICENSE

%{python3_sitelib}/*
%{_bindir}/prunerepo
%{_mandir}/man1/prunerepo.1*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.25-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.25-2
- Rebuilt for Python 3.12

* Tue Jun 06 2023 Pavel Raiskup <praiskup@redhat.com> 1.25-1
- PruneRepoAnalyzer to use the temporary cachedir, too
- Read BUILDTIME from the repo metadata, rather than every single RPM file

* Mon Jun 05 2023 Pavel Raiskup <praiskup@redhat.com> 1.24-1
- tests: use --setopt=cachedir=<local-relative-dir>

* Mon Jun 05 2023 Pavel Raiskup <praiskup@redhat.com> 1.23-2
- using a temporary DNF cache directory, Koji FTBFS and https://github.com/fedora-copr/copr/issues/2756

* Mon Jun 05 2023 Pavel Raiskup <praiskup@redhat.com> 1.22-1
- ajust to the current/future DNF packaging
- fix for new DNF that doesn't accept %%location in --queryformat

* Fri Apr 30 2021 Pavel Raiskup <praiskup@redhat.com> 1.21-1
- Don't leak descriptors in Python API call
- fix misleading /bin/prunerepo message when no rpms are to be removed

* Tue Apr 27 2021 Pavel Raiskup <praiskup@redhat.com> 1.20-1
- Move the stderr output to log
- Don't sys.exit() from library function

* Mon Apr 19 2021 Silvie Chlupova <schlupov@redhat.com> 1.19-1
- api: new api method get_rpms_to_remove
- Enhance the logging mechanism a bit
- Faster srpm pairing with rpms
- Start using functions from helpers
- Move prunerepo to helpers.py
- Explicitly depend on python3-setuptools

* Sat Feb 29 2020 clime <clime@fedoraproject.org> 1.18-1
- add --setopt='skip_if_unavailable=False' to listpkgsbyrepo in testlib

* Tue Dec 17 2019 clime <michal.novotny@comprimato.com> 1.17-1
- fix changelog

* Mon Dec 16 2019 clime <clime@fedoraproject.org> 1.16-1
- deprecate --copr
- avoid additional newlines in stderr
- skip prunerepo if set(latest_rpms) is empty
- Use splitlines instead of split for repoquery parsing
- Set skip_if_unavailable=False to not loose the data
- Always dump stderr of repoquery (not only in error case)
- Drop useless double-quote in --queryformat

* Mon Apr 01 2019 clime <clime7@gmail.com> 1.15-1
- fix changelog

* Fri Oct 19 2018 Miroslav Suchý <msuchy@redhat.com> 1.14-1
- /usr/bin/env python3 -> /usr/bin/python3
- use git_dir_archive instead of git_dir_pack
- fix test non-determinism

* Sat Aug 18 2018 clime <clime@redhat.com> 1.13-1
- keep all the latest NEVRAS on disk since dnf3

* Mon Aug 06 2018 clime <clime@redhat.com> 1.12-1
- fix reading spec file values from setup.py
- rpkg deployment into COPR
- use builtin cd in tests

* Wed Jan 24 2018 clime <clime@redhat.com> 1.11-1
- do not recreate repo if there was no change in data unless
  --alwayscreaterepo is specified
- add builddep on createrepo_c as well
- add Builddep on dnf that is no longer present in Builddep chain
- optimize createrepo_c
- run tests during build
- use just --repo instead of --disablerepo= --enablerepo=
- Spelling fixes

* Wed Apr 19 2017 clime <clime@redhat.com> 1.10-1
- replace fedorahosted links

* Thu May 26 2016 clime <clime@redhat.com> 1.9-1
- --days now also influences --cleancopr

* Mon May 23 2016 Miroslav Suchý <msuchy@redhat.com> 1.8-1
- just skip the missing srpm
- first remove srpm and then the rpm

* Mon Mar 14 2016 clime <clime@redhat.com> 1.7-1
- rpm-python3 dependency added back

* Mon Mar 14 2016 Jakub Kadlčík <jkadlcik@redhat.com> 1.6-1
- removed obsolete dependency on rpm-python
- doc update

* Fri Feb 26 2016 clime <clime@redhat.com> 1.5-1
- srpm deletion logic changed

* Mon Feb 22 2016 clime <clime@redhat.com> 1.4-1
- deletion of srpms when the same rpm is present in multiple dirs and --days is used fixed

* Fri Jan 29 2016 Miroslav Suchý <msuchy@redhat.com> 1.3-1
- rebuild for release

* Tue Jan 26 2016 clime <clime@redhat.com> 1.2-1
- bugfix for --cleancopr when a log for the respective dir does not
  exist (e.g. copr repos with old dir naming)

* Mon Jan 25 2016 clime <clime@redhat.com> 1.1-1
- test suite finished
- --quiet, --cleancopr and --days options implemented

* Tue Jan 19 2016 clime <clime@redhat.com> 1.0-1
- Initial package version
