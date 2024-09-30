%if 0%{?fedora}
# If the definition isn't available for python3_pkgversion, define it
%{?!python3_pkgversion:%global python3_pkgversion 3}
%bcond_without  python3
%else
%bcond_with     python3
%endif

%global plugin_install_path %{_datadir}/pdc-client/plugins

# Disable automatic byte-compilation of plugins
%global _python_bytecompile_extra 0

Name:           pdc-client
Version:        1.8.0
Release:        35%{?dist}
Summary:        Console client for interacting with Product Definition Center
License:        MIT
URL:            https://github.com/product-definition-center/pdc-client
BuildArch:      noarch

Source0:        https://files.pythonhosted.org/packages/source/p/pdc-client/pdc-client-%{version}.tar.gz


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python3-requests-kerberos
BuildRequires:  python3-beanbag
BuildRequires:  python3-zombie-imp

Requires:  python%{python3_pkgversion}-pdc-client = %{version}-%{release}

%description
This client package contains two separate Product Definition Center clients and
API module. Both clients contain extensive built-in help. Just run the
executable with -h or --help argument.

1. pdc_client

This is a very simple client. Essentially this is just a little more convenient
than using curl manually. Each invocation of this client obtains a token and
then performs a single request.

This client is not meant for direct usage, but just as a helper for integrating
with PDC from languages where it might be easier than performing the network
requests manually.

2. pdc

This is much more user friendly user interface. A single invocation can perform
multiple requests depending on what subcommand you used.

The pdc client supports Bash completion if argcomplete Python package is
installed.

3. Python API (pdc_client)

When writing a client code interfacing with PDC server, you might find
pdc_client module handy. It provides access to the configuration defined above
and automates obtaining authorization token.

%package -n python%{python3_pkgversion}-pdc-client
Summary:    Python 3 client library for Product Definition Center

Requires:  python3-beanbag
Requires:  python3-requests-kerberos
Requires:  pdc-client

%description -n python%{python3_pkgversion}-pdc-client
This is a python module for interacting with Product Definition Center
programatically. It can handle common authentication and configuration of PDC
server connections

%prep
%setup -q -n pdc-client-%{version}

# Replace installation plugin path in code
sed -i 's|^DEFAULT_PLUGIN_DIR = .*|DEFAULT_PLUGIN_DIR = "%{plugin_install_path}"|' \
        pdc_client/runner.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
# Override plugin directory for tests.
export PDC_CLIENT_PLUGIN_PATH="%{buildroot}%{plugin_install_path}"
test -d "$PDC_CLIENT_PLUGIN_PATH"

# Smoke-test executables.
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
for executable in "%{buildroot}%{_bindir}"/*; do
    "$executable" --version
    "$executable" --help
done

%install
%pyproject_install
%pyproject_save_files 'pdc_client*'

# Plugins are only required in the "pdc" script (not the Python packages). So
# move plugins to pdc-client package from Python package (this should also
# contain compiled bytecode).
mkdir -p %{buildroot}/%{plugin_install_path}
mv -T %{buildroot}/%{python3_sitelib}/pdc_client/plugins %{buildroot}/%{plugin_install_path}

mkdir -p %{buildroot}/%{_mandir}/man1
cp docs/pdc_client.1 %{buildroot}/%{_mandir}/man1/

mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d/
cp pdc.bash %{buildroot}/%{_sysconfdir}/bash_completion.d/

mkdir -p %{buildroot}/%{_sysconfdir}/pdc.d
cat > %{buildroot}/%{_sysconfdir}/pdc.d/fedora.json << EOF
{
    "fedora": {
        "host": "https://pdc.fedoraproject.org/rest_api/v1/",
        "develop": false,
        "ssl-verify": true
    }
}
EOF

%files
%doc README.markdown
%{_mandir}/man1/pdc_client.1*
%{_sysconfdir}/bash_completion.d
%dir %{_sysconfdir}/pdc.d
%config(noreplace) %{_sysconfdir}/pdc.d/fedora.json
%{_bindir}/pdc
%{_bindir}/pdc_client
%dir %{_datadir}/pdc-client
%dir %{plugin_install_path}
%{plugin_install_path}/*

%files -n python%{python3_pkgversion}-pdc-client -f %{pyproject_files}
%doc README.markdown
%license LICENSE


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.8.0-34
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Maxwell G <maxwell@gtmx.me> - 1.8.0-31
- Remove unused python3-mock dependency

* Thu Jul 27 2023 Kevin Fenzi <kevin@scrye.com> - 1.8.0-30
- Add python3-zombie-imp to BuildRequires to bandaid ftbfs until it can be fixed.
- Fixes rhbz#2220064

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.8.0-28
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.8.0-25
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.8.0-22
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-19
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Lubomír Sedlář <lsedlar@redhat.com> - 1.8.0-17
- Bump release to be the same as 31

* Fri Oct 25 2019 Lubomír Sedlář <lsedlar@redhat.com> - 1.8.0-16
- Require pdc-client from python subpackage

* Mon Sep 02 2019 Lubomír Sedlář <lsedlar@redhat.com> - 1.8.0-15
- Remove python2 subpackage

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Lubomír Sedlář <lsedlar@redhat.com> - 1.8.0-11
- Use python2_sitelib instead of python_sitelib

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-9
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Lubomír Sedlář <lsedlar@redhat.com> - 1.8.0-8
- Disable automatic python bytecompilation

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-7
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.8.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Chuang Cao <chcao@redhat.com> 1.8.0-4
- Add the page_size=None when get auth (chcao@redhat.com)

* Wed Nov 29 2017 Chuang Cao <chcao@redhat.com> 1.8.0-3
- Rollback codes on parent class of PDCClient (chcao@redhat.com)

* Fri Nov 24 2017 Chuang Cao <chcao@redhat.com> 1.8.0-2
- Add new version 1.8.0 in setup.py (chcao@redhat.com)
- Remove "setup.py test" part from sepc file (chcao@redhat.com)

* Wed Nov 22 2017 Chuang Cao <chcao@redhat.com> 1.8.0-1
- Add PDCClient tests and fix the discovered bugs (lholecek@redhat.com)
- Add comments for rpm requirements (chcao@redhat.com)
- Get the endpoint as attr which includes "-" (chcao@redhat.com)
- Fix wrapping BeanBag methods and operators (lholecek@redhat.com)
- Fix bug of Multipaged (chcao@redhat.com)
- Add MultiPageBeanBag class to support get multi pages (chcao@redhat.com)
- Add the close function when load plugins (chcao@redhat.com)
- Correct the flake8 issues (chcao@redhat.com)
- Change the docstrings and fix issues (chcao@redhat.com)
- Remove duplicate code (lholecek@redhat.com)
- Update documentation (lholecek@redhat.com)
- Add documentation link to README file (lholecek@redhat.com)
- Add discription of page_size=-1 in help doc (chcao@redhat.com)
- Fix printing errors and exit code for pdc_client (lholecek@redhat.com)
- Add smoke-test for all executables (lholecek@redhat.com)
- Fix running tests when building rpm (lholecek@redhat.com)
- Override plugin paths with PDC_CLIENT_PLUGIN_PATH (lholecek@redhat.com)
- Improve installing plugins (lholecek@redhat.com)
- Revert removing comments from downstream (lholecek@redhat.com)
- Add the page argument on pdc (chcao@redhat.com)

* Fri Sep 08 2017 Lukas Holecek <lholecek@redhat.com> 1.7.0-3
- Fix printing help for missing sub-commands (lholecek@redhat.com)
- Fix "pdc_client --version" (lholecek@redhat.com)

* Mon Aug 28 2017 Lukas Holecek <lholecek@redhat.com> 1.7.0-2
- Omit installing plugins with Python packages

* Tue Aug 22 2017 Lukas Holecek <lholecek@redhat.com> 1.7.0-1
- Bump versin in setup.py (lholecek@redhat.com)
- Update spec file from downstream (lholecek@redhat.com)
- Bug fix for ssl_verify in old pdc_client (chuzhang@redhat.com)
- Fix content-delivery-repo list ordering (lholecek@redhat.com)
- Print table with minimum width for content-deliver-repo list
  (lholecek@redhat.com)
- Update test data for content-deliver-repo (lholecek@redhat.com)
- Update value type for "Shadow" field (lholecek@redhat.com)
- Increase `pdc content-deliver-repo list` verbosity. (dmach@redhat.com)
- Fix passing ordering parameter (lholecek@redhat.com)
- Make error reporting less verbose (lholecek@redhat.com)
- Omit printing long HTML with error (lholecek@redhat.com)
- Remove unused import (lholecek@redhat.com)
- Simplify reporting server errors. (dmach@redhat.com)
- Modify base_product plugin according to commit 79cbe98 (chuzhang@redhat.com)
- Sort commands in pdc --help. (dmach@redhat.com)
- Remove the arch parameter from option (chcao@redhat.com)
- Use local development plugin directory (lholecek@redhat.com)
- Add content-delivery-repo export/import sub-commands. (dmach@redhat.com)
- Unify json output serialization. (dmach@redhat.com)
- Add base-product command (chcao@redhat.com)
- Add base-product command. (dmach@redhat.com)
- Allow deleting multiple repos at once. (dmach@redhat.com)
- Allow deleting multiple group resource perms at once. (dmach@redhat.com)
- Fix running tests with Travis (lholecek@redhat.com)
- Replace a custom test runner with standard setup.py test. (dmach@redhat.com)
- Allow deleting release variants. (dmach@redhat.com)
- Add "release-variant" command (chcao@redhat.com)
- Add "release-variant" command. (dmach@redhat.com)
- OrderedDict support in python 2.6 (chcao@redhat.com)
- Add "product-version" command. (dmach@redhat.com)
- OrderedDict support in python 2.6 (chcao@redhat.com)
- Add "product" command. (dmach@redhat.com)
- plugin_helpers: Allow overriding 'dest' option. (dmach@redhat.com)
- Fix reading "develop" option from settings (lholecek@redhat.com)
- Fix configuration name in README (lholecek@redhat.com)
- Fix the Sphix dependency (caochuangxiang@gmail.com)
- Change the new token secure with chcao (caochuangxiang@gmail.com)
- Feedback: incorrect place to specify default SSL behavior (ahills@redhat.com)
- Fix SSL command line options (ahills@redhat.com)
- Surport SSL cert when swith insecure to false (bliu@redhat.com)
- Fix the bug about the include-shadow para in repo clone (bliu@redhat.com)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Lubomír Sedlář <lsedlar@redhat.com> - 1.2.0-3
- Fix dependencies on Python 3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 bliu <bliu@redhat.com> 1.2.0-1
- Fix the porblem in repo clone (ycheng@redhat.com)
- Add the SSL and remove the Warning Info (bliu@redhat.com)
- Add RPC "clone" command to content-delivery-repo (ahills@redhat.com)
- Bug about ssl verify (bliu@redhat.com)
- Add a new plugin of group-resource-permission (bliu@redhat.com)
- Support option --server as well. (chuzhang@redhat.com)
- Add insecure configuration option back with a warning (ahills@redhat.com)
- Fix PEP8 violation (ahills@redhat.com)
- More flexible SSL certificate verification configuration (ahills@redhat.com)
- Create a new plugin of compose-full-import (bliu@redhat.com)
- Update the SPEC file (bliu@redhat.com)
- Update the README.markdown file in pdc-client repo (bliu@redhat.com)
- Merge plugins in config file with default plugins. (chuzhang@redhat.com)
- fix TypeError: unorderable types: NoneType() <= int() (jpopelka@redhat.com)
- [spec] Python3 build (jpopelka@redhat.com)
- update the requirements file with flake<=3.0.3 (bliu@redhat.com)
- Update the SPEC file for removing the directories. (bliu@redhat.com)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuild for Python 3.6

* Fri Aug 12 2016 Jiri Popelka <jpopelka@redhat.com> - 1.1.0-2
- Python3 build

* Sun Aug 07 2016 bliu <bliu@redhat.com> 1.1.0-1
- When page_size <= 0; the pagination will be disabled. (bliu@redhat.com)
- Handle page_size in mocked API calls. (nils@redhat.com)
- Move necessary arguments to required argument list. (ycheng@redhat.com)
- Make format strings compatible with python 2.6 (chuzhang@redhat.com)
- Fix failure with requests-kerberos 0.9+ and Python 3 (drop monkey_patch.py)
  (mzibrick@redhat.com)
- Add FILES section and fix issue link in manpage (sochotnicky@redhat.com)

* Sun Jul 17 2016 bliu <bliu@redhat.com> 1.0.0-2
- Move plugins outside of python_sitelib. (bliu@redhat.com)
- Allow specifying plugins in the config file. (chuzhang@redhat.com)
- Change configuration files for pdc-client. (bliu@redhat.com)
- Add field 'subvariant' to image sub-command. (ycheng@redhat.com)

* Thu May 05 2016 bliu <bliu@redhat.com> 0.9.0-3
- Change filtering arguments's underscore to minus to be consistent.
  (ycheng@redhat.com)
- Modify compose-tree-locations in client because API url changed.
  (ycheng@redhat.com)
- Add support for repo manipulation into pdc client (ycheng@redhat.com)

* Fri Feb 26 2016 bliu <bliu@redhat.com> 0.9.0-1
- Add headers in result for pdc client output. (ycheng@redhat.com)
- Add pdc client project page and PyPI release docomentation.
  (ycheng@redhat.com)
- Update the error info (bliu@redhat.com)
- Update the more detail info (bliu@redhat.com)
- Add error info when input irregular or illegal para (bliu@redhat.com)
- Let pdc client handle pdc warning header (ycheng@redhat.com)
- Pypi setup (sochotnicky@redhat.com)
- Fix release component update logging type (sochotnicky@redhat.com)

* Wed Jan 13 2016 bliu <bliu@redhat.com> 0.2.0-3
- PATCH on build-image-rtt-tests with build_nvr/format (bliu@redhat.com)
- Add beanbag required version. (xchu@redhat.com)
- Add header for build image in new pdc client output (ycheng@redhat.com)
- Add tests for permission list. (xchu@redhat.com)
- Add test for build-image detail. (xchu@redhat.com)
- Add support for compose-tree-locations. (chuzhang@redhat.com)
- Add head in result when running build_image_rtt_tests (bliu@redhat.com)
- Use new get_paged method instead of deprecated one. (ycheng@redhat.com)
- Pdc client add support for build-image-rtt-tests (bliu@redhat.com)
- Add support for compose-image-rtt-tests in pdc client (ycheng@redhat.com)
- Make mocked endpoints possibly callable. (rbean@redhat.com)
- Add help message for 'active' filter. (xchu@redhat.com)
- Enable page_size in new pdc client (bliu@redhat.com)

* Wed Jan 13 2016 bliu <bliu@redhat.com> 0.2.0-2

* Fri Dec 04 2015 Xiangyang Chu <xchu@redhat.com> 0.2.0-1
- Add python 2.6 check. (xchu@redhat.com)
- Fix spec URL (rbean@redhat.com)
- Allow PDCClient to be configured with arguments. (rbean@redhat.com)
- Imporvements on new `pdc` client.
* Fri Sep 11 2015 Xiangyang Chu <xychu2008@gmail.com> 0.1.0-1
- new package built with tito
