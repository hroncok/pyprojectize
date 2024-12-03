%global pypi_name mackup

%bcond_without tests

Name:           python-%{pypi_name}
Version:        0.8.32
Release:        14%{?dist}
Summary:        Keep your application settings in sync

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/lra/mackup
# pypi_source does not have license and tests
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  procps-ng
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(six)
%endif

%global _description %{expand:
Mackup:
- Backs up your application settings in a safe directory (e.g. Dropbox)
- Syncs your application settings among all your workstations
- Restores your configuration on any fresh install in one command line

By only tracking pure configuration files, it keeps the cruft out of your
freshly new installed workstation (no cache, temporary and locally specific
files are transferred).

Mackup makes setting up the environment easy and simple, saving time for your
family, great ideas, and all the cool stuff you like. }

%description %{_description}


%package -n     %{pypi_name}
Summary:        %{summary}
Requires:       procps-ng

%description -n %{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%pytest


%files -n %{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/mackup


%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.32-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.32-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.32-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.32-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.32-2
- Rebuilt for Python 3.10

* Wed May 12 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.8.32-1
- Initial package
