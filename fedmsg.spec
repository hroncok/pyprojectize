%global modname fedmsg

Name:           fedmsg
Version:        1.1.7
Release:        8%{?dist}
Summary:        Tools for Fedora Infrastructure real-time messaging
License:        LGPL-2.1-or-later
URL:            https://github.com/fedora-infra/fedmsg
BuildArch:      noarch
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Source2:        fedmsg-gateway-3.service
Source3:        fedmsg-hub-3.service
Source4:        fedmsg-irc-3.service
Source5:        fedmsg-relay-3.service

# Needed for compatibility with Python 3.12
Patch:          https://github.com/fedora-infra/fedmsg/pull/539.patch

BuildRequires:  gnupg
%{?systemd_requires}
BuildRequires:  systemd

# Docs requirements
BuildRequires:  python3-sphinx

# Python 3 requirements
BuildRequires:  python3-arrow
BuildRequires:  python3-click
BuildRequires:  python3-cryptography >= 1.6
BuildRequires:  python3-devel
BuildRequires:  python3-kitchen
BuildRequires:  python3-moksha-hub >= 1.3.2
BuildRequires:  python3-six
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-pyOpenSSL >= 16.1.0
BuildRequires:  python3-pygments
BuildRequires:  python3-psutil
BuildRequires:  python3-vcrpy
BuildRequires: make

# Finally, make the 'fedmsg' master package require all these components
Requires:       python3-fedmsg = %{version}-%{release}

%description
Python API used around Fedora Infrastructure to send and receive messages with
zeromq.  Includes some CLI tools.


%package base
Summary: Base file system layout for other fedmsg packages

%description base
This package contains some of the common filesystem layout shared by the
python2 and python3 versions of the fedmsg package.


%package doc
Summary: Documentation for the fedmsg library and CLI

%description doc
Documentation for the fedmsg library and CLI.


%package -n python3-fedmsg
Summary: Python 3 API and CLI for fedmsg
%{?python_provide:%python_provide python3-fedmsg}
Requires:       python3-arrow
Requires:       python3-click
Requires:       python3-cryptography >= 1.6
Requires:       python3-kitchen
Requires:       python3-moksha-hub >= 1.3.2
Requires:       python3-psutil
Requires:       python3-pygments
Requires:       python3-pyOpenSSL >= 16.1.0
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-zmq
Requires:       fedmsg-base = %{version}-%{release}

Conflicts:      python2-fedmsg < 1.1.1-7
Provides: python3-fedmsg-core = %{version}-%{release}
Obsoletes: python3-fedmsg-core < %{version}-%{release}

%description -n python3-fedmsg
Python 3 API used around Fedora Infrastructure to send and receive messages
with zeromq.


%prep
%autosetup -p1 -n %{modname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

make %{?_smp_mflags} -C doc SPHINXBUILD=sphinx-build-3 html PYTHONPATH=$(pwd)
rm doc/_build/html/.buildinfo


%check
PYTHONPATH=$(pwd) py.test-3 fedmsg

# Remove compiled .py files from config caused by the tests reading the config
rm -f %{buildroot}%{_sysconfdir}/fedmsg.d/*.py{c,o}


%install
%pyproject_install

# fedmsg provides a huge number of scripts and we need to move them all so the Python 2
# version is the un-versioned entry.
#
# config
mv %{buildroot}%{_bindir}/fedmsg-config %{buildroot}%{_bindir}/fedmsg-config-%{python3_version}
ln -s %{_bindir}/fedmsg-config-%{python3_version} %{buildroot}%{_bindir}/fedmsg-config-3
ln -s %{_bindir}/fedmsg-config-3 %{buildroot}%{_bindir}/fedmsg-config
# logger
mv %{buildroot}%{_bindir}/fedmsg-logger %{buildroot}%{_bindir}/fedmsg-logger-%{python3_version}
ln -s %{_bindir}/fedmsg-logger-%{python3_version} %{buildroot}%{_bindir}/fedmsg-logger-3
ln -s %{_bindir}/fedmsg-logger-3 %{buildroot}%{_bindir}/fedmsg-logger
# tail
mv %{buildroot}%{_bindir}/fedmsg-tail %{buildroot}%{_bindir}/fedmsg-tail-%{python3_version}
ln -s %{_bindir}/fedmsg-tail-%{python3_version} %{buildroot}%{_bindir}/fedmsg-tail-3
ln -s %{_bindir}/fedmsg-tail-3 %{buildroot}%{_bindir}/fedmsg-tail
# collectd
mv %{buildroot}%{_bindir}/fedmsg-collectd %{buildroot}%{_bindir}/fedmsg-collectd-%{python3_version}
ln -s %{_bindir}/fedmsg-collectd-%{python3_version} %{buildroot}%{_bindir}/fedmsg-collectd-3
ln -s %{_bindir}/fedmsg-collectd-3 %{buildroot}%{_bindir}/fedmsg-collectd
# announce
mv %{buildroot}%{_bindir}/fedmsg-announce %{buildroot}%{_bindir}/fedmsg-announce-%{python3_version}
ln -s %{_bindir}/fedmsg-announce-%{python3_version} %{buildroot}%{_bindir}/fedmsg-announce-3
ln -s %{_bindir}/fedmsg-announce-3 %{buildroot}%{_bindir}/fedmsg-announce
# trigger
mv %{buildroot}%{_bindir}/fedmsg-trigger %{buildroot}%{_bindir}/fedmsg-trigger-%{python3_version}
ln -s %{_bindir}/fedmsg-trigger-%{python3_version} %{buildroot}%{_bindir}/fedmsg-trigger-3
ln -s %{_bindir}/fedmsg-trigger-3 %{buildroot}%{_bindir}/fedmsg-trigger
# dg-replay
mv %{buildroot}%{_bindir}/fedmsg-dg-replay %{buildroot}%{_bindir}/fedmsg-dg-replay-%{python3_version}
ln -s %{_bindir}/fedmsg-dg-replay-%{python3_version} %{buildroot}%{_bindir}/fedmsg-dg-replay-3
ln -s %{_bindir}/fedmsg-dg-replay-3 %{buildroot}%{_bindir}/fedmsg-dg-replay
# check
mv %{buildroot}%{_bindir}/fedmsg-check %{buildroot}%{_bindir}/fedmsg-check-%{python3_version}
ln -s %{_bindir}/fedmsg-check-%{python3_version} %{buildroot}%{_bindir}/fedmsg-check-3
ln -s %{_bindir}/fedmsg-check-3 %{buildroot}%{_bindir}/fedmsg-check
# hub
mv %{buildroot}%{_bindir}/fedmsg-hub %{buildroot}%{_bindir}/fedmsg-hub-%{python3_version}
ln -s %{_bindir}/fedmsg-hub-%{python3_version} %{buildroot}%{_bindir}/fedmsg-hub-3
ln -s %{_bindir}/fedmsg-hub-3 %{buildroot}%{_bindir}/fedmsg-hub
# relay
mv %{buildroot}%{_bindir}/fedmsg-relay %{buildroot}%{_bindir}/fedmsg-relay-%{python3_version}
ln -s %{_bindir}/fedmsg-relay-%{python3_version} %{buildroot}%{_bindir}/fedmsg-relay-3
ln -s %{_bindir}/fedmsg-relay-3 %{buildroot}%{_bindir}/fedmsg-relay
# signing-relay
mv %{buildroot}%{_bindir}/fedmsg-signing-relay %{buildroot}%{_bindir}/fedmsg-signing-relay-%{python3_version}
ln -s %{_bindir}/fedmsg-signing-relay-%{python3_version} %{buildroot}%{_bindir}/fedmsg-signing-relay-3
ln -s %{_bindir}/fedmsg-signing-relay-3 %{buildroot}%{_bindir}/fedmsg-signing-relay
# gateway
mv %{buildroot}%{_bindir}/fedmsg-gateway %{buildroot}%{_bindir}/fedmsg-gateway-%{python3_version}
ln -s %{_bindir}/fedmsg-gateway-%{python3_version} %{buildroot}%{_bindir}/fedmsg-gateway-3
ln -s %{_bindir}/fedmsg-gateway-3 %{buildroot}%{_bindir}/fedmsg-gateway
# irc
mv %{buildroot}%{_bindir}/fedmsg-irc %{buildroot}%{_bindir}/fedmsg-irc-%{python3_version}
ln -s %{_bindir}/fedmsg-irc-%{python3_version} %{buildroot}%{_bindir}/fedmsg-irc-3
ln -s %{_bindir}/fedmsg-irc-3 %{buildroot}%{_bindir}/fedmsg-irc


%{__mkdir_p} %{buildroot}%{_sysconfdir}/fedmsg.d/
%{__cp} fedmsg.d/*.py %{buildroot}%{_sysconfdir}/fedmsg.d/.

%{__mkdir_p} %{buildroot}/%{_var}/run/%{modname}
%{__mkdir_p} %{buildroot}/%{_var}/log/%{modname}

%{__mkdir_p} %{buildroot}%{_unitdir}
%{__install} -Dm0644 %{SOURCE2} %{buildroot}%{_unitdir}/
%{__install} -Dm0644 %{SOURCE3} %{buildroot}%{_unitdir}/
%{__install} -Dm0644 %{SOURCE4} %{buildroot}%{_unitdir}/
%{__install} -Dm0644 %{SOURCE5} %{buildroot}%{_unitdir}/

ln -s ./fedmsg-hub-3.service %{buildroot}%{_unitdir}/fedmsg-hub.service
ln -s ./fedmsg-relay-3.service %{buildroot}%{_unitdir}/fedmsg-relay.service
ln -s ./fedmsg-irc-3.service %{buildroot}%{_unitdir}/fedmsg-irc.service
ln -s ./fedmsg-gateway-3.service %{buildroot}%{_unitdir}/fedmsg-gateway.service

# Logrotate configuration
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/logrotate.d
%{__install} logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{modname}
chmod 0644 %{buildroot}/%{_sysconfdir}/logrotate.d/%{modname}

# tmpfiles.d
%{__install} -Dm0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf


# Installation scriptlets
%pre base
%{_sbindir}/groupadd -r %{modname} &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d %{_datadir}/%{modname} -M \
                     -c 'FedMsg' -g %{modname} %{modname} &>/dev/null || :

# python3 scriptlets
%post -n python3-fedmsg
%systemd_post fedmsg-hub-3.service fedmsg-relay-3.service fedmsg-irc-3.service fedmsg-gateway-3.service

%preun -n python3-fedmsg
%systemd_preun fedmsg-hub-3.service fedmsg-relay-3.service fedmsg-irc-3.service fedmsg-gateway-3.service

%postun -n python3-fedmsg
%systemd_postun_with_restart fedmsg-hub-3.service fedmsg-relay-3.service fedmsg-irc-3.service fedmsg-gateway-3.service


%files
%license LICENSE
%doc README.rst


%files doc
%license LICENSE
%doc README.rst doc/_build/html


%files -n python3-fedmsg
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}.dist-info/
%{_bindir}/fedmsg-announce
%{_bindir}/fedmsg-announce-3*
%{_bindir}/fedmsg-collectd
%{_bindir}/fedmsg-collectd-3*
%{_bindir}/fedmsg-config
%{_bindir}/fedmsg-config-3*
%{_bindir}/fedmsg-gateway
%{_bindir}/fedmsg-gateway-3*
%{_bindir}/fedmsg-hub
%{_bindir}/fedmsg-hub-3*
%{_bindir}/fedmsg-irc
%{_bindir}/fedmsg-irc-3*
%{_bindir}/fedmsg-relay
%{_bindir}/fedmsg-relay-3*
%{_bindir}/fedmsg-logger
%{_bindir}/fedmsg-logger-3*
%{_bindir}/fedmsg-tail
%{_bindir}/fedmsg-tail-3*
%{_bindir}/fedmsg-trigger
%{_bindir}/fedmsg-trigger-3*
%{_bindir}/fedmsg-dg-replay
%{_bindir}/fedmsg-dg-replay-3*
%{_bindir}/fedmsg-signing-relay
%{_bindir}/fedmsg-signing-relay-3*
%{_bindir}/fedmsg-check
%{_bindir}/fedmsg-check-3*
%{_unitdir}/fedmsg-hub.service
%{_unitdir}/fedmsg-hub-3.service
%{_unitdir}/fedmsg-relay.service
%{_unitdir}/fedmsg-relay-3.service
%{_unitdir}/fedmsg-irc.service
%{_unitdir}/fedmsg-irc-3.service
%{_unitdir}/fedmsg-gateway.service
%{_unitdir}/fedmsg-gateway-3.service


%files base
%license LICENSE
%doc README.rst
%attr(755, %{modname}, %{modname}) %dir %{_var}/log/%{modname}
%attr(775, %{modname}, %{modname}) %dir %{_var}/run/%{modname}
%dir %{_sysconfdir}/fedmsg.d/
%config(noreplace) %{_sysconfdir}/fedmsg.d/*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{modname}
%{_tmpfilesdir}/%{name}.conf


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.1.7-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Maxwell G <maxwell@gtmx.me> - 1.1.7-4
- Remove unused python3-mock dependency

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.1.7-2
- Rebuilt for Python 3.12

* Fri Mar 31 2023 Michal Konecny <mkonecny@redhat.com> - 1.1.7-1
- Bump to version 1.1.7
  See changelog at https://github.com/fedora-infra/fedmsg/releases/tag/1.1.7

* Mon Feb 27 2023 Michal Konecny <mkonecny@redhat.com> - 1.1.6-1
- Latest upstream
  See changelog at https://github.com/fedora-infra/fedmsg/releases/tag/1.1.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 msuchy <msuchy@redhat.com> 1.1.2-10
- migrate to SPDX license

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 1.1.2-8
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.2-5
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Timothée Ravier <travier@redhat.com> - 1.1.2-2
- /var/run -> /run in tmpfiles.d config

* Sun Sep 20 2020 Kevin Fenzi <kevin@scrye.com> - 1.1.2-1
- Update to 1.1.2. Fixes 1880772

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-10
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Subpackage python2-fedmsg has been removed
  See https://bugzilla.redhat.com/show_bug.cgi?id=1737530

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.7

* Tue Mar 20 2018 Jeremy Cline <jeremy@jcline.org> - 1.1.1-1
- Update to the latest upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Jeremy Cline <jeremy@jcline.org> - 1.1.0-1
- Update to latest upstream

* Thu Sep 14 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-4
- Move python3-fedmsg-core obsoletes/provides to python3 subpackage
- Resolves: rhbz#1491625

* Wed Sep 13 2017 Jeremy Cline <jeremy@jcline.org> - 1.0.1-3
- Add a missing provides/obsoletes for python3-fedmsg-core

* Tue Sep 12 2017 Jeremy Cline <jeremy@jcline.org> - 1.0.1-2
- Provide the python- versions of the old sub-packages

* Tue Sep 12 2017 Jeremy Cline <jeremy@jcline.org> - 1.0.1-1
- Update to latest upstream

* Tue Aug 22 2017 Jeremy Cline <jeremy@jcline.org> - 1.0.0-1
- Update to latest upstream
- Provide Python 3 builds
- Combine many of the subpackages

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.0-1
- Update to the latest upstream release.
- Switch from m2crypto to cryptography/pyOpenSSL
- Re-enable tests.

* Wed Jun 28 2017 Jeremy Cline <jeremy@jcline.org> - 0.18.4-1
- Update to latest upstream release (#1465692).

* Sat May 27 2017 Kevin Fenzi <kevin@scrye.com> - 0.18.3-2
- Change python3-pkgvers-macros to new python3-rpm-macros package.
- Disable tests for now until they can be fixed.

* Wed Apr 12 2017 Ralph Bean <rbean@redhat.com> - 0.18.3-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.18.2-1
- New version

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 0.18.1-2
- Rebuild for Python 3.6

* Thu Dec 01 2016 Ralph Bean <rbean@redhat.com> - 0.18.1-1
- new version

* Thu Nov 10 2016 Ralph Bean <rbean@redhat.com> - 0.18.0-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 0.17.2-1
- new version

* Thu Mar 03 2016 Ralph Bean <rbean@redhat.com> - 0.16.4-1
- new version

* Thu Mar 03 2016 Ralph Bean <rbean@redhat.com> - 0.16.3-1
- new version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Ralph Bean <rbean@redhat.com> - 0.16.2-6
- Replace manual Provides with the python_provide macro.

* Sun Nov 15 2015 Ralph Bean <rbean@redhat.com> - 0.16.2-5
- Rename subpackges to explicit python2 prefixes and add Provides
  on the old names.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Oct 29 2015 Ralph Bean <rbean@redhat.com> - 0.16.2-3
- Only pull in python3-pkgversion-macros on f22 and later and epel7.

* Sat Oct 24 2015 Ralph Bean <rbean@redhat.com> - 0.16.2-2
- Create the fedmsg user in the fedmsg-base subpackage for rhbz#1274973.

* Thu Oct 08 2015 Ralph Bean <rbean@redhat.com> - 0.16.2-1
- new version

* Fri Oct 02 2015 Ralph Bean <rbean@redhat.com> - 0.16.1-4
- Remove commands after py3 installation step.  Let the python2
  install step re-install them.

* Wed Sep 23 2015 Ralph Bean <rbean@redhat.com> - 0.16.1-3
- Knock 'daemon' out of setuptools requirements as it's only
  really needed on el6.

* Wed Sep 23 2015 Ralph Bean <rbean@redhat.com> - 0.16.1-2
- Knock 'cryptography' out of the setuptools requirements for epel7.

* Wed Sep 23 2015 Ralph Bean <rbean@redhat.com> - 0.16.1-1
- new version

* Sat Sep 05 2015 Ralph Bean <rbean@redhat.com> - 0.16.0-1
- new version

* Thu Aug 27 2015 Nathaniel Yazdani <nyazdani@redhat.com> - 0.15.0-3
- Move duplicate fedmsg-collectd out of python-fedmsg-commands
- Remove unneeded python-daemon and python-moksha-hub dependencies from python-fedmsg-commands
- Add missing python-daemon dependency to python-fedmsg-consumers

* Wed Aug 26 2015 Ralph Bean <rbean@redhat.com> - 0.15.0-2
- Swap order of py2 and py3 in the install section for #1255974.

* Wed Aug 19 2015 Ralph Bean <rbean@redhat.com> - 0.15.0-1
- new version

* Mon Jun 29 2015 Ralph Bean <rbean@redhat.com> - 0.14.1-1
- new version

* Mon Jun 29 2015 Ralph Bean <rbean@redhat.com> - 0.14.0-4
- Added dep on python-kitchen.

* Thu Jun 25 2015 Ralph Bean <rbean@redhat.com> - 0.14.0-3
- Try getting the package ready for EPEL7 + python34.

* Thu Jun 25 2015 Ralph Bean <rbean@redhat.com> - 0.14.0-2
- Add omitted 'fedmsg' package back in.

* Thu Jun 25 2015 Ralph Bean <rbean@redhat.com> - 0.14.0-1
- Enable python3 subpackage
- Split fedmsg into lots of smaller subpackages to accomodate python3.

* Tue Jun 23 2015 Ralph Bean <rbean@redhat.com> - 0.13.3-1
- new version

* Tue Jun 23 2015 Ralph Bean <rbean@redhat.com> - 0.13.2-1
- new version

* Wed Jun 17 2015 Ralph Bean <rbean@redhat.com> - 0.13.1-4
- Re-enable cert validation for end clients.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Ralph Bean <rbean@redhat.com> - 0.13.1-2
- Fix logrotate mode.

* Thu Apr 23 2015 Ralph Bean <rbean@redhat.com> - 0.13.1-1
- new version
- add dep on python-six
- adjust ownership of fedmsg.d/ files.

* Wed Apr 15 2015 Ralph Bean <rbean@redhat.com> - 0.13.0-1
- new version

* Tue Mar 24 2015 Ralph Bean <rbean@redhat.com> - 0.12.3-1
- new version

* Sun Mar 22 2015 Ralph Bean <rbean@redhat.com> - 0.12.2-2
- No longer package compiled py files in /etc/fedmsg.d/

* Thu Feb 19 2015 Ralph Bean <rbean@redhat.com> - 0.12.2-1
- new version

* Thu Feb 19 2015 Ralph Bean <rbean@redhat.com> - 0.12.1-1
- new version

* Tue Feb 10 2015 Ralph Bean <rbean@redhat.com> - 0.12.0-2
- rebuilt

* Tue Feb 10 2015 Ralph Bean <rbean@redhat.com> - 0.12.0-1
- new version
- Drop test suite patch.

* Fri Nov 07 2014 Ralph Bean <rbean@redhat.com> - 0.11.1-1
- Latest upstream.
- Systemd services now restart on failure.
- Items in the conglomerators are now de-duplicated (bodhi).
- You can now call .tail_messages() while configured for active mode (koschei).
- Apply patch to try and get tests passing in koji again.

* Thu Oct 30 2014 Luke Macken <lmacken@redhat.com> - 0.11.0-3
- Add a tmpfiles.d configuration for /var/run/fedmsg
- Make the runtime path group-writable

* Wed Oct 22 2014 Luke Macken <lmacken@redhat.com> - 0.11.0-2
- Fix the permissions on the systemd service files

* Thu Oct 09 2014 Ralph Bean <rbean@redhat.com> - 0.11.0-1
- Fix harmless error about twisted.words at daemon startup.
- Optional shortening of links in IRC.
- IRC bot now reconnects when dropped.
- New fedmsg.meta.msg2long_form API.

* Wed Aug 27 2014 Ralph Bean <rbean@redhat.com> - 0.10.0-1
- New conglomerate API.
- New dep on python-arrow.

* Fri Aug 08 2014 Ralph Bean <rbean@redhat.com> - 0.9.3-1
- Fix broken default config.  Disable backlog out of the box.

* Fri Aug 08 2014 Ralph Bean <rbean@redhat.com> - 0.9.2-1
- Remove patches.

* Thu Jul 24 2014 Ralph Bean <rbean@redhat.com> - 0.9.1-3
- Update patch.

* Thu Jul 24 2014 Ralph Bean <rbean@redhat.com> - 0.9.1-2
- Bring in two patches from upstream to fix issues on el7.

* Fri Jul 18 2014 Ralph Bean <rbean@redhat.com> - 0.9.1-1
- Upstream releases with fixes for el6.

* Fri Jul 18 2014 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- Daemons can now process backlog at startup.
- New fedmsg-dg-replay command for debugging.
- Reorganized docs, especially the topics section.
- New dep on python-psutil.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Ralph Bean <rbean@redhat.com> - 0.8.0-1
- Latest upstream with new monitoring capabilities.
- fedmsg-tweet is retired.

* Tue Mar 25 2014 Ralph Bean <rbean@redhat.com> - 0.7.7-2
- Added ownership of /etc/fedmsg.d/

* Tue Mar 25 2014 Ralph Bean <rbean@redhat.com> - 0.7.7-1
- fedmsg-config and fedmsg-tail now share the --query option.
- Added a deployment doc.
- New fedmsg.crypto.validate_signed_by convenience function.
- Username is now automatically appended to the fedmsg-logger meta subtitle.
- A UserWarning is now issued if no fedmsg.meta plugins are found.
- Fixed the fedmsg.meta __name__ regex.
- Removed TCP_KEEPALIVE debug statements.

* Fri Feb 21 2014 Ralph Bean <rbean@redhat.com> - 0.7.6-2
- Copy test config into the test directory before building.

* Fri Feb 21 2014 Ralph Bean <rbean@redhat.com> - 0.7.6-1
- Latest upstream.
- New option to fedmsg-config to query for particular values.
- Avoid pkg_resources warning.

* Sun Feb 09 2014 Ralph Bean <rbean@redhat.com> - 0.7.5-1
- Latest upstream.
- Gource tail is removed.
- Fixes to fedmsg-tail.
- Updated documentation.
- Messages now carry a 'crypto' field indicating their sig type.
- Seamless switching between x509 and gpg crypto validation.

* Wed Jan 15 2014 Ralph Bean <rbean@redhat.com> - 0.7.4-1
- Latest upstream.
- Protect against NotImplementedError in fedmsg-tail.
- Fix documentation templates for broader compatibility with python tools.
- Scrub "None" links from the irc bot.

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.2-2
- Change BuildRequires from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Wed Nov 13 2013 Ralph Bean <rbean@redhat.com> - 0.7.2-1
- Latest upstream.
- Cap message timestamp at the second-level precision.
- Automatically listify endpoints.
- Code cleaning.

* Fri Sep 27 2013 Ralph Bean <rbean@redhat.com> - 0.7.1-2
- Remove old patch.

* Fri Sep 27 2013 Ralph Bean <rbean@redhat.com> - 0.7.1-1
- Bugfix to parsing certificate revocation list serials.

* Fri Sep 06 2013 Ralph Bean <rbean@redhat.com> - 0.7.0-5
- Fix that messed up sed statement.

* Fri Sep 06 2013 Ralph Bean <rbean@redhat.com> - 0.7.0-4
- Temporarily disable message validation by default.

* Thu Sep 05 2013 Ralph Bean <rbean@redhat.com> - 0.7.0-3
- Patch tests to use socket.gethostname consistently.

* Thu Sep 05 2013 Ralph Bean <rbean@redhat.com> - 0.7.0-2
- Knock out sqlalchemy test dep.

* Thu Sep 05 2013 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- Latest upstream.
- Add new fedmsg-trigger command.
- Remove the gpg and replay tests for now.
- Conditionalize systemd requirement.

* Tue Aug 06 2013 Dennis Gilmore <dennis@ausil.us> - 0.6.8-6
- BuildRequire systemd

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Ralph Bean <rbean@redhat.com> - 0.6.8-4
- Make file ownership over /etc/fedmsg.d explicit per sub-package.

* Mon Mar 25 2013 Ralph Bean <rbean@redhat.com> - 0.6.8-3
- Added forgotten mkdir for %%{buildroot}%%{_unitdir}

* Mon Mar 25 2013 Ralph Bean <rbean@redhat.com> - 0.6.8-2
- Moved .service files from a dbus folder to a systemd folder
  https://github.com/fedora-infra/fedmsg/issues/125
- Marked .service files as no longer %%config files.

* Mon Mar 04 2013 Ralph Bean <rbean@redhat.com> - 0.6.8-1
- New fedmsg-tail --gource option for visualizations.
- fedmsg-tweet reorganized to be more similar to other daemons.

* Thu Jan 31 2013 Ralph Bean <rbean@redhat.com> - 0.6.7-1
- Configurable colors for fedmsg-irc
- Better error checking in fedmsg-tweet
- Enhanced docs.

* Sun Jan 27 2013 Ralph Bean <rbean@redhat.com> - 0.6.6-2
- Disable sysv %%preun sections for Fedora

* Mon Jan 21 2013 Ralph Bean <rbean@redhat.com> - 0.6.6-1
- Typofix.
- Support loading remote CA cert for end-user message validation.

* Mon Jan 21 2013 Ralph Bean <rbean@redhat.com> - 0.6.5-1
- Latest upstream
- Fix JSON encoding between php and python
- Stop fedmsg-tweet from falling over.
- Improved logging.
- Improved crl cache location; don't keep it in /tmp/
- Fix a crl permissions issue with fedmsg-tail.
- Remove duplicate help strings for commands.
- Added systemd service files.
- Multiple outbound relay endpoints are now possible.
- Removed old chkconfig statements.

* Fri Dec 07 2012 Ralph Bean <rbean@redhat.com> - 0.6.3-2
- Removed a file that shouldn't have been included.

* Wed Dec 05 2012 Ralph Bean <rbean@redhat.com> - 0.6.3-1
- Use python-logutils for dictConfig on py2.6.
- Attempt to fixup rhel conditionals.
- Added test dependency on python-six and python-mock.

* Wed Dec 05 2012 Ralph Bean <rbean@redhat.com> - 0.6.2-1
- New support for zmq_tcp_keepalive.
- New logging config.
- Simplified fedmsg.commands internally.

* Tue Nov 27 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Stripped fedmsg.text out into its own plugin module.
- Commands are now defined as classes and use the logging module.
- Bugfixes to fedmsg-collectd.
- Renamed fedmsg-tweet.ini to fedmsg-tweet.init.

* Thu Nov 15 2012 Ralph Bean <rbean@redhat.com> - 0.6.0-1
- New upstream version.
- New service and subpackage: fedmsg-tweet.
- New command and subpackage: fedmsg-announce.
- New command and subpackage: fedmsg-collectd.
- New routing_policy config and extension of fedmsg.crypto.
- New functions in fedmsg.text to extract usernames and packages for a msg.
- Updated docs
- Pull in logrotate configuration from upstream.
- Updated rhel conditionals.
- Remove old temporary BR on orbited

* Wed Nov 14 2012 Ralph Bean <rbean@redhat.com> - 0.5.6-2
- Added a logrotate configuration.

* Thu Oct 25 2012 Ralph Bean <rbean@redhat.com> - 0.5.6-1
- More fedmsg.text enhancements.
- New fedmsg-collectd command.
- Reenabled test_text.py

* Tue Oct 23 2012 Ralph Bean <rbean@redhat.com> - 0.5.5-1
- Lots of work on enhancing and simplifying fedmsg.text from Luke Macken.
- Remove test_text.py since it now depends on test_hub.py

* Tue Oct 09 2012 Ralph Bean <rbean@redhat.com> - 0.5.4-4
- Disable those few tests that require network connectivity for koji.

* Tue Oct 09 2012 Ralph Bean <rbean@redhat.com> - 0.5.4-3
- BuildRequires on python-pygments.

* Tue Oct 09 2012 Ralph Bean <rbean@redhat.com> - 0.5.4-2
- BuildRequires on python-pygments.

* Mon Oct 08 2012 Ralph Bean <rbean@redhat.com> - 0.5.4-1
- New mediawiki, tagger, and git icons in fedmsg.text.
- Create symlink of dev_certs in build section so tests can pass.
- Re-enable the test suite in %%check again.
- fedmsg.text entries for tagger rank changes.
- Updated default FI endpoints (for staging).
- Remove full text from mediawiki messages to reduce spam.
- Recursively merge dicts in /etc/fedmsg.d/

* Fri Oct 05 2012 Ralph Bean <rbean@redhat.com> - 0.5.3-1
- Icons and fedmsg.text support for fedmsg-notify
- Re-disabled the tests to get a quick release out for fedmsg-notify.

* Thu Oct 04 2012 Luke Macken <lmacken@redhat.com> - 0.5.2-2
- Re-enable the test suite in %%check which got accidently removed.

* Wed Oct 03 2012 Ralph Bean <rbean@redhat.com> - 0.5.2-1
- Allow timeout when connecting to a non-existant fedmsg-relay
- fedmsg.text entries for new lookaside messages
- fedmsg.text groundwork support for icons
- Enhancements to the docs
- Fixed regression in fedmsg-irc

* Thu Sep 27 2012 Ralph Bean <rbean@redhat.com> - 0.5.1-1
- Fixed links in meetbot reprs
- fedmsg.text entries for pkgdb2branch and releng
- unicode bugfix for fedmsg-tail --terse
- Fix bug alongside python-moksha-hub-1.0.3-1
- New defaults fedora-infrastructure endpoints
- Improved docs
- Links to real diffs for mediawiki messages
- Specifiable and longer default tcp timeout for fedmsg-irc
- Improved config parsing for fedmsg-irc
- Bugfix to git-hook; ignore pushed tags instead of crashing
- Allow inner context to be destroyed and recreated inside a thread

* Thu Sep 27 2012 Ralph Bean <rbean@redhat.com> - 0.5.0-2
- Require python-pygments.

* Wed Sep 19 2012 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Depend on new Moksha
- Massive docs improvement.
- Minor API simplification.
- Suppress some annoying warnings from fedmsg-tail.

* Fri Aug 31 2012 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Bugfix to fedmsg.encoding.

* Fri Aug 31 2012 Ralph Bean <rbean@redhat.com> - 0.3.9-1
- Bugfix to fedmsg-gateway.
- to_json utility for sqlalchemy.
- More convenient default config for end users.

* Thu Aug 23 2012 Ralph Bean <rbean@redhat.com> - 0.3.8-1
- fedmsg-gateway command, new!
- Improved thread cleanup with weakref.
- --terse option for fedmsg-tail
- Meetbot text processing support.
- Update to consumer API.. systematized enablement.

* Fri Aug 17 2012 Ralph Bean <rbean@redhat.com> - 0.3.6-1
- Expanded reprs.  Support for fedoratagger-0.2.2-1 messages.
- Unicode bugfix.

* Tue Aug 14 2012 Ralph Bean <rbean@redhat.com> - 0.3.5-1
- IRC colors
- fedmsg2repr updates (Luke Macken)
- Removed fedmsg-status and the heartbeat producer

* Mon Aug 13 2012 Ralph Bean <rbean@redhat.com> - 0.3.4-1
- Threadsafety bugfixes to fedmsg-tail
- New fedmsg.text items from Luke Macken.

* Sun Aug 12 2012 Ralph Bean <rbean@redhat.com> - 0.3.3-1
- thread safety (for bodhi masher)

* Wed Aug 08 2012 Ralph Bean <rbean@redhat.com> - 0.3.2-1
- msg2repr updates for scm.

* Wed Aug 08 2012 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- msg2repr updates
- fedmsg-logger grepping.

* Tue Aug 07 2012 Ralph Bean <rbean@redhat.com> - 0.3.0-1
- Bugfix to fedmsg.text.

* Tue Aug 07 2012 Ralph Bean <rbean@redhat.com> - 0.2.9-1
- Upstream update including nicer message for fedmsg-irc.
- fedmsg.text.msg2repr

* Mon Aug 06 2012 Ralph Bean <rbean@redhat.com> - 0.2.7-4
- Remove unnecessary %%ghost on /var/run/fedmsg.

* Mon Aug 06 2012 Ralph Bean <rbean@redhat.com> - 0.2.7-3
- Hopefully fix to creation of /var/run/fedmsg.

* Mon Aug 06 2012 Ralph Bean <rbean@redhat.com> - 0.2.7-2
- Added a forgotten new requirement on python-requests.

* Sun Aug 05 2012 Ralph Bean <rbean@redhat.com> - 0.2.7-1
- Upstream bugfix to -logger and enhancement to -irc.

* Mon Jul 30 2012 Ralph Bean <rbean@redhat.com> - 0.2.6-2
- Require moksha >= 0.8.8

* Mon Jul 30 2012 Ralph Bean <rbean@redhat.com> - 0.2.6-1
- Upstream bugfixes and API enhancements.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Ralph Bean <rbean@redhat.com> - 0.2.5-1
- Upstream crypto updates in preparation for a more realistic X509 setup.

* Fri Jul 13 2012 Ralph Bean <rbean@redhat.com> - 0.2.4-1
- Upstream bugfix for when ssl is disabled.

* Wed Jul 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.3-1
- Upstream bump that fixes some typos.

* Tue Jul 10 2012 Ralph Bean <rbean@redhat.com> - 0.2.2-3
- Added deps on python-argparse for py < 2.7 (rhel6)

* Sat Jul 07 2012 Ralph Bean <rbean@redhat.com> - 0.2.2-2
- Added deps on m2crypto and python-m2ext

* Sat Jul 07 2012 Ralph Bean <rbean@redhat.com> - 0.2.2-1
- Update to fedmsg-irc to fix lineRate issues
- fedmsg.crypto module - sign and validate messages

* Mon Jun 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.1-2
- Require moksha >= 0.8.3

* Mon Jun 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.1-1
- Override producers and consumers entry-points in the hub.  Should fix a
  collision that fedmsg-irc is having with fedoracommunity.

* Mon Jun 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-4
- Introduce temporary hard dep on orbited.

* Mon Jun 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-3
- /var/log/fedmsg wasn't being created correctly.

* Sat Jun 09 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Split package into different daemonizable components.

* Thu Jun 07 2012 Ralph Bean <rbean@redhat.com> - 0.1.8-1
- Split config up into /etc/fedmsg.d/
- Removed tests.

* Wed Jun 06 2012 Ralph Bean <rbean@redhat.com> - 0.1.7-1
- Bugfix and tests.
- Added %%check section.

* Mon Jun 04 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-1
- Support multiple endpoints per node-service.

* Tue May 29 2012 Ralph Bean <rbean@redhat.com> - 0.1.5-1
- Support multiple nodes-per-service.

* Fri May 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.4-1
- Fresh version with removed shebang for packaging.
- %%define -> %%global
- Fixed end-of-line encodings in doc/conf.py

* Fri May 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.3-2
- Renamed to just 'fedmsg' from python-fedmsg.

* Fri May 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.3-1
- Integrating various pieces.  IRC bot fixes.
- Fixed a few specfile typos.

* Fri May 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.2-1
- Version bump.

* Wed May 02 2012 Ralph Bean <rbean@redhat.com> - 0.1.1-2
- Removed clean section
- Removed defattr in files section
- Removed unnecessary references to buildroot

* Thu Apr 26 2012 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- Support for busmon websocket options.

* Sat Apr 14 2012 Ralph Bean <rbean@redhat.com> - 0.1.0-1
- Initial packaging.
