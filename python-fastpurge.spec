%global srcname fastpurge

Summary: A Python client for the Akamai Fast Purge API
Name: python-%{srcname}
Version: 1.0.3
Release: 12%{?dist}
URL: https://github.com/release-engineering/%{name}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
BuildArch: noarch

%description
This library provides a simple asynchronous Python wrapper for the Fast
Purge API, including authentication and error recovery.

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:	python3-devel

# Dependencies for test suite
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(edgegrid-python)
BuildRequires:	python3dist(monotonic)
BuildRequires:	python3dist(more-executors)
BuildRequires:	python3dist(mock)
BuildRequires:	python3dist(requests-mock)

# for Requires we rely on the automatic Python dep generator

%description -n python3-%{srcname}
This library provides a simple asynchronous Python wrapper for the Fast
Purge API, including authentication and error recovery.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

%{__python3} -m pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.3-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.0.3-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Rohan McGovern <rohanpm@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.2-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 1.0.2-8
- Explicitly BuildRequires python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 1.0.2-2
- Run test suite during build

* Sat Mar 30 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 1.0.2-1
- Initial RPM release
