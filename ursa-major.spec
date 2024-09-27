%if 0%{?fedora} || 0%{?rhel} > 7
# we have some koji hubs doesn't support Python3 with kerberos auth
# at this moment, so we build with Python2 for all platforms now
%global with_python3 1
%endif

Name:       ursa-major
Version:    0.4.2
Release:    12%{?dist}
Summary:    A utility for working with module's koji tags in koji's tag inheritance.

Group:      Development/Tools
License:    MIT
URL:        https://pagure.io/ursa-major
Source0:    https://files.pythonhosted.org/packages/source/u/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
# libmodulemd is not available for ppc or i686
ExclusiveArch:  noarch aarch64 ppc64le s390x x86_64


BuildRequires:  help2man

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-gobject-base
BuildRequires:  python3-cairo
BuildRequires:  python3-koji
BuildRequires:  python3-six
BuildRequires:  python3-requests
BuildRequires:  python3-jinja2
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
%else
BuildRequires:  python2-devel
BuildRequires:  python2-koji
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
BuildRequires:  python-gobject-base
BuildRequires:  pycairo
BuildRequires:  python-six
BuildRequires:  python-requests
BuildRequires:  python-jinja2
BuildRequires:  python-futures
BuildRequires:  pytest
BuildRequires:  python-mock
%else
BuildRequires:  python2-setuptools
BuildRequires:  python2-gobject-base
BuildRequires:  python2-cairo
BuildRequires:  python2-six
BuildRequires:  python2-requests
BuildRequires:  python2-jinja2
BuildRequires:  python2-futures
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
%endif
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  libmodulemd > 1
Requires:  libmodulemd > 1
%else
BuildRequires:  libmodulemd2
Requires:  libmodulemd2
%endif

Requires:       gobject-introspection
Requires:       krb5-workstation
Requires:       koji

%if 0%{?with_python3}
Requires:       python3-gobject-base
Requires:       python3-cairo
Requires:       python3-koji
Requires:       python3-m2crypto
Requires:       python3-six
Requires:       python3-requests
Requires:       python3-jinja2
Requires:       python3-setuptools
%else
Requires:       python2-koji
Requires:       m2crypto
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       python-gobject-base
Requires:       pycairo
Requires:       python-six
Requires:       python-requests
Requires:       python-jinja2
Requires:       python-futures
Requires:       python-setuptools
%else
Requires:       python2-gobject-base
Requires:       python2-cairo
Requires:       python2-six
Requires:       python2-requests
Requires:       python2-jinja2
Requires:       python2-futures
Requires:       python2-setuptools
%endif
%endif

# Need brewkoji.conf
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       brewkoji
%else
Recommends:     brewkoji
%endif


%description
Usra-Major can be used to edit a tag config file and update module's koji tags
in koji's tag inheritance accordingly per the configuration in tag config file.


%package        -n ursa-major-stage
Summary:        A utility for working with module's koji tags in koji's tag inheritance.
Requires:       %{name} = %{version}-%{release}

# Need brewkoji-stage.conf
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       brewkoji-stage
%else
Recommends:     brewkoji-stage
%endif

%description    -n ursa-major-stage
The ursa-major-stage package contains script and configurations for Ursa-Major
to talk with Fedora's stage instances (Koji, MBS).


%prep
%setup -q

%if 0%{?rhel} && 0%{?rhel} <= 7
# old setuptools not support environment marker
sed -i 's/futures.*/futures/' requirements.txt
%endif

# workaround for no egg-info
sed -i '/koji/d' requirements.txt

%build
%if 0%{?with_python3}
%py3_build
%else
%py2_build
%endif


%install
%if 0%{?with_python3}
%py3_install
%else
%py2_install
%endif

%if 0%{?with_python3}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%else
export PYTHONPATH=%{buildroot}%{python2_sitelib}
%endif
mkdir -p %{buildroot}/%{_mandir}/man1

help2man -N --no-discard-stderr --version-string=%{version} %{buildroot}/%{_bindir}/ursa-major > %{buildroot}/%{_mandir}/man1/ursa-major.1
for cmd in show-config check-config remove-module add-module add-tag; do
    help2man -N --no-discard-stderr --version-string=%{version} "%{buildroot}/%{_bindir}/ursa-major $cmd" > %{buildroot}/%{_mandir}/man1/ursa-major-${cmd}.1
done

%check
# disable unittest due to missing libmodulemd v1 in buildroot
%if 0%{?with_python3}
py.test-3
%else
py.test
%endif


%files
%doc README.rst
%license LICENSE

%if 0%{?with_python3}
%{python3_sitelib}/ursa_major*
%else
%{python2_sitelib}/ursa_major*
%endif

%{_bindir}/ursa-major
%dir %{_sysconfdir}/ursa-major
%config(noreplace) %{_sysconfdir}/ursa-major/ursa-major.conf
%doc %{_mandir}/man1/ursa-major*.1*

%files stage
%{_bindir}/ursa-major-stage
%config(noreplace) %{_sysconfdir}/ursa-major/ursa-major-stage.conf


%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.2-11
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.4.2-8
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.10

* Thu Mar 11 2021 Yu Ming Zhu <yzhu@redhat.com> - 0.4.2-1
- Use old tuple syntax for mock.call.call_args of old mock release (Yuming Zhu)
- Fix unittests for missing koji profile (Yuming Zhu)
- Using libmodulemd v2 API (Yuming Zhu)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Yu Ming Zhu <yzhu@redhat.com> - 0.4.1-3
- Requires python3-m2crypto for python3
- Recommends brew[-stage] instead of Requires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Qixiang Wan <qwan@redhat.com> - 0.4.1-1
- Remove updating koji inheritance ability from add-module and remove-module

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-4
- Require correct version of m2crypto

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Qixiang Wan <qwan@redhat.com> - 0.3.1-1
- Not check requires/buildrequires for existing koji tags (Qixiang Wan)
- Updating existing inheritance instead of removing and adding (Qixiang Wan)

* Mon Apr 15 2019 Chenxiong Qi <cqi@redhat.com> - 0.2.2-3
- Build Python 3 package for Fedora and Python 2 for EL

* Fri Apr 12 2019 Chenxiong Qi <cqi@redhat.com> - 0.2.2-2
- Add missing python-setuptools in requires

* Wed Mar 27 2019 Chenxiong Qi <cqi@redhat.com> - 0.2.2-1
- For adding tag, allow filtering on buildrequires to find out koji_tags from tag inheritance (Chenxiong Qi)

* Wed Mar 20 2019 Chenxiong Qi <cqi@redhat.com> - 0.2.1-1
- Make setup_method/teardown_method compatible with newer version of pytest (Chenxiong Qi)
- Add missing file CHANGELOG.rst to sdist package (Chenxiong Qi)

* Wed Mar 20 2019 Chenxiong Qi <cqi@redhat.com> - 0.2.0-1
- Add tests for AddModuleHandler methods (Chenxiong Qi)
- Avoid long modulemd embedded into fake data for tests (Chenxiong Qi)
- Fixes according to review comments (Chenxiong Qi)
- Command check-config supports filtering modules on buildrequires (Chenxiong Qi)
- Command add-module supports buildrequires now (Chenxiong Qi)
- Command remove-module supports filtering modules on buildrequires (Chenxiong Qi)
- Allow passing buildrequires to MBS.get_modules_with_requires (Chenxiong Qi)
- Reword remove-module help and --tag option help text (Chenxiong Qi)
- Allow filtering on buildrequires (Chenxiong Qi)

* Mon Dec 03 2018 Qixiang Wan <qwan@redhat.com> - 0.1.1-4
- build can be scheduled to i386 arch, include ix86

* Mon Dec 03 2018 Qixiang Wan <qwan@redhat.com> - 0.1.1-3
- libmodulemd is missing from EPEL ppc64le buildroot, enable x86_64 only

* Fri Nov 16 2018 Qixiang Wan <qwan@redhat.com> - 0.1.1-2
- Limit build arches as libmodulemd is not available for ppc or i686

* Fri Oct 26 2018 Qixiang Wan <qwan@redhat.com> - 0.1.1-1
- Initial version of spec file
