%global distname fedscm_admin

Name:           fedscm-admin
Version:        1.1.7
Release:        9%{?dist}
Summary:        CLI tool to process Fedora SCM requests
License:        GPL-2.0-or-later
URL:            https://pagure.io/fedscm-admin
Source0:        https://releases.pagure.org/fedscm-admin/fedscm_admin-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(python-bugzilla)
BuildRequires:  python3dist(python-fedora)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(fasjson-client)

Requires:  git-core

%description
CLI tool to process Fedora SCM requests.

%prep
%autosetup -n %{distname}-%{version}
rm -vr *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
#export FEDSCM_ADMIN_TEST_CONFIG=true
#export PYTHONPATH=%{buildroot}/%{python3_sitelib}
#export LC_ALL=C.UTF-8
#export LANG=C.UTF-8
#py.test-3 tests/
#unset FEDSCM_ADMIN_TEST_CONFIG

%install
# Set where the config file is so that generating the man pages will not traceback
export FEDSCM_ADMIN_CONFIG=%{buildroot}/%{_sysconfdir}/fedscm-admin/config.ini
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
%pyproject_install
%pyproject_save_files %{distname}

cat >append-to-manual <<EOF
[see also]
%{_pkgdocdir}/README.md
EOF

mkdir -p %{buildroot}/%{_mandir}/man1
help2man -N --no-discard-stderr --version-string=%{version} --include=append-to-manual %{buildroot}/%{_bindir}/fedscm-admin > %{buildroot}/%{_mandir}/man1/fedscm-admin.1
unset FEDSCM_ADMIN_CONFIG

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/fedscm-admin
%dir %{_sysconfdir}/fedscm-admin
%{_sysconfdir}/fedscm-admin/config.ini
%{_mandir}/man1/fedscm-admin.1*

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 1.1.7-8
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 1.1.7-4
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.7-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Tomas Hrcka <thrcka@redhat.com> - 1.1.7-1
- New upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.1.6-2
- Rebuilt for Python 3.11

* Fri Mar 18 2022 Tomas Hrcka <thrcka@redhat.com> - 1.1.6-1
- New upstream release

* Mon Mar 14 2022 Tomas Hrcka <thrcka@redhat.com> - 1.1.5-1
- Use new bugzilla authentication

* Tue Feb 08 2022 Tomas Hrcka <thrcka@redhat.com> - 1.1.4-1
- New upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 18 2021 Mohan Boddu <mboddu@bhujji.com> - 1.1.3-0
- New upstream release

* Mon Aug 09 2021 Tomas Hrcka <thrcka@redhat.com> - 1.1.2-1
- New upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Tomas Hrcka <thrcka@redhat.com> - 1.1.1-1
- New upstream release

* Fri Mar 19 2021 Tomas Hrcka <thrcka@redhat.com> - 1.1.0-2
- New upstream release

* Thu Feb 11 2021 Tomas Hrcka <thrcka@redhat.com> - 1.0.22-1
- New upstream release

* Wed Feb 03 2021 Tomas Hrcka <thrcka@redhat.com> - 1.0.21-1
- New upstream release

* Wed Feb 03 2021 Tomas Hrcka <thrcka@redhat.com> - 1.0.20-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Tomas Hrcka <thrcka@redhat.com> - 1.0.19-1
- Update to v1.0.19
- Fedscm now creates rawhide and main branches

* Wed Dec 16 09:53:08 CET 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.18-1
- Update to 1.0.18 

* Fri Sep 18 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.17-1
- Update to 1.0.17

* Wed Sep 16 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.16-1
- Update to 1.0.16

* Thu Aug 13 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.15-1
- Update to 1.0.15

* Thu Aug 06 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.14-4
- rebuilt

* Thu Aug 06 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.14-3
- Rebuilt

* Thu Aug 06 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.14-2
- Rebuilt with correct sources

* Wed Aug 05 2020 Tomas Hrcka <thrcka@redhat.com> - 1.0.14-1
- Update to 1.0.14

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.13-2
- Rebuilt for Python 3.9

* Mon Apr 06 2020 Mohan Boddu <mboddu@bhujji.com> - 1.0.13-1
- Update to 1.0.13

* Thu Feb 13 2020 Mohan Boddu <mboddu@bhujji.com> - 1.0.12-1
- Update to 1.0.12

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11

* Tue Sep 24 2019 Mohan Boddu <mboddu@bhujji.com> - 1.0.10-1
- Update to 1.0.10

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Mohan Boddu <mboddu@bhujji.com> - 1.0.9-1
- Fixes creating package.cfg in epel7 branches

* Wed Jul 17 2019 Mohan Boddu <mboddu@bhujji.com> - 1.0.8-1
- Create package.cfg file in epel7+ branches

* Mon Jul 08 2019 Mohan Boddu <mboddu@bhujji.com> - 1.0.7-1
- Adding support for epel8 and epel8-playground branches

* Tue May 14 2019 Mohan Boddu <mboddu@bhujji.com> - 1.0.6-1
- Adding support for flatpak namespace

* Wed Feb 20 2019 Mohan Boddu <mboddu@bhujji.com> - 1.0.5-1
- Fixing tests

* Wed Feb 20 2019 Mohan Boddu <mboddu@bhujji.com> - 1.0.4-1
- Fedora 30 is now branching
- Give a little more details when finding a ticket to be invalid (pingou)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.2-2
- Bump release to allow a push to F29.

* Tue Aug 14 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.2-1
- Update to 1.0.2 which can process F29 branches properly.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 mprahl <mprahl@redhat.com> - 1.0.0-1
- Initial release
