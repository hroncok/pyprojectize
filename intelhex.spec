Name:          intelhex
Version:       2.3.0
Release:       15%{?dist}
Summary:       Utilities for manipulating Intel HEX file format
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/python-intelhex/intelhex
Source0:       https://github.com/python-intelhex/intelhex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: dos2unix
BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: make

%description
The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard for representation of code
to be programmed into microelectronic devices.

This work implements an intelhex Python library and a number of utilities to 
read, write, create from scratch and manipulate data from Intel HEX file format.

The distribution package also includes several convenience Python scripts,
including "classic" hex2bin and bin2hex converters and more, those based on the
library itself. Check the docs to know more.

%package -n python3-intelhex
Summary:  A python3 library for manipulating Intel HEX file format

%description -n python3-intelhex
The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard for representation of code
to be programmed into microelectronic devices.

This work implements an intelhex Python library and a number of utilities to 
read, write, create from scratch and manipulate data from Intel HEX file format.

The distribution package also includes several convenience Python scripts,
including "classic" hex2bin and bin2hex converters and more, those based on the
library itself. Check the docs to know more.

%package docs
Summary:  Manuak for the IntelHex python library

%description docs
User manual for IntelHex

%prep
%autosetup -p1
dos2unix README.rst
dos2unix NEWS.rst
sed -i '1d' intelhex/bench.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs/manual/
make html
popd 

%install
%pyproject_install
%pyproject_save_files 'intelhex*'

%files
%doc NEWS.rst README.rst
%{_bindir}/*.py

%files -n python3-intelhex -f %{pyproject_files}
%license LICENSE.txt

%files docs
%doc docs/intelhex.pdf docs/manual.txt
%doc docs/manual/.build/html/*.html
%doc docs/manual/.build/html/searchindex.js

%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0-13
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.3.0-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Mon Sep 28 2020 Than Ngo <than@redhat.com> - 2.2.1-7
- fixed FTBFS, python 3.2: tostring() is renamed to tobytes()

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.2.1-4
- Review updates, URL update

* Sat Jul 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.1-3
- Split python bindings and utilities

* Thu Nov  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.1-2
- Minor package updates

* Sun Oct 28 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.1-1
- Initial package
