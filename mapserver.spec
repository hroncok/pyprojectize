%global ini_name 39-mapserver.ini
%global project_owner MapServer
%global project_name MapServer

%global python_mapscript 1
%global srcname mapscript

%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

%if 0%{?fedora} >= 41
%ifarch %{ix86}
%bcond_with    php
%else
%bcond_without php
%endif
%else
%bcond_without php
%endif


Name:           mapserver
Version:        8.2.2
Release:        1%{?dist}
Summary:        Environment for building spatially-enabled internet applications
%global dashver %(echo %version | sed 's|\\.|-|g')

License:        MIT
URL:            http://www.mapserver.org

Source0:        https://github.com/%{project_owner}/%{project_name}/archive/rel-%{dashver}/%{project_name}-%{version}.tar.gz


## Upstream patches
# mappostgresql.c: avoid potential invalid use of strcpy()
Patch1001:      f202bd52b35c82508555af722a8ad0f04910c403.patch

Requires:       httpd
Requires:       dejavu-sans-fonts

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  fcgi-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gd-devel >= 2.0.16
BuildRequires:  gdal-devel
BuildRequires:  geos-devel >= 3.7.1
BuildRequires:  giflib-devel
BuildRequires:  httpd-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXpm-devel
BuildRequires:  libxslt-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  pam-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  protobuf-c-devel
BuildRequires:  libpq-devel
BuildRequires:  proj-devel => 5.2.0
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  zlib-devel
#Get
#/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf
#/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf
# See %%prep below
BuildRequires:  dejavu-sans-fonts


%description
Mapserver is an internet mapping program that converts GIS data to
map images in real time. With appropriate interface pages,
Mapserver can provide an interactive internet map based on
custom GIS data.


%package  libs
Summary:  %{summary}

%description libs
This package contains the libs for mapserver.


%package  devel
Summary:        Development files for mapserver
Requires:       %{name} = %{version}

%description devel
This package contains development files for mapserver.

%if %{with php}
%package -n php-%{name}
Summary:        PHP/Mapscript map making extensions to PHP
BuildRequires:  php-devel
Requires:       php-gd%{?_isa}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

%description -n php-%{name}
The PHP/Mapscript extension provides full map customization capabilities within
the PHP scripting language.
%endif


%package perl
Summary:        Perl/Mapscript map making extensions to Perl
Requires:       %{name} = %{version}-%{release}

%description perl
The Perl/Mapscript extension provides full map customization capabilities
within the Perl programming language.

%if 0%{python_mapscript}
%package -n python3-mapserver
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:        Python/Mapscript map making extensions to Python
BuildRequires:  python3-devel
Requires:       %{name} = %{version}-%{release}
Requires:       python3

%description -n python3-mapserver
The Python/Mapscript extension provides full map customization capabilities
within the Python programming language.
%endif

%if %{with java}
%package java
Summary:        Java/Mapscript map making extensions to Java
BuildRequires:  java-devel
Requires:       %{name} = %{version}-%{release}
Requires:       java-headless

%description java
The Java/Mapscript extension provides full map customization capabilities
within the Java programming language.
%endif


%package ruby
Summary:       Ruby/Mapscript map making extensions to Ruby
BuildRequires: ruby-devel
Requires:      %{name} = %{version}-%{release}

%description ruby
The Ruby/Mapscript extension provides full map customization capabilities within
the ruby programming language.


%prep
%autosetup -p1 -n %{project_owner}-rel-%{dashver}

# replace fonts for tests with symlinks
ln -sf /usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf tests/vera/Vera.ttf
ln -sf /usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf tests/vera/VeraBd.ttf

# Force swig to regenerate the wrapper
rm -rf mapscript/perl/mapscript_wrap.c


%generate_buildrequires
%pyproject_buildrequires


%build
export CFLAGS="${CFLAGS} -ldl -fPIC -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"

%cmake -DINSTALL_LIB_DIR=%{_libdir} \
      -DCMAKE_SKIP_RPATH=ON \
      -DCMAKE_SKIP_INSTALL_RPATH=ON \
      -DWITH_CAIRO=TRUE \
      -DWITH_CLIENT_WFS=TRUE \
      -DWITH_CLIENT_WMS=TRUE \
      -DWITH_CURL=TRUE \
      -DWITH_FCGI=TRUE \
      -DWITH_FRIBIDI=TRUE \
      -DWITH_GD=TRUE \
      -DWITH_GDAL=TRUE \
      -DWITH_GEOS=TRUE \
      -DWITH_GIF=TRUE \
      -DWITH_ICONV=TRUE \
%if %{with java}
      -DWITH_JAVA=TRUE \
%else
      -DWITH_JAVA=FALSE \
%endif
      -DWITH_KML=TRUE \
      -DWITH_LIBXML2=TRUE \
      -DWITH_OGR=TRUE \
      -DWITH_MYSQL=TRUE \
      -DWITH_PERL=TRUE \
      -DCUSTOM_PERL_SITE_ARCH_DIR="%{perl_vendorarch}" \
%if %{with php}
      -DWITH_PHPNG=TRUE \
%endif
      -DWITH_POSTGIS=TRUE \
      -DWITH_PROJ=TRUE \
%if 0%{python_mapscript}
      -DWITH_PYTHON=TRUE \
%endif
      -DWITH_RUBY=TRUE \
      -DWITH_V8=FALSE \
      -DWITH_SOS=TRUE \
      -DWITH_THREAD_SAFETY=TRUE \
      -DWITH_WCS=TRUE \
      -DWITH_WMS=TRUE \
      -DWITH_WFS=TRUE \
      -DWITH_XMLMAPFILE=TRUE \
      -DWITH_POINT_Z_M=TRUE \
      -DWITH_APACHE_MODULE=FALSE \
      -DWITH_SVGCAIRO=FALSE \
      -DWITH_CSHARP=FALSE \
      -DWITH_ORACLESPATIAL=FALSE \
      -DWITH_ORACLE_PLUGIN=FALSE \
      -DWITH_MSSQL2008=FALSE \
      -DWITH_SDE=FALSE \
      -DWITH_SDE_PLUGIN=FALSE \
      -DWITH_EXEMPI=FALSE \
      -Wno-dev

%cmake_build


%install
%cmake_install

# cmake tries to invoke pip and download things. we'll just use setuptools.
mkdir -p %{buildroot}%{python3_sitearch}
pushd redhat-linux-build/src/mapscript/python
%pyproject_install
popd

mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 src/xmlmapfile/mapfile.xsd %{buildroot}%{_datadir}/%{name}
install -p -m 644 src/xmlmapfile/mapfile.xsl %{buildroot}%{_datadir}/%{name}

%if %{with java}
# install java
mkdir -p %{buildroot}%{_javadir}
install -p -m 644 %{_vpath_builddir}/src/mapscript/java/mapscript.jar %{buildroot}%{_javadir}/
%endif

%if %{with php}
# install php config file
mkdir -p %{buildroot}%{php_inidir}
cat > %{buildroot}%{php_inidir}/%{ini_name} <<EOF
; Enable %{name} extension module
extension=php_mapscriptng.so
EOF
%endif

# Install sample config file as %%doc
rm %{buildroot}%{_usr}/%{_sysconfdir}/mapserver-sample.conf


%files
%doc README.md
%doc etc/mapserver-sample.conf
%{_bindir}/coshp
%{_bindir}/legend
%{_bindir}/mapserv
%{_bindir}/map2img
%{_bindir}/msencrypt
%{_bindir}/scalebar
%{_bindir}/shptree
%{_bindir}/shptreetst
%{_bindir}/shptreevis
%{_bindir}/sortshp
%{_bindir}/tile4ms
%{_datadir}/%{name}/

%files libs
%doc README.md
%{_libdir}/libmapserver.so.%{version}
%{_libdir}/libmapserver.so.2

%files devel
%doc README.md
%{_libdir}/libmapserver.so
%{_includedir}/%{name}/

%if %{with php}
%files -n php-%{name}
%doc src/mapscript/php/README.md
%config(noreplace) %{php_inidir}/%{ini_name}

# this is only installed when swig < 4.0.2 https://github.com/MapServer/MapServer/blob/25ef061bec310773511eb84ef03f4a91e0f5a081/src/mapscript/phpng/CMakeLists.txt#L86
%if ! 0%{?fedora} && 0%{?rhel} < 10
%{php_extdir}/mapscript.php
%endif

%{php_extdir}/php_mapscriptng.so
%endif
# end php-mapcache

%files perl
%doc README.md
%doc src/mapscript/perl/examples
%dir %{perl_vendorarch}/auto/mapscript
%{perl_vendorarch}/auto/mapscript/*
%{perl_vendorarch}/mapscript.pm

%if 0%{python_mapscript}
%files -n python3-mapserver
%doc src/mapscript/python/README.rst
%doc src/mapscript/python/examples
%doc src/mapscript/python/tests
%{python3_sitearch}/*mapscript*
%endif

%if %{with java}
%files java
%doc src/mapscript/java/README
%doc src/mapscript/java/examples
%doc src/mapscript/java/tests
%{_javadir}/*.jar
%{_libdir}/libjavamapscript.so
%endif

%files ruby
%doc src/mapscript/ruby/README
%doc src/mapscript/ruby/examples
%doc mapserver-ruby/README
%doc mapserver-ruby/examples
%{ruby_sitearchdir}/mapscript.so

%changelog
* Tue Sep 03 2024 Neil Hanlon <neil@shrug.pw> - 8.2.2-1
- update to 8.2.2

* Tue Aug 20 2024 Neil Hanlon <neil@shrug.pw> - 8.2.1-1
- update to 8.2.1
- bring in patch for zero-size malloc and buffer overflow

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 8.0.1-17
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.0.1-16
- Rebuilt for Python 3.13

* Mon May 13 2024 Sandro Mani <manisandro@gmail.com> - 8.0.1-15
- Rebuild (gdal)

* Tue Apr  9 2024 Remi Collet <remi@fedoraproject.org> - 8.0.1-14
- disable PHP extension on 32-bit
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0.1-11
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Wed Jan 03 2024 Florian Weimer <fweimer@redhat.com> - 8.0.1-10
- Fix C compatibility issue

* Wed Nov 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0.1-9
- Backport upstream patch for compilation with libxml2 2.12.0

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 8.0.1-8
- Rebuild (gdal)

* Tue Oct 03 2023 Sandro Mani <manisandro@gmail.com> - 8.0.1-7
- Fix implicit declarations of strlcat

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 8.0.1-6
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 8.0.1-4
- Perl 5.38 rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 8.0.1-3
- Rebuilt for Python 3.12

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 8.0.1-2
- Rebuild (gdal)

* Mon Apr 24 2023 Sandro Mani <manisandro@gmail.com> - 8.0.1-1
- Update to 8.0.1

* Thu Mar 09 2023 Sandro Mani <manisandro@gmail.com> - 8.0.0-7
- Fix php extension name in 40-mapserver.ini

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0.0-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 8.0.0-4
- Rebuild (gdal)

* Sun Oct 30 2022 Sandro Mani <manisandro@gmail.com> - 8.0.0-3
- Fix %%files for build with swig 4.1+

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 8.0.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Tue Sep 13 2022 Sandro Mani <manisandro@gmail.com> - 8.0.0-1
- Update to 8.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Sandro Mani <manisandro@gmail.com> - 7.6.4-18
- Limit -java subpackage to %%java_arches

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 7.6.4-17
- Rebuilt for Python 3.11

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 7.6.4-16
- Perl 5.36 rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 7.6.4-15
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Tue Mar 22 2022 Sandro Mani <manisandro@gmail.com> - 7.6.4-14
- It's no longer needed to move Python bindings with setuptools >= 60.x

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 7.6.4-13
- Rebuild for proj-9.0.0

* Mon Mar 07 2022 Karolina Surma <ksurma@redhat.com> - 7.6.4-12
- It's no longer needed to move Python bindings with setuptools >= 60.x

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 7.6.4-11
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.6.4-10
- F-36: rebuild against ruby31

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 7.6.4-8
- Adapt mapserver_php8.patch to drop TSRMLS_FETCH_FROM_CTX call

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 7.6.4-7
- Rebuild (gdal)

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 7.6.4-6
- Rebuilt for protobuf 3.19.0

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 7.6.4-5
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Tue Oct 26 2021 Adrian Reber <adrian@lisas.de> - 7.6.4-4
- Rebuilt for protobuf 3.18.1

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 7.6.4-3
- Rebuild (geos)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Sandro Mani <manisandro@gmail.com> - 7.6.4-1
- Update to 7.6.4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.6.3-3
- Rebuilt for Python 3.10

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.6.3-2
- Perl 5.34 re-rebuild updated packages

* Sat May 22 2021 Sandro Mani <manisandro@gmail.co;> - 7.6.3-1
- Update to 7.6.3

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 7.6.2-12
- Perl 5.34 rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 7.6.2-11
- Rebuild (gdal)

* Mon Mar 29 2021 Sandro Mani <manisandro@gmail.com> - 7.6.2-10
- Rebuild (proj)

* Tue Mar 23 2021 Sandro Mani <manisandro@gmail.com> - 7.6.2-9
- Bump

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 7.6.2-8
- Rebuild (proj)

* Fri Mar 05 2021 Sandro Mani <manisandro@gmail.com> - 7.6.2-7
- Rebuild (php)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 7.6.2-6
- Rebuild (geos)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 7.6.2-5
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 09:47:12 CET 2021 Adrian Reber <adrian@lisas.de> - 7.6.2-3
- Rebuilt for protobuf 3.14

* Thu Jan  7 2021 Vít Ondruch <vondruch@redhat.com> - 7.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 7.6.2-1
- Update to 7.6.2

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 7.6.1-1
- Update to 7.6.1

* Wed Nov 11 12:47:11 CET 2020 Sandro Mani <manisandro@gmail.com> - 7.4.3-11
- Rebuild (proj, gdal)

* Thu Oct 01 2020 Petr Pisar <ppisar@redhat.com> - 7.4.3-10
- Adapt to new CMake (bug #1864110)

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 7.4.3-9
- Rebuilt for protobuf 3.13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 7.4.3-6
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 7.4.3-5
- Perl 5.32 rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 7.4.3-4
- Rebuilt for protobuf 3.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.4.3-3
- Rebuilt for Python 3.9

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 7.4.3-2
- Rebuild (gdal)

* Wed Mar 04 2020 Sandro Mani <manisandro@gmail.com> - 7.4.3-1
- Update to 7.4.3

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 7.2.2-5.git7fe9b2b
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-4.git7fe9b2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-3.git7fe9b2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 7.2.2-2.git7fe9b2b
- Perl 5.30 rebuild

* Sun Feb 24 2019 Julien Enselme <jujens@jujens.eu> - 7.2.2-1.git7fe9b2b
- Update to 7.2.2

* Mon Feb 04 2019 Devrim Gündüs <devrim@gunduz.org> - 7.0.5-16.git208bb3a
- Rebuild for new GeOS and Proj

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-15.git208bb3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Julien Enselme <jujens@jujens.eu> - 7.0.5-14.git208bb3a
- Remove Python 2 mapscript support

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-13.git208bb3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 7.0.5-12.git208bb3a
- Perl 5.28 rebuild

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 7.0.5-11.git208bb3a
- Rebuild with new redhat-rpm-config/perl build flags
- Add "BuildRequires: perl-devel"

* Tue Feb 13 2018 Sandro Mani <manisandro@gmail.com> - 7.0.5-10.git208bb3a
- Rebuild (giflib)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-9.git208bb3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 05 2017 Julien Enselme <jujens@jujens.eu> - 7.0.5-8.git208bb3a
- Use mariadb-connector-c-devel openssl-devel (#1494098)

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.5-7.git208bb3a
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.5-6.git208bb3a
- Python 2 binary package renamed to python2-mapserver
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-5.git208bb3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-4.git208bb3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 7.0.5-3.git208bb3a
- Perl 5.26 rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.5-2.git208bb3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon May 15 2017 Julien Enselme <jujens@jujens.eu> - 7.0.5-1.git208bb3a
- Update to 7.0.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-3.gitb4bc015
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Devrim Gündüz <devrim@gunduz.org> - 7.0.4-2.gitb4bc015
- Rebuilt for Proj 4.9.3

* Thu Jan 19 2017 Julien Enselme <jujens@jujens.eu> - 7.0.4-1.gitb4bc015
- Update to 7.0.4

* Fri Jan 13 2017 Vít Ondruch <vondruch@redhat.com> - 7.0.3-2.git0f9ece8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Mon Dec 12 2016 Julien Enselme <jujens@jujens.eu> - 7.0.3-1.git0f9ece8
- Update to 7.0.3

* Wed Sep 21 2016 Julien Enselme <jujens@jujens.eu> - 7.0.2-1.git4ea78eb
- Update to 7.0.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.1-4.git6ae2bc6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Julien Enselme <jujens@jujens.eu> - 7.0.1-3.git6ae2bc6
- Disable PHP support.

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.0.1-2.git6ae2bc6
- Perl 5.24 rebuild

* Thu  Feb 25 2016 Julien Enselme <jujens@jujens.eu> - 7.0.1-1.git6ae2bc6
- Update to 7.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 30 2015 Peter Robinson <pbrobinson@fedoraproject.org> 6.2.2-7
- Rebuild again for GDAL 2.0

* Sun Aug 2 2015 Devrim Gündüz <devrim@gunduz.org> - 6.2.2-6
- Rebuilt for new gdal

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.2.2-4
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.2.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 11 2015 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.2.2-2
- Rebuilt for Proj 4.9.1
- Add patch for GCC5 build, also add -fPIC to CFLAGS
- Add a patch for swig 3.0.5

* Tue Dec 23 2014 Pavel Lisý <pali@fedoraproject.org> - 6.2.2-1
- Update to latest 6.2 release
- BZ 1048689 - CVE-2013-7262 mapserver: SQL injections with postgis TIME filters
- BZ 747409 - MapServer uses internal AGG and does not depend on agg-devel

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.2.1-10
- Perl 5.20 rebuild
- Regenerated the wrapper to work with new Perl

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Mat Booth <mat.booth@redhat.com> - 6.2.1-8
- Drop dep on gcj.

* Fri Jun 20 2014 Remi Collet <rcollet@redhat.com> - 6.2.1-7
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file
- add minimal PHP extension load test
- add upstream patch for PHP 5.6 (fix #1111478)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 6.2.1-5
- Rebuild for gdal 1.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 6.2.1-3
- Perl 5.18 rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 6.2.1-2
- rebuild for new GD 2.1.0

* Tue May 21 2013 Pavel Lisý <pali@fedoraproject.org> - 6.2.1-1
- Update to latest stable release
- BZ 910689 - dependency on bitstream-vera-sans-fonts changed to dejavu-sans-fonts
- BZ 960856 - Missing dependency: bitstream-vera-sans-fonts
- BZ 747421 - Move CGI executable from /usr/sbin to /usr/libexec
- BZ 796344 - Not compatible with JDK7
- BZ 846543 - mapserver-java is incorrectly packaged (missing required native library)
- trim of changelog

* Tue Apr 09 2013 Pavel Lisý <pali@fedoraproject.org> - 6.2.0-2
- changed MS_REL from 6x to 62

* Thu Apr 04 2013 Pavel Lisý <pali@fedoraproject.org> - 6.2.0-1
- Update to latest stable release
- dependency on bitstream-vera-sans-fonts replaced to dejavu-sans-fonts

* Mon Mar 25 2013 Oliver Falk <oliver@linux-kernel.at> - 6.0.3-10.1
- Rebuild - fix changelog (bogus date)

* Sat Mar 23 2013 Remi Collet <rcollet@redhat.com> - 6.0.3-10
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 6.0.3-8
- rebuild due to "jpeg8-ABI" feature drop

* Fri Oct 26 2012 Remi Collet <remi@fedoraproject.org> - 6.0.3-7
- conform to PHP Guidelines (#828161)
- add minimal load test for php extension

* Tue Oct 16 2012 Pavel Lisý <pali@fedoraproject.org> - 6.0.3-6
- temporary removed mapserver-java (mapscript) due to build problem
  with jdk7

* Fri Oct 12 2012 Pavel Lisý <pali@fedoraproject.org> - 6.0.3-5
- Merged from 6.0.3-4
- fix of build for php4 and swig > 2.0.4

* Tue Aug 14 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.0.3-4
- Rebuilt for new perl.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 6.0.3-2
- Perl 5.16 rebuild

* Sat Jun 30 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.0.3-1
- Update to 6.0.3, for various fixes described at:
  https://github.com/mapserver/mapserver/blob/rel-6-0-3-0/HISTORY.TXT
- Update URL, per bz #835426

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 6.0.2-2
- Perl 5.16 rebuild

* Mon Apr 16 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.0.2-1
- Update to 6.0.2, for various fixes described at:
  http://trac.osgeo.org/mapserver/browser/tags/rel-6-0-2/mapserver/HISTORY.TXT

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 6.0.1-4
- Rebuild for new libpng

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 6.0.1-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 6.0.1-2
- Perl mass rebuild

* Mon Jul 18 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 6.0.1-1
- Update to 6.0.1, for various fixes described at:
  http://trac.osgeo.org/mapserver/browser/tags/rel-6-0-1/mapserver/HISTORY.TXT
- Fixes bz #722545
- Apply changes to spec file for new major version.

