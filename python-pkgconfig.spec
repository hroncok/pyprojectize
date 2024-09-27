%global srcname pkgconfig
%if 0%{?fedora} && 0%{?fedora} <= 30
%bcond_without python2
%else
%bcond_with python2
%endif

Name:           python-%{srcname}
Version:        1.5.5
Release:        11%{?dist}
Summary:        Python interface to the pkg-config command line tool

License:        MIT
URL:            https://github.com/matze/pkgconfig
Source:         %{pypi_source}

BuildArch:      noarch

%description
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 2.6+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        Python2 interface to the pkg-config ocmmand line tool
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       %{_bindir}/pkg-config

%description -n python2-%{srcname}
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 2.6+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

Python 2 version.
%endif

%package -n python3-%{srcname}
Summary:        Python3 interface to the pkg-config command line tool
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       %{_bindir}/pkg-config

%description -n python3-%{srcname}
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 2.6+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
# We need to keep egg-info as a directory
# https://github.com/sdispater/poetry/issues/866
sed -i -e s/distutils.core/setuptools/ setup.py

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%if %{with python2}
%py2_install
%endif
%py3_install

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.5-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.5-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.5-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.5.5-1
- Update to version 1.5.5 (#1967782)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.2-2
- Rebuilt for Python 3.10

* Sun Mar 21 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.5.2-1
- Update to version 1.5.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Drop python2 for Fedora 31+ (bug #1694619)

* Mon Apr  1 2019 Orion Poplawski <orion@nwra.com> - 1.5.1-1
- Update to 1.5.1
- Patch setup.py to revert to setuptools

* Sun Mar 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.7

* Sun Feb 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuild for Python 3.6

* Sun Dec 04 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Wed Oct 12 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-7
- Fix build for EPEL

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 14 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-5
- Make package compliant with new packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-1
- Add BR on python-nose
- Combined build

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-1
- Initial package
