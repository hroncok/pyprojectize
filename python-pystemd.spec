# Enable Python dependency generation

%global pypi_name pystemd

Name:           python-%{pypi_name}
Version:        0.13.2
Release:        10%{?dist}
Summary:        A thin Cython-based wrapper on top of libsystemd

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/pystemd
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch0:         %{url}/pull/87.patch#/pystemd-fix_deprecation_warning.diff

BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(psutil)

%description
This library allows you to talk to systemd over D-Bus from Python,
without actually thinking that you are talking to systemd over D-Bus.

This allows you to programmatically start/stop/restart/kill and verify
service status from systemd point of view, avoiding subprocessing systemctl
and then parsing the output to know the result.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This library allows you to talk to systemd over D-Bus from Python,
without actually thinking that you are talking to systemd over D-Bus.

This allows you to programmatically start/stop/restart/kill and verify
service status from systemd point of view, avoiding subprocessing systemctl
and then parsing the output to know the result.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
# remove installed source files if present
# seems to vary based on dependency versions (EPEL 9 does not install these)
rm -f %{buildroot}%{python3_sitearch}/%{pypi_name}/*.c

%check
%pyproject_check_import

# This test fails in mock because systemd isn't running
rm -f tests/test_daemon.py
%if 0%{?el8}
# This test doesn't work with Python 3.6
rm -f tests/test_futures.py
%endif

export PYTHONPATH=%{buildroot}%{python3_sitearch}
pushd tests
%{__python3} -m unittest discover
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.13.2-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.13.2-5
- Fix deprecation warning and EL builds

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.13.2-4
- Rebuilt for Python 3.12

* Mon Jul 03 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.13.2-3
- Fix rpmlint warnings: remove shipped *.c sources

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.13.2-2
- Rebuilt for Python 3.12

* Fri Jun 30 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.13.2-1
- Update to 0.13.2; Fixes: rhbz#2210519

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.13.1-2
- Rebuilt for Python 3.12

* Wed May 17 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1; Fixes: RHBZ#2207826
- Drop some unnecessary logic from the spec

* Mon May 01 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Fri Feb 10 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 0.11.0-4
- Gate out unsupported test on el8

* Fri Feb 10 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 0.11.0-3
- Add psutil to BuildRequires for test_futures
- Update project URL

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0 (#2151054)
- Convert license tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.0-5
- Rebuilt for Python 3.11

* Mon Apr 11 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-4
- Drop unnecessary BuildRequires for deprecated package

* Thu Apr 07 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-3
- Add new upstream dependency to BuildRequires

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 20 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0
- Ensure we always rebuild the Cython bindings (Resolves: rhbz#1900529)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 16:08:15 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 0.8.0-1
- Update to 0.8.0 (#1891609)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 19:09:25 EDT 2019 Neal Gompa <ngompa13@gmail.com> - 0.6.0-1
- Initial packaging
