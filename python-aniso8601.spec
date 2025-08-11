%global srcname aniso8601
%global sum Another ISO 8601 parser for Python

Name:           python-%{srcname}
Version:        9.0.1
Release:        13%{?dist}
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://bitbucket.org/nielsenb/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel python3-dateutil

%description
Python library for parsing date strings
in ISO 8601 format into datetime format.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Python 3 library for parsing date strings
in ISO 8601 format into datetime format.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%{__python3} -m unittest discover aniso8601/tests/

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 9.0.1-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 9.0.1-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 9.0.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 9.0.1-2
- Rebuilt for Python 3.10

* Tue Mar 02 2021 František Zatloukal <fzatlouk@redhat.com> - 9.0.1-1
- New upstream release 9.0.1

* Thu Feb 18 2021 František Zatloukal <fzatlouk@redhat.com> - 9.0.0-2
- Stop removing egg-info

* Thu Feb 18 2021 František Zatloukal <fzatlouk@redhat.com> - 9.0.0-1
- New upstream release 9.0.0
- Modernize spec a bit

* Mon Feb 08 2021 František Zatloukal <fzatlouk@redhat.com> - 8.1.1-1
- New upstream release 8.1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 06 2020 František Zatloukal <fzatlouk@redhat.com> - 8.1.0-1
- New upstream release 8.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 František Zatloukal <fzatlouk@redhat.com> - 8.0.0-4
- Add BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 František Zatloukal <fzatlouk@redhat.com> - 8.0.0-1
- New upstream release 8.0.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 František Zatloukal <fzatlouk@redhat.com> - 7.0.0-1
- New upstream release 7.0.0

* Mon Mar 11 2019 František Zatloukal <fzatlouk@redhat.com> - 6.0.0-1
- New upstream release 6.0.0

* Sat Mar 02 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.1.0-1
- Update to upstream 5.1.0 release

* Tue Feb 12 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.1.0-1
- Update to upstream 4.1.0 release
- Drop Python 2 support

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Fri Jun 01 2018 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.0.0-1
- Update to latest upstream (rhbz#1447152)

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 11 2015 Jan Sedlak <jsedlak@redhat.com> - 1.1.0-1
- update to 1.1.0, rebuild with Python 3

* Wed Jul 08 2015 Jan Sedlak <jsedlak@redhat.com> - 1.0.0-1
- update to newest version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.82-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu May 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.82-2
- disabled tests for EL6

* Wed Jan 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.82-1
- initial packaging
