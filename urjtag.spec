%if 0%{?centos} > 6 || 0%{?rhel} > 6 || 0%{?fedora}
%global with_python3 1
%else
%global without_python3 1
%endif

Name:           urjtag
Version:        2021.03
Release:        14%{?dist}
Summary:        A tool for communicating over JTAG with flash chips and CPUs

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://urjtag.org
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:         %{name}-fixarm.patch

%global py3_prefix python3

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libftdi-devel
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  readline-devel
BuildRequires:  swig
%if 0%{?rhel} || 0%{?centos}
BuildRequires: %{py3_prefix}4-devel
%else
BuildRequires: %{py3_prefix}-devel
%endif
BuildRequires:  bison
BuildRequires:  flex

%description
UrJTAG aims to create an enhanced, modern tool for communicating
over JTAG with flash chips, CPUs, and many more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n %{py3_prefix}-%{name}
%if 0%{?rhel} || 0%{?centos}
Provides:       python3-%{name}
%else
%{?python_provide:%python_provide %{py3_prefix}-%{name}}
%endif
Summary:        Python bindings for %{name}
Requires:       %{name} = %{version}-%{release}

%description    -n %{py3_prefix}-%{name}
Python bindings and examples for %{name}.

%prep
%setup -q
%patch -P0 -p2 -b .armfix

%build
%configure --enable-jedec-exp --enable-stapl --enable-bsdl --enable-svf --disable-static --enable-shared
# V=1: verbose build, disables AM_SILENT_RULES
%{__make} %{?_smp_mflags} V=1
pushd bindings/python/
%py3_build

%install
# cd urjtag
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
%find_lang %{name}
pushd bindings/python/
%py3_install

%ldconfig_scriptlets
 
%files -f %{name}.lang
%doc README NEWS ChangeLog COPYING AUTHORS
%doc doc/howto_add_support_for_more_flash.txt
%doc doc/README.ejtag doc/README.pld doc/README.stapl
%doc doc/UrJTAG.txt
%{_bindir}/jtag
%{_bindir}/bsdl2jtag
%{_libdir}/liburjtag.so.*
%dir %{_datadir}/urjtag/
%{_datadir}/urjtag/*
%{_mandir}/man1/jtag.1*
%{_mandir}/man1/bsdl2jtag.1*

%files devel
%dir %{_includedir}/urjtag
%{_includedir}/urjtag/*.h
%{_libdir}/liburjtag.so
%{_libdir}/pkgconfig/urjtag.pc

%files -n %{py3_prefix}-%{name}
%{python3_sitearch}/urjtag*
%doc doc/urjtag-python.txt 
%doc bindings/python/t_urjtag_chain.py
%doc bindings/python/t_srst.py

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2021.03-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2021.03-12
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 30 2023 Filipe Rosset <rosset.filipe@gmail.com> - 2021.03-10
- Fix FTBFS rhbz#2226495 rhbz#2220616 rhbz#2175186 and rhbz#1785878

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2021.03-8
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2021.03-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2021.03-2
- Rebuilt for Python 3.10

* Sat Apr 10 2021 Jiri Kastner <jkastner@fedoraproject.org> - 2021.03-1
- update to 2021.03

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.12-4
- Rebuilt for Python 3.9

* Thu Feb 13 2020 Dan Horák <dan[at]danny.cz> - 2019.12-3
- fix FTBFS with gcc10 (#1793499)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Dan Horák <dan[at]danny.cz> - 2019.12-1
- update to 2019.12

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.09-2
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Dan Horák <dan[at]danny.cz> - 2018.09-1
- update to 2018.09

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.06-4
- Remove python2 subpackage (#1628187)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.06-2
- Rebuilt for Python 3.7

* Mon Jun 25 2018 Jiri Kastner <jkastner@redhat.com> - 2018.06-1
- update to 2018.06

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.10-3
- Rebuilt for Python 3.7

* Thu Mar 22 2018 Jiri Kastner <jkastner@redhat.com> - 2017.10-2
- revert back armfix patch

* Thu Mar 22 2018 Jiri Kastner <jkastner@redhat.com> - 2017.10-1
- update to release 2017.10
- enabled experimental jedec flash detection
- added python3

* Thu Mar 01 2018 Jiri Kastner <jkastner@redhat.com> - 0.10-22.20171020git49a4f5b5
- added bison and flex for bsdl2jtag command
- updated to latest master

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10-21.20111215gite1a4227
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10-19.20111215gite1a4227
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10-18.20111215gite1a4227
- Python 2 binary package renamed to python2-urjtag
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10-14.20111215gite1a4227
- Rebuild for readline 7.x

* Fri Dec  9 2016 Jiri Kastner <jkastner@fedoraproject.org> - 0.10-13.20111215gite1a4227
- libftdi is not detected as it is libftdi1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-12.20111215gite1a4227
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.10-9.20111215gite1a4227
- Add patch to fix FTBFS on ARMv7

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Scott Tsai <scottt.tw@gmail.com> - 0.10-6.20111215gite1a4227
- Rebuilt for libftdi soname bump

* Wed Oct  9 2013 Shakthi Kannan <shakthimaan@fedoraproject.org>  - 0.10-5.20111215gite1a4227
- ExcludeArch armv7hl

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3.20111215gite1a4227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Dec 15 2011 Scott Tsai <scottt.tw@gmail.com> 0.10-2.20111215gite1a4227
- Initial RPM release
