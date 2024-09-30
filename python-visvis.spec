%global srcname visvis
Name:             python-%{srcname}
Version:          1.14.0
Release:          10%{?dist}
Summary:          Python library for visualization of 1D to 4D data in an object oriented way
# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
URL:              https://github.com/almarklein/%{srcname}
Source0:          %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:        noarch
BuildRequires:    python3-devel
BuildRequires:    sed

%global _description\
Visvis is a pure Python library for visualization of 1D to 4D data in an\
object oriented way. Essentially, visvis is an object oriented layer of\
Python on top of OpenGl, thereby combining the power of OpenGl with the\
usability of Python. A Matlab/Matplotlib-like interface in the form of a\
set of functions allows easy creation of objects (e.g. plot(), imshow(),\
volshow(), surf()).

%description
%{_description}

%package -n python3-%{srcname}
Summary:          %{summary}
BuildRequires:    python3-devel
Requires:         python3-numpy, python3-pyopengl
Recommends:       python3-PyQt4, python3-wxpython4
Recommends:       python3-gobject

%description -n python3-%{srcname}
%{_description}

%prep
%setup -n %{srcname}-%{version}

# fix shebangs in examples
pushd examples
sed -i "1 s|#!/usr/bin/env python|#!%{python3}|" *.py
popd

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license license.txt
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.14.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.14.0-4
- Rebuilt for new python
  Resolves: rhbz#2220557

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.14.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.14.0-1
- New version
  Resolves: rhbz#2154618

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.13.0-6
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.13.0-5
- Fixed FTBFS
  Resolves: rhbz#2069145

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.13.0-2
- Rebuilt for Python 3.10

* Mon May  3 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.13.0-1
- New version
  Resolves: rhbz#1956244

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.12.4-1
- New version
  Resolves: rhbz#1840466

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-2
- Rebuilt for Python 3.9

* Mon Apr  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.12.3-1
- New version
  Resolves: rhbz#1821247

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.2-5
- Dropped Python 2 support
  Resolves: rhbz#1769828

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.2-1
- New version
  Resolves: rhbz#1693484

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 1.11.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Jun 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.1-3
- Simplified source URL

* Fri Jun 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.1-2
- Simplified the spec

* Thu Jun  7 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.1-1
- Initial release
