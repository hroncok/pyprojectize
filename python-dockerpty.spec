# what it's called on pypi
%global srcname dockerpty
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%if 0%{?fedora} >= 30
%bcond_with python2
%else
%bcond_without python2
%endif
%bcond_without python3

Name:           python-%{pkgname}
Version:        0.4.1
Release:        34%{?dist}
Summary:        Python library to use the pseudo-tty of a docker container
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/d11wtq/dockerpty
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Provides the functionality needed to operate the pseudo-tty (PTY) allocated to\
a docker container, using the Python client

%description    %{_description}

%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-six

%description -n python2-%{pkgname} %{_description}
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}
%endif

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{?with_python2:%py2_build}
%{?with_python3:%pyproject_wheel}

%install
%{?with_python2:%py2_install}
%{?with_python3:%pyproject_install}
%pyproject_save_files %{libname}

# we are missing the 'expects' library to run the tests
# %%check
# LANG=en_US.utf8 py.test-%%{python3_version} -vv tests
# LANG=en_US.utf8 py.test-%%{python2_version} -vv tests

%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE.txt
%doc README.md MANIFEST.in
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md MANIFEST.in
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.1-34
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.1-32
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.1-28
- Rebuilt for Python 3.12

* Fri Apr 21 2023 Tomas Tomecek <ttomecek@redhat.com> - 0.4.1-27
- Rebuilt after unretirement

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.1-25
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.1-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-19
- Rebuilt for Python 3.9

* Thu Mar  5 2020 Michael Hampton <error@ioerror.us> - 0.4.1-18
- Rebuilt for unretired package

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Carl George <carl@george.computer> - 0.4.1-13
- Disable python2 subpackage on F30+ rhbz#1634971

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Carl George <carl@george.computer> - 0.4.1-9
- EPEL compatibility, including Python 3 build
- Mark license appropriately
- Use tarball from git tag

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-8
- Python 2 binary package renamed to python2-dockerpty
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.4.1-6
- don't depend on docker-py when not importing it (#1425461)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 08 2016 Tomas Tomecek <ttomecek@redhat.com> - 0.4.1-2
- fix dependencies for py 3 (rhbz#1287729)

* Tue Mar 08 2016 Tomas Tomecek <ttomecek@redhat.com> - 0.4.1-1
- new upstream release: 0.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 10 2015 Roman Mohr <roman@fenkhuber.at> - 0.3.4-1
- Update to 0.3.4 (#1253859)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jul 22 2015 Roman Mohr <roman@fenkhuber.at> - 0.3.3-3
- Do not run unit tests until python-expects is packaged

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Roman Mohr <roman@fenkhuber.at> - 0.3.3-1
- Python3 compatible version (rhbz#1172357)

* Sun Nov 30 2014 Roman Mohr <roman@fenkhuber.at> - 0.3.2-1
- Update to latest upstream
- Enable unit tests

* Fri Aug 22 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.3-1
- Update to latest upstream

* Mon Aug 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.1-4
- Fixed egg-info dir listings, set noarch based on reviewer feedback

* Mon Aug 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.1-3
- Fixed files section, fixed py3 summary listing

* Fri Aug 08 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.1-2
- Fix __python vs __python2 macro usage and  __python3's description
- Set ExclusiveArch because of docker
- Remove clean section, not needed

* Wed Jul 23 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.1-1
- Initial package for Fedora
