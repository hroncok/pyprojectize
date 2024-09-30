Name:           PyX
Version:        0.16
Release:        8%{?dist}
Summary:        Python graphics package

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pyx-project.org/
Source0:        https://files.pythonhosted.org/packages/source/P/PyX/PyX-%{version}.tar.gz

# Patches from Debian
Patch0:         manual-pythonpath.patch
Patch1:         sphinx-local-mathjax.patch
Patch2:         sphinx-no-eager-only.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  ghostscript
BuildRequires:  python3dist(sphinx)

#BuildRequires:  texlive-collection-latexextra
BuildRequires:  texlive-lib-devel
BuildRequires:  texlive-collection-latexrecommended
BuildRequires:  latexmk
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(tgtermes.sty)
BuildRequires:  tex(wrapfig.sty)

Requires:       tex(latex)
Provides:       python3-pyx = %{version}-%{release}

%description
PyX is a Python package for the creation of PostScript and PDF files. It
combines an abstraction of the PostScript drawing model with a TeX/LaTeX
interface. Complex tasks like 2d and 3d plots in publication-ready quality are
built out of these primitives.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
%{Summary}

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
# Set the extensions to be built
%{__sed} -i 's|^build_t1code =.*|build_t1code = 1|' setup.cfg
%{__sed} -i 's|^build_pykpathsea =.*|build_pykpathsea = 1|' setup.cfg

%{pyproject_wheel}

# turn on ipc in config file
%{__sed} -i 's|^texipc =.*|texipc = 1|' pyx/data/pyxrc

pushd faq
%{__sed} -i 's|sphinx-build|sphinx-build-3|' Makefile
make
make html
mv _build/html/ faq
mv _build/latex/pyxfaq.pdf ..
popd

pushd manual
%{__sed} -i 's|sphinx-build|sphinx-build-3|' Makefile
make
make html
mv _build/html/ manual
mv _build/latex/manual.pdf ..
popd

%install
rm -rf %{buildroot}
%{pyproject_install}
%pyproject_save_files pyx

%{__mkdir} %{buildroot}%{_sysconfdir}
%{__cp} -a pyx/data/pyxrc %{buildroot}%{_sysconfdir}/pyxrc

# Fix the non-exec with shellbang rpmlint errors
for file in `find %{buildroot}%{python3_sitearch}/pyx -type f -name "*.py"`; do
  [ ! -x ${file} ] && %{__sed} -i 's|^#!|##|' ${file}
done


%files -f %{pyproject_files}
%license LICENSE
%doc AUTHORS CHANGES PKG-INFO README.md
%config(noreplace) %{_sysconfdir}/pyxrc

%files doc
%license LICENSE
%doc *.pdf
%doc faq/faq manual/manual
%doc contrib/
%doc examples/

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.16-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.16-6
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.16-2
- Rebuilt for Python 3.12

* Thu Mar 23 2023 José Matos <jamatos@fedoraproject.org> - 0.16-1
- Update to 0.16
- Remove patch already included in this version

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.15-9
- Rebuilt for Python 3.11

* Wed Feb  2 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.15-8
- fix extension module with Python 3.10

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15-5
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 José Matos <jamatos@fedoraproject.org> - 0.15-1
- Update to 0.15
- Turn on the pdf generation
- Add several patches from Debian

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-13
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 José Matos <jamatos@fedoraproject.org> - 0.14.1-9
- fix BuildRequires
- disable for the moment the pdf manual and faq

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-8
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 12 2016 José Matos <jamatos@fedoraproject.org> - 0.14.1-1
- update to 0.14.1
- remove patch (already present in this version)
- source changed to pypi
- make virtual provides versionned

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 23 2015 José Matos <jamatos@fedoraproject.org> - 0.14-1
- Update to 0.14
- Since version 0.13 only supports python 3
- Add -doc subpackage
- Provides python3-pyx

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 José Matos <jamatos@fedoraproject.org> - 0.12.1-1
- update to 0.12.1
- add the PyX FAQ to the documentation
- Provides python2-pyx since this is the latest version to support python2

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Jindrich Novy <jnovy@redhat.com> 0.11.1-4
- rebuild against new kpathsea in TeX Live 2012

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 José Matos <jamatos@fedoraproject.org> - 0.11.1-1
- New upstream release
- Clean spec file

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 30 2009 José Matos <jamatos@fc.up.pt> - 0.10-8
- Disable faq pdf generation for now (it breaks the build)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10-5
- Rebuild for Python 2.6

* Thu Feb 14 2008 José Matos <jamatos[AT]fc.up.pt> - 0.10-4
- Rebuild for gcc 4.3

* Sat Jan 12 2008 José Matos <jamatos[AT]fc.up.pt> - 0.10-3
- egg-info is in sitearch...

* Fri Jan 11 2008 José Matos <jamatos[AT]fc.up.pt> - 0.10-2
- Add egg-info to F9+.

* Fri Jan 11 2008 José Matos <jamatos[AT]fc.up.pt> - 0.10-1
- New upstream release (#426816).
- Package cleanup.

* Tue Aug 28 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9-5
- License fix, rebuild for devel (F8).

* Mon Dec 11 2006 José Matos <jamatos[AT]fc.up.pt> - 0.9-4
- Rebuild for python 2.5.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 José Matos <jamatos[AT]fc.up.pt> - 0.9-2
- Rebuild for FC-6.
- Unghost .pyo files.

* Sat Jun 03 2006 Michael A. Peters <mpeters@mac.com> - 0.9-1
- New upstream release (closes bug #193956)

* Sun Apr 30 2006 Michael A. Peters <mpeters@mac.com> - 0.8.1-4
- Fixed rpmlint errors noted in 190247#3
- Don't build pykpathsea C module for x86_64 (Bug #150085)

* Sat Apr 29 2006 Michael A. Peters <mpeters@mac.com> - 0.8.1-3
- Fixed a typo in the borrowed SuSE patch

* Sat Apr 29 2006 Michael A. Peters <mpeters@mac.com> - 0.8.1-2
- Fix improper siteconfig.py (Patch0, borrowed from SuSE)
- alter default config file (turn texipc on)
- BuildRequires python-devel >= 2.2

* Sat Apr 29 2006 Michael A. Peters <mpeters@mac.com> - 0.8.1-1
- Initial packaging for Fedora Extras
