Name:           python-kitchen
Version:        1.2.6
Release:        22%{?dist}
Summary:        Small, useful pieces of code to make python coding easier

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pypi.python.org/pypi/kitchen/
Source0:        https://github.com/fedora-infra/kitchen/archive/%{version}.tar.gz

Patch0:         kitchen-1.2.6-sphinx-ext-imgmath.patch

BuildArch:      noarch

BuildRequires:  langpacks-pt_BR

BuildRequires:  python%{python3_pkgversion}-devel
# BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-test
BuildRequires:  python%{python3_pkgversion}-chardet
%if 0%{?rhel}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%description
kitchen includes functions to make gettext easier to use, handling unicode
text easier (conversion with bytes, outputting xml, and calculating how many
columns a string takes), and compatibility modules for writing code that uses
python-2.7 modules but needs to run on python-2.3.

%package -n python%{python3_pkgversion}-kitchen
Summary:    Small, useful pieces of code to make python 3 coding easier

Requires:   python%{python3_pkgversion}
Requires:   python%{python3_pkgversion}-chardet

%description -n python%{python3_pkgversion}-kitchen
kitchen includes functions to make gettext easier to use, handling unicode
text easier (conversion with bytes, outputting xml, and calculating how many
columns a string takes).

This is the python3 version of the kitchen module.

%package -n python%{python3_pkgversion}-kitchen-doc
Summary:    API documentation for the Kitchen python3 module
#Requires: python3-kitchen = %{version}-%{release}
%description -n python%{python3_pkgversion}-kitchen-doc
kitchen includes functions to make gettext easier to use, handling unicode
text easier (conversion with bytes, outputting xml, and calculating how many
columns a string takes).

This package contains the API documenation for programming with the
python-3 version of the kitchen library.

%prep
%autosetup -p1 -n kitchen-%{version}

# Remove bundled egg info, if any.
rm -rf *.egg*

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

# Build docs
%if 0%{?rhel}
sphinx-build kitchen3/docs/ build/sphinx/html
cp -pr build/sphinx/html .
rm -rf html/.buildinfo
%endif

%install
%{pyproject_install}
%pyproject_save_files -l 'kitchen*'

# %check
# # In current mock, the PATH isn't being reset.  This causes failures in some
# # subprocess tests as a check tests /root/bin/PROGRAM and fails with Permission
# # Denied instead of File Not Found.  reseting the PATH works around this.
# PATH=/bin:/usr/bin
# PYTHONPATH=.:kitchen3/ nosetests-%{python3_version} kitchen3/tests/

%files -n python%{python3_pkgversion}-kitchen -f %{pyproject_files}
%doc README.rst NEWS.rst

%files -n python%{python3_pkgversion}-kitchen-doc
%doc kitchen3/docs/*
%license COPYING COPYING.LESSER
%if 0%{?rhel}
%doc html
%endif

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.6-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.6-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.6-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.6-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.6-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Merlin Mathesius <mmathesi@redhat.com> - 1.2.6-8
- Build the Python3 version of the docs
- Patch sphinx doc config to use imgmath instead of deprecated pngmath extension

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-4
- Subpackage python2-kitchen has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Ralph Bean <rbean@redhat.com> - 1.2.6-1
- New version with updated codepoints.
- Disable the check section, due to issues discussed in #1583600.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-5
- Rebuilt for Python 3.7 (with tests temporarily disabled)

* Fri Jun 08 2018 Ralph Bean <rbean@redhat.com> - 1.2.5-4
- Update unicode combining table for py3.7.
  https://bugzilla.redhat.com/show_bug.cgi?id=1583600

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.5-1
- Update to 1.2.5. Fixes bug #1484856

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-5
- Rebuild for Python 3.6
- Add docs back as a separate source (to fix build with recent sphinx)
- Update codepoints patch for latest Python and unicode data

* Mon Sep 12 2016 Ralph Bean <rbean@redhat.com> - 1.2.4-4
- Explicit python2 subpackage.
- Support python34 on epel7.
- Modernize python macros.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Ralph Bean <rbean@redhat.com> - 1.2.4-1
- new version
- Apply patch fixing the unicode codepoints table for py3.5.

* Wed Nov 11 2015 Ralph Bean <rbean@redhat.com> - 1.2.1-5
- Support python34 on EPEL7.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 02 2014 Ralph Bean <rbean@redhat.com> - 1.2.1-2
- Include patch to get py34 tests working for rawhide.

* Tue Dec 02 2014 Ralph Bean <rbean@redhat.com> - 1.2.1-1
- Latest upstream, now with python3 support!
- Added python3 subpackages.
- Remove use of build_sphinx.
- Rename README and NEWS with new .rst extension.
- Modernized python2 macros.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-6
- Move the html docs to the docs package

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.1-4
- Move the api documentation into its own subpackage

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.1-1
- Bugfix for using easy_gettext_setup or get_translation_object with the
  default localedirs

* Thu Jan 12 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 final

* Thu Apr 14 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.0-1
- Upstream update to 1.0 final

* Sun Feb 20 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.4-1
- Upstream update 0.2.4
  - Changes i18n.easy_gettext_setup() to return lgettext functions when
    byte strings are requested.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 5 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.3-2
- Upstream respin of the tarball

* Wed Jan 5 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.3-1
- Upstream update to 0.2.3
- Fixes https://bugzilla.redhat.com/show_bug.cgi?id=667433

* Mon Jan 3 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.2-1
- Upstream update 0.2.2
  - Adds exception to message functions
- Build html docs

* Thu Sep 2 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.1-0.1.a1
- Update to upstream 0.2.1a1 release.
- Fixes build on python-2.7, adds iterutils module, optimizes some functions,
  increases documentation

* Thu Jul 29 2010 Dennis Gilmore <dennis@ausil.us> - 0.2-0.1.a2
- propoerlly version accrding to pre-release guidelines
- run tests
- update to 0.2a2
- include COPYING.LESSER and docs dir

* Thu Jul 29 2010 Dennis Gilmore <dennis@ausil.us> - 0.2a1-2
- rename to python-kitchen

* Thu Jul 29 2010 Dennis Gilmore <dennis@ausil.us> - 0.2a1-1
- update to 0.2a1

* Thu Jul 15 2010 Dennis Gilmore <dennis@ausil.us> - 0.1a3-3
- fix spelling mistake in description

* Thu Jul 15 2010 Dennis Gilmore <dennis@ausil.us> - 0.1a3-2
- add documentaion
- fix description

* Thu Jul 15 2010 Dennis Gilmore <dennis@ausil.us> - 0.1a3-1
- initial package
