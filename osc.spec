# SUSE guys use OBS to automatically handle release numbers,
# when rebasing check what they are using on
# https://download.opensuse.org/repositories/openSUSE:/Tools/Fedora_39/src/
# update the obsrel to match the upstream release number
%global obsrel 420.1

# osc plugin support
%global osc_plugin_dir %{_prefix}/lib/osc-plugins

# for obs source services
%global obsroot %{_prefix}/lib/obs
%global obs_srcsvc_dir %{obsroot}/service

# Real release number
%global baserelease 1

Name:           osc
Summary:        Open Build Service Commander
Version:        1.9.1
# Bump the release as necessary to ensure we're one level up from upstream
Release:        %{obsrel}.%{baserelease}%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/%{name}
Source:         %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  diffstat
BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  python3-rpm
BuildRequires:  python3-progressbar2
BuildRequires:  python3-pip
BuildRequires:  python3-cryptography
BuildRequires:  python3-urllib3
BuildRequires:  argparse-manpage
Requires:       python3-distro
Requires:       python3-rpm
Requires:       python3-cryptography
Requires:       python3-urllib3
Requires:       python3-lxml
Requires:       python3-progressbar2
# for MFA via ssh
Recommends:     /usr/bin/ssh-keygen

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     obs-build
Recommends:     obs-service-source_validator
%else
Requires:       obs-service-source_validator
%endif

# To ensure functional parity
Conflicts:      obs-build < 20191205

%description
Commandline client for the Open Build Service.

See http://en.opensuse.org/openSUSE:OSC , as well as
http://en.opensuse.org/openSUSE:Build_Service_Tutorial for a general
introduction.


%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# write rpm macros
cat << EOF > macros.osc
%%osc_plugin_dir %{osc_plugin_dir}
EOF

# build man page
PYTHONPATH=. argparse-manpage \
    --output=osc.1 \
    --format=single-commands-section \
    --module=osc.commandline \
    --function=get_parser \
    --project-name=osc \
    --prog=osc \
    --description="openSUSE Commander" \
    --author="Contributors to the osc project. See the project's GIT history for the complete list." \
    --url="https://github.com/openSUSE/osc/"


%install
%pyproject_install
%pyproject_save_files -l 'osc*'

mkdir -p %{buildroot}%{_localstatedir}/lib/osc-plugins
# mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dm0644 contrib/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -Dm0644 contrib/complete.sh %{buildroot}%{_datadir}/bash-completion/completions/osc
install -Dm0755 contrib/osc.complete %{buildroot}%{_datadir}/osc/complete
install -Dm0644 contrib/osc.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/osc.fish

mkdir -p %{buildroot}%{obs_srcsvc_dir}

mkdir -p %{buildroot}%{osc_plugin_dir}

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/

# install rpm macros
install -Dm0644 macros.osc %{buildroot}%{_rpmmacrodir}/macros.osc

# install man page
install -Dm0644 osc.1 %{buildroot}%{_mandir}/man1/osc.1

%check
%pyproject_check_import

python3 -m unittest

%files -f %{pyproject_files}
%doc AUTHORS README.md NEWS
%{_bindir}/osc*
%{_sysconfdir}/profile.d/osc.csh
%{_datadir}/bash-completion/completions/osc
%{_datadir}/fish/vendor_completions.d/osc.fish
%dir %{_localstatedir}/lib/osc-plugins
%{_mandir}/man1/osc.*
%{_datadir}/osc
%{_rpmconfigdir}/macros.d/macros.osc
%dir %{obsroot}
%dir %{obs_srcsvc_dir}
%dir %{osc_plugin_dir}

%changelog
* Wed Sep 04 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.9.1-415.1.1
- New upstream release 1.9.1, fixes CVE-2024-22034 and rhbz#2309529

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-415.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.8.3-415.1.1
- New upstream release 1.8.3, fixes rhbz#2295680

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7.0-408.1.2
- Rebuilt for Python 3.13

* Thu May 23 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.7.0-408.1.1
- New upstream release 1.7.0, fixes rhbz#2282795

* Tue Apr 16 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.6.2-402.1.1
- New upstream release 1.6.2, fixes rhbz#2275268

* Sun Feb 25 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.6.1-400.1.1
- New upstream release 1.6.1, fixes rhbz#2265732

* Fri Jan 26 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.6.0-400.1.4
- New upstream release 1.6.0, fixes rhbz#2260508

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-397.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-397.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 07 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.5.1-397.1.1
- New upstream release 1.5.1, fixes rhbz#2253104

* Thu Nov 23 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.5.0-391.1.1
- New upstream release 1.5.0, fixes rhbz#2249726

* Fri Nov 03 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.4.4-390.1.1
- New upstream release 1.4.4, fixes rhbz#2247782

* Mon Oct 23 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.4.3-383.1.1
- New upstream release 1.4.3, fixes rhbz#2245427

* Tue Oct 17 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.4.2-381.1.1
- New upstream release 1.4.2, fixes rhbz#2244637

* Thu Oct 12 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.4.1-380.2.1
- New upstream release 1.4.1, fixes rhbz#2243425

* Thu Oct 05 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.4.0-376.19.1
- New upstream release 1.4.0, fixes rhbz#2242260

* Thu Aug 31 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.3.1-375.1.1
- New upstream release 1.3.1, fixes rhbz#2236047

* Wed Aug  9 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.3.0-372.1.1
- New upstream release 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-372.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.2.0-372.1.1
- New upstream release 1.2.0, fixes rhbz#2223109

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1.4-370.2.2
- Rebuilt for Python 3.12

* Tue May 30 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.1.4-370.2.1
- New upstream release 1.1.4, fixes rhbz#2209816

* Thu May 11 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.1.3-367.1.1
- New upstream release 1.1.3, fixes rhbz#2203143

* Wed May 03 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.1.2-362.1.1
- New upstream release 1.1.2, fixes rhbz#2192933

* Wed Apr 12 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.1.1-359.1.1
- New upstream release 1.1.1, fixes rhbz#2186043

* Tue Apr 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.0-357.1.1
- 1.1.0, fixes rhbz#2184191

* Mon Mar 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.1-1
- 1.0.1, fixes rhbz#2179512

* Thu Mar 16 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.0-353.1.1
- New upstream release 1.0.0

* Thu Feb 09 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.0~b5-1
- 1.0.0b5

* Fri Feb  3 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.0~b4-1
- New upstream release 1.0.0~b4, fixes rhbz#2166895

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~b3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.0~b3-1
- New upstream release 1.0.0~b3
- Switch license identifier to SPDX

* Fri Sep 23 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.0~b2-1
- New upstream release 1.0.0b2, fixes rhbz#2125807

* Wed Aug 24 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.0~b1-2
- Recommend ssh-keygen for ssh MFA

* Tue Aug  9 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.0~b1-1
- New upstream release 1.0.0~b1, fixes rhbz#2111361

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.180.0-332.4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.180.0-332.4.1
- New upstream release 0.180.0, fixes rhbz#2101107

* Sat Jun 04 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.179.0-330.1.1
- Update to 0.179.0

* Thu May 26 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.178.0-326.20.2
- New upstream release 0.178.0, fixes rhbz#2089844

* Tue Apr 26 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.177.0-324.28.1
- New upstream release 0.177.0, fixes rhbz#2078825

* Tue Mar  1 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.176.0-378.24.1
- New upstream release 0.176.0, fixes rhbz#2059486

* Mon Jan 24 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.175.0-322.5.1
- New upstream release 0.175.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.174.0-321.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.174.0-321.1.1
- New upstream release 0.174.0
- Enable test suite in check

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.169.1-303.1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.169.1-303.1.4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.169.1-303.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.169.1-303.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Adam Williamson <awilliam@redhat.com> - 0.169.1-303.1.1
- Update to 0.169.1
- Drop merged or otherwise-fixed PRs
- Backport PR #800 to fix build with Python 3.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.167.1-281.1.5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.167.1-281.1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Neal Gompa <ngompa13@gmail.com> - 0.167.1-281.1.3
- Rebuild again to deal with random Koji+Bodhi breakage

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 0.167.1-281.1.2
- Rebuild to deal with random Koji+Bodhi breakage

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 0.167.1-281.1.1
- Update to 0.167.1
- Backport fix for regressions in osc chroot
- Refresh patch for fixing local builds
- Drop patch incorporated in this release
- Add patch to fix osc importsrcpkg on Python 3

* Mon Nov 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.166.2-272.1.2
- Fix patch for replacing cgi.escape with html.escape

* Mon Nov 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.166.2-272.1.1
- Update to 0.166.2
- Add fixes for Python 3.8 compatibility

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.165.1-255.1.2.3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.165.1-255.1.2.2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.165.1-255.1.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Neal Gompa <ngompa13@gmail.com> - 0.165.1-255.1.2
- Add patch proposed upstream to fix local builds

* Thu May 30 2019 Neal Gompa <ngompa13@gmail.com> - 0.165.1-255.1.1
- Update to 0.165.1
- Backport fixes from upstream for Python 3
- Drop patches incorporated in this release

* Sun Mar 24 2019 Neal Gompa <ngompa13@gmail.com> - 0.164.2-245.1.1
- Update to 0.164.2
- Add proposed patches to build for Python 3 for Fedora 30+
- Add Recommends for obs-build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.163.0-237.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Neal Gompa <ngompa13@gmail.com> - 0.163.0-237.1.1
- Update to 0.163.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.162.1-230.1.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.162.1-230.1.1.2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.162.1-230.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Neal Gompa <ngompa13@gmail.com> - 0.162.1-230.1.1
- Rebase to 0.162.1 to fix CVE-2017-9274

* Sun Nov 05 2017 Neal Gompa <ngompa13@gmail.com> - 0.161.1-224.1.1
- Rebase to 0.161.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.157.1-202.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Neal Gompa <ngompa13@gmail.com> - 0.157.1-202.1.1
- Rebase to 0.157.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.155.0-190.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Neal Gompa <ngompa13@gmail.com> - 0.155.0-190.1.1
- Rebase to 0.155.0

* Tue Jul 26 2016 Neal Gompa <ngompa13@gmail.com> - 0.154.0-187.1.1
- Rebase to 0.154.0
- Setup for working on EL7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.151.1-166.2.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.151.1-165.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.151.1-164.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Miroslav Suchý <msuchy@redhat.com> 0.151.1-163.2.1
- rebase to 0.140.1
- fixed shell command injection via crafted _service files CVE-2015-0778

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140.1-109.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140.1-108.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Miroslav Suchý <msuchy@redhat.com> 0.140.1-107.1.1
- add one number to release so we can distinguish from OpenSuse v-r
  (msuchy@redhat.com)
- rebase to 0.140.1 (msuchy@redhat.com)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.132.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.132.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.132.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Jerome Soyer <saispo@gmail.com> - 0.132.4-1
- Update to 0.132.4

* Thu Jun  9 2011 Jerome Soyer <saispo@gmail.com> - 0.132.1-2
- Fix non-arch dependent shell script in /usr/lib for multilib

* Wed Jun  8 2011 Jerome Soyer <saispo@gmail.com> - 0.132.1-1
- Update to 0.132.1
- Fix tab/space in SPEC file
- Add comment and command for tarball creation
- Fix libdir-macro-in-noarch-package

* Wed Jun  8 2011 Jerome Soyer <saispo@gmail.com> - 0.132.0-1
- Initial build
