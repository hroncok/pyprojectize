%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} >= 8 )
# Not all python modules are built with Python3 in EPEL
%global with_python3 1
%endif

Name:           module-build-service
Version:        3.9.2
Release:        10%{?dist}
Summary:        The Module Build Service for Modularity

License:        MIT
URL:            https://pagure.io/fm-orchestrator
Source0:        https://files.pythonhosted.org/packages/source/m/%{name}/%{name}-%{version}.tar.gz
Patch:          module-build-service-3.9.2-py312.patch

BuildArch:      noarch

%if 0%{?rhel}
ExclusiveArch:  %{ix86} x86_64 noarch
%endif

%if 0%{?with_python3}

BuildRequires:  python3-devel
BuildRequires:  python3-m2crypto
BuildRequires:  python3-munch
BuildRequires:  python3-solv
BuildRequires:  python3-libmodulemd
BuildRequires:  python3-openidc-client
BuildRequires:  python3-ldap3
BuildRequires:  python3-koji
BuildRequires:  python3-click
BuildRequires:  python3-flask-sqlalchemy
BuildRequires:  python3-flask-migrate
BuildRequires:  python3-six
BuildRequires:  python3-flask
BuildRequires:  python3-dogpile-cache
BuildRequires:  python3-requests
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-moksha-hub
BuildRequires:  python3-kobo
BuildRequires:  python3-kobo-rpmlib
BuildRequires:  python3-fedmsg
BuildRequires:  python3-pungi
BuildRequires:  python3-prometheus_client
BuildRequires:  python3-dnf
BuildRequires:  python3-celery

%else

BuildRequires:  python2-devel

BuildRequires:  m2crypto
BuildRequires:  python-flask-script
BuildRequires:  python-m2ext
BuildRequires:  python-munch
BuildRequires:  python2-funcsigs
BuildRequires:  python2-solv
BuildRequires:  python2-libmodulemd
BuildRequires:  python-openidc-client
BuildRequires:  python-ldap3
BuildRequires:  python-enum34
BuildRequires:  python2-koji
BuildRequires:  python2-fedmsg
BuildRequires:  python2-prometheus_client
BuildRequires:  python2-dnf
BuildRequires:  python2-celery

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
BuildRequires:  python-flask-sqlalchemy
BuildRequires:  python-flask-migrate
BuildRequires:  python-six
BuildRequires:  pyOpenSSL
BuildRequires:  python-sqlalchemy
BuildRequires:  python-moksha-hub
BuildRequires:  python-futures
BuildRequires:  python-flask
BuildRequires:  python-dogpile-cache
BuildRequires:  python-backports-ssl_match_hostname
BuildRequires:  python-requests
%else
BuildRequires:  python2-setuptools
BuildRequires:  python2-flask-sqlalchemy
BuildRequires:  python2-flask-migrate
BuildRequires:  python2-six
BuildRequires:  python2-futures
BuildRequires:  python2-flask
BuildRequires:  python2-dogpile-cache
BuildRequires:  python2-requests
BuildRequires:  python2-pyOpenSSL
BuildRequires:  python2-sqlalchemy
BuildRequires:  python2-moksha-hub
BuildRequires:  python2-m2crypto
BuildRequires:  python2-kobo
BuildRequires:  python2-kobo-rpmlib
# python2-pungi is not available in EPEL and can't be a BuildRequire for RHEL
BuildRequires:  python2-pungi
%endif

%endif

BuildRequires:  git-core
BuildRequires:  help2man
BuildRequires:  mock
BuildRequires:  rpm-build

%if 0%{?with_python3}
Requires:       python3-click
Requires:       python3-munch
Requires:       python3-openidc-client
Requires:       python3-ldap3
Requires:       python3-libmodulemd
Requires:       python3-solv
Requires:       python3-koji
Requires:       python3-flask-sqlalchemy
Requires:       python3-flask-migrate
Requires:       python3-six
Requires:       python3-pungi
Requires:       python3-sqlalchemy
Requires:       python3-moksha-hub
Requires:       python3-m2crypto
Requires:       python3-kobo
Requires:       python3-kobo-rpmlib
Requires:       python3-flask
Requires:       python3-dogpile-cache
Requires:       python3-requests
Requires:       python3-pyOpenSSL
Requires:       python3-fedmsg
Requires:       python3-prometheus_client
Requires:       python3-dnf
Requires:       python3-celery
%else
Requires:       python-flask-script
Requires:       python-munch
Requires:       python2-funcsigs
Requires:       python-enum34
Requires:       python-openidc-client
Requires:       python-ldap3
Requires:       python2-libmodulemd
Requires:       python2-solv
Requires:       python2-koji
Requires:       python2-fedmsg
Requires:       python2-pungi
Requires:       python2-prometheus_client
Requires:       python2-dnf
Requires:       python2-celery

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       python-flask-sqlalchemy
Requires:       python-flask-migrate
Requires:       python-six
Requires:       python-sqlalchemy
Requires:       python-moksha-hub
Requires:       python-futures
Requires:       python-flask
Requires:       python-dogpile-cache
Requires:       python-backports-ssl_match_hostname
Requires:       python-requests
%else
Requires:       python2-flask-sqlalchemy
Requires:       python2-flask-migrate
Requires:       python2-six
Requires:       python2-futures
Requires:       python2-flask
Requires:       python2-dogpile-cache
Requires:       python2-requests
Requires:       python2-pyOpenSSL
Requires:       python2-sqlalchemy
Requires:       python2-moksha-hub
Requires:       python2-m2crypto
Requires:       python2-kobo
Requires:       python2-kobo-rpmlib
%endif

%endif

Requires:       fedpkg
Requires:       git-core
Requires:       mock
Requires:       rpm-build
# https://bugzilla.redhat.com/show_bug.cgi?id=1466792
Requires:       mock-scm


%description
The Module Build Service (MBS) coordinates module builds and is responsible
for a number of tasks:

- Providing an interface for module client-side tooling via which module build
  submission and build state queries are possible.
- Verifying the input data (modulemd, RPM SPEC files and others) is available
  and correct.
- Preparing the build environment in the supported build systems, such as koji.
- Scheduling and building of the module components and tracking the build
  state.
- Emitting bus messages about all state changes so that other infrastructure
  services can pick up the work.


%prep
%autosetup -p1


# Workaround because python2-koji has no egg-info file at the momement
sed -i '/koji/d' requirements.txt

# Remove Python 2 only dependencies
sed -i '/futures/d' requirements.txt
sed -i '/enum34/d' requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?with_python3}
%pyproject_wheel
%else
%py2_build
%endif


%install
%if 0%{?with_python3}
%pyproject_install
%else
%py2_install
%endif

%if 0%{?with_python3}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%else
export PYTHONPATH=%{buildroot}%{python2_sitelib}
%endif

# The version of kobo required is not in RHEL/EPEL, so these commands will fail
%if 0%{?fedora}
mkdir -p %{buildroot}/%{_mandir}/man1
for command in mbs-manager mbs-frontend mbs-upgradedb ; do
    %{buildroot}/%{_bindir}/$command --help
    help2man -N --version-string=%{version} \
    %{buildroot}/%{_bindir}/$command > \
    %{buildroot}/%{_mandir}/man1/$command.1
done
%endif

%files
%doc README.rst
%license LICENSE

%if 0%{?with_python3}
%{python3_sitelib}/module_build_service*
%else
%{python2_sitelib}/module_build_service*
%endif

%{_bindir}/mbs-*
%dir %{_sysconfdir}/module-build-service
%config(noreplace) %{_sysconfdir}/module-build-service/koji.conf
%config(noreplace) %{_sysconfdir}/module-build-service/mock.cfg
%config(noreplace) %{_sysconfdir}/module-build-service/yum.conf
%config(noreplace) %{_sysconfdir}/fedmsg.d/mbs-scheduler.py
%config(noreplace) %{_sysconfdir}/fedmsg.d/mbs-logging.py
%config(noreplace) %{_sysconfdir}/fedmsg.d/module_build_service.py

%if 0%{?with_python3}
%exclude %{python3_sitelib}/conf/
%exclude %{python3_sitelib}/tests/
%else
%exclude %{python2_sitelib}/conf/
%exclude %{python2_sitelib}/tests/
%endif

%if 0%{?fedora}
%{_mandir}/man1/mbs-*.1*
%endif

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Nils Philippsen <nils@tiptoe.de> - 3.9.2-9
- Revert constraining SQLAlchemy version

* Thu Mar 21 2024 Nils Philippsen <nils@tiptoe.de> - 3.9.2-8
- Require SQLAlchemy < 2
- Adapt for Python 3.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Python Maint <python-maint@redhat.com> - 3.9.2-4
- Rebuilt for Python 3.12

* Tue May 30 2023 Diego Herrera <dherrera@redhat.com> - 3.9.2-3
- Remove the python3-funcsigs runtime requirement

* Mon Apr 24 2023 Diego Herrera <dherrera@redhat.com> - 3.9.2-2
- Remove the python3-funcsigs requirement
- EL8+ uses python3

* Tue Apr 18 2023 Brendan Reilly <breilly@redhat.com> - 3.9.2-1
- new version

* Tue Apr 18 2023 Brendan Reilly <breilly@redhat.com> - 3.9.0-1
- new version

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Tomas Hrcka <thrcka@redhat.com> - 3.8.0-2
- rebuilt

* Wed Dec 07 2022 Brendan Reilly <breilly@redhat.com> - 3.8.0-1
- new version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 30 2021 Brendan Reilly - 3.6.1-6
- Replaced python3-flask-script with python3-click in Requires

* Thu Sep 30 2021 Brendan Reilly - 3.6.1-5
- Added patch to remove flask-script in favor of click (BZ1968843)

* Thu Aug 12 2021 Brendan Reilly - 3.6.1-4
- Added patch to remove dbapi error handler (BZ1968843)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.6.1-2
- Rebuilt for Python 3.10

* Thu Apr 22 2021 Mike McLean <mikem@redhat.com> - 3.6.1-1
- new version

* Tue Jan 26 2021 Brendan Reilly <breilly@redhat.com> - 3.4.1-1
- new version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.32.0-2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Mike McLean <mikem@redhat.com> - 2.32.0-1
- new version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Mike McLean <mikem@redhat.com> - 2.31.0-1
- new version

* Mon Nov 25 2019 Mike McLean <mikem@redhat.com> - 2.30.4-1
- new version

* Mon Nov 11 2019 mprahl <mprahl@redhat.com> - 2.30.3-1
- new version

* Fri Nov 08 2019 mprahl <mprahl@redhat.com> - 2.30.2-1
- new version

* Wed Nov 06 2019 mprahl <mprahl@redhat.com> - 2.30.1-1
- new version

* Tue Nov 05 2019 mprahl <mprahl@redhat.com> - 2.30.0-1
- new version

* Thu Oct 03 2019 Mike McLean <mikem@redhat.com> - 2.29.1-1
- Fix a fork in the database migration scripts

* Thu Oct 03 2019 Mike McLean <mikem@redhat.com> - 2.29.0-1
- Add buildonly support
- Make the DNF minrate setting configurable when loading repos
- Load the DNF repos in parallel to improve speed
- Record the build_context without base modules
- Convert arch to Koji's canon arch for default modules
- Initial KojiResolver code
- Disable handling collisions on local builds due to RHBZ#1693683

* Thu Sep 19 2019 mprahl <mprahl@redhat.com> - 2.28.2-1
- new version

* Tue Sep 17 2019 mprahl <mprahl@redhat.com> - 2.28.0-1
- new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.26.0-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Jan Kaluza <jkaluza@redhat.com> - 2.26.0-1
- new version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 mprahl <mprahl@redhat.com> - 2.25.0-2
- Fix the specfile change log

* Wed Jul 17 2019 mprahl <mprahl@redhat.com> - 2.25.0-1
- new version

* Fri Jul 12 2019 Owen Taylor <otaylor@redhat.com> - 2.24.0-2
- Require python{2,3}-libmodulemd, needed for correct operation
  of the libmodulemd python bindings.

* Tue Jul 02 2019 Valerij Maljulin <vmaljuli@redhat.com> - 2.24.0-1
- new version

* Thu Jun 20 2019 mprahl <mprahl@redhat.com> - 2.23.0-1
- new version

* Tue Jun 18 2019 Valerij Maljulin <vmaljuli@redhat.com> - 2.22.0-1
- new version

* Fri May 10 2019 mprahl <mprahl@redhat.com> - 2.20.0-1
- new version

* Tue Apr 16 2019 mprahl <mprahl@redhat.com> - 2.19.1-1
- new version

* Thu Apr 04 2019 mprahl <mprahl@redhat.com> - 2.19.0-1
- new version

* Wed Mar 20 2019 mprahl <mprahl@redhat.com> - 2.18.1-1
- new version

* Thu Feb 14 2019 mprahl <mprahl@redhat.com> - 2.14.0-2
- Add python-prometheus_client as a dependency

* Thu Feb 14 2019 mprahl <mprahl@redhat.com> - 2.14.0-1
- new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 mprahl <mprahl@redhat.com> - 2.13.1-1
- new version

* Thu Jan 17 2019 mprahl <mprahl@redhat.com> - 2.12.2-1
- new version

* Wed Jan 16 2019 mprahl <mprahl@redhat.com> - 2.12.1-1
- new version

* Mon Jan 14 2019 mprahl <mprahl@redhat.com> - 2.12.0-1
- new version

* Wed Jan 09 2019 mprahl <mprahl@redhat.com> - 2.11.1-2
- Add python-pungi as a dependency for Fedora builds
- Remove pdc-client as a dependency

* Wed Dec 19 2018 mprahl <mprahl@redhat.com> - 2.11.1-1
- new version

* Tue Dec 18 2018 mprahl <mprahl@redhat.com> - 2.11.0-1
- new version

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 2.9.1-2
- Drop ambiguous Python 2 dependencies (kobo, m2crypto, pyOpenSSL)

* Fri Dec 07 2018 mprahl <mprahl@redhat.com> - 2.9.1-1
- new version

* Mon Nov 19 2018 mprahl <mprahl@redhat.com> - 2.8.1-2
- Don't assume the context is set on base modules in the 526fb7d445f7_module_buildrequires migration

* Mon Nov 19 2018 mprahl <mprahl@redhat.com> - 2.8.1-1
- new version

* Fri Oct 12 2018 Matt Prahl <mprahl@redhat.com> - 2.7.0-1
- new version

* Mon Sep 10 2018 Ralph Bean <rbean@redhat.com> - 2.6.0-2
- Apply https://pagure.io/fm-orchestrator/pull-request/1013.patch

* Fri Sep 07 2018 Ralph Bean <rbean@redhat.com> - 2.6.0-1
- new version

* Tue Aug 14 2018 Ralph Bean <rbean@redhat.com> - 2.5.0-1
- new version

* Tue Aug 07 2018 mprahl <mprahl@redhat.com> - 2.4.2-1
- new version

* Tue Aug 07 2018 mprahl <mprahl@redhat.com> - 2.4.1-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 mprahl <mprahl@redhat.com> - 2.4.0-2
- Remove copr.conf from the expected files

* Wed Jul 11 2018 mprahl <mprahl@redhat.com> - 2.4.0-1
- new version

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.7

* Wed Jun 27 2018 Ralph Bean <rbean@redhat.com> - 2.3.2-1
- new version

* Wed Jun 27 2018 Ralph Bean <rbean@redhat.com> - 2.3.1-1
- new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 mprahl <mprahl@redhat.com> - 2.3.0-1
- new version

* Fri Jun 01 2018 mprahl <mprahl@redhat.com> - 2.2.4-1
- new version

* Thu May 31 2018 mprahl <mprahl@redhat.com> - 2.2.3-1
- new version

* Wed May 30 2018 mprahl <mprahl@redhat.com> - 2.2.2-1
- new version

* Tue May 29 2018 mprahl <mprahl@redhat.com> - 2.2.1-1
- new version

* Thu May 10 2018 mprahl <mprahl@redhat.com> - 2.2.0-1
- new version

* Tue May 08 2018 Merlin Mathesius <mmathesi@redhat.com> - 2.1.1-2
- Correct fedmsg deps.

* Tue May 08 2018 Ralph Bean <rbean@redhat.com> - 2.1.1-1
- new version

* Tue May 08 2018 Ralph Bean <rbean@redhat.com> - 2.1.0-3
- Add missing deps and scrub unneeded py3 egg requirements.

* Tue May 08 2018 Ralph Bean <rbean@redhat.com> - 2.1.0-2
- Try to fix 'm2ext' and moksha.hub dep issues.
  https://pagure.io/fm-orchestrator/issue/931

* Fri May 04 2018 mprahl <mprahl@redhat.com> - 2.1.0-1
- new version

* Fri Apr 20 2018 Jan Kaluza <jkaluza@redhat.com> - 2.0.2-5
- Allow block the packages in a module build before they are built as
  part of a module

* Tue Apr 17 2018 Jan Kaluza <jkaluza@redhat.com> - 2.0.2-4
- use python3 by default

* Thu Apr 05 2018 Jan Kaluza <jkaluza@redhat.com> - 2.0.2-3
- fix wrong component reuse caused by missing change for buildrequires.

* Thu Apr 05 2018 Jan Kaluza <jkaluza@redhat.com> - 2.0.2-2
- fix issue with expanded requires section in case empty list is used as input.

* Thu Apr 05 2018 mprahl <mprahl@redhat.com> - 2.0.2-1
- New version
- Clean up dependencies

* Thu Apr 05 2018 mprahl <mprahl@redhat.com> - 2.0.1-1
- new version

* Thu Apr 05 2018 Jan Kaluza <jkaluza@redhat.com> - 2.0.0-1
- new version

* Wed Feb 07 2018 mprahl <mprahl@redhat.com> - 1.7.0-1
- new version

* Thu Jan 25 2018 mprahl <mprahl@redhat.com> - 1.6.3-2
- Update the required version of modulemd

* Tue Jan 23 2018 mprahl <mprahl@redhat.com> - 1.6.3-1
- new version

* Mon Jan 22 2018 mprahl <mprahl@redhat.com> - 1.6.2-1
- new version

* Mon Jan 22 2018 mprahl <mprahl@redhat.com> - 1.6.1-1
- new version

* Mon Jan 22 2018 mprahl <mprahl@redhat.com> - 1.6.0-1
- new version

* Tue Nov 28 2017 mprahl <mprahl@redhat.com> - 1.5.2-1
- new version

* Mon Nov 27 2017 mprahl <mprahl@redhat.com> - 1.5.1-1
- new version

* Fri Nov 17 2017 mprahl <mprahl@redhat.com> - 1.5.0-1
- new version

* Tue Nov 14 2017 mprahl <mprahl@redhat.com> - 1.4.7-1
- new version

* Tue Nov 14 2017 mprahl <mprahl@redhat.com> - 1.4.6-1
- new version

* Tue Nov 07 2017 mprahl <mprahl@redhat.com> - 1.4.5-2
- Support building without EPEL

* Mon Nov 06 2017 mprahl <mprahl@redhat.com> - 1.4.5-1
- new version

* Mon Nov 06 2017 mprahl <mprahl@redhat.com> - 1.4.4-1
- new version

* Thu Nov 2 2017 Matt Prahl <mprahl@redhat.com> - 1.4.3.1
- New version

* Thu Nov 2 2017 Matt Prahl <mprahl@redhat.com> - 1.4.2.1
- New version

* Thu Nov 2 2017 Matt Prahl <mprahl@redhat.com> - 1.4.1.1
- New version

* Thu Nov 2 2017 Matt Prahl <mprahl@redhat.com> - 1.4.0-2
- Remove the caching patch that was merged upstream
- Add a patch that fixes a typo in error messages

* Wed Nov 1 2017 Matt Prahl <mprahl@redhat.com> - 1.4.0-1
- New version

* Wed Oct 11 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.31-3
- Fix wrong attr for untagged builds.

* Wed Oct 11 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.31-2
- Fix bad performance while getting data from PDC for modules with many deps.

* Mon Oct 2 2017 Matt Prahl <mprahl@redhat.com> - 1.3.31-1
- New version

* Thu Sep 21 2017 Ralph Bean <rbean@redhat.com> - 1.3.30-2
- Re-enable ldap3 requirement now that it is available in epel7.
- Add new requirement on python-requests-kerberos.

* Thu Sep 21 2017 Ralph Bean <rbean@redhat.com> - 1.3.30-1
- new version

* Mon Sep 18 2017 Ralph Bean <rbean@redhat.com> - 1.3.29-1
- new version

* Fri Sep 15 2017 Ralph Bean <rbean@redhat.com> - 1.3.28-1
- new version

* Tue Sep 12 2017 Ralph Bean <rbean@redhat.com> - 1.3.27-3
- Remove the nobuild patch for EL7.

* Tue Sep 12 2017 Ralph Bean <rbean@redhat.com> - 1.3.27-2
- Merge epel7 spec branch into rawhide to consolidate streams.

* Tue Sep 12 2017 Ralph Bean <rbean@redhat.com> - 1.3.27-1
- new version

* Tue Sep 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.26-5
- Really apply patches

* Sun Sep 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.26-4
- Backport patches to fix skiptests behavior
- Cleanups / Fixes in spec

* Fri Aug 18 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.26-3
- add missing dependency on python2-dogpile-cache

* Thu Aug 17 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.26-2
- fix mbs-build issue with trailing slash in REST API url

* Thu Aug 17 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.26-1
- new version

* Mon Aug 07 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.25-8
- do not wait for kojira when generating module-build-macros repository

* Mon Aug 07 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.25-7
- upload modulemd.yaml to Koji as modulemd.txt

* Fri Aug 04 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.25-6
- fix tagging components when all of them are reused

* Fri Aug 04 2017 Ralph Bean <rbean@redhat.com> - 1.3.25-5
- upload content generator logs to Koji
- Require mock-scm for local builds.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.25-4
- fix bug during build caused by not set SERVER_NAME in configuration file
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.25-3
- fix typo in spec file

* Mon Jul 17 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.25-2
- fix dependency on koji

* Mon Jul 17 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.25-1
- new version

* Tue Jul 11 2017 Ralph Bean <rbean@redhat.com> - 1.3.24-3
- Fix the runtime dep for pdc-client.

* Tue Jun 27 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.24-2
- Fix the pdc-client dependency

* Tue Jun 27 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.24-1
- new version

* Mon Jun 05 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.23-5
- Fix the components reuse if database returns them in different order

* Mon Jun 05 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.23-4
- Tag the untagged artifacts when returning their build_id

* Mon Jun 05 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.23-3
- correct the patch from previous commit

* Mon Jun 05 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.23-2
- fix bug when untagged builds couldn't be find in Koji

* Wed May 31 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.23-1
- new version

* Thu May 25 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.22-3
- Use the same spec file for both epel7 and fedora

* Tue May 16 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.22-2
- fix reusing all components

* Fri May 12 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.22-1
- new version

* Fri Apr 07 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.20-1
- new version

* Fri Apr 07 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.18-1
- new version

* Thu Apr 06 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.17-1
- new version

* Sat Mar 25 2017 Petr Šabata <contyk@redhat.com> - 1.3.16-2
- Adding a missing runtime dependency, fedpkg

* Thu Mar 23 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.16-1
- new version

* Thu Mar 23 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.15-1
- new version

* Wed Mar 22 2017 Ralph Bean <rbean@redhat.com> - 1.3.14-1
- new version

* Wed Mar 22 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.13-1
- 1.3.13

* Wed Mar 22 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.12-1
- 1.3.12

* Fri Mar 17 2017 Jan Kaluza <jkaluza@redhat.com> - 1.3.11-1
- 1.3.11 bump

* Fri Mar 17 2017 Petr Šabata <contyk@redhat.com> - 1.3.10-1
- 1.3.10 bump

* Thu Mar 16 2017 Ralph Bean <rbean@redhat.com> - 1.3.9-1
- new version

* Wed Mar 15 2017 Ralph Bean <rbean@redhat.com> - 1.3.8-1
- new version

* Tue Mar 14 2017 Ralph Bean <rbean@redhat.com> - 1.3.6-1
- new version

* Tue Mar 14 2017 Ralph Bean <rbean@redhat.com> - 1.3.5-1
- new version

* Mon Mar 13 2017 Ralph Bean <rbean@redhat.com> - 1.3.4-1
- new version

* Fri Mar 03 2017 Ralph Bean <rbean@redhat.com> - 1.3.3-1
- new version

* Fri Mar 03 2017 Petr Šabata <contyk@redhat.com> - 1.3.2-3
- MBS requires modulemd-1.1.0+ to work properly

* Thu Mar 02 2017 Ralph Bean <rbean@redhat.com> - 1.3.2-2
- Conditionalize arch for epel7 building.

* Thu Mar 02 2017 Ralph Bean <rbean@redhat.com> - 1.3.2-1
- new version

* Tue Feb 28 2017 Ralph Bean <rbean@redhat.com> - 1.3.1-2
- Disable the test suite in koji for now.

* Tue Feb 28 2017 Ralph Bean <rbean@redhat.com> - 1.3.1-1
- new version

* Wed Feb 15 2017 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  1 2017 Filip Valder <fvalder@redhat.com> - 1.1.1-2
- New revision (deps & cleanups)

* Tue Jan 31 2017 Ralph Bean <rbean@redhat.com> - 1.1.1-1
- new version

* Tue Jan 24 2017 Ralph Bean <rbean@redhat.com> - 1.1.0-3
- Include fedmsg.d/mbs-scheduler.py by default.

* Wed Jan 18 2017 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Dep fixes (for EPEL7).

* Tue Jan 17 2017 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- new version

* Wed Jan 11 2017 Ralph Bean <rbean@redhat.com> - 1.0.2-4
- Conditionalize some deps for EPEL7.

* Wed Jan 11 2017 Ralph Bean <rbean@redhat.com> - 1.0.2-3
- Sync spec file from upstream git.

* Thu Dec 15 2016 Matt Prahl <mprahl@redhat.com> - 1.0.2-2
- Replace systemd unit with fedmsg-hub
- Remove an old .pyc file that got included by accident.

* Wed Dec 14 2016 Ralph Bean <rbean@redhat.com> - 1.0.2-1
- Enable test suite in the check section.
- Add systemd scriptlets, per review feedback.

* Mon Dec 12 2016 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- Cleanup in preparation for package review.

* Tue Dec 6 2016 Matt Prahl <mprahl@redhat.com> - 1.0.0-2
- Adds systemd unit.

* Fri Nov 25 2016 Filip Valder <fvalder@redhat.com> - 1.0.0-1
- Let's get this party started.
