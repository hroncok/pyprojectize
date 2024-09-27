%global         sum Spreadsheet python library
%global         commit 98ab3e962ef31c04bba684c82888354eafb243a5
%global         git_tag 1.3.0
%global         shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-xlwt
Version:        1.3.0
Release:        13%{?dist}
Summary:        %{sum}

                # Utils.py is LPGL2.0+
# Automatically converted from old format: LGPLv2+ and BSD and BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising
URL:            http://pypi.python.org/pypi/xlwt
                # See also https://github.com/python-excel/xlwt
Source0:        https://github.com/python-excel/xlwt/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel


%description
A library for generating spreadsheet files that are compatible with
Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement
is Python 2.6 or later.


%package -n python3-xlwt
Summary:      %{sum}
              # https://github.com/python-excel/xlwt/issues/73
Provides:     bundled(antlr) = 2.7.7
%{?python_provide:%python_provide python3-xlwt}

%description -n python3-xlwt
A library for generating spreadsheet files that are compatible with
Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement
is Python 2.6 or later.


%prep
%autosetup -p1 -n xlwt-%{commit}
sed -i "s|tests/python.bmp|python.bmp|g" tests/test_bitmaps.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
cd tests
PYTHONPATH=.. %{__python3} -m unittest discover


%install
%pyproject_install
mkdir tmp_docs
cp -ar examples docs tmp_docs


%files -n python3-xlwt
%license docs/licenses.rst
%doc README.rst tmp_docs/*
%{python3_sitelib}/xlwt
%{python3_sitelib}/*.dist-info


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.0-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.0-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.3.0-1
- last released version
- drop obsolete patch

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.2-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-9
- Subpackage python2-xlwt has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Alec Leamas <leamas.alec@gmail.com> - 1.1.2-1
- New version
- Get sources from github instead of broken pypis source repos.
- Add patch from upstream to make tests run.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Alec Leamas <leamas.alec@gmail.com> - 1.0.0-2
- Add python3 subpackage

* Mon Jan 04 2016 Alec Leamas <leamas.alec@gmail.com> - 1.0.0-1
- Updating to new upstream.
- Remove upstreamed patch xlwt-fsf-address.
- Bundling antlr.py, the system one is unusable; upstream issue filed.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Rewriting license according to legal advice.
- Adding %%check

* Thu May 03 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Tentative rewrite of License tag (blocked on FE_LEGAL)
- Unbundle antlr
- Explicit naming of files in %%{python_sitelib}

* Thu May 03 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Fixing bad License:
- Fixing license file encoding.

* Wed May 02 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Initial release
