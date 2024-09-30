%global srcname keylime
%global policy_version 38.1.0

# Package is actually noarch, but it has an optional dependency that is
# arch-specific.
%global debug_package %{nil}
%global with_selinux 1
%global selinuxtype targeted

Name:    keylime
Version: 7.10.0
Release: %autorelease
Summary: Open source TPM software for Bootstrapping and Maintaining Trust

URL:            https://github.com/keylime/keylime
Source0:        https://github.com/keylime/keylime/archive/refs/tags/v%{version}.tar.gz
Source1:        %{srcname}.sysusers
# The selinux policy for keylime is distributed via this repo: https://github.com/RedHat-SP-Security/keylime-selinux
Source2:        https://github.com/RedHat-SP-Security/%{name}-selinux/archive/v%{policy_version}/keylime-selinux-%{policy_version}.tar.gz

# Main program: Apache-2.0
# Icons: MIT
License: Apache-2.0 AND MIT

BuildRequires: git-core
BuildRequires: swig
BuildRequires: openssl-devel
BuildRequires: python3-devel
BuildRequires: python3-dbus
BuildRequires: python3-jinja2
BuildRequires: systemd-rpm-macros

Requires: python3-%{srcname} = %{version}-%{release}
Requires: %{srcname}-base = %{version}-%{release}
Requires: %{srcname}-verifier = %{version}-%{release}
Requires: %{srcname}-registrar = %{version}-%{release}
Requires: %{srcname}-tenant = %{version}-%{release}
Requires: %{srcname}-tools = %{version}-%{release}

# webapp was removed upstream in release 6.4.2.
Obsoletes: %{srcname}-webapp < 6.4.2

# python agent was removed upstream in release 7.0.0.
Obsoletes: python3-%{srcname}-agent < 7.0.0

# Agent.
Requires: keylime-agent
Suggests: %{srcname}-agent-rust

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

%{?python_enable_dependency_generator}
%description
Keylime is a TPM based highly scalable remote boot attestation
and runtime integrity measurement solution.

%package base
Summary: The base package contains the default configuration
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires(pre): python3-jinja2
Requires(pre): shadow-utils
Requires: procps-ng
Requires: tpm2-tss
Requires: openssl

%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Recommends:       (%{srcname}-selinux if selinux-policy-%{selinuxtype})
%endif

%ifarch %efi
Requires: efivar-libs
%endif


%description base
The base package contains the Keylime default configuration

%package -n python3-%{srcname}
Summary: The Python Keylime module
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}

Requires: python3-tornado
Requires: python3-sqlalchemy
Requires: python3-alembic
Requires: python3-cryptography
Requires: python3-pyyaml
Requires: python3-packaging
Requires: python3-requests
Requires: python3-gpg
Requires: python3-lark
Requires: python3-pyasn1
Requires: python3-pyasn1-modules
Requires: python3-jsonschema
Requires: python3-typing-extensions
Requires: tpm2-tools

%description -n python3-%{srcname}
The python3-keylime module implements the functionality used
by Keylime components.

%package verifier
Summary: The Python Keylime Verifier component
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}

%description verifier
The Keylime Verifier continuously verifies the integrity state
of the machine that the agent is running on.

%package registrar
Summary: The Keylime Registrar component
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}

%description registrar
The Keylime Registrar is a database of all agents registered
with Keylime and hosts the public keys of the TPM vendors.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             keylime SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom SELinux policy module
%endif

%package tenant
Summary: The Python Keylime Tenant
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}


%description tenant
The Keylime Tenant can be used to provision a Keylime Agent.

%package tools
Summary: Keylime tools
License: MIT

# Conflicts with the monolithic versions of the package, before the split.
Conflicts: keylime < 6.3.0-3

Requires: %{srcname}-base = %{version}-%{release}
Requires: python3-%{srcname} = %{version}-%{release}

%description tools
The keylime tools package includes miscelaneous tools.


%prep
%autosetup -S git -n %{srcname}-%{version} -a2

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module

make -f %{_datadir}/selinux/devel/Makefile %{srcname}.pp
bzip2 -9 %{srcname}.pp
%endif

%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}/%{_sharedstatedir}/%{srcname}
mkdir -p --mode=0700 %{buildroot}/%{_rundir}/%{srcname}

mkdir -p --mode=0700 %{buildroot}/%{_sysconfdir}/%{srcname}/
for comp in "verifier" "tenant" "registrar" "ca" "logging"; do
    mkdir -p --mode=0700  %{buildroot}/%{_sysconfdir}/%{srcname}/${comp}.conf.d
    install -Dpm 400 config/${comp}.conf %{buildroot}/%{_sysconfdir}/%{srcname}
done

# Ship some scripts.
mkdir -p %{buildroot}/%{_datadir}/%{srcname}/scripts
for s in create_runtime_policy.sh \
         create_mb_refstate \
         ek-openssl-verify; do
    install -Dpm 755 scripts/${s} \
        %{buildroot}/%{_datadir}/%{srcname}/scripts/${s}
done

# Ship configuration templates.
cp -r ./templates %{buildroot}%{_datadir}/%{srcname}/templates/

mkdir -p --mode=0755 %{buildroot}/%{_bindir}
install -Dpm 755 ./keylime/cmd/convert_config.py %{buildroot}/%{_bindir}/keylime_upgrade_config

%if 0%{?with_selinux}
install -D -m 0644 %{srcname}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{srcname}.pp.bz2
install -D -p -m 0644 keylime-selinux-%{policy_version}/%{srcname}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{srcname}.if
%endif

install -Dpm 644 ./services/%{srcname}_verifier.service \
    %{buildroot}%{_unitdir}/%{srcname}_verifier.service

install -Dpm 644 ./services/%{srcname}_registrar.service \
    %{buildroot}%{_unitdir}/%{srcname}_registrar.service

cp -r ./tpm_cert_store %{buildroot}%{_sharedstatedir}/%{srcname}/

install -p -d %{buildroot}/%{_tmpfilesdir}
cat > %{buildroot}/%{_tmpfilesdir}/%{srcname}.conf << EOF
d %{_rundir}/%{srcname} 0700 %{srcname} %{srcname} -
EOF

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{srcname}.conf

%pre base
%sysusers_create_compat %{SOURCE1}
exit 0

%post base
/usr/bin/keylime_upgrade_config --component ca --component logging >/dev/null
exit 0

%posttrans base
if [ -d %{_sysconfdir}/%{srcname} ]; then
    chmod 500 %{_sysconfdir}/%{srcname}
    chown -R %{srcname}:%{srcname} %{_sysconfdir}/%{srcname}

    for comp in "verifier" "tenant" "registrar" "ca" "logging"; do
        [ -d %{_sysconfdir}/%{srcname}/${comp}.conf.d ] && \
            chmod 500 %{_sysconfdir}/%{srcname}/${comp}.conf.d
    done
fi

[ -d %{_sharedstatedir}/%{srcname} ] && \
    chown -R %{srcname} %{_sharedstatedir}/%{srcname}/

[ -d %{_sharedstatedir}/%{srcname}/tpm_cert_store ] && \
    chmod 400 %{_sharedstatedir}/%{srcname}/tpm_cert_store/*.pem && \
    chmod 500 %{_sharedstatedir}/%{srcname}/tpm_cert_store/

[ -d %{_localstatedir}/log/%{srcname} ] && \
    chown -R %{srcname} %{_localstatedir}/log/%{srcname}/
exit 0

%post verifier
/usr/bin/keylime_upgrade_config --component verifier >/dev/null
%systemd_post %{srcname}_verifier.service

%post registrar
/usr/bin/keylime_upgrade_config --component registrar >/dev/null
%systemd_post %{srcname}_registrar.service

%post tenant
/usr/bin/keylime_upgrade_config --component tenant >/dev/null
exit 0

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{srcname}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
    # The services need to be restarted for the custom label to be
    # applied in case they where already present in the system,
    # restart fails silently in case they where not.
    for svc in registrar verifier; do
        [ -f "%{_unitdir}/%{srcname}_${svc}".service ] && \
            %systemd_postun_with_restart "%{srcname}_${svc}".service
    done
fi
exit 0

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{srcname}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%preun verifier
%systemd_preun %{srcname}_verifier.service

%preun registrar
%systemd_preun %{srcname}_registrar.service

%preun tenant
%systemd_preun %{srcname}_registrar.service

%postun verifier
%systemd_postun_with_restart %{srcname}_verifier.service

%postun registrar
%systemd_postun_with_restart %{srcname}_registrar.service

%files verifier
%license LICENSE
%attr(500,%{srcname},%{srcname}) %dir %{_sysconfdir}/%{srcname}/verifier.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{srcname},%{srcname}) %{_sysconfdir}/%{srcname}/verifier.conf
%{_bindir}/%{srcname}_verifier
%{_bindir}/%{srcname}_ca
%{_unitdir}/keylime_verifier.service

%files registrar
%license LICENSE
%attr(500,%{srcname},%{srcname}) %dir %{_sysconfdir}/%{srcname}/registrar.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{srcname},%{srcname}) %{_sysconfdir}/%{srcname}/registrar.conf
%{_bindir}/%{srcname}_registrar
%{_unitdir}/keylime_registrar.service

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{srcname}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{srcname}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{srcname}
%endif

%files tenant
%license LICENSE
%attr(500,%{srcname},%{srcname}) %dir %{_sysconfdir}/%{srcname}/tenant.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{srcname},%{srcname}) %{_sysconfdir}/%{srcname}/tenant.conf
%{_bindir}/%{srcname}_tenant

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}
%{_datadir}/%{srcname}/scripts/create_mb_refstate
%{_bindir}/keylime_attest
%{_bindir}/keylime_convert_runtime_policy
%{_bindir}/keylime_create_policy
%{_bindir}/keylime_sign_runtime_policy


%files tools
%license LICENSE
%{_bindir}/%{srcname}_userdata_encrypt

%files base
%license LICENSE
%doc README.md
%attr(500,%{srcname},%{srcname}) %dir %{_sysconfdir}/%{srcname}/{ca,logging}.conf.d
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{srcname},%{srcname}) %{_sysconfdir}/%{srcname}/ca.conf
%config(noreplace) %verify(not md5 size mode mtime) %attr(400,%{srcname},%{srcname}) %{_sysconfdir}/%{srcname}/logging.conf
%attr(700,%{srcname},%{srcname}) %dir %{_rundir}/%{srcname}
%attr(700,%{srcname},%{srcname}) %dir %{_sharedstatedir}/%{srcname}
%attr(500,%{srcname},%{srcname}) %dir %{_sharedstatedir}/%{srcname}/tpm_cert_store
%attr(400,%{srcname},%{srcname}) %{_sharedstatedir}/%{srcname}/tpm_cert_store/*.pem
%{_tmpfilesdir}/%{srcname}.conf
%{_sysusersdir}/%{srcname}.conf
%{_datadir}/%{srcname}/scripts/create_runtime_policy.sh
%{_datadir}/%{srcname}/scripts/ek-openssl-verify
%{_datadir}/%{srcname}/templates
%{_bindir}/keylime_upgrade_config

%files
%license LICENSE

%changelog
%autochangelog
