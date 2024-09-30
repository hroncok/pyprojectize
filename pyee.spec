# Tests don't currently pass
%bcond_with tests

Name:      pyee
Version:   9.0.4
Release:   11%{?dist}
Summary:   A port of node.js's EventEmitter to python
License:   MIT
URL:       https://pypi.python.org/pypi/pyee
Source0:   https://github.com/jfhbrook/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:    pyee-switch-to-unittest-mock.diff
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: python3-tox
BuildRequires: python3-twisted
%if %{with tests}
BuildRequires: python3-flake8
BuildRequires: python3-pytest
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-pytest-runner
BuildRequires: python3-pytest-trio
%endif

%description
A port of node.js's EventEmitter to python.

%package -n python3-ee
Summary:       A port of node.js's EventEmitter to python

%description -n python3-ee
A port of node.js's EventEmitter to python.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# currently segfaults
# %%py3_check_import pyee
%if %{with tests}
%pytest -v
%endif

%files -n python3-ee
%license LICENSE
%{python3_sitelib}/*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 9.0.4-10
- Rebuilt for Python 3.13

* Thu Feb 15 2024 Michel Lind <salimma@fedoraproject.org> - 9.0.4-9
- Replace mock with unittest.mock
- Use bcond to toggle tests and gate test BRs but keep them disabled for now

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 9.0.4-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 9.0.4-2
- Rebuilt for Python 3.11

* Sun Feb 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 9.0.4-1
- Update to 9.0.4

* Sun Jan 30 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 9.0.3-1
- Update to 9.0.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 8.2.2-1
- Update to 8.2.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 8.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 8.1.0-1
- Update to 8.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> 7.0.2-1
- Update to 7.0.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.1-2
- Rebuilt for Python 3.9

* Sat Feb  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> 7.0.1-1
- Update to 7.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-4
- Rebuilt for Python 3.7

* Thu May 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 5.0-3
- Fix FTBFS, drop python2 support

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Peter Robinson <pbrobinson@fedoraproject.org> 5.0.0-1
- Update to 5.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb  5 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.0-1
- initial packaging
