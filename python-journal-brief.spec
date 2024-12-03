%global srcname journal-brief
%global sum Find new systemd journal entries since last run

Name:		python-%{srcname}
Version:	1.1.8
Release:	12%{?dist}
Summary:	%{sum}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://pypi.python.org/pypi/%{srcname}
Source0:	https://pypi.python.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
# en_US.UTF-8 locale required for tests
BuildRequires:	glibc-langpack-en
BuildRequires:	python3-devel
BuildRequires:	python3-PyYAML
%if 0%{?with_check}
BuildRequires:	python3-pytest python3-flexmock
%endif # with_check

%description
Python module for examining, bookmarking, and filtering systemd
journal entries.


%package -n %{srcname}
Summary:	Show interesting new systemd journal entries since last run
Requires:	python3-%{srcname} = %{version}-%{release}
Requires:	python3-setuptools

%description -n %{srcname}
Run this from cron to get a daily or hourly briefing of interesting
new systemd journal entries.


%package -n python3-%{srcname}
Summary:	%{sum}
Requires:	systemd-python3
Requires:	python3-PyYAML
Recommends:	%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}
Python module for examining, bookmarking, and filtering systemd
journal entries.


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '*'


%if 0%{?with_check}
%check
%pyproject_check_import

%{__python3} %{py_setup} test
%endif # with_check


%files -n %{srcname}
%{_bindir}/%{srcname}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.8-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.8-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.8-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.8-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Tim Waugh <twaugh@redhat.com> - 1.1.8-1
- 1.1.8 (bug #2039454).

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Tim Waugh <twaugh@redhat.com> - 1.1.7-3
- Build requires python3-setuptools.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tim Waugh <twaugh@redhat.com> - 1.1.7-1
- 1.1.7.

* Tue Jul  7 2020 Tim Waugh <twaugh@redhat.com> - 1.1.6-1
- 1.1.6.

* Fri Jun 19 2020 Tim Waugh <twaugh@redhat.com> - 1.1.5-16
- Add conditional markers for checks.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Tim Waugh <twaugh@redhat.com> - 1.1.5-12
- Rebuild against Python 3.8.

* Thu Aug 15 2019 Tim Waugh <twaugh@redhat.com> - 1.1.5-11
- Fix running of tests.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Tim Waugh <twaugh@redhat.com> - 1.1.5-9
- Build requires en_US.UTF-8 for test suite (bug #1675746).

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-2
- Rebuild for Python 3.6

* Tue Nov  1 2016 Tim Waugh <twaugh@redhat.com> - 1.1.5-1
- 1.1.5:
  - setup: don't install tests.format (RH bug #1390250)

* Sun Jul 24 2016 Tim Waugh <twaugh@redhat.com> - 1.1.4-1
- 1.1.4.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov  9 2015 Tim Waugh <twaugh@redhat.com> - 1.1.3-1
- 1.1.3 (bug #1279097).

* Wed Nov  4 2015 Tim Waugh <twaugh@redhat.com> - 1.1.2-2
- Add python3-PyYAML runtime dependency (bug #1277715).

* Fri Oct 30 2015 Tim Waugh <twaugh@redhat.com> - 1.1.2-1
- 1.1.2.
- Run doctests in %%check.

* Fri Oct 23 2015 Tim Waugh <twaugh@redhat.com> - 1.1.1-2
- journal-brief sub-package requires python3-setuptools due to
  entrypoint usage.
- python3-journal-brief sub-package requires systemd-python3, not
  (absent) main package.

* Fri Oct 16 2015 Tim Waugh <twaugh@redhat.com> - 1.1.1-1
- Initial spec file.
