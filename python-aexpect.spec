# Conditional for release vs. snapshot builds. Set to 1 for release build.
%if ! 0%{?rel_build:1}
    %global rel_build 1
%endif

# Settings used for build from snapshots.
%if 0%{?rel_build}
    %global gittar              aexpect-%{version}.tar.gz
%else
    %if ! 0%{?commit:1}
        %global commit          a542688c95dd3d5a55def634f998e9ac635d8304
    %endif
    %if ! 0%{?commit_date:1}
        %global commit_date     20210602
    %endif
    %global shortcommit         %(c=%{commit};echo ${c:0:8})
    %global gitrel              .%{commit_date}git%{shortcommit}
    %global gittar              aexpect-%{shortcommit}.tar.gz
%endif

# Selftests are provided but skipped because they use unsupported tooling.
%global with_tests 0

Name: python-aexpect
Version: 1.6.2
Release: 13%{?gitrel}%{?dist}
Summary: A python library to control interactive applications

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/avocado-framework/aexpect

%if 0%{?rel_build}
Source0: %{url}/archive/%{version}/%{gittar}
%else
Source0: %{url}/archive/%{commit}/%{gittar}
%endif

BuildArch: noarch
BuildRequires: python3-devel

%description
Aexpect is a python library used to control interactive applications, very
similar to pexpect. You can use it to control applications such as ssh, scp
sftp, telnet, among others.

%package -n python%{python3_pkgversion}-aexpect
Summary: %{summary}

%description -n python%{python3_pkgversion}-aexpect
Aexpect is a python library used to control interactive applications, very
similar to pexpect. You can use it to control applications such as ssh, scp
sftp, telnet, among others.

%prep
%if 0%{?rel_build}
%autosetup -n aexpect-%{version} -p 1
%else
%autosetup -n aexpect-%{commit} -p 1
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l aexpect
ln -s aexpect_helper %{buildroot}%{_bindir}/aexpect_helper-%{python3_pkgversion}
ln -s aexpect_helper %{buildroot}%{_bindir}/aexpect_helper-%{python3_version}

%if %{with_tests}
%check
%pyproject_check_import

selftests/checkall
%endif

%files -n python%{python3_pkgversion}-aexpect -f %{pyproject_files}
%doc README.rst
%{_bindir}/aexpect_helper*

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.2-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.2-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.2-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Cleber Rosa <cleber@redhat.com> - 1.6.2-1
- Sync with upstream release 1.6.2.
- Removed patch to fix rpmlint error, now included upstream.

* Thu Mar 18 2021 Merlin Mathesius <mmathesi@redhat.com> - 1.6.1-2
- Spec file cleanup following package review.
- Include upstream patch to fix rpmlint error.

* Mon Feb 15 2021 Cleber Rosa <cleber@redhat.com> - 1.6.1-1
- Sync with upstream release 1.6.1.
- Dropped Python2 support completely

* Tue Nov 26 2019 Merlin Mathesius <mmathesi@redhat.com> - 1.5.1-6
- Drop Python 2 support from RHEL8 onward.

* Tue May 14 2019 Merlin Mathesius <mmathesi@redhat.com> - 1.5.1-5
- Drop Python 2 support from F31 onward.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Merlin Mathesius <mmathesi@redhat.com> - 1.5.1-1
- Sync with upstream release 1.5.1 (BZ#1588660).
- Now with full python3 support (BZ#1437184).

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.4.0-1
- Sync with upstream release 1.4.0 (BZ#1438782).
- Update source location to refer to new home.
- Provide python2 version-specific executables.

* Mon Feb 20 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.3.1-1
- Sync with upstream release 1.3.1 (BZ#1425027).

* Tue Feb 14 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.3.0-1
- Sync with upstream release 1.3.0.
- SPEC updates to easily switch between release and snapshot builds.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6.20161110gitaca459d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.2.0-5
- SPEC updates to build and install for EPEL.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4.20161110gitaca459d
- Rebuild for Python 3.6

* Thu Nov 10 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.2.0-3
- Initial packaging for Fedora.
