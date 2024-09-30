%global pypi_name pysodium

Name:           python-%{pypi_name}
Version:        0.7.12
Release:        12%{?dist}
Summary:        A Python libsodium wrapper

License:        BSD-2-Clause
URL:            https://github.com/stef/pysodium
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  pkgconfig(libsodium)
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This is a very simple wrapper around libsodium masquerading as nacl.}

%description
%{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       libsodium

%description -n python3-%{pypi_name}
%{_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS README.md
%license LICENSE.txt

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.12-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 0.7.12-8
- rebuild for new libsodium

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.12-6
- Rebuilt for Python 3.12

* Sun Mar 05 2023 Andreas Schneider <asn@redhat.com> - 0.7.12-5
- Update License to SPDX expression

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.12-2
- Rebuilt for Python 3.11

* Tue Jun 07 2022 Andreas Schneider <asn@redhat.com> - 0.7.12-1
- rhbz#2086472 - Initial package
