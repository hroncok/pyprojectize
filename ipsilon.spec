# Bundling request for bootstrap/patternfly: https://fedorahosted.org/fpc/ticket/483

#%%global snapdate 20210601
#%%global commit b68a5e30ad98fca7e058b292f8f2abe6fa1e9e42
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})

# post-release format...
#%%global snaprel %%{?snapdate:.git%%{snapdate}.%%{shortcommit}}

# for rpmdev-bumpspec
%global baserelease 18

Name:       ipsilon
Version:    3.0.4
Release:    %{baserelease}%{?snaprel}%{?dist}
Summary:    An Identity Provider Server

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://pagure.io/ipsilon
%if %{defined snaprel}
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:    https://pagure.io/%{name}/archive/v%{version}/ipsilon-%{version}.tar.gz
%endif
Patch:      https://pagure.io/ipsilon/c/f45e9df2b79780a493bfd19f9f7522f51ca622f9.patch
Patch:      https://pagure.io/ipsilon/c/5d0b7d883dfd240248e86d4c06ba63186ecceb0c.patch
Patch:      0001-Fix-SAML2-metadata-regeneration.patch
Patch:      0002-remove-deprecated-autoescape-extension.patch
# https://pagure.io/ipsilon/pull-request/400
# enhancements to make life easier for Bodhi development environment
Patch:      0001-openidc-provider-respect-secure-no.patch
Patch:      0002-httpd-config-Listen-on-port-specified-in-hostname.patch
Patch:      0003-httpd-config-include-ServerName-directive.patch
Patch:      0004-openidcp-allow-setting-default-attribute-mapping-at-.patch
Patch:      0005-testauth-add-a-mechanism-to-specify-groups-via-usern.patch
# https://pagure.io/ipsilon/pull-request/405
# Don't confuse ProviderException.code with ProviderException.statuscode
Patch:      0001-Don-t-confuse-ProviderException.code-with-ProviderEx.patch
Patch:      0002-Fix-a-syntax-error.patch
# https://pagure.io/ipsilon/pull-request/406
# add token_introspection_endpoint to config to fix waiverdb token auth
# https://github.com/release-engineering/waiverdb/issues/219
Patch:      0003-openidc-add-token_introspection_endpoint-to-well-kno.patch
# https://pagure.io/ipsilon/pull-request/407
# also add introspection_endpoint, which should *really* fix it
Patch:      0001-openidc-also-set-introspection_endpoint.patch

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-lasso
BuildRequires:  python3-openid, python3-openid-cla, python3-openid-teams
BuildRequires:  python3-m2crypto
BuildRequires:  make

Requires:       python3-setuptools
Requires:       python3-requests
Requires:       %{name}-base = %{version}-%{release}

%description
Ipsilon is a multi-protocol Identity Provider service. Its function is to
bridge authentication providers and applications to achieve Single Sign On
and Federation.


%package base
Summary:        Ipsilon base IDP server
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       httpd
Requires:       mod_ssl
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-provider = %{version}-%{release}
Requires:       python3-mod_wsgi
Requires:       python3-cherrypy
Requires:       python3-jinja2
Requires:       python3-lxml
Requires:       python3-sqlalchemy
Requires:       open-sans-fonts
Requires:       font(fontawesome)
Requires:       pam
Requires(pre):  shadow-utils

%description base
The Ipsilon IdP server without installer


%package filesystem
Summary:        Package providing files required by Ipsilon
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

%description filesystem
Package providing basic directory structure required
for all Ipsilon parts


%package client
Summary:        Tools for configuring Ipsilon clients
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-saml2-base = %{version}-%{release}
Requires:       mod_auth_mellon
Requires:       mod_auth_openidc
Requires:       mod_ssl
Requires:       python3-requests
BuildArch:      noarch

%description client
Client install tools


%package tools-ipa
summary:        IPA helpers
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-authgssapi = %{version}-%{release}
Requires:       %{name}-authform = %{version}-%{release}
Requires:       %{name}-infosssd = %{version}-%{release}
%if 0%{?rhel}
Requires:       ipa-client
Requires:       ipa-admintools
%else
Requires:       freeipa-client
Requires:       freeipa-admintools
%endif
BuildArch:      noarch

%description tools-ipa
Convenience client install tools for IPA support in the Ipsilon identity Provider


%package saml2-base
Summary:        SAML2 base
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       openssl
Requires:       python3-lasso
Requires:       python3-lxml
BuildArch:      noarch

%description saml2-base
Provides core SAML2 utilities


%package saml2
Summary:        SAML2 provider plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-saml2-base = %{version}-%{release}
BuildArch:      noarch

%description saml2
Provides a SAML2 provider plugin for the Ipsilon identity Provider


%package openid
Summary:        Openid provider plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-openid
Requires:       python3-openid-cla
Requires:       python3-openid-teams
BuildArch:      noarch

%description openid
Provides an OpenId provider plugin for the Ipsilon identity Provider

%package openidc
Summary:        OpenID Connect provider plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-jwcrypto
BuildArch:      noarch

%description openidc
Provides an OpenID Connect and OAuth2 provider plugin for the Ipsilon
identity Provider


%package authform
Summary:        mod_intercept_form_submit login plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       mod_intercept_form_submit
BuildArch:      noarch

%description authform
Provides a login plugin to authenticate with mod_intercept_form_submit


%package authpam
Summary:        PAM based login plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-pam
BuildArch:      noarch

%description authpam
Provides a login plugin to authenticate against the local PAM stack


%package authgssapi
Summary:        mod_auth_gssapi based login plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       mod_auth_gssapi
BuildArch:      noarch

%description authgssapi
Provides a login plugin to allow authentication via the mod_auth_gssapi
Apache module.


%package authldap
Summary:        LDAP info and login plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-ldap
BuildArch:      noarch

%description authldap
Provides a login plugin to allow authentication and info retrieval via LDAP.


%package infofas
Summary:        Fedora Authentication System login plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-infosssd = %{version}-%{release}
BuildArch:      noarch

%description infofas
Provides an info plugin to retrieve info from the Fedora Authentication System


%package infosssd
Summary:        SSSD based identity plugin
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-sssdconfig
Requires:       sssd >= 1.12.4
BuildArch:      noarch

%description infosssd
Provides an info plugin to allow retrieval via SSSD.

%package theme-Fedora
Summary:        Fedora Account System theme
Requires:       %{name}-base = %{version}-%{release}
BuildArch:      noarch

%description theme-Fedora
Provides a theme for Ipsilon used for the Fedora Account System.

%package theme-openSUSE
Summary:        openSUSE Accounts theme
Requires:       %{name}-base = %{version}-%{release}
BuildArch:      noarch

%description theme-openSUSE
Provides a theme for Ipsilon used for openSUSE Accounts.

%prep
%if %{defined snaprel}
%autosetup -n %{name}-%{commit} -p1
%else
%autosetup -p1
%endif


%build
%py3_build


%install
%py3_install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libexecdir}/ipsilon
mkdir -p %{buildroot}%{_defaultdocdir}
mkdir -p %{buildroot}%{_localstatedir}/cache/ipsilon
# These 0700 permissions are because ipsilon will store private keys here
install -d -m 0700 %{buildroot}%{_sharedstatedir}/ipsilon
install -d -m 0700 %{buildroot}%{_sysconfdir}/ipsilon
mv %{buildroot}/%{_bindir}/ipsilon %{buildroot}/%{_libexecdir}/ipsilon/ipsilon
mv %{buildroot}/%{_bindir}/ipsilon-server-install %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_bindir}/ipsilon-upgrade-database %{buildroot}/%{_sbindir}
mv %{buildroot}%{_defaultdocdir}/%{name} %{buildroot}%{_defaultdocdir}/%{name}-%{version}
rm -fr %{buildroot}%{python3_sitelib}/tests
ln -s %{_datadir}/fonts %{buildroot}%{_datadir}/ipsilon/ui/fonts

mkdir -p  %{buildroot}%{_sysconfdir}/pam.d
cp %{buildroot}%{_datadir}/ipsilon/templates/install/pam/ipsilon.pamd %{buildroot}%{_sysconfdir}/pam.d/ipsilon

#%check
# The test suite is not being run because:
#  1. The last step of %%install removes the entire test suite
#  2. It increases build time a lot
#  3. It adds more build dependencies (namely postgresql server and client libraries)

%pre base
getent group ipsilon >/dev/null || groupadd -r ipsilon
getent passwd ipsilon >/dev/null || \
    useradd -r -g ipsilon -d %{_sharedstatedir}/ipsilon -s /sbin/nologin \
    -c "Ipsilon Server" ipsilon
exit 0


%files filesystem
%doc README.md
%license COPYING
%dir %{_datadir}/ipsilon
%dir %{_datadir}/ipsilon/templates
%dir %{_datadir}/ipsilon/templates/install
%dir %{python3_sitelib}/ipsilon
%{python3_sitelib}/ipsilon/__init__.py*
%{python3_sitelib}/ipsilon-*.egg-info
%dir %{python3_sitelib}/ipsilon/__pycache__/
%{python3_sitelib}/ipsilon/__pycache__/__init__.*
%dir %{python3_sitelib}/ipsilon/tools
%{python3_sitelib}/ipsilon/tools/__init__.py*
%{python3_sitelib}/ipsilon/tools/files.py*
%dir %{python3_sitelib}/ipsilon/tools/__pycache__
%{python3_sitelib}/ipsilon/tools/__pycache__/__init__.*
%{python3_sitelib}/ipsilon/tools/__pycache__/files.*

%files
%license COPYING
%{_sbindir}/ipsilon-server-install
%{_bindir}/ipsilon-db2conf
%{_datadir}/ipsilon/templates/install/*.conf
%{_datadir}/ipsilon/ui/saml2sp
%dir %{python3_sitelib}/ipsilon/helpers
%{python3_sitelib}/ipsilon/helpers/common.py*
%{python3_sitelib}/ipsilon/helpers/__init__.py*
%dir %{python3_sitelib}/ipsilon/helpers/__pycache__
%{python3_sitelib}/ipsilon/helpers/__pycache__/__init__.*
%{python3_sitelib}/ipsilon/helpers/__pycache__/common.*
%{_mandir}/man*/ipsilon-server-install.1*

%files base
%license COPYING
%doc examples doc
%{_defaultdocdir}/%{name}-%{version}
%{python3_sitelib}/ipsilon/admin
%{python3_sitelib}/ipsilon/authz
%{python3_sitelib}/ipsilon/rest
%{python3_sitelib}/ipsilon/tools/dbupgrade.py*
%{python3_sitelib}/ipsilon/tools/__pycache__/dbupgrade.*
%dir %{python3_sitelib}/ipsilon/login
%{python3_sitelib}/ipsilon/login/__init__*
%{python3_sitelib}/ipsilon/login/common*
%{python3_sitelib}/ipsilon/login/authtest*
%dir %{python3_sitelib}/ipsilon/login/__pycache__
%{python3_sitelib}/ipsilon/login/__pycache__/__init__*
%{python3_sitelib}/ipsilon/login/__pycache__/common*
%{python3_sitelib}/ipsilon/login/__pycache__/authtest*
%dir %{python3_sitelib}/ipsilon/info
%{python3_sitelib}/ipsilon/info/__init__*
%{python3_sitelib}/ipsilon/info/common*
%{python3_sitelib}/ipsilon/info/infonss*
%dir %{python3_sitelib}/ipsilon/info/__pycache__
%{python3_sitelib}/ipsilon/info/__pycache__/__init__*
%{python3_sitelib}/ipsilon/info/__pycache__/common*
%{python3_sitelib}/ipsilon/info/__pycache__/infonss*
%dir %{python3_sitelib}/ipsilon/providers
%{python3_sitelib}/ipsilon/providers/__init__*
%{python3_sitelib}/ipsilon/providers/common*
%dir %{python3_sitelib}/ipsilon/providers/__pycache__
%{python3_sitelib}/ipsilon/providers/__pycache__/__init__*
%{python3_sitelib}/ipsilon/providers/__pycache__/common*
%{python3_sitelib}/ipsilon/root.py*
%{python3_sitelib}/ipsilon/__pycache__/root.*
%{python3_sitelib}/ipsilon/util
%{python3_sitelib}/ipsilon/user
%{_mandir}/man*/ipsilon.7*
%{_mandir}/man*/ipsilon.conf.5*
%{_datadir}/ipsilon/templates/*.html
%{_datadir}/ipsilon/templates/admin
%{_datadir}/ipsilon/templates/user
%dir %{_datadir}/ipsilon/templates/login
%{_datadir}/ipsilon/templates/login/index.html
%{_datadir}/ipsilon/templates/login/form.html
%dir %{_datadir}/ipsilon/ui
%{_datadir}/ipsilon/ui/css
%{_datadir}/ipsilon/ui/img
%{_datadir}/ipsilon/ui/js
%{_datadir}/ipsilon/ui/fonts
%{_datadir}/ipsilon/ui/fonts-local
%{_libexecdir}/ipsilon/
%{_sbindir}/ipsilon-upgrade-database
%dir %attr(0751,root,root) %{_sharedstatedir}/ipsilon
%dir %attr(0751,root,root) %{_sysconfdir}/ipsilon
%dir %attr(0750,ipsilon,apache) %{_localstatedir}/cache/ipsilon
%config(noreplace) %{_sysconfdir}/pam.d/ipsilon
%dir %{_datadir}/ipsilon/themes

%files client
%license COPYING
%{_bindir}/ipsilon-client-install
%{_datadir}/ipsilon/templates/install/saml2
%{_datadir}/ipsilon/templates/install/openidc
%{_mandir}/man*/ipsilon-client-install.1*

%files tools-ipa
%license COPYING
%{python3_sitelib}/ipsilon/helpers/ipa.py*
%{python3_sitelib}/ipsilon/helpers/__pycache__/ipa.*

%files saml2-base
%license COPYING
%{python3_sitelib}/ipsilon/tools/saml2metadata.py*
%{python3_sitelib}/ipsilon/tools/certs.py*
%{python3_sitelib}/ipsilon/tools/__pycache__/saml2metadata.*
%{python3_sitelib}/ipsilon/tools/__pycache__/certs.*

%files saml2
%license COPYING
%{python3_sitelib}/ipsilon/providers/saml2*
%{python3_sitelib}/ipsilon/providers/__pycache__/saml2*
%{_datadir}/ipsilon/templates/saml2

%files openid
%license COPYING
%{python3_sitelib}/ipsilon/providers/openidp.py*
%{python3_sitelib}/ipsilon/providers/__pycache__/openidp.*
%{python3_sitelib}/ipsilon/providers/openid/
%{python3_sitelib}/ipsilon/providers/openid/__pycache__/
%{_datadir}/ipsilon/templates/openid

%files openidc
%license COPYING
%{python3_sitelib}/ipsilon/providers/openidcp.py*
%{python3_sitelib}/ipsilon/providers/__pycache__/openidcp.*
%{python3_sitelib}/ipsilon/providers/openidc/
%{python3_sitelib}/ipsilon/providers/openidc/__pycache__/
%{_datadir}/ipsilon/templates/openidc

%files authform
%license COPYING
%{python3_sitelib}/ipsilon/login/authform*
%{python3_sitelib}/ipsilon/login/__pycache__/authform*

%files authpam
%license COPYING
%{python3_sitelib}/ipsilon/login/authpam*
%{python3_sitelib}/ipsilon/login/__pycache__/authpam*
%{_datadir}/ipsilon/templates/install/pam

%files authgssapi
%license COPYING
%{python3_sitelib}/ipsilon/login/authgssapi*
%{python3_sitelib}/ipsilon/login/__pycache__/authgssapi*
%{_datadir}/ipsilon/templates/login/gssapi.html

%files authldap
%license COPYING
%{python3_sitelib}/ipsilon/login/authldap*
%{python3_sitelib}/ipsilon/info/infoldap*
%{python3_sitelib}/ipsilon/login/__pycache__/authldap*
%{python3_sitelib}/ipsilon/info/__pycache__/infoldap*

%files infosssd
%license COPYING
%{python3_sitelib}/ipsilon/info/infosssd.*
%{python3_sitelib}/ipsilon/info/__pycache__/infosssd*

%files infofas
%license COPYING
%{python3_sitelib}/ipsilon/info/infofas.*
%{python3_sitelib}/ipsilon/info/__pycache__/infofas*

%files theme-Fedora
%license COPYING
%{_datadir}/ipsilon/themes/Fedora

%files theme-openSUSE
%license COPYING
%{_datadir}/ipsilon/themes/openSUSE


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.4-18
- convert license to SPDX

* Thu Jul 18 2024 Adam Williamson <awilliam@redhat.com> - 3.0.4-17
- Backport PR #407 to really fix token introspection

* Thu Jul 18 2024 Adam Williamson <awilliam@redhat.com> - 3.0.4-16
- Backport PR #405 (don't confuse ProviderException.code with statuscode) (abompard)
- Backport PR #406 (add token_introspection_endpoint to config to fix waiverdb token auth)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Python Maint <python-maint@redhat.com> - 3.0.4-14
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 21 2023 Adam Williamson <awilliam@redhat.com> - 3.0.4-12
- Backport PR #400 to add needed features for Bodhi dev environment

* Fri Dec 8 2023 Francois Andrieu <darknao@drkn.ninja> - 3.0.4-11
- backport upstream patch 23b706f: Remove deprecated autoescape extension

* Sat Aug 12 2023 Francois Andrieu <darknao@drkn.ninja> - 3.0.4-10
- backport upstream patch 64a9d5e: Fix SAML2 metadata regeneration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Python Maint <python-maint@redhat.com> - 3.0.4-8
- Rebuilt for Python 3.12

* Wed Jun 28 2023 Kevin Fenzi <kevin@scrye.com> - 3.0.4-7
- Drop Requires on libsss_simpleifp as that no longer exists and isn't needed.
- Fixes rhbz#2217912 rhbz#2207913 rhbz#2113451

* Thu Mar 30 2023 Jerry James <loganjerry@gmail.com> - 3.0.4-6
- Change fontawesome-fonts R to match fontawesome 4.x

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.4-3
- Backport another upstream patch: 5d0b7d8

* Mon Jul 11 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.4-2
- Add an upstream patch: f45e9df

* Wed Jul 06 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.4-1
- Upgrade to 3.0.4

* Tue Jul 05 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.3-2
- Fix dependencies of infofas

* Tue Jul 05 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.3-1
- Upgrade to 3.0.3

* Thu Jun 23 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.2-1
- Upgrade to 3.0.2

* Wed May 25 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.1-2
- Drop patch, turns out it's harmful. Restore the executable name in libexec.

* Tue May 24 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.1-1
- Upgrade to 3.0.1

* Tue May 24 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-1
- Upgrade to 3.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-23.git20210601.b68a5e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-22.git20210601.b68a5e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-21.git20210601.b68a5e3
- Rebuilt for Python 3.10

* Tue Jun 01 2021 Neal Gompa <ngompa13@gmail.com> - 2.1.0-20.git20210601.b68a5e3
- Bump to new snapshot to split OTP field from the password field

* Thu Mar 18 2021 Neal Gompa <ngompa13@gmail.com> - 2.1.0-19.git20210318.b1d2ffe
- Bump to new snapshot to refresh Fedora theme with new Fedora logo

* Mon Mar 15 2021 Neal Gompa <ngompa13@gmail.com> - 2.1.0-18.git20210315.8c0e216
- Bump to new snapshot to refresh Fedora theme for FAS->Fedora Accounts change

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17.git20200618.c90a76b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Nils Philippsen <nils@redhat.com> - 2.1.0-16.git20200618.c90a76b
- Let saml2-base subpackage require openssl

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15.git20200618.c90a76b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-14.git20200618.c90a76b
- Bump to new snapshot

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-13.git20200428.f99a7d4
- Rebuilt for Python 3.9

* Tue May 05 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-12.git20200428.f99a7d4
- Bump to new snapshot

* Fri Apr 10 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-11.git20200301.171ffda
- Bump to new snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10.git20190910.aa89b1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-9.git20190910.aa89b1f
- Require python3-m2crypto, not just m2crypto (provided by python2-m2crypto)

* Tue Sep 10 2019 Neal Gompa <ngompa13@gmail.com> - 2.1.0-8.git20190910.aa89b1f
- Upgrade to git snapshot release
- Switch to Python 3

* Thu Jul 25 2019 Leigh Scott <leigh123linux@gmail.com> - 2.1.0-7
- Fix build issue

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 15 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.1.0-1
- Rebase to 2.1.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-5
- Removed dependency on mod_lookup_identity

* Tue Feb 14 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-4
- Added dependency on python-setuptools

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-2
- Add patch to fix RHBZ#1391445

* Thu Nov 24 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-1
- Upgrade to 2.0.2

* Mon Oct 31 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.1-1
- New release to enable authz allow on upgrade

* Fri Oct 28 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.0-1
- Rebase to Ipsilon 2.0.0

* Wed Aug 31 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-7
- Backport ipsilon-upgrade-database fix for configfile

* Wed Aug 10 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-6
- Move pam file to base package

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-4
- Backport unicode patches (RHBZ#1334637)

* Tue May 10 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-3
- Move user creation to -base subpackage (RHBZ#1334583)

* Tue May 03 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-2
- Install pam file

* Mon May 02 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-1
- Rebase to upstream 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1.1-2
- Fix files and requires

* Wed Oct 14 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1.1-1
- Rebase to upstream 1.1.1

* Tue Sep 08 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1.0-1
- Rebased to 1.1.0 release

* Fri Aug 21 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-5
- Backported some patches
- Fix for CVE-2015-5215/CVE-2015-5216/CVE-2015-5217

* Tue Aug 11 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-4
- Remove the gpg check

* Mon Jun 22 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-3
- Add mod_ssl dependency on ipsilon-client

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-1
- Update to release 1.0.0

* Mon Apr 20 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.6.0-1
- Update to release 0.6.0

* Mon Mar 30 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.0-1
- Update to release 0.5.0

* Mon Mar 02 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.4.0-1
- Update to release 0.4.0

* Wed Jan 28 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-5
- Split IPA tools

* Mon Jan 12 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-4
- Add symlink to fonts directory

* Tue Dec 16 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-3
- Fix typo
- Add comments on why the test suite is not in check
- The subpackages require the base package
- Add link to FPC ticket for bundling exception request

* Tue Dec 16 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-2
- Fix shebang removal

* Tue Dec 16 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-1
- Initial packaging
