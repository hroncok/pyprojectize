%global modname zope.component


Summary: Zope Component Architecture
Name: python-zope-component
Version: 5.0.1
Release: 11%{?dist}
Source0: https://pypi.io/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
License: ZPL-2.1
BuildArch: noarch
URL: https://pypi.io/project/zope.component

%description
This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%package -n python3-zope-component
Summary: Zope Component Architecture

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

Requires: python3-zope-interface
Requires: python3-zope-event

%description -n python3-zope-component
This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%prep
%setup -q -n %{modname}-%{version}

rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# build Sphinx documents
COPYRIGHT=`grep Author: PKG-INFO |sed -e 's/Author: //'`
cat >docs/conf.py <<END
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = '%{modname}'
copyright = '$COPYRIGHT'
version = '%{version}'
release = '%{version}'
pygments_style = 'sphinx'
html_static_path = ['_static']
extensions = []
END

sphinx-build -b html docs/ html

rm -fr html/{.buildinfo,.doctrees}

%install
%pyproject_install

%files -n python3-zope-component
%doc CHANGES.rst COPYRIGHT.txt README.rst
%doc html/
%license LICENSE.txt
%{python3_sitelib}/zope/component/
%exclude %{python3_sitelib}/zope/component/*.txt
%{python3_sitelib}/%{modname}-*.dist-info
%{python3_sitelib}/%{modname}-*-nspkg.pth

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.0.1-10
- Rebuilt for Python 3.13

* Sun Apr 14 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.1-9
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 5.0.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.0.1-2
- Rebuilt for Python 3.11

* Wed May 25 2022 Nick Bebout <nb@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 4.3.0-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-11
- Subpackage python2-zope-component has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-2
- Rebuild for Python 3.6

* Tue Sep 27 2016 Ralph Bean <rbean@redhat.com> - 4.3.0-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.2.2-4
- Add an explicit python2 subpackage.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 4.2.2-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 4.2.1-1
- Latest upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 4.2.0-1
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Ralph Bean <rbean@redhat.com> - 4.1.0-1
- Updated to latest upstream: 4.1.0.
- Rename {README,CHANGES}.txt to {README,CHANGES}.rst

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 4.0.2-2
- Fix python3 conditional

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 4.0.2-1
- Latest upstream.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Tomas Dabasinskas <tomas@redhat.com> - 4.0.1-2
- Fixed python3 package files section
- Removed exclude *.txt for pyhon2 package as no txt files are generated during install

* Thu Nov 29 2012 Ralph Bean <rbean@redhat.com> - 4.0.1-1
- Updated to latest upstream.
- Included python3 subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan  2 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.10.0-2
- Get rid of the utility script

* Sun Jan  2 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0
- Include a utility script to build Sphinx documents

* Mon Sep 20 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.9.5-2
- Rearrange the documents

* Sun Sep  5 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.9.5-1
- Update to 3.9.5
- Don't move documents
- Requires: python-zope-filesystem and python-setuptools removed
- Spec cleaned up

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.9.4-1
- Initial packaging
