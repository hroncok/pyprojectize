%global debug_package %{nil}

Name:           pysubnettree
Version:        0.35
Release:        12%{?dist}
Summary:        Python Module for CIDR Lookups

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/zeek/pysubnettree
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

%description
The PySubnetTree package provides a Python data structure SubnetTree which
maps subnets given in CIDR notation (incl. corresponding IPv6 versions) to
Python objects. Lookups are performed by longest-prefix matching.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l SubnetTree _SubnetTree

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc CHANGES README

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.35-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.35-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.35-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.35-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.35-1
- Update to latest upstream release 0.35

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.34-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.34-1
- Update to lastest upstream release 0.34

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.33-2
- Add python3-setuptools as BR

* Mon Jun 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.33-1
- Update to lastest upstream release 0.33

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.32-2
- Rebuilt for Python 3.9

* Sun Feb 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.32-1
- Update to lastest upstream release 0.32

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.30-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.30-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.30-1
- Update to lastest upstream release 0.30

* Tue Mar 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.28-1
- Update to lastest upstream release 0.28

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.27-2
- Rebuilt for Python 3.7

* Sun Jul 01 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.27-1
- Update to lastest upstream release 0.27

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.26-1
- Update to lastest upstream release 0.26

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.24-7
- Rebuild for Python 3.6

* Tue Aug 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-6
- Fix FTBFS (rhbz#1307892)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-3
- Cleanup and py3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-1
- Update to lastest upstream release 0.24

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.23-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.23-3
- Fix macro

* Sun Jun 22 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.23-2
- Use PyPI as SOURCE0 for now
- Fix permission

* Fri Jun 20 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.23-1
- Initial package
