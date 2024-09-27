# Conditional for release vs. snapshot builds. Set to 1 for release build.
%if ! 0%{?rel_build:1}
    %global rel_build 1
%endif

# Settings used for build from snapshots.
%if 0%{?rel_build}
    %global gitref          %{version}
    %global gittar          avocado-%{version}.tar.gz
%else
    %if ! 0%{?commit:1}
        %global commit      5b21f030001d6eed69c0357cc45b6128c73dc860
    %endif
    %if ! 0%{?commit_date:1}
        %global commit_date 20240819
    %endif
    %global shortcommit     %(c=%{commit};echo ${c:0:9})
    %global gitrel          .%{commit_date}git%{shortcommit}
    %global gitref          %{commit}
    %global gittar          avocado-%{shortcommit}.tar.gz
%endif

# Selftests are provided but may need to be skipped because many of
# the functional tests are time and resource sensitive and can
# cause race conditions and random build failures. They are
# enabled by default.
%global with_tests 1

# resultsdb is not available for RHEL
%if ! 0%{?rhel}
%global with_resultsdb 1
%else
%global with_resultsdb 0
%endif

Name: python-avocado
Version: 92.3
Release: 1%{?gitrel}%{?dist}
Summary: Framework with tools and libraries for Automated Testing
# Found licenses:
# avocado/core/tapparser.py: MIT
# avocado/utils/external/gdbmi_parser.py: MIT
# avocado/utils/external/spark.py: MIT
# optional_plugins/html/avocado_result_html/templates/bootstrap.min.css: MIT
# optional_plugins/html/avocado_result_html/templates/bootstrap.min.js: MIT
# selftests/.data/jenkins-junit.xsd: MIT
# Other files: GPLv2 and GPLv2+
License: GPLv2+ and GPLv2 and MIT
URL: https://avocado-framework.github.io/
Source0: https://github.com/avocado-framework/avocado/archive/%{gitref}/%{gittar}
BuildArch: noarch

BuildRequires: kmod
BuildRequires: procps-ng
BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-jinja2
BuildRequires: python3-lxml
BuildRequires: python3-psutil
%if %{with_resultsdb}
BuildRequires: python3-resultsdb_api
BuildRequires: python3-pycdlib
%endif

%if 0%{?with_tests}
BuildRequires: genisoimage
BuildRequires: libcdio
BuildRequires: psmisc
%if ! 0%{?rhel}
BuildRequires: perl-Test-Harness
%endif
BuildRequires: glibc-all-langpacks
BuildRequires: python3-netifaces
BuildRequires: python3-yaml
%endif
# with_tests

%description
Avocado is a set of tools and libraries (what people call
these days a framework) to perform automated testing.


%prep
%setup -q -n avocado-%{gitref}
%if 0%{?rhel}
sed -e "s/'PyYAML>=4.2b2'/'PyYAML>=3.12'/" -i optional_plugins/varianter_yaml_to_mux/setup.py
%endif
# drop unnecessary install requirement
sed -e "s/'markupsafe<2.0.0', //" -i optional_plugins/html/setup.py
# loosen jinja2 version requirement
sed -e "s/'jinja2<3.0.0'/'jinja2'/" -i optional_plugins/html/setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%py3_build
pushd optional_plugins/html
    %py3_build
popd
%if %{with_resultsdb}
pushd optional_plugins/resultsdb
    %py3_build
popd
%endif
pushd optional_plugins/varianter_yaml_to_mux
    %py3_build
popd
pushd optional_plugins/golang
    %py3_build
popd
pushd optional_plugins/varianter_pict
    %py3_build
popd
pushd optional_plugins/varianter_cit
    %py3_build
popd
pushd optional_plugins/result_upload
    %py3_build
popd
rst2man man/avocado.rst man/avocado.1

%install
%py3_install
for exe in \
    avocado \
    avocado-runner \
    avocado-runner-noop \
    avocado-runner-dry-run \
    avocado-runner-exec-test \
    avocado-runner-python-unittest \
    avocado-runner-avocado-instrumented \
    avocado-runner-tap \
    avocado-runner-requirement-asset \
    avocado-runner-requirement-package \
    avocado-runner-sysinfo \
    avocado-software-manager
do
    mv %{buildroot}%{_bindir}/$exe %{buildroot}%{_bindir}/$exe-%{python3_version}
    ln -s $exe-%{python3_version} %{buildroot}%{_bindir}/$exe-3
    ln -s $exe-%{python3_version} %{buildroot}%{_bindir}/$exe
done
# configuration is held at /etc/avocado only and part of the
# python-avocado-common package
rm -rf %{buildroot}%{python3_sitelib}/avocado/etc
# ditto for libexec files
rm -rf %{buildroot}%{python3_sitelib}/avocado/libexec
# adjust permissions for file containing shebang line needed for
# spawning tasks in podman containers
chmod -c +x %{buildroot}%{python3_sitelib}/avocado/core/nrunner.py
pushd optional_plugins/html
    %py3_install
popd
%if %{with_resultsdb}
pushd optional_plugins/resultsdb
    %py3_install
popd
%endif
pushd optional_plugins/varianter_yaml_to_mux
    %py3_install
popd
pushd optional_plugins/golang
    %py3_install
popd
pushd optional_plugins/varianter_pict
    %py3_install
popd
pushd optional_plugins/varianter_cit
    %py3_install
popd
pushd optional_plugins/result_upload
    %py3_install
popd
# cleanup plugin test cruft
rm -rf %{buildroot}%{python3_sitelib}/tests
mkdir -p %{buildroot}%{_sysconfdir}/avocado
cp -r avocado/etc/avocado/scripts %{buildroot}%{_sysconfdir}/avocado/scripts
cp -r avocado/etc/avocado/sysinfo %{buildroot}%{_sysconfdir}/avocado/sysinfo
mkdir -p %{buildroot}%{_libexecdir}/avocado
cp avocado/libexec/avocado-bash-utils %{buildroot}%{_libexecdir}/avocado/avocado-bash-utils
cp avocado/libexec/avocado_debug %{buildroot}%{_libexecdir}/avocado/avocado_debug
cp avocado/libexec/avocado_error %{buildroot}%{_libexecdir}/avocado/avocado_error
cp avocado/libexec/avocado_info %{buildroot}%{_libexecdir}/avocado/avocado_info
cp avocado/libexec/avocado_warn %{buildroot}%{_libexecdir}/avocado/avocado_warn
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man/avocado.1 %{buildroot}%{_mandir}/man1/avocado.1
mkdir -p %{buildroot}%{_pkgdocdir}
install -m 0644 README.rst %{buildroot}%{_pkgdocdir}
install -d -m 0755 %{buildroot}%{_sharedstatedir}/avocado/data
# place examples in documentation directory
install -d -m 0755 %{buildroot}%{_docdir}/avocado
cp -r examples/gdb-prerun-scripts %{buildroot}%{_docdir}/avocado/gdb-prerun-scripts
cp -r examples/plugins %{buildroot}%{_docdir}/avocado/plugins
cp -r examples/tests %{buildroot}%{_docdir}/avocado/tests
cp -r examples/varianter_cit %{buildroot}%{_docdir}/avocado/varianter_cit
cp -r examples/varianter_pict %{buildroot}%{_docdir}/avocado/varianter_pict
cp -r examples/wrappers %{buildroot}%{_docdir}/avocado/wrappers
cp -r examples/yaml_to_mux %{buildroot}%{_docdir}/avocado/yaml_to_mux
find %{buildroot}%{_docdir}/avocado -type f -name '*.py' -exec chmod -c -x {} ';'


%if 0%{?with_tests}
%check
    # LANG: to make the results predictable, we pin the language
    # that is used during test execution.
    # AVOCADO_CHECK_LEVEL: package build environments have the least
    # amount of resources we have observed so far. Let's avoid tests that
    # require too much resources or are time sensitive
    PATH=%{buildroot}%{_bindir}:%{buildroot}%{_libexecdir}/avocado:$PATH \
        PYTHONPATH=%{buildroot}%{python3_sitelib}:. \
        LANG=en_US.UTF-8 \
        AVOCADO_CHECK_LEVEL=0 \
        %{python3} selftests/check.py --job-api --nrunner-interface \
        --unit --jobs --functional --optional-plugins \
        --disable-plugin-checks robot
%endif


%package -n python3-avocado
Summary: %{summary}
Requires: python-avocado-common == %{version}-%{release}
Requires: gdb
Requires: gdb-gdbserver
Requires: procps-ng
%if ! 0%{?rhel}
Requires: python3-pycdlib
%endif

%description -n python3-avocado
Avocado is a set of tools and libraries (what people call
these days a framework) to perform automated testing.

%files -n python3-avocado
%license LICENSE
%{_pkgdocdir}/README.rst
%{python3_sitelib}/avocado/
%{python3_sitelib}/avocado_framework-%{version}.dist-info
%{_bindir}/avocado-%{python3_version}
%{_bindir}/avocado-3
%{_bindir}/avocado
%{_bindir}/avocado-runner-%{python3_version}
%{_bindir}/avocado-runner-3
%{_bindir}/avocado-runner
%{_bindir}/avocado-runner-noop-%{python3_version}
%{_bindir}/avocado-runner-noop-3
%{_bindir}/avocado-runner-noop
%{_bindir}/avocado-runner-dry-run-%{python3_version}
%{_bindir}/avocado-runner-dry-run-3
%{_bindir}/avocado-runner-dry-run
%{_bindir}/avocado-runner-exec-test-%{python3_version}
%{_bindir}/avocado-runner-exec-test-3
%{_bindir}/avocado-runner-exec-test
%{_bindir}/avocado-runner-python-unittest-%{python3_version}
%{_bindir}/avocado-runner-python-unittest-3
%{_bindir}/avocado-runner-python-unittest
%{_bindir}/avocado-runner-avocado-instrumented-%{python3_version}
%{_bindir}/avocado-runner-avocado-instrumented-3
%{_bindir}/avocado-runner-avocado-instrumented
%{_bindir}/avocado-runner-tap-%{python3_version}
%{_bindir}/avocado-runner-tap-3
%{_bindir}/avocado-runner-tap
%{_bindir}/avocado-runner-requirement-asset-%{python3_version}
%{_bindir}/avocado-runner-requirement-asset-3
%{_bindir}/avocado-runner-requirement-asset
%{_bindir}/avocado-runner-requirement-package-%{python3_version}
%{_bindir}/avocado-runner-requirement-package-3
%{_bindir}/avocado-runner-requirement-package
%{_bindir}/avocado-runner-sysinfo-%{python3_version}
%{_bindir}/avocado-runner-sysinfo-3
%{_bindir}/avocado-runner-sysinfo
%{_bindir}/avocado-software-manager-%{python3_version}
%{_bindir}/avocado-software-manager-3
%{_bindir}/avocado-software-manager


%package -n python-avocado-common
Summary: Avocado common files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later

%description -n python-avocado-common
Common files (such as configuration) for the Avocado Testing Framework.

%files -n python-avocado-common
%license LICENSE
%{_mandir}/man1/avocado.1.gz
%dir %{_docdir}/avocado
%dir %{_sharedstatedir}/avocado
%dir %{_sysconfdir}/avocado
%dir %{_sysconfdir}/avocado/sysinfo
%dir %{_sysconfdir}/avocado/scripts
%dir %{_sysconfdir}/avocado/scripts/job
%dir %{_sysconfdir}/avocado/scripts/job/pre.d
%dir %{_sysconfdir}/avocado/scripts/job/post.d
%config(noreplace) %{_sysconfdir}/avocado/sysinfo/commands
%config(noreplace) %{_sysconfdir}/avocado/sysinfo/files
%config(noreplace) %{_sysconfdir}/avocado/sysinfo/profilers
%{_sysconfdir}/avocado/scripts/job/pre.d/README
%{_sysconfdir}/avocado/scripts/job/post.d/README


%package -n python3-avocado-plugins-output-html
Summary: Avocado HTML report plugin
License: GPLv2+ and MIT
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-output-html
Adds to avocado the ability to generate an HTML report at every job results
directory. It also gives the user the ability to write a report on an
arbitrary filesystem location.

%files -n python3-avocado-plugins-output-html
%{python3_sitelib}/avocado_result_html/
%{python3_sitelib}/avocado_framework_plugin_result_html-%{version}.dist-info


%if %{with_resultsdb}
%package -n python3-avocado-plugins-resultsdb
Summary: Avocado plugin to propagate job results to ResultsDB
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-resultsdb
Allows Avocado to send job results directly to a ResultsDB
server.

%files -n python3-avocado-plugins-resultsdb
%{python3_sitelib}/avocado_resultsdb/
%{python3_sitelib}/avocado_framework_plugin_resultsdb-%{version}.dist-info
%endif
# with_resultsdb


%package -n python3-avocado-plugins-varianter-yaml-to-mux
Summary: Avocado plugin to generate variants out of yaml files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-varianter-yaml-to-mux
Can be used to produce multiple test variants with test parameters
defined in a yaml file(s).

%files -n python3-avocado-plugins-varianter-yaml-to-mux
%{python3_sitelib}/avocado_varianter_yaml_to_mux/
%{python3_sitelib}/avocado_framework_plugin_varianter_yaml_to_mux-%{version}.dist-info


%package -n python3-avocado-plugins-golang
Summary: Avocado plugin for execution of golang tests
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: python3-avocado == %{version}-%{release}
Requires: golang

%description -n python3-avocado-plugins-golang
Allows Avocado to list golang tests, and if golang is installed,
also run them.

%files -n python3-avocado-plugins-golang
%{python3_sitelib}/avocado_golang/
%{python3_sitelib}/avocado_framework_plugin_golang-%{version}.dist-info
%{_bindir}/avocado-runner-golang


%package -n python3-avocado-plugins-varianter-pict
Summary: Varianter with combinatorial capabilities by PICT
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-varianter-pict
This plugin uses a third-party tool to provide variants created by
Pair-Wise algorithms, also known as Combinatorial Independent Testing.

%files -n python3-avocado-plugins-varianter-pict
%{python3_sitelib}/avocado_varianter_pict/
%{python3_sitelib}/avocado_framework_plugin_varianter_pict-%{version}.dist-info


%package -n python3-avocado-plugins-varianter-cit
Summary: Varianter with Combinatorial Independent Testing capabilities
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-varianter-cit
A varianter plugin that generates variants using Combinatorial
Independent Testing (AKA Pair-Wise) algorithm developed in
collaboration with CVUT Prague.

%files -n python3-avocado-plugins-varianter-cit
%{python3_sitelib}/avocado_varianter_cit/
%{python3_sitelib}/avocado_framework_plugin_varianter_cit-%{version}.dist-info


%package -n python3-avocado-plugins-result-upload
Summary: Avocado plugin propagate job results to a remote host
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-result-upload
This optional plugin is intended to upload the Avocado Job results to
a dedicated sever.

%files -n python3-avocado-plugins-result-upload
%{python3_sitelib}/avocado_result_upload/
%{python3_sitelib}/avocado_framework_plugin_result_upload-%{version}.dist-info


%package -n python-avocado-examples
Summary: Avocado Test Framework Example Tests
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
# documentation does not require main package, but needs to be in lock-step if present
Conflicts: python3-avocado < %{version}-%{release}, python3-avocado > %{version}-%{release}

%description -n python-avocado-examples
The set of example tests present in the upstream tree of the Avocado framework.
Some of them are used as functional tests of the framework, others serve as
examples of how to write tests on your own.

%files -n python-avocado-examples
%license LICENSE
%dir %{_docdir}/avocado
%{_docdir}/avocado/gdb-prerun-scripts
%{_docdir}/avocado/plugins
%{_docdir}/avocado/tests
%{_docdir}/avocado/varianter_cit
%{_docdir}/avocado/varianter_pict
%{_docdir}/avocado/wrappers
%{_docdir}/avocado/yaml_to_mux


%package -n python-avocado-bash
Summary: Avocado Test Framework Bash Utilities
License: GPLv2+ and GPLv2
Requires: python-avocado-common == %{version}-%{release}

%description -n python-avocado-bash
A small set of utilities to interact with Avocado from the Bourne
Again Shell code (and possibly other similar shells).

%files -n python-avocado-bash
%license LICENSE
%dir %{_libexecdir}/avocado
%{_libexecdir}/avocado/avocado-bash-utils
%{_libexecdir}/avocado/avocado_debug
%{_libexecdir}/avocado/avocado_error
%{_libexecdir}/avocado/avocado_info
%{_libexecdir}/avocado/avocado_warn


%changelog
* Mon Aug 19 2024 Cleber Rosa <crosa@redhat.com> - 92.3-1
- Updated to 92.3
- Support building and running under Python 3.13 for F42
- Removed patch from 92.1 as its present in 92.3

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 92.1-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 92.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 92.1-6
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 92.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 92.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 92.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 92.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Cleber Rosa <crosa@redhat.com> - 92.1-1
- Updated to 92.1
- Support building and running under Python 3.12 for F39

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 92.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  9 2022 Cleber Rosa <crosa@redhat.com> - 92.0-1
- Use selftests/check.py job instead of more limited selftests/run
- Included avocado-runner-sysinfo, avocado-runner-requirement-package,
  avocado-runner-requirement-asset and avocado-runner-dry-run and
  avocado-runner-golang executables
- Removed avocado-runner-exec executable
- Removed loader_yaml and glib plugin packages

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 82.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 82.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 82.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Merlin Mathesius <mmathesi@redhat.com> - 82.0-4
- Loosen jinja2 version requirement to fix FTBFS in Rawhide

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 82.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Merlin Mathesius <mmathesi@redhat.com> - 82.0-2
- Drop obsolete packages from BuildRequires
- Generate man page directly using 'rst2man' rather than requiring 'make'
- Adjust PATH to make sure self-tests find internal modules
- Spec file cleanup following package review.

* Mon Sep 14 2020 Cleber Rosa <cleber@redhat.com> - 82.0-1
- Sync with upstream release 82.0.
- Removed python libvirt depedency as the vm runner has been removed
  upstream
- Dropped configuration files to sync with upstream which made them
  optional and doesn't ship them anymore
- Add on extra character to short commit to sync with upstream

* Sat Jun  6 2020 Cleber Rosa <cleber@redhat.com> - 80.0-1
- Sync with upstream release 80.0.
- Dropped use of custom avocado command for tests
- Do not build deprecated runners

* Tue May 12 2020 Cleber Rosa <cleber@redhat.com> - 79.0-1
- Sync with upstream release 79.0.
- Added Python's user base bin dir to the PATH environment variable
  while running tests, so that avocado-runner-* scripts can be found
- Moved comment to new lines closing the conditionals, to avoid
  errors from rpmlint and rpmbuild

* Wed Apr 15 2020 Merlin Mathesius <mmathesi@redhat.com> - 78.0-1
- Sync with upstream release 78.0.

* Tue Mar 17 2020 Merlin Mathesius <mmathesi@redhat.com> - 77.0-1
- Sync with upstream release 77.0.

* Mon Mar 09 2020 Merlin Mathesius <mmathesi@redhat.com> - 76.0-1
- Sync with upstream release 76.0.

* Mon Jan 20 2020 Merlin Mathesius <mmathesi@redhat.com> - 75.1-1
- Sync with upstream release 75.1.

* Mon Dec 23 2019 Merlin Mathesius <mmathesi@redhat.com> - 74.0-1
- Sync with upstream release 74.0.

* Wed Nov 27 2019 Merlin Mathesius <mmathesi@redhat.com> - 73.0-1
- Sync with upstream release 73.0.
- Adjustments to build for RHEL 8.

* Wed Oct 02 2019 Merlin Mathesius <mmathesi@redhat.com> - 72.0-1
- Sync with upstream release 72.0.

* Wed Aug 28 2019 Merlin Mathesius <mmathesi@redhat.com> - 71.0-1
- Sync with upstream release 71.0.

* Wed Jun 26 2019 Merlin Mathesius <mmathesi@redhat.com> - 70.0-1
- Sync with upstream release 70.0.
- Drop all Python 2 support from SPEC file.

* Wed May 22 2019 Merlin Mathesius <mmathesi@redhat.com> - 69.0-4
- pyliblzma is Python 2-only and no longer available as of F31.
- Unversioned executables should now be Python 3.

* Mon May 20 2019 Merlin Mathesius <mmathesi@redhat.com> - 69.0-3
- Drop Python 2 support from F31 and RHEL8 onward.
- Disable components dependent upon Fiber in Fedora 31 and later,
  since avocado is currently incompatible with the new Fiber API.

* Tue Mar 19 2019 Merlin Mathesius <mmathesi@redhat.com> - 69.0-2
- python2-sphinx is no longer available or needed as of F31

* Wed Feb 27 2019 Merlin Mathesius <mmathesi@redhat.com> - 69.0-1
- Sync with upstream release 69.0.

* Fri Feb 22 2019 Merlin Mathesius <mmathesi@redhat.com> - 68.0-1
- Sync with upstream release 68.0.

* Thu Jan 31 2019 Merlin Mathesius <mmathesi@redhat.com> - 67.0-1
- Sync with upstream release 67.0.
- genisoimage, libcdio, and psmisc added as build deps so iso9660 tests run.
- Replace pystache requirement with jinja2.
- glibc-all-langpacks added as build dep for F30+ so vmimage tests run.
- python2-resultsdb_api package has been removed in F30 so
  python2-avocado-plugins-resultsdb was also disabled.

* Wed Nov 21 2018 Merlin Mathesius <mmathesi@redhat.com> - 66.0-1
- Sync with upstream release 66.0.
- python2-pycdlib package has been removed in F30 as part of
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 04 2018 Merlin Mathesius <mmathesi@redhat.com> - 65.0-1
- Sync with upstream release 65.0.

* Tue Aug 28 2018 Merlin Mathesius <mmathesi@redhat.com> - 64.0-1
- Sync with upstream release 64.0.

* Thu Jul 26 2018 Merlin Mathesius <mmathesi@redhat.com> - 63.0-2
- Added missing python[2]-enum34 requirement.

* Mon Jul 23 2018 Merlin Mathesius <mmathesi@redhat.com> - 63.0-1
- Sync with upstream release 63.0. (BZ#1602175)
  Include upstream patches needed to build for Rawhide.

* Wed Jun 13 2018 Merlin Mathesius <mmathesi@redhat.com> - 62.0-1
- Sync with upstream release 62.0. (BZ#1590572)
- Correct libvirt dependency for EPEL7/RHEL7

* Thu May 17 2018 Merlin Mathesius <mmathesi@redhat.com> - 61.0-1
- Sync with upstream release 61.0.
- Packaging updates for Python 3.
- Reorganize SPEC file.

* Mon Apr  9 2018 Cleber Rosa <cleber@redhat.com> - 52.1-2
- Added Fedora CI tests

* Tue Apr 03 2018 Merlin Mathesius <mmathesi@redhat.com> - 52.1-1
- Sync with upstream release 52.1 (LTS series).
- Correct deprecated use of unversioned python.

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 52.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 52.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Merlin Mathesius <mmathesi@redhat.com> - 52.0-3
- Fix FTBFS error by disabling selfcheck producing false failures
- Update SPEC to use pkgname instead of srcname macro where appropriate

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Merlin Mathesius <mmathesi@redhat.com> - 52.0-1
- Sync with upstream release 52.0. (BZ#1465409)

* Wed Jun 14 2017 Merlin Mathesius <mmathesi@redhat.com> - 51.0-1
- Sync with upstream release 51.0. (BZ#1460837)
- Disable selftests when libvirt may not be available.

* Wed May 17 2017 Merlin Mathesius <mmathesi@redhat.com> - 50.0-1
- Sync with upstream release 50.0. (BZ#1431413)
- Be explicit about selftest level run on check.

* Tue Apr 25 2017 Merlin Mathesius <mmathesi@redhat.com> - 49.0-1
- Sync with upstream release 49.0. (BZ#1431413)

* Tue Apr 18 2017 Merlin Mathesius <mmathesi@redhat.com> - 48.0-1
- Sync with upstream release 48.0. (BZ#1431413)
- Allow rel_build macro to be defined outside of the SPEC file.

* Mon Mar 27 2017 Merlin Mathesius <mmathesi@redhat.com> - 47.0-1
- Sync with upstream release 47.0.
- Enable self-tests during build.
- Add example test to be run by Taskotron.

* Mon Feb 27 2017 Merlin Mathesius <mmathesi@redhat.com> - 46.0-2
- Incorporate upstream SPEC file changes to split plugins into subpackages.
- Remove obsolete CC-BY-SA license, which went away with the halflings font.

* Tue Feb 14 2017 Merlin Mathesius <mmathesi@redhat.com> - 46.0-1
- Sync with upstream release 46.0.
- Remove halflings license since font was removed from upstream.
- SPEC updates to easily switch between release and snapshot builds.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Merlin Mathesius <mmathesi@redhat.com> - 43.0-7
- SPEC updates to build and install for EPEL.

* Mon Nov 21 2016 Merlin Mathesius <mmathesi@redhat.com> - 43.0-6
- Initial packaging for Fedora.
