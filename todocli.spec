%global commit 219db73c723e4b197c2784718c86b29c782e4b95
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global project todo.py
%global owner okulbilisim
%global date 20151115

Name:           todocli
Version:        0.1
Release:        32.%{date}git%{shortcommit}%{?dist}
Summary:        Command line To Do application

License:        MIT
URL:            https://github.com/okulbilisim/todo.py
Source0:        https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{commit}.tar.gz
Source1:        todocli.1
Patch0:         todocli-fix-version.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A To Do command line application with SQLite back end written in Python.

%prep
%setup -q -n %{project}-%{commit}
%patch -P0 -p1
#Remove egg.info
rm -rf %{name}.egg.info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*'

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/
 
%files -f %{pyproject_files}
%doc README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/* 

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1-31.20151115git219db73
- Rebuilt for Python 3.13

* Thu Feb 08 2024 Didier Fabert <didier.fabert@gmail.com> - 0.1-30.20151115git219db73
- Fix FTBFS https://bugzilla.redhat.com/show_bug.cgi?id=2259654

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 22 2023 Didier Fabert <didier.fabert@gmail.com> - 0.1-28.20151115git219db73
- migrated to SPDX license

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1-26.20151115git219db73
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1-23.20151115git219db73
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1-20.20151115git219db73
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-17.20151115git219db73
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-15.20151115git219db73
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-14.20151115git219db73
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-10.20151115git219db73
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-6.20151115git219db73
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5.20151115git219db73
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4.20151115git219db73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 William Moreno <williamjmorenor@gmail.com> - 0.1-3.20151115git219db73
- Update to 20151115git219db73

* Sun Nov 15 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 0.1-220140709gitf50c240
- Python3 Support: https://fedoraproject.org/wiki/FAD_Python_3_Porting_2015

* Thu Jul 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 0.1-20140709gitf50c240
- Update Python Macros

* Thu Jul 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 0.1-20140709gitf50c240.3
- Add manpage

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-20140709gitf50c240.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Fedora <williamjmorenor@gmail.com> 
- 0.1-20140709gitf50c240.1
- Fix macros for el6

* Sat Dec 27 2014 William Moreno Reyes  <williamjmorenor at gmail.com> - 0.1-20140709gitf50c240
- Initial Packaging

