%bcond_without selinux
%global selinux_variants targeted
%global selinuxtype targeted
%global selinux_package_dir %{_datadir}/selinux/packages

%global logdir %{_localstatedir}/log/%{name}
%global modulename %{name}

Name:           cepces
Version:        0.3.9
Release:        %autorelease
Summary:        Certificate Enrollment through CEP/CES

License:        GPL-3.0-or-later
URL:            https://github.com/openSUSE/%{name}
Source0:        https://github.com/openSUSE/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python%{python3_pkgversion}-%{name} = %{version}-%{release}
%if %{with selinux}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

Recommends:     logrotate

Supplements:    %{name}-certmonger = %{version}-%{release}

%description
cepces is an application for enrolling certificates through CEP and CES.
It requires certmonger to operate.

Only simple deployments using Microsoft Active Directory Certificate Services
have been tested.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python part of %{name}

BuildRequires:  python3dist(cryptography) >= 1.2
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(gssapi)
BuildRequires:  python3dist(requests-gssapi)
BuildRequires:  python3-devel

Requires:       python3dist(setuptools)
Requires:       python3dist(cryptography) >= 1.2
Requires:       python3dist(requests)
Requires:       python3dist(gssapi)
Requires:       python3dist(requests-gssapi)

%description -n python%{python3_pkgversion}-%{name}
%{name} is an application for enrolling certificates through CEP and CES.
This package provides the Python part for CEP and CES interaction.

%package certmonger
Summary:        certmonger integration for %{name}
Requires(pre):  %{name} = %{version}-%{release}
Requires:       certmonger

%description certmonger
Installing %{name}-certmonger adds %{name} as a CA configuration.
Uninstall revert the action.

%if %{with selinux}
%package selinux
Summary:        SELinux support for %{name}

BuildRequires:  selinux-policy-devel

Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}

%description selinux
SELinux support for %{name}
#endif with selinux
%endif

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with selinux}
# Build the SELinux module(s).
for SELINUXVARIANT in %{selinux_variants}; do
    make %{?_smp_mflags} -C selinux clean all
    mv -v selinux/%{modulename}.pp selinux/%{modulename}-${SELINUXVARIANT}.pp
done
%endif

%install
%pyproject_install
%pyproject_save_files -l %{name}

install -d  %{buildroot}%{logdir}

%if %{with selinux}
# Install the SELinux module(s).
rm -fv selinux-files.txt

for SELINUXVARIANT in %{selinux_variants}; do
    install -d -m 755 %{buildroot}%{selinux_package_dir}/${SELINUXVARIANT}
    bzip2 selinux/%{modulename}-${SELINUXVARIANT}.pp
    MODULE_PATH=%{selinux_package_dir}/${SELINUXVARIANT}/%{modulename}.pp.bz2
    install -p -m 644 selinux/%{name}-${SELINUXVARIANT}.pp.bz2 \
      %{buildroot}${MODULE_PATH}

    echo ${MODULE_PATH} >> selinux-files.txt
done
#endif with selinux
%endif

# Configuration files
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/
install -m 644  conf/cepces.conf.dist  %{buildroot}%{_sysconfdir}/%{name}/cepces.conf
install -m 644  conf/logging.conf.dist %{buildroot}%{_sysconfdir}/%{name}/logging.conf

# Default logrotate file
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
cat <<EOF>%{buildroot}%{_sysconfdir}/logrotate.d/%{name}
/var/log/%{name}/*.log {
    compress
    delaycompress
    missingok
    rotate 4
}
EOF

%check
# Create a symlink so test can locate cepces_test
ln -s tests/cepces_test .
%{__python3} setup.py test

%if %{with selinux}
%pre selinux
for SELINUXVARIANT in %{selinux_variants}; do
    %selinux_relabel_pre -s ${SELINUXVARIANT}
done

%post selinux
for SELINUXVARIANT in %{selinux_variants}; do
    MODULE_PATH=%{selinux_package_dir}/${SELINUXVARIANT}/%{modulename}.pp.bz2
    %selinux_modules_install -s ${SELINUXVARIANT} ${MODULE_PATH}
done

%postun selinux
if [ $1 -eq 0 ]; then
    for SELINUXVARIANT in %{selinux_variants}; do
        %selinux_modules_uninstall -s ${SELINUXVARIANT} %{modulename}
    done
fi

%posttrans selinux
for SELINUXVARIANT in %{selinux_variants}; do
    %selinux_relabel_post -s ${SELINUXVARIANT}
done
#endif with selinux
%endif

%post certmonger
# Install the CA into certmonger.
if [[ "$1" == "1" ]]; then
    getcert add-ca -c %{name} \
      -e %{_libexecdir}/certmonger/%{name}-submit >/dev/null || :
fi

%preun certmonger
# Remove the CA from certmonger, unless it's an upgrade.
if [[ "$1" == "0" ]]; then
    getcert remove-ca -c %{name} >/dev/null || :
fi

%files
%doc README.rst
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/logging.conf
%attr(0700,-,-) %dir %{logdir}
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}

%files certmonger
%{_libexecdir}/certmonger/%{name}-submit

%if %{with selinux}
%files selinux -f selinux-files.txt
%endif

%changelog
%autochangelog
