# While the headers are architecture independent, the package must be
# built separately on all architectures so that the tests are run
# properly. See also
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
%global debug_package %{nil}

# Whether to run the tests, enabled by default
%bcond_without tests

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 9
%global python2_enabled 0
%else
%global python2_enabled 1
%endif

%global python3_enabled 1

Name:    pybind11
Version: 2.13.1
Release: 3%{?dist}
Summary: Seamless operability between C++11 and Python
License: BSD-3-Clause
URL:	 https://github.com/pybind/pybind11
Source0: https://github.com/pybind/pybind11/archive/v%{version}/%{name}-%{version}.tar.gz

# Patch out header path
Patch1:  pybind11-2.10.1-hpath.patch

# https://github.com/pybind/pybind11/commit/51c2aa16de5b50fe4be6a0016d6090d4a831899e
Patch2:  0001-fixed-a-compilation-error-with-gcc-14.patch

BuildRequires: make
%if %{python2_enabled}
# Needed to build the python libraries
BuildRequires: python2-devel
BuildRequires: python2-setuptools
# These are only needed for the checks
%if %{with tests}
BuildRequires: python2-pytest
BuildRequires: python2-numpy
BuildRequires: python2-scipy
%endif
%endif

%if %{python3_enabled}
# Needed to build the python libraries
BuildRequires: python3-devel
# These are only needed for the checks
%if %{with tests}
BuildRequires: python3-pytest
BuildRequires: python3-numpy
BuildRequires: python3-scipy
%endif
%endif

BuildRequires: eigen3-devel
BuildRequires: gcc-c++
BuildRequires: cmake

%global base_description \
pybind11 is a lightweight header-only library that exposes C++ types \
in Python and vice versa, mainly to create Python bindings of existing \
C++ code.

%description
%{base_description}

%package devel
Summary:  Development headers for pybind11
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
Provides: %{name}-static = %{version}-%{release}
# For dir ownership
Requires: cmake

%description devel
%{base_description}

This package contains the development headers for pybind11.

%if %{python2_enabled}
%package -n     python2-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-pybind11}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description -n python2-%{name}
%{base_description}

This package contains the Python 2 files.
%endif

%if %{python3_enabled}
%package -n     python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-pybind11}

Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%if !%{python2_enabled}
# Take care of upgrade path
Obsoletes:      python2-%{name} < %{version}-%{release}
%endif

%description -n python3-%{name}
%{base_description}

This package contains the Python 3 files.
%endif

%prep
%setup -q
%patch 1 -p1 -b .hpath
%patch 2 -p1 -b .gcc-14

%generate_buildrequires
%pyproject_buildrequires

%build
pys=""
%if %{python2_enabled}
pys="$pys python2"
%endif
%if %{python3_enabled}
pys="$pys python3"
%endif
for py in $pys; do
    mkdir $py
    # When -DCMAKE_BUILD_TYPE is set to Release, the tests in %%check might segfault.
    # However, we do not ship any binaries, and therefore Debug
    # build type does not affect the results.
    # https://bugzilla.redhat.com/show_bug.cgi?id=1921199
    %cmake -B $py -DCMAKE_BUILD_TYPE=Debug -DPYTHON_EXECUTABLE=%{_bindir}/$py -DPYBIND11_INSTALL=TRUE -DUSE_PYTHON_INCLUDE_DIR=FALSE %{!?with_tests:-DPYBIND11_TEST=OFF}
    %make_build -C $py
done

%if %{python2_enabled}
%py2_build
%endif
%if %{python3_enabled}
%pyproject_wheel
%endif

%if %{with tests}
%check
%if %{python2_enabled}
make -C python2 check %{?_smp_mflags}
%endif
%if %{python3_enabled}
make -C python3 check %{?_smp_mflags}
%endif
%endif

%install
# Doesn't matter if both installs run
%if %{python2_enabled}
%make_install -C python2
%endif
%if %{python3_enabled}
%make_install -C python3
%endif
# Force install to arch-ful directories instead.
%if %{python2_enabled}
PYBIND11_USE_CMAKE=true %py2_install "--install-purelib" "%{python2_sitearch}"
%endif
%if %{python3_enabled}
PYBIND11_USE_CMAKE=true %py3_install "--install-purelib" "%{python3_sitearch}"
%endif

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/pybind11/
%{_datadir}/cmake/pybind11/
%{_bindir}/pybind11-config
%{_datadir}/pkgconfig/%{name}.pc

%if %{python2_enabled}
%files -n python2-%{name}
%{python2_sitearch}/%{name}/
%{python2_sitearch}/%{name}-%{version}.dist-info
%endif

%if %{python3_enabled}
%files -n python3-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}.dist-info
%endif

%changelog
* Sat Jul 20 2024 Kefu Chai <tchaikov@gmail.com> - 2.13.1-3
- Apply upstream patch to fix build with GCC-14

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.13.1-1
- Update to 2.13.1.

* Mon Jun 10 2024 Lukáš Zaoral <lzaoral@redhat.com> - 2.12.0-4
- migrate to SPDX license format

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.12.0-3
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.12.0-2
- Bootstrap for Python 3.13

* Tue Apr 09 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.12.0-1
- Update to 2.12.0.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.11.1-1
- Update to 2.11.1.

* Mon Jul 24 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.10.4-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.10.4-2
- Bootstrap for Python 3.12

* Fri Mar 17 2023 Pavel Šimovec <psimovec@redhat.com> - 2.10.4-1
- Update to 2.10.4 rhbz#2179208

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Jonathan Wright <jonathan@almalinux.org> - 2.10.3-1
- Update to 2.10.3 rhbz#2155679

* Mon Nov 07 2022 Jonathan Wright <jonathan@almalinux.org> - 2.10.1-1
- Update to 2.10.1 rhbz#2139245

* Tue Aug 02 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.10.0-1
- Update to 2.10.0.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.9.2-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.9.2-2
- Bootstrap for Python 3.11

* Sat Apr 02 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.9.2-1
- Update to 2.9.2.

* Tue Feb 08 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0.

* Fri Nov 26 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1.

* Wed Aug 04 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.2-3
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.2-2
- Bootstrap for Python 3.10

* Wed Jan 27 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1.

* Wed Aug 12 2020 Merlin Mathesius <mmathesi@redhat.com> - 2.5.0-5
- Drop Python 2 support for ELN and RHEL9+

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.0-6
- Adapt to new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-3
- Rebuilt for Python 3.9

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Bootstrap for Python 3.9

* Wed Apr 01 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3.

* Tue Oct 08 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.4.2-2
- Fix Python 3.8 incompatibility.

* Sat Sep 28 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2.

* Fri Sep 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1.

* Fri Sep 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0.

* Fri May 03 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.4-3
- Fix incompatibility with pytest 4.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.4-1
- Remove python2 packages for Fedora >= 30.
- Update to 2.2.4.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-4
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.2.2-3
- Add Python subpackages based on Elliott Sales de Andrade's patch.

* Sat Feb 17 2018 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.2.2-2
- Fix FTBS by patch from upstream.

* Wed Feb 14 2018 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.2.2-1
- Update to 2.2.2.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.1-1
- Update to latest version
- Update Source URL to include project name.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.0.1-5
- Full compliance with header only libraries guidelines.

* Thu Feb 23 2017 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.0.1-4
- As advised by upstream, disable dtypes test for now.
- Include patch for tests on bigendian systems.

* Thu Feb 23 2017 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.0.1-3
- Make the package arched so that tests can be run on all architectures.
- Run tests both against python2 and python3.

* Wed Feb 22 2017 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.0.1-2
- Switch to python3 for tests.

* Sun Feb 05 2017 Susi Lehtola <jussilehtola@fedorapeople.org> - 2.0.1-1
- First release.
