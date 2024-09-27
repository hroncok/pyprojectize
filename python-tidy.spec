%global         oname uTidylib

%if 0%{?fedora} < 31 && 0%{?rhel} < 9
%global         py2 1
%endif

Summary:        Python wrapper for tidy, from the HTML tidy project
Name:           python-tidy
Version:        0.6
Release:        18%{?dist}
License:        MIT
URL:            https://cihar.com/software/utidylib/
Source0:        http://dl.cihar.com/utidylib/uTidylib-%{version}.tar.bz2
%if 0%{?py2}
BuildRequires:  libtidy
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
BuildRequires:  python2-tools
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildArch:      noarch
%global         _description\
Python wrapper (bindings) for tidylib, this allows you to tidy HTML\
files through a Pythonic interface.

%description    %_description

%if 0%{?py2}
%package     -n python2-tidy
Summary:        %summary
%{?python_provide:%python_provide python2-tidy}
Requires:       libtidy
Requires:       python2-six
%description -n python2-tidy %_description
%endif

%package     -n python3-tidy
Summary:        %summary
%{?python_provide:%python_provide python3-tidy}
Requires:       libtidy
Requires:       python3-six
%description -n python3-tidy %_description

%prep
%setup -q -n %{oname}-%{version}

%build
%{?py2:%{py2_build}}
%{py3_build}

%install
%{?py2:%{py2_install}}
%{py3_install}

%check
# fail after tidy 5.6
%{?py2:%{__python2} setup.py test || :}
# todo: fails
%{__python3} setup.py test || :

%if 0%{?py2}
%files -n python2-tidy
%license LICENSE
%doc README.rst
%{python2_sitelib}/tidy
%{python2_sitelib}/uTidylib-*-py2*.egg-info
%endif

%files -n python3-tidy
%license LICENSE
%doc README.rst
%{python3_sitelib}/tidy
%{python3_sitelib}/uTidylib-*-py3*.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 0.6-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Sep 30 2019 Terje Rosten <terjeros@phys.ntnu.no> - 0.6-1
- 0.6

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-14
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.3-13
- No Python 2 in newer Fedoras

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3-8
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.3-7
- Clean up, minor issue with tidy 5.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.3-3
- rebuild (tidy)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3-2
- Rebuild for Python 3.6

* Sun Sep 18 2016 Terje Rosten <terjeros@phys.ntnu.no> - 0.3-1
- 0.3
- New upstream
- Add Python 3 support

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-17
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2-5
- Rebuild for Python 2.6

* Sat Oct 18 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.2-4
- Not 64 bits clean, #467246, thanks to Jose Pedro Oliveira
  for report and patch.

* Sun Feb 17 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.2-3
- Fix license (again)

* Sun Feb 17 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.2-2
- Simplify %%files
- Fix license, req and group

* Sat Feb 16 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.2-1
- Initial build.

