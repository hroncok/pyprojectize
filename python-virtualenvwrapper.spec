%global modname virtualenvwrapper
%global desc virtualenvwrapper is a set of extensions to Ian Bicking's \
`virtualenv <http://pypi.python.org/pypi/virtualenv>`_ tool.  The extensions \
include wrappers for creating and deleting virtual environments and otherwise \
managing your development workflow, making it easier to work on more than \
one project at a time without introducing conflicts in their dependencies.
%global sum Enhancements to virtualenv

Name:             python-%{modname}
Version:          4.8.4
Release:          10%{?dist}
Summary:          %{sum}

License:          MIT
URL:              https://pypi.python.org/pypi/%{modname}
Source0:          https://pypi.python.org/packages/source/v/%{modname}/%{modname}-%{version}.tar.gz
Patch0:           python-virtualenvwrapper-4.8.4-default-binaries.patch
# Don’t call deprecated egrep wrapper. Fix from upstream:
# https://github.com/python-virtualenvwrapper/virtualenvwrapper/commit/168db18a65bf14c39434670683e86efc210b1f7b
Patch1:           python-virtualenvwrapper-4.8.4-fix-deprecated-egrep.patch

BuildArch:        noarch

BuildRequires:      python3-devel
BuildRequires:      python3-virtualenv
BuildRequires:      python3-virtualenv-clone
BuildRequires:      python3-stevedore
BuildRequires:      python3-pbr

## Just for tests
#BuildRequires:      python-tox
#BuildRequires:      ksh
#BuildRequires:      zsh

%description
%{desc}

%package -n python3-%{modname}
Summary:            %{sum}
Requires:           python3-virtualenv
Requires:           python3-virtualenv-clone
Requires:           python3-stevedore
Requires:           which

%description -n python3-%{modname}
%{desc}

%prep
%setup -q -n %{modname}-%{version}
rm -rf %{modname}.egg-info
# Fix default binaries
%patch -P0 -p1 -b .default-binaries
# Fix egrep -> grep -E
%patch -P1 -p1 -b .fix-deprecated-egrep

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

# Prepend a shebang to these so they are not stripped of executable bits
sed -i '1i #!/bin/sh' %{buildroot}/%{_bindir}/%{modname}.sh

%{__mkdir_p} %{buildroot}/%{_sysconfdir}/profile.d/
ln -s %{_bindir}/virtualenvwrapper_lazy.sh %{buildroot}/%{_sysconfdir}/profile.d/virtualenvwrapper.sh

ln -s %{_bindir}/virtualenvwrapper_lazy.sh %{buildroot}/%{_bindir}/virtualenvwrapper_lazy-3.sh
ln -s %{_bindir}/virtualenvwrapper.sh %{buildroot}/%{_bindir}/virtualenvwrapper-3.sh


#%%check
# Tests won't fly in koji since they try to install stuff from pypi
#tox -e py27

%files -n python3-%{modname} -f %{pyproject_files}
%doc PKG-INFO docs
%license LICENSE
%{_bindir}/virtualenvwrapper.sh
%{_bindir}/virtualenvwrapper_lazy.sh
%{_bindir}/virtualenvwrapper-3.sh
%{_bindir}/virtualenvwrapper_lazy-3.sh
%config(noreplace) %{_sysconfdir}/profile.d/virtualenvwrapper.sh

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.8.4-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 4.8.4-5
- Rebuilt for Python 3.12

* Fri Mar 24 2023 Nils Philippsen <nils@redhat.com> - 4.8.4-4
- Use `grep -E` instead of deprecated `egrep`

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Suvayu Ali <fatkasuvayu+linux@gmail.com> - 4.8.4-1
- Update to the latest upstream version 4.8.4
Resolves: rhbz#2100944

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 4.8.2-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.8.2-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.8.2-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8.2-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Charalampos Stratakis <cstratak@redhat.com> - 4.8.2-8
- Remove the python2 subpackage

* Fri Sep 28 2018 Nils Philippsen <nils@redhat.com> - 4.8.2-7
- fix default binary names

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.2-5
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Kevin Fenzi <kevin@scrye.com> - 4.8.2-4
- Fixed perms on wrapper scripts. Fixes bug #1554632

* Mon Mar 19 2018 Lumír Balhar <lbalhar@redhat.com> - 4.8.2-3
- Separated scripts for different Python versions

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.8.2-2
- Escape macros in %%changelog

* Mon Dec 18 2017 Kevin Fenzi <kevin@scrye.com> - 4.8.2-1
- Update to 4.8.2. Fixes bug #1488276

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.7.2-2
- Rebuild for Python 3.6

* Sat Aug 27 2016 Kevin Fenzi <kevin@scrye.com> - 4.7.2-1
- Update to 4.7.2. Fixes bug #1370847

* Mon Jul 25 2016 Lumir Balhar <lbalhar@redhat.com> - 4.7.1-5
- Python2/3 subpackages

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Ralph Bean <rbean@redhat.com> - 4.7.1-3
- Add dep on which for #1354506.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Ralph Bean <rbean@redhat.com> - 4.7.1-1
- new version

* Wed Jun 17 2015 Ralph Bean <rbean@redhat.com> - 4.6.0-1
- new version

* Wed Apr 29 2015 Ralph Bean <rbean@redhat.com> - 4.5.1-1
- new version

* Mon Apr 27 2015 Ralph Bean <rbean@redhat.com> - 4.5.0-1
- new version

* Mon Apr 27 2015 Ralph Bean <rbean@redhat.com> - 4.3.2-2
- Use virtualenvwrapper_lazy.sh by default, fixing #1213121.

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 4.3.2-1
- new version

* Thu Jul 24 2014 Ralph Bean <rbean@redhat.com> - 4.3.1-1
- Latest upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Ralph Bean <rbean@redhat.com> - 4.2-2
- Add a symlink to /etc/profile.d/ so that the package works out of the box.

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 4.2-1
- Latest upstream

* Wed Dec 04 2013 Ralph Bean <rbean@redhat.com> - 4.1.1-2
- BuildRequires on python-pbr

* Wed Dec 04 2013 Ralph Bean <rbean@redhat.com> - 4.1.1-1
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Ralph Bean <rbean@redhat.com> - 4.0-1
- Latest upstream including the following:
- The python modules for extensions are now always run with
  PWD=$WORKON_HOME (previously the value of PWD varied depending
  on the hook). The shell portion of any hook (anything sourced
  by the user’s shell when the hook is run) is still run in the
  same place as before.
- Fix the name of the script in an error message produced by
  virtualenvwrapper_lazy.sh.

* Mon Apr 08 2013 Ralph Bean <rbean@redhat.com> - 3.7.1-1
- Latest upstream including the following bugfix changes.
- Rename functions for generating help so they do not pollute the global
  namespace, and especially so they do not interfere with tab completion.
  Contributed by davidszotten.
- Fix an issue with listing project templates if none are installed.
  (issue 179)
- Fix an issue with the --python option to mkvirtualenv becoming sticky
  for future calls that do not explicitly specify the option. (issue 178)

* Wed Mar 20 2013 Ralph Bean <rbean@redhat.com> - 3.7-1
- Latest upstream.
- Improve tab-completion support for users of the lazy-loading mode.
- Add --help option to mkproject.
- Add --help option to workon.
- Turn off logging from the hook loader by default.
- Use flake8 for style checking.

* Fri Mar 08 2013 Ralph Bean <rbean@redhat.com> - 3.6.1-1
- Latest upstream

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 3.6-1
- Latest upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Ralph Bean <rbean@redhat.com> 3.5-2
- Added new dependency on python-virtualenv-clone

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> 3.5-1
- Latest upstream version.

* Fri May 25 2012 Ralph Bean <rbean@redhat.com> 3.4-1
- New upstream release with security fix and new features.
- Packaging new file virtualenvwrapper_lazy.sh
- More explicit directory ownership in python_sitelib.
- Removed old patches due to upstream bugfixes.
- Using modname macro in Source url.

* Mon May 07 2012 Ralph Bean <rbean@redhat.com> 3.2-4
- Fixed a typo in the changelog

* Mon May 07 2012 Ralph Bean <rbean@redhat.com> 3.2-3
- Applied security patch from Aron Griffis.  http://bit.ly/IHJqxs

* Tue Apr 17 2012 Ralph Bean <rbean@redhat.com> 3.2-2
- Updated the Shebangs-and-permissions patch to add a shebang to
  /usr/bin/virtualenvwrapper.sh

* Mon Apr 09 2012 Ralph Bean <rbean@redhat.com> 3.2-1
- Packaged latest version which includes disambiguated license.
- Removed %%defattr macro.
- Added patch to quiet up rpmlint.

* Wed Apr 04 2012 Ralph Bean <rbean@redhat.com> 3.1-1
- initial package for Fedora
