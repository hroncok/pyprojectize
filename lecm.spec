%global srcname lecm

Name:           %{srcname}
Version:        0.0.7
Release:        28%{?dist}

Summary:        Let's Encrypt Certificate Manager
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.io/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        lecm.cron
Source2:        lecm.1.gz


BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       acme-tiny
Requires:       python3-prettytable
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-pyOpenSSL

%description
Let's Encrypt Certificate Manager is an utility to ease the management
and renewal of Let's Encrypt SSL certificates.


%prep
%autosetup -n %{srcname}-%{version}
# NOTE(spredzy): We need to kee acme-tiny in the requirements in the tarball
# for user to still be able to use it fully from pip install, but the acme-tiny
# package does not install a python module but just the independant script. Hence
# the need for the sed command below.
sed -i '/acme-tiny/d' requirements.txt


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.d/lecm

mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/lecm.1.gz

mkdir -p %{buildroot}%{_datadir}/%{srcname}/sample/
install -p -m 0644 sample/*.conf %{buildroot}%{_datadir}/%{srcname}/sample/


%files
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info
%{_bindir}/%{srcname}
%{_datadir}/%{srcname}
%{_mandir}/man1/%{srcname}.1.gz
%config(noreplace) %{_sysconfdir}/cron.d/%{srcname}

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.7-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.7-26
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.7-22
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.7-19
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.7-16
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-13
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-10
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-2
- Rebuild for Python 3.6

* Fri Nov 18 2016 Yanis Guenane <yguenane@redhat.com> 0.0.7-1
- Service reload: Optimize the way services are reloaded #52
- Display a flag showing if conf and cert are in sync #51
- Allow user to force regenerate/renew certificates #50
- Renew: Do not fail when no certificate has already been generated #47

* Wed Nov 09 2016 Yanis Guenane <yguenane@redhat.com> 0.0.6-1
- doc: Added instal. documentation (pypi/debian) #37
- Print USAGE message when no parameter has been passed #43
- certificates: Allow one to use Let's Encrypt staging API #42
- setup.py: Fix url and add Python 3.5 support #41
- Travis: Add check for Python 3.5 #39
- certificates: Allow one to reload multiple service #38
- Fix mistake in the alias statement #36

* Thu Oct 27 2016 Yanis Guenane <yguenane@redhat.com> 0.0.5-1
- Deb and Rpm packaging
- Reload service only when necessary #29
- Add more sample to show how lecm address different situation #28
- Enforce proper SELinux context on generated files #25
- Have a default value for account_key_name #23

* Wed Sep 28 2016 Yanis Guenane <yguenane@redhat.com> 0.0.4-1
- Initial commit
