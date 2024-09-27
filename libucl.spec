Name:           libucl
Version:        0.8.2
Release:        8%{?dist}
Summary:        Universal configuration library parser

# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/vstakhov/libucl
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libtree-devel
BuildRequires:  make
BuildRequires:  mum-hash-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Partial http://troydhanson.github.io/uthash (BSD) - 2.x is shipped in Fedora.
Provides: bundled(uthash) = 1.9.8

# Partial and patched https://github.com/attractivechaos/klib (MIT).
# Upstream is not released as a single archive and only provide per-file
# versioning.
Provides: bundled(klib)

%description
%{summary}.

%package        devel
Summary:        libucl development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%package     -n python3-libucl
Summary:        Python bindings for libucl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-libucl
%{summary}.

%prep
%autosetup

# pkg-config: remove trailing slash from standard include dir.
sed -i 's/includedir}\/$/includedir}/' libucl.pc.in

# Remove bundled libraries.
sed -i '/mum\.h/d' src/Makefile.am
sed -i '/tree\.h/d' src/Makefile.am
sed -i 's/ucl_chartable.h \\/ucl_chartable.h/' src/Makefile.am
rm src/mum.h src/tree.h

# Set include/lib dir for python bindings.
sed -i "s%language = 'c'%language = \'c\', include_dirs = [ \"../include\"],  library_dirs = [ \"../src/.libs\"]%" python/setup.py

# Remove network-dependent tests.
for def in schema/ref.json schema/refRemote.json schema/definitions.json; do
  rm tests/$def
done

%build
# Run autoconf.
./autogen.sh

%configure --disable-static

V=1 %make_build
(cd python; %py3_build)

%install
%make_install
(cd python; %py3_install)

# Remove useless la file (SHOULD NOT be included per Fedora packaging
# policies).
rm %{buildroot}%{_libdir}/%{name}.la

%check
%make_build check

%files
%license COPYING
%doc README.md
%{_libdir}/libucl.so.*
%{_mandir}/man3/libucl.3*

%files devel
%{_libdir}/pkgconfig/libucl.pc
%{_libdir}/libucl.so
%{_includedir}/ucl*

%files -n python3-libucl
%{python3_sitearch}/ucl*

%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.2-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.2-6
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.12

* Sun Apr 30 2023 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.1-11
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.1-8
- Rebuilt for Python 3.10

* Fri Apr 09 2021 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-7
- Add missing python3-devel dependency.
- Fix include and lib dirs when building python subpackage.

* Wed Mar 24 2021 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-6
- Unbundle mum-hash and libtree.

* Sat Mar 06 2021 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-5
- Mark bundled libraries and adapt license.
- Package Python bindings.

* Sun Dec 27 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-4
- Remove statically compiled output and .la libtool file from devel subpackage.
- Move check section after install section.
- Patch pkgconfig includes.

* Sun Dec 27 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-3
- Run test suite in check section.
- Make devel subpackage requires on base package arch-dependent.

* Sun Apr 19 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-2
- Build with automake instead of incomplete Makefile.unix

* Mon Feb 24 2020 Timothée Floure <fnux@fedoraproject.org> - 0.8.1-1
- Let there be package.
