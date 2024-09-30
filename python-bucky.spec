%global forgeurl        https://github.com/trbs/bucky
%global commit          cda507241c8898c3a1926cae18371bce84be6d2c
%global forgesetupargs  -n bucky-%{commit}

Name:           python-bucky
Version:        2.3.1
Release:        %autorelease -p
Summary:        CollectD and StatsD adapter for Graphite
%forgemeta

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{forgeurl}

Source0:        %{forgesource}
Source1:        python-bucky-example.conf
Source2:        python-bucky-supervisord-example.conf

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
Bucky is a small server for collecting and translating metrics for\
Graphite. It can current collect metric data from CollectD daemons\
and from StatsD clients.

%description %_description

%package -n python3-bucky
Summary: %summary
Requires:       collectd
Requires:       python3-six
Requires:       python3-setuptools
Requires:       python3-watchdog
Requires:       python3-setproctitle
Requires:       python3-cryptography

%description -n python3-bucky %_description

%prep
%forgeautosetup
%{__install} -m 644 %{SOURCE2} .


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
# Delete the Python 2 executable so that the Python 3
# version can take it's place.
rm -rf %{_bindir}/bucky
%pyproject_install
%{__mkdir_p} %{buildroot}%{_localstatedir}/log/bucky
%{__mkdir_p} %{buildroot}%{_localstatedir}/run/bucky
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bucky
%{__install} -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bucky/bucky.conf


%pre
getent group bucky >/dev/null || groupadd -r bucky
getent passwd bucky >/dev/null || \
    useradd -r -g bucky -d / \
    -s /sbin/nologin -c "Bucky daemon" bucky


%postun
if [ $1 = 0 ]; then
  getent passwd bucky >/dev/null && \
      userdel -r bucky 2>/dev/null
fi

 
%files -n python3-bucky
%license LICENSE
%doc THANKS README.rst python-bucky-supervisord-example.conf
%{_bindir}/bucky
%attr(-,bucky,bucky) %{_localstatedir}/log/bucky
%attr(-,bucky,bucky) %{_localstatedir}/run/bucky
%config(noreplace) %{_sysconfdir}/bucky/bucky.conf
%{python3_sitelib}/bucky/
%{python3_sitelib}/bucky-%{version}.dist-info


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.1-0.1
- convert license to SPDX

* Sun Apr 09 2023 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.3.1-0.1.20230409gitcda5072
- Update BuildRequires to python3-cryptography (RHBZ#2061786)
- Update to 2.3.1 prerelease with support for python3-cryptography

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.0-4
- Subpackage python2-bucky has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.0-1
- Add Python 3 subpackage and modernize spec file
- Add a missing dependency on python2/3-crypto
- Update to version 2.3.0

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.2-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.2-8
- Python 2 binary package renamed to python2-bucky
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 22 2014 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.2.2-2
- Add python-watchdog requirement
- Add python-setproctitle requirement

* Sat Nov 22 2014 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 24 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.2.6-3
- Update requires (RHBZ#953834), adding python-setuptools

* Thu Sep 19 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.2.6-2
- Update requires (RHBZ#953834)

* Tue Sep 17 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Sat Aug 18 2012 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Mon May 14 2012 Jonathan Steffan <jsteffan@fedoraproject.org> - 0.1.0-1
- Initial package
