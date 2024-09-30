%global         gituser         CoreSecurity
%global         gitname         pcapy
%global         commit          b91a418374d1636408c435f11799ef725ef70097
%global         commitdate      20170116

%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         sum             A Python interface to libpcap

%global         with_tests      0



Name:           pcapy
Version:        0.11.5
Release:        25%{?dist}
Summary:        %{sum}

License:        Apache-1.1
URL:            https://www.coresecurity.com/corelabs-research/open-source-tools/pcapy
#               http://oss.coresecurity.com/projects/pcapy.html
#               https://github.com/CoreSecurity/pcapy/releases
#Source0:       https://github.com/%%{gituser}/%%{gitname}/archive/%%{commit}/%%{name}-%%{version}-%%{shortcommit}.tar.gz
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{version}.tar.gz#/%{gitname}-%{version}.tar.gz

# Fix FTBFS issue with setuptools >= 61.0.0
# Upstream issue: https://github.com/helpsystems/pcapy/issues/73
# Fix backported from the fork: https://github.com/stamparm/pcapy-ng/commit/84a15d2faefaae410198f5739d6ed3c69daa17ec
Patch0:         fix-setuptools-build.patch
Patch1:         py_ssize_t.patch
Patch2:         py313.patch

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  libpcap-devel

%description
Pcapy is a Python extension module that interfaces with the libpcap
packet capture library. Pcapy enables python scripts to capture packets
on the network. Pcapy is highly effective when used in conjunction with 
a packet-handling package such as Impacket, which is a collection of 
Python classes for constructing and dissecting network packets.



#===== the python3 package definition
%package -n python3-%{gitname}
Summary:        %{sum}


%description -n python3-%{gitname}
Python3 package of %{gitname}.
Pcapy is a Python extension module that interfaces with the libpcap
packet capture library. Pcapy enables python scripts to capture packets
on the network. Pcapy is highly effective when used in conjunction with
a packet-handling package such as Impacket, which is a collection of
Python classes for constructing and dissecting network packets.



%prep
%setup -q

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

#fix encodings
sed -i 's/\r//' LICENSE
sed -i 's/\r//' README
sed -i 's/\r//' pcapy.html
iconv -f IBM850 -t UTF8 pcapy.html > pcapy.html.tmp
mv pcapy.html.tmp pcapy.html


%install
%pyproject_install
%pyproject_save_files '*'

rm -rf %{buildroot}/usr/share/doc/pcapy

%files -n python3-%{gitname} -f %{pyproject_files}
%license LICENSE
%doc README pcapy.html


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.11.5-24
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.11.5-21
- Patch for Python 3.13.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.11.5-19
- Rebuilt for Python 3.12

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.11.5-18
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.11.5-16
- Patch for Python 3.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.11.5-14
- Fix FTBFS issue with the latest setuptools
- Resolves: rhbz#2097119

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.11.5-13
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.11.5-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.11.5-7
- BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.5-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.11.5-4
- Drop Python 2.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.11.5-1
- 0.11.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-2
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.11.4-1
- 0.11.4

* Sun Mar 11 2018 Michal Ambroz <rebus _AT seznam.cz> - 0.11.1-1
- bump to version 0.11.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.8-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10.8-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Jon Ciesla <limburgher@gmail.com> - 0.10.8-1
- Latest upstream, BZ 901992.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Jon Ciesla <limburgher@gmail.com> - 0.10.5-10
- Fixed file listing.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.5-4
- Rebuild for Python 2.6

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 0.10.5-3
- GCC 4.3 rebuild.

* Thu Jan 03 2008 Jon Ciesla <limb@jcomserv.net> - 0.10.5-2
- Fixed file listing.

* Thu Nov 29 2007 Jon Ciesla <limb@jcomserv.net> - 0.10.5-1
- create.
