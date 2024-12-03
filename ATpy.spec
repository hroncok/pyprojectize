Name: ATpy
Version: 0.9.7
Release: 40%{?dist}
Summary: Astronomical Tables in Python
License: MIT

URL: http://atpy.readthedocs.org
Source0: https://pypi.python.org/packages/source/A/ATpy/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

%global _description\
ATpy is a high-level Python package providing a way to manipulate tables of\
astronomical data in a uniform way. It provides built-in support for NumPy\
recarrays and common astronomical file/database formats (FITS, VO, HDF5,\
and ASCII tables) with a very simple API.

%description %_description

%package -n python3-ATpy
Summary: Astronomical Tables in Python
Requires: python3-numpy python3-astropy

%description -n python3-ATpy
ATpy is a high-level Python package providing a way to manipulate tables of 
astronomical data in a uniform way. It provides built-in support for NumPy
recarrays and common astronomical file/database formats (FITS, VO, HDF5, 
and ASCII tables) with a very simple API.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l atpy

%check
%pyproject_check_import

%files -n python3-ATpy -f %{pyproject_files}
%doc CHANGES README.md

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.7-39
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.7-34
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.7-31
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.7-28
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-25
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-23
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-22
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-21
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.7-18
- Update spec file
- Drop python2 subpackage

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-16
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.7-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.7-13
- Python 2 binary package renamed to python2-atpy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jan 27 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.7-3
- Activate python3 build

* Thu Jan 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.7-2
- Add a requirement on python-astropy
- Macro fixes

* Tue Jul 30 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.7-1
- New upstream release 0.9.7
- Minor cleanups in the spec

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.6-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.6-3
- remove rhel logic from with_python3 conditional

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.6-1
- New upstream release.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.5.3-1
- New upstream release.

* Wed May 11 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.5-2
- Moving Requires for python3 to its proper place in package macro

* Mon May 02 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.5-1
- New upstream release

* Tue Apr 26 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.4-3
- Added support for python3

* Tue Apr 26 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.4-2
- Updated upstream web site
- More details in files section

* Tue Nov 30 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.9.4-1
- Initial spec file
