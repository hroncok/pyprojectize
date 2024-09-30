%if ( 0%{?fedora} && 0%{?fedora} >= 31 ) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
%global with_python3 1
%else
%global with_python2 1
%endif

%global modname moksha.hub

Name:           python-moksha-hub
Version:        1.5.17
Release:        26%{?dist}
Summary:        Hub components for Moksha

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.io/project/moksha.hub
Source0:        https://pypi.io/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz
# https://github.com/mokshaproject/moksha/pull/76
Patch0:         0002-decode-topics.patch

BuildArch:      noarch

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
BuildRequires:  python2-mock

BuildRequires:  python2-six

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-moksha-common
BuildRequires:  python-txzmq
BuildRequires:  python-txws
BuildRequires:  python-daemon
BuildRequires:  python-twisted-core
BuildRequires:  python-stomper
%else
BuildRequires:  python2-moksha-common
BuildRequires:  python2-txzmq
BuildRequires:  python2-txws
BuildRequires:  python2-daemon
BuildRequires:  python2-twisted
BuildRequires:  python2-stomper
BuildRequires:  python2-pyasn1
BuildRequires:  python2-service-identity
%endif
%endif

%if 0%{?with_python2}
%if 0%{?fedora}
BuildRequires:  python2-websocket-client
%endif
%endif

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-mock

BuildRequires:  python3-moksha-common >= 1.0.6
BuildRequires:  python3-twisted
BuildRequires:  python3-txzmq
BuildRequires:  python3-txws
BuildRequires:  python3-six
BuildRequires:  python3-stomper
BuildRequires:  python3-pyasn1
BuildRequires:  python3-service-identity
BuildRequires:  python3-daemon

BuildRequires:  python3-websocket-client
%endif

# When installed, these enable new plugins for the moksha.hub
#BuildRequires:  python2-qpid
#Requires:       python2-qpid

# Its a whole different package now.

%global _description\
Hub components for Moksha.\


%description %_description

%if 0%{?with_python2}
%package -n python2-moksha-hub
Summary: %summary

Requires:       python2-six

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       python-moksha-common
Requires:       python-txzmq
Requires:       python-txws
Requires:       python-daemon
Requires:       python-twisted-core
Requires:       python-stomper
%else
Requires:       python2-moksha-common
Requires:       python2-txzmq
Requires:       python2-txws
Requires:       python2-daemon
Requires:       python2-twisted
Requires:       python2-stomper
Requires:       python2-pyasn1
Recommends:     python2-service-identity
%endif

Conflicts:      moksha < 1.0.0
Conflicts:      python3-moksha-hub < 1.5.17-4

%description -n python2-moksha-hub %_description
%endif

%if 0%{?with_python3}
%package -n python3-moksha-hub
Summary:        Hub components for Moksha

Requires:       python3-moksha-common >= 1.0.6
Requires:       python3-twisted
Requires:       python3-stomper
Requires:       python3-pyasn1
Requires:       python3-txzmq
Requires:       python3-txws
Requires:       python3-daemon
Requires:       python3-six

Recommends:     python3-service-identity

Conflicts:      python2-moksha-hub < 1.5.17-4

%description -n python3-moksha-hub
Hub components for Moksha.
%endif


%prep
%setup -q -n %{modname}-%{version}
%patch 0 -p1

# Removed twisted from the list of deps in setup.py.
%{__sed} -i 's/"Twisted",//' setup.py

# *Experimental* support for python-zmq-13.0.0 in rawhide.
%{__sed} -i 's/pyzmq<=2.2.0.1/pyzmq/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%pyproject_wheel
%endif


%install
%if 0%{?with_python2}
%py2_install
mv %{buildroot}%{_bindir}/moksha-hub %{buildroot}%{_bindir}/moksha-hub-%{python2_version}
ln -s ./moksha-hub-%{python2_version} %{buildroot}%{_bindir}/moksha-hub-2
%endif

%if 0%{?with_python3}
%pyproject_install
%pyproject_save_files -l moksha
ln -s ./moksha-hub %{buildroot}%{_bindir}/moksha-hub-3
ln -s ./moksha-hub %{buildroot}%{_bindir}/moksha-hub-%{python3_version}
%endif

%check
%if 0%{?rhel}
# Test suite requires a more modern Twisted than is in el6, so don't run it for
# now.

# Furthermore, the test suite requires python-websocket-client, which is in a
# rhel7-optional and isn't showing up in the fedoraproject koji buildroot.
# https://bugzilla.redhat.com/show_bug.cgi?id=1185049

%else
%if 0%{?with_python2}
%{__python2} setup.py test
%endif
%endif

%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%if 0%{?with_python2}
%files -n python2-moksha-hub
%doc README AUTHORS
%license COPYING
%{python2_sitelib}/moksha/hub/
%{python2_sitelib}/%{modname}-%{version}*
%{_bindir}/moksha-hub-2
%{_bindir}/moksha-hub-%{python2_version}
%endif

%if 0%{?with_python3}
%files -n python3-moksha-hub -f %{pyproject_files}
%doc README AUTHORS
%{_bindir}/moksha-hub
%{_bindir}/moksha-hub-3
%{_bindir}/moksha-hub-%{python3_version}
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.17-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.5.17-24
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 1.5.17-20
- Rebuilt for Python 3.12

* Fri Jun 30 2023 Michal Konecny <mkonecny@redhat.com> - 1.5.17-19
- Add patch for https://github.com/mokshaproject/moksha/pull/76

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.5.17-18
- Rebuilt for Python 3.12

* Tue Jan 24 2023 Diego Herrera <dherrera@redhat.com> - 1.5.17-17
- Fix python version filters for RHEL/EPEL

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.5.17-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.17-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.17-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.17-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.17-5
- Rebuilt for Python 3.8

* Mon Aug 05 2019 Lumír Balhar <lbalhar@redhat.com> - 1.5.17-4
- Move unversioned command to Python 3 subpackage and add proper conflicts

* Mon Aug 05 2019 Lumír Balhar <lbalhar@redhat.com> - 1.5.17-3
- Disable Python 2 subpackage in Fedora 31+
- Fixes: rhbz#1736510

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Ralph Bean <rbean@redhat.com> - 1.5.17-1
- new version

* Wed Feb 06 2019 Ralph Bean <rbean@redhat.com> - 1.5.16-1
- new version

* Wed Feb 06 2019 Ralph Bean <rbean@redhat.com> - 1.5.15-4
- Make service-identity a weak dependency.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Ralph Bean <rbean@redhat.com> - 1.5.15-2
- Remove patch for https://github.com/mokshaproject/moksha/pull/65
  which didn't prove helpful.

* Thu Jan 10 2019 Ralph Bean <rbean@redhat.com> - 1.5.15-1
- new version

* Mon Jan 07 2019 Ralph Bean <rbean@redhat.com> - 1.5.14-1
- new version

* Mon Sep 24 2018 Ralph Bean <rbean@redhat.com> - 1.5.13-2.0.1cb025525
- Apply experimental upstream patch for stomp heartbeat handling
  https://github.com/mokshaproject/moksha/pull/65

* Tue Aug 21 2018 Ralph Bean <rbean@redhat.com> - 1.5.13-1
- new version

* Tue Aug 07 2018 Ralph Bean <rbean@redhat.com> - 1.5.12-1
- new version

* Thu Aug 02 2018 Ralph Bean <rbean@redhat.com> - 1.5.11-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.10-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Ralph Bean <rbean@redhat.com> - 1.5.10-1
- new version

* Fri Jun 08 2018 Ralph Bean <rbean@redhat.com> - 1.5.9-1
- new version

* Thu Jun 07 2018 Ralph Bean <rbean@redhat.com> - 1.5.8-1
- new version

* Fri May 25 2018 Ralph Bean <rbean@redhat.com> - 1.5.7-1
- new version

* Mon Apr 30 2018 Ralph Bean <rbean@redhat.com> - 1.5.6-1
- new version

* Mon Mar 19 2018 Ralph Bean <rbean@redhat.com> - 1.5.5-2
- Conditionalize deps for epel7.

* Mon Mar 19 2018 Ralph Bean <rbean@redhat.com> - 1.5.5-1
- new version

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.4-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Ralph Bean <rbean@redhat.com> - 1.5.4-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.3-5
- Python 2 binary package renamed to python2-moksha-hub
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Mon Jul 31 2017 Lumír Balhar <lbalhar@redhat.com> - 1.5.3-4
- Python 3 subpackage enabled
- Specfile modernized and improved

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Ralph Bean <rbean@redhat.com> - 1.5.3-2
- Apply patch to increase logging when JSON is weird.

* Tue Jul 11 2017 Ralph Bean <rbean@redhat.com> - 1.5.3-1
- new version

* Mon Jun 26 2017 Ralph Bean <rbean@redhat.com> - 1.5.2-1
- new version

* Fri Jun 09 2017 Ralph Bean <rbean@redhat.com> - 1.5.1-1
- new version

* Fri Jun 09 2017 Ralph Bean <rbean@redhat.com> - 1.5.0-1
- new version

* Wed May 31 2017 Ralph Bean <rbean@redhat.com> - 1.4.9-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Ralph Bean <rbean@redhat.com> - 1.4.8-1
- new version

* Thu Oct 13 2016 Ralph Bean <rbean@redhat.com> - 1.4.7-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Ralph Bean <rbean@redhat.com> - 1.4.6-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Ralph Bean <rbean@redhat.com> - 1.4.5-1
- Latest upstream.  Fixes exception counting stats.

* Wed Oct 22 2014 Ralph Bean <rbean@redhat.com> - 1.4.4-1
- Latest upstream; removed our patches.
- Consumers can now handle a list of multiple topics again.

* Wed Oct 01 2014 Ralph Bean <rbean@redhat.com> - 1.4.3-2
- Patch to make polling producers advertise the last time they ran.

* Thu Sep 25 2014 Ralph Bean <rbean@redhat.com> - 1.4.3-1
- Latest upstream with stomp improvements.

* Mon Sep 15 2014 Ralph Bean <rbean@redhat.com> - 1.4.2-1
- Latest upstream with support for STOMP-1.1.

* Fri Aug 08 2014 Ralph Bean <rbean@redhat.com> - 1.4.1-1
- Configurable permissions on the monitoring socket.
- Suggest a threadpool size to twisted based on the number of consumers.

* Fri Jul 18 2014 Ralph Bean <rbean@redhat.com> - 1.4.0-1
- New API points: pre_consume and post_consume.

* Mon Jun 30 2014 Ralph Bean <rbean@redhat.com> - 1.3.4-1
- Improved exception handling in the consumer API.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Ralph Bean <rbean@redhat.com> - 1.3.3-1
- Added threading model to the polling producer API.

* Thu Apr 24 2014 Ralph Bean <rbean@redhat.com> - 1.3.2-1
- Bugfixes to the monitoring socket.

* Thu Apr 24 2014 Ralph Bean <rbean@redhat.com> - 1.3.1-2
- Add dep on python-six.

* Thu Apr 24 2014 Ralph Bean <rbean@redhat.com> - 1.3.1-1
- More stats written to the monitoring socket.

* Sun Apr 13 2014 Ralph Bean <rbean@redhat.com> - 1.3.0-1
- Introduce a new monitoring socket.
- Moksha consumers are now given their own thread and incoming queue.

* Tue Jan 14 2014 Ralph Bean <rbean@redhat.com> - 1.2.2-2
- Enable websocket portion of the test suite again.
- Remove hard dep on python-qpid.

* Fri Dec 13 2013 Ralph Bean <rbean@redhat.com> - 1.2.2-1
- Latest upstream fixing a memory leak in the websocket server.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Ralph Bean <rbean@redhat.com> - 1.2.1-1
- Latest upstream with a bugfix to consumer loading.

* Tue Mar 26 2013 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- Latest upstream.
- Removed websocket tests until this review is complete:
  https://bugzilla.redhat.com/show_bug.cgi?id=909644

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- Latest upstream with support for zmq_tcp_keepalive.

* Tue Dec 04 2012 Ralph Bean <rbean@redhat.com> - 1.0.9-1
- Latest upstream.
- Fixed check conditional for rhel6.

* Wed Oct 10 2012 Ralph Bean <rbean@redhat.com> - 1.0.7-1
- Various bugfixes.
- Support for zeromq3.
- Needs python-moksha-common-1.0.6 or later.

* Mon Oct 01 2012 Ralph Bean <rbean@redhat.com> - 1.0.4-1
- Allow moksha-hub to use a non-standard config (specified as an argument).
- Temporary bug fix in websocket server message distribution.

* Wed Sep 26 2012 Ralph Bean <rbean@redhat.com> - 1.0.3-1
- Fix to _initialized namespacing for consumers.
- More careful still when cleaning up consumers.

* Wed Sep 19 2012 Ralph Bean <rbean@redhat.com> - 1.0.2-1
- Miscellaneous bugfixes in consumer cleanup.
- Added conflicts tag against old moksha.

* Wed Sep 12 2012 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- Require latest python-moksha-common

* Sat Sep 08 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-5
- Disable test suite for el6.

* Sat Sep 08 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-4
- Remove "Twisted" from the list of deps in setup.py.

* Wed Sep 05 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-3
- Use optflags instead of RPM_OPT_FLAGS to be consistent.

* Wed Sep 05 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-2
- Added RPM_OPT_FLAGS to the build section.

* Tue Sep 04 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial package for Fedora and fork from moksha core.
