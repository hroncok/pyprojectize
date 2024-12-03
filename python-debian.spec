Name:           python-debian
Version:        0.1.49
Release:        10%{?dist}
Summary:        Modules for Debian-related data formats
# debfile.py, arfile.py, debtags.py are release under GPL v3 or above
# everything else is GPLv2+
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Source0:        http://ftp.debian.org/debian/pool/main/p/python-debian/python-debian_%{version}.tar.xz
URL:            https://salsa.debian.org/python-debian-team/python-debian
BuildArch:      noarch
BuildRequires:  python3-devel
#tests
BuildRequires:  dpkg
BuildRequires:  python3-six
BuildRequires:  python3-chardet
BuildRequires:  python3-pytest
%if ! 0%{?rhel}
BuildRequires:  python3-apt
%endif

%global _description\
This package provides Python modules that abstract many formats of Debian\
related files. Currently handled are:\
* Debtags information (debian.debtags module)\
* debian/changelog (debian.changelog module)\
* Packages files, pdiffs (debian.debian_support module)\
* Control files of single or multiple RFC822-style paragraphs, e.g.\
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.\
  (debian.deb822 module)\
* Raw .deb and .ar files, with (read-only) access to contained\
  files and meta-information

%description %_description

%package -n python3-debian
Summary:        Modules for Debian-related data formats
BuildRequires:  python3-devel
Requires:       python3-chardet
Requires:       xz
Requires:       python3-six
Suggests:       gnupg
%if ! 0%{?rhel}
Recommends:     python3-apt
%endif

%description -n python3-debian
This package provides Python modules that abstract many formats of Debian
related files. Currently handled are:
* Debtags information (debian.debtags module)
* debian/changelog (debian.changelog module)
* Packages files, pdiffs (debian.debian_support module)
* Control files of single or multiple RFC822-style paragraphs, e.g.
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.
  (debian.deb822 module)
* Raw .deb and .ar files, with (read-only) access to contained
  files and meta-information


%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
sed -e 's/__CHANGELOG_VERSION__/%{version}/' < lib/debian/_version.py.in > lib/debian/_version.py
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files deb822 debian debian_bundle 'python_debian*'

%check
%pyproject_check_import

%if 0%{?rhel}
# this fail because of missing apt-get python module, but this file is
# use to create test.ar file
rm lib/debian/tests/test_deb822.py
touch lib/debian/tests/test_deb822.py
# this will fail because python is build with hashlib. This conflicts
# with the required internal _sha1 module
rm lib/debian/tests/test_debian_support.py
touch lib/debian/tests/test_debian_support.py.
# Expected to fail. To be fixed.
rm lib/debian/tests/test_debfile.py
touch lib/debian/tests/test_debfile.py
%endif
%pytest

%files -n python3-debian -f %{pyproject_files}
%doc README.rst HISTORY.deb822

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.49-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.49-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Miro Hrončok <mhroncok@redhat.com> - 0.1.49-6
- Don't own /usr/lib/python3.X/site-packages/__pycache__

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.49-4
- Rebuilt for Python 3.12

* Sat Feb 11 2023 msuchy <msuchy@redhat.com> - 0.1.49-3
- migrate license to spdx

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 0.1.49-1
- version 0.1.49

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.36-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Stefan Bluhm <stefan.bluhm@clacee.eu> - 0.1.36-9
- Added RHEL8 build

* Wed Jul 28 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.1.36-8
- Add weak dependency on python-apt on Fedora

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.36-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.36-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Miroslav Suchý <msuchy@redhat.com> 0.1.36-1
- rebase to 0.1.36

* Tue Oct 16 2018 Miroslav Suchý <msuchy@redhat.com> 0.1.33-1
- rebase to python-debian-0.1.33
- update url to new homepage
- removed python2 subpackage

* Fri Aug 03 2018 Miroslav Suchý <msuchy@redhat.com> 0.1.32-3
- Update python macros to python2
- correctly replace version in setup.py

* Thu Aug 02 2018 Miroslav Suchý <msuchy@redhat.com> 0.1.32-2
- BR python-chardet for tests
- BR python-six for tests
- BR dpkg for tests
- do not call python but rather python2

* Thu Aug 02 2018 Miroslav Suchý <msuchy@redhat.com> 0.1.32-1
- rebase python-debian to 0.1.32

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.30-5
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.30-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Miroslav Suchý <msuchy@redhat.com> 0.1.30-2
- Python 2 binary package renamed to python2-debian

* Wed Aug 09 2017 Miroslav Suchý <msuchy@redhat.com> 0.1.30-1
- remove lzma patch as it is already in upstream
- update to python-debian_0.1.30

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.27-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.27-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 14 2016 Miroslav Suchý <msuchy@redhat.com> 0.1.27-3
- 1021625 - add support for lzma

* Thu Oct 08 2015 Miroslav Suchý <msuchy@redhat.com> 0.1.27-2
- define macro for epel

* Thu Oct 08 2015 Miroslav Suchý <msuchy@redhat.com> 0.1.27-1
- rebase to python-debian_0.1.27
- add python3 subpackage

* Mon Apr 13 2015 Miroslav Suchý <msuchy@redhat.com> 0.1.26-2
- rebase to 0.1.26

* Mon Apr 13 2015 Miroslav Suchý <msuchy@redhat.com> 0.1.26-1
- rebase to 0.1.26

* Thu Nov 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.21-10
- add dependency on python-six

* Thu Nov 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.21-9
- specify patch level
- specify prefix of tar

* Thu Nov 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.21-8
- rebase to nmu2 release

* Thu Nov 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.21-7
- 1021625 - recognize xz compression

* Mon Oct  3 2011 Miroslav Suchy <msuchy@redhat.com> 0.1.21-2
- rebase to 0.1.21 release
- require python-chardet

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May  7 2010 Miroslav Suchy <msuchy@redhat.com> 0.1.16-4
- rebuild for python 2.7

* Fri May  7 2010 Miroslav Suchy <msuchy@redhat.com> 0.1.16-3
- use proper tar.gz from upstream
- add %%check section

* Fri Apr 30 2010 Miroslav Suchy <msuchy@redhat.com> 0.1.16-2
- add dist tag

* Thu Apr 22 2010 Lukáš Ďurfina <lukas.durfina@gmail.com> 0.1.16-1
- Creation of package
