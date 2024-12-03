%global pypi_name prefixed
%global desc %{expand:
Prefixed provides an alternative implementation of the built-in float which
supports formatted output with SI (decimal) and IEC (binary) prefixes.}

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        3%{?dist}
Summary:        Prefixed alternative numeric library

License:        MPL-2.0
URL:            https://github.com/Rockhopper-Technologies/prefixed
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description %{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'prefixed*'

%check
%pyproject_check_import

%{__python3} -m unittest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.1-2
- Rebuilt for Python 3.13

* Sun Apr 21 2024 Avram Lubkin <aviso@rockhopper.net> - 0.7.1-1
- Update to 0.7.1

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0-6
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Avram Lubkin <aviso@rockhopper.net> - 0.6.0-1
- Update to 0.6.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.10

* Sun Jan 31 2021 Avram Lubkin <aviso@rockhopper.net> - 0.3.2-2
- Implement review feedback

* Mon Jan 18 2021 Avram Lubkin <aviso@rockhopper.net> - 0.3.2-1
- Initial package.
