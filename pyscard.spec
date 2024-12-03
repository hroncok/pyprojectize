Name:           pyscard
Version:        2.0.5
Release:        9%{?dist}
Summary:        A framework for building smart card aware applications in Python


# The entire source code is LGPLv2+ except for ClassLoader.py (Python),
# and Synchronization.py, Observer.py (CC-BY-SA 3.0), according to
# http://sourceforge.net/p/pyscard/code/619/

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/LudovicRousseau/pyscard
Source0:        https://github.com/LudovicRousseau/pyscard/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pcsc-lite-devel
BuildRequires:  swig >= 1.3.31

%description
The pyscard smartcard library is a framework for building smart card aware
applications in Python. The smartcard module is built on top of the PCSC API
Python wrapper module.

%package -n python%{python3_pkgversion}-%{name}
Summary:        A framework for building smart card aware applications in Python
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       pcsc-lite

%description -n python%{python3_pkgversion}-%{name}
The pyscard smartcard library is a framework for building smart card aware
applications in Python. The smartcard module is built on top of the PCSC API
Python wrapper module.

This is the python3 package.

%prep
%setup -q
# license file is CRLF terminated -- prevent a rpmlint warning
#sed -i 's/\r//' LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l smartcard
chmod 755 %{buildroot}%{python3_sitearch}/smartcard/scard/*.so


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-%{name} -f %{pyproject_files}
%doc ACKS README.md
%doc smartcard/doc/*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.5-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.5-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.5-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 23 2022 Orion Poplawski <orion@nwra.com> - 2.0.5-1
- Update to 2.0.5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.3-2
- Rebuilt for Python 3.11

* Tue May 31 2022 Orion Poplawski <orion@nwra.com> - 2.0.3-1
- Update to 2.0.3
- New URL

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.7-12
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.9.7-11
- remove %{python3_other_version} ifs
- explicitly buildrequire python3-setuptools

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.7-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.7-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.7-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.7-2
- Subpackage python2-pyscard has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Nov 16 2018 Orion Poplawski <orion@nwra.com> - 1.9.7-1
- Update to 1.9.7
- Drop python2 on Fedora 30+, RHEL 8+ (BZ# 1634871)
- Support python3 on EPEL (BZ# 1540752)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.5-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.5-6
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.5-5
- Python 2 binary package renamed to python2-pyscard
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Seth Jennings <sethdjennings@gmail.com> - 1.9.5-2
- upstream release 1.9.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Aug 31 2015 Seth Jennings <spartacus06@gmail.com> 1.9.0-2
- New subpackage for python3 build

* Fri Aug 14 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> 1.9.0-1
- New upstream release
- Built with python3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> 1.6.16-2
- Clarified licenses.

* Fri Aug 01 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> 1.6.16-1
- New (unofficial) release.

* Fri Jan 21 2011 Andrew Elwell <andrew.elwell@gmail.com> 1.6.12-4
- Rebuilt to address comments in package review (bug #663102)

* Fri Jan 14 2011 Andrew Elwell <andrew.elwell@gmail.com> 1.6.12-3
- Added missing BuildRequres on swig.

* Thu Dec 16 2010 Andrew Elwell <andrew.elwell@gmail.com> 1.6.12-2
- Corrected CFLAGS in build.

* Tue Dec 14 2010 Andrew Elwell <andrew.elwell@gmail.com> 1.6.12-1
- Initial package of 1.6.12 from upstream.
