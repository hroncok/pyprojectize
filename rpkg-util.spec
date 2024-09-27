# vim: syntax=spec

%if 0%{?fedora} || 0%{?rhel} > 7
%global python          /usr/bin/python3
%global python_build    %py3_build
%global python_install  %py3_install
%global python_sitelib  %python3_sitelib
%else
%global python          /usr/bin/python2
%global python_build    %py2_build
%global python_install  %py2_install
%global python_sitelib  %python2_sitelib
%endif

Name: rpkg-util
Version: 3.3
Release: 1%{?dist}
Summary: RPM packaging utility
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#55d05bb00449c2816114732e70911b53bbf97c42:
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util
# git checkout rpkg-util-3.3-1
# ./rpkg spec --sources
Source0: rpkg-util-55d05bb0.tar.gz

BuildArch: noarch

%description
This package contains the rpkg utility. We are putting
the actual 'rpkg' package into a subpackage because there already
exists package https://src.fedoraproject.org/rpms/rpkg. That package,
however, does not actually produce rpkg rpm whereas rpkg-util does.

%package -n rpkg
Summary: RPM packaging utility
BuildArch: noarch

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python3-mock
BuildRequires: python3-pytest
BuildRequires: python3-munch
BuildRequires: python3-rpm-macros
BuildRequires: python3-cached_property
BuildRequires: python3-rpm
BuildRequires: python3-pycurl
Requires: python3-cached_property
Requires: python3-munch
Requires: python3-rpm
Requires: python3-pycurl
# https://bugzilla.redhat.com/show_bug.cgi?id=2035475
Requires: python3-setuptools
%else
BuildRequires: python2
BuildRequires: python2-setuptools
BuildRequires: python2-devel
BuildRequires: python2-mock
BuildRequires: python2-pytest
BuildRequires: python2-configparser
BuildRequires: python-munch
BuildRequires: python2-rpm-macros
BuildRequires: python2-cached_property
BuildRequires: rpm-python
BuildRequires: python-pycurl
Requires: python2-configparser
Requires: python2-cached_property
Requires: python-munch
Requires: rpm-python
Requires: python-pycurl
%endif

BuildRequires: preproc
BuildRequires: rpkg-macros
Requires: preproc
Requires: rpkg-macros
Requires: rpm-build
Requires: cpio

%description -n rpkg
This is an RPM packaging utility that can work with both DistGit
and standard Git repositories and handles packed directory content
as well as unpacked one.

%prep
%setup -T -b 0 -q -n rpkg-util

version=%version
version=${version//.${version#*.*.}/}
sed -i 's/version=.*/version="'$version'",/' setup.py

%check
PYTHON=%{python} ./unittests

%build
%python_build
%{python} man/rpkg_man_page.py > rpkg.1

%install
%{python_install}

sed -i '1 s|#.*|#!%{python}|' %{buildroot}%{_bindir}/rpkg

install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 rpkg.1 %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_datarootdir}/bash-completion/completions

cp -a rpkg.conf %{buildroot}%{_sysconfdir}/
cp -a rpkg.bash %{buildroot}%{_datarootdir}/bash-completion/completions/

%files -n rpkg
%{!?_licensedir:%global license %doc}
%license LICENSE
%{python_sitelib}/*

%config(noreplace) %{_sysconfdir}/rpkg.conf
%{_datadir}/bash-completion/completions/rpkg.bash

%{_bindir}/rpkg
%{_mandir}/*/*

%changelog
* Fri Aug 09 2024 Jakub Kadlcik <frostyx@email.cz> 3.3-1
- Make the INVALID_SPEC_TEMPLATE really invalid
- Use quote from shlex instead of deprecated pipes
- rpkg-macros.spec: testsuite work-around for new git
- Fix FTBFS on Fedora 38+

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.2-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2-2
- Rebuilt for Python 3.11

* Thu Feb 03 2022 clime <clime@fedoraproject.org> 3.2-1
- fix #39: .spec.rpkg$ have (always) precendence over .spec$ files

* Fri Jan 28 2022 clime <clime@fedoraproject.org> 3.1-1
- lookaside: define %%(ns<N>) and %%(name)s
- lookaside: fix undefined DownloadError traceback
- require python3-setuptools explicitly

* Sun Jul 18 2021 clime <clime@fedoraproject.org> 3.0-1
- final release

* Wed May 12 2021 clime <clime@fedoraproject.org> 3.rc2-1
- _sourcedir should possibly be set to pkg_path when parsing spec
- check for invalid config keys passed on command-line
- allow --spec to be a directory, autolocate spec then

* Sat May 01 2021 clime <clime@fedoraproject.org> 3.rc1-1
- evaluate preproc in cwd, not in pkg_path
- improve auto-completion

* Fri Apr 30 2021 clime <clime@fedoraproject.org> 3.beta-1
- v3 base
- total rewrite from v2, pyrpkg is no longer used
- lots of new git commands added (merge, log, status, ...)
- configuration extended, contains now three sections rpkg, git, lookaside
- also there are dynamic config section git_props and DEFAULT
- the configuration options can be cross-referenced
- possibility to change config options from command-line
- rpkg now uses the latest rpkg-macros package (2.0)
- commit and tag signing
- auto-packing removed

* Sat Jan 26 2019 clime <clime@redhat.com> 3.prototype-1
- [macros] update examples
- [macros] move patch check in git_setup_macro to correct place
- man page update
- and we also need rpm-build
- another missing dep on python-pycurl
- add missing dep on rpm-python
- add missing deps on GitPython
- [macros] resetting IFS for the subprocess seems to be needed for bash 4.2.46
- [macros] do render version suffices on VERSION/RELEASE bump
- 3.0 prototype/sketch
- [macros] fix tests
- [macros] add git_archive retval handling into git_pack
- [macros] fixes related to querying and prevent output of just \n from queries
- [macros] remove requirement to have clean work (sub)tree for git_archive
- [macros] fix git_vcs invocation this time for macros subpackage
- [preproc] pass now required path to git_vcs macro in spec file
- [macros] reenable running tests in spec
- [macros] remove no longer used file
- [macros] remove unneded part of the condition for adding dirty flag
- [macros] restrict git_archive again not to be able to archive dirty path
- [macros] change order of merged tags to DESC by time
- [macros] fix tests
- [macros] fix git_version
- [macros] use basename instead of --short for symbolic-ref due to
compatibility, use --revs-only for rev-parse
- [macros] path prefix can be empty
- [macros] make querying explicit in the main git functions
- [macros] source env before sourcing anything else
- [macros] add non-empty path check, strip trailing slashes from treeish in
git_vcs
- [macros] use process substitution and read to record returned values verbatim
in query_output
- [macros] filter errors when no remote is set
- [macros] we want use echo in query_output because command substitution eats a
new line
- [macros] first check if path is a directory before anything else
- [macros] use string comparison for lead in git_bumped_version to allow non-
numeric leads
- [macros] move the bumped_release/version to helpers
- [macros] move git_bumped_release and version to helpers section
- fix spec files after CACHE to OUTPUT rename
- pass INPUT_DIR_PATH to preproc
- [macros] fix naming for encode_decimal -> rename to utils_encode_decimal
- [macros] rename CACHE array to OUTPUT and QUERY_CACHE to QUERY_OUTPUT
- [macros] split non-git related helper functions and vars to separate files,
INPUT_DIR_PATH will be passed by rpkg
- [macros] do not print bootstrap errors, at the same time check if git repo in
each macro
- fix rpkg-util spec files
- [macros] we want to cache output of git_archive in git_pack as well
- [macros] fix regular expression to check if git version < 1.8
- [macros] fix line continuations
- [macros] switch from aliases back to functions, aliases simply don't work in
scripts
- [macros] optimize the exclude filter in git_pack
- [macros] fix file exclusion for git_pack
- [macros] actually output the dirty appendix
- [macros] changes according to shellcheck.net
- [macros] no input param for git_latest_ctime
- [macros] fix sorting of tags for legacy git
- [macros] using "$*" makes more sense when using that as array index
- [macros] we need to only render "-dirty" flag if the repo is overall dirty
- [macros] improve generated source names
- [macros] return 1 from everywhere, replace exits with normal returns
- [macros] make the macro outputs consistent even if another process is
interfering
- [macros] fix git_pack to exclude untracked files
- [macros] fix derivation of lead in git_version with specified lead
- [macros] fix follow derivation in git_version
- [macros] fix git_version, we cannot filter tags by $name-$lead at the moment
- [macros] fix path_to_name_prefix and path_to_name_suffix
- [macros] introduce git_toplevel alias
- [macros] convert functions to aliases, rename __cached to cache, add input
checks
- [macros] change function order, add back reading cache for base functions
- [macros] rename git_tree_name to git_tree_ref
- [macros] make it possible to set empty lead= for git_version*, filter tags
also by lead**, return lost git_bumped_version, refactor code
- [macros] try to get branch remote url in git_vcs first before getting origin
url
- [macros] refactor out the base functionality and provide current git_x macros
as git_repo_x macros, fix caching, fix get_tree_name and rename it to
git_tree_name
- [macros] for relevant defaults, try to use cached, otherwise invoke the key
- [macros] add explicit defaults for git_dir and git_cwd functions
- [macros] remove no longer needed name= param for git_pack and git_archive
- [macros] fix params declaration for get_tree_name
- [macros] fix test invocation in spec file
- [macros] use git describe to determine source names
- use correct file naming for bash files in tests
- improve error logging in tests
- improve git check-ignore support check in git_pack
- add git_release tests
- add bumped_release test
- add git_release
- [util] basic cmdline test framework added
- [macros] add /bin to tests path, on rhel6 /usr/bin is not alias to /bin
- [preproc] build fix for rhel6
- [macros] provide proxy git script for legacy gits without -C, fix varcaps
- [preproc] provide man pages statically and add regen.sh
- [preproc] add some explanation for tags matching
- [preproc] allow multiple lines inside {{{}}}, fix expression for quoted
strings so that the closest quote is matched
- [util] fix rpkg.macros sourcing
- [macros] exporting SCRIPTDIR in git.bash is not needed
- [util] add missing BR
- [util] add missing BR
- [preproc] add missing BRs
- [macros] add missing BR
- install pack_sources into /bin/, enable macros tests in spec file
- update .gitignore with .pytest_cache
- fix tests
- regenerate tests with tweaked logging
- move preproc and rpkg macro defs into separate packages
- fix problem with changes in dynamic values after ./run_test.sh copy

* Wed Sep 26 2018 clime <clime@redhat.com> 2.6-1
- be more specific about auto-packing deprecation
- fix encoding issues on python2 with POSIX locale set
- fix invalid arguments to setopt on EPEL

* Tue Sep 18 2018 clime <clime@redhat.com> 2.5-1
- EPEL6 fixes
- resolve SafeConfigParser deprecation warning
- EPEL fixes, old git + python related issues
- remove unneded format for tag sorting

* Wed Aug 29 2018 clime <clime@redhat.com> 2.4-1
- fix pg#13: print out more information when lookaside cache is missing
- fix verrel command

* Thu Aug 02 2018 clime <clime@redhat.com> 2.3-1
- tar >= 1.28 condition no longer needed as we dropped --exclude-vcs-ignores
- instead of tar --exclude-vcs-ignores, get the exclude list by git check-ignore
- fix rpkg srpm completion
- switch to git_dir_* macros
- fix no tagname given for rpkg tag -d
- fix for new pyrpkg
- improve git_archive logging info
- print help if no command is given
- add comments to the example config file in man pages
- fix name suffixing for git_cwd and git_dir macros on top-level dir
- follow redirects when downloading sources
- add __pycache__ into .gitignore
- zero umask before creating /tmp/rpkg, ad. #4a4311a
- add log info about path being packed into git_pack
- return back python2 support
- create /tmp/rpkg as writeable by all with sticky bit set
- explicitly mention needed version of git and tar in the spec file
- #8 rpkg error when EDITOR="gvim -f"

* Wed May 02 2018 clime <clime@redhat.com> 2.2-1
- python3 migration
- fix pack_sources script for (sym)linked paths
- fix test dependancy on a parent git repo existance

* Fri Apr 27 2018 clime <clime@redhat.com> 2.1-1
- filter GIT_DISCOVERY_ACROSS_FILESYSTEM not set in tests

* Fri Apr 27 2018 clime <clime@redhat.com> 2.0-1
- slight update in man pages
- fix copr build
- arch param renamed to target + fix tests
- allow --with/--without/--arch for srpm generation

* Thu Apr 19 2018 clime <clime@redhat.com> 2.rc2-1
- implement --with/--without for local, install, prep, compile
- add --follow-tags for push
- fix Git protocol Url parsing for ns_module_name
- fix setup.py not to install tests dir

* Mon Apr 16 2018 clime <clime@redhat.com> 2.rc1-1
- set follow to rc1
- limit renderred commits in tag changelog to path
- invert (fix) logic git_changelog's since_tag and until_tag
for non-existentent tags
- move ~/.config/rpkg to ~/.config/rpkg.conf

* Mon Apr 09 2018 clime <clime@redhat.com> 1.0-1
- spec templates basic impl
- basic command set pretty much determined
- project tagging implemented
- examples and man pages
- rename of package wrapper to rpkg-util
- provide features to manage .spec enriched git projects

* Sun Feb 18 2018 clime <clime@redhat.com> 0.14-1
- fix error when redownloading sources
- do not invoke parent's module_name in load_ns_module_name
- fix python builddeps naming

* Mon Dec 04 2017 clime <clime@redhat.com> 0.13-1
- add LICENSE to ignored file regex

* Mon Oct 23 2017 clime <clime@redhat.com> 0.12-1
- respect hashtype from the sources file if any

* Fri Oct 20 2017 clime <clime@redhat.com> 0.11-1
- set default distgit target to src.fedoraproject.org
- fix downloading sources for any-length-namespace
  modules
- make the whole lookaside url template explict in
  the config file
- rename 'rpkg' config section to 'distgit'
- update in command descriptions

* Wed Oct 18 2017 clime <clime@redhat.com> 0.10-1
- possibility to give directory to --spec
- also take --spec in account for rpmdefines

* Mon Oct 16 2017 clime <clime@redhat.com> 0.9-1
- update spec descriptions
- added is-packed subcommand
- try reading ~/.config/rpkg before /etc/rpkg
- add unittests
- for source downloading, try both url formats
  with/without hashtype
- add make-source subcommand
- patch srpm to generate Source0 if unpacked content
- override load_ns_module_name to work with any length
  namespaces
- added --spec for srpm, make-source, and copr-build
- fixed tagging not to include host dist tag
- docs update
- make all config values optional

* Thu Jul 27 2017 clime <clime@redhat.com> 0.8-1
- fix man pages to only include actually provided part of pyrpkg functionality
- add rpkglib to provide functional interface
- change summary of wrapper package

* Wed Jul 26 2017 clime <clime@redhat.com> 0.7-1
- use %%py2_build and %%py2_install macros
- explicitly invoke python2 for doc generation
- remove no longer needed $BUILDROOT removal in %%install clause
- add missing BuildRequires on python-setuptools

* Fri Jul 07 2017 clime <clime@redhat.com> 0.6-1
- fix build error

* Tue Jun 27 2017 clime <clime@redhat.com> 0.5-1
- remove Requires bash-completion

* Tue Jun 27 2017 clime <clime@redhat.com> 0.4-1
- move config file to /etc/rpkg.conf
- add Requires bash-completion

* Tue Jun 27 2017 clime <clime@redhat.com> 0.3-1
- remove some directories from %%files in .spec
- add (for now) short README.md

* Tue Jun 20 2017 clime <clime@redhat.com> 0.2-1
- new rpkg-client package built with tito

* Mon Jun 12 2017 clime <clime@redhat.com> 0.1-1
- Initial version
