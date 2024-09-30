%define BothRequires() \
Requires:		%1 \
BuildRequires:	%1 \
%{nil}

%global		native_wayland	1

%global		majorver		4.18
%define		mainver		4.18.0
%undefine		betaver		

%define		baserelease		5

Name:		catfish
Version:	%{mainver}
Release:	%{?betaver:0.}%{baserelease}%{?betaver:.%betaver}%{?dist}
Summary:	A handy file search tool

# SPDX confirmed
License:	GPL-2.0-only
URL:		https://docs.xfce.org/apps/catfish/start
Source0:	https://archive.xfce.org/src/apps/catfish/%{majorver}/catfish-%{version}%{?betaver}.tar.bz2
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool

BuildRequires:	python3-devel
BuildRequires:	python3-distutils-extra
BuildRequires:	/usr/bin/appstream-util

# python module
%BothRequires	python3-gobject
%BothRequires	python3-pexpect
%BothRequires	python3-dbus

# gir repository
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	gobject-introspection
Requires:	gtk3 >= 3.10.0
Requires:	pango
Requires:	xfconf
# optional zeitgeist dependency not listed
# /usr/share/mime/globs2
Requires:	shared-mime-info
# opening file uses this
Requires:	%{_bindir}/xdg-open
# search engine
Requires:	%{_bindir}/locate
# icon
# Requires:	redhat-artwork

%description
Catfish is a handy file searching tool. The interface is
intentionally lightweight and simple, using only GTK+3.
You can configure it to your needs by using several command line
options.


%prep
# Because %%build is not allowed to write files under %%buildroot,
# and calling setup.py --installed with target root under unpackaged directory
# causes some trouble, here once create temporaily directory
# and unpack source after that

%setup -q -T -c -a 0 %{name}-%{mainver}%{?betaver}
pushd %{name}-%{mainver}*

# Fix up permissions...
find . -type f -print0 | xargs --null chmod 0644
chmod 0755 bin/%{name}

popd

%generate_buildrequires
%pyproject_buildrequires

%build
TOPDIR=$(pwd)

pushd %{name}-%{mainver}*

# Remove unneeded shebang
grep -rl "/usr/bin/env" . | \
	xargs sed -i -e "\@/usr/bin/env[ ][ ]*python@d"


#%%pyproject_wheel
# separation of build / install --skip-build not supported
# (separation causes some error for creating additional files
#  such as desktop file, also installation directory gets wrong)

mkdir -p ./_TMPINSTDIR/python3
%__python3 setup.py \
	install \
	--root ${TOPDIR}/_TMPINSTDIR/python3

popd

%install
cp -a %{name}-%{mainver}*/[A-Z]* .

#%%pyproject_install
cp -a _TMPINSTDIR/python3/* %{buildroot}

# Explicitly set GDK_BACKEND
%if ! 0%{?native_wayland}
# Release notes says 1.4.12 has wayland support
# But 4.16.0 gets wayland error again:
# https://bugzilla.redhat.com/show_bug.cgi?id=1920378
# https://gitlab.xfce.org/apps/catfish/-/issues/42

mkdir %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/catfish %{buildroot}%{_libexecdir}/
cat > %{buildroot}%{_bindir}/catfish <<EOF
#!/usr/bin/bash

export GDK_BACKEND=x11
exec %{_libexecdir}/catfish \$@
EOF
chmod 0755 %{buildroot}%{_bindir}/catfish

%endif

# for backwards compatibility:
ln -s catfish %{buildroot}%{_bindir}/catfish-py3


pushd %{name}-%{mainver}*

# Install man page manually
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -cpm 0644 ./%{name}.1 %{buildroot}%{_mandir}/man1/

popd

# Remove all unnecessary documentation
%{__rm} -rf %{buildroot}%{_datadir}/doc/

# Rename desktop files for now
pushd %{buildroot}%{_datadir}/applications/
mv *desktop %{name}.desktop
popd

%{find_lang} %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files -f %{name}.lang
%doc AUTHORS
%doc NEWS
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-py3

%if ! 0%{?native_wayland}
%{_libexecdir}/%{name}
%endif

%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.xfce.%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}_lib/
%{python3_sitelib}/%{name}-%{version}.dist-info


%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.18.0-4
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.18.0-1
- 4.18.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.4-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.16.4-1.2
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 29 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.16.4-1
- 4.16.4

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.3-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.16.3-2.2
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct  3 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.16.3-2
- get_exo_preferred_file_manager: check if the requested key exists before actually use it
  (bug 2009994)

* Thu Sep 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.16.3-1
- 4.16.3
- List gir repository dependency explicitly

* Wed Aug  4 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.16.2-1
- 4.16.2

* Tue Jul 27 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.16.1-1
- 4.16.1
- Build with native wayland support on F-35+

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.16.0-2.1
- Rebuilt for Python 3.10

* Sun Jan 31 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.16.0-2
- Add GDK_BACKEND=x11 wrapper again (bug 1920378, upstream bug 42)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.16.0-1
- 4.16.0

* Tue Oct 27 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.15.0-1
- 4.15.0 (versioning scheme changed)

* Thu Oct  1 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-2
- Fix crash when some extensional scheme (supported by Thunar, PcmanFM,
  for example) is used (bug 1883688)

* Wed Sep 30 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.13-1
- 1.4.13
- Remove x11 backend wrapper, 1.4.12 says wayland is supported
- Patch to support python 3.9

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.11-1.2
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.11-1
- 1.4.11

* Tue Sep 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.10-1
- 1.4.10

* Fri Sep 13 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.8-2
- set GDK_BACKEND as x11 explicitly (ref: bug 1702891)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.8-1.1
- Rebuilt for Python 3.8

* Sun Aug 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.8-1
- 1.4.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.7-1
- 1.4.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5-4
- Some packaging fixes

* Mon Jul 16 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-4
- Only have one Python version (only the Python 3 implementation is provided)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-1.1
- Rebuilt for Python 3.7

* Mon May  7 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5-1
- 1.4.5

* Fri Feb 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.4-2
- spec file craft: move %%description out of %%_fedora scope

* Fri Feb 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.4-1
- 1.4.4

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.2-3.1
- Remove obsolete scriptlets

* Sat Nov 18 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.2-3
- Fix up python2 namespace script bug manually

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2.1
- Rebuild for Python 3.6

* Wed Aug 17 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.2-2
- Support python3 for F-25+ (only)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-1.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.2-1
- 1.4.2

* Sun Mar  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-1
- 1.4.1

* Mon Feb 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.4-2
- Bump release

* Sun Feb 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.4-1
- 1.3.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.3-1
- 1.3.3

* Thu Oct  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-2
- Fix traceback on en_US locale with non-sudoer user
  (bug 1266785)

* Thu Sep 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-1
- 1.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct  1 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-1
- 1.2.2

* Mon Sep  8 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-1
- 1.0.2

* Sun Mar 02 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1
- Fix insecure loading of script at startup (CVE-2014-2093 through 
  CVE-2014-2096, bug 1069398)

* Sat Feb 15 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Thu Oct  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.4-1
- 0.6.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.2-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0.2-3
- Fix GError module error on launch (bug 964356)
- Fix infinite loop when searching words with asterisk (bug 964356)

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.4.0.2-2.1
- Update stock_info patch so that build completes

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0.2-2
- F-19: kill vendorization of desktop file (fpc#247)

* Fri Oct 05 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0.2-1
- Update to 0.4.02 (GTK3 port)
- Require pygobject3 instead of pygtk2-libglade

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr  4 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.3.2-5
- Remove pinot dependency, seems no longer available

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.3.2-4
- Don't use missing gtk.STOCK_INFO (bug 753512)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-14: rebuild against python 2.7

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.2-3
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.2-2
- GTK icon cache updating script update

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com>
- Rebuild for Python 2.6

* Tue Oct 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3.2-1
- 0.3.2

* Thu Oct 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-1
- 0.3

* Fri Oct  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.3.c
- Remove beagle dependency for now because beagle is not
  available on ppc64 (although catfish itself is noarch :( )

* Wed Oct  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.2.c
- License update
- Create sub-metapackage to install all supported search engines
- Remove redhat-artwork dependency

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.c
- 0.3c

* Tue May 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.b
- 0.3b

* Wed Apr  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.a
- 0.3a

* Wed Feb 28 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2.2-1
- 0.2.2

* Sun Feb 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2.1-1
- 0.2.1

* Wed Feb 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2stable-1
- 0.2

* Wed Jan 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2d-1
- 0.2d

* Mon Jan 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2c-1
- 0.2c

* Sun Jan 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2b-1
- Upstream rename: search4files -> catfish
- Remove the dependencies for beagle, nautilus,
  replace with redhat-artwork

* Mon Jan  1 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2a-1
- 0.2a

* Sat Dec 23 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Require pyxdg again (fc7)

* Wed Dec 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1e-1
- 0.1e

* Thu Dec 14 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1d-1
- 0.1d
- Disable pyxdg support on devel for now.

* Sat Dec  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1c-2
- Fix type typo

* Fri Dec  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1c-1
- Initial packaging to import to Fedora Extras.
