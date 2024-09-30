Name:          bpython
Summary:       Fancy curses interface to the Python interactive interpreter
Version:       0.24
Release:       9%{?dist}
URL:           http://www.bpython-interpreter.org/
License:       MIT
Source0:       https://github.com/bpython/bpython/archive/%{version}-release.tar.gz
BuildArch:     noarch
BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: python3-blessed
BuildRequires: python3-devel
BuildRequires: python3-sphinx
%description
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems. It has the following features:
 o in-line syntax highlighting
 o readline-like autocomplete with suggestions displayed as you type
 o expected parameter list for any Python function.
 o eewind function to pop the last line of code from memory and
   re-evaluate.
 o send the code you've entered off to a pastebin and display the
   pastebin URL for copying, etc.
 o save the code you've entered to a file
 o auto indentation

%package -n    python3-bpython
Summary:       Fancy curses interface to the Python 3 interactive interpreter
Provides:      bpython3 = %{version}-%{release}
Provides:      bpython = %{version}-%{release}
Obsoletes:     bpython < 0.17.1-6
Obsoletes:     bpython-gtk < 0.14
Requires:      python3-curtsies >= 0.3.5
Requires:      python3-greenlet
Requires:      python3-pygments
Requires:      python3-requests > 1.2.3
Requires:      python3-six >= 1.5
Recommends:    python3dist(jedi)
Recommends:    python3dist(watchdog)
%description -n python3-bpython
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems. It has the following features:
 o in-line syntax highlighting
 o readline-like autocomplete with suggestions displayed as you type
 o expected parameter list for any Python function.
 o eewind function to pop the last line of code from memory and
   re-evaluate.
 o send the code you've entered off to a pastebin and display the
   pastebin URL for copying, etc.
 o save the code you've entered to a file
 o auto indentation

This is the Python 3 build of bpython.

%package -n    python3-bpython-urwid
Summary:       Urwid interface to the Python 3 interactive interpreter
Requires:      python3-bpython = %{version}-%{release}
Requires:      python3dist(urwid)
Requires:      python3dist(twisted)

%description -n python3-bpython-urwid
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems. It has the following features:
 o in-line syntax highlighting
 o readline-like autocomplete with suggestions displayed as you type
 o expected parameter list for any Python function.
 o eewind function to pop the last line of code from memory and
   re-evaluate.
 o send the code you've entered off to a pastebin and display the
   pastebin URL for copying, etc.
 o save the code you've entered to a file
 o auto indentation

%prep
%autosetup -n %{name}-%{version}-release

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}
pushd doc/sphinx/
make man
popd

%install
%{pyproject_install}
%pyproject_save_files bpdb 'bpython*'
# backwards compatibility links python3
ln -s bpython %{buildroot}/%{_bindir}/bpython3
ln -s bpython-curses %{buildroot}/%{_bindir}/bpython3-curses
ln -s bpdb %{buildroot}%{_bindir}/bpdb3
ln -s bpython %{buildroot}%{_bindir}/python3-bpython
install -m0644 -p -D doc/sphinx/build/man/bpython.1 \
    %{buildroot}%{_mandir}/man1/bpython.1
install -m0644 -p -D doc/sphinx/build/man/bpython-config.5 \
    %{buildroot}%{_mandir}/man5/bpython-config.5

%files -n python3-bpython -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%doc theme/light.theme theme/sample.theme theme/windows.theme
%{_bindir}/bpdb
%{_bindir}/bpython
%{_bindir}/bpython-curses
%{_bindir}/bpdb3
%{_bindir}/bpython3
%{_bindir}/bpython3-curses
%{_bindir}/python3-bpython
%{_mandir}/man1/bpython.1*
%{_mandir}/man5/bpython-config.5*
%{_datadir}/pixmaps/bpython.png
%{_datadir}/metainfo/org.bpython-interpreter.bpython.metainfo.xml
%{_datadir}/applications/org.bpython-interpreter.bpython.desktop

%files -n python3-bpython-urwid
%{_bindir}/bpython-urwid

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.24-8
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 15 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.24-5
- Install man pages by script

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.24-3
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.24-1
- 0.24

* Fri Sep 02 2022 Terje Rosten <terje.rosten@ntnu.no> - 0.23-1
- 0.23

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.22.1-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.22.1-1
- 0.22.1

* Sun Nov 07 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.22.0-1
- 0.22.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.21-2
- Rebuilt for Python 3.10

* Sat Apr 03 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.21-1
- 0.21

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.20.1-2
- Backport upstream patch to fix six issue (rhbz#1914468)

* Tue Jan 19 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.20.1-1
- 0.20.1

* Tue Oct 13 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.20-1
- 0.20

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.19-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.19-1
- 0.19

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.18-1
- Undo breakage in reqs from previous commit
- 0.18

* Fri Mar 08 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-6
- Drop Python 2 bpython
- Add Python 3 bpython-urwid

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.17.1-4
- Use correct python macro

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-2
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.17.1-1
- 0.17.1

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.17-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Jul 28 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.17-1
- 0.17

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.16-1
- 0.16

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.15-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.15-1
- 0.15

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.14.2-1
- 0.14.2

* Thu Mar 26 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.14.1-1
- 0.14.1
- gtk gone upstream, remove sub package and add obsolete
- appdata, desktop file and png upstream
- new deps
- curtsies now default

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.13.2-2
- Add an AppData file for the software center

* Mon Jan 12 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.13.2-1
- 0.13.2
- Swap bpython3 symlinks
- Add bpython3 provide
- Python requests package required

* Sun Jan 11 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.13.1-3
- Add bpython3 symlink

* Sat Jan 10 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.13.1-2
- Move bpython-gtk to subpackage (bz #1178996)

* Mon Aug 11 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.13.1-1
- 0.13.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Nov 18 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.12-4
- Add patch to fix resize crash (bz #667934)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.12-2
- Add patch to fix import crash (bz #823662)

* Wed Jan 30 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.12-1
- 0.12

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-3
- remove rhel logic from with_python3 conditional

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.11-1
- 0.11

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.10.1-2
- Add python-urwid to buildreq

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.10.1-1
- 0.10.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 02 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.7.1-1
- 0.9.7.1

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9.6.2-7
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun May 30 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6.2-5
- Add patch to fix suspend

* Sun May 09 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6.2-4
- bpython don't use pyparsing

* Fri May 07 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.6.2-3
- Add python3 subpackage (bz #590107)

* Fri Apr 09 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6.2-2
- Fix man page (bz #561800)

* Fri Apr 09 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6.2-1
- 0.9.6.2

* Thu Nov 05 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5.2-1
- 0.9.5.2

* Fri Jul 31 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-1
- 0.9.4
- Update urls

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-1
- 0.8.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.7.1-2
- Add setuptools to buildreq

* Mon Jan  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.7.1-1
- 0.7.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.7.0-2
- Rebuild for Python 2.6

* Mon  Sep 1 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.7.0-1
- 0.7.0

* Tue Aug 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.6.3-1
- 0.6.3

* Mon May  5 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.3.1-2
- fix summary
- remove desktop file and optflags

* Wed Apr 30 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.3.1-1
- 0.3.1
- drop patch

* Sun Apr 27 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-1
- random fixes

* Sun Apr 27 2008 Pascal Bleser <guru@unixtech.be> 0.2.3
- new package
