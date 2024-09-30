%global srcname %(echo %{name} | sed 's/^python-//')
Name:           python-fqdn
Version:        1.5.1
Release:        14%{?dist}
Summary:        Validates fully-qualified domain names against RFC 1123
BuildArch:      noarch
License:        MPL-2.0
URL:            https://github.com/ypcrts/fqdn
Source0:        %pypi_source
# Missing in pypi tar ball release, present at github :(
Source1:        test_fqdn.py

%global _description %{expand:
Validates fully-qualified domain names against RFC 1123, so that they
are acceptable to modern browsers.}
%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
mkdir tests/
touch tests/__init__.py
cp %{SOURCE1} tests/
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.1-13
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.1-12
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Paul Wouters <paul.wouters@aiven.io> - 1.5.1-2
- Initial package
