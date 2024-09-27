Name:           netstat-monitor
Version:        1.1.3
Release:        30%{?dist}
Summary:        A command line tool to monitor network connections

License:        AGPL-3.0-or-later
URL:            https://github.com/stalexan/netstat-monitor
Source0:        https://www.alexan.org/netstat-monitor/%{name}-%{version}.tar.gz
# Use ipaddress module (from Python 3 stdlib), not non-Python-3 compatible
# ipaddr (which ipaddress is a fork of in any case)
# https://github.com/stalexan/netstat-monitor/pull/15 , rediffed
Patch0:         netstat-monitor-1.1.3-ipaddress.patch
# Make test runner exit 1 if tests fail (not 0)
Patch1:         https://github.com/stalexan/netstat-monitor/pull/16.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-netaddr

Requires:       python3-netaddr

%description
Netstat-monitor is a command line tool for monitoring network connections.
Its output is similar to the output from the netstat command with the options
"netstat --inet -alp". Netstat-monitor can be left running, though, and will
report new connections as they are made. Also, filters can be used to limit
what's displayed to just what's unexpected or interesting.

%prep
%autosetup -p1
sed -i -e '/^#!\//, 1d' netstat.py

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}/usr/sample-filters \
    %{buildroot}%{_datadir}/%{name}/sample-filters

%check
PYTHONPATH=./ %{__python3} test/test-netstat

%files
%doc README.md
%license LICENSE 
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/%{name}/sample-filters
%{python3_sitelib}/__pycache__/*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.3-29
- Rebuilt for Python 3.13

* Sun Apr 21 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-28
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1.3-24
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.3-21
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.3-18
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-15
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-12
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-10
- Fix ownership (rhbz#1672095)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-7
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Adam Williamson <awilliam@redhat.com> - 1.1.3-3
- Use ipaddress (from Py3 stdlib) not ipaddr (we have no python3-ipaddr)
- Enable tests

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 09 2016 Fabian Affolter <mail@fabian-affolter.ch>- 1.1.3-1
- Update to latest upstream version 1.1.3 (rhbz#1310163)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-3
- Fix changelog entries
- Remove loop

* Wed Apr 23 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-2
- Add requirements

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Initial package for Fedora
