Name:           rpl
Version:        1.5.7
Release:        30%{?dist}
Summary:        Intelligent recursive search/replace utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/kcoyner/rpl/
Source0:        https://github.com/kcoyner/rpl/archive/v%{version}.tar.gz

# Reported upstream at https://github.com/kcoyner/rpl/issues/5
Patch0:         rpl-python3.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
rpl is a UN*X text replacement utility. It will replace strings with
new strings in multiple text files. It can work recursively over
directories and supports limiting the search to specific file
suffixes.

rpl was originally written by Joe Laffey; this is a rewritten version.

%prep
%setup -q

%patch -P0

# upstream mistake
sed -i s/1\.5\.6/%{version}/ setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*'
%{__install} -m 0644 -D rpl.1 %{buildroot}%{_mandir}/man1/rpl.1



%check
%pyproject_check_import



%files -f %{pyproject_files}
%doc LICENSE README.md
%{_bindir}/rpl
%{_mandir}/man1/rpl.1.gz

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.7-30
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.7-28
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.7-23
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.7-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.7-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Tim Jackson <rpm@timj.co.uk> - 1.5.7-15
- Add explicit BuildRequires on python3-setuptools

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.7-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.7-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.7-7
- Rebuilt for Python 3.7

* Fri May 11 2018 Tim Jackson <rpm@timj.co.uk> - 1.5.7-6
- Fix issue related to replacing strings with an empty string/use of --prompt (rhbz #1524082)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Tim Jackson <rpm@timj.co.uk> - 1.5.7-2
- Fix build on arbitrary versions of python 3, by using Python install macro
- Package python metadata properly

* Sat Jan 21 2017 Tim Jackson <rpm@timj.co.uk> - 1.5.7-1
- Update to upstream 1.5.7
- No longer requires python2 (RHBZ #1374924)
- Change references to new upstream location (at GitHub)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 19 2008 Tim Jackson <rpm@timj.co.uk> 1.5.5-1
- Update to version 1.5.5
- Move to new upstream distribution location (Sourceforge)

* Sun Sep 10 2006 Tim Jackson <rpm@timj.co.uk> 1.5.3-4
- Requires: python in place of env/python hack

* Sat Sep 09 2006 Tim Jackson <rpm@timj.co.uk> 1.5.3-3
- Fix missing dep on python

* Sat Sep 09 2006 Tim Jackson <rpm@timj.co.uk> 1.5.3-2
- Correct file mode on manpage (0755->0644)

* Mon Sep 04 2006 Tim Jackson <rpm@timj.co.uk> 1.5.3-1
- Initial RPM build
