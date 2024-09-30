%global srcname bitarray
%global sum Efficient Array of Booleans --C Extensions

Name:           python-%{srcname}
Version:        2.8.5
Release:        6%{?dist}
Summary:        %{sum}

# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            https://pypi.python.org/pypi/%{srcname}/
Source0:        https://pypi.python.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-devel


%description
Bitarrays are sequence types and behave very much like usual lists.
Eight bits are represented by one byte in contiguous block of memory.
The user can select between two representations; little-endian and big-endian.
Most of the functionality is implemented in C.Methods for accessing the machine
representation are provided. This can be useful when bit level access to binary
files is required, such as portable bitmap image files (.pbm). Also, when
dealing with compressed data which uses variable bit length encoding
you may find this module useful.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:  %{sum}

%description -n python%{python3_pkgversion}-%{srcname}
Bitarrays are sequence types and behave very much like usual lists.
Eight bits are represented by one byte in contiguous block of memory.
The user can select between two representations; little-endian and big-endian.
Most of the functionality is implemented in C.Methods for accessing the machine
representation are provided. This can be useful when bit level access to binary
files is required, such as portable bitmap image files (.pbm). Also, when
dealing with compressed data which uses variable bit length encoding
you may find this module useful.
This is Python 3 version.


%prep
%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '%{srcname}*'


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.8.5-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.8.5-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 09 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.8.5-1
- Update to 2.8.5 (#2217191)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.7.5-2
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Nick Bebout <nb@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.3-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.3-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.3-2
- Rebuilt for Python 3.10

* Tue Feb 02 2021 Nick Bebout <nb@fedoraproject.org> - 1.6.3-1
- Update to 1.6.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1 (#1853987)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Sérgio Basto <sergio@serjux.com> - 1.2.2-1
- Update python-bitarray to 1.2.2 (#1837147)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1 (#1771103)

* Tue Sep 03 2019 Sérgio Basto <sergio@serjux.com> - 1.0.1-1
- Update to 1.0.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Sérgio Basto <sergio@serjux.com> - 0.9.3-1
- Update to 0.9.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-4
- Subpackage python2-bitarray has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Jul 23 2018 Nick Bebout <nb@fedoraproject.org> - 0.8.3-3
- Add gcc to BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 9 2018 Nick Bebout <nb@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-5
- Rebuild for Python 3.6

* Tue Oct 04 2016 Sérgio Basto <sergio@serjux.com> - 0.8.1-4
- Clean trailing whitespaces
- Add support to epel 7 and 6, disable python3 in el6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 03 2016 Sérgio Basto <sergio@serjux.com> - 0.8.1-2
- Replace python-bitarray with python2-bitarray
  https://fedoraproject.org/wiki/Packaging:Guidelines#Renaming.2FReplacing_Existing_Packages

* Thu Jun 30 2016 Sérgio Basto <sergio@serjux.com> - 0.8.1-1
- Clean up the spec

* Thu Jun 09 2016 Dominika Krejci <dkrejci@redhat.com>
- Add Python 3
- Upgrade to version 0.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 08 2009 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> 0.3.5-1
- Initial RPM release

