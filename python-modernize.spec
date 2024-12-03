%global srcname modernize

Name:           python-modernize
Version:        0.8.0
Release:        15%{?dist}
Summary:        Modernizes Python code for eventual Python 3 migration

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/modernize
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It attempts, but does not guarantee, to generate a Python 2/3 compatible
codebase.  The code that it generates needs python2.6+ and has a runtime
dependency on python-six.

%package -n python3-modernize
Summary:        %{summary}
Provides: python-modernize = %{version}-%{release}
Obsoletes: python-modernize < 0.4-3

%description -n python3-modernize
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It attempts, but does not guarantee, to generate a Python 2/3 compatible
codebase.  The code that it generates needs python2.6+ and has a runtime
dependency on python-six.

%prep
%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'libmodernize*' 'modernize*'

%check
%pyproject_check_import

%files -n python3-modernize -f %{pyproject_files}
%doc README.rst
%{_bindir}/python-modernize
%{_bindir}/modernize

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Kevin Fenzi <kevin@scrye.com> - 0.8.0-1
- Update to 0.8.0. Fixes rhbz#1881536

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 0.7-1
- Update to 0.7. Fixes bug #1680393

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6.1-1
- Update to 0.6.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5-5
- Rebuild for Python 3.6

* Sat Sep 17 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-4
- Obsoletes/Provide old python-modernize name to fix upgrades. Fixes bug #1375605

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Ralph Bean <rbean@redhat.com> - 0.5-2
- Switch over to a python3 package with modern python macros.

* Thu Feb 04 2016 Ralph Bean <rbean@redhat.com> - 0.5-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Ralph Bean <rbean@redhat.com> - 0.4-1
- new version

* Wed Aug 27 2014 Luke Macken <lmacken@redhat.com> - 0.3-1
- Update to 0.3 (#1130054)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-2
- BuildRequire python-setuptools; needed by setup.py
- Remove rpm constructs not needed in EPEL6+ or any current Fedora

* Mon Jul 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-1
- Initial Fedora build.

