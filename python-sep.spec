%global srcname sep

Name: python-%{srcname}
Version: 1.2.1
Release: 12%{?dist}
Summary: Astronomical source extraction and photometry in Python

# Code from photutils is BSD (src/overlap.h)
# Code from sextractor is LGPLv3+
# Python wrapper is MIT (sex.pyx)
# Automatically converted from old format: MIT and LGPLv3+ and BSD - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LGPL-3.0-or-later AND LicenseRef-Callaway-BSD

URL: http://sep.readthedocs.org/
Source0: %{pypi_source}

BuildRequires: gcc
BuildRequires: python3-devel

%description
SEP makes available some of the astronomical source extraction and 
photometry algorithms in Source Extractor as stand-alone 
functions and classes. These operate directly on in-memory numpy arrays 
(no FITS files, configuration files, etc). It’s derived directly from 
(and tested against) the Source Extractor code base.

%package -n python3-%{srcname}
Summary: Astronomical source extraction and photometry in Python
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires: %{py3_dist Cython}
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist numpy}

%description -n python3-%{srcname}
SEP makes available some of the astronomical source extraction and 
photometry algorithms in Source Extractor as stand-alone 
functions and classes. These operate directly on in-memory numpy arrays 
(no FITS files, configuration files, etc). It’s derived directly from 
(and tested against) the Source Extractor code base.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc AUTHORS.md README.md CHANGES.md
%license licenses/MIT_LICENSE.txt licenses/LGPL_LICENSE.txt licenses/BSD_LICENSE.txt
%{python3_sitearch}/sep-*.egg-info
%{python3_sitearch}/sep*.so

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.2.1-10
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Sergio Pascual <sergio.pasra@gmail.com> - 1.2.1-1
- New upstream source (1.2.1)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Sergio Pascual <sergio.pasra@gmail.com> - 1.2.0-1
- New upstream source (1.2.0)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Sergio Pascual <sergio.pasra@gmail.com> - 1.1.1-2
- New upstream source (1.1.1)
- Fix changelog date

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Charalampos Stratakis <cstratak@redhat.com> - 1.0.3-6
- Recythonize the sources

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.3-4
- Drop python2 subpackage

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.0.3-3
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Christian Dersch <lupinix@mailbox.org> - 1.0.3-1
- new version, also fixes the FTBFS with Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Sergio Pascual <sergio.pasra@gmail.com> - 1.0.1-1
- New upstream source (1.0.1)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuild for Python 3.6

* Mon Oct 17 2016 Sergio Pascual <sergio.pasra@gmail.com> - 1.0.0-1
- New upstream (1.0.0)
- License changes to BSD plus MIT plus LGPLv3+

* Tue Sep 13 2016 Sergio Pascual <sergio.pasra@gmail.com> - 0.6.0-1
- New upstream (0.6.0)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Sergio Pascual <sergio.pasra@gmail.com> - 0.5.2-1
- New upstream (0.5.2)
- Change source url to pypi.io

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Sergio Pascual <sergio.pasra@gmail.com> - 0.4.1-1
- New upstream (0.4.1)
- Use new python macros

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Sergio Pascual <sergio.pasra@gmail.com> - 0.4.0-1
- New upstream (0.4.0)

* Tue Dec 16 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.0-1
- Initial specfile

