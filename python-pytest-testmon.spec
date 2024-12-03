%global pypi_name pytest-testmon

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        3%{?dist}
Summary:        A py.test plug-in which executes only tests affected by recent changes
License:        MIT
URL:            http://testmon.org/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-coverage
#BuildRequires:  python3-unittest_mixins

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%package -n     python3-%{pypi_name}
Summary:        A py.test plug-in which executes only tests affected by recent changes

Requires:       python3-pytest
Requires:       python3-coverage
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

This a Python 3 version of the package.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l testmon

%check
%pyproject_check_import

# This project doesn't appear to have tests

%files -n python3-%{pypi_name}  -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.13

* Tue Mar 12 2024 Dan Radez <dradez@redhat.com> - 2.1.1-1
- update to 2.1.1 rhbz#2251208

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 07 2023 Dan Radez <dradez@redhat.com> - 2.1.0-1
- update to 2.1.0 rhbz#2247818

* Thu Nov 02 2023 Dan Radez <dradez@redhat.com> - 2.0.15-1
- update to 2.0.15 rhbz#2247251

* Mon Oct 30 2023 Dan Radez <dradez@redhat.com> - 2.0.13-1
- update to 2.0.13 rhbz#2244657

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Dan Radez <dradez@redhat.com> - 2.0.12-1
- update to 2.0.12 rhbz#2222214

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 2.0.9-2
- Rebuilt for Python 3.12

* Mon Jun 19 2023 Dan Radez <dradez@redhat.com> - 2.0.9-1
- update to 2.0.9 rhbz#2192513

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.6-2
- Rebuilt for Python 3.12

* Tue Apr 11 2023 Dan Radez <dradez@redhat.com> - 2.0.6-1
- update to 2.0.6 rhbz#2185045

* Thu Apr 06 2023 Dan Radez <dradez@redhat.com> - 2.0.5-1
- update to 2.0.5 (rhbz#2181746)

* Fri Mar 24 2023 Dan Radez <dradez@redhat.com> - 2.0.0-1
- update to 2.0 (rhbz#2162765)

* Wed Jan 18 2023 Dan Radez <dradez@redhat.com> - 1.4.4-1
- update to 1.4.5 (rhbz#2155546)

* Sat Dec 31 2022 Tom Callaway <spot@fedoraproject.org> - 1.4.2-2
- allow use of coverage v7 (upstream already has this change in git) (#2157154)

* Wed Nov 23 2022 Dan Radez <dradez@redhat.com> - 1.4.2-1
- update to 1.4.2 (rhbz#2143715)

* Tue Nov 01 2022 Dan Radez <dradez@redhat.com> - 1.4.1-1
- update to 1.4.1 (rhbz#2127148)

* Mon Sep 12 2022 Dan Radez <dradez@redhat.com> - 1.3.6-1
- updating to 1.3.6

* Sun Aug 28 2022 Dan Radez <dradez@redhat.com> - 1.3.5-1
- updating to 1.3.5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Dan Radez <dradez@redhat.com> - 1.3.4-1
- updating to 1.3.4

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Dan Radez <dradez@redhat.com> - 1.3.1-1
- updating to 1.3.1

* Tue Mar 01 2022 Dan Radez <dradez@redhat.com> - 1.3.0-1
- updating to 1.3.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Dan Radez <dradez@redhat.com> - 1.2.2-1
- updating to 1.2.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.10

* Fri Apr 30 2021 Dan Radez <dradez@redhat.com> - 1.1.1-1
- updating to 1.1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Dan Radez <dradez@redhat.com> - 1.0.3-1
- updating to 1.0.3

* Thu Jul 30 2020 Dan Radez <dradez@redhat.com> - 1.0.2-1
- Updating to 1.0.2
- Had to disable tests for now, missing coverage mixins rpm for tests

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.19-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Dan Radez <dradez@redhat.com> - 0.9.19-9
- Updating to 0.9.19
- remove fix-py38-compat.patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 02 2019 Charalampos Stratakis <cstratak@redhat.com> - 0.9.16-4
- Fix Python 3.8 compatibility

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Dan Radez <dradz@redhat.com> - 0.9.16-1
- updating to 0.9.16
- removing < 4 pytest req

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.13-1
- Update to 0.9.13
- Remove the python2 package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.9.6-1
- update to 0.9.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-1
- Update
- Rebuild for Python 3.6

* Sat Oct 01 2016 Julien Enselme <jujens@jujens.eu> - 0.8.2-3
- Add patch for pytest3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 13 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-1
- New upstream release (removes the need for old patch)
- Be consistent with Requires and BRs
- Add coverage_pth to Requires
- Run tests and BR on dependencies
- Use GitHub archive to get tests
- export PYTHONPATH before running tests
- Add LICENSE file to %%license

* Fri Mar 11 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-1
- Initial package
