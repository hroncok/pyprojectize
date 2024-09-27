%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%if 0%{?rhel} && 0%{?rhel} <= 7
%global with_yum 1
%global with_bzr 1
%global bazaar bzr
%endif

%if 0%{?fedora}
%global with_brz 1
%global bazaar brz
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%global dnf_is_mandatory 1
%global dnf_uses_python3 1
%endif

Name:      etckeeper
Version:   1.18.21
Release:   4%{?dist}
Summary:   Store /etc in a SCM system (git, mercurial, bzr or darcs)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       https://etckeeper.branchable.com/
Source0:   https://git.joeyh.name/index.cgi/etckeeper.git/snapshot/%{name}-%{version}.tar.gz
Source1:   README.fedora
Source2:   cron.daily
# build plugins separately
Patch0:    etckeeper-makefile-remove-python-plugins.patch
# see rhbz#1460461
Patch1:    etckeeper-1.18.7-fix-rpm-ignores.patch
# see rhbz#1480843
Patch2:    etckeeper-1.18.18-fix-hg-warnings.patch
# From https://bugs.launchpad.net/ubuntu/+source/etckeeper/+bug/1826855
Patch3:    etckeeper-add-breezy-python3-plugin.patch
# see rhbz#1762693 and https://github.com/ansible/ansible/issues/54949
# see also rhbz#1917461
Patch4:    etckeeper-1.18.18-fix-output-for-ansible.patch
# see rhbz#2203408 and pr#7
Patch5:    etckeeper-1.18.21-bz2203408.patch
BuildArch: noarch
BuildRequires: %{_bindir}/markdown_py
Requires:  git-core
Requires:  perl-interpreter
Requires:  crontabs
Requires:  findutils
Requires:  hostname
Requires:  which
%if 0%{?dnf_is_mandatory}
Requires:  %{name}-dnf = %{version}-%{release}
%endif # dnf_is_mandatory
BuildRequires:  systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The etckeeper program is a tool to let /etc be stored in a git,
mercurial, bzr or darcs repository. It hooks into yum to automatically
commit changes made to /etc during package upgrades. It tracks file
metadata that version control systems do not normally support, but that
is important for /etc, such as the permissions of /etc/shadow. It's
quite modular and configurable, while also being simple to use if you
understand the basics of working with version control.

The default backend is git, if want to use a another backend please
install the appropriate tool (mercurial, darcs or bzr).
%{?bazaar: To use bazaar/breezy as backend, please also install the %{name}-%{bazaar} package.}

To start using the package please read %{_pkgdocdir}/README.


%if 0%{?with_bzr}
%package bzr
Summary:  Support for bzr with etckeeper
BuildRequires: python2-devel
BuildRequires: bzr
Requires: %{name} = %{version}-%{release}
Requires: bzr

%description bzr
This package provides a bzr backend for etckeeper, if you want to use
etckeeper with bzr backend, install this package.
%endif # with_bzr


%if 0%{?with_brz}
%package brz
Summary:  Support for bzr with etckeeper (via breezy)
BuildRequires: python3-devel
BuildRequires: (python3-setuptools if python3-devel >= 3.12)
BuildRequires: brz
Requires: %{name} = %{version}-%{release}
Requires: brz

%description brz
This package provides a brz (breezy) backend for etckeeper, if you want to use
etckeeper with (bzr) bazaar repositories, install this package.
%endif # with_brz


%package dnf
Summary:  DNF plugin for etckeeper support
%if 0%{?dnf_uses_python3}
BuildRequires: python3-devel
BuildRequires: (python3-setuptools if python3-devel >= 3.12)
BuildRequires: python3-dnf
Requires: python3-dnf
%else
BuildRequires: python2-devel
BuildRequires: dnf
Requires: dnf
%endif # dnf_uses_python3
BuildRequires: dnf-plugins-core
BuildRequires: make
Requires: %{name} = %{version}-%{release}
Requires: dnf-plugins-core

%description dnf
This package provides a DNF plugin for etckeeper. If you want to use
etckeeper with DNF, install this package.


%prep
%autosetup -p1
%if 0%{?with_yum}
# we set yum here, so the yum plugin gets built, and change that to
# dnf later, if needed
sed -e 's|HIGHLEVEL_PACKAGE_MANAGER=.*|HIGHLEVEL_PACKAGE_MANAGER=yum|' \
%else
sed -e 's|HIGHLEVEL_PACKAGE_MANAGER=.*|HIGHLEVEL_PACKAGE_MANAGER=dnf|' \
%endif # with_yum
    -e 's|LOWLEVEL_PACKAGE_MANAGER=.*|LOWLEVEL_PACKAGE_MANAGER=rpm|' \
    -i etckeeper.conf
sed -e 's|^prefix=.*|prefix=%{_prefix}|' \
    -e 's|^bindir=.*|bindir=%{_bindir}|' \
    -e 's|^etcdir=.*|etcdir=%{_sysconfdir}|' \
    -e 's|^mandir=.*|mandir=%{_mandir}|' \
    -e 's|^vardir=.*|vardir=%{_localstatedir}|' \
    -e 's|^INSTALL=.*|INSTALL=install -p|' \
    -e 's|^CP=.*|CP=cp -pR|' \
    -e 's|^systemddir=.*|systemddir=%{_unitdir}|' \
    -i Makefile
# move each plugin in its own subdirectory, so each has its own build/
# directory
mkdir bzr-plugin ; mv etckeeper-bzr bzr-plugin
mkdir brz-plugin ; mv etckeeper-brz brz-plugin
mkdir dnf-plugin ; mv etckeeper-dnf dnf-plugin
cp -av %{SOURCE1} .


%build
%make_build

%if 0%{?with_bzr}
pushd bzr-plugin
%define py_setup etckeeper-bzr/__init__.py
%py2_build
popd
%endif # with_bzr

%if 0%{?with_brz}
pushd brz-plugin
%define py_setup etckeeper-brz/__init__.py
%py3_build
popd
%endif # with_brz

pushd dnf-plugin
%define py_setup etckeeper-dnf/etckeeper.py build
%if 0%{?dnf_uses_python3}
%py3_build
%else
%py2_build
%endif # dnf_uses_python3
popd

markdown_py -f README.html README.md


%install
%make_install

%if 0%{?with_bzr}
pushd bzr-plugin
%define py_setup etckeeper-bzr/__init__.py
%py2_install
popd
%endif # with_bzr

%if 0%{?with_brz}
pushd brz-plugin
%define py_setup etckeeper-brz/__init__.py
%py3_install
popd
%endif # with_brz

pushd dnf-plugin
%define py_setup etckeeper-dnf/etckeeper.py build
%if 0%{?dnf_uses_python3}
%py3_install
%else
%py2_install
%endif # dnf_uses_python3
popd

%if 0%{?dnf_is_mandatory}
sed -e 's|HIGHLEVEL_PACKAGE_MANAGER=.*|HIGHLEVEL_PACKAGE_MANAGER=dnf|' \
    -i %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
%endif # dnf_is_mandatory

install -D -p %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.daily/%{name}
install -d  %{buildroot}%{_localstatedir}/cache/%{name}


%post
if [ $1 -gt 1 ] ; then
   %{_bindir}/%{name} update-ignore
fi
%systemd_post %{name}.service
%systemd_post %{name}.timer


%preun
%systemd_preun %{name}.service
%systemd_preun %{name}.timer


%postun
%systemd_postun %{name}.service
%systemd_postun %{name}.timer


%files
%doc README.html README.fedora
%license GPL
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*.d
%{_sysconfdir}/%{name}/daily
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/cron.daily/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_%{name}
%if 0%{?with_yum}
%dir %{_prefix}/lib/yum-plugins
%{_prefix}/lib/yum-plugins/%{name}.*
%dir %{_sysconfdir}/yum/pluginconf.d
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/%{name}.conf
%endif # with_yum
%{_localstatedir}/cache/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer


%if 0%{?with_bzr}
%files bzr
%{python2_sitelib}/bzrlib/plugins/%{name}
# exclude egg-info dir, doesn't contain meaningful information
%exclude %{python2_sitelib}/bzr_%{name}-*.egg-info
%endif # with_bzr


%if 0%{?with_brz}
%files brz
# co-own the plugins directories
# breezy installs to sitearch
%dir %{python3_sitelib}/breezy/
%dir %{python3_sitelib}/breezy/plugins/
%{python3_sitelib}/breezy/plugins/%{name}/
# exclude egg-info dir, doesn't contain meaningful information
%exclude %{python3_sitelib}/brz_%{name}-*.egg-info
%endif # with_brz


%files dnf
%if 0%{?dnf_uses_python3}
%{python3_sitelib}/dnf-plugins/%{name}.py
%exclude %{python3_sitelib}/dnf-plugins/__init__.py
%{python3_sitelib}/dnf-plugins/__pycache__/%{name}.*
%exclude %{python3_sitelib}/dnf-plugins/__pycache__/__init__.*
# exclude egg-info dir, doesn't contain meaningful information
%exclude %{python3_sitelib}/dnf_%{name}-*.egg-info
%else
%{python2_sitelib}/dnf-plugins/%{name}.py*
%exclude %{python2_sitelib}/dnf-plugins/__init__.py*
# exclude egg-info dir, doesn't contain meaningful information
%exclude %{python2_sitelib}/dnf_%{name}-*.egg-info
%endif # dnf_uses_python3


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.18.21-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.18.21-2
- Rebuilt for Python 3.13

* Wed May  1 2024 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.21-1
- Update to 1.18.21.
- Add patch for rhbz#2203408 from pr#7.
- Depend on python3-dnf, not dnf (pr#6).

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Python Maint <python-maint@redhat.com> - 1.18.20-3
- Rebuilt for Python 3.12

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 28 2023 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.20-1
- Update to 1.18.20.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec  2 2022 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.18-1
- Update to 1.18.18.
- Rebase patches.
- Update patch to fix logging with Ansible (#1917461).
- BuildRequire setuptools when Python >= 3.12.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.18.17-2
- Rebuilt for Python 3.11

* Tue Mar  8 2022 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.17-1
- Update to 1.18.17.

* Wed Feb 16 2022 Todd Zullinger <tmz@pobox.com> - 1.18.16-6
- Require git-core instead of git

* Mon Jan 31 2022 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.16-5
- Exclude egg-info directories for dnf, bzr and brz plugins (#2048085).

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.18.16-2
- Rebuilt for Python 3.10

* Tue Feb  9 2021 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.16-1
- Update to 1.18.16.
- Update spec file, remove obsolete conditionals.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.18.14-2
- Rebuilt for Python 3.9

* Sat Mar 14 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.14-1
- Update to 1.18.14.
- Include zsh completion.
- Mark cron file as config file.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec  1 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.12-1
- Update to 1.18.12.
- New version of patch to fix logging with Ansible (#1762693).

* Tue Nov 19 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.10-6
- Add patch to fix logging with Ansible (#1762693).

* Fri Nov 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1.18.10-5
- Add breezy plugin on Fedora 31+
- Remove bazaar plugin on Fedora 32+
- https://fedoraproject.org/wiki/Changes/ReplaceBazaarWithBreezy

* Fri Oct  4 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.10-4
- Package fixes for CentOS8.
- Build dnf plugin on CentOS7.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.18.10-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Oct  3 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.10-2
- There is currently no bzr for rhel8.

* Thu Oct  3 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.10-1
- Update to 1.18.10.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.18.8-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.8-1
- Update to 1.18.8.
- Update URL: and Source: tags.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.18.7-4
- Rebuilt for Python 3.7

* Mon May 14 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.7-3
- Use correct Requires: for the hostname cmd on EPEL6.

* Sat Apr 21 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.7-2
- DNF is no longer available in EPEL7.

* Sat Apr 21 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.7-1
- Update to 1.18.7.
- Rebase patches.
- Slightly modernize spec file.
- Update Python dependencies.
- Fix ignore rules (rhbz#1460461).
- Update README.fedora (rhbz#1478655).
- Add missing BRs (rhbz#1418790).
- Add patch to prevent mercurial warnings (rhbz#1480843).

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.18.5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.18.5-4
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.18.5-2
- Rebuild for Python 3.6

* Tue Aug 23 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.5-1
- Update to 1.18.5.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar  2 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.3-2
- Move completion file back to /etc/bash_completion.d on EPEL<7.

* Mon Feb 22 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.3-1
- Update to 1.18.3.
- Bash completions have been moved to /usr/share/bash-completion.

* Wed Feb  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.2-4
- Do not own /etc/bash_completion.d on Fedora and EPEL>=7.
- Drop %%defattr.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 24 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.2-1
- Update to etckeeper 1.18.2.
- Depend on dnf for F22+ (rhbz#1229131).
- Minor changelog fixes.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.1-2
- Fix HTML generation from markdown (rhbz#1213776).

* Thu Mar 26 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.18.1-1
- Update to 1.18.1.
- Add missing dependency on python3-devel for dnf plugin on F23+.

* Fri Mar 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.18-1
- Update to 1.18.
- Update upstream URLs.
- Package DNF plugin.
- Slightly modernize spec file.

* Thu Dec 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.14-2
- Disable bzr plugin on epel5.

* Fri Sep  5 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.14-1
- Update to 1.14.

* Fri Aug 15 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.13-1
- Update to 1.13.

* Sun Jun 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.12-1
- Update to 1.12.
- Format README.md.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.11-1
- Update to 1.11.

* Sat Nov  9 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10-1
- Update to 1.10.

* Thu Sep 12 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.9-1
- Update to 1.9.

* Sun Aug 18 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.7-1
- Update to 1.7.
- Define (if undefined) and use _pkgdocdir macro (rhbz#993741).

* Tue Jul 30 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.6-1
- Update to 1.6.

* Sat Jul 27 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.5-1
- Update to 1.5.

* Sat Jul 27 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 1.4-2
- Add a missing requirement on crontabs to spec file

* Sun Jun 23 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4-1
- Update to 1.4.

* Fri May 10 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3-1
- Update to 1.3.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.64-1
- Update to 0.64.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun  4 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.63-1
- Update to 0.63.

* Tue Mar 13 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.62-2
- Add missing dependency on perl (bz 798563).

* Tue Mar 13 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.62-1
- Update to 0.62.

* Tue Jan 17 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.61-1
- Update to 0.61.

* Fri Jan 13 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.60-1
- Update to 0.60.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  1 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.58-1
- Update to 0.58.

* Wed Nov  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.57-1
- Update to 0.57.

* Wed Aug 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.56-2
- Rebuilt for trailing slash bug of rpm-4.9.1

* Thu Jul 21 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.56-1
- Update to 0.56.

* Fri Jun 24 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.55-1
- Update to 0.55.

* Wed Jun  1 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.54-1
- Update to 0.54.
- Add patch for bz 709487.

* Mon Mar 28 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.53-1
- Update to 0.53.
- Run update-ignore on package upgrade (bz 680632).

* Wed Feb  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.52-1
- Update to 0.52.
- Include a README.fedora (bz 670934).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.51-1
- Update to 0.51.
- etckeeper has been moved out of sbin.

* Sat Dec 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.50-2
- Don't package INSTALL.

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.50-1
- Update to 0.50.
- Change %%define -> %%global.

* Fri Sep 17 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.49-2
- Adjust minimum required version of GIT.
- egg-info files are not created automatically on RHEL5.

* Wed Sep 15 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.49-1
- Update to 0.49.
- Remove obsolete patch.

* Fri Sep  3 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.48-1
- Update to 0.48.
- Don't list /etc/etckeeper/*.d directories twice in %%files.
- Add patch from upstream that fixes bz 588086.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Sep 12 2009 Bernie Innocenti <bernie@codewiz.org> - 0.41-1
- Update to 0.41
- Add missing directory ownerships

* Sat Sep 12 2009 Bernie Innocenti <bernie@codewiz.org> - 0.40-3
- Make the bzr subpackage builddepend on python-devel

* Wed Sep 09 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.40-2
- Package is noarch
- Rpmlint clean
- Random cleanup
- Ship cache dir in package
- bzr subpackage
- Add bzr to buildreq

* Sat Sep 05 2009 Bernie Innocenti <bernie@codewiz.org> - 0.40-1
- Update to 0.40

* Sun Jun 14 2009 Bernie Innocenti <bernie@codewiz.org> - 0.37-1
- Update to 0.37
- Change license tag to GPLv2+

* Fri Feb 27 2009 Jimmy Tang <jtang@tchpc.tcd.ie> - 0.33-4
- fix up initial install to make directory in /var/cache/etckeeper
- install the etckeeper daily cron job
- define some config files that shouldn't be replaced, should the hooks
in commit.d, init.d etc... saved and not blown away? if so they can
defined as config files. etckeeper should record the changes anyway.

* Wed Feb 25 2009 Jimmy Tang <jtang@tchpc.tcd.ie> - 0.32-1
- yum etckeeper plugin is now apart of this package

* Tue Feb 24 2009 Jimmy Tang <jtang@tchpc.tcd.ie> - 0.31-1
- initial package
