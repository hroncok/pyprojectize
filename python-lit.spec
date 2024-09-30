%bcond_with snapshot_build

%if %{with snapshot_build}
# Unlock LLVM Snapshot LUA functions
%{llvm_sb_verbose}
%{llvm_sb}
%endif

%global lit_version 18.1.8
#global rc_ver 4
#global post_ver 0

%global python_lit_srcdir %{srcname}-%{version}%{?rc_ver:rc%{rc_ver}}%{?post_ver:.post%{post_ver}}

%if %{with snapshot_build}
%undefine rc_ver
%global lit_version %{llvm_snapshot_version}
%global python_lit_srcdir llvm-%{lit_version}.src/utils/lit
%endif

%bcond_without check

Name: python-lit
Version: %{lit_version}%{?rc_ver:~rc%{rc_ver}}%{?llvm_snapshot_version_suffix:~%{llvm_snapshot_version_suffix}}
Release: 2%{?dist}
BuildArch: noarch

License: Apache-2.0 WITH LLVM-exception OR NCSA
Summary: Tool for executing llvm test suites
URL: https://pypi.python.org/pypi/lit
%if %{without snapshot_build}
Source0: %{pypi_source lit %{lit_version}%{?rc_ver:rc%{rc_ver}}%{?post_ver:.post%{post_ver}}}
%else
Source0:  %{llvm_snapshot_source_prefix}llvm-%{llvm_snapshot_yyyymmdd}.src.tar.xz
%{llvm_snapshot_extra_source_tags}
%endif

# for file check
%if %{with check}
BuildRequires: llvm-test
%endif
BuildRequires: python3-devel

%description
lit is a tool used by the LLVM project for executing its test suites.

%package -n python3-lit
Summary: LLVM lit test runner for Python 3

Requires: python3-setuptools
Recommends: python3-psutil

%description -n python3-lit
lit is a tool used by the LLVM project for executing its test suites.

%prep
%if %{with snapshot_build}
%autosetup -n %{python_lit_srcdir} -p4
%else
%autosetup -n lit-%{lit_version}%{?rc_ver:rc%{rc_ver}}%{?post_ver:.post%{post_ver}} -p4
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

# Strip out #!/usr/bin/env python
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/lit/*.py

%if %{with check} && %{without snapshot_build}
%check
%{__python3} lit.py -v tests
%endif

%files -n python3-lit -f %{pyproject_files}
%doc README.rst
%{_bindir}/lit

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Jesus Checa Hidalgo <jchecahi@redhat.com> - 18.1.8-1
- 18.1.8 Release

* Mon Jun 10 2024 Tom Stellard <tstellar@redhat.com> - 18.1.7-1
- 18.1.7 Release

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 18.1.6-2
- Rebuilt for Python 3.13

* Sat May 18 2024 Tom Stellard <tstellar@redhat.com> - 18.1.6-1
- 18.1.6 Release

* Thu Apr 25 2024 Tom Stellard <tstellar@redhat.com> - 18.1.4-1
- 18.1.4 Release

* Fri Apr 12 2024 Tom Stellard <tstellar@redhat.com> - 18.1.3-1
- 18.1.3 Release

* Thu Mar 21 2024 Tom Stellard <tstellar@redhat.com> - 18.1.2-1
- 18.1.2 Release

* Tue Mar 12 2024 Tom Stellard <tstellar@redhat.com> - 18.1.1-1
- 18.1.1 Release

* Wed Feb 28 2024 Tom Stellard <tstellar@redhat.com> - 18.1.0~rc4-1
- 18.1.0-rc4 Release

* Wed Feb 21 2024 Tom Stellard <tstellar@redhat.com> - 18.1.0~rc3-1
- 18.1.0-rc3 Release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%{?llvm_snapshot_changelog_entry}

* Tue Nov 28 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.6-1
- Update to LLVM 17.0.6

* Tue Nov 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.5-1
- Update to LLVM 17.0.5

* Tue Oct 31 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.4-1
- Update to LLVM 17.0.4

* Tue Oct 17 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.3-1
- Update to LLVM 17.0.3

* Mon Oct 09 2023 Tom Stellard <tstellar@redhat.com> - 17.0.2-2
- Update license

* Tue Oct 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.2-1
- Update to LLVM 17.0.2

* Mon Sep 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.1-1
- Update to LLVM 17.0.1

* Tue Sep 05 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc4-1
- Update to LLVM 17.0.0 RC4

* Tue Aug 22 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-1
- Update to LLVM 17.0.0 RC3

* Thu Aug 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc2-1
- Update to LLVM 17.0.0 RC2

* Mon Jul 31 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-1
- Update to LLVM 17.0.0 RC1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-2
- Rebuilt for Python 3.12 again

* Wed Jun 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-1
- Update to LLVM 16.0.6

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 16.0.5.post0-2
- Rebuilt for Python 3.12

* Fri Jun 02 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.5.post0-1
- Update to LLVM 16.0.5.post0

* Thu May 18 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.4-1
- Update to LLVM 16.0.4

* Mon May 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-2
- Add a patch that accepts ppc64le as a valid triple

* Tue May 09 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-1
- Update to LLVM 16.0.3

* Tue Apr 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.2-1
- Update to LLVM 16.0.2

* Mon Apr 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-1
- Update to LLVM 16.0.1

* Mon Mar 20 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Tue Mar 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Wed Feb 22 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Wed Feb 01 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc1-1
- Update to LLVM 16.0.0 RC1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-2
- Update to LLVM 15.0.7

* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Thu Nov 03 2022 Nikita Popov <npopov@redhat.com> - 15.0.1-1
- Update to lit 15.0.1

* Fri Oct 21 2022 Serge Guelton <serge.guelton@telecom-bretagne.eu> - 15.0.0-2
- Add python3-psutil recommends to avoid runtime warning

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to lit 15.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 14.0.3-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Tom Stellard <tstellar@redhat.com> - 14.0.3-1
- 14.0.3 Release

* Wed Mar 02 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Fri Feb 04 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Nikita Popov <npopov@redhat.com> - 13.0.0-3
- Backport patch 46c947af7 for build reproducibility

* Thu Oct 21 2021 Konrad Kleine <kkleine@redhat.com> - 13.0.0-2
- Remove python 2 support

* Tue Oct 05 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-2
- Add missing dist tag to release

* Fri Aug 06 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 12.0.0-3
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 12.0.0-2
- Bootstrap for Python 3.10

* Thu May 06 2021 sguelton@redhat.com - 12.0.0-1
- 12.0.0 final release

* Tue Feb 23 2021 Pete Walter <pwalter@fedoraproject.org> - 12.0.0-0.2.rc1
- rebuilt

* Wed Feb 03 2021 sguelton@redhat.com - 12.0.0-0.1.rc1
- 12.0.0 rc1 Release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 sguelton@redhat.com - 0.11.1-2.rc2
- 0.11.1 rc2 Release

* Wed Dec 02 2020 sguelton@redhat.com - 0.11.1-1.rc1
- 0.11.1 rc1 Release

* Sun Oct 25 2020 sguelton@redhat.com - 0.11.0-1
- llvm 11.0.0 - final release

* Fri Oct 09 2020 sguelton@redhat.com - 0.11.0-0.2.rc1
- Correctly ship license

* Fri Aug 07 2020 Tom Stellard <tstellar@redhat.com> - 0.11.0-0.1.rc1
- 0.11.0 rc1 Release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.9

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-2
- Bootstrap for Python 3.9

* Thu Apr 9 2020 sguelton@redhat.com - 0.10.0-1
- 0.10.0 final release

* Tue Feb 11 2020 sguelton@redhat.com - 0.10.0-0.1.rc1
- 0.10.0 rc1 Release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-3
- Re-enable tests

* Fri Sep 20 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-2
- Disable check to avoid circular dependency with llvm-test

* Fri Sep 20 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-1
- 0.9.0 Release

* Thu Aug 22 2019 Tom Stellard <tstellar@redhat.com> - 0.9.0-0.1.rc4
- 0.9.0 rc4 Release

* Tue Aug 20 2019 sguelton@redhat.com - 8.0.0-7
- Rebuild for Python 3.8 with test, preparatory work for rhbz#1715016

* Tue Aug 20 2019 sguelton@redhat.com - 8.0.0-6
- Rebuild for Python 3.8 without test, preparatory work for rhbz#1715016

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 sguelton@redhat.com - 8.0.0-3
- Fix rhbz#1728067

* Fri Jun 28 2019 sguelton@redhat.com - 8.0.0-2
- Fix rhbz#1725155

* Thu Mar 21 2019 sguelton@redhat.com - 8.0.0-1
- 0.8.0 Release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 sguelton@redhat.com - 0.7.1-1
- 7.0.1 Release

* Tue Sep 25 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-2
- Add missing dist to release tag

* Fri Sep 21 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-1
- 0.7.0 Release

* Fri Aug 31 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-0.2.rc1
- Add Requires: python[23]-setuptools

* Mon Aug 13 2018 Tom Stellard <tstellar@redhat.com> - 0.7.0-0.1.rc1
- 0.7.0 rc1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-1
- 0.6.0 Release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Stellard <tstellar@redhat.com> - 0.6.0-0.1.rc1
- 0.6.0 rc1

* Tue Jan 23 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.5.1-4
- Add a missed python3 conditional around a sed operation

* Mon Jan 15 2018 Merlin Mathesius <mmathesi@redhat.com> - 0.5.1-3
- Cleanup spec file conditionals

* Wed Dec 06 2017 Tom Stellard <tstellar@redhat.com> - 0.5.1-2
- Fix python prefix in BuildRequires

* Tue Oct 03 2017 Tom Stellard <tstellar@redhat.com> - 0.5.1-1
- Rebase to 0.5.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Tom Stellard <tstellar@redhat.com> - 0.5.0-1
- Initial version
