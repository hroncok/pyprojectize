Name:       barman
Version:    3.11.1
Release:    1%{?dist}
Summary:    Backup and Recovery Manager for PostgreSQL
License:    GPL-3.0-only
URL:        http://www.pgbarman.org/
BuildArch:  noarch

Source0:    https://files.pythonhosted.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
Source1:    %{name}.cron
Source2:    %{name}.logrotate

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# https://docs.fedoraproject.org/en-US/packaging-guidelines/CronFiles/#_cron_job_files_packaging:
Requires:       cronie
Requires:       logrotate
Requires(pre):  shadow-utils
Requires:       rsync >= 3.0.4
Requires:       %{py3_dist argcomplete}
Requires:       %{py3_dist barman}

%description
Barman (Backup and Recovery Manager) is an open-source administration tool for
disaster recovery of PostgreSQL servers written in Python.

It allows your organization to perform remote backups of multiple servers in
business critical environments to reduce risk and help DBAs during the recovery
phase.

%package cli
Summary:    Client Utilities for Barman
Requires:   %{py3_dist barman}

%description cli
Client utilities for the integration of Barman in PostgreSQL clusters.

%package -n python3-barman
Summary:    Shared libraries for Barman
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-barman
Python libraries used by Barman.

%prep
%autosetup

# Change shebang in all relevant executable files in this directory and all subdirectories
find -type f -executable -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/

install -p -m 644 doc/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -p -m 644 doc/%{name}.d/* %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -m 644 scripts/%{name}.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}

sed -i 's|/etc/%{name}.d|/etc/%{name}/conf.d|g' %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%files
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(700,%{name},%{name}) %dir %{_sharedstatedir}/%{name}
%attr(755,%{name},%{name}) %dir %{_localstatedir}/log/%{name}

%files cli
%{_bindir}/%{name}-cloud-backup
%{_bindir}/%{name}-cloud-backup-delete
%{_bindir}/%{name}-cloud-backup-keep
%{_bindir}/%{name}-cloud-backup-list
%{_bindir}/%{name}-cloud-backup-show
%{_bindir}/%{name}-cloud-check-wal-archive
%{_bindir}/%{name}-cloud-restore
%{_bindir}/%{name}-cloud-wal-archive
%{_bindir}/%{name}-cloud-wal-restore
%{_bindir}/%{name}-wal-archive
%{_bindir}/%{name}-wal-restore
%{_mandir}/man1/%{name}-cloud-backup.1*
%{_mandir}/man1/%{name}-cloud-backup-delete.1.gz
%{_mandir}/man1/%{name}-cloud-backup-keep.1.gz
%{_mandir}/man1/%{name}-cloud-backup-list.1*
%{_mandir}/man1/%{name}-cloud-backup-show.1*
%{_mandir}/man1/%{name}-cloud-check-wal-archive.1.gz
%{_mandir}/man1/%{name}-cloud-restore.1*
%{_mandir}/man1/%{name}-cloud-wal-archive.1*
%{_mandir}/man1/%{name}-cloud-wal-restore.1*
%{_mandir}/man1/%{name}-wal-archive.1*
%{_mandir}/man1/%{name}-wal-restore.1*

%files -n python3-%{name}
%license LICENSE
%doc NEWS README.rst
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}/

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /bin/bash \
    -c "Backup and Recovery Manager for PostgreSQL" %{name}
exit 0

%changelog
* Sun Aug 25 2024 Simone Caronni <negativo17@gmail.com> - 3.11.1-1
- Update to 3.11.1.

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.10.1-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Simone Caronni <negativo17@gmail.com> - 3.10.1-1
- Update to 3.10.1.

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.10.0-2
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Simone Caronni <negativo17@gmail.com> - 3.10.0-1
- Update to 3.10.0.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Simone Caronni <negativo17@gmail.com> - 3.9.0-1
- Update to 3.9.0.

* Mon Sep 04 2023 Simone Caronni <negativo17@gmail.com> - 3.8.0-1
- Update to 3.8.0.

* Mon Aug 07 2023 Simone Caronni <negativo17@gmail.com> - 3.7.0-1
- Update to 3.7.0.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 3.6.0-2
- Rebuilt for Python 3.12

* Thu Jun 22 2023 Simone Caronni <negativo17@gmail.com> - 3.6.0-1
- Update to 3.6.0.

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.5.0-4
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Simone Caronni <negativo17@gmail.com> - 3.5.0-3
- Remove Python dependencies version, pep-0440 is enforced when building
  packages.

* Mon May 15 2023 Simone Caronni <negativo17@gmail.com> - 3.5.0-2
- Adjust Python dependencies.

* Mon May 08 2023 Simone Caronni <negativo17@gmail.com> - 3.5.0-1
- Update to 3.5.0.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Simone Caronni <negativo17@gmail.com> - 3.0.1-1
- Update to 3.0.1.

* Sat Jul 09 2022 Simone Caronni <negativo17@gmail.com> - 3.0.0-1
- Update to 3.0.0.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.17-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Simone Caronni <negativo17@gmail.com> - 2.17-1
- Update to 2.17.

* Fri Nov 26 2021 Charalampos Stratakis <cstratak@redhat.com> - 2.16-1
- Update to 2.16

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.12-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Francisco Javier Tsao Santín <tsao@disroot.org> - 2.12-1
- Update to 2.12.

* Tue Aug 18 2020 Simone Caronni <negativo17@gmail.com> - 2.11-1
- Update to 2.11.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Simone Caronni <negativo17@gmail.com> - 2.10-5
- Require cronie, not crontabs.

* Wed Jul 01 2020 Simone Caronni <negativo17@gmail.com> - 2.10-4
- Update SPEC file.
- Use macros where possible.
- Adjust Python requirements. Generator is already enforced on Fedora &
  CentOS/RHEL 8+.
- Install license and docs in python libraries, so they are always installed.
- Do not remove logs on uninstallation.
- Trim changelog.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.10-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.10-1
- RHBZ#1778773 Updated to 2.10 version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9-2
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.9-1
- RHBZ#1742344 Updated to 2.9 version

* Tue Jul 30 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-6
- RHBZ#1734137 fix python_provide macro in the right block of spec file

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-4
- RHBZ#1721158 fix typo that breaks config file

* Wed Jun 19 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-3
- RHBZ#1721158 updated spec in order to split package as recommended by upstream

* Thu May 16 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-2
- Minor fixes over previous commit

* Thu May 16 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-1
- Update to 2.8 version (fixes RHBZ#1707150)

* Wed Mar 20 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.7-1
- Update to 2.7 version

* Mon Feb 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5-3
- Enable python dependency generator

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
