# Needed for RHEL/CentOS 8
%undefine __cmake_in_source_build

# Set a common one for all architectures and not _target_platform, fixes aarch64
%global __cmake_builddir build

%filter_provides_in %{python3_sitearch}/.*\.so$

Summary:    Library and tool to control NAT in UPnP-enabled routers
Name:       miniupnpc
Version:    2.2.5
Release:    8%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://miniupnp.free.fr/

BuildRequires:  cmake >= 3.5.0
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel

Source0:    http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz

%description
miniupnpc is an implementation of a UPnP client library, enabling applications
to access the services provided by an UPnP "Internet Gateway Device" present on
the network. In UPnP terminology, it is a UPnP Control Point.

This package includes upnpc, a UPnP client application for configuring  port
forwarding in UPnP enabled routers.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development documentation for
%{name}.

%package -n python3-%{name}
Summary:    Python3 interface to %{name}

%description -n python3-%{name}
This package contains python3 interfaces to %{name}.

%prep
%autosetup -p2

# Use already built shared object for Python module
# Unversioned link is not enough to avoid a rebuild
sed -i -e 's|build/libminiupnpc.a|build/libminiupnpc.so.%{version}|g' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DNO_GETADDRINFO=FALSE \
    -DUPNPC_BUILD_SAMPLE=TRUE \
    -DUPNPC_BUILD_SHARED=TRUE \
    -DUPNPC_BUILD_STATIC=FALSE \
    -DUPNPC_BUILD_TESTS=TRUE \
    -DUPNPC_NO_INSTALL=FALSE

%cmake_build
%pyproject_wheel

%install
%cmake_install
%pyproject_install
%pyproject_save_files 'miniupnpc*'

mv %{buildroot}%{_bindir}/upnpc-shared %{buildroot}%{_bindir}/upnpc
mv %{buildroot}%{_bindir}/listdevices %{buildroot}%{_bindir}/upnp-listdevices
rm -f %{buildroot}%{_bindir}/external-ip.sh

%check
make CFLAGS="%{optflags} -DMINIUPNPC_SET_SOCKET_TIMEOUT" check

%files
%license LICENSE
%doc Changelog.txt README
%{_bindir}/upnpc
%{_bindir}/upnp-listdevices
%{_libdir}/libminiupnpc.so.17
%{_libdir}/libminiupnpc.so.%{version}

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}/libminiupnpc-shared-noconfig.cmake
%{_libdir}/cmake/%{name}/libminiupnpc-shared.cmake
%{_libdir}/cmake/%{name}/miniupnpc-config.cmake
%{_libdir}/libminiupnpc.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3*

%files -n python3-%{name} -f %{pyproject_files}

%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.5-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.5-6
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.2.5-2
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Simone Caronni <negativo17@gmail.com> - 2.2.5-1
- Update to 2.2.5.

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.4-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 Simone Caronni <negativo17@gmail.com> - 2.2.4-2
- Restore test client binary.

* Tue Oct 25 2022 Simone Caronni <negativo17@gmail.com> - 2.2.4-1
- Update to 2.2.4.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.3-3
- Rebuilt for Python 3.11

* Sat Jan 29 2022 Simone Caronni <negativo17@gmail.com> - 2.2.3-2
- Build fixes.

* Fri Jan 28 2022 Simone Caronni <negativo17@gmail.com> - 2.2.3-1
- Update to 2.2.3.
- Update SPEC file (license, tabs/spaces, trim changelog, etc.)
- Switch to CMake build.
- Drop static libraries.
- Drop test client and obsolete documentation.
- Do not use static library when building Python module.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.2-2
- Rebuilt for Python 3.10

* Wed Mar 03 2021 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.2.2-1
- Update to version 2.2.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Kalev Lember <klember@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-4
- Subpackage python2-miniupnpc has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 2.1-1
- Update to 2.1

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 2.0-13
- Fix FTBFS (#1604853)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
