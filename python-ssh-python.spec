%{?python_enable_dependency_generator}

%global modname ssh-python

Name:           python-%{modname}
Version:        1.0.0
Release:        9%{?dist}
Summary:        Bindings for libssh C library

License:        GPL-2.0-or-later
URL:            https://github.com/ParallelSSH/ssh-python
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

Patch0001:      0001-Set-master_doc-to-index-in-conf.py-for-sphinx.patch
# Upstream MR:  https://github.com/ParallelSSH/ssh-python/pull/71
Patch0002:	0002-Versioneer_patches_for_Python_3.12.patch
# Versioneer used is extremely old, force version, see above MR for suggestion
Patch0003:      0003-Fix_version_due_to_old_versioneer.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libssh-devel

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

# test dependencies
BuildRequires:  python3-pytest
BuildRequires:  %{_sbindir}/sshd %{_bindir}/ssh-agent

Recommends: python3-%{modname}-doc

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
%{summary}.

Python 3 version.


%prep
%autosetup -p1 -n %{modname}-%{version}
# No bundled libs
rm -vrf libssh
sed -i -r 's:build_ssh[(].*:pass:' setup.py
# Remove pre-generated sources
rm $(grep -rl '/\* Generated by Cython')

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
export HAVE_AGENT_FWD=0
# use build_ext to completely instruct cythonize options
export CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}"
export LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"
export CXXFLAGS="${CXXFLAGS:-${RPM_OPT_FLAGS}}"
%{python3} setup.py build_ext --inplace
%{python3} -msphinx -M html doc _build

%install
%pyproject_install
# remove 0 length files
rm -f %{buildroot}/%{python3_sitearch}/ssh/__init__.pxd
chmod 0755 %{buildroot}/%{python3_sitearch}/ssh/*.so


%check
# disable some options for sshd running inside mock
echo UsePrivilegeSeparation no >> tests/embedded_server/sshd_config.tmpl
echo StrictModes no >> tests/embedded_server/sshd_config.tmpl
# test_statvfs/test_fstatvfs do not seem to work in mock
rm -f tests/test_sftp.py
%pytest -v tests

%files -n python3-%{modname}
%license COPYING LICENSE
%doc README.rst Changelog.rst
%{python3_sitearch}/ssh_python-*.dist-info/
%{python3_sitearch}/ssh/

%package -n python3-%{modname}-doc
Summary:        %{summary} documentation

%description -n python3-%{modname}-doc
%{summary} documentation.

%files -n python3-%{modname}-doc
%doc examples/ _build/html/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.12

* Fri Apr 28 2023 Federico Pellegrin <fede@evolware.org> - 1.0.0-2
- More patches for Python 3.12 compatibility (fixes rhbz#2190204)

* Tue Apr 18 2023 Federico Pellegrin <fede@evolware.org> - 1.0.0-1
- Bump to version 1.0.0
- Local patch for Python 3.12 compatibility (fixes rhbz#2165556)
- Fix wrong version in provides (fixes rhbz#2048102)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.10.0-4
- Rebuilt for Python 3.11

* Thu Jun 16 2022 James Slagle <jslagle@redhat> - 0.10.0-1
- Update to 0.10.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 8 2021 James Slagle <jslagle@redhat.com> - 0.9.0-1
- Initial package
