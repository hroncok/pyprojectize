%global oname   exif-py

Summary:        Python module to extract EXIF information
Name:           python-exif
Version:        3.0.0
Release:        11%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ianare/exif-py
Source0:        https://github.com/ianare/%{oname}/archive/%{version}/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
Python Library to extract EXIF information in digital camera image files.

%description %_description

%package -n    python3-exif
Summary:       Python 3 module to extract EXIF information
%description -n python3-exif %_description

%prep
%setup -q -n %{oname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files exifread
ln -s EXIF.py %{buildroot}%{_bindir}/EXIF

%files -n python3-exif -f %{pyproject_files}
%license LICENSE.txt
%doc ChangeLog.rst README.rst
%{_bindir}/EXIF
%{_bindir}/EXIF.py

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.11

* Sun May 08 2022 Terje Rosten <terje.rosten@ntnu.no> - 3.0.0-1
- 3.0.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.3.2-1
- 2.3.2

* Sun Oct 11 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.3.1-1
- 2.3.1

* Fri Jul 31 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.2.1-1
- 2.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-3
- Drop Python 2 support in newer Fedoras

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-1
- 2.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-10
- Make Python 3 default

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.2-8
- Python 2 binary package renamed to python2-exif
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 20 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-1
- 2.1.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.1.1-1
- 2.1.1

* Mon Apr 13 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.0.2-1
- 2.0.2
- Add python3 sub package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Terje Rosten <terje.rosten@ntnu.no> - 1.4.2-1
- 1.4.2
- Fix github source url

* Tue Oct 22 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.4.1-1
- 1.4.1

* Tue Aug 13 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.3.3-1
- 1.3.3, (fixing bz #996583)
- Project has moved to github

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Terje Rosten <terjeros@phys.ntnu.no> - 1.1.0-1
- 1.1.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.8-2
- Rebuild for Python 2.6

* Fri Aug 15 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.8-1
- 1.0.8

* Mon Mar  3 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-4
- Fix script (bz #435758)

* Mon Feb 11 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-3
- Add script and changes.txt

* Sat Jan 19 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-2
- Improve setup.py

* Thu Jan  3 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-1
- 1.0.7
- Include egg info

* Mon Nov 19 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.5-1
- 1.0.5

* Mon Aug 06 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.2-3
- Tagging...

* Mon Aug 06 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.2-2
- Fix typo in url
- Add python-devel to buildreq
- Add license to setup.py
- Strip code from %%doc file
- Fix typo in sitelib macro

* Sat Aug 04 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.2-1
- Initial build

