Name:           python-eccodes
Version:        1.7.0
Release:        3%{?dist}
Summary:        Python interface to the ecCodes GRIB and BUFR decoder/encoder
License:        Apache-2.0

%global sphinx_doc_path build/sphinx/html/

# note: upstream has changed the name on pypi from eccodes-python to eccodes
URL:            https://pypi.org/project/eccodes/
Source0:        https://files.pythonhosted.org/packages/source/e/eccodes/eccodes-%{version}.tar.gz
# see https://github.com/ecmwf/eccodes-python/pull/21
Patch1:         python-eccodes-setup.patch
# see https://github.com/ecmwf/eccodes-python/issues/36
Patch2:         python-eccodes-sphinx-config.patch
# ECMWF introduced a new dependency called findlibs
# to find libeccodes.so easier on non-linux platforms.
# Since this is not useful at all for fedora users 
# I don't plan to package this python lib, so I patched out the use of it.
Patch3:         python-eccodes-disable-findlibs.patch

# note that the fast bindings are arch dependent
BuildRequires:  eccodes-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# needed to build the fast bindings
BuildRequires:  python3-cffi
# needed for checks/tests
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
# these next 2 seem not actually used, although they are mentioned as
# test dependencies in the setup.py file:
#BuildRequires:  python3-pytest-cov
#BuildRequires:  python3-pytest-flakes

# needed to build the documentation
BuildRequires:  python3-sphinx

# dont try to build for architectures for which the main
# ecccodes library cannot yet be build

# as explained in bugzilla #1562066
ExcludeArch: i686
# as explained in bugzilla #1562076
# this one should no longer be necessary
# ExcludeArch: s390x
# as explained in bugzilla #1562084
ExcludeArch: armv7hl


%global _description \
Python 3 interface to encode and decode GRIB and BUFR files via the \
ECMWF ecCodes library. It allows reading and writing of GRIB 1 and 2 \
files and BUFR 3 and 4 files.

%description %_description

%package -n python3-eccodes
Summary: %summary

%{?python_provide:%python_provide python3-eccodes}

%description -n python3-eccodes %_description

%prep
%autosetup -n eccodes-%{version} -p1

%build
%py3_build

%install
%py3_install

# NOTE:
# this package includes 2 c header files named gribapi/eccodes.h and
# gribapi/grib_api.h in the python module. This is intentional.
# The cffi interface reads them during runtime and extracts some
# constants from them.
# The function grib_get_api_version is called during import of the eccodes
# module and crashes with a runtime error if the files are not there.
# Therefore this next delete has been disabled.
#rm %%{buildroot}%%{python3_sitearch}/gribapi/*.h

# build documentation
# note that the new sphinx-build command only works AFTER installation
# of the module # so it can no longer be executed during the build stage.
PYTHONPATH=%{buildroot}%{python3_sitearch} \
sphinx-build -b html docs %sphinx_doc_path

# remove generated sphinx files that are not part of the actual documentation
rm %sphinx_doc_path/.buildinfo
rm -rf %sphinx_doc_path/.doctrees

%check

%{__python3} -m eccodes selfcheck
%{__python3} -m pytest -v

%files -n python3-eccodes
%doc README.rst
%doc %sphinx_doc_path
%license LICENSE
%{python3_sitearch}/eccodes-*-py*.egg-info
%{python3_sitearch}/eccodes
%{python3_sitearch}/gribapi


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.13

* Sun Mar 24 2024 Jos de Kloe <josdekloe@gmail.com> 1.7.0-1
- new upstream release 1.7.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Jos de Kloe <josdekloe@gmail.com> 1.6.1-1
- new upstream release 1.6.1

* Tue Aug 01 2023 Jos de Kloe <josdekloe@gmail.com> 1.6.0-2
- fix sphinx call #bz2221958

* Sat Jul 29 2023 Jos de Kloe <josdekloe@gmail.com> 1.6.0-1
- new upstream release 1.6.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.5.2-2
- Rebuilt for Python 3.12

* Sat May 20 2023 Jos de Kloe <josdekloe@gmail.com> 1.5.2-1
- new upstream release 1.5.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Jos de Kloe <josdekloe@gmail.com> 1.5.0-1
- SPDX migration: change ASL 2.0 to Apache-2.0

* Thu Sep 15 2022 Jos de Kloe <josdekloe@gmail.com> 1.5.0-1
- new upstream release 1.5.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Jos de Kloe <josdekloe@gmail.com> 1.4.2-1
- new upstream release 1.4.2

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.11

* Sat Mar 12 2022 Jos de Kloe <josdekloe@gmail.com> 1.4.1-1
- new upstream release 1.4.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Jos de Kloe <josdekloe@gmail.com> 1.3.3-2
- remove exclude arch voor s390x; should not be needed anymore
  since eccodes builds now for this arch.

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Jos de Kloe <josdekloe@gmail.com> 1.3.3-1
- new upstream release 1.3.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.2-2
- Rebuilt for Python 3.10

* Sat Apr 17 2021 Jos de Kloe <josdekloe@gmail.com> 1.3.2-1
- new upstream release 1.3.2

* Fri Apr 09 2021 Jos de Kloe <josdekloe@gmail.com> 1.2.0-1
- new upstream release 1.2.0

* Sat Jan 30 2021 Jos de Kloe <josdekloe@gmail.com> 1.1.0-1
- new upstream release 1.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Jos de Kloe <josdekloe@gmail.com> 1.0.0-1
- new upstream release 1.0.0; remove no longer needed patch 3

* Sun Oct 18 2020 Jos de Kloe <josdekloe@gmail.com> 0.9.9-1
- new upstream version, and adapt to upstream project name change
- add patch for sphinx configuration problem
- add patch to fix test run for eccodes 2.19.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Jos de Kloe <josdekloe@gmail.com> 0.9.8-1
- new upstream version

* Tue May 26 2020 Miro Hron?ok <mhroncok@redhat.com> - 0.9.7-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Jos de Kloe <josdekloe@gmail.com> 0.9.7-1
- First version for Fedora, based on a spec file contributed by
  Emanuele Di Giacomo and Daniele Branchini.
