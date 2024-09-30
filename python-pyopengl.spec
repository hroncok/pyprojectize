%global srcname PyOpenGL
%global shortname pyopengl

Name:           python-%{shortname}
Version:        3.1.7
Release:        9%{?dist}
Summary:        Python bindings for OpenGL
License:        BSD-3-Clause and X11-distribute-modifications-variant
URL:            https://github.com/mcfletch/pyopengl
Source0:        https://pypi.python.org/packages/source/P/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://pypi.python.org/packages/source/P/%{srcname}-accelerate/%{srcname}-accelerate-%{version}.tar.gz
Patch0:         python-3.12.patch
Patch1: python-pyopengl-c99.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-Cython

# For tests
BuildRequires:  libglvnd-opengl
BuildRequires:  mesa-dri-drivers
BuildRequires:  mesa-libGLU
BuildRequires:  python3-pygame
BuildRequires:  python3-pytest
BuildRequires:  xorg-x11-server-Xvfb

%description
PyOpenGL is the cross platform Python binding to OpenGL and related APIs. It
includes support for OpenGL v1.1, GLU, GLUT v3.7, GLE 3 and WGL 4. It also
includes support for dozens of extensions (where supported in the underlying
implementation).

PyOpenGL is inter-operable with a large number of external GUI libraries
for Python including (Tkinter, wxPython, FxPy, PyGame, and Qt). 


%package -n     python3-%{shortname}
Summary:        Python 3 bindings for OpenGL
Requires:       freeglut
Requires:       libglvnd-opengl
Requires:       python3-numpy

%description -n python3-%{shortname}
PyOpenGL is the cross platform Python binding to OpenGL and related APIs. It
includes support for OpenGL v1.1, GLU, GLUT v3.7, GLE 3 and WGL 4. It also
includes support for dozens of extensions (where supported in the underlying
implementation).

PyOpenGL is inter-operable with a large number of external GUI libraries
for Python including (Tkinter, wxPython, FxPy, PyGame, and Qt). 


%package -n     python3-%{shortname}-tk
Summary:        %{srcname} Python 3.x Tk widget
BuildArch:      noarch
Requires:       python3-%{shortname} = %{version}-%{release}
Requires:       python3-tkinter

%description -n python3-%{shortname}-tk
%{srcname} Togl (Tk OpenGL widget) 1.6 support for Python 3.x.


%prep
%setup -q -c -n %{srcname}-%{version} -T -a0 -a1
%patch -P0 -p1
%patch -P 1 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
# Delete all Cython generated .c files to force a rebuild in py3_build
# (py2_build then reuses the Cython output)
pushd %{srcname}-accelerate-%{version}/src
for f in *.pyx ; do
    rm -f "${f%.pyx}.c"
done
popd

for dir in %{srcname}-%{version} %{srcname}-accelerate-%{version} ; do
    pushd $dir
    %pyproject_wheel
    popd
done


%install
for dir in %{srcname}-%{version} %{srcname}-accelerate-%{version} ; do
    pushd $dir
    %pyproject_install
    popd
done

# Fix up perms on compiled object files
find %{buildroot}%{python3_sitearch}/OpenGL_accelerate/ -name *.so -exec chmod 755 '{}' \;

# Remove shebangs - note that weirdly these files have a space between
# the #! and the /, so this sed recipe is not the usual one
pushd %{buildroot}%{python3_sitelib}/OpenGL/arrays
sed -i -e '/^#! \//, 1d' buffers.py _buffers.py
popd


%check
%ifarch s390x
export PYTEST_ADDOPTS="-k 'not test_buffer_api_basic'"
%endif
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} \
  xvfb-run -a -s "-screen 0 1024x768x24 -ac +extension GLX +render -noreset" \
  pytest %{srcname}-%{version}/tests


%files -n python3-%{shortname}
%license %{srcname}-%{version}/license.txt
%{python3_sitelib}/%{srcname}-%{version}.dist-info
%{python3_sitelib}/OpenGL/
%exclude %{python3_sitelib}/OpenGL/Tk
%{python3_sitearch}/OpenGL_accelerate/
%{python3_sitearch}/%{srcname}_accelerate-%{version}.dist-info/


%files -n python3-%{shortname}-tk
%{python3_sitelib}/OpenGL/Tk


%changelog
* Wed Aug 07 2024 Scott Talbert <swt@techie.net> - 3.1.7-9
- Update License tag to use SPDX identifiers

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 3.1.7-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 3.1.7-4
- Fix C compatibility issues

* Mon Jul 24 2023 Scott Talbert <swt@techie.net> - 3.1.7-3
- Add runtime depends on libglvnd-opengl also

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Scott Talbert <swt@techie.net> - 3.1.7-1
- Update to new upstream release 3.1.7 (#2209308)

* Tue Jul 18 2023 Scott Talbert <swt@techie.net> - 3.1.6-3
- Fix FTBFS with Python 3.12 (#2220441)

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1.6-2
- Rebuilt for Python 3.12

* Thu Jan 26 2023 Scott Talbert <swt@techie.net> - 3.1.6-1
- Update to new upstream release 3.1.6 (#2056226)
- Enable upstream tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.5-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.5-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Scott Talbert <swt@techie.net> - 3.1.5-1
- Update to new upstream release 3.1.5 (#1787861)

* Sun Dec 01 2019 Scott Talbert <swt@techie.net> - 3.1.4-1
- Update to new upstream release 3.1.4

* Tue Nov 19 2019 Scott Talbert <swt@techie.net> - 3.1.1a1-21
- Remove Python 2 support

* Fri Oct 04 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1a1-20
- Rebuilt for new freeglut

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1a1-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1a1-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1a1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Petr Viktorin <pviktori@redhat.com> - 3.1.1a1-16
- Remove build dependency on python2-Cython

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1a1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Scott Talbert <swt@techie.net> - 3.1.1a1-14
- Remove unused python2-pyopengl-tk subpackage (#1627406)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1a1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jonathan Underwood <Jonathan G. Underwood@gmail.com> - 3.1.1a1-12
- Add BuildRequires for python{2,3}-Cython
- Remove uneeded Provides/Obsoletes
- Force Cython rebuild of c files
- Add missing .pxd files from upstream github repository
- Update URL to point to github
- Rename async.py modules to async_.py to avoid clash with async keyword

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.1a1-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1a1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1a1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1a1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1a1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.1.1a1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1a1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar  4 2016 Jonathan Underwood <Jonathan G. Underwood@gmail.com> - 3.1.1a1-4
- Fix upgrade path for python3-PyOpenGL

* Sat Feb 27 2016 Jonathan Underwood <Jonathan G. Underwood@gmail.com> - 3.1.1a1-3
- Fix python_provide macro calls for the -tk packages

* Sat Feb 27 2016 Jonathan Underwood <Jonathan G. Underwood@gmail.com> - 3.1.1a1-2
- Rename package to python-pyopengl
- Rename -Tk subpackages to -tk
- Fix Requires of python2-pyopengl-Tk to require python2-pyopengl

* Sat Feb 27 2016 Jonathan Underwood <Jonathan G. Underwood@gmail.com> - 3.1.1a1-1
- Fix Provides for renamed sub-packages
- Use standard build and install python packaging macros

* Fri Feb 26 2016 Jonathan Underwood <Jonathan G. Underwood@gmail.com> - 3.1.1a1-0
- Rename package to python-PyOpenGL
- Fix package to comply with current python packaging guidelines
- Add Provides for python2-PyOpenGL (BZ 1249421)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Jonathan Underwood <Jonathan G. Underwood@gmail.com> - 3.1.0-2
- Add accelerate modules for Python 2 and 3
- Package is no longer noarch
- Tk sub-packages are noarch

* Thu Jul 31 2014 Christopher Meng <rpm@cicku.me> - 3.1.0-1
- Update to 3.1.0
- Correct the python3 package dependency.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0b2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.1.0b2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 05 2014 Christopher Meng <rpm@cicku.me> - 3.1.0b2-1
- Build python3 interface.
- Drop unneeded dependencies.

* Fri Apr 11 2014 François Cami <fcami@fedoraproject.org> - 3.1.0b2-1
- Update to latest upstream.

* Fri Aug 23 2013 François Cami <fcami@fedoraproject.org> - 3.0.2-1
- Update to latest upstream.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Nikolay Vladimirov <nikolay@vladimiroff.com> - 3.0.1-3
- Upload new archive with removed binary blobs - RHB #760366

* Sat Apr 16 2011 Nikolay Vladimirov <nikolay@vladimiroff.com> - 3.0.1-2
- Fix date in previous changelog entry
- specfile fixes

* Fri Apr 15 2011 Nikolay Vladimirov <nikolay@vladimiroff.com> - 3.0.1-1
- New upstream release
- Fix BZ # 635496 - PyOpenGL crashes on every program
- Update the shebang patch to work on the latest version
- Upstream restored license.txt to their distribution

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 30 2009 Jesse Keating <jkeating@redhat.com> - 3.0.0-2
- Rebuild for Fedora 12 mass rebuild

* Tue Jun 9 2009 Nikolay Vladimirov <nikolay@vladimiroff.com> - 3.0.0-1
- Updated to 3.0 stable
- Changed requires from python-numeric to numpy for BZ #504681
- upstream removed full license text in license.txt
- other minor spec fixes

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.12.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 2 2009 Nikolay Vladimirov <nikolay@vladimiroff.com> - 3.0.0-0.11.b8
- New upstream 3.0.0b8 (b7 was skipped by upstream)
- performance, bug-fix and packaging release. 
- Use macro for "python"
- remove "--single-version-externally-managed" option for setup.py
- *.egg-info is no longer a folder, it's a file now 
- Tests are no longer installed by setup.py
- Obsolete 'doc' subpackage (no longer distributed "documentation" folder)
- license.txt is also no longer provided by upstream. Using one from b6
- Removed Requires for libGL and libGLU ( should be pulled for freeglut)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.0-0.10.b6
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.0-0.9.b6
- Rebuild for Python 2.6

* Mon Sep 22 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> 3.0.0-0.8.b6
- New upstream release 3.0.0b6

* Mon Jul 28 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> 3.0.0-0.7.b5
- New upstream release 3.0.0b5

* Fri Jul 18 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> 3.0.0-0.6.b4
- New upstream release 3.0.0b4

* Mon Dec 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.5.b1
- New upstream release 3.0.0b1

* Thu Aug 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.4.a6
- Change BuildRequires python-setuptools to python-setuptools-devel for
  the python-setuptools package split

* Fri Apr 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.3.a6
- Add missing freeglut, libGL and libGLU requires (bz 236159)

* Thu Mar 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.2.a6
- Remove tests from the package (bz 234121)
- Add -Tk subpackage (bz 234121)
- Remove shebang from files with shebang instead of chmod +x (bz 234121)
- Better description

* Sat Mar 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0.0-0.1.a6
- Initial Fedora Extras package
