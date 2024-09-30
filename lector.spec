Name:       lector
Summary:    Ebook reader and collection manager
URL:        https://github.com/BasioMeusPuga/Lector
Version:    0.5.1
Release:    17%{?dist}
BuildArch:  noarch

# Lector uses GPLv3, the bundled Rarfile library uses the MIT license.
# Automatically converted from old format: GPLv3 and MIT - review is highly recommended.
License: GPL-3.0-only AND LicenseRef-Callaway-MIT

Source0: https://github.com/BasioMeusPuga/Lector/archive/%{version}/%{name}-%{version}.tar.gz
# TODO: Remove after it's fully merged into upstream's build scripts, in the next release.
Source1: https://raw.githubusercontent.com/terrycloth/Lector/packaging/lector/resources/raw/io.github.BasioMeusPuga.Lector.metainfo.xml

BuildRequires: desktop-file-utils
BuildRequires: hicolor-icon-theme
BuildRequires: libappstream-glib
BuildRequires: python3dist(beautifulsoup4) >= 4.6
BuildRequires: python3-devel >= 3.6
BuildRequires: python3-poppler-qt5 >= 0.24.2
BuildRequires: python3-PyQt5 >= 5.10.1
BuildRequires: pkgconfig(Qt)

Requires: hicolor-icon-theme
Requires: python3 >= 3.6
Requires: python3dist(beautifulsoup4) >= 4.6
Requires: python3dist(lxml) >= 4.3
Requires: python3-poppler-qt5 >= 0.24.2
Requires: python3dist(pymupdf) >= 1.14.5
Requires: python3-PyQt5 >= 5.10.1
Requires: python3dist(xmltodict) >= 0.11

Recommends: python3dist(python-djvulibre) >= 0.8.4
Recommends: python3dist(markdown) >= 3.0.1
Recommends: python3dist(textile) >= 3.0.4

%description
Lector is an ebook reader and collection manager. It offers a
full-screen distraction-free view, document highlighting and
annotations, a built-in dictionary, bookmarks, and multiple profiles for
changing the way the books are presented. Lector can also edit metadata,
so you can correct information about the books, and add keywords to make
them easier to find.

It supports the following file formats:

* PDF
* EPUB
* DjVu
* FictionBook (.fb2)
* Mobipocket (.mobi)
* Amazon Kindle (.azw, .azw3, .azw4)
* Comic book archives (.cbr, .cbz)
* Markdown




%prep
%autosetup -n Lector-%{version}
# These files contain a Python shebang, but seem to get installed by upstream's setup.py without an executability bit set, so there's a mismatch in whether it's supposed to be executable...
chmod -x ./lector/KindleUnpack/compatibility_utils.py
chmod -x ./lector/KindleUnpack/mobi_split.py
chmod -x ./lector/KindleUnpack/unipath.py
chmod -x ./lector/__main__.py
chmod -x ./lector/rarfile/dumprar.py
# Non-executable Python files don't need a shebang line.
find ./  -type f  -iname "*.py"  '!' -executable  -exec sed --regexp-extended 's|^#! */usr/bin/env python[[:digit:]._-]*$||g'  --in-place '{}' ';'
# For executable Python files, don't use env python.
find ./  -type f  -iname "*.py"  -executable  -exec sed --regexp-extended 's|^#! */usr/bin/env python[[:digit:]._-]*$|#!%{__python3}|g'  --in-place '{}' ';'



%generate_buildrequires
%pyproject_buildrequires



%build
%pyproject_wheel
mv  ./lector/rarfile/LICENSE  ./LICENSE-rarfile



%install
%pyproject_install
%pyproject_save_files 'lector*'

# TODO: When upstream merges the .metainfo.xml and .desktop file changes and adds them to setup.py, I won't need to manually install SOURCE1 metainfo, nor rename the .desktop file anymore.
# Solved by a pull request here <https://github.com/BasioMeusPuga/Lector/pull/120>
# and should be part of the next upstream release.
mkdir -p %{buildroot}/%{_metainfodir}/
cp --archive  %{SOURCE1}  %{buildroot}/%{_metainfodir}/
mv  %{buildroot}/%{_datadir}/applications/lector.desktop  %{buildroot}/%{_datadir}/applications/io.github.BasioMeusPuga.Lector.desktop

# TODO: When upstream moves the install location for the icon or switches to an actual scalable format, I won't need to move the icon anymore.
# See <https://github.com/BasioMeusPuga/Lector/issues/138>
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/
mv  %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/Lector.png  %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/Lector.png

# TODO: I won't need to remove these duplicate files when upstream fixes their build script.
# See <https://github.com/BasioMeusPuga/Lector/issues/63>
rm -rf  %{buildroot}/%{python3_sitelib}/lector/resources/raw/


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.github.BasioMeusPuga.Lector.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/io.github.BasioMeusPuga.Lector.metainfo.xml



%files -f %{pyproject_files}
%doc      AUTHORS  README.md
%license  LICENSE  LICENSE-rarfile
%{_bindir}/%{name}
%{_datadir}/applications/io.github.BasioMeusPuga.Lector.desktop
%{_datadir}/icons/hicolor/512x512/apps/Lector.png
%{_metainfodir}/io.github.BasioMeusPuga.Lector.metainfo.xml



%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.5.1-15
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.5.1-11
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.1-8
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.1-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 1 2020 Audrey Toskin <audrey@tosk.in> - 0.5.1-3
- Minor spec fix: Add hicolor-icon-theme as a BuildRequire.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Dec 18 2019 Audrey Toskin <audrey@tosk.in> - 0.5.1-1
- New package.
