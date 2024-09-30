# Enable generated Python dependencies on EL8
%{?python_enable_dependency_generator}

Name:           python-apt
Version:        2.3.0
Release:        11%{?dist}
Summary:        Python bindings for APT
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/python-apt
Source0:        https://salsa.debian.org/apt-team/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Requires Debian's apt
BuildRequires:  apt-devel >= 2.0.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(python-distutils-extra)
BuildRequires:  zlib-devel

%description
python-apt is a wrapper to use features of APT from Python.

%package -n python3-apt
Summary:        Python 3 bindings for APT
# Without dpkg installed, it crashes
Requires:       dpkg
# Needed for source format support
Recommends:     dpkg-dev

%description -n python3-apt
The apt_pkg Python 3 interface will provide full access to the internal
libapt-pkg structures allowing Python 3 programs to easily perform a
variety of functions, such as:

 - Access to the APT configuration system
 - Access to the APT package information database
 - Parsing of Debian package control files, and other files with a
   similar structure

The included 'aptsources' Python interface provides an abstraction of
the sources.list configuration on the repository and the distro level.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
# Deal with python-apt not having proper default version set by using debver hack
export DEBVER="%{version}"
%pyproject_wheel


%install
# Deal with python-apt not having proper default version set by using debver hack
export DEBVER="%{version}"
%pyproject_install
%pyproject_save_files apt 'apt_*' aptsources

# Get rid of unused garbage
rm -rf %{buildroot}%{python3_sitelib}/apt_*-stubs*


%files -n  python3-apt -f %{pyproject_files}
%license COPYING.GPL
%doc README.md
%{_datadir}/%{name}/


%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.11

* Thu Jan 27 2022 Neal Gompa <ngompa@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 (#1979091)
- Require dpkg so using it doesn't crash (#2016019)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Neal Gompa <ngompa13@gmail.com> - 2.2.0-1
- Initial package (#1974787)
