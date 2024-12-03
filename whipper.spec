%global srcname whipper
%global sum Python CD-DA ripper preferring accuracy over speed
%global desc CD ripper preferring accuracy over speed


Name:    %{srcname}
Version: 0.10.0
Release: 15%{?dist}
Summary: %{sum}
URL:     https://github.com/whipper-team/whipper
License: GPL-3.0-or-later

Source0: https://github.com/whipper-team/%{srcname}/archive/v%{version}.tar.gz
# Fix now deprecated usage of dump in ruamel.yaml causing crash (https://github.com/whipper-team/whipper/issues/626)
# Cherry pick commit fixing this from upstream
Patch:         https://patch-diff.githubusercontent.com/raw/whipper-team/whipper/pull/543.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools_scm
BuildRequires: gcc
BuildRequires: libsndfile-devel
BuildRequires: libappstream-glib

Requires: cdrdao
Requires: libcdio-paranoia
Requires: gobject-introspection
Requires: python3-gobject
Requires: python3-setuptools
Requires: python3-musicbrainzngs
Requires: python3-mutagen
Requires: python3-requests
Requires: python3-ruamel-yaml
Requires: python3-pycdio
Requires: python3-discid
Requires: flac
Requires: sox


# Exclude s390x due to missing cdrdao dep
ExcludeArch: s390x

%description
%{desc}

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l %{srcname} 'accuraterip*'

%if "%_metainfodir" != "%{_datadir}/metainfo"
mv %{buildroot}%{_datadir}/metainfo/ \
   %{buildroot}%{_metainfodir}/
%endif

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/whipper
%{_bindir}/accuraterip-checksum
%{_metainfodir}/com.github.whipper_team.Whipper.metainfo.xml
%doc README.md TODO CHANGELOG.md HACKING COVERAGE

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Matthew Martin <matthew@mttmartin.com> - 0.10.0-14
- Cherry pick commit from upstream that updates now deprecated usage of dump in ruamel.yaml

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.10.0-13
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.10.0-10
- Rebuilt for Python 3.12

* Mon Apr 24 2023 Peter Oliver <rpm@mavit.org.uk> - 0.10.0-9
- SPDX migration.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.0-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.10

* Mon May 24 2021 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.10.0-2
- Include new python3-discid dependency

* Mon May 17 2021 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-8
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Adrian Reber <adrian@lisas.de> - 0.9.0-7
- Rebuilt for libcdio-2.1.0

* Thu Mar 12 2020 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.9.0-6
- Bump release for rebuild

* Thu Mar 12 2020 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.9.0-5
- Bump release for rebuild

* Tue Mar 10 2020 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.9.0-4
- Bump release for rebuild due to Koji outage

* Tue Mar 10 2020 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.9.0-3
- Adjust pycdio to require python3 version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.9.0-1
- Update to release of 0.9.0

* Mon Dec 02 2019 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.9.0-0.1
- Prerelease of 0.9.0, intended to comply with impending Py2 retirement

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Thu Nov 01 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.7.2-3
- Adjustment to metainfodir fix

* Thu Nov 01 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.7.2-2
- Fix metainfodir on f27

* Thu Nov 01 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.7.2-1
- Update to version 0.7.2

* Tue Oct 23 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.7.1-1
- Update to version 0.7.1

* Mon Oct 22 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.7.0-3
- New upstream repository

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.7.0-1
- Update to version 0.7.0.

* Tue Feb 20 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.6.0-7
- Exclude s390x due to missing cdrdao dependency.

* Sat Feb 17 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.6.0-6
- Added gcc build requirement.

* Tue Feb 13 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.6.0-5
- Fix missing python2-setuptools requirement.

* Mon Feb 12 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.6.0-4
- Fix ownership of directories and returned to a single package.

* Wed Feb 7 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.6.0-3
- Fix incorrect gobject dependency.

* Fri Feb 2 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.6.0-2
- Split Requires into separate lines and commenting patch.

* Fri Feb 2 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.6.0-1
- Update to version 0.6.0.

* Tue Jan 23 2018 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-5
- Adjust accuraterip patch to include debug info.

* Tue Jun 27 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-4
- Move python2 sitelib into python2 subpackage.

* Tue Apr 25 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-3
- Added license and doc macros to conform with proper best practices.

* Mon Apr 24 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-2
- Remove libsndfile dependency, rpm picks that up on build.

* Mon Apr 24 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-1
- Version 0.5.1

* Sun Jan 8 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.4.2-1
- Version 0.4.2 released. Removal of submodule logic.

* Wed Dec 21 2016 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.4.0-3
- Fixed setup macro and patches accuraterip-checksum to the correct bin
  directory

* Wed Dec 21 2016 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.4.0-2
- Added forgotten python2 requirement

* Wed Dec 21 2016 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.4.0-1
- Initial RPM release
