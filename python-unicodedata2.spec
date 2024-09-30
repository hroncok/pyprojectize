# Created by pyp2rpm-3.3.7
%global pypi_name unicodedata2
%global pypi_version 15.1.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        5%{?dist}
Summary:        Unicodedata backport updated to the latest Unicode version

License:        Apache-2.0
URL:            http://github.com/fonttools/unicodedata2
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)
BuildRequires:  python3dist(pytest-xdist)

%description
This module provides access to the Unicode Character Database (UCD)
which defines character properties for all Unicode characters. The
data contained in this database is compiled from the UCD version 13.0.0.

The versions of this package match Unicode versions, so unicodedata2==13.0.0
is data from Unicode 13.0.0.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module provides access to the Unicode Character Database (UCD) 
which defines character properties for all Unicode characters. The 
data contained in this database is compiled from the UCD version 13.0.0.

The versions of this package match Unicode versions, so unicodedata2==13.0.0 
is data from Unicode 13.0.0.


%prep
%autosetup -n %{pypi_name}-%{pypi_version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}%{python3_ext_suffix}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 15.1.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 08 2023 Parag Nemade <pnemade AT redhat DOT com> - 15.1.0-1
- Update to 15.1.0 version (#2241026)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 15.0.0-2
- Rebuilt for Python 3.12

* Tue Mar 21 2023 Parag Nemade <pnemade AT redhat DOT com> - 15.0.0-1
- Update to 15.0.0 release

* Mon Dec 05 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-6
- Update license tag to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 14.0.0-4
- Rebuilt for Python 3.11

* Mon May 16 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-3
- Update as suggested in this package review

* Mon May 16 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-2
- Drop un-necessary packaging lines from SPEC file

* Sun Feb 27 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-1
- Initial package.
