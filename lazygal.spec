Name:           lazygal
Version:        0.10.9
Release:        3%{?dist}
Summary:        A static web gallery generator

License:        GPL-2.0-or-later AND MIT
URL:            https://sml.zincube.net/~niol/repositories.git/lazygal/about/
Source0:        https://sml.zincube.net/~niol/repositories.git/lazygal/snapshot/lazygal-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  /usr/bin/ffmpeg
BuildRequires:  /usr/bin/ffprobe
BuildRequires:  gettext
BuildRequires:  js-jquery
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-gexiv2
BuildRequires:  python3-genshi
BuildRequires:  python3-pillow
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe
Requires:       js-jquery
Requires:       python3-gexiv2
Requires:       python3-genshi
Requires:       python3-pillow
Provides:       bundled(jquery.tipTip.js) = 1.3
Provides:       bundled(respond.js) = 1.4.2
Provides:       bundled(jquery.colorbox.js) = 1.4.36
# still bundled JS in themes/
# inverted/SHARED_plugins.tjs TipTip 1.3 https://github.com/drewwilson/TipTip
# inverted/SHARED_respond.js https://github.com/scottjehl/Respond
# singlepage/SHARED_jquery.colorbox.js Colorbox v1.4.36 - http://www.jacklmoore.com/colorbox (available via npm)

%description
Lazygal is another static web gallery generator written in Python.
It can be summed up by the following features :
* Command line based (thus scriptable).
* Handles album updates.
* Presents all your pictures and videos and associated data.
* Makes browsing sharing pictures easy.
* Make customization easy.
* Does not change your original pictures directories (the source argument).

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%{__python3} setup.py build_i18n
%{__python3} setup.py build_manpages

%install
%pyproject_install
install -dm755 %{buildroot}%{_mandir}/man{1,5}
install -pm644 man/lazygal.1 %{buildroot}%{_mandir}/man1/
install -pm644 man/lazygal.conf.5 %{buildroot}%{_mandir}/man5/
install -dm755 %{buildroot}%{_datadir}/locale
cp -pr build/mo/* %{buildroot}%{_datadir}/locale/

%find_lang %{name}

%check
%{__python3} setup.py test

%files -f %{name}.lang
%license COPYING
%doc README.md TODO ChangeLog
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info
%{python3_sitelib}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.10.9-2
- Rebuilt for Python 3.13

* Tue Mar 19 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.10.9-1
- update to 0.10.9 (#2262048)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.10.8-1
- update to 0.10.8 (#2249340)

* Thu Aug 24 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.10.7-1
- update to 0.10.7 (#2216216)
- Add dependency on ffmpeg for video support and tests
- Switch License: tag to SPDX

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.10.5-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.5-2
- Rebuilt for Python 3.11

* Thu Mar 10 2022 Dominik Mierzejewski <dominik@greysector.net> - 0.10.5-1
- update to 0.10.5 (#2061080)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Dominik Mierzejewski <rpm@greysector.net> - 0.10.3-1
- update to 0.10.3 (#2021027)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.10

* Thu Feb 18 2021 Dominik Mierzejewski <rpm@greysector.net> - 0.10.2-1
- update to 0.10.2 (#1925981)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Dominik Mierzejewski <rpm@greysector.net> - 0.10.1-1
- update to 0.10.1 (#1888371)
- drop obsolete patches
- BuildRequire setuptools explicitly

* Mon Aug 31 2020 Dominik Mierzejewski <rpm@greysector.net> - 0.10-1
- update to 0.10 (#1873092)
- upstream switched from GStreamer to FFmpeg, so drop GStreamer dependencies
- backport upstream commit to skip tests which depend on FFmpeg
- backport upstream commit to fix user comment test with recent gexiv2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Dominik Mierzejewski <rpm@greysector.net> - 0.9.4-1
- update to 0.9.4 (#1836851)
- drop obsolete patch

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-10
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Dominik Mierzejewski <rpm@greysector.net> - 0.9.3-9
- Rebase to current git HEAD to fix build with Python 3.9
- Drop obsolete patches and work-arounds
- Switch from xsltproc to pandoc
- Use modern jquery

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.9.3-4
- fix two test failures

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.3-2
- Add BR:glibc-langpack-en
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Nov 03 2018 Dominik Mierzejewski <rpm@greysector.net> - 0.9.3-1
- update to 0.9.3 (#1643661)
- update URLs
- use license macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-2
- Rebuild for Python 3.6

* Fri Nov 18 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.9.1-1
- update to 0.9.1 (#1390795)
- drop obsolete patches

* Fri Nov 11 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.9-2
- backport fix for bad author tag decoding test

* Fri Nov 04 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.9-1
- update to 0.9 (#1390795)
- backport a patch to use the default nojs theme
- add missing gstreamer dependencies for video processing
- switch to python3

* Mon Aug 22 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.8.8-2
- fix broken dependency after libgexiv2-python2 rename

* Fri Oct 09 2015 Dominik Mierzejewski <rpm@greysector.net> - 0.8.8-1
- update to 0.8.8
- unbundle jquery
- enable testsuite
- use new python convenience macros
- add a soft dependency on python-gstreamer1
- add required Provides: for bundled JavaScript libraries

* Wed Jul 23 2014 Dominik Mierzejewski <rpm@greysector.net> - 0.8.4-2
- drop Group: tag
- fix manpages listing in file list

* Sun Jul 20 2014 Dominik Mierzejewski <rpm@greysector.net> - 0.8.4-1
- update to 0.8.4
- split BRs and Requires into separate lines and sort
- drop redundant specfile parts
- use python version-specific macros

* Fri Jul 30 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-6
- add patch to fix broken imports under python 2.7

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 8 2009 Byron Clark <byron@theclarkfamily.name> 0.4.1-3
- Use python-devel in place of python for BuildRequires.
- Add TODO and ChangeLog to docs.
- Add spacing to changelog entries.

* Mon May 25 2009 Byron Clark <byron@theclarkfamily.name> 0.4.1-2
- Fix typo in upstream URL.

* Sun May 24 2009 Byron Clark <byron@theclarkfamily.name> 0.4.1-1
- Initial release
