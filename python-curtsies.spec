Summary:       Curses-like terminal wrapper, with colored strings
Name:          python-curtsies
Version:       0.4.2
Release:       6%{?dist}
License:       MIT
URL:           https://github.com/bpython/curtsies
Source0:       https://files.pythonhosted.org/packages/source/c/curtsies/curtsies-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: python3-blessed
BuildRequires: python3-blessings
BuildRequires: python3-cwcwidth
BuildRequires: python3-devel
BuildRequires: python3-nose
BuildRequires: python3-pyte
%global _description\
Curtsies is curses-like terminal wrapper, can be to annotate portions\
of strings with terminal colors and formatting.\
\
Most terminals will display text in color if you use ANSI escape codes\
- curtsies makes rendering such text to the terminal easy. Curtsies\
assumes use of an VT-100 compatible terminal: unlike curses, it has no\
compatibility layer for other types of terminals.
%description %_description

%package     -n python3-curtsies
Summary:        %summary
Requires:       python3-blessings >= 1.5
Requires:       python3-cwcwidth
%description -n python3-curtsies %_description

%prep
%autosetup -p1 -n curtsies-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files curtsies

%check
nosetests .

%files -n python3-curtsies -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 17 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.4.2-2
- Rebuild

* Tue Aug 08 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.4.2-1
- 0.4.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 23 2022 Terje Rosten <terje.rosten@ntnu.no> - 0.4.1-1
- 0.4.1

* Fri Sep 02 2022 Terje Rosten <terje.rosten@ntnu.no> - 0.4.0-1
- 0.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.10-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 20 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.3.10-1
- 0.3.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.5-2
- Rebuilt for Python 3.10

* Sun Mar 14 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.3.5-1
- 0.3.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.3.4-1
- 0.3.4

* Sun Jul 12 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.3.3-1
- 0.3.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.3.1-1
- 0.3.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.3.0-5
- Remove legacy

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Sun May 27 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.3.0-1
- 0.3.0

* Tue Feb 13 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.2.12-1
- 0.2.12

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.11-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.11-5
- Python 2 binary package renamed to python2-curtsies
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.11-2
- Rebuild for Python 3.6

* Tue Oct 25 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.11-1
- 0.2.11

* Tue Oct 11 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.10-1
- 0.2.10

* Sun Sep 18 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.9-1
- 0.2.9

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.6-1
- 0.2.6

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.1.19-1
- 0.1.19
- bpython needs < 0.2

* Tue Jan 13 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.2.0-1
- 0.2.0

* Wed May 28 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.0.32-1
- initial package
