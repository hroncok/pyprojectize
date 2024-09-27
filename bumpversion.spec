%if 0%{?rhel}
# https://bugzilla.redhat.com/show_bug.cgi?id=2125297
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           bumpversion
Version:        1.0.1
Release:        10%{?dist}
Summary:        Version-bump your software with a single command

License:        MIT
URL:            https://github.com/c4urself/bump2version
Source0:        %{url}/archive/v%{version}/bump2version-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-testfixtures
%endif

%description
A small command line tool to simplify releasing software by updating all
version strings in your source code by the correct increment. Also creates
commits and tags:

 * version formats are highly configurable
 * works without any VCS, but happily reads tag information from and writes
    commits and tags to Git and Mercurial if available
 * just handles text files, so it's not specific to any programming language


%prep
%autosetup -n bump2version-%{version}


%build
%py3_build


%if %{with tests}
%check
%pytest -k "not test_usage_string and not test_defaults_in_usage_with_config"
%endif


%install
%py3_install


%files
%doc README.md
%license LICENSE.rst
%attr(0755,root,root) %{_bindir}/{bumpversion,bump2version}
%{python3_sitelib}/bumpversion/
%{python3_sitelib}/bump2version-%{version}*egg-info/


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.1-9
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.12

* Fri Feb 03 2023 Davide Cavalca <dcavalca@centosproject.org> - 1.0.1-4
- Gate tests out for EPEL builds due to missing dependency

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 08 2022 Jonathan Wright <jonathan@almalinux.org> - 1.0.1-2
- Modernize spec file
- Add tests
- rhbz#1496612

* Thu Sep 08 2022 Federico Pellegrin <fede@evolware.org> - 1.0.1-1
- Update to version 1.0.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.8-15
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.8-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.8-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.8-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.8-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.8-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Hui Tang <duriantang@gmail.com> - 0.5.8-1
- update to version 0.5.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 0.5.5-1
- temporarily switched upstream to https://github.com/c4urself/bump2version
  since the development of https://github.com/peritus/bumpversion has been stuck
- update to version 0.5.5 (which among other features creates annotated tags)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  1 2015 Jakub Dorňák <jdornak@redhat.com> - 0.5.3-2
- Remove exclamation mark from summary
- Use tarball from git, which contains LICENSE.rst

* Fri Jul  3 2015 Jakub Dorňák <jdornak@redhat.com> - 0.5.3-1
- Initial package
