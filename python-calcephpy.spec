%global srcname calcephpy

Name:           python-%{srcname}
Version:        4.0.0
Release:        3%{?dist}
Summary:        Astronomical library to access planetary ephemeris files

License:        CECILL-2.0 OR CECILL-B OR CECILL-C
URL:            https://pypi.python.org/pypi/calcephpy
Source0:        %{pypi_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Documentation build doesn't work anymore because it relies on several
# sphinx extensions not packaged / not packageable in Fedora
Obsoletes:      python3-calcephpy-docs < 4.0.0


%global _description %{expand:
This is the Python module of calceph.
Calceph is a library designed to access the binary planetary ephemeris files,
such INPOPxx, JPL DExxx and SPICE ephemeris files.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  python3-devel
%if 0%{?rhel} == 7
BuildRequires:  python36-Cython
%else
BuildRequires:  python3-Cython
%endif

# Needed by EPEL7
%py_provides python3-%{srcname}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove egg files from source


%generate_buildrequires
%pyproject_buildrequires


%build
export CPPFLAGS="$CXXFLAGS"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '*'


%check
%pyproject_check_import


%files -n       python3-%{srcname} -f %{pyproject_files}


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0.0-2
- Rebuilt for Python 3.13

* Thu Apr 25 2024 Mattia Verga <mattia.verga@proton.me> - 4.0.0-1
- Update to 4.0.0 (fedora#2276851)
- Removed documentation subpackage due to missing required build tools
- Drop i686 build

* Wed Feb 07 2024 Mattia Verga <mattia.verga@protonm.me> - 3.5.5-1
- Update to 3.5.5 (fedora#2262749)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 03 2023 Mattia Verga <mattia.verga@protonm.me> - 3.5.4-1
- Update to 3.5.4 (fedora#2252667)

* Sat Sep 09 2023 Mattia Verga <mattia.verga@protonm.me> - 3.5.3-2
- Fix build flags

* Wed Sep 06 2023 Mattia Verga <mattia.verga@protonm.me> - 3.5.3-1
- Update to 3.5.3 (fedora#2237640)
- Fix compatibility with Cython 3.x (fedora#2226167)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.5.2-2
- Rebuilt for Python 3.12

* Sat Apr 15 2023 Mattia Verga <mattia.verga@protonm.me> - 3.5.2-1
- Update to 3.5.2 (fedora#2186143)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.5.1-2
- Rebuilt for Python 3.11

* Wed Mar 02 2022 Mattia Verga <mattia.verga@protonmail.com> - 3.5.1-1
- Update to 3.5.1 (fedora#2059290)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 28 2021 Mattia Verga <mattia.verga@protonmail.com> - 3.5.0-1
- Update to 3.5.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4.7-5
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-4
- Patch sources to fix build with Python 3.10a
- Fix rhbz#1948439

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-2
- Create a doc subpackage
- Remove executable bit set on license files
- Add py_provides macro for EPEL7

* Sat Nov 07 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-1
- Update to 3.4.7

* Tue Nov 3 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.6-1
- Initial packaging
