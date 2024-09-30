%global srcname  slacker
	
%if 0%{?fedora}
%global with_tests 1
%endif

%if 0%{?rhel}
%global with_tests 0
%endif

Name:           python-%{srcname}
Version:        0.14.0
Release:        17%{?dist}
Summary:        Python Slack API client

License:        Apache-2.0
URL:            https://github.com/os/slacker
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Slacker is a full-featured Python interface for the Slack API.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  python3-responses
%if %{?with_tests}
BuildRequires:  python3-tox
%endif
Requires:       python3-requests

%description -n python3-%{srcname}
Slacker is a full-featured Python interface for the Slack API.

%package -n python3-%{srcname}-doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description -n python3-%{srcname}-doc
Documentation files for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{?with_tests: %{__python3} setup.py test}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n python3-%{srcname}-doc
%license LICENSE
%doc examples/
%exclude /tests/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.14.0-16
- Rebuilt for Python 3.13

* Tue Feb 27 2024 Michel Lind <salimma@fedoraproject.org> - 0.14.0-15
- Remove unused python3-mock dependency
- Use SPDX license identifier

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.14.0-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.14.0-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.14.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-2
- Rebuilt for Python 3.9

* Sun Feb 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Update to latest upstream release 0.14.0 (rhbz#1803330)

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-4
- Update and simplify spec file

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 0.13.0-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Raphael Groner <projects.rg@smart.ms> - 0.12.0-2
- drop useless shebang
- add explicitly runtime dependency

* Sat Dec 15 2018 Raphael Groner <projects.rg@smart.ms> - 0.12.0-1
- new version
- prepare to support second python version for epel
- fix execution of tests if supported with all needed dependencies
- add documentation

* Fri Nov  2 2018 Raphael Groner <projects.rg@smart.ms> - 0.9.65-1
- initial
