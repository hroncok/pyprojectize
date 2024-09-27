Name:       odcs
Version:    0.8.0
Release:    6%{?dist}
Summary:    The On Demand Compose Service


License:    MIT
URL:        https://pagure.io/odcs
Source0:    https://files.pythonhosted.org/packages/source/o/%{name}/%{name}-%{version}.tar.gz
Source1:    odcs-backend.service
# Fedora related configuration for ODCS.
Patch0:     odcs-fedora-conf.patch
Patch1:     https://pagure.io/odcs/pull-request/667.patch

BuildArch:    noarch

BuildRequires:    help2man
BuildRequires:    python3-libmodulemd
BuildRequires:    gobject-introspection
BuildRequires:    systemd
BuildRequires:    python3-devel
BuildRequires:    python3-requests-gssapi
BuildRequires:    python3-fedora
BuildRequires:    python3-productmd
BuildRequires:    python3-filelock
BuildRequires:    python3-funcsigs
BuildRequires:    python3-openidc-client
BuildRequires:    python3-flask-sqlalchemy
BuildRequires:    python3-flask-migrate
BuildRequires:    python3-jwt
BuildRequires:    python3-nose
BuildRequires:    python3-mock
BuildRequires:    python3-tabulate
BuildRequires:    python3-six
BuildRequires:    python3-flask
BuildRequires:    python3-systemd
BuildRequires:    python3-defusedxml
BuildRequires:    python3-koji
BuildRequires:    python3-httplib2
BuildRequires:    python3-pyOpenSSL
BuildRequires:    python3-sqlalchemy
BuildRequires:    python3-ldap
BuildRequires:    python3-gobject-base
BuildRequires:    python3-flask-login
BuildRequires:    python3-psutil
BuildRequires:    python3-flufl-lock
BuildRequires:    python3-celery
BuildRequires:    python3-kobo
BuildRequires:    python3-prometheus_client
BuildRequires:    python3-tomli

%{?systemd_requires}

Requires(pre): shadow-utils
Requires:    systemd
Requires:    pungi
Requires:    python3-requests-gssapi
Requires:    python3-fedora
Requires:    python3-funcsigs
Requires:    python3-openidc-client
Requires:    python3-productmd
Requires:    hardlink
Requires:    python3-libmodulemd
Requires:    gobject-introspection
Requires:    python3-psutil
Requires:    python3-flufl-lock
Requires:    python3-celery
Requires:    python3-flask
Requires:    python3-flask-login
Requires:    python3-flask-sqlalchemy
Requires:    python3-sqlalchemy
Requires:    python3-systemd
Requires:    python3-ldap
Requires:    python3-defusedxml
Requires:    python3-flask-migrate
Requires:    python3-fedora-messaging
Requires:    fedora-messaging
Requires:    python3-kobo
Requires:    python3-prometheus_client

Requires:    python3-odcs-common = %{version}-%{release}


%description
The On Demand Compose Service (ODCS) creates temporary composes using Pungi
tool and manages their lifetime. The composes can be requested by external
services or users using the REST API provided by Flask frontend.

%package -n python3-odcs-common
Summary:        ODCS subpackage providing code shared between server and client.
%{?python_provide:%python_provide python3-odcs-client}

Requires:       python3-six

%description -n python3-odcs-common
ODCS subpackage providing code shared between server and client.

%package -n python3-odcs-client
Summary:        ODCS client module
%{?python_provide:%python_provide python3-odcs-client}

Requires:       python3-filelock
Requires:       python3-jwt
Requires:       python3-requests
Requires:       python3-requests-gssapi
Requires:       python3-odcs-common = %{version}-%{release}

%description -n python3-odcs-client
Client library for sending requests to On Demand Compose Service (ODCS).

%package -n odcs-client
Summary:        ODCS command line client
Requires:       python3-odcs-client = %{version}-%{release}

%description -n odcs-client
Command line client for sending requests to ODCS.


%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install

export PYTHONPATH=%{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}%{_mandir}/man1
for command in odcs-manager odcs-frontend odcs-gencert ; do
export ODCS_CONFIG_DIR=server/conf/
export ODCS_DEVELOPER_ENV=1
help2man -N \
    --version-string=%{version} %{buildroot}%{_bindir}/$command  > \
    %{buildroot}%{_mandir}/man1/$command.1 || \
    %{buildroot}%{_bindir}/$command --help

done

install -d -m 0755 %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/

install -d -m 0755 %{buildroot}%{_datadir}/odcs
install -p -m 0644 server/contrib/odcs.wsgi %{buildroot}%{_datadir}/odcs


%pre
getent group odcs >/dev/null || groupadd -r odcs
getent passwd odcs >/dev/null || \
    useradd -r -g odcs -s /sbin/nologin \
    -c "On Demand Compose Service user" odcs
exit 0

%post
%systemd_post odcs-backend.service

%preun
%systemd_preun odcs-backend.service

%postun
%systemd_postun_with_restart odcs-backend.service

%check
nosetests-%{python3_version} -v

%files -n odcs-client
%doc README.md
%{_bindir}/odcs

%files -n python3-odcs-common
%doc README.md
%dir %{python3_sitelib}/odcs/
%{python3_sitelib}/odcs/__init__.py*
%{python3_sitelib}/odcs/common/
%{python3_sitelib}/odcs-%{version}.dist-info/
%exclude %{python3_sitelib}/odcs/__pycache__

%files -n python3-odcs-client
%doc README.md
%dir %{python3_sitelib}/odcs/
%{python3_sitelib}/odcs/client/
%exclude %{python3_sitelib}/odcs/__pycache__

%files
%doc README.md
%{_unitdir}/odcs-backend.service
%{python3_sitelib}/odcs/server
%{_bindir}/odcs-*
%{_mandir}/man1/odcs-*.1*
%{_datadir}/odcs
%dir %{_sysconfdir}/odcs
%config(noreplace) %{_sysconfdir}/odcs/config.py
%config(noreplace) %{_sysconfdir}/odcs/pungi.conf
%config(noreplace) %{_sysconfdir}/odcs/raw_config_urls.conf
%config(noreplace) %{_sysconfdir}/odcs/raw_config_wrapper.conf
%exclude %{_sysconfdir}/odcs/*.py[co]
%exclude %{_sysconfdir}/odcs/__pycache__
%exclude %{python3_sitelib}/odcs/__pycache__


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Lubomír Sedlář <lsedlar@redhat.com> - 0.8.0-5
- Backport patch for client printing non-json to stdout

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.13

* Mon Mar 25 2024 Nils Philippsen <nils@tiptoe.de> - 0.8.0-3
- Revert constraining SQLAlchemy version

* Thu Mar 21 2024 Nils Philippsen <nils@tiptoe.de> - 0.8.0-2
- Require SQLAlchemy < 2

* Wed Jan 24 2024 Haibo Lin <hlin@redhat.com> - 0.8.0-1
- client: Add --env option
- client: Add arg for extending compose's life
- client: Avoid waiting for finished compose
- client: Convert client script to entry point
- client: Enable OpenTelemetry tracing for client
- client: Fix wait command failed with error: KeyError: 'state_name'
- client: Improve token expiration checking
- client: Move server config to a file
- client: Replace openidc_client with TokenManager
- client: Support OIDC authentication
- client: Use NO_OIDC_AUTHZ_CODE to disalbe authz code flow
- docker: Add healthchecks to docker-compose.yml
- docker: Install mod_auth_openidc
- docker: Pass extra args to start_odcs_from_here
- docker: Update Dockerfile to install opentelemetry
- docker: Update base image to fedora 38
- docker: Use post release for container
- docker: download cacert securely
- docker: new RH IT Root CA location
- docs: Update docs configuration
- server/client: Renew compose with new label
- server: Add oidc_or_kerberos auth backend
- server: Add retry to clone_repo
- server: Add souce and debuginfo configurations
- server: Enable OpenTelemetry tracing on server side
- server: Fix compatibility with Python 3.6
- server: Flask 2.3 compatibility
- server: Improve raw_config_composes metric
- server: Load ODCS_CELERY_BROKER_URL in config file
- server: Make raw_config_composes_total a Gauge
- server: Rework handling Pulp content sets
- server: Update example config with OIDC options
- server: metrics: Avoid decrementing counter
- tests: Run backend tests with py36
- tests: Set flask.g._login_user for tests

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 Haibo Lin <hlin@redhat.com> - 0.7.0-1
- backend: Add odcs-credential-helper executable
- backend: Add support for git credentials
- backend: Set env var with raw config source name
- backend: Use credential helper for initial config clone
- backend: pulp: Handle missing product_versions
- client: Add --arch option to create-build subcommand
- doc: Document env argument to utils.execute_cmd
- frontend: Allow admins to request any compose
- frontend: Delete deprecated conf.auth_ldap_group_base
- frontend: Merge all metrics into a single thread
- frontend: Optimize compose count metrics gathering
- frontend: Support OIDC authentication to CTS
- server: Fix compatibility with Python 3.12
- server: Fix flake8 complaints

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Haibo Lin <hlin@redhat.com> - 0.6.0-3
- Backport patch for Python 3.12

* Mon Jul 10 2023 Python Maint <python-maint@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.12

* Wed May 24 2023 Haibo Lin <hlin@redhat.com> - 0.6.0-1
- backend/client: Allow compose with no label
- backend: Clean up ODCS backend code
- backend: Switch to PKI authentication for pulp
- backend: pulp: Correctly handle merged repos
- backend: pulp: Stop stripping https
- client: Remove dependency on pyopenssl from client
- frontend: Add metrics of workers per queue
- frontend: Only warn when openapi is missing

* Tue May 16 2023 Lubomír Sedlář <lsedlar@redhat.com> - 0.5.0-2
- Remove obsolete dependencies

* Wed Mar 01 2023 Haibo Lin <hlin@redhat.com> - 0.5.0-1
- backend: Handle raw config file in subdirectory implicitly
- backend: pulp: Always include explicitly mentioned repos
- client: switch to HTTPSPNEGOAuth and drop mutual_authentication
- docs: Improve documentation for pulp composes
- server: Load raw_config_urls config without reboot
- server: Refine server config initializing
- Add missing comma in setup.py
- Update formatting to satisfy latest black
- Update license info

* Fri Feb 10 2023 Lubomír Sedlář <lsedlar@redhat.com> - 0.4.0-2
- Resolve conflict after branches diverging after mass rebuild for Fedora 38
- Drop unused patches

* Wed Dec 07 2022 Haibo Lin <hlin@redhat.com> - 0.4.0-1
- backend: Drop python 2 support
- backend: Remove non-latest symlink before creating
- cleanup: Delete unneeded requirement
- client: Add missing requirement openidc-client
- client: Customize user-agent of odcs-client
- client: Drop python 2 support
- client: improve create-tag --help description
- frontend: Allow `^` character in ODCS input.
- frontend: Allow querying rover groups
- frontend: Brand new API doc available at /api/1/
- frontend: Drop python 2 support
- frontend: Optimized metrics raw_config_types
- promote: Stop checking symlinks before promoting

* Fri Sep 30 2022 Haibo Lin <hlin@redhat.com> - 0.3.8-2
- Revert "server: Add new metrics for raw_config source"

* Thu Sep 29 2022 Haibo Lin <hlin@redhat.com> - 0.3.8-1
- server: Mark compose as failed on scheduling error
- server: Do not append newline to state_reason when no errors from pungi log
- server: Fix escaping issue in Bad Request error message
- server: Add new metrics for raw_config source
- server: Update Dockerfile
- server: Add compose id to scheduling error message
- server: Fix routing rule checking
- server: Fix hardcoded path
- server: Added CSS to index.html
- server: Fix python 2 compatibility in promote script
- server: Convert ldap query result from bytes to str
- server: Print mbs url when query failed
- server: Check existence of target_dir in runtime
- server: Use conf.target_dir_url in home page
- client: Replace requests-kerberos with requests-gssapi
- client: Improve help message of renew and delete commands
- client: Return 1 if the generated compose is failed
- tests: Generate html coverage report in CI job
- tests: Update Dockerfile-test
- tests: Add docs env to tox.ini
- tests: Add Jenkinsfile for CI
- tests: Fix tests for rhel 8 build
- tests: Check pytest for TestConfiguration
- cleanup: Add .env to gitignore
- cleanup: Update author in setup.py
- cleanup: Remove funcsigs and httplib2 from requirements.txt
- cleanup: Remove python-fedora from requirements.txt

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 22 2022 Haibo Lin <hlin@redhat.com> - 0.3.7-1
- server: Add compose_id attribute when the compose is re-used
- server: Return empty value for results_repourl and results_repofile for raw_config composes
- server: Fix Python 2 compatibility
- server: Avoid koji tag cache being removed while in use
- server: Update the error message when the brew connection is failed
- client: Replace http request with https in order prevent false redirection
- doc: Remove EPEL from README
- cleanup: Delete Jenkinsfile
- cleanup: Format code for black 22.1.0
- cleanup: Fix create_sqlite_db script

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Haibo Lin <hlin@redhat.com> - 0.3.6-1
- server: Use conf.koji_profile instead of hardcoded brew value
- server: Cleanup generating composes never finished
- server: ODCS fail with "Unknown Koji tag" even for first compose from this tag
- server: Disable celery built-in periodic task celery.backend_cleanup
- server: fix spelling for seconds_to_live description
- server: Fix retry decorator when ProtocolError happens in pulp requests
- server: Improve error reporting for MBS failures
- server: modify odcs-promote-compose to continue an interrupted promote
- server: Allow multiarch ODCS repo install from correct basearch
- server: Fix the error while renewing the empty compose
- server: Fix error while deleting the compose by anonymous user
- server: Handle celery broker connection issue
- client: Suggest KRB5_TRACE env variable option on auth failure
- client: Improve odcs create-module user experience
- client: improve renew --help description
- README: improve "renewing the compose" section
- README: update client install instructions
- cleanup: Delete copr since it is not used anymore
- Move "mock" pypi package to test-requirements.txt
- Create docker-compose file in order to run the ODCS locally

* Tue Aug 17 2021 Lubomír Sedlář <lsedlar@redhat.com> - 0.3.4-6
- Rebuilt to sync changelog and release

* Tue Aug 17 2021 Lubomír Sedlář <lsedlar@redhat.com> - 0.3.4-5
- New upstream release
- Drop dependency on python-flask-script
- Backport patch for client to talk to old servers

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.51-4
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.51-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Lubomír Sedlář <lsedlar@redhat.com> - 0.2.51-1
- New upstream release
- Remove unused dependency on python3-pdc-client and instead pull in
  python3-requests-kerberos directly

* Tue Sep 08 2020 Lubomír Sedlář <lsedlar@redhat.com> - 0.2.50-1
- New upstream release

* Wed Aug 19 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.49-1
- new version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.48-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 31 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.48-1
- new version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.46-2
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.46-1
- new version

* Tue Apr 21 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.45-1
- new version

* Mon Apr 20 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.44-1
- new version

* Wed Apr 01 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.42-1
- new version

* Fri Mar 20 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.41-1
- new version

* Mon Mar 16 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.40-1
- new version

* Wed Mar 04 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.39-1
- new version

* Tue Feb 25 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.38-1
- new version

* Thu Oct 24 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-4
- add fedora-messaging requirement.

* Wed Oct 23 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-3
- backport patch to support fedora-messaging.

* Tue Oct 22 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-2
- Add missing requires, backport patch to disable SNI when not needed.

* Thu Oct 17 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.23-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.23-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.23-2
- require python3-fedmsg instead of fedmsg-hub

* Fri Feb 15 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.23-1
- new version

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.2.7-5
- Update requires for python-gobject -> python2-gobject rename

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Ralph Bean <rbean@redhat.com> - 0.2.7-1
- new version

* Wed Jun 20 2018 Ralph Bean <rbean@redhat.com> - 0.2.6.2-1
- new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6.1-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6.1-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Ralph Bean <rbean@redhat.com> - 0.2.6.1-1
- new version

* Thu Jun 14 2018 Ralph Bean <rbean@redhat.com> - 0.2.6-1
- new version

* Wed Jun 06 2018 Ralph Bean <rbean@redhat.com> - 0.2.4-2
- Add dep on python-requests-kerberos
  https://pagure.io/odcs/issue/203

* Mon Jun 04 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.4-1
- updated to new version 0.2.4

* Mon May 07 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.3-1
- updated to new version 0.2.3.

* Thu Apr 19 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.2-1
- updated to new version 0.2.2.

* Mon Mar 12 2018 Ralph Bean <rbean@redhat.com> - 0.2.1-2
- Python3 subpackages.

* Mon Mar 12 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.1-1
- updated to new version 0.2.1.

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 26 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.0-1
- updated to new version 0.2.0.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Jan Kaluza <jkaluza@redhat.com> - 0.1.7-2
- restart odcs-backend.service on failure.

* Mon Feb 05 2018 Jan Kaluza <jkaluza@redhat.com> - 0.1.7-1
- updated to new version 0.1.7.

* Thu Jan 11 2018 Jan Kaluza <jkaluza@redhat.com> - 0.1.6-1
- updated to new version 0.1.6.

* Tue Dec 12 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-5
- do not remove pungi ODCS composes

* Mon Dec 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-4
- fix Koji kerberos login with keytab

* Mon Dec 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-3
- fix Koji kerberos login with keytab

* Mon Dec 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-2
- fix traceback in unique_path.

* Fri Dec 08 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-1
- updated to new version 0.1.5

* Fri Nov 24 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.4-1
- updated to new version 0.1.4.

* Fri Nov 24 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.3-1
- updated to new version 0.1.3.

* Wed Nov 01 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.2-1
- updated to new version 0.1.2.

* Mon Oct 30 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.1-3
- Require:hardlink

* Mon Oct 30 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.1-1
- updated to new version 0.1.1.

* Thu Oct 12 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.0-2
- use http instead of https for pulp .repo file

* Fri Oct 06 2017 Ralph Bean <rbean@redhat.com> - 0.1.0-1
- new version

* Thu Oct 05 2017 Ralph Bean <rbean@redhat.com> - 0.0.8-1
- new version

* Fri Sep 29 2017 Ralph Bean <rbean@redhat.com> - 0.0.7-1
- new version

* Tue Sep 26 2017 Ralph Bean <rbean@redhat.com> - 0.0.6-1
- new version

* Thu Sep 21 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.5-1
- new version

* Thu Aug 10 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.4-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-4
- fix reversed condition for python2-* dependencies

* Mon Jul 17 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-3
- Add python2- prefix to requirements when it makes sense
- Add -p to install command to preserve timestamp
- Fix macros formatting, use _datadir instead of /usr/share

* Tue Jul 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-2
- fix dependencies

* Thu Jun 29 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-1
- Initial version of spec file
