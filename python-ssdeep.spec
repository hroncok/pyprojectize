%global pypi_name ssdeep

%global pypi_description A straightforward Python module for ssdeep by Jesse Kornblum, \
which is a library for computing context triggered piecewise hashes (CTPH). \
Also called fuzzy hashes, CTPH can match inputs that have homologies. \
Such inputs have sequences of identical bytes in the same order, although \
bytes in between these sequences may be different in both content and length.


Name: python-%{pypi_name}
Summary: Python wrapper for the ssdeep library
License: LGPL-3.0-or-later

Version: 3.4
Release: 20%{?dist}

URL: https://github.com/DinoTools/python-ssdeep/
Source0: %pypi_source

BuildRequires: make
BuildRequires: gcc
BuildRequires: ssdeep-devel

BuildRequires: python3-cffi >= 0.8.6
BuildRequires: python3-devel
BuildRequires: python3-pytest-runner
BuildRequires: python3-six >= 1.4.1
BuildRequires: python3-sphinx


%description
%{pypi_description}


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{pypi_description}


%package -n python3-%{pypi_name}-doc
Summary: Documentation for python3-%{pypi_name}
BuildArch: noarch

%description -n python3-%{pypi_name}-doc
This package contains documentation (in HTML and man page format)
for the ssdeep Python3 module.


%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

pushd docs/
make man
make html


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

install -d -m 755 %{buildroot}%{_mandir}/man5/
install -m 644 docs/build/man/pythonssdeep.1 %{buildroot}%{_mandir}/man5/python3-%{pypi_name}.5


%check
%pyproject_check_import

%{__python3} setup.py test


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst CONTRIBUTING.rst

%files -n python3-%{pypi_name}-doc
%doc docs/build/html/*
%{_mandir}/man5/python3-%{pypi_name}.5*


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4-19
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.4-18
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.4-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.4-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.4-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Artur Iwicki <fedora@svgames.pl> - 3.4-4
- Add an explicit BuildRequires on python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4-3
- Rebuilt for Python 3.9

* Thu Mar 05 2020 Artur Iwicki <fedora@svgames.pl> - 3.4-2
- Fix package description and BuildRequires
- Add documentation in a -doc package

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 3.4-1
- Initial packaging
