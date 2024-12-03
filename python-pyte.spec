Summary:        In memory VT-compatible terminal emulator
Name:           python-pyte
Version:        0.8.2
Release:        6%{?dist}
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/selectel/pyte
Source0:        https://github.com/selectel/pyte/archive/%{version}/pyte-%{version}.tar.gz
Patch0:         python-pyte-0.8.0-docs.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-sphinx
BuildRequires:  python3-wcwidth
%description
In memory VTXXX-compatible terminal emulator.  XXX stands for a series
of video terminals, developed by DEC between 1970 and 1995.

%package     -n python3-pyte
Summary:        %{summary}
%description -n python3-pyte
In memory VTXXX-compatible terminal emulator.  XXX stands for a series
of video terminals, developed by DEC between 1970 and 1995.


%package     -n python3-pyte-docs
Summary:        Documentation of API in Python module pyte
%description -n python3-pyte-docs
This contains documentation of the API in Python module pyte.

%prep
%autosetup -p1 -n pyte-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs && make all

%install
%pyproject_install
%pyproject_save_files -l pyte

%check
%pyproject_check_import

%{__python3} setup.py test

%files -n python3-pyte -f %{pyproject_files}
%doc AUTHORS CHANGES README 

%files -n python3-pyte-docs
%license LICENSE
%doc examples/
%doc docs/_build/html

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.2-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 14 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.8.2-1
- 0.8.2

* Sun Sep 24 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-1
- 0.8.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.8.0-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.10

* Mon Mar 08 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-4
- Fix changelog

* Sun Feb 21 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-3
- Fix source and url
- Drop explicit requires, autodetected these days
- Add AUTHORS and CHANGES to doc
- Use py_provides macro for Fedora 32, automatically elsewhere
- Add patch from Robert-Andre Mauchin to avoid network access during buil
- Build and ship API docs in docs subpackage, include examples too

* Sun Feb 07 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-2
- Remove Python 2 support
- Minor clean up

* Tue May 8 2018 Mateusz Mikuła <mati865 at gmail.com> - 0.8.0-1
- Initial packaging
