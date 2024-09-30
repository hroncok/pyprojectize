%bcond_with tests_py

%global srcurl  https://github.com/andreikop/%{name}

Name:           enki
Version:        22.08.0
Release:        9%{?dist}
Summary:        Text editor for programmers

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://%{name}-editor.org/

Source0:        %{srcurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch: %{qt5_qtwebengine_arches} noarch

BuildRequires:  python3-devel

BuildRequires:  python3-qt5
BuildRequires:  python3-pyparsing
BuildRequires:  python3-qutepart

# documentation
BuildRequires:  python3-sphinx

# tests
BuildRequires:  desktop-file-utils
%if %{with tests_py}
#BuildRequires:  python3-sip
BuildRequires:  python3-qt5-webengine
BuildRequires:  xorg-x11-server-Xvfb
%endif

# FIXME add more optional dependencies to enable specific tests
BuildRequires:  python3-markdown
BuildRequires:  python3-mock
BuildRequires:  python3-regex

# runtime
Requires:       python3

Requires:       python3-qt5
Requires:       python3-pyparsing
# enforce fix for python 3.10
Requires:       python3-qutepart >= 3.3.2
# FIXME is sphinx optional?
Requires:       python3-sphinx

# FIXME issue#425, markdown is needed as dependency
Requires:       python3-markdown

%if 0%{?fedora}

# optional for special runtime
Recommends:     python3-flake8
Recommends:     python3-docutils
#Recommends:     python3-markdown
Recommends:     python3-regex
Recommends:     ctags
# FIXME do we need QtWebEngine for sure?
# upstream issues/446, rhbz#1642060
Recommends:     python3-qt5-webengine

# upstream issues/465
Suggests:       python3-qtconsole

%endif # fedora

# we place additional icons
Requires:       hicolor-icon-theme

# compatibility, accidently used subpackage, rhbz#1292724
Obsoletes:      %{name}-plugins < 19.10.0

%description
Enki is a text editor for programmers. It is:

    - User friendly. Intuitive interface. Works out of the box. You don’t have
      to read a lot of docs.
    - Hacker friendly. Work as quickly as possible. Navigate efficiently without
      your mouse.
    - Advanced. You invent software. An editor helps you focus on inventing,
      instead of fighting with your tools.
    - Extensible. Operating systems are designed for running applications. Enki
      is designed for running plugins.
    - Cross platform. Use your habitual editor on any OS. Tested on Linux and
      Windows. Users report that Enki works Mac OS X.
    - High quality. No long list of fancy features. But, what is done, is done
      well.
    - Open source. Created, tested, and designed for the community, by the
      community, and with the community.

%package doc
Summary:        Additional documentation for %{name}

%description doc
%{summary}.


%prep
%autosetup -p1 -n%{name}-%{version}
# distutils does not know options entry_points and install_requires: use setuptools instead
sed -i s:distutils\.core:setuptools: setup.py
# skip enforcement of optional dependencies
sed -i -r -e '/flake8/d' -e '/CodeChat/d' -e '/regex/d' setup.py
# ignore useless distribution folders
rm -rv debian rpm win
# skip tests of plugins, too hungry for poor Xvfb
rm -v tests/test_plugins/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
sphinx-build-3 doc html
rm -rv html/.buildinfo html/.doctrees

%install
%pyproject_install
%pyproject_save_files %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# FIXME rhbz#1752766, python3-sip not available
%if %{with tests_py}
# we must be inside the tests folder to let the script find something
pushd tests
# FIXME ugly hackery to disable failing tests
# https://github.com/andreikop/enki/issues/456
sed -i "s:'TRAVIS_OS_NAME' in os.environ:True:" test_base.py
# run tests in a mocked X environment
xvfb-run -s '-screen :0 1024x768x16' %{__python3} run_all.py
%endif


%files -f %{pyproject_files}
%license LICENSE.GPL2
%doc README.md ChangeLog
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%files doc
%license LICENSE.GPL2
%doc html/

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 22.08.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.08.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 22.08.0-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.08.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.08.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.08.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Python Maint <python-maint@redhat.com> - 22.08.0-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.08.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 22.08.0-1
- Update to 22.08.0 (#2117246)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 21.11.0-4
- Rebuilt for pyparsing-3.0.9

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 21.11.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Raphael Groner <raphgro@fedoraproject.org> - 21.11.0-1
- new version, rhbz#2023192
- fix crash with python 3.10, rhbz#2019640
- ignore weak dependencies for builds without fedora

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.03.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20.03.1-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.03.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.03.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.03.1-2
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Raphael Groner <projects.rg@smart.ms> - 20.03.1-1
- new version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Raphael Groner <projects.rg@smart.ms> - 19.10.0-2
- rebuilt (python-qutepart)

* Sat Nov 23 2019 Raphael Groner <projects.rg@smart.ms> - 19.10.0-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 18.08.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 18.08.0-5
- Rebuilt for Python 3.8

* Wed Aug 07 2019 Dan Horák <dan[at]danny.cz> - 18.08.0-4
- set ExclusiveArch as there is dependency on qt5-qtwebengine

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Raphael Groner <projects.rg@smart.ms> - 18.08.0-1
- new version

* Sun Jul 22 2018 Raphael Groner <projects.rg@smart.ms> - 17.03.0-10
- mark markdown as mandatory to fix an issue with setup.py

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.03.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 17.03.0-8
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.03.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Raphael Groner <projects.rg@smart.ms> - 17.03.0-6
- add dependency python3-sphinx

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.03.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Raphael Groner <projects.rg@smart.ms> - 17.03.0-4
- thread regex as optional, too

* Sun May 07 2017 Raphael Groner <projects.rg@smart.ms> - 17.03.0-3
- drop hard dependencies to flake8 and CodeChat, latter not packaged yet

* Tue Mar 28 2017 Raphael Groner <projects.rg@smart.ms> - 17.03.0-2
- mark optional dependencies

* Tue Mar 28 2017 Raphael Groner <projects.rg@smart.ms> - 17.03.0-1
- Update to 17.03.0 (#1436456)
- use setuptools instead of distutils
- explicitly set screen depth for tests: qt dropped support for depth 8
- add verbose option to rm

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.04.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 16.04.1-5
- Rebuild for Python 3.6

* Thu Dec 08 2016 Builder <projects.rg@smart.ms> - 16.04.1-4
- rebuilt for Qt 5.7.1

* Tue Aug 30 2016 Raphael Groner <projects.rg@smart.ms> - 16.04.1-3
- rhbz#1365138, add python3-pyparsing and drop python2 relations
- reorder dependency list for better overview

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.04.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Raphael Groner <projects.rg@smart.ms> - 16.04.1-1
- new version
- drop upstreamed patch

* Mon May 09 2016 Raphael Groner <projects.rg@smart.ms> - 16.04.0-3
- fix TypeError: decorated slot, rhbz#1332274

* Sun Apr 24 2016 Raphael Groner <projects.rg@smart.ms> - 16.04.0-2
- add R: python3-qt5-webkit, enki does not work without

* Fri Apr 22 2016 Raphael Groner <projects.rg@smart.ms> - 16.04.0-1
- bump to v16.04.0

* Thu Mar 24 2016 Raphael Groner <projects.rg@smart.ms> - 15.11.2-0.3.20160227git8e374ef
- remove obsolete workarounds

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 15.11.2-0.2
- Requires: python3-qt5-webkit

* Sun Feb 28 2016 Raphael Groner <projects.rg@smart.ms> - 15.11.2-0.1
- v15.11.2, maybe 15.12.0 or similiar, but pre1
- move to python3 and qt5

* Sat Feb 27 2016 Raphael Groner <projects.rg@smart.ms> - 15.11.1-3
- rebuild to validate dependencies (crash in koschei)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 15.11.1-1
- Update to 15.11.1 (#1297567)

* Sat Jan 09 2016 Raphael Groner <projects.rg@smart.ms> - 15.11.0-2
- merge plugins subpackage, rhbz#1292724

* Thu Dec 03 2015 Raphael Groner <projects.rg@smart.ms> - 15.11.0-1
- new version
- add python-regex
- remove license breakdown, now generally GPLv2+
- remove Suggests: enki-plugins

* Tue Nov 17 2015 Raphael Groner <projects.rg@smart.ms> - 15.05.0-2
- fix license breakdown
- ignore useless distribution folders
- use python macros to build and install
- split plugins into subpackage

* Fri Nov 13 2015 Raphael Groner <projects.rg@smart.ms> - 15.05.0-1
- continue review
- new upstream version
- add proper snippets for mime database and icon cache
- generate documentation
- execute tests

* Thu May 7 2015 Jairo Llopis <yajo.sk8@gmail.com> 14.07.2-7
- New upstream version.
- Updated dependencies.
- Updated description.
- Remove translations.

* Mon Jul 7 2014 Jairo Llopis <yajo.sk8@gmail.com> 14.03.0-6
- New upstream version.
- Fix some macros in the spec file.

* Sun Oct 6 2013 Jairo Llopis <yajo.sk8@gmail.com> 13.09.2-5
- Add dependency to python-docutils.

* Sun Oct 6 2013 Jairo Llopis <yajo.sk8@gmail.com> 13.09.2-4
- New upstream version.

* Sun Sep 8 2013 Jairo Llopis <yajo.sk8@gmail.com> 13.08.1-3
- New upstream version, now based on qutepart.
- Remove patch that has already been merged upstream.

* Tue Jul 16 2013 Jairo Llopis <yajo.sk8@gmail.com> 12.10.3-2
- Declare variables with global.
- Link patch0 to its upstream bug.
- Validate desktop file installation.
- Add icon cache scriptlets.
- Change Source tag for Source0.
- Fix requirements.

* Sat Jul 6 2013 Jairo Llopis <yajo.sk8@gmail.com> 12.10.3-1
- Initial release.
