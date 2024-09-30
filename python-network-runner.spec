# Created by pyp2rpm-3.2.2
%global pypi_name network-runner
%global ansible_role network-runner

Name:           python-%{pypi_name}
Version:        0.3.6
Release:        16%{?dist}
Summary:        Abstraction and Python API for Ansible Networking

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/ansible-network/%{pypi_name}
Source0:        https://github.com/ansible-network/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: ansible >= 2.6
BuildRequires:  python3-devel
BuildRequires:  python3dist(ansible-runner)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(six)

%description
Network Runner is a set of ansible roles and python library that
abstracts Ansible Networking operations. It interfaces
programatically through ansible-runner.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(ansible-runner)
# Python code cannot work without the ansible roles
Requires:  ansible-role-%{ansible_role} = %{version}-%{release}
Requires:  python3dist(six)

%description -n python3-%{pypi_name}
Network Runner is a set of ansible roles and python library that
abstracts Ansible Networking operations. It interfaces
programatically through ansible-runner.

%package -n ansible-role-%{ansible_role}
Summary:   Role for Python Network Runner Library

Requires: ansible >= 2.6
# No cross sub-package dependency.
# Can be installed and used without python package.

%description -n ansible-role-%{ansible_role}
Role for Python Network Runner Library

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l network_runner

%check
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n ansible-role-%{ansible_role}
%license LICENSE
%{_sysconfdir}/ansible/roles/%{ansible_role}/

%changelog
* Fri Aug 02 2024 Dan Radez <dradez@redhat.com> - 0.3.6-16
- Add dependeny on six rhbz#2291791

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.6-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Python Maint <python-maint@redhat.com> - 0.3.6-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 Dan Radez <dradez@redhat.com> - 0.3.6-10
- remove README.md rhbz#2226256
- RPM build warnings: File listed twice: /etc/ansible/roles/network-runner/README.md

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.3.6-6
- Rebuilt for Python 3.11

* Tue Feb 08 2022 Dan Radez <dradez@redhat.com> - 0.3.6-5
- Don't remove egginfo

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Dan Radez <dradez@redhat.com> - 0.3.6-1
- updating to 0.3.6

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.4-2
- Rebuilt for Python 3.10

* Fri Apr 30 2021 Dan Radez <dradez@redhat.com> - 0.3.4-1
- update to 0.3.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Dan Radez <dradez@redhat.com> - 0.2.2-1
- update to 0.2.2

* Tue May 26 2020 Yatin Karel <ykarel@redhat.com> - 0.2.1-3
- Fix 0.2.1 sources and cleanup old sources

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Dan Radez <dradez@redhat.com> - 0.2.1-1
- Updated to 0.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Dan Radez <dradez@redhat.com> - 0.1.7-1
- Updated to 0.1.7

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Dan Radez <dradez@redhat.com> - 0.1.6-1
- Updated to 0.1.6

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 0.1.5-1
- Updated to 0.1.5
- added %check

* Wed Mar 20 2019 Dan Radez <dradez@redhat.com> - 0.1.1-1
- Initial package.
