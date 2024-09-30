%define with_admin 1
%define with_client 1
%define with_django 1
%define with_hub 1
%define with_worker 1

Name:           kobo
Version:        0.37.0
Release:        3%{?dist}
License:        LGPL-2.1-only
Summary:        Python modules for tools development
URL:            https://github.com/release-engineering/kobo
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Kobo is a set of python modules designed for rapid tools development.

%if 0%{?with_admin}
%package admin
Summary:        Kobo admin script for instant project deployment
Requires:       python3-%{name}-admin

%description admin
Kobo admin provides templates for various kobo-based projects,
incl. CLI, hub client, worker and hub.
%endif

%package -n python3-%{name}
Summary:        Python modules for tools development
Requires:       %{py3_dist six}
%py_provides    python3-%{name}

%description -n python3-%{name}
Kobo is a set of python modules designed for rapid tools development.


%if 0%{?with_django}
%package -n python3-%{name}-django
Summary:        Django components
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3dist(django) >= 1.11
Requires:       python3-setuptools
%py_provides    python3-%{name}-django

%description -n python3-%{name}-django
Django components.
%endif


%if 0%{?with_client}
%package -n python3-%{name}-client
Summary:        CLI client
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-requests-gssapi
%py_provides    python3-%{name}-client

%description -n python3-%{name}-client
CLI client.
%endif


%if 0%{?with_worker}
%package -n python3-%{name}-worker
Summary:        Worker daemon processing tasks submitted to the hub
Requires:       python3-%{name} = %{version}-%{release}
%py_provides    python3-%{name}-worker

%description -n python3-%{name}-worker
Worker daemon processing tasks submitted to the hub.
%endif


%if 0%{?with_hub}
%package -n python3-%{name}-hub
Summary:        XML-RPC and web interface to a task database
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3dist(django) >= 1.11
Requires:       python3-setuptools
Requires:       gzip
%py_provides    python3-%{name}-hub

%description -n python3-%{name}-hub
Hub is a XML-RPC and web interface to a task database.
%endif


%package -n python3-%{name}-rpmlib
Summary:        Functions to manipulate with RPM files
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-rpm
Requires:       python3-koji
%py_provides    python3-%{name}-rpmlib

%description -n python3-%{name}-rpmlib
Rpmlib contains functions to manipulate with RPM files.


%if 0%{?with_admin}
%package -n python3-%{name}-admin
Summary:        Kobo admin script for instant project deployment
Requires:       python3-%{name} >= %{version}
Requires:       python3dist(django) >= 1.11
%py_provides    python3-%{name}-admin

%description -n python3-%{name}-admin
Python library for kobo-admin command.
%endif


%prep
%autosetup
%py3_shebang_fix kobo/admin/kobo-admin kobo/admin/templates/*/*


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%if ! 0%{?with_admin}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/admin
rm -rf $RPM_BUILD_ROOT/%{_bindir}/kobo-admin
%endif

%if ! 0%{?with_client}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/client
%endif

%if ! 0%{?with_django}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/django
%endif

%if ! 0%{?with_hub}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/hub
%endif

%if ! 0%{?with_worker}
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/kobo/worker
%endif

%if 0%{?with_admin}
%files admin
%{_bindir}/kobo-admin
%endif

%files -n python3-%{name}
%dir %{python3_sitelib}/kobo
%{python3_sitelib}/kobo/*.py*
%{python3_sitelib}/kobo/__pycache__
%exclude %{python3_sitelib}/kobo/rpmlib.py*
%{python3_sitelib}/%{name}-*.dist-info
%doc AUTHORS
%license COPYING LICENSE


%if 0%{?with_django}
%files -n python3-%{name}-django
%{python3_sitelib}/kobo/django
%endif


%if 0%{?with_client}
%files -n python3-%{name}-client
%{python3_sitelib}/kobo/client
%endif


%if 0%{?with_worker}
%files -n python3-%{name}-worker
%{python3_sitelib}/kobo/worker
%endif


%if 0%{?with_hub}
%files -n python3-%{name}-hub
%{python3_sitelib}/kobo/hub
%endif


%files -n python3-%{name}-rpmlib
%{python3_sitelib}/kobo/rpmlib.py*


%if 0%{?with_admin}
%files -n python3-%{name}-admin
%{python3_sitelib}/kobo/admin
%endif


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Lukáš Zaoral <lzaoral@redhat.com> - 0.37.0-2
- use provides for django to be compatible with versioned django packages

* Thu Jul 04 2024 Lukáš Zaoral <lzaoral@redhat.com> - 0.37.0-1
- rebase to latest upstream release (rhbz#2295515)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.36.2-2
- Rebuilt for Python 3.13

* Mon May 06 2024 Lukáš Zaoral <lzaoral@redhat.com> - 0.36.2-1
- rebase to latest upstream version (rhbz#2278908)

* Fri Apr 05 2024 Lukáš Zaoral <lzaoral@redhat.com> - 0.36.1-1
- rebase to latest upstream version (rhbz#2273570)

* Wed Mar 20 2024 Lukáš Zaoral <lzaoral@redhat.com> - 0.36.0-1
- rebase to latest upstream version (rhbz#2270305)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Lukáš Zaoral <lzaoral@redhat.com> - 0.35.1-1
- rebase to latest upstream release (rhbz#2255494)

* Wed Dec 13 2023 Lukáš Zaoral <lzaoral@redhat.com> - 0.35.0-1
- rebase to latest upstream release (rhbz#2254256)

* Fri Nov 24 2023 Lukáš Zaoral <lzaoral@redhat.com> - 0.34.0-1
- rebase to latest upstream release (rhbz#2250475)

* Wed Nov 08 2023 Lukáš Zaoral <lzaoral@redhat.com> - 0.33.0-1
- rebase to latest upstream release (rhbz#2245972)

* Mon Oct 23 2023 Lukáš Zaoral <lzaoral@redhat.com> - 0.32.0-1
- rebase to latest upstream release (rhbz#2245360)

* Thu Oct 19 2023 Lukáš Zaoral <lzaoral@redhat.com> - 0.31.0-1
- rebase to latest upstream release (rhbz#2244965)

* Wed Sep 06 2023 Lukáš Zaoral <lzaoral@redhat.com> - 0.30.1-2
- modernize spec file

* Mon Sep 04 2023 Pavel Simovec <psimovec@redhat.com> - 0.30.1-1
- New upstream release 0.30.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.27.0-2
- Rebuilt for Python 3.12

* Wed Mar 08 2023 Rohan McGovern <rohanpm@fedoraproject.org> - 0.27.0-1
- New upstream release 0.27.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Rohan McGovern <rohanpm@fedoraproject.org> - 0.25.0-2
- Declare dependencies on python3-setuptools (#2155008)
- Apply pathfix.py for ambiguous shebangs

* Thu Sep 01 2022 Rohan McGovern <rohanpm@fedoraproject.org> - 0.25.0-1
- New upstream release 0.25.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.24.0-2
- Rebuilt for Python 3.11

* Wed May 04 2022 Rohan McGovern <rohanpm@fedoraproject.org> - 0.24.0-1
- New upstream release 0.24.0

* Mon Apr 11 2022 Rohan McGovern <rohanpm@fedoraproject.org> - 0.23.0-1
- New upstream release 0.23.0

* Thu Mar 10 2022 Rohan McGovern <rohanpm@fedoraproject.org> - 0.20.3-1
- New upstream release 0.20.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Rohan McGovern <rohanpm@fedoraproject.org> - 0.20.1-1
- New upstream release 0.20.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Rohan McGovern <rohanpm@fedoraproject.org> - 0.20.0-1
- New upstream release 0.20.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.19.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Rohan McGovern <rohanpm@fedoraproject.org> - 0.19.0-1
- New upstream release 0.19.0

* Mon Nov 30 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 0.18.0-1
- New upstream release 0.18.0

* Mon Oct 05 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 0.17.0-1
- New upstream release 0.17.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 0.15.1-1
- New upstream release 0.15.1

* Thu Jun 25 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 0.15.0-1
- New upstream release 0.15.0

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 0.14.0-1
- New upstream release 0.14.0
- Adds client dependency on requests-gssapi for gssapi client auth

* Wed Apr 22 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0 (#1789890)

* Thu Feb 13 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 0.12.0-1
- New upstream release 0.12.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 0.11.0-1
- New upstream release 0.11.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-4
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 0.10.0-3
- Disable python2 subpackages by default (RHBZ#1732080)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 0.10.0-1
- New upstream release 0.10.0

* Sun Feb 17 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 0.9.0-1
- New upstream release 0.9.0
- Use pypi_source to obtain sources

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Petr Viktorin <pviktori@redhat.com> - 0.8.0-2
- Remove packages needing python2-django1.11 on Fedora 30+ (RHBZ#1632301)

* Fri Nov 30 2018 Rohan McGovern <rmcgover@redhat.com> - 0.8.0-1
- New upstream release 0.8.0

* Fri Nov 30 2018 Rohan McGovern <rmcgover@redhat.com> - 0.7.0-10
- Add missing dependencies on python-six (RHBZ#1654946)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-8
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-7
- Fixes in packaging

* Tue Jan 30 2018 Rohan McGovern <rmcgover@redhat.com> - 0.7.0-6
- Migrate to python2-django1.11
  https://fedoraproject.org/wiki/Changes/Django20

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 0.7.0-5
- Fix directory ownership in python3 subpackage

* Mon Oct 30 2017 Lumír Balhar <lbalhar@redhat.com> - 0.7.0-4
- Remove redefinition of epel macro (RHBZ#1164700)

* Wed Oct 18 2017 Rohan McGovern <rmcgover@redhat.com> - 0.7.0-3
- Fix duplicate packaging of kobo-admin for python2, python3
- Fix some python3 packages depending on python2 packages
- Prefer python2-* packages over unprefixed packages for Requires
- Move kobo-admin to own package (Lubomír Sedlář)

* Wed Oct 18 2017 Rohan McGovern <rmcgover@redhat.com> - 0.7.0-2
- Fix Provides/Obsoletes to follow packaging guidelines (Lubomír Sedlář)

* Tue Oct 17 2017 Rohan McGovern <rmcgover@redhat.com> - 0.7.0-1
- New upstream release 0.7.0
- Build Python 3 packages (Lubomír Sedlář)

* Tue Sep 05 2017 Rohan McGovern <rmcgover@redhat.com> - 0.6.0-1
- New upstream release 0.6.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov  4 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.2-2
- Convert to modern python macros
- Own /usr/lib/python2.7/site-packages/kobo/ directory

* Tue Jul 26 2016 Daniel Mach <dmach@redhat.com> - 0.5.2-1
- conf.py: use print() function (Ken Dreyer)
- conf.py: py2/py3 compatible exception handling (Ken Dreyer)
- Fix shortcuts to run on py2.4. (Daniel Mach)
- Closed tasks can be interrupted without throwing an exception (Marek Šabo)
- Add __setitem__ to FileCache (Lubomír Sedlář)
- Show minimal priority in admin (Tomas Kopecek)
- Add tests/README (Alexander Todorov)
- Add tests for RPMs with 'something-X.Y' names (Alexander Todorov)
- xmlrpc: remember to call super class constructor (Kamil Dudka)
- Condition for setting hostport generalized (Marek Šabo)
- Http proxy working on Fedora 22 (Marek Šabo)
- Pass arbitrary args to logging module (Lubomír Sedlář)
- migration for min_priority (Tomas Kopecek)
- fix default values (Tomas Kopecek)
- minimal priority for worker (Tomas Kopecek)
- backward compatibility with django 1.6 (Tomas Kopecek)
- make get_tasks call backwards compatible (Tomas Kopecek)
- Add permission for displaying task tracebacks (Tomas Kopecek)
- report correct allowed username length (Tomas Kopecek)
- Add a RPC call and a command to list running tasks. (Tomas Kopecek)
- Add --all option for enable|disable worker command. (Tomas Kopecek)
- Fix multiple same checksum types. (Tomas Kopecek)
- Django 1.8 rebase (Tomas Kopecek)
- Add ssl context for https. (Tomas Kopecek)
- Don't add additional space when printing log. (Tomas Kopecek)
- Fix displayed task time (Tomas Kopecek)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Daniel Mach <dmach@redhat.com> - 0.5.1-1
- Enable/disable worker. (Tomas Kopecek)
- upload_task_log: correctly handle unicode vs str strings. (Tomas Kopecek)
- resubmit_task: add missing 'force' parameter. (Tomas Kopecek)

* Sat Nov 15 2014 Daniel Mach <dmach@redhat.com> - 0.5.0-1
- Modify shortcuts.run() to pass all **kwargs to Popen(). (Daniel Mach)
- Admin page for kobo.auth.User (Tomas Kopecek)
- Unset active menu if no other menu is active (Lubomír Sedlář)
- Allow rendering menu for bootstrap's navbar (Lubomír Sedlář)
- Handle menu items without text as dividers (Lubomír Sedlář)
- allow --force in resubmit-tasks CLI command (Tomas Kopecek)
- Django 1.6 db transaction model (Tomas Kopecek)
- CLI command for viewing log files (Tomas Kopecek)
- Display overall time in task page (Tomas Kopecek)
- Fix shortcuts.run() to handle errno.EINTR correctly. (Tomas Tomecek)
- Don't count assigned tasks into worker load. (Tomas Tomecek)
- Human readable state exceptions. (Tomas Kopecek)
- Human readable JSONField. (Tomas Kopecek)

* Fri Jan 17 2014 Daniel Mach <dmach@redhat.com> - 0.4.3-1
- Rename User model to properly adjust to older db schema. (Tomas Kopecek)
- Fix typo in login template. (Tomas Kopecek)
- Switch from simplejson to json. (Daniel Mach)

* Tue Dec 17 2013 Daniel Mach <dmach@redhat.com> - 0.4.2-1
- Revamp make_nvr() and make_nvra(), make them public (add to __all__), add tests. (Daniel Mach)
- Fix: display subtasks in task's detail view (Tomas Tomecek)
- Fix JSONField (load and dump) (Tomas Tomecek)
- Fix CSRF exemption in XML-RPC handler factory (Tomas Tomecek)
- View simplifications (Tomas Kopecek)
- Translate everything in templates (Tomas Kopecek)
- Additional fields visible in admin, searching/filtering (Tomas Kopecek)
- Use more proper class-based style for generic forms (Tomas Kopecek)
- Refactored generic views. (Tomas Kopecek)
- Fix rtf content type test for py2.4. (Daniel Mach)
- Add FileCache.items() to export items() and also fix py3. (Daniel Mach)
- Remove slots from most places. (Daniel Mach)
- Improve shortcuts.parse_checksum_line() to support escaped checksum lines. (Daniel Mach)
- Add 'executable' argument to shortcuts.run(). (Daniel Mach)

* Mon Oct 14 2013 Daniel Mach <dmach@redhat.com> - 0.4.1-1
- Return 'nosrc' arch when RPMTAG_NOPATCH RPM header is set. (Daniel Mach)
- Fix 'ImproperlyConfigured: The SECRET_KEY setting must not be empty.' exception in test_types.py. (Daniel Mach)
- Fix setup script to install additional package data. (Daniel Mach)
- Fix reading RPMTAG_NOSOURCE and RPMTAG_NOPATCH headers from 'nosrc' RPMs. (Daniel Mach)

* Mon Jul 29 2013 Daniel Mach <dmach@redhat.com> - 0.4.0-2
- Drop admin subpackage on rhel <= 5
- Drop admin, django and hub subpackages on epel 6

* Thu Jul 25 2013 Daniel Mach <dmach@redhat.com> - 0.4.0-1
- Drop django and hub subpackages on rhel <= 5
- Set filename to be real name of a downloaded file. (Tomas Tomecek)
- Fix logwatcher to scroll to latest logs. (Tomas Tomecek)
- Remove obsolete function kobo.django.views.generic._object_list(). (Tomas Kopecek)
- Updated README for 0.4.0 release (Tomas Kopecek)
- Revamp setup.py and related files. (Daniel Mach)
- LongnameUser table has auth_user db table name for easier upgrade. (Tomas Kopecek)
- Add checksum_type to SimpleRpmWrapper. (Tomas Kopecek)
- Add kobo.threads.run_in_threads() helper. (Tomas Kopecek)
- Django 1.5 rebase. (Tomas Kopecek)
- Remove unnecessary slots from pkgset.FileCache. (Daniel Mach)

* Mon Feb 11 2013 Daniel Mach <dmach@redhat.com> - 0.3.8-1
- Don't catch and mask any exceptions in cli.CommandOptionParser.run(). (Daniel Mach)
- Set an empty keyring in rpmlib.get_rpm_header(). (Daniel Mach)
- Format Fault's output to be nicer. (Tomas Tomecek)
- Display error when cancelling task fails. (Tomas Tomecek)
- Fix task cancelation method name. (Tomas Tomecek)
- Add pkgset.SimpleRpmWrapper; support pickle by providing __getstate__() and __setstate__() methods. (Daniel Mach)
- Enable searching in task list by label. (Tomas Tomecek)
- Enable making custom queries in view task_list. (Tomas Tomecek)
- Limit value length to 200 characters in tback.Traceback. (Daniel Mach)
- Fix email.utils import to work with py2.4. (Daniel Mach)
- Backwards compatibility bugfix in hub.models. (Tomas Tomecek)

* Wed Jan 16 2013 Daniel Mach <dmach@redhat.com> - 0.3.7-1
- Proxy support enhancement (Tomas Mlcoch)
- Improve task ordering. (Daniel Mach)
- Better formatting in Traceback output. (Tomas Tomecek)
- Add JSONField.value_to_string() method. (Tomas Tomecek)
- Improve task dir deletion and task files view. (Tomas Tomecek)
- allow line buffering for shortcuts.run() (Tomas Kopecek)
- Allow to specify buffer_size in shortcuts.run(). (Daniel Mach)
- Add rpmlib.get_changelogs_from_header() and pkgset.RpmWrapper.changelogs. (Daniel Mach)
- Support https_proxy environ variable (Tomas Mlcoch)
- Create pid file in a more secure way. (Daniel Mach)
- Create empty kobo.django.auth.models module to fix crashes in Django 1.4. (Daniel Mach)
- Add shortcuts.makedirs() function which is identical to os.makedirs but doesn't fail on existing dirs. (Daniel Mach)
- Fix typo in the 404.html template. (Daniel Mach)
- Fix traceback on undefined workdir in kobo.shortcuts.run(). (Daniel Mach)
- Add help-rst command which generates rst documentation for all CommandOptionParser's commands. (Daniel Mach)

* Wed Dec 21 2011 Daniel Mach <dmach@redhat.com> - 0.3.6-1
- Clarify auth middleware ordering in the hub settings template. (Daniel Mach)
- Add kobo.threads -- a simple threading worker pool. (Daniel Mach)
- Fix force_list and force_tuple to work with sets. (Daniel Mach)
- Implement removing files from a file cache. (Daniel Mach)
- Make shortcuts.run() thread-safe. (Daniel Mach)

* Mon Oct 10 2011 Daniel Mach <dmach@redhat.com> - 0.3.5-1
- Bump version to 0.3.5. (Daniel Mach)
- Return tracebacks in the XML-RPC dispatcher as unicode. (Daniel Mach)
- Refactor MainMenu to be Django 1.3 compliant. (Martin Magr)
- Make StateEnumField Django 1.2 compliant. (Martin Magr)
- Add proxy support to XML-RPC transports. (Daniel Mach)
- Cache stat values in FileWrapper objects, add size and mtime properties. (Tomas Mlcoch)
- Fix unittest kobo.http for Python 2.4. (Tomas Mlcoch)
- Add unit test for kobo.pkgset. (Tomas Mlcoch)
- Rename pkgset.FileCache.__get__ to __getitem__. (Tomas Mlcoch)
- Add unit test for kobo.http. (Tomas Mlcoch)
- Add unit test for kobo.decorators. (Tomas Mlcoch)
- Add docstrings to kobo.http. (Tomas Mlcoch)
- Add UndoHardlink class to __all__. (Tomas Mlcoch)
- Add unit test for kobo.hardlink. (Tomas Mlcoch)
- Fix params for os.utime() call in UndoHardlink class. (Tomas Mlcoch)
- Fix tback.Traceback to work properly in interpreter. (Tomas Mlcoch)
- Use getattr to read Krb5Error.err_code to prevent possible AttributeError in HubProxy. (Daniel Mach)
- Add a new task state - CREATED. (Daniel Mach)
- Fix templates to work properly in debug mode. (Daniel Mach)
- Revamp log downloads - download as a stream, better support for other than .log files, enforce using UPLOAD_DIR in settings. (Daniel Mach)
- Delete empty directories on FileUpload.delete(). (Daniel Mach)
- Catch an exception when deleting an FileUpload object and target file is missing. (Daniel Mach)
- Make sure that xmlrpc.decode_xmlrpc_chunk() won't fail on existing directory. (Daniel Mach)
- Run task cleanup and notification for foreground tasks. (Daniel Mach)
- Enhance shortcuts.iter_chunks() to work with files. (Daniel Mach)
- Upload files in chunks in order to prevent client-side memory issues. (Daniel Mach)
- Exclude file uploads from CSRF protection. (Daniel Mach)
- Add assertRegexpMatches and assertIsInstance to tback tests to make them work on python < 2.7. (Daniel Mach)
- Fix processing unitialized variables in tback. (Martin Bukatovic)
- Fix a traceback in kobo-admin start-hub when a project name contained dashes. (Daniel Mach)
- Add -tt python interpreter argument to project templates. (Daniel Mach)
- Add kobo.rpmlib.parse_evr() to parse E:VR. (Daniel Mach)
- Fix parse_nvra() - arch must not contain '-'. (Daniel Mach)
- Add missing {{ project_name }} prefix to kobo admin templates. (Daniel Mach)
- Start daemons in "/" rather than in working dir. (Daniel Mach)
- Add TransactionMiddleware to the hub template's settings. (Daniel Mach)
- Add skip_broken argument to PluginContainer.register_module() class method. (Daniel Mach)

* Fri Feb 18 2011 Daniel Mach <dmach@redhat.com> - 0.3.4-1
- Add kobo.decorators.log_traceback() devel decorator to log function tracebacks to a file. (Daniel Mach)
- Fix tback.Traceback for py2.4. (Daniel Mach)

* Tue Feb  1 2011 Daniel Mach <dmach@redhat.com> - 0.3.3-1
- Replace double underscores with dots in xmlrpc method names. (Daniel Mach)
- Fix regex in test_tback.py so unit tests pass. (Daniel Mach)
- Fix session handling in worker. (Daniel Mach)
- Fix kobo.Traceback to return empty string on no exception. Add traceback tests. (Tomas Kopecek)
- Simplify hub deployment (add menu and template to default). Tweak kobo-admin templates. (Daniel Mach)
- Add a warning about a possibly read-only database to the worker middleware assert. (Daniel Mach)
- Add task notification() and cleanup() class methods. (Daniel Mach)
- Revamp hub urls and admin templates. (Daniel Mach)
- Prevent a race condition when using CookieTransport in threads in py2.7. (Daniel Mach)
- Add unit test for EnumItem.change_state() return value. (Daniel Mach)
- StateEnum.change_state() now returns bool as documented. (Martin Magr)
- Command argument in kobo.shortcuts.run() can be also a list now. (Daniel Mach)
- Strip path from nvr in kobo.rpmlib.parse_nvr() and parse_nvra(). (Daniel Mach)
- Exclude XML-RPC from CSRF processing. (Daniel Mach)
- Add stdin data support to kobo.shortcuts.run(). (Daniel Mach)
- Add kobo.shortcuts.iter_chunks() to iterate through a list, string or generator and yield chunks of defined size. (Daniel Mach)
- Raise an exception when spawn_subtask() or wait() method is called in a foreground task. (Daniel Mach)
- Add constructor to kobo.django.hacks.UserChangeForm to fix maximum recursion depth error. (Daniel Mach)
- Fix username max_length hack to work with Django 1.2.1. (Martin Bukatovic)
- Add kobo.notification module to send email notifications. (Daniel Mach)
- Process kobo.shortcuts.run() logging in chunks and print data immediately. (Daniel Mach)
- Subtasks have to follow parent's channel and arch. (Martin Magr)
- Compute elapsed time for running tasks. (Tomas Kopecek)

* Wed Oct 27 2010 Daniel Mach <dmach@redhat.com> - 0.3.2-1
- Fix XML-RPC transports to make them work in py2.5 and py2.6. (Daniel Mach)
- Automatically scroll the task log window when we're at the bottom of the page. (Daniel Mach)
- Show self.* attributes in extended tracebacks. (Daniel Mach)
- Compress logs with gzip when a task finishes. (Daniel Mach)
- Convert task logs to utf8 (with "replace" option) to prevent raising UnicodeDecodeError during template processing. (Daniel Mach)

* Tue Oct 19 2010 Daniel Mach <dmach@redhat.com> - 0.3.1-1
- Add help-admin command to display help for admin commands. (Daniel Mach)
- Add config parser support for glob matching on dict keys. (Tomas Kopecek)
- Implement timeout support in xmlrpc transports. (Daniel Mach)
- Improve kobo.xmlrpc.CookieTransport to work with python 2.7 as well. (Daniel Mach)
- Add kobo-admin utility. (Martin Bukatovic)
- Add missing HttpResponseForbidden import to kobo.hub.views. (Daniel Mach)
- Fix bug in "Show only my tasks" search option on Tasks page. (Daniel Mach)

* Fri Aug 13 2010 Daniel Mach <dmach@redhat.com> - 0.3.0-2
- Bump to new upstream version.
- Fix kobo.rpmlib.get_digest_algo_from_header() when RPMTAG_FILEDIGESTALGO contains None value. (Daniel Mach)
- Pass 'conf' argument do daemonized worker's main_loop. (Daniel Mach)

* Mon Feb 15 2010 Daniel Mach <dmach@redhat.com> - 0.2.1-1
- Split rpmlib to a subpackage.
- Add missing "compare_nvr" to __all__. (Daniel Mach)
- Remove duplicate subtask removal in Task.wait(). (Tomas Kopecek)
- Parent task didn't wake up even if all child tasks were finished. (Tomas Kopecek)
- Change 'make log' to use C locales and automatically fill name and email from GIT. (Daniel Mach)
- Fix spawn_subtask argument. (cherry picked from commit 374a4165c16d6b34fa486a38525753969e549415) (Tomas Kopecek)
- Fix XML-RPC method registration. (original patch by Xuqing Kuang) (Daniel Mach)
- Convert rpm.labelCompare's arguments to string to prevent segfaulting. Add compare_nvr tests. (Tomas Kopecek)
- Add Task.get_time_display() to get time spent in task in human readable form. (Daniel Mach)
- Use koji.get_sigpacket_key_id() to read sigkey id from a rpm header. (Daniel Mach)

* Thu Nov  5 2009 Daniel Mach <dmach@redhat.com> - 0.2.0-1
- Rewrite menu to get rid of tuples in menu definition. Always use MenuItem classes. (Daniel Mach)
- Send task logs to hub to enable realtime log watching. (Daniel Mach)
- Add menu_item helper. (Tomas Kopecek)
- New version of menu component. (Tomas Kopecek)
- Order tasks to assign by priority first. (Daniel Mach)
- Fix spacing errors to be more PEP 8 compliant. (Daniel Mach)
- Handle SystemExit in TaskManager.run_task(). (Daniel Mach)
- Add a shortcut and pkgset support for computing hashlib based hashes. (Daniel Mach)
- Add hack enabling 'VERBOSE' log level in the python logging module and Logger class. (Daniel Mach)
- Run tests in alphabetical order. (Daniel Mach)
- Fix TaskAdmin to search for user in correct db field. (Tomas Kopecek)
- More convenient admin listing for Worker model. (Tomas Kopecek)
- Add files to cache faster (skip stat call when possible). (Tomas Kopecek)
- Remove deps on postgresql, httpd, mod_auth_kerb and python-krbV.
- Add AUTHORS, COPYING and LICENSE to kobo.rpm.

* Tue Aug 18 2009 Daniel Mach <dmach@redhat.com> - 0.1.2-1
- Read default paginate_by value from settings in kobo.django.views.generic.object_list. (Tomas Kopecek)
- Add read_from_file() and rename save() to save_to_file() in kobo.shortcuts. (Daniel Mach)
- Reverse FileUpload default ordering. (Daniel Mach)
- Add kobo.conf.get_dict_value() to support dicts with default values. (Daniel Mach)
- Add direct access to files via pkgset.RpmWrapper. (Tomas Kopecek)
- Add documentation to django.auth.krb5. (Daniel Mach)
- Fix worker key generation in kobo.hub.models.Worker.save(). (Daniel Mach)
- Fix a security hole in krb5 middleware: a user was able to log in as different user to admin interface. (Daniel Mach)
- Change Makefile to run tests before creating source tarball. (Daniel Mach)
- Change HubProxy._hub verification to fix exceptions in Python2.6. (Martin Magr)
- Another SQL performance improvement in Task admin. (Tomas Kopecek)
- Set Task.parent as raw_id field to improve admin performance. (Daniel Mach)
- Add (spent) time method to Task and display it in the admin listing. (Tomas Kopecek)

* Wed Jul 22 2009 Daniel Mach <dmach@redhat.com> - 0.1.1-1
- Enhance types.Enum to support help_text and additonal options. Update tests for types module. (Daniel Mach)
- Remove temp directory after file upload. (Tomas Kopecek)
- Remove MANIFEST in make clean. (Daniel Mach)
- Fix shortcuts.run to read complete stdout. (Jan Blazek)
- Add rpmlib.get_file_list_from_header() which extracts file list, colors and checksums from a rpm header. (Daniel Mach)
- Add get_digest_algo_from_header() function to read rpm digest algorithm. (Daniel Mach)
- Update epydoc docstrings in kobo.rpmlib. (Daniel Mach)
- Fix deadlock in run(). Use proc.poll() instead of proc.wait(). (Daniel Mach)
- Update epydoc docstrings in kobo.shortcuts. (Daniel Mach)
- Fix AtributeError when active_submenu is None. (Daniel Mach)
- Return menu dict even if no menu is active. (Daniel Mach)
- Do not allow to register plugins to PluginContainer base class. Add several tests. (Daniel Mach)
- Add test runner. (Daniel Mach)
- Add support for empty submenus. (Martin Magr)

* Wed Jun 17 2009 Daniel Mach <dmach@redhat.com> - 0.1.0-1
- first release
