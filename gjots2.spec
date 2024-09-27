# -*-Mode: rpm-spec -*-

Name:    gjots2
Version: 3.2.1
Release: 7%{?dist}
Summary: A hierarchical note jotter - organize your ideas, notes, facts in a tree
License: GPL-2.0-only
URL:     http://bhepple.freeshell.org/gjots
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: python3-gobject
Requires: gtk3

# epel has gtksourceview3 only. f-31/2 also have gtksourceview4. Maybe use weak dependencies?
Requires: gtksourceview3

%description

gjots2 ("gee-jots" or, if you prefer, "gyachts"!) is a way to marshal
and organize your text notes in a convenient, hierarchical way. For
example, use it for all your notes on Unix, personal bits and pieces,
recipes and even PINs and passwords (encrypted with ccrypt(1), gpg(1)
or openssl(1)).

You can also use it to "mind-map" your compositions - write down all
your thoughts and then start to organize them into a tree. By
manipulating the tree you can easily reorder your thoughts and
structure them appropriately.

%prep
%autosetup -p1

# Convert to utf-8
for file in doc/man/man1/*.1; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

rm -rf %{buildroot}%{_datadir}/doc/gjots2-%{version}/

for file in $(find po/ -name gjots2.mo | sed 's|po/||') ; do
  install -Dpm0644 po/$file %{buildroot}%{_datadir}/locale/$file
done

%find_lang %{name}

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications              \
        --remove-category Application                           \
        %{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files -f gjots2.lang
%license COPYING
%doc AUTHORS ChangeLog README doc/gjots2.gjots
%doc %lang(en_US) doc/gjots2.en_US.gjots
%doc %lang(fr) doc/gjots2.fr.gjots
%doc %lang(nb) doc/gjots2.nb.gjots
%doc %lang(no) doc/gjots2.no.gjots
%doc %lang(ru) doc/gjots2.ru.gjots
%doc %lang(es) doc/gjots2.es.gjots
%{_bindir}/gjots2
%{_bindir}/gjots2org
%{_bindir}/org2gjots
%{_bindir}/gjots2html*
%{_bindir}/gjots2docbook
%{_bindir}/docbook2gjots
%{_bindir}/gjots2emacs
%{_bindir}/gjots2lpr
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}.dist-info
%{_datadir}/%{name}/
%{_datadir}/pixmaps/gjots2.png
%{_datadir}/metainfo/gjots2.metainfo.xml
%{_datadir}/applications/*gjots2.desktop
%{_datadir}/glib-2.0/schemas/org.gtk.gjots2.gschema.xml
%{_mandir}/man1/%{name}*
%{_mandir}/man1/docbook2gjots*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.1-6
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Bob Hepple <bob.hepple@gmail.com> - 3.2.1-1
- new version
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Bob Hepple <bob.hepple@gmail.com> - 3.2.0-2
- rebuilt

* Tue Dec 20 2022 Bob Hepple <bob.hepple@gmail.com> - 3.2.0-1
- new version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.9-7
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.9-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Bob Hepple <bob.hepple@gmail.com> - 3.1.9-1
- ui/about.ui: remove redundant translater credits - seems to have no effect here
- fix: some environments don't always show images in buttons
- add tooltip for Find button
- fix: printDialog needed import gi, os; was using old mktemp
- Change popup dialogs type to 'top-level' instead of 'popup'!!! -
- as documented on GtkWindow page - avoids the message: Window
  0x560942cc2d60 is a temporary window without parent, application
  will not be able to position it on screen.

* Mon Jun 29 2020 Bob Hepple <bob.hepple@gmail.com> - 3.1.8-1
- fix popup context menus (right click on tree)
- fix locale_dir when running from source tree
- add LC_ALL=zh_TW translation
- accomodate installation to any $prefix with setup.py
- fix tree_select_all
- fine tune python version requirement to >= 3.6.8 for epel8
- try for gtksourceview4 and failover to gtksourceview3

* Wed Jun 24 2020 Bob Hepple <bob.hepple@gmail.com> - 3.1.7-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.6-3
- Rebuilt for Python 3.9

* Sun May 03 2020 Bob Hepple <bob.hepple@gmail.com> - 3.1.6-2
- remove BR for python3-setuptools

* Sun May 03 2020 Bob Hepple <bob.hepple@gmail.com> - 3.1.6-1
- rebuilt in response to RHBZ#1823599

* Sat May 02 2020 Bob Hepple <bob.hepple@gmail.com> - 3.1.5-1
- in response to RHBZ#1823599

* Sun Apr 19 2020 <bob.hepple@gmail.com> - 3.1.4-1
- Update more FSF addresses
- Change shebangs to absolute paths (fedora required)
- Change appdata to metainfo

* Fri Apr 17 2020 <bob.hepple@gmail.com> - 3.1.3-1
- new version upstream - fixed FSF address

* Sun Mar 08 2020 <bob.hepple@gmail.com> - 3.1.2-2
- minor spec file fixes

* Sun Mar 08 2020 <bob.hepple@gmail.com> - 3.1.2-1
- merged fedora-30 spec file
