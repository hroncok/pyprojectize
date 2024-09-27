# whether to do a verbose build
%bcond_without verbose_build
%if %{with verbose_build}
%global _verbose -v
%else
%global _verbose %{nil}
%endif

Name:           aubio
Version:        0.4.9
Release:        24%{?dist}
Summary:        An audio labeling tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://aubio.org/
Source0:        https://aubio.org/pub/aubio-%{version}.tar.bz2
Patch0:         %{name}-unversioned-python.patch
Patch1:         %{name}-python39.patch
Patch2:         %{name}-invalid-escape-sequence.patch
Patch3:         %{name}-imp-removed.patch
Patch4:         0001-py-add-const-qualifiers-to-ufuncs-prototypes-for-lat.patch

BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  python3-numpy
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  txt2man

Requires:       %{name}-python3 = %{version}-%{release}

%global _description %{expand:
aubio is a tool and library for audio labeling. Its features include
segmenting a sound file before each of its attacks, performing pitch
detection, tapping the beat and producing midi streams from live
audio. The name aubio comes from 'audio' with a typo: several
transcription errors are likely to be found in the results too.

The aim of this project is to provide these automatic labeling
features to other audio software. Functions can be used offline in
sound editors and software samplers, or online in audio effects and
virtual instruments.}

%description %_description

This package contains the aubio tool.

%package        lib
Summary:        An audio labeling library

%description    lib %_description

This package contains the aubio library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python3
Summary:        Python 3 language bindings for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python3

%description    python3
The %{name}-python3 package contains the Python 3 language bindings for
%{name}.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%set_build_flags

%{python3} ./waf configure \
    --prefix="%_prefix" \
    --bindir="%_bindir" \
    --sysconfdir="%_sysconfdir" \
    --datadir="%_datadir" \
    --includedir="%_includedir" \
    --libdir="%_libdir" \
    --mandir="%_mandir" \
    --docdir="%_docdir" \
    --enable-fftw3f \
    --enable-complex \
    --enable-jack \
    --enable-samplerate

%{python3} ./waf build %{_verbose} %{?_smp_mflags}

%pyproject_wheel

%install
%{python3} ./waf --destdir=%{buildroot} %{_verbose} install
rm -f %{buildroot}%{_libdir}/*.a
rm -rf libaubio-doc
cp -r %{buildroot}%{_docdir}/libaubio-doc libaubio-doc
rm -rf %{buildroot}%{_docdir}/libaubio-doc

%pyproject_install

# Remove shebang from python files
sed -i -e '/^#![[:blank:]]*\//, 1d' %{buildroot}%{python3_sitearch}/%{name}/*.py

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/*
%{_mandir}/man1/*

%files lib
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc libaubio-doc/api
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/aubio

%files python3
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}*.dist-info

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.9-24
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.4.9-22
- Rebuilt for Python 3.13

* Wed Mar 20 2024 Nils Philippsen <nils@tiptoe.de> - 0.4.9-21
- Fix building on F40+ (rhbz#2260997)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.4.9-18
- Fix FTBFS with Python 3.12 #2219938

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.9-16
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.9-13
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.9-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Nils Philippsen <nils@tiptoe.de> - 0.4.9-8
- Split off aubio-lib subpackage
- Require Python subpackage from main package
- Require arch-specific -lib subpackage from -devel

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.4.9-6
- Fix FTBFS with Python 3.9 (#1804725)

* Fri Feb 14 2020 Petr Viktorin <pviktori@redhat.com> - 0.4.9-5
- Use Python 3 to build

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.4.9-1
- Update to 0.4.9
- Some spec cleanup
- CVE-2018-19800 prevent a possible buffer overflow in new_aubio_tempo
- CVE-2018-19801 prevent a null-pointer dereference in new_aubio_filterbank
- CVE-2018-19802 prevent a null-pointer dereference in new_aubio_onset

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-2
- Remove Python 2 subpackage (#1628183)

* Wed Jul 25 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.6-1
- version 0.4.6

* Tue Jul 24 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.2-11
- BR: /usr/bin/python on Fedora 29 and later
- explicitly require gcc for building

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-9
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Nils Philippsen <nils@tiptoe.de> - 0.4.2-1
- version 0.4.2
- new license: GPLv3+
- use %%autosetup macro
- remove some old cruft
- waf: build verbosely
- rename python subpackage to python2, add python3 subpackage
- many Python fixes, especially for Python 3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Feb 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.2-8
- Fix DSO-linking failure
- Fix byte-compilation failure

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.2-5
- Rebuild for Python 2.6

* Sun Jul 13 2008 Anthony Green <green@redhat.com> 0.3.2-4
- BuildRequire python-devel.

* Sun Jul 13 2008 Anthony Green <green@redhat.com> 0.3.2-3
- Fix python package installation.

* Sun Jul 13 2008 Anthony Green <green@redhat.com> 0.3.2-2
- Untabify.
- Don't use rpath.
- Add python subpackage.

* Thu Jul 10 2008 Anthony Green <green@redhat.com> 0.3.2-1
- Created.
