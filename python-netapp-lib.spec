# what it's called on pypi
%global srcname netapp-lib
# what it's imported as
%global libname netapp_lib
# name of egg info directory
%global eggname %{libname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Library to allow Ansible deployments to interact with NetApp storage systems}

Name:           python-%{srcname}
Version:        2021.6.25
Release:        12%{?dist}
Summary:        NetApp library for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.org/project/netapp-lib/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description %{common_description}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}



%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{libname}

# Note that there is no %%files section for the unversioned python module
%check
%pyproject_check_import
%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst
%exclude /usr/LICENSE.txt


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2021.6.25-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2021.6.25-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2021.6.25-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2021.6.25-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Sam P <survient@fedoraproject.org> - 2021.06.25-1
- Updated to latest upstream release.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.7.16-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.7.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Sam P <survient@fedoraproject.org> - 2020.7.16-1
- Updated to upstream latest release
- Included reference to license file

* Wed Jul 15 2020 Sam P <survient@fedoraproject.org> - 2020.3.13-1
- Updated to latest release
- Updated to reflect license change

* Wed Apr 01 2020 Sam P <survient@fedoraproject.org> - 2020.3.12-1
- Updated to latest release

* Fri Feb 21 2020 Sam P <survient@fedoraproject.org> - 2019.12.20-2
- Simplified spec file

* Fri Feb 21 2020 Sam P <survient@fedoraproject.org> - 2019.12.20-1
- Initial Commit

