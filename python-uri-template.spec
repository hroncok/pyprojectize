%global pypi_name uri-template
%global pypi_version 1.2.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        10%{?dist}
Summary:        RFC 6570 URI Template Processor

License:        MIT
URL:            https://github.com/plinss/uri_template/
Source0:        %{url}/archive/refs/tags/v%{pypi_version}.tar.gz#/%{name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
An implementation of RFC 6570 URI Templates.This packages implements
URI Template expansion in strict adherence to RFC 6570, but adds a
few extensions.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
An implementation of RFC 6570 URI Templates.This packages implements
URI Template expansion in strict adherence to RFC 6570, but adds a
few extensions.

%prep
%autosetup -n uri_template-%{pypi_version}

# Upstream released tarball contains version 0.0.0 in setup.py
sed -i 's/0.0.0/%{pypi_version}/g' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l uri_template

%check
%pyproject_check_import
%{python3} test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Parag Nemade <pnemade AT redhat DOT com> - 1.2.0-6
- Mark this as SPDX license expression converted

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Parag Nemade <pnemade AT redhat DOT com> - 1.2.0-2
- Fix as per suggested in package review (#2102060)

* Wed Jun 29 2022 Parag Nemade <pnemade AT redhat DOT com> - 1.2.0-1
- Initial package.
