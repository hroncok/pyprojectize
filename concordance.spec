%global libpkg libconcord

Name: concordance
Version: 1.5
Release: 11%{?dist}
Summary: Software to program the Logitech Harmony remote control

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.phildev.net/concordance/
Source0: https://github.com/jaymzh/concordance/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: hidapi-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libcurl-devel
BuildRequires: libtool
BuildRequires: libzip-devel
BuildRequires: make
Requires: %{libpkg} = %{version}-%{release}

%description
This software will allow you to program your Logitech Harmony universal
remote control.


%package -n %{libpkg}
Summary: Library to talk to Logitech Harmony universal remote controls
Requires: udev
# For usbnet-based remotes: 900, 1000, 1100
Requires: dnsmasq

%description -n %{libpkg}
Library to talk to Logitech Harmony universal remote controls


%package -n %{libpkg}-devel
Summary: Development libraries for libconcord
Requires: %{libpkg} = %{version}-%{release}

%description -n %{libpkg}-devel
Development libraries for libconcord


%package -n python3-%{libpkg}
Summary: Python 3 bindings for libconcord
Requires: %{libpkg} = %{version}-%{release}
BuildArch: noarch

%description -n python3-%{libpkg}
Python 3 bindings for libconcord


%prep
%setup -q


%build
cd %{libpkg}

%configure --disable-static --disable-mime-update
make %{_smp_mflags}
cd -

# python bindings
cd %{libpkg}/bindings/python
%py3_build
cd -

cd %{name}
export CFLAGS="%{optflags} -I../libconcord"
export LDFLAGS="%{__global_ldflags} -L../libconcord/.libs"
%configure --enable-shared
make %{_smp_mflags}


%install
cd %{libpkg}
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install_udev

find %{buildroot} -type f -name \*.a -exec %{__rm} -f {} \;
find %{buildroot} -type f -name \*.la -exec %{__rm}  -f {} \;
cd -

# python bindings
cd %{libpkg}/bindings/python
%py3_install
cd -

cd %{name}
make DESTDIR=%{buildroot} install


%files
%doc Changelog CodingStyle LICENSE SubmittingPatches TODO 
%doc README.md %{name}/INSTALL.linux
%attr(0755, root, root) %{_bindir}/*
%{_mandir}/man1/*

%files -n %{libpkg}
%doc Changelog CodingStyle LICENSE SubmittingPatches
%doc %{libpkg}/README %{libpkg}/INSTALL.linux
/lib/udev/rules.d/*.rules
/lib/udev/*.sh
%{_datadir}/mime/packages/%{libpkg}.xml
%{_libdir}/*.so.*

%files -n %{libpkg}-devel
%doc TODO
%{_includedir}/*.h
%{_libdir}/*.so

%files -n python3-%{libpkg}
%doc %{libpkg}/bindings/python/README
%{python3_sitelib}/*


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5-9
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5-2
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Scott Talbert <swt@techie.net> - 1.5-1
- Update to new upstream release 1.5 (#2079624)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Scott Talbert <swt@techie.net> - 1.4-1
- Update to new upstream release 1.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-10
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Scott Talbert <swt@techie.net> - 1.3-7
- Revert obsolete as it is being done in fedora-obsolete-packages

* Thu Sep 20 2018 Adam Williamson <awilliam@redhat.com> - 1.3-6
- Have python3-libconcord obsolete python2-libconcord
  This should work for most users as congruity switched

* Tue Sep 11 2018 Scott Talbert <swt@techie.net> - 1.3-5
- Remove use of Group tag

* Mon Sep 10 2018 Scott Talbert <swt@techie.net> - 1.3-4
- Remove Python 2 bindings

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-2
- Rebuilt for Python 3.7

* Sun Jun 10 2018 Scott Talbert <swt@techie.net> - 1.3-1
- New upstream release 1.3
- Remove perl bindings subpackage (unused)
- Remove old Provides/Obsoletes
- Build subpackage for Python 3 bindings
- Remove scriptlets that are no longer needed

* Mon Feb 19 2018 Scott Talbert <swt@techie.net> - 1.2-18
- Add missing BR for gcc and gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-14
- Perl 5.26 rebuild

* Fri Mar 03 2017 Scott Talbert <swt@techie.net> - 1.2-13
- Rebuild for libzip 1.2.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-10
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Scott Talbert <swt@techie.net> - 1.2-8
- Removed superfluous defattrs

* Mon Jan 04 2016 Scott Talbert <swt@techie.net> - 1.2-7
- Modernize python packaging, libconcord-python -> python2-libconcord

* Sun Dec 27 2015 Scott Talbert <swt@techie.net> - 1.2-6
- Replace define macros with global ones

* Sat Sep 19 2015 Scott Talbert <swt@techie.net> - 1.2-5
- Fixed LDFLAGS so that hardening flags will be included

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-3
- Perl 5.22 rebuild

* Thu May 07 2015 Remi Collet <remi@fedoraproject.org> - 1.2-2
- rebuild for new libzip

* Sun Apr 19 2015 Scott Talbert <swt@techie.net> - 1.2-1
- New upstream release 1.2, RHBZ #1209465

* Sat Apr 04 2015 Scott Talbert <swt@techie.net> - 1.1-7
- Merged libconcord package into concordance package

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Scott Talbert <swt@techie.net> - 1.0-3
- New upstream release 1.1
- Removed items no longer required in recent Fedoras

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Adam Williamson <awilliam@redhat.com> - 1.0-1
- new upstream release 1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Adam Williamson <awilliam@redhat.com> - 0.23-1
- bump to 0.23

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Douglas E. Warner <silfreed@silfreed.net> 0.21-1
- moved udev/policykit rules to libconcord package
- supports flashing 5** remotes
- improved IR learning support

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Douglas E. Warner <silfreed@silfreed.net> 0.20-5
- removing registered marks

* Sat May 03 2008 Douglas E. Warner <silfreed@silfreed.net> 0.20-4
- adding additional docs
- removed harmony provides/obsoletes
- removing private getopt sources
- removing udev/pam_console rules
- running generated xml file through xmllint at build time

* Tue Apr 22 2008 Douglas E. Warner <silfreed@silfreed.net> 0.20-3
- fixed Source0 url to downloads.sourceforge.net instead of dl.sourceforge.net

* Tue Apr 22 2008 Douglas E. Warner <silfreed@silfreed.net> 0.20-2
- fixed Source0 url
- changing to build/install dir rather than setting it in setup macro
- install using autoconf script

* Mon Apr 21 2008 Douglas E. Warner <silfreed@silfreed.net> 0.20-1
- updating to 0.20

* Fri Mar 21 2008 Douglas E. Warner <silfreed@silfreed.net> 0.20-0.2.20080318cvs
- disable static linking against libconcord

* Tue Mar 18 2008 Douglas E. Warner <silfreed@silfreed.net> 0.20-0.1.20080318cvs
- renamed from harmony to concordance
- update to pre-release 0.20 that works with libconcord
- adding BuildRequires libconcord-devel
- adding Obsoletes harmony <= 0.20 and Provides harmony to provide upgrade
  path

* Mon Mar 03 2008 Douglas E. Warner <silfreed@silfreed.net> 0.13-1
- update to 0.13

* Mon Jan 14 2008 Douglas E. Warner <silfreed@silfreed.net> 0.12-1
- update to 0.12

* Fri Oct 12 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-8
- moving udev/PolicyKit generation from install to build

* Fri Oct 12 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-7
- fixed typo in harmony-gen-policykit-rules.sh

* Fri Oct 12 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-6
- generating udev rules at build time
- updated udev rules to include more devices
- generating and packaging PolicyKit rules

* Fri Oct 12 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-5
- fixing udev rules path

* Fri Oct 12 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-4
- including license.txt in doc
- switching defattr from (-, root, root, -) to (0644, root, root, 0755)
  and attr(0755) the binary

* Fri Oct 12 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-3
- removing examples from docs
- installing binary by hand to bindir instead of sbindir
- removed commented epoch
- added ® where appropriate
- reordered elements of spec file; updated buildroot
- added udev rules for creating symlinks with nicer names
- added pam_console perms for setting devices to current user

* Thu Oct 11 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-2
- removing bogus Requires: ldconfig
- adding BuildRequies: libusb-devel

* Wed Oct 10 2007 Douglas E. Warner <silfreed@silfreed.net> 0.11-1
- Initial RPM release.

