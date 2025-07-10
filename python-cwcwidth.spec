Summary:        Python bindings for wc(s)width
Name:           python-cwcwidth
Version:        0.1.9
Release:        5%{?dist}
License:        MIT
URL:            https://github.com/sebastinas/cwcwidth
Source0:        %{pypi_source cwcwidth}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.28
%global _description \
Python bindings for wc(s)widthcwcwidth provides Python bindings for \
wcwidth and wcswidth functions defined in POSIX.1-2001 and \
POSIX.1-2008 based on Cython . These functions compute the printable \
length of a unicode character/string on a terminal.
%description %_description

%package     -n python3-cwcwidth
Summary:        %{summary}
%{?fc32:%py_provides python3-cwcwidth}
%description -n python3-cwcwidth %_description

%prep
%autosetup -n cwcwidth-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cwcwidth

%check
%pyproject_check_import

%{__python3} setup.py test

%files -n python3-cwcwidth -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.9-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 08 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.1.9-1
- 0.1.9

* Sun Sep 10 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.1.8-1
- 0.1.8

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.4-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.4-3
- Rebuilt for Python 3.10

* Thu Mar 11 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1.4-2
- Fix license and source tags

* Mon Mar 08 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1.4-1
- 0.1.4
- Fix python provide for Fedora 32

* Sun Feb 07 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1.2-1
- 0.1.2

* Tue Jan 26 2021 Terje Rosten <terje.rosten@ntnu.no> - 0.1-1
- initial package
