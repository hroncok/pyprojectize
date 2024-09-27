# avoid providing the private libs:
%global __provides_exclude_from ^(%{python3_sitearch})/.*\\.so.*$

Name:       pygrib
Version:    2.1.6
Release:    1%{?dist}
Summary:    Python module for reading and modifying GRIB files

# this software uses the "MIT:Modern Style with sublicense" license
License:    MIT
URL:        https://github.com/jswhit/%{name}
Source0:    https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

# Adapt setup.py to prevent an rpath definition in the *.so file
Patch1: %{name}-build.patch

# Workaround needed for new matplotlib version.
# See https://github.com/jswhit/pygrib/issues/256
Patch2: %{name}-test-gaussian.patch

# exclude architectures not supported by eccodes
# as explained in bugzilla #1562066
ExcludeArch: i686
# as explained in bugzilla #1562084
ExcludeArch: armv7hl

# these are required for building pygrib
BuildRequires: gcc
BuildRequires: make
BuildRequires: eccodes-devel
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-Cython
# no longer needed as direct BR without gribapi
# (but still an indirect dependency through cartopy)
# BuildRequires: python3-pyproj

# these are used for pytest testing in the check section
BuildRequires: python3-pytest
BuildRequires: python3-pytest-mpl
BuildRequires: python3-matplotlib
BuildRequires: python3-cartopy
BuildRequires: python3-scipy

# these are needed to prevent cartopy from downloading shape files
BuildRequires: natural-earth-map-data-110m
BuildRequires: natural-earth-map-data-50m

%global _description \
Cython wrapper to provide a high-level interface to the ECMWF eccodes \
C library for handling GRIB files. \
 \
GRIB is the the World Meteorological Organization (WMO) standard for \
distributing gridded data. \
This module contains python interfaces for reading and modifying GRIB files \
using the ECMWF ECCODES C library, \
as well as command-line utilities for listing and re-packing GRIB files. \
 \
There are for now limited capabilities for writing GRIB files, i.e. \
you can modify the contents of an existing file, \
but you can't create one from scratch.

%description %_description

%package -n python3-%{name}

Summary: %summary

# this requirement is not automatically resolved and needs to be
# inserted manually (see bug #996834)
Requires:  eccodes
Requires:  python3-pyproj

# ensure python provides are provided
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name} %_description

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build

%pyproject_wheel

%install

# this setting triggers installation of man pages by the setup.py file
export MAN_DIR=/usr/share/man/

%pyproject_install

# copy documentation
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -r %{_builddir}/%{name}-%{version}/docs/_build/html \
      %{buildroot}%{_datadir}/doc/%{name}/html

# ensure the autogenerated hidden .buildinfo file is not included
# since rpmlint does not like hidden files in the documentation
%{__rm} %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo

%check

# note: need to do out-of-source-dir testing
#       otherwise the source pygrib folder is imported
#       in stead of the copy in the build dir containing the shared object.
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
export MPLBACKEND=agg

export TESTROOT=%{_builddir}/%{name}-%{version}-tmp-test
mkdir $TESTROOT
cp -R sampledata $TESTROOT
cp -R test $TESTROOT

cd  $TESTROOT/test
# check a simple import statement
%{__python3} -c "import pygrib"
# execute the doc tests as defined in test/test.py
%{__python3} test.py

# This run script automatically executes all
# tests in the test folder starting with "test_",
# but it only executes the data read functionality of pygrib, and
# does not test generate the test maps by cartopy and does not compare
# those to the reference maps provided.
# That is done by the pytest call below.
%{__python3} run_tests.py

# note: pyspharm is not yet available in fedora
#       this test is automatically skipped when run as python script
#       but pytest crashes on it so this is just a reminder for now.
%{__python3} test_spectral.py

# run the same tests again, but now produce maps using cartopy
# and compare these to reference maps provided with the test suite.
%pytest test_gaussian.py test_latlons.py \
        test_lambert.py test_ndfd_conus.py \
        test_ndfd_pr.py \
        test_rotated_ll.py test_set_bitmap.py  test_stere.py \
        --mpl --mpl-baseline-path=`pwd`/baseline_images
# Disabled the next 3 since they started to fail after the Fedora 35
# mass-rebuild.
# After inspecting the generated images it is clear that the failures
# are caused by a change in behaviour of cartopy and not related at all
# to the ability of pygrib to read the test files, so for now it seems
# safe to just disable these 3 test cases.
#    test_reduced_gg.py
#    test_reduced_ll.py
#    test_reglatlon.py
# This has been reported here:
# https://github.com/jswhit/pygrib/issues/188

%files -n python3-%{name}
%doc LICENSE PKG-INFO README.md
%doc %{_datadir}/doc/%{name}/
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-*.dist-info
%{_bindir}/cnv*
%{_bindir}/grib_*
%{_mandir}/man1/cnv*
%{_mandir}/man1/grib_*

%changelog
* Fri Jul 19 2024 Jos de Kloe <josdekloe@gmail.com> 2.1.6-1
- Update to 2.1.6 (#2295876)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Jos de Kloe <josdekloe@gmail.com> 2.1.5-5
- fix doctest problem by patching one test following upstream suggestion

* Wed Jun 26 2024 Python Maint <python-maint@redhat.com> - 2.1.5-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 17 2023 Jos de Kloe <josdekloe@gmail.com> 2.1.5-1
- Update to 2.1.5 (#2249583)

* Wed Jul 19 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.4-9
- Rebuild for Python 3.12b4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Jos de Kloe <josdekloe@gmail.com> 2.1.4-7
- remove no longer needed BR for python3-pyproj
- SPDX migration: checked the license text, and concluded that MIT is the
  correct SPDX license tag.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Jos de Kloe <josdekloe@gmail.com> 2.1.4-5
- remove ExcludeArch: s390x, since this is now supported by eccodes

* Wed Jun 29 2022 Python Maint <python-maint@redhat.com> - 2.1.4-4
- Rebuilt for Python 3.11

* Sun Jan 30 2022 Jos de Kloe <josdekloe@gmail.com> 2.1.4-3
- Disable 3 problematic test cases that fail after the mass rebuild.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 19 2021 Jos de Kloe <josdekloe@gmail.com> 2.1.4-1
- Update to 2.1.4 (#2005528)

* Thu Sep 09 2021 Jos de Kloe <josdekloe@gmail.com> 2.1.3-6
- Fix a zorder problem in the testsuite that was triggered by the move
  to matplotlib 3.5.0 in rawhide.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.3-4
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Jos de Kloe <josdekloe@gmail.com> 2.1.3-3
- Fix rpath error as reported by the new check-rpaths tool during rpm build.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Jos de Kloe <josdekloe@gmail.com> 2.1.3-1
- Update to 2.1.3 (#1910130)
- Activate cartopy based tests run by pytest

* Wed Dec 23 2020 Jos de Kloe <josdekloe@gmail.com> 2.1.2-1
- update to new upstream version 2.1.2
- activate new set of cartopy based tests

* Fri Dec 04 2020 Jos de Kloe <josdekloe@gmail.com> 2.1.1-1
- update to new upstream version 2.1.1
- general clean-up and remove grib_api workarounds since upstream
  no longer supports grib_api
- remove support for architectures not supported by eccodes

* Wed Nov 25 2020 Jos de Kloe <josdekloe@gmail.com> 2.0.5-1
- update to new upstream version 2.0.5

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Jos de Kloe <josdekloe@gmail.com> 2.0.4-1
- update to new upstream version 2.0.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Jos de Kloe <josdekloe@gmail.com> 2.0.3-2
- remove python2 sub-package as per Mass Python 2 Package Removal for f30

* Fri Aug 24 2018 Jos de Kloe <josdekloe@gmail.com> 2.0.3-1
- update to new upstream version 2.0.3

* Fri Aug 17 2018 Jos de Kloe <josdekloe@gmail.com> 2.0.2-17
- merge with cython patch by Miro Hrončok <pagure@pkgs.fedoraproject.org>
  (there is no more cython3, use the -m syntax)

* Thu Aug 02 2018 Jos de Kloe <josdekloe@gmail.com> - 2.0.2-16
- Build using eccodes for those architectures that provide it

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-14
- Rebuilt for Python 3.7

* Thu Feb 15 2018 Jos de Kloe <josdekloe@gmail.com> - 2.0.2-13
- Rebuild after mass rebuild caused dependency troubles

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Jos de Kloe <josdekloe@gmail.com> 2.0.2-11
- Adapt to changed name of g2c static library

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Jos de Kloe <josdekloe@gmail.com> 2.0.2-8
- reorganize spec file (following pyproj) example to ensure
  Requires are used for the right sub-package, and added optflags

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.0.2-7
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Jun 30 2017 Jos de Kloe <josdekloe@gmail.com> 2.0.2-6
- rename pygrib to python2-pygrib following the new package naming scheme

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Rebuild for Python 3.6

* Sat Dec 3 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.2-3
- force a rebuild, needed due to libjasper so version bump

* Sat Nov 26 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.2-2
- fix mistake in patch for setup.py file that caused python3 package
  to provide python2 version tools

* Sun Nov 20 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.2-1
- update to new upstream version
- provide tools below /usr/bin for python3 in stead of python2
- move to new predictable pypi source location
- add python_provide macros

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.1-1
- update to new upstream version

* Sun Nov 15 2015 Jos de Kloe <josdekloe@gmail.com> 2.0.0-5
- update patch pygrib-2.0.0-g2clib.pyx.patch and add a new
  pygrib-2.0.0-pygrib.pyx.patch to adapt to stricter
  variable type checking of cython
  
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jul 15 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-3
- Rebuild for grib_api 1.14.0 soname bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Jos de Kloe <josdekloe@gmail.com> 2.0.0-1
- update to upstream version 2.0.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Jos de Kloe <josdekloe@gmail.com> 1.9.9-2
- move requires for python3-pyproj above description section

* Sat Jul 05 2014 Jos de Kloe <josdekloe@gmail.com> 1.9.9-1
- update to upstream version 1.9.9
- replace python_sitearch macro with python2_sitearch
- activate installation of the newly added man pages
- fix requires problem for python3-pyproj
- update url for Source0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Oct 26 2013 Jos de Kloe <josdekloe@gmail.com> 1.9.7-1
- update to upstream version 1.9.7

* Fri Aug 23 2013 Jos de Kloe <josdekloe@gmail.com> 1.9.6-1
- update to upstream version 1.9.6
  and move to use grib_api-devel as BR as suggested by Orion Poplawski
  on devel mailinglist on 23-Aug-2013

* Wed Aug 14 2013 Jos de Kloe <josdekloe@gmail.com> 1.9.5-4
- add an explicit requirement on grib_api

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Nov 22 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.5-2
- adapt to build with python3 as well
- fix typo in weekdays in dates of changelog entries 1.9.2-1 and 1.9.4-1

* Thu Nov 08 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.5-1
- update to upstream version 1.9.5
- add the doc files to the files list
- activate the check section

* Sat Sep 08 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.4-3
- remove BR of grib_api-devel and g2clib-devel and some textual 
  changes in the comments

* Wed Aug 29 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.4-2
- address comments 3 and 4 in bugzilla review request 806037

* Thu Aug 23 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.4-1
- move to version 1.9.4 and fix a bunch of rpmlint warnings

* Sun Mar 18 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.2-1
- initial version