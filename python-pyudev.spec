%global srcname pyudev
Name:             python-%{srcname}
Version:          0.24.3
Release:          3%{?dist}
Summary:          A libudev binding

License:          LGPL-2.1-or-later
URL:              http://pypi.python.org/pypi/pyudev
Source0:          https://pypi.io/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:        noarch

%description
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.
The binding supports CPython 3 and PyPy.

%package -n python3-%{srcname}
Summary:          A libudev binding
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools

# Needed for libudev, loaded through ctypes
Requires:         systemd-libs

%description -n python3-%{srcname}
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.
The binding supports CPython 3 and PyPy.

%package -n python3-%{srcname}-qt4
Summary:          Qt4 integration for pyudev

Requires:         python3-PyQt4
Requires:         python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-qt4
Qt4 integration for pyudev.

This package provides a module pyudev.pyqt4 that contains classes for
integrating a pyudev monitor with the Qt4 main loop.

%package -n python3-%{srcname}-qt5
Summary:          Qt5 integration for pyudev

Requires:         python3-qt5
Requires:         python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-qt5
Qt5 integration for pyudev.

This package provides a module pyudev.pyqt5 that contains classes for
integrating a pyudev monitor with the Qt5 main loop.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf pyudev.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/pyudev
%{python3_sitelib}/pyudev-%{version}-*.egg-info
%exclude %{python3_sitelib}/pyudev/glib.py
%exclude %{python3_sitelib}/pyudev/__pycache__/glib.*
%exclude %{python3_sitelib}/pyudev/pyqt4.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt4.*
%exclude %{python3_sitelib}/pyudev/pyqt5.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt5.*
%exclude %{python3_sitelib}/pyudev/pyside.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyside.*
%exclude %{python3_sitelib}/pyudev/wx.py
%exclude %{python3_sitelib}/pyudev/__pycache__/wx.*

%files -n python3-%{srcname}-qt4
%license COPYING
%{python3_sitelib}/pyudev/pyqt4.py
%{python3_sitelib}/pyudev/__pycache__/pyqt4.*

%files -n python3-%{srcname}-qt5
%license COPYING
%{python3_sitelib}/pyudev/pyqt5.py
%{python3_sitelib}/pyudev/__pycache__/pyqt5.*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.24.3-2
- Rebuilt for Python 3.13

* Fri May 10 2024 mulhern <mulhern@redhat.com> - 0.24.1
- Update to 0.24.3

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.24.1-4
- Rebuilt for Python 3.12

* Tue Jun 13 2023 mulhern <amulhern@redhat.com> - 0.24.1-3
- Use SPDX-format license; also make it match upstream

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.24.1-2
- Rebuilt for Python 3.12

* Fri Apr 21 2023 mulhern <amulhern@redhat.com> - 0.24.1-1
- Update to 0.24.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 mulhern <amulhern@redhat.com> - 0.24.0-1
- Update to 0.24.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.23.2-2
- Rebuilt for Python 3.11

* Tue Feb 15 2022 mulhern <amulhern@redhat.com> - 0.23.2-1
- Update to 0.23.2

* Tue Feb 15 2022 mulhern <amulhern@redhat.com> - 0.22.0-8
- Drop redundant Requires

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 0.22.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.22.0-2
- Rebuilt for Python 3.9

* Wed Feb  5 2020 David Shea <dshea@fedoraproject.org> - 0.22.0-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.21.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.21.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.21.0-9
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.21.0-7
- Rebuilt for Python 3.7

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.21.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Kevin Fenzi <kevin@scrye.com> - 0.21.0-2
- Rebuild for Python 3.6

* Fri Jul 29 2016 mulhern <amulhern@redhat.com> - 0.21.1
- Deprecate use of Device object as mapping from udev property names to values
- Add a Properties class and a Device.properties() method for udev properties
- Fix places where Device object was incorrectly used in a boolean context
- Return an empty string, not None, if the property value is an empty string
- Exceptions re-raised from libudev calls now have a message string
- Insert a warning about using a Device in a boolean context in docs
- Infrastructure for vagrant tests is removed
- Various internal refactorings
- Extensive test improvements
- Numerous documentation fixes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 2 2016 mulhern <amulhern@redhat.com> - 0.20.0
- Remove parsing code added in previous release
- No longer do CI for Python 2.6
- Eliminate all wildcard imports and __all__ statements
- No longer use deprecated Device.from_sys_path() method
- Minor pylint induced changes
- Documentation fixes

* Mon Feb 08 2016 mulhern <amulhern@redhat.com> - 0.19.0
- Never raise a DeviceNotFoundError when iterating over a device enumeration
- Device.subsystem() now returns None if device has no subsystem
- Add DeprecationWarnings to deprecated Device methods
- Replace "/" with "!" in Device.from_name() sys_name parameter
- Add some unstable classes for parsing some kinds of values
- Make version info more like Python's including micro numbers and levels
- Refactor some internal modules into subdirectories
- Work on tests and reproducers

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 mulhern <amulhern@redhat.com> - 0.18.1
- Restore raising KeyError in astring, asint, asbool methods in Attributes
- Add dependency on six package
- pyudev sources now in src directory
- Added support for pyqt5 monitor observer
- Added discover module, which looks up a device on limited information
- DeviceNotFoundError is no longer a subtype of LookupError
- Attributes class no longer extends Mapping class
- Attributes class no longer inherits [] operator and other Mapping methods
- Attributes class object are no longer iterable or indexable and have no length
- Attributes.available_attributes property added
- Attributes.get() method, with usual semantics explicitly defined
- Device.from_* methods are deprecated, use Devices.from_* methods instead
- Device.from_device_number() now raises DeviceNotFoundByNumberError
- Devices.from_interface_index() method added
- Devices.from_kernel_device() method added

* Thu Dec  3 2015 David Shea <dshea@redhat.com> - 0.17-4
- Add requires for things that are required
- Split the main-loop integration modules into separate packages

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 0.17-3
- Rebuilt for Python3.5 rebuild

* Wed Sep 15 2015 David Shea <dshea@redhat.com> - 0.17.1-2
- Fix a typo in the python3-pyudev Provides

* Mon Sep 14 2015 David Shea <dshea@redhat.com> - 0.17.1-1
- Really start the monitor on pyudev.Monitor.poll()
- Force non-blocking IO in pyudev.Monitor to avoid blocking on receiving the device
- Set proper flags on pipe fs
- Handle irregular polling events properly
- Rename MonitorObserver GUI classes and deprecate the old ones
- Remove patches for #1170337 and #1230773 that are now part of upstream
- Switch to new packaging guidelines which renames python-pyudev to python2-pyudev

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 David Shea <dshea@redhat.com> - 0.16.1-3
- Retry interrupted system calls (#1230773)
- Rearrange the build process to match current packaging recommendations

* Wed Jan 28 2015 David Shea <dshea@redhat.com> - 0.16.1-2
- Use %%license for the license file

* Wed Dec 10 2014 David Shea <dshea@redhat.com> - 0.16.1-1
- Update to pyudev-0.16.1 (#880644)
- Apply a patch from upstream to remove a global reference to libudev (#1170337)

* Wed Dec 10 2014 David Shea <dshea@redhat.com> - 0.15-7
- Fix license tag (LGPL -> LGPLv2+) (#990579)
- Remove rst tags from description
- Remove unnecessary requires and buildrequires (#1095459)
- Avoid packaging upstream egg-info files
- Add a python3 package
- Drop the Group tag which wasn't even the right group

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Chris Lockfort <clockfort@redhat.com> 0.15-3
- Reflect rawhide merging udev into systemd
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Mon Jun 18 2012 Chris Lockfort <clockfort@redhat.com> 0.15-1
- initial package
