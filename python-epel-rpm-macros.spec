Name:           python-epel-rpm-macros
Version:        3
Release:        26%{?dist}
Summary:        The EPEL Python RPM macros

License:        MIT
Source4:        macros.python3_other

BuildArch:      noarch

%description
This source package contains the EPEL Python RPM macros.

%package -n python3-other-rpm-macros
Summary:        RPM macros for building Python 3 other packages
Conflicts:      python3-rpm-macros < 3-25

%description -n python3-other-rpm-macros
RPM macros for building Python 3 packages for the secondary
Python 3 stack in EPEL.


%prep

%generate_buildrequires
%pyproject_buildrequires

%build

%install
mkdir -p %{buildroot}/%{rpmmacrodir}
install -m 644 %{SOURCE4} %{buildroot}/%{rpmmacrodir}/


%files -n python3-other-rpm-macros
%{rpmmacrodir}/macros.python3_other


%changelog
* Mon Sep 30 2019 Miro Hrončok <mhroncok@redhat.com> - 3-26
- Define %%python3_other

* Tue Apr 30 2019 Miro Hrončok <mhroncok@redhat.com> - 3-25
- Split python3-other-rpm-macros from python-rpm-macros to python-epel-rpm-macros

* Thu Apr 25 2019 Miro Hrončok <mhroncok@redhat.com> - 3-24
- %%python_provide: Obsolete and provide python36- from python3-
- %%python_provide: Provide python3- from python36-

* Thu Jan 31 2019 Miro Hrončok <mhroncok@redhat.com> - 3-23
- Make Python 3.6 the main Python 3 version
- Make Python 3.4 the other Python 3 version

* Sat Jul 14 2018 Tomas Orsava <torsava@redhat.com> - 3-22
- Move macros.pybytecompile in here from python3X-devel
- macros.pybytecompile: Detect Python version through sys.version_info instead
  of guessing from the executable name

* Mon Jul 09 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3-21
- Backport %%python3_platform and add %%python3_other_platform.

* Thu Jun 21 2018 Tadej Janež <tadej.j@nez.si> - 3-20
- Add %%python3_other_* counterparts for %%python3_* macros in EPEL 7

* Mon Jun 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3-19
- Add %%pypi_source macro.

* Wed Dec 20 2017 Charalampos Stratakis <cstratak@redhat.com> - 3-18
- Add python36 in EPEL 7.

* Mon Jan 23 2017 Michal Cyprian <mcyprian@redhat.com> - 3-17
- Add --no-deps option to py_install_wheel macros

* Tue Jan 17 2017 Tomas Orsava <torsava@redhat.com> - 3-16
- Added macros for Build/Requires tags using Python dist tags:
  https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Nov 24 2016 Orion Poplawski <orion@cora.nwra.com> 3-15
- Make expanded macros start on the same line as the macro

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> 3-14
- Fix %%py3_install_wheel (bug #1395953)

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> 3-13
- Add missing sleeps to other build macros
- Fix build_egg macros
- Add %%py_build_wheel and %%py_install_wheel macros

* Tue Nov 15 2016 Orion Poplawski <orion@cora.nwra.com> 3-12
- Add %%py_build_egg and %%py_install_egg macros
- Allow multiple args to %%py_build/install macros
- Tidy up macro formatting

* Wed Aug 24 2016 Orion Poplawski <orion@cora.nwra.com> 3-11
- Use %%rpmmacrodir

* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> 3-10
- Do not generate useless Obsoletes with %%{?_isa}

* Fri May 13 2016 Orion Poplawski <orion@cora.nwra.com> 3-9
- Make python-rpm-macros require python-srpm-macros (bug #1335860)

* Thu May 12 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 3-8
- Add single-second sleeps to work around setuptools bug.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Orion Poplawski <orion@cora.nwra.com> 3-6.1
- Set %%__python3 to /usr/bin/python3.4

* Thu Jan 14 2016 Orion Poplawski <orion@cora.nwra.com> 3-6
- Fix typo in %%python_provide

* Thu Jan 14 2016 Orion Poplawski <orion@cora.nwra.com> 3-5
- Handle noarch python sub-packages (bug #1290900)

* Thu Jan 14 2016 Orion Poplawski <orion@cora.nwra.com> 3-4.1
- EPEL version

* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> 3-4
- Fix python2/3-rpm-macros package names

* Thu Jan 7 2016 Orion Poplawski <orion@cora.nwra.com> 3-3
- Add empty %%prep and %%build

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> 3-2
- Combined package

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> 3-1
- Initial package
