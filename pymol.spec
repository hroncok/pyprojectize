Name: pymol
Summary: PyMOL Molecular Graphics System
Version: 2.5.0
Release: 13%{?dist}

# Which files use following license:
# BSD: main license of open source PyMOL and some plugins
# MIT: modules/pymol_web/examples/sample13/jquery.js
# Bitstream Vera: layer1/FontTTF.h
# OFL: layer1/FontTTF2.h
# Automatically converted from old format: MIT and BSD and Bitstream Vera and OFL - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND Bitstream-Vera AND LicenseRef-Callaway-OFL
URL: http://www.pymol.org
Source0: https://github.com/schrodinger/pymol-open-source/archive/v%{version}/%{name}-open-source-%{version}.tar.gz
Source1: %{name}.png
Source2: %{name}.desktop
Source3: %{name}.appdata.xml

# Set optimization level
Patch0: %{name}-setup.py.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1311626
Patch1: %{name}-wmclass-main.patch
Patch2: %{name}-wmclass-pmgapp.patch

Patch3: %{name}-mmtf.patch

# https://github.com/schrodinger/pymol-open-source/issues/186
Patch4: %{name}-2.5.0-bug186.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: glm-devel
BuildRequires: libGL-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
BuildRequires: mmtf-cpp-devel
BuildRequires: msgpack-devel
BuildRequires: netcdf-devel
BuildRequires: catch-devel
BuildRequires: python3-devel
BuildRequires: python3-simplejson
BuildRequires: python3-mmtf
BuildRequires: python3-numpy

# Qt interface
BuildRequires: python3-qt5-devel
BuildRequires: freeglut-devel

# Optional, will fall back to Tk interface
%if 0%{?fedora}
#BuildRequires: python3-pyside2-devel
%endif

Requires: apbs%{?_isa}
Requires: python3-numpy%{?_isa}
Requires: python3-mmtf
Requires: python3-pmw
Requires: python3-tkinter%{?_isa}
Requires: python3-PyQt4%{?_isa}
Requires: chemical-mime-data

Provides: PyMOL%{?_isa} = 0:%{version}-%{release}

%description
PyMOL is a molecular graphics system with an embedded Python
interpreter designed for real-time visualization and rapid generation
of high-quality molecular graphics images and animations. It is fully
extensible and available free to everyone via the "Python"
license. Although a newcomer to the field, PyMOL can already be used
to generate stunning images and animations with ease. It can also
perform many other valuable tasks (such as editing PDB files) to
assist you in your research.

%prep
%autosetup -n %{name}-open-source-%{version} -p1

ln -sr modules/web modules/pymol_web

%generate_buildrequires
%pyproject_buildrequires

%build
export CXXFLAGS="%{optflags}"
%pyproject_wheel -C--global-option='--use-msgpackc=c++11 --use-openmp=yes --jobs `/usr/bin/getconf _NPROCESSORS_ONLN`'

%install
%py3_install -- --use-msgpackc=c++11 --use-openmp=yes --pymol-path=%{python3_sitearch}/%{name}

# Create executable script for running PyMOL
echo "#!/bin/sh" > pymol
echo "export PYMOL_PATH=%{python3_sitearch}/%{name}" >> %{name}
echo "exec %{__python3} %{python3_sitearch}/%{name}/__init__.py \"\$@\"" >> %{name}

cp -a data examples test %{buildroot}%{python3_sitearch}/%{name}/

rm -f %{buildroot}%{python3_sitearch}/%{name}/examples/devel/link_demo.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/examples/devel/particle01.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/examples/devel/particle02.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/test/inp/B03.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/test/inp/B05.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/test/inp/B11.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/test/ref/T01.log

rm -f %{buildroot}%{python3_sitearch}/%{name}/pymol_path/examples/devel/link_demo.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/pymol_path/examples/devel/particle01.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/pymol_path/examples/devel/particle02.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/pymol_path/test/inp/B03.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/pymol_path/test/inp/B05.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/pymol_path/test/inp/B11.py
rm -f %{buildroot}%{python3_sitearch}/%{name}/pymol_path/test/ref/T01.log

mkdir -p %{buildroot}%{_bindir}
install -p -m 755 pymol %{buildroot}%{_bindir}/

desktop-file-install --vendor='' --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

mkdir -p %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

%files
%doc AUTHORS DEVELOPERS README.* ChangeLog
%license LICENSE
%{python3_sitearch}/*.dist-info
%{python3_sitearch}/chempy/
%{python3_sitearch}/pmg_tk/
%{python3_sitearch}/pmg_qt/
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}2/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.0-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.5.0-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.5.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-4
- Exclude pyside2 dependency (rhbz#2098790)

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2.5.0-3
- Rebuild for glew 2.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-1
- Release 2.5.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.4.0-8
- Rebuild for netcdf 4.8.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.4.0-7
- Rebuild for netcdf 4.8.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Antonio Trande <sagitter@fedoraproject.org> 2.4.0-3
- Fix for upstream bug #119 (rhbz#1861558)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Antonio Trande <sagitter@fedoraproject.org> 2.4.0-1
- Release 2.4.0

* Tue Jun 16 2020 Antonio Trande <sagitter@fedoraproject.org> 2.3.0-9
- Patched for using Qt interface (rhbz#1794874)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Antonio Trande <sagitter@fedoraproject.org> 2.3.0-6
- Patched for Python 3.9

* Thu Jan 16 2020 Antonio Trande <sagitter@fedoraproject.org> 2.3.0-5
- Fix default flags for g++

* Tue Dec 31 2019 Antonio Trande <sagitter@fedoraproject.org> 2.3.0-4
- Patched brp-python-bytecompile script

* Sun Dec 08 2019 Antonio Trande <sagitter@fedoraproject.org> 2.3.0-3
- Use metainfodir

* Sun Dec 08 2019 Antonio Trande <sagitter@fedoraproject.org> 2.3.0-2
- Some packaging modifications

* Sat Dec 07 2019 Antonio Trande <sagitter@fedoraproject.org> 2.3.0-1
- Release 2.3.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6.20180321svn4187
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5.20180321svn4187
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-4.20180321svn4187
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3.20180321svn4187
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2.20180321svn4187
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Tim Fenn <tim.fenn@gmail.com> - 2.1.0-1.20180321svn4187
- update to 2.1.0, switch to PyQt

* Mon Feb 26 2018 Tim Fenn <tim.fenn@gmail.com> - 1.9.0-1.20180224svn4178
- update to 1.9.0, includes fix for BZ 1539225

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-5.20170314svn4170
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Jan Beran <jberan@redhat.com> - 1.8.6-4.20170314svn4170
- Fix of both Python 2 and Python 3 dependence issue

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-3.20170314svn4170
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2.20170314svn4170
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Tim Fenn <tim.fenn@gmail.com> - 1.8.6-1.20170314svn4170
- update to 1.8.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4.20161007svn4162
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.8.4-3.20161007svn4162
- Rebuild for glew 2.0.0

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-2.20161007svn4162
- Rebuild for Python 3.6

* Fri Oct 7 2016 Tim Fenn - 1.8.4-1.20161007svn4162
- update to 1.8.4

* Thu Sep 1 2016 Tim Fenn - 1.8.2.2-5.20160625svn4159
- add python3-tkinter requires (BZ 1368810)

* Sat Jul 30 2016 Tim Fenn - 1.8.2.2-4.20160625svn4159
- fix for python requires (BZ 1359812)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2.2-3.20160625svn4159
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jul 16 2016 Tim Fenn - 1.8.2.2-2.20160625svn4159
- fix to pmw requires (BZ 1357051)

* Fri Apr 29 2016 Tim Fenn - 1.8.2.2-1.20160625svn4159
- update to 1.8.2.2
- update to python3

* Sat Mar 12 2016 Tim fenn - 1.8-4.20151208svn4142
- add WM_CLASS patches (BZ 1311626)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3.20151208svn4142
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.8-2.20151208svn4142
- Rebuild for glew 1.13

* Tue Dec 08 2015 Tim Fenn <tim.fenn@gmail.com> - 1.8-1.20151208svn4142
- update to 1.8

* Sat Sep 26 2015 Tim Fenn <tim.fenn@gmail.com> - 1.7.6-2.20150610svn4121
- fix icon and appdata

* Sun Jun 28 2015 Tim Fenn <tim.fenn@gmail.com> - 1.7.6-1.20150610svn4121
- update to 1.7.6 (SVN 4121)
- add appdata.xml

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-3.20141207svn4104
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.4-2.20141207svn4104
- Rebuilt for GCC 5 C++11 ABI change

* Sun Dec 07 2014 Tim Fenn <tim.fenn@gmail.com> - 1.7.4-1.20141207svn4104
- update to 1.7.4 (SVN 4104)

* Tue Sep 16 2014 Tim Fenn <tim.fenn@gmail.com> - 1.7.2-1.20140916svn4087
- update to 1.7.2 (SVN 4087)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3.20140519svn4076
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7.1-2.20140519svn4076
- Replace the python-setuptools-devel BR with pyhton-setuptools

* Tue Jun 17 2014 Tim Fenn <tim.fenn@gmail.com> - 1.7.1-1.20140519svn4076
- update to 1.7.1 (SVN 4076)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3.20140115svn4060
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 07 2014 Tim Fenn <tim.fenn@gmail.com> - 1.7.0-2.20140115svn4060
- fix for error-format-security to maeffplugin.cpp

* Wed Jan 15 2014 Tim Fenn <tim.fenn@gmail.com> - 1.7.0-1.20140115svn4060
- update to 1.7 (SVN 4060)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.6.0-3.20130620svn4032
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2.20130620svn4032
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Tim Fenn <tim.fenn@gmail.com> - 1.6.0-1.20130620svn4032
- update to 1.6 (SVN 4032)
- update svn command to use export, use xz instead of gz compression (BZ 766206)
- includes fixes for graphics/opengl code (BZ 955323)
- include new pymol_web interface

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.5.0.2-6.20120218svn3982
- Rebuild for glew 1.9.0

* Fri Jul 27 2012 Jon Ciesla <limburgher@gmail.com> - 1.5.0.2-5.20120218svn3982
- libGLEW rebuild.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.2-4.20120218svn3982
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 08 2012 Tim Fenn <tim.fenn@gmail.com> - 1.5.0.2-3.20120218svn3982
- remove web module to fix conflict with python-webpy, reported upstream

* Tue May 01 2012 Gökçen Eraslan <gokcen.eraslan@gmail.com> - 1.5.0.2-2.20120218svn3982
- Validate desktop file and add various mimetypes

* Sat Feb 18 2012 Tim Fenn <tim.fenn@gmail.com> - 1.5.0.2-1.20120218svn3982
- update to version 1.5.0.2 (SVN 3982), fixes bug related to loading maps

* Mon Feb 13 2012 Tim Fenn <tim.fenn@gmail.com> - 1.5.0.1-1.20120213svn3978
- update to version 1.5.0.1 (SVN 3978)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-7.20110502svn3947
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.4.1-6.20110502svn3947
- Rebuild for new libpng

* Mon Jun 20 2011 ajax@redhat.com - 1.4.1-5.20110502svn3947
- Rebuild for new glew soname

* Tue Jun 07 2011 Tim Fenn <fenn@stanford.edu> - 1.4.1-4.20110502svn3947
- include missing data directory bits
- remove pre script
- remove pymol_path completely, add patch to init.py to set it properly

* Wed May 18 2011 Tim Fenn <fenn@stanford.edu> - 1.4.1-3.20110502svn3947
- remove old pymol_path directory if necessary using pre script

* Tue May 17 2011 Tim Fenn <fenn@stanford.edu> - 1.4.1-2.20110502svn3947
- fix broken pymol_path and missing shaders issue (BZ 705144)

* Mon May 02 2011 Tim Fenn <fenn@stanford.edu> - 1.4.1-1.20110502svn3947
- update to 1.4.1 (svn 3947)

* Sat Apr 02 2011 Tim Fenn <fenn@stanford.edu> - 1.4-1.20110402svn3938
- update to 1.4 (svn 3938)
- include python web module
- require glew

* Fri Mar 25 2011 Tim Fenn <fenn@stanford.edu> - 1.3-5.20100705svn3911
- add freeglut requires, bz690299

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4.20100705svn3911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.3-3.20100705svn3911
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 06 2010 Tim Fenn <fenn@stanford.edu> - 1.3-2.20100705svn3911
- include pymol-setup.py.patch

* Mon Jul 05 2010 Tim Fenn <fenn@stanford.edu> - 1.3-1.20100705svn3911
- update to SVN 3911, version 1.3

* Mon Mar 15 2010 Tim Fenn <fenn@stanford.edu> - 1.2-10.20100315svn3897
- update to SVN 3897

* Sun Nov 29 2009 Tim Fenn <fenn@stanford.edu> - 1.2-9.20091006svn3866
- pull in python-devel
- add apbs as a Requires
- minor modification to pymol.desktop

* Tue Oct 06 2009 Tim Fenn <fenn@stanford.edu> - 1.2-8.20091006svn3866
- update to SVN 3866, 1.2r2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7.20090709svn3827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Tim Fenn <fenn@stanford.edu> - 1.2-6.20090709svn3827
- include chempy, pmg_tk and tut subdirectories in data folder

* Thu Jul 07 2009 Tim Fenn <fenn@stanford.edu> - 1.2-5.20090709svn3827
- update to SVN 3827, 1.2r1

* Fri Jun 12 2009 Tim Fenn <fenn@stanford.edu> - 1.2-4.20090612svn3729
- update to SVN 3729, fixes contrib module bug

* Wed Apr 08 2009 Tim Fenn <fenn@stanford.edu> - 1.2-3.20090408svn3694
- update to 1.2beta5, aka SVN 3694

* Thu Feb 26 2009 Tim Fenn <fenn@stanford.edu> - 1.2-2.20090226svn3616
- include pymol2 module, update to SVN 3616 (fixes cmd2.py)

* Tue Feb 24 2009 Tim Fenn <fenn@stanford.edu> - 1.2-1.20090224svn3615
- update to trunk svn rev 3615, fixes python 2.6 incompatibility

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-14.20081015svn3468
- Rebuild for Python 2.6

* Thu Oct 30 2008 Jon Ciesla <limb@jcomserv.net> - 1.1-13-20081015svn3468
- Fixed vendor flag per kkofler.

* Wed Oct 29 2008 Tim Fenn <fenn@stanford.edu> - 1.1-12-20081015svn3468
- fix vendor flag, remove space from pymol.desktop

* Tue Oct 28 2008 Tim Fenn <fenn@stanford.edu> - 1.1-11-20081015svn3468
- add vendor flag to desktop-file-install

* Tue Oct 21 2008 Tim Fenn <fenn@stanford.edu> - 1.1-10-20081015svn3468
- add demo files

* Mon Oct 20 2008 Tim Fenn <fenn@stanford.edu> - 1.1-9-20081015svn3468
- minor edit to defattr

* Sat Oct 18 2008 Tim Fenn <fenn@stanford.edu> - 1.1-8-20081015svn3468
- separate pmg_wx into -wxpython package, minor patch fix

* Fri Oct 17 2008 Tim Fenn <fenn@stanford.edu> - 1.1-7-20081015svn3468
- patch setup.py to remove opt flags

* Thu Oct 16 2008 Tim Fenn <fenn@stanford.edu> - 1.1-6-20081015svn3468
- SVN bump, minor edit to pymol.desktop

* Tue Oct 07 2008 Tim Fenn <fenn@stanford.edu> - 1.1-5-20080912svn3419
- fix optflags, svn co comment, buildrequires/requires

* Sun Oct 05 2008 Tim Fenn <fenn@stanford.edu> - 1.1-4-20080912svn3419
- fix license, add AUTHORS to %%doc, add python-numeric to requires
- fix optflags, permissions problems, minor fixes

* Thu Oct 02 2008 Tim Fenn <fenn@stanford.edu> - 1.1-3-20080912svn3419
- fix release tag, add egg-info, minor fixes

* Sun Sep 28 2008 Tim Fenn <fenn@stanford.edu> - 1.1-2
- add desktop file, fix buildrequires, fix SourceURL

* Fri Sep 12 2008 Tim Fenn <fenn@stanford.edu> - 1.1-1
- initial build
