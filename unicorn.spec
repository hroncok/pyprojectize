Name:           unicorn
Version:        2.0.1.post1
Release:        %autorelease
Summary:        Lightweight multi-platform, multi-architecture CPU emulator framework

# GPLv2:        Most of unicorn is licensed under the GPLv2, with exception
#               being the code which followed the project's fork of QEMU.
# LGPLv2:       Portions of code from QEMU
# MIT:          Portions of code from QEMU
# BSD:          Portions of code from QEMU
# Automatically converted from old format: GPLv2 and LGPLv2+ and MIT and BSD - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://www.unicorn-engine.org/
Source0:        https://github.com/unicorn-engine/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Much of Unicorn follows from QEMU, which the Unicorn project forked in
# 2015. Since then, the Unicorn team has applied a number of bugfixes to
# the forked QEMU code along with the modifications necessary for Unicorn.
# QEMU 2.2.1 formed the basis of this work. The Unicorn project documents
# the relationship between Unicorn and QEMU at
# http://www.unicorn-engine.org/docs/beyond_qemu.html.
Provides: bundled(qemu) = 2.2.1

# https://bugzilla.redhat.com/show_bug.cgi?id=2223039
# https://github.com/unicorn-engine/unicorn/issues/1840
ExcludeArch:    s390x

%description
Unicorn is a lightweight multi-platform, multi-architecture CPU emulator
framework.

%package devel
Summary:        Files needed to develop applications using unicorn
Requires:       %{name} = %{version}-%{release}

%description devel
This package provides the libraries, include files, and other resources
needed for developing applications using unicorn.

%package -n python3-unicorn
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-unicorn
The unicorn-python3 package contains python3 bindings for unicorn.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake
%cmake_build

pushd bindings/python
%py3_build
popd

%install
%cmake_install

pushd bindings/python
%py3_install
popd

rm $RPM_BUILD_ROOT%{_libdir}/libunicorn.a

%check
%ctest

%files
%doc AUTHORS.TXT ChangeLog CREDITS.TXT README.md
%license COPYING
%{_libdir}/libunicorn.so.2

%files devel
%{_libdir}/libunicorn.so
%{_libdir}/pkgconfig/unicorn.pc
%{_includedir}/unicorn/

%files -n python3-unicorn
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{name}/

%changelog
%autochangelog
