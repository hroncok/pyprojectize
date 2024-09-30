%global srcname remoto

Name:           python-%{srcname}
Version:        1.2.1
Release:        11%{?dist}
Summary:        Execute remote commands or processes

License:        MIT
URL:            https://github.com/alfredodeza/remoto

Source0:        %pypi_source

Patch0001: 0001-use-unittest.mock-on-py3.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-execnet >= 1.2.0

%global _description\
Execute remote commands or processes.

%description %_description

%package -n python3-%{srcname}
Summary:        Execute remote commands or processes
Requires:       python3
Requires:       python3-execnet >= 1.2.0

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l '*'

%check
py.test-%{python3_version} -v remoto/tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.1-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.2.1-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 03 2021 Ken Dreyer <kdreyer@redhat.com> - 1.2.1-1
- Update to 1.2.1 (rhbz#1786786)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.4-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Ken Dreyer <kdreyer@redhat.com> 1.1.4-1
- Update to 1.1.4 (rhbz#1704464)

* Wed Mar 20 2019 Ken Dreyer <kdreyer@redhat.com> 1.1.2-1
- Update to 1.1.2
- Use standard %%srcname macro
- Use %%pypi_source macro for Source0
- Switch to %%autosetup
- Drop PYTHONPATH manipulation in %%check

* Tue Feb 26 2019 Ken Dreyer <kdreyer@redhat.com> 1.1.0-1
- Update to 1.1.0 (rhbz#1683347)

* Thu Feb 21 2019 Ken Dreyer <kdreyer@redhat.com> 1.0.0-1
- Update to 1.0.0
- Use py3_build and py3_install macros

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Ken Dreyer <kdreyer@redhat.com> - 0.0.35-1
- Update to 0.0.35
- Drop python2 subpackage

* Wed Jul 18 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 0.0.33-1
- Update to 0.0.33 (rhbz#1601652)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 0.0.31-1
- Update to 0.0.31 (rhbz#1599934)
- Change obsolete python_version macro to python2_version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.30-6
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.30-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.30-3
- Python 2 binary package renamed to python2-remoto
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Ken Dreyer <ktdreyer@ktdreyer.com> 0.0.30-1
- Update to 0.0.30 (rhbz#1468070)
- Vendored library is gone upstream, no need for REMOTO_NO_VENDOR
- rm Group tag

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.29-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.29-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.29-1
- Update to remoto 0.0.29 (rhbz#1347889)

* Mon May 16 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.28-1
- Update to remoto 0.0.28 (rhbz#1335338)
- Update Source0 URL for pypi breakage (see
  https://bitbucket.org/pypa/pypi/issues/438/backwards-compatible-un-hashed-package)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.27-1
- Update to remoto 0.0.27 (rhbz#1296748)
- Use %%license macro
- Drop unneeded %%python_sitelib definition

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.25-1
- Update to remoto-0.0.25
- rm python3_version compat macro; this has been defined since F13
- Remove pre-existing .pyc files during %%prep

* Mon Jan 05 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.24-1
- Update to remoto-0.0.24
- Add Group tag
- Enable tests during %%check (RHBZ #1178930)
- Add python3 subpackage

* Fri Dec 12 2014 Ken Dreyer <kdreyer@redhat.com> - 0.0.23-1
- Update to remoto-0.0.23 (RHBZ #1146478)
- Use pypi URL for Source0 (requires LICENSE file to be shipped separately)
- Use HTTPS for homepage

* Fri Sep 12 2014 Federico Simoncelli <fsimonce@redhat.com> 0.0.21-1
- update remoto-0.0.21

* Fri Aug  1 2014 Federico Simoncelli <fsimonce@redhat.com> 0.0.19-1
- update to remoto-0.0.19

* Fri Jun 27 2014 Federico Simoncelli <fsimonce@redhat.com> 0.0.17-2
- specfile cleanups

* Sun Jun 22 2014 Federico Simoncelli <fsimonce@redhat.com> 0.0.17-1
- initial build
