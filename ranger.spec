Name:           ranger
Version:        1.9.3
Release:        17%{?dist}
Summary:        A vim-like file manager
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://ranger.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
#Suggests:       w3m-img

%description
Ranger is a free console file manager that gives you greater flexibility and a
good overview of your files without having to leave your *nix console. It
visualizes the directory tree in two dimensions: the directory hierarchy on
one, lists of files on the other, with a preview to the right so you know where
you'll be going.


%prep
%autosetup
sed -i -e '1d;2i#!/usr/bin/python3' %{name}.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '*'
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_pkgdocdir} _doc
find _doc -type f -exec chmod -R -x '{}' \;


%files -f %{pyproject_files}
%doc _doc/*
%{_bindir}/ranger
%{_bindir}/rifle
%{_datadir}/applications/ranger.desktop
%{_mandir}/man1/ranger.1*
%{_mandir}/man1/rifle.1*


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.3-17
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.9.3-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.9.3-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.3-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.3-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-2
- Rebuilt for Python 3.9

* Sun Apr 19 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.3-1
- Update to 1.9.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 21 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.2-2
- spec modernization thanks to Filip Szymański <fszymanski@fedoraproject.org>
- fixes rhbz #1592733 #1408563 #1495481 and #1559823

* Sun Oct 21 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.2-1
- update to latest version + spec cleanup, fixes rhbz #1408563

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 13 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.2-1
- update to 1.7.2

* Wed Sep 30 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.1-3
- run find on the right directory

* Tue Sep 29 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.1-2
- remove executable bits from docs
- remove defattr line

* Sat Sep 26 2015 Ben Boeckel <mathstuf@gmail.com> - 1.7.1-1
- update to 1.7.1

* Thu Sep 10 2015 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-7
- use python3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-5
- fix mupdf binary name (rhbz#1186823)

* Sat Dec 13 2014 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-4
- Fix the right file (was the source file, but upstream regenerates the
  installed file manually).

* Thu Dec 11 2014 Ben Boeckel <mathstuf@gmail.com> - 1.6.1-3
- Fix documentation typo

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1
- add rifle command

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Ben Boeckel <mathstuf@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sat Jul 24 2010 Ben Boeckel <mathstuf@gmail.com> - 1.1.2-2
- Add patch to remove shebang line
- BR python2-devel

* Fri Jul 23 2010 Ben Boeckel <mathstuf@gmail.com> - 1.1.2-1
- Initial package
