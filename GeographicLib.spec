%global nativever 2.4
%global baserelease 2
%global pythonver 2.0
%global pythonrelease %{nativever}.%{baserelease}

Name:           GeographicLib
Version:        %{nativever}
Release:        %{baserelease}%{?dist}
Summary:        Library for geographic coordinate transformations

License:        MIT
URL:            https://github.com/geographiclib/geographiclib
Source0:        https://github.com/geographiclib/geographiclib/archive/v%{nativever}/%{name}-%{nativever}.tar.gz
Source1:        %{pypi_source geographiclib %pythonver}

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build

%description
GeographicLib is a small set of C++ classes for performing conversions 
between geographic, UTM, UPS, MGRS, geocentric, and local Cartesian 
coordinates, for gravity (e.g., EGM2008), geoid height and geomagnetic 
field (e.g., WMM2010) calculations, and for solving geodesic problems. 
The emphasis is on returning accurate results with errors close to round-off 
(about 5–15 nanometers). New accurate algorithms for Geodesics on an 
ellipsoid of revolution and Transverse Mercator projection have been 
developed for this library. The functionality of the library can be accessed 
from user code, from the Utility programs provided, or via the 
Implementations in other languages.


%package devel
Summary:        Development files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{nativever}-%{baserelease}%{?dist}
Requires:       cmake

%description devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%package doc
Summary:        Development documentation for %name
BuildArch:      noarch

%description doc
This package contains doxygen-generated html API documentation for
the %{name} library.


%package -n python3-%{name}
Summary:        Python 3 implementation of %{name}
Version:        %{pythonver}
Release:        %{pythonrelease}%{?dist}
BuildArch:      noarch

%description -n python3-%{name}
A translation of the GeographicLib::Geodesic class to Python 3


%package -n mingw32-%{name}
Summary:        MinGW Windows %{name} library
BuildArch:      noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw32-python3-%{name}
Summary:        MinGW Windows %{name} python 3 bindings
Version:        %{pythonver}
Release:        %{pythonrelease}%{?dist}
BuildArch:      noarch

%description -n mingw32-python3-%{name}
MinGW Windows %{name} python 3 bindings.


%package -n mingw64-%{name}
Summary:        MinGW Windows %{name} library
BuildArch:      noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%package -n mingw64-python3-%{name}
Summary:        MinGW Windows %{name} python 3 bindings
Version:        %{pythonver}
Release:        %{pythonrelease}%{?dist}
BuildArch:      noarch

%description -n mingw64-python3-%{name}
MinGW Windows %{name} python 3 bindings.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n geographiclib-%{nativever} -a1


%generate_buildrequires
%pyproject_buildrequires


%build
# Native build
%cmake \
  -DLIBDIR=%{_lib} \
  -DPKGDIR=%{_lib}/pkgconfig \
  -DCMAKEDIR=%{_lib}/cmake/%{name} \
  -DEXAMPLEDIR=%{_defaultdocdir}/%{name}/examples
%cmake_build
# MinGW build
%mingw_cmake -DDOCDIR= -DMANDIR= -DEXAMPLEDIR=
%mingw_make_build

pushd geographiclib-%{pythonver}
# Native build
%pyproject_wheel
# MinGW build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
popd


%install
# Native build
%cmake_install
# MinGW build
%mingw_make_install

pushd geographiclib-%{pythonver}
# Native build
%pyproject_install
# MinGW build
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
popd

%mingw_debug_install_post


%check
%cmake_build -t testprograms
%ctest


%files
%doc AUTHORS NEWS
%license LICENSE.txt
%{_bindir}/CartConvert
%{_bindir}/ConicProj
%{_bindir}/GeoConvert
%{_bindir}/GeodesicProj
%{_bindir}/GeodSolve
%{_bindir}/GeoidEval
%{_bindir}/Gravity
%{_bindir}/IntersectTool
%{_bindir}/MagneticField
%{_bindir}/Planimeter
%{_bindir}/RhumbSolve
%{_bindir}/TransverseMercatorProj
%{_sbindir}/geographiclib-get-geoids
%{_sbindir}/geographiclib-get-gravity
%{_sbindir}/geographiclib-get-magnetic
%{_libdir}/libGeographicLib.so.26*
%{_mandir}/man1/*.1.*
%{_mandir}/man8/*.8.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libGeographicLib.so
%{_libdir}/cmake/GeographicLib
%{_libdir}/pkgconfig/geographiclib.pc

%files doc
%license LICENSE.txt
%doc %{_defaultdocdir}/%{name}/

%files -n python3-%{name}
%license LICENSE.txt
%{python3_sitelib}/geographiclib/
%{python3_sitelib}/geographiclib-%{pythonver}.dist-info

%files -n mingw32-%{name}
%license LICENSE.txt
%{mingw32_bindir}/CartConvert.exe
%{mingw32_bindir}/ConicProj.exe
%{mingw32_bindir}/GeoConvert.exe
%{mingw32_bindir}/GeodesicProj.exe
%{mingw32_bindir}/GeodSolve.exe
%{mingw32_bindir}/GeoidEval.exe
%{mingw32_bindir}/Gravity.exe
%{mingw32_bindir}/IntersectTool.exe
%{mingw32_bindir}/MagneticField.exe
%{mingw32_bindir}/Planimeter.exe
%{mingw32_bindir}/RhumbSolve.exe
%{mingw32_bindir}/TransverseMercatorProj.exe
%{mingw32_bindir}/libGeographicLib.dll
%{mingw32_includedir}/%{name}/
%{mingw32_libdir}/libGeographicLib.dll.a
%{mingw32_libdir}/cmake/GeographicLib/
%{mingw32_libdir}/pkgconfig/geographiclib.pc

%files -n mingw32-python3-%{name}
%license LICENSE.txt
%{mingw32_python3_sitearch}/geographiclib/
%{mingw32_python3_sitearch}/geographiclib-%{pythonver}.dist-info/

%files -n mingw64-%{name}
%license LICENSE.txt
%{mingw64_bindir}/CartConvert.exe
%{mingw64_bindir}/ConicProj.exe
%{mingw64_bindir}/GeoConvert.exe
%{mingw64_bindir}/GeodesicProj.exe
%{mingw64_bindir}/GeodSolve.exe
%{mingw64_bindir}/GeoidEval.exe
%{mingw64_bindir}/Gravity.exe
%{mingw64_bindir}/IntersectTool.exe
%{mingw64_bindir}/MagneticField.exe
%{mingw64_bindir}/Planimeter.exe
%{mingw64_bindir}/RhumbSolve.exe
%{mingw64_bindir}/TransverseMercatorProj.exe
%{mingw64_bindir}/libGeographicLib.dll
%{mingw64_includedir}/%{name}/
%{mingw64_libdir}/libGeographicLib.dll.a
%{mingw64_libdir}/cmake/GeographicLib/
%{mingw64_libdir}/pkgconfig/geographiclib.pc

%files -n mingw64-python3-%{name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/geographiclib/
%{mingw64_python3_sitearch}/geographiclib-%{pythonver}.dist-info/


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Sandro Mani <manisandro@gmail.com> - 2.4-1
- Update to 2.4

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3-6
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 Sandro Mani <manisandro@gmail.com> - 2.3-2
- Bump release

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 2.3-1
- Update to 2.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2-4
- Rebuilt for Python 3.12

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 2.2-3
- Rebuild with octave 8.1.0

* Fri Mar 31 2023 Sandro Mani <manisandro@gmail.com> - 2.2-2
- Switch to pypi source

* Wed Mar 08 2023 Sandro Mani <manisandro@gmail.com> - 2.2-1
- Update to 2.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 2.1.1-2
- Switch to python3-build

* Tue Jul 26 2022 Sandro Mani <manisandro@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Sandro Mani <manisandro@gmail.com> - 2.1-2
- Fix borken requires

* Wed Jun 29 2022 Sandro Mani <manisandro@gmail.com> - 2.1-1
- Update to 2.1

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0-3
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.0-2
- Rebuild for octave 7.1

* Sun May 22 2022 Sandro Mani <manisandro@gmail.com> - 2.0-1
- Update to 2.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.52-8
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 1.52-7
- Make mingw subpackages noarch

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 1.52-6
- Add mingw subpackages

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 1.52-3
- Rebuild for octave 6.3.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Sandro Mani <manisandro@gmail.com> - 1.52-1
- Update to 1.52

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.51-3
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Sandro Mani <manisandro@gmail.com> - 1.51-1
- Update to 1.51

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.50.1-5
- Fix to work with C++17 (streamoff is in std:: not std::ios::)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.50.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sandro Mani <manisandro@gmail.com> - 1.50.1-1
- Update to 1.50.1

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 1.50-1
- Update to 1.50

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.49-11
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Rich Mattes <richmattes@gmail.com> - 1.49-9
- Use setup.py to install python library (rhbz#1724031)

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.49-8
- Rebuild for octave 5.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.49-6
- Subpackage python2-GeographicLib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.49-5
- Rebuild for octave 4.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.49-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1.49-1
- Update to 1.49

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.48-5
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.48-2
- Define %%octpkg for octave scriptlets

* Wed Jun 07 2017 Sandro Mani <manisandro@gmail.com> - 1.48-1
- Update to 1.48

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.43-8
- Rebuild for Python 3.6

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 1.43-7
- Rebuild for octave 4.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jul 3 2015 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.43-3
- Add Python 3 subpackage

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Rich Mattes <richmattes@gmail.com> - 1.43-1
- Update to release 1.43

* Mon May 04 2015 Rich Mattes <richmattes@gmail.com> - 1.42-1
- Update to release 1.42
- Add octave subpackage

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.40-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 02 2015 Rich Mattes <richmattes@gmail.com> - 1.40-1
- Update to release 1.40

* Sat Oct 04 2014 Rich Mattes <richmattes@gmail.com> - 1.38-2
- Fix cmake installation directory

* Sat Oct 04 2014 Rich Mattes <richmattes@gmail.com> - 1.38-1
- Update to 1.38
- Change BR from python2 to python2-devel
- Remove buildroot cleanup from install section

* Fri Sep 19 2014 Rich Mattes <richmattes@gmail.com> - 1.37-1
- Initial package
