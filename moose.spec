# for F < 33
# If it isn't defined, undefine doesn't do anything, so no conditional required
%undefine __cmake_in_source_build

#global commit 0e12e41b52deb8ea746bc760cddd6e100ca5cfd8
#global shortcommit %%(c=%{commit}; echo ${c:0:7})

Name:           moose
Version:        3.1.5
%global codename chamcham
Release:        23%{?dist}%{?prerelease:.%{prerelease}}%{?commit:.git%{shortcommit}}
Summary:        Multiscale Neuroscience and Systems Biology Simulator
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://moose.ncbs.res.in/
%if %{defined commit}
Source0:        https://github.com/BhallaLab/moose-core/archive/%{commit}.tar.gz#/moose-core-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/BhallaLab/moose-core/archive/v%{version}.tar.gz#/moose-core-%{version}.tar.gz
%endif

# Fix segfault on py3.9
# https://github.com/BhallaLab/moose-core/pull/420
Patch0:         c570f7c057f9c0ca7360c82a8932bcb0df222da9.patch
Patch1:         665c532745987fb1c7a8fc2a9a57bffa330480b4.patch
# ppc defines a different suffix which breaks the build
Patch2:         0001-Use-.so-suffix-for-all-arches.patch
# Python 3.10 support
# https://github.com/BhallaLab/moose-core/issues/437
Patch3:         moose-python3.10.patch

ExcludeArch: s390x

BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  tinyxml-devel
BuildRequires:  muParser-devel
BuildRequires:  libsbml-devel
# for tests
BuildRequires:  checksec
BuildRequires:  procps-ng
BuildRequires:  openssl

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-libsbml

%description
MOOSE is the base and numerical core for large, detailed simulations
including Computational Neuroscience and Systems Biology. MOOSE spans
the range from single molecules to subcellular networks, from single
cells to neuronal networks, and to still larger systems. It is
backwards-compatible with GENESIS, and forward compatible with Python
and XML-based model definition standards like SBML and NeuroML.

MOOSE uses Python as its primary scripting language. For backward
compatibility we have a GENESIS scripting module, but this is
deprecated. MOOSE numerical code is written in C++.

%package -n python3-%{name}
Summary:  %{summary}

Requires: python3-numpy
Requires: python3-matplotlib
Requires: python3-matplotlib-qt5
Requires: python3-lxml

%description -n python3-%{name}
This package contains the %{summary}.

%prep
%autosetup -n moose-core-%{version} -S git

# Remove O3 flag set in CMakeLists
sed -i 's/-O3//' CMakeLists.txt

%global py_setup setup.cmake.py

%generate_buildrequires
%pyproject_buildrequires

%build
# On armv7 we get a failure with LTO.
# Disable LTO for armv7
%ifarch armv7hl
%define _lto_cflags %{nil}
%endif

cmake_opts=(
        -DBUILD_SHARED_LIBS:BOOL=OFF
        -DCMAKE_SKIP_RPATH:BOOL=ON
        -DCMAKE_C_FLAGS="%optflags"
        -DCMAKE_CXX_FLAGS="%optflags"
        -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS -Wl,--build-id"
        -DCMAKE_MODULE_LINKER_FLAGS="$LDFLAGS -Wl,--build-id"
        -DVERSION_MOOSE=%{version}
        -DCMAKE_BUILD_TYPE="Release|RelWithDebugInfo"
        -DCMAKE_INSTALL_DO_STRIP=0
        -DPYTHON_EXECUTABLE=%{__python3}
)

CXXFLAGS="%optflags -DH5_USE_110_API" \
%cmake "${cmake_opts[@]}"
%cmake_build

pushd %{__cmake_builddir}/python
%pyproject_wheel
popd

%install
install -vD %{__cmake_builddir}/moose.bin %{buildroot}%{_bindir}/moose
install -vDt %{buildroot}%{_libdir}/ %{__cmake_builddir}/libmoose.so

pushd %{__cmake_builddir}/python
%pyproject_install}
# this is necessary for the dependency generator to work
chmod +x %{buildroot}%{python3_sitearch}/moose/_moose*.so
popd

%check
checksec --file=%{buildroot}%{_bindir}/moose

pushd %{__cmake_builddir}
# test_streamer fails randomly when quitting moose every once in a while.
ctest --output-on-failure -V -E 'test_streamer'
# ctest --output-on-failure -V -E 'test_streamer|test_pyrun'
popd

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -c \
    'import moose; element = moose.Neutral("/yyy"); print(element.path)'

%global _docdir_fmt %{name}

%files
%{_bindir}/moose
%{_libdir}/libmoose.so
%license LICENSE
%doc README.md

%files -n python3-%{name}
%{python3_sitearch}/moose
%{python3_sitearch}/rdesigneur
%{python3_sitearch}/pymoose-%{version}.dist-info
%license LICENSE
%doc README.md

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.5-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.1.5-21
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1.5-17
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.5-15
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.1.5-13
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 3.1.5-11
- Rebuild for hdf5 1.12.1

* Tue Aug 31 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1.5-10
- Fix FTI: python3-matplotlib-qt4 was obsoleted by -qt5
- https://bugzilla.redhat.com/show_bug.cgi?id=1996423
- Remove unneeded provides macro

* Mon Aug 16 2021 Orion Poplawski <orion@nwra.com> - 3.1.5-9
- Add patch for python 3.10 support (bz#1899115)

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 3.1.5-8
- Rebuild for hdf5 1.10.7

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.5-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1.5-4
- Undefine cmake macro for F < 33

* Sat Aug 29 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1.5-3
- Update patch

* Thu Aug 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1.5-2
- Add patch to fix ppc build
- Disable lto on arm

* Wed Aug 26 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.1.5-1
- Update to 3.1.5
- Use new cmake macros
- Include patch to fix on Py3.9

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 3.1.4-13
- Use __cmake_in_source_build

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 3.1.4-12
- Rebuild for hdf5 1.10.6

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-11
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.4-9
- Add missing libmoose.so (#1754997)

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.4-8
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-7
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for hdf5 1.10.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-3
- Subpackage python2-moose has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Aug 28 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.4-2
- Rebuild because the package was not tagged properly

* Tue Aug 14 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.4-1
- Switch source back to use "moose-core" instead of "moose"
- Update to latest version
- Actually run the tests and look at the output

* Tue Aug  7 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.3-1
- Update to latest version, fix packaging (#1604882)
- Libmubml seems to be gone
- Add some dependencies useful for tests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.19.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-0.18.beta.2.git0e12e41
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.17.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.2-0.16.beta.2.git0e12e41
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.15.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.14.beta.2.git0e12e41
- Rebuild for gsl-2.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.13.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-0.12.beta.2.git0e12e41
- Rebuild for Python 3.6

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 3.0.2-0.11.beta.2.git0e12e41
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-0.10.beta.2.git0e12e41
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar  7 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 3.0.2-0.9.beta.2.git0e12e41
- Restore patch that removes broken shared linking

* Mon Mar  7 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 3.0.2-0.8.beta.2.git0e12e41
- Update to git snapshot
- Add python3 subpackage

* Tue Feb 23 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-0.7.beta.2
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.6.beta.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-0.5.beta.2
- Rebuild for hdf5 1.8.16

* Sun Dec 13 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.4.beta.2
- Fix permissions on files in debuginfo subpackage
- Tweak python package generation

* Sun Dec 13 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.3.beta.2
- Fix build on i686

* Sat Dec 12 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.2.beta.2
- Remove obsolete cxx11 fix
- Use chrpath --delete

* Wed Dec  9 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.1.beta.2
- Initial packaging
