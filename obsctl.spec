Name:           obsctl
Version:        0.7.0
Release:        8%{?dist}
License:        GPL-2.0-or-later
Summary:        Unified high level interface for common actions with the Open Build Service
URL:            https://gitlab.com/datto/engineering/DevOps/obsctl
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core

BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros

BuildRequires:  python3dist(click)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(rpm)
BuildRequires:  python3dist(urlgrabber)
BuildRequires:  python3dist(osc)

Requires:       osc

# For the source services obsctl uses
# For specimport, tarimport, and scratchbuild
Requires:       obs-service-download_files
# For tarimport and scratchbuild
Requires:       obs-service-extract_file
# For scratchbuild
Requires:       obs-service-set_version

%description
This is a command line interface to simplify the packaging and deploy process
for packages built in the openSUSE Open Build Service. This utility functions
in a non-interactive manner allowing it to be utilized in continuous integration
and continuous deployment infrastructure.

%prep
%autosetup -S git_am


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files obsctl

# Setup obsauth ghost config file
mkdir -p %{buildroot}%{_sysconfdir}/obsctl
touch %{buildroot}%{_sysconfdir}/obsctl/obsauth.json


%files -f %{pyproject_files}
%doc README.md TODO contrib obsauth.json.dist
%license COPYING
%dir %{_sysconfdir}/obsctl
%ghost %{_sysconfdir}/obsctl/obsauth.json
%{_bindir}/obsctl


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.7.0-7
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Neal Gompa <ngompa@datto.com> - 0.7.0-1
- Adapt packaging for Fedora

* Thu Jan 05 2023 Neal Gompa <ngompa@datto.com> - 0.7.0
- Initial public release

* Mon Nov 21 2022 Neal Gompa <ngompa@datto.com> - 0.6.0
- Drop Python 2 support
- tarimport: add the '--watch-build' parameter

* Mon Sep 27 2021 Neal Gompa <ngompa@datto.com> - 0.5.5
- Add getbinaries subcommand to fetch binary packages from OBS

* Mon Jul 27 2020 Neal Gompa <ngompa@datto.com> - 0.5.4
- tarimport: Fix typo in variable name for extract extra files _service snippet

* Wed Jul 15 2020 Neal Gompa <ngompa@datto.com> - 0.5.3
- scratchbuild, tarimport: Allow extracting additional dist files

* Wed Dec 11 2019 Neal Gompa <ngompa@datto.com> - 0.5.2
- specimport: Fix check for existence of Dist-Git 'sources' file

* Wed Dec 04 2019 Neal Gompa <ngompa@datto.com> - 0.5.1
- tarimport: Ensure OBS source service file is committed as '_service' to OBS

* Tue Dec 03 2019 Neal Gompa <ngompa@datto.com> - 0.5.0
- Ensure that --repo-name switch is marked as required in all subcommands
- specimport: Add support for fetching Dist-Git resources automatically
- scratchbuild: Add support for building from Package SCM repositories
- Misc internal API changes to support new Package SCM functionality

* Sat Mar 30 2019 Neal Gompa <ngompa@datto.com> - 0.4.2
- scratchbuild: Add with/without flags to toggle build features

* Thu Mar 28 2019 Neal Gompa <ngompa@datto.com> - 0.4.1
- Fix sed expression to fix Python metadata for EL7 builds
- Adjust black to format to 100 columns per line

* Tue Mar 26 2019 Neal Gompa <ngompa@datto.com> - 0.4.0
- Python 3 support for Fedora 30+
- Code is now formatted using 'black'
- Misc internal API changes to address pylint issues

* Wed Nov 07 2018 Neal Gompa <ngompa@datto.com> - 0.3.14
- Fix timestamp format for snapshot versions

* Wed Oct 24 2018 Neal Gompa <ngompa@datto.com> - 0.3.13
- Implement version match check for tarimport

* Mon Aug 27 2018 Neal Gompa <ngompa@datto.com> - 0.3.12
- scratchbuild: Add '--local-package' switch to 'osc build' invocation
- scratchbuild: Clean up success and failure exit messaging

* Wed Feb 28 2018 Neal Gompa <ngompa@datto.com> - 0.3.11
- Allow 'prerel-upver' for snapshot version form

* Tue Jan 23 2018 Neal Gompa <ngompa@datto.com> - 0.3.10
- Further sanitize the branch names to prevent unexpected breakages

* Thu Dec 14 2017 Neal Gompa <ngompa@datto.com> - 0.3.9
- Fix prerel spec version generation

* Tue Dec 12 2017 Neal Gompa <ngompa@datto.com> - 0.3.8
- Fix pattern match for generated _service in tarimport

* Tue Dec 12 2017 Neal Gompa <ngompa@datto.com> - 0.3.7
- Fill in the setuptools metadata
- scratchbuild, tarimport: Add option to set non-default path to extract spec file

* Fri Dec 08 2017 Neal Gompa <ngompa@datto.com> - 0.3.6
- Revert scratchbuild changes in 0.3.4 and 0.3.5

* Fri Dec 08 2017 Neal Gompa <ngompa@datto.com> - 0.3.5
- scratchbuild: Use restricted matching for generated directory

* Fri Dec 08 2017 Neal Gompa <ngompa@datto.com> - 0.3.4
- Print out where people can see the OBS build for obsimport commands
- scratchbuild: Use exact name of the generated directory for spec extraction

* Thu Nov 30 2017 Neal Gompa <ngompa@datto.com> - 0.3.3
- Add download_files service support to scratchbuild

* Thu Nov 30 2017 Neal Gompa <ngompa@datto.com> - 0.3.2
- Add download_files service support to tarimport

* Wed Nov 29 2017 Neal Gompa <ngompa@datto.com> - 0.3.1
- Fix _service file existence check in dscimport

* Wed Nov 29 2017 Neal Gompa <ngompa@datto.com> - 0.3.0
- Implement dscimport for dsc packaging repos

* Tue Nov 28 2017 Neal Gompa <ngompa@datto.com> - 0.2.10
- Add explicit dependencies for required OBS source services
- Ensure scratchbuild ignores hidden files (dotfiles)

* Wed Nov 22 2017 Neal Gompa <ngompa@datto.com> - 0.2.9
- Refactor scratchbuild to not require checkout of OBS package

* Wed Nov 22 2017 Neal Gompa <ngompa@datto.com> - 0.2.8
- Add missing import for os to tarimport

* Wed Nov 22 2017 Neal Gompa <ngompa@datto.com> - 0.2.7
- Remove accidental superfluous delete command

* Wed Nov 22 2017 Neal Gompa <ngompa@datto.com> - 0.2.6
- Fix tarimport and tarball creation logic

* Wed Nov 22 2017 Neal Gompa <ngompa@datto.com> - 0.2.5
- Mark '--source-file' as a required arg for scratchbuild and tarimport

* Wed Nov 22 2017 Neal Gompa <ngompa@datto.com> - 0.2.4
- The scratchbuild command now requires a path to an existing tarball
- Librarized the tarball regeneration logic into new internal tar lib
- Fix osc config generation to keep tempfile for the whole run

* Tue Nov 21 2017 Neal Gompa <ngompa@datto.com> - 0.2.3
- Bump version

* Tue Nov 21 2017 Neal Gompa <ngompa@datto.com> - 0.2.2
- Add missing runtime dependency on setuptools for obsctl executable

* Tue Nov 21 2017 Neal Gompa <ngompa@datto.com> - 0.2.1
- Add initial spec internal library module
- Unify logic in scratchbuild and {tar,spec}import commands
- Make the CLI arguments consistent across commands

* Thu Nov 16 2017 Neal Gompa <ngompa@datto.com> - 0.2.0
- Rename tarsrc-obsimport to tarimport
- Implement specimport for spec+patches repos
- Make tarimport and specimport use the same releasing code in obsc library
- Fix python2_pkgversion conditional in spec for Fedora 27

* Wed Nov 15 2017 Mark Bluemer <mbluemer@datto.com> - 0.1.9
- Bump version

* Wed Nov 15 2017 Mark Bluemer <mbluemer@datto.com> - 0.1.8
- Bump version

* Wed Nov 15 2017 Mark Bluemer <mbluemer@datto.com> - 0.1.7
- Fix tarsrc_obsimport script

* Tue Nov 14 2017 Neal Gompa <ngompa@datto.com> - 0.1.6
- Reword one of the options to match the original script

* Tue Nov 14 2017 Mark Bluemer <mbluemer@datto.com> - 0.1.5
- bump version with addition of CI

* Mon Nov 13 2017 Neal Gompa <ngompa@datto.com> - 0.1.4
- Fix local definition of python2_sitelib

* Mon Nov 13 2017 Neal Gompa <ngompa@datto.com> - 0.1.3
- Consistently use python2_pkgversion macro in spec
- Fix ghost file entry typo
- Add bobs and bits to make openSUSE builds happy

* Mon Nov 13 2017 Neal Gompa <ngompa@datto.com> - 0.1.2
- Revise build-time dependencies to be cross-distribution
- Add missing runtime dependencies
- Wrap the description correctly

* Mon Nov 13 2017 Mark Bluemer <mbluemer@datto.com> - 0.1.1
- Add ghost configuration file for auth information

* Fri Nov 10 2017 Mark Bluemer <mbluemer@datto.com> - 0.1.0
- Inital Packaging

