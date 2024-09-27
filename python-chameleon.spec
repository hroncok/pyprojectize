%global srcname Chameleon

Name:           python-chameleon
Version:        4.5.4
Release:        5%{?dist}
Summary:        XML-based template compiler

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/malthe/chameleon
Source0:        https://github.com/malthe/chameleon/archive/%{version}/chameleon-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-lxml

%generate_buildrequires
%pyproject_buildrequires -t


%global _description\
Chameleon is an XML attribute language template compiler. It comes with\
implementations for the Zope Page Templates (ZPT) and Genshi templating\
languages.\
\
The engine compiles templates into Python byte-code. This results in\
performance which is on average 10-15 times better than implementations which\
use run-time interpretation.

%description %_description

%package -n python3-chameleon
Summary: %summary

Requires:   python3-setuptools
Requires:   python3-lxml
%{?python_provide:%python_provide python3-chameleon}

%description -n python3-chameleon %_description

%prep
%autosetup -n chameleon-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# No need to ship tests as part of the module
rm -rf  %{buildroot}%{python3_sitelib}/chameleon/tests
# Data files for the tests
find %{buildroot}%{python3_sitelib}/chameleon -name '*.txt' -exec rm \{\} \;

%check
#pytest
%tox


%files -n python3-chameleon
%doc README.rst
%{python3_sitelib}/chameleon/
%{python3_sitelib}/Chameleon-%{version}*

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.5.4-5
- convert license to SPDX

* Mon Aug 19 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.5.4-4
- Switch to tox instead of setup.py test

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.5.4-2
- Rebuilt for Python 3.13

* Mon Apr 08 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.5.4-1
- Update to upstream.

* Fri Apr 05 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.5.3-1
- Update to upstream.

* Tue Jan 30 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.5.2-1
- Update to upstream.

* Sun Jan 28 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.5.1-1
- Update to upstream.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.5.0-1
- Update to upstream.

* Sat Dec 30 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.4.3-1
- Update to upstream.

* Mon Dec 18 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.4.1-1
- Update to upstream.

* Wed Dec 13 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.4.0-1
- Update to upstream.

* Mon Dec 04 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.3.0-1
- Update to upstream.

* Thu Sep 28 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.2.0-1
- Update to upstream.

* Tue Aug 29 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.1.0-1
- Update to upstream.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 4.0.1-2
- Rebuilt for Python 3.12

* Mon Jun 19 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.0.1-1
- Update to upstream.

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.10.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.10.2-1
- Update to upstream.

* Sun Sep 18 2022 Kevin Fenzi <kevin@scrye.com> - 3.10.1-1
- Update to 3.10.1. Fixes rhbz#2072607

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.9.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.9.1-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Kevin Fenzi <kevin@scrye.com> - 3.9.1-1
- Update to 3.9.1. Fixes rhbz#1960539

* Sun Feb 28 2021 Kevin Fenzi <kevin@scrye.com> - 3.9.0-1
- Update to 3.9.0. Fixes rhbz#1933237

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Kevin Fenzi <kevin@scrye.com> - 3.8.1-1
- Update to 3.8.1. Fixes rhbz#1848107

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.7.2-1
- Update to upstream
- Fixed build on python 3.9 (bz#1818599)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.2-4
- Subpackage python2-chameleon has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Kevin Fenzi <kevin@scrye.com> - 3.6.2-1
- Update to 3.6.2. Fixes bug #1723037

* Tue Apr 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.1-1
- Update to 3.6.1 (#1678778)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.4-1
- Update to 3.4
- Modernize spec file a little
- Drop building the documentation as apparently upstream stopped shipping it in
  their tarball

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2-4
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Kevin Fenzi <kevin@scrye.com> - 3.2-1
- Update to 3.2. Fixes bug #1504336

* Wed Aug 09 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1-3
- Python 2 binary package renamed to python2-chameleon
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Kevin Fenzi <kevin@scrye.com> - 3.1-1
- Update to 3.1. Fixes bug #1425631

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Kevin Fenzi <kevin@scrye.com> - 3.0-1
- Update to 3.0. Fixes bug #1402375

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.25-2
- Rebuild for Python 3.6

* Sun Sep 25 2016 Kevin Fenzi <kevin@scrye.com> - 2.25-1
- Update to 2.25. Fixes bug #1379057

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 Ralph Bean <rbean@redhat.com> - 2.24-1
- new version

* Tue Oct 27 2015 Ralph Bean <rbean@redhat.com> - 2.23-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 2.20-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 2.16-1
- Latest upstream.
- Modernize python2 macros.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Apr 11 2014 Ralph Bean <rbean@redhat.com> - 2.15-1
- Latest upstream.

* Fri Jan 17 2014 Ralph Bean <rbean@redhat.com> - 2.11-4
- Add dependency on ordereddict for el6.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Ralph Bean <rbean@redhat.com> - 2.11-1
- Latest upstream version.
- More specific file/dir ownership.
- Removed unnecessary buildroot.
- Removed unnecessary defattr.
- Removed unnecessary clean section.
- Packaging a python3 subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.7.0-1
- New upstream release

* Thu Nov 10 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.5.3-1.1
- Fix to build on RHEL6

* Thu Nov 10 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.5.3-1
- New upstream release

* Mon Oct 3 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.5.1-1
- New upstream release

* Sun Aug 21 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.8-1
- New upstream release

* Thu Aug 18 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.6-1
- New upstream release

* Wed Aug 10 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2-1
- New upstream release

* Fri Jul 15 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-1
- New upstream release
- This release removes the genshi-like syntax support -- F17+, only

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 18 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.12-4
- Move COPYING file out of the ast directory and into docdir.

* Fri Sep 17 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.12-3
- Fix unittests on python-2.7.

* Thu Sep 16 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.12-2
- Add a patch so we can run with newer versions of the optional deps

* Wed Sep 15 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.12-1
- Initial package
