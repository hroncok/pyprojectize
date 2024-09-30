Name:           brotli
Version:        1.1.0
Release:        5%{?dist}
Summary:        Lossless compression algorithm

License:        MIT
URL:            https://github.com/google/brotli
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz


%if 0%{?rhel} == 7
BuildRequires:  devtoolset-7-toolchain, devtoolset-7-libatomic-devel
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion}-devel
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package -n libbrotli
Summary:        Library for brotli lossless compression algorithm

%description -n libbrotli
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.


%package -n python%{python3_pkgversion}-%{name}
Summary:        Lossless compression algorithm (python 3)

%description -n python%{python3_pkgversion}-%{name}
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.
This package installs a Python 3 module.


%package devel
Summary:        Lossless compression algorithm (development files)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description devel
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.
This package installs the development files

%prep
%autosetup -p1
# fix permissions for -debuginfo
# rpmlint will complain if I create an extra %%files section for
# -debuginfo for this so we'll put it here instead
chmod 644 c/enc/*.[ch]
chmod 644 c/include/brotli/*.h
chmod 644 c/tools/brotli.c

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%cmake3 \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%cmake3_build
%else
%cmake \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%cmake_build
%endif
%pyproject_wheel

%install
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%cmake3_install
%else
%cmake_install
%endif

# I couldn't find the option to not build the static libraries
#rm "%{buildroot}%{_libdir}/"*.a

%pyproject_install
%pyproject_save_files _brotli brotli
install -dm755 "%{buildroot}%{_mandir}/man3"
cd docs
for i in *.3;do
install -m644 "$i" "%{buildroot}%{_mandir}/man3/${i}brotli"
done

%ldconfig_scriptlets

%check
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%ctest3
%else
%ctest
%endif

%files
%{_bindir}/brotli

%files -n libbrotli
%license LICENSE
%{_libdir}/libbrotlicommon.so.1*
%{_libdir}/libbrotlidec.so.1*
%{_libdir}/libbrotlienc.so.1*

# Note that there is no %%files section for the unversioned python module
# if we are building for several python runtimes
%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}
%license LICENSE

%files devel
%{_includedir}/brotli
%{_libdir}/libbrotlicommon.so
%{_libdir}/libbrotlidec.so
%{_libdir}/libbrotlienc.so
%{_libdir}/pkgconfig/libbrotlicommon.pc
%{_libdir}/pkgconfig/libbrotlidec.pc
%{_libdir}/pkgconfig/libbrotlienc.pc
%{_mandir}/man3/constants.h.3brotli*
%{_mandir}/man3/decode.h.3brotli*
%{_mandir}/man3/encode.h.3brotli*
%{_mandir}/man3/types.h.3brotli*


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 1.1.0-1
- Update to 1.1.1 rhbz#2233368

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.9-12
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 03 2022 Jonathan Wright <jonathan@almalinux.org> - 1.0.9-10
- Fix EL7 builds

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.9-8
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1.0.9-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Travis Kendrick <pouar@pouar.net> - 1.0.9-3
- Apparently %%autosetup calls %%patch on its own

* Thu Oct 01 2020 Travis Kendrick <pouar@pouar.net> - 1.0.9-2
- Fix pc file (#1884364)

* Wed Sep 30 2020 Travis Kendrick <pouar@pouar.net> - 1.0.9-1
- Update to 1.0.9 (#1872932)

* Wed Aug 12 2020 Carl George <carl@george.computer> - 1.0.7-14
- Update cmake invocation rhbz#1863298

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-11
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.7-9
- Splil out the libs to a separate package

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-7
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Orion Poplawski <orion@nwra.com> - 1.0.7-5
- Build with devtoolset-7 on EPEL7 to fix aarch64 builds

* Thu Mar 28 2019 Carl George <carl@george.computer> - 1.0.7-4
- EPEL compatibility

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-2
- Remove last python2 bits

* Wed Nov 28 2018 Travis Kendrick pouar@pouar.net> - 1.0.7-1
- Update to 1.0.7

* Wed Nov 28 2018 Travis Kendrick pouar@pouar.net> - 1.0.5-2
- remove Python 2 support https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Travis Kendrick pouar@pouar.net> - 1.0.5-1
- update to 1.0.5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.7

* Wed Apr 18 2018 Travis Kendrick pouar@pouar.net> - 1.0.4-2
- update to 1.0.4

* Sat Mar 03 2018 Travis Kendrick <pouar@pouar.net> - 1.0.3-1
- update to 1.0.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Switch to %%ldconfig_scriptlets

* Fri Sep 22 2017 Travis Kendrick <pouar@pouar.net> - 1.0.1-1
- update to 1.0.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-4
- add man pages

* Sun May 14 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-3
- wrong directory for ctest
- LICENSE not needed in -devel
- fix "spurious-executable-perm"
- rpmbuild does the cleaning for us, so 'rm -rf %%{buildroot}' isn't needed

* Sat May 13 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-2
- include libraries and development files

* Sat May 06 2017 Travis Kendrick <pouar@pouar.net> - 0.6.0-1
- Initial build
