%global pypi_name itanium_demangler

Name:           python-%{pypi_name}
Version:        1.1
Release:        8%{?dist}
Summary:        Python parser for mangled itanium symbols

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/whitequark/python-itanium_demangler
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/whitequark/python-itanium_demangler/master/LICENSE-0BSD.txt
BuildArch:      noarch

%description
The Python Itanium Demangler is a pure Python parser for the Itanium C++ ABI 
symbol mangling language. This demangler generates an abstract syntax tree
from mangled symbols, which can be used for directly extracting type
information, as opposed to having to interpret the C++ source code.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
The Python Itanium Demangler is a pure Python parser for the Itanium C++ ABI 
symbol mangling language. This demangler generates an abstract syntax tree
from mangled symbols, which can be used for directly extracting type
information, as opposed to having to interpret the C++ source code.

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE-0BSD.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE-0BSD.txt

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1-2
- Rebuilt for Python 3.12

* Sat Feb 18 2023 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-1
- Update to latest upstream release 1.1 (closes rhbz#2119978)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Initial package for Fedora
