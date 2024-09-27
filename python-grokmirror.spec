Name:           python-grokmirror
Version:        2.0.11
Release:        11%{?dist}
Summary:        Framework to smartly mirror git repositories

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/grokmirror/grokmirror.git
Source0:        https://www.kernel.org/pub/software/network/grokmirror/grokmirror-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
Grokmirror was written to make mirroring large git repository\
collections more efficient. Grokmirror uses the manifest file published\
by the master mirror in order to figure out which repositories to\
clone, and to track which repositories require updating. The process is\
extremely lightweight and efficient both for the master and for the\
mirrors.

%description %_description

%package -n python3-grokmirror
Summary:        %summary
Requires:       python3-GitPython, python3-anyjson, python3-setuptools, python3-enlighten
%{?python_provide:%python_provide python3-grokmirror}

%description -n python3-grokmirror %_description

%prep
%autosetup -n grokmirror-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%{__mkdir_p} -m 0755 \
    %{buildroot}%{_mandir}/man1

%{__install} -m 0644 man/*.1 %{buildroot}/%{_mandir}/man1/


%files -n python3-grokmirror
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/*
%{_bindir}/grok-*
%{_mandir}/*/*

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.11-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.11-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.11-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.11-2
- Rebuilt for Python 3.11

* Thu May 05 2022 Kevin Fenzi <kevin@scrye.com> - 2.0.11-1
- Update to 2.0.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Konstantin Ryabitsev <konstantin@linuxfoundation.org> - 1.2.0-1
- Upstream 1.2.0 with new features

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.1-2
- Subpackage python2-grokmirror has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 25 2018 Konstantin Ryabitsev <konstantin@linuxfoundation.org> - 1.1.1-1
- Update to 1.1.1 with a hotfix for grok-fsck

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Tue Apr 24 2018 Konstantin Ryabitsev <konstantin@linuxfoundation.org> - 1.1.0-1
- Build for py2 and py3
- Version update to 1.1.0 with minor bugfixes and feature updates

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-5
- Python 2 binary package renamed to python2-grokmirror
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 with minor bugfixes (rebranded 0.4.3)

* Mon Feb 22 2016 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2 with major new features.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.4-1
- Update to 0.3.4 containing minor bugfixes

* Mon May 27 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.3-1
- Update to 0.3.3 containing bugfixes and new features

* Mon May 13 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.2-1
- Update to 0.3.2 containing important bugfixes and minor new features

* Mon May 13 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.1-1
- Update to 0.3.1 containing important bugfixes

* Mon May 06 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.3-1
- Preparing for 0.3 with new features.

* Thu Apr 25 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.2-1
- Version 0.2 with new features and manpages.

* Wed Apr 03 2013 Konstantin Ryabitsev <mricon@kernel.org> - 0.1-1
- Initial packaging
