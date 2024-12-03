%global commit 62ece4b929482702f5b2e716e3ee8998a29546cd
%global commitdate 20230224
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if %{defined commit}
%if 0%{?rhel} && 0%{?rhel} <= 7
%global snapshotversuffix +git%{commitdate}.%{shortcommit}
%else
%global snapshotversuffix ^git%{commitdate}.%{shortcommit}
%endif
%endif

Name:		openssh-ldap-authkeys
Version:	0.2.0%{?commit:%{snapshotversuffix}}
Release:	7%{?dist}
Summary:	Python script to generate SSH authorized_keys files using an LDAP directory

License:	MIT
URL:		https://github.com/fuhry/%{name}
%if %{defined commit}
Source0:	%{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildArch:	noarch

BuildRequires:	systemd-rpm-macros
BuildRequires:	python%{python3_pkgversion}-devel

# This is only for cases that we don't have a dependency generator active...
%if ! (%{defined python_enable_dependency_generator} || %{defined python_disable_dependency_generator})
Requires:	python%{python3_pkgversion}-ldap
Requires:	python%{python3_pkgversion}-dns
Requires:	python%{python3_pkgversion}-yaml
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
Requires:	%{name}-selinux = %{version}-%{release}
%else
Requires:	(%{name}-selinux = %{version}-%{release} if selinux-policy)
%endif


%description
openssh-ldap-authkeys is an implementation of AuthorizedKeysCommand for
OpenSSH 6.9 and newer that allows SSH public keys to be retrieved from
an LDAP source. It's provided for situations where a solution other
than 1:1 mapping is needed for users.

With SSH keys stored centrally in LDAP, revocation of a compromised
key is a quick and painless exercise for the user or IT department.

openssh-ldap-authkeys allows shared accounts to be fully auditable as
to who used them.


%if 0%{?el7}
%post
%sysusers_create %{name}.sysusers.conf
%tmpfiles_create %{name}.tmpfiles.conf
%endif


%files -f %{pyproject_files}
%doc README.md
%doc *.example
%{_bindir}/openssh-ldap-authkeys
%dir %{_sysconfdir}/%{name}
%ghost %config(noreplace) %{_sysconfdir}/%{name}/olak.yml
%ghost %config(noreplace) %{_sysconfdir}/%{name}/authmap
%{_tmpfilesdir}/openssh-ldap-authkeys.tmpfiles.conf
%{_sysusersdir}/openssh-ldap-authkeys.sysusers.conf

# -------------------------------------------------------------------

%package selinux
Summary:	SELinux module for %{name}
BuildRequires:	selinux-policy
BuildRequires:	selinux-policy-devel
BuildRequires:	make
%{?selinux_requires}

%description selinux
This package provides the SELinux policy module to ensure
%{name} runs properly under an environment with
SELinux enabled.

%pre selinux
%selinux_relabel_pre

%post selinux
%selinux_modules_install %{_datadir}/selinux/packages/olak.pp.bz2

%posttrans selinux
if [ $1 -eq 1 ] && /usr/sbin/selinuxenabled ; then
	fixfiles -FR %{name} restore || :
fi

%postun selinux
%selinux_modules_uninstall olak
if [ $1 -eq 0 ]; then
	%selinux_relabel_post
fi

%files selinux
%license COPYING
%attr(0600,-,-) %{_datadir}/selinux/packages/olak.pp.bz2
%{_datadir}/selinux/devel/include/contrib/olak.if
%{_mandir}/man8/olak_selinux.8*

# -------------------------------------------------------------------

%prep
%if %{defined commit}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build SELinux policy module
pushd selinux
make SHARE="%{_datadir}" TARGETS="olak"
popd


%install
%pyproject_install
%pyproject_save_files -l ldapauthkeys

# Make ghost entries for config files
touch %{buildroot}%{_sysconfdir}/%{name}/olak.yml
touch %{buildroot}%{_sysconfdir}/%{name}/authmap

# Delete example files, we'll docify them later
rm %{buildroot}%{_sysconfdir}/%{name}/*.example

# Install SELinux policy
install -d %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -d %{buildroot}%{_mandir}/man8/

install -m 644 selinux/olak.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
install -m 644 selinux/olak.if  %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -m 644 selinux/olak_selinux.8 %{buildroot}%{_mandir}/man8/


%check
%pyproject_check_import


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^git20230224.62ece4b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.0^git20230224.62ece4b-6
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^git20230224.62ece4b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^git20230224.62ece4b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^git20230224.62ece4b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.2.0^git20230224.62ece4b-2
- Rebuilt for Python 3.12

* Fri Feb 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0^git20230224.62ece4b-1
- Update to post-release snapshot
- Add SELinux subpackage

* Sat Jan 21 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.0~git20200205.aee4c46-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0~git20200205.aee4c46-3
- Rebuilt for Python 3.10

* Tue Apr 06 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.0~git20200205.aee4c46-2
- Correctly guard out manual dependencies

* Mon Apr 05 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.0~git20200205.aee4c46-1
- Build pre-release snapshot
