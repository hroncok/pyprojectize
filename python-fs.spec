%global srcname fs

# RHEL does not include the test dependencies
%bcond tests %{undefined rhel}

Name:           python-%{srcname}
Version:        2.4.16
Release:        9%{?dist}
Summary:        Python's Filesystem abstraction layer

# https://spdx.org/licenses/MIT.html
License:        MIT
URL:            https://pypi.org/project/fs/
Source0:        https://github.com/PyFilesystem/pyfilesystem2/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Replace TestCase method aliases removed in Python 3.12
# https://github.com/PyFilesystem/pyfilesystem2/pull/570
# changelog fragment removed to avoid conflict
Patch:          570.patch

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(six)
%if %{with tests}
# Required for running tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)
BuildRequires:  python3dist(parameterized)
%endif

%global _description %{expand:
Think of PyFilesystem's FS objects as the next logical step to Python's file
objects. In the same way that file objects abstract a single file, FS objects
abstract an entire filesystem.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n pyfilesystem2-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with tests}
%check
# tests/test_ftpfs.py needs pyftpdlib (not packaged yet)
# test_seek_current and test_seek_end are skipped due to regression in Python 3.12
# upstream issue: https://github.com/python/cpython/issues/102956
%{python3} -m pytest --ignore tests/test_ftpfs.py -k "not test_seek_current and not test_seek_end"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md examples

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.4.16-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Parag Nemade <pnemade AT redhat DOT com> - 2.4.16-4
- Help msuchy to count this package as already using SPDX license expression

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 2.4.16-3
- Rebuilt for Python 3.12

* Thu May 25 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4.16-2
- Disable tests in RHEL builds

* Thu Mar 16 2023 Parag Nemade <pnemade AT redhat DOT com> - 2.4.16-1
- Update to 2.4.16 version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.4.11-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.11-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-5
- Add missing BR: python3-setuptools

* Mon Jun 01 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-4
- Disable few tests temporary for now (rhbz#1820916, rhbz#1841708)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.11-3
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-2
- enable tests and use upstream source tarball

* Mon Mar 30 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.4.11-1
- Initial packaging

