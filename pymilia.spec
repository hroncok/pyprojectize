
Name: pymilia
Version: 1.0.0
Release: 45%{?dist}
Summary: Python wrappers for milia
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later

URL: http://guaix.fis.ucm.es/projects/pymilia/wiki
Source0: ftp://astrax.fis.ucm.es/pub/software/pymilia/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: milia-devel >= 1.0.0

%global _description\
Python wrappers for milia. Milia is a C++ library created to\
compute cosmological distances and ages in the\
Friedmann-Lemaître-Robertson-Walker metric.

%description %_description

%package -n python3-pymilia
Summary: Python wrappers for milia
BuildRequires: python3-devel
BuildRequires: python3-Cython

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

%description -n python3-pymilia 
Python wrappers for milia. Milia is a C++ library created to 
compute cosmological distances and ages in the 
Friedmann-Lemaître-Robertson-Walker metric.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files milia

%files -n python3-pymilia -f %{pyproject_files}
%doc README.txt NEWS.txt
%license LICENSE.txt

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-45
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.0-43
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.0-39
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-36
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-33
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-30
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-28
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-27
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.0-24
- Drop python2 subpackage

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.0-23
- build requires c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-21
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-20
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-18
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-17
- Python 2 binary package renamed to python2-pymilia
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-14
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 28 2016 Kalev Lember <kalevlember@gmail.com> - 1.0.0-10
- Rebuilt for new milia

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.0-1
- New upstream source
- Adding support for python3

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.3.0-16
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.3.0-15
- Rebuild for Boost-1.53.0

* Mon Aug 13 2012 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-14
- Rebuilt for new boost 1.50

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 20 2012 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-12
- Rebuilt for new milia

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-10
- Rebuilt for new boost 1.48

* Tue Aug 23 2011 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-9
- Added filter to remove false provides

* Thu Apr 07 2011 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-8
- Rebuilt for new boost

* Thu Mar 17 2011 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-7
- Rebuilt for new boost

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.3.0-5
- rebuild for new boost

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jan 20 2010 Sergio Pascual <sergiopr at fedoraproject.com> - 0.3.0-3
- Adding CFLAGS in build line

* Wed Jan 20 2010 Sergio Pascual <sergiopr at fedoraproject.com> - 0.3.0-2
- Updated build requires
- Corrected minor typos

* Mon Jan 18 2010 Sergio Pascual <sergiopr at fedoraproject.com> - 0.3.0-1
- Initial spec file
