Name:           binwalk
Version:        2.3.4
Release:        9%{?dist}
Summary:        Firmware analysis tool
License:        MIT
URL:            https://github.com/ReFirmLabs/binwalk
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         binwalk-2.3.3-tests.patch
Patch1:         %{url}/pull/559/commits/6e7736869d998edb6384728c03a348cd9ab1f9ca.patch
Patch2:         version-oops.patch
# https://github.com/ReFirmLabs/binwalk/issues/507
Patch3:         requires-zombie-imp.patch
BuildArch:      noarch
BuildRequires:  python3-devel
# https://github.com/ReFirmLabs/binwalk/issues/507
BuildRequires:  (python3-zombie-imp if python3-devel >= 3.12)
# For tests
BuildRequires:  python3-nose python3-coverage
# Optional, for graphs and visualizations
Suggests:       python3-pyqtgraph
# Optional, for --disasm functionality
Suggests:       capstone
# Optional, for automatic extraction/decompression of files and data
Recommends:     mtd-utils gzip bzip2 tar arj p7zip p7zip-plugins cabextract squashfs-tools lzop srecord
Suggests:       sleuthkit

%description
Binwalk is a tool for searching a given binary image for embedded files and
executable code. Specifically, it is designed for identifying files and code
embedded inside of firmware images. Binwalk uses the python-magic library, so 
it is compatible with magic signatures created for the Unix file utility. 

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -f %{pyproject_files}
%doc API.md INSTALL.md README.md
%{_bindir}/%{name}

%changelog
* Wed Jul 31 2024 Scott Talbert <swt@techie.net> - 2.3.4-9
- Confirm License tag is already SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.4-7
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Scott Talbert <swt@techie.net> - 2.3.4-3
- BR python3-zombie-imp to fix FTBFS with Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3.4-2
- Rebuilt for Python 3.12

* Fri Feb 03 2023 Scott Talbert <swt@techie.net> - 2.3.4-1
- Update to new upstream release 2.3.4 (#2166724)

* Fri Jan 27 2023 Scott Talbert <swt@techie.net> - 2.3.3-3
- Fix path traversal in PFS extractor script (#2165006)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Scott Talbert <swt@techie.net> - 2.3.3-1
- Update to new upstream release 2.3.3 (#2003337 #2156566)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.2-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 Scott Talbert <swt@techie.net> - 2.3.2-1
- Update to new upstream release 2.3.2 (#1994176)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.1-2
- Rebuilt for Python 3.10

* Fri Mar 26 2021 Scott Talbert <swt@techie.net> - 2.3.1-1
- Update to new upstream release 2.3.1 (#1941447)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Scott Talbert <swt@techie.net> - 2.2.0-1
- Update to new upstream release 2.2.0 (#1761636)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-13
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-9
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Scott Talbert <swt@techie.net> - 2.1.1-7
- Add p7zip-plugins as a dependency and change from Suggests to Recommends (#1511958)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Scott Talbert <swt@techie.net> - 2.1.1-1
- New upstream release 2.1.1
- Remove patches (all upstream/obsolete), switch to noarch, add suggests

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Aug 24 2015 Scott Talbert <swt@techie.net> - 2.0.0-6
- Needed to specify python3 to configure

* Mon Aug 24 2015 Scott Talbert <swt@techie.net> - 2.0.0-5
- Cherry-pick patch from upstream for python3 fix
- Add weak dependency on python3-pyqtgraph (#1248735)

* Thu Jul 30 2015 Scott Talbert <swt@techie.net> - 2.0.0-4
- Switch to python3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov  1 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.0-2
- Fix *.so permissions for -debuginfo

* Mon Sep 29 2014 Scott Talbert <swt@techie.net> - 2.0.0-1
- New upstream release 2.0.0 (#1085059, #1111576)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  8 2013 Tom Callaway <spot@fedoraproject.org> 1.2-1
- update to 1.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Adam Jackson <ajax@redhat.com> 0.4.5-1
- Initial packaging.

