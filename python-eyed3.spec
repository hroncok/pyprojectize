%global srcname eyed3

Name:           python-%{srcname}
Version:        0.9.7
Release:        7%{?dist}
Summary:        Python audio data toolkit (ID3 and MP3)
License:        GPL-3.0-or-later
URL:            https://github.com/nicfit/eyeD3
Source0:        https://github.com/nicfit/eyeD3/releases/download/v%{version}/eyeD3-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-deprecation
BuildRequires:  python3-filetype
# Test dependencies.
BuildRequires:  python3-factory-boy
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-six

%global _description\
A Python module and program for processing ID3 tags. Information about\
mp3 files(i.e bit rate, sample frequency, play time, etc.) is also\
provided. The formats supported are ID3 v1.0/v1.1 and v2.3/v2.4.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
Requires:       python3-six

%description -n python3-%{srcname} %_description


%prep
%autosetup -n eyeD3-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
# Ignore tests which require:
# - test data (test_classic_plugin.py, test_core.py, id3/test_frames.py,
# id3_test_rva.py, test_issues.py)
py.test-%{python3_version} --ignore=tests/{test_classic_plugin.py,test_core.py,id3/test_frames.py,test_jsonyaml_plugin.py,id3/test_rva.py,test_issues.py}


%files -n python3-%{srcname}
%doc AUTHORS.rst HISTORY.rst README.rst examples/
%license LICENSE
%{_bindir}/eyeD3
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/eyed3-%{version}.dist-info/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.7-6
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Maxwell G <maxwell@gtmx.me> - 0.9.7-5
- Remove unused python3-mock test dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 David King <amigadave@amigadave.com> - 0.9.7-1
- Update to 0.9.7

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.9.6-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.6-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 David King <amigadave@amigadave.com> - 0.9.6-1
- Update to 0.9.6

* Tue Oct 13 2020 David King <amigadave@amigadave.com> - 0.9.5-1
- Update to 0.9.5 (#1887706)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-8
- Subpackage python2-eyed3 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Frank Dana (FeRD) <ferdnyc@gmail.com - 0.8-4
- Add weak dependency on python3-grako

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-2
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8-1
- Update to 0.8
- Add a Python 3 subpackage (#1472490)

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.10-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.10-4
- Python 2 binary package renamed to python2-eyed3
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 David King <amigadave@amigadave.com> - 0.7.10-1
- Update to 0.7.10

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 01 2016 David King <amigadave@amigadave.com> - 0.7.9-2
- Remove unused python-magic dependency

* Fri Feb 26 2016 David King <amigadave@amigadave.com> - 0.7.9-1
- Update to 0.7.9
- Use license macro for COPYING
- Use python_provide macro (#1285546)
- Use py2_build and py2_install macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 28 2014 P J P <pjp@fedoraproject.org> - 0.7.5-1
- New release

* Wed Nov 19 2014 Mr Niranjan <mrniranjan@fedoraproject.org> - 0.7.4-4
- Fixed CVE-2014-1934, patch from Travis Shirk.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Christopher Meng <rpm@cicku.me> - 0.7.4-2
- Dependencies cleanup.

* Fri Dec 27 2013 Christopher Meng <rpm@cicku.me> - 0.7.4-1
- Update to 0.7.4.
- Add EPEL support.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Christopher Meng <rpm@cicku.me> - 0.7.3-1
- New version.
- Remove paver BR.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 bpepple <bpepple@fedoraproject.org> 0.6.18-2
- Rebase UserTextFrames patch.

* Fri Jan 27 2012 bpepple <bpepple@fedoraproject.org> 0.6.18-1
- Update to 0.6.18.

* Mon Jan 09 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.6.17-7
- Rebuild for new gcc.

* Fri Aug  5 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.6.17-6
- Add patch to fix crashes on files with empty UserTextFrames.
- Drop buildroot & clean sections. No longer needed.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.17-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  3 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.6.17-1
- Update to 0.6.17.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.16-2
- Rebuild for Python 2.6

* Thu Jun 19 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.6.16-1
- Update to 0.6.16.

* Sat Mar  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.6.15-1
- Update to 0.6.15.
- Update license tag.

* Fri May 18 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.6.14-1
- Update to 0.6.14.

* Sat Feb 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.6.12-1
- Update to 0.6.12.

* Fri Dec  8 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.6.11-3
- Change BR to python-devel.

* Fri Dec  8 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.6.11-2
- Rebuild against new python.

* Wed Nov 22 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.6.11-1
- Update to 0.6.11.

* Sat Oct  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.6.10-2
- Change BR to python.
- Remove unnecessary make in build section.

* Sat Oct  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.6.10-1
- Initial FE spec.
