%global pypi_name op1svg

%global forgeurl https://github.com/op1hacks/op1svg
%global commit 50a3b01ebb74fd07b33d91c08b1e59e11494801d
%forgemeta

%global common_description %{expand:
op1svg normalizes SVG files so that the OP-1 understands them:
- Remove unsupported tags and attributes
- Remove comments
- Convert styles to attributes, and drop unsupported styles
- Fix decimals; a maximum of 4 decimals is supported by the OP-1
- Reformat the path data in paths}

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        14%{?dist}
Summary:        Normalize SVG files so that the OP-1 understands them

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        op1svg.1
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel

%description
%{common_description}

%package -n     %{pypi_name}
Summary:        %{summary}

%description -n %{pypi_name}
%{common_description}

%prep
%forgesetup
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python3|d" -i %{pypi_name}/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
mkdir -p %{buildroot}%{_mandir}/man1
cp -P %{SOURCE1} %{buildroot}%{_mandir}/man1

%check
%pyproject_check_import

%files -n %{pypi_name} -f %{pyproject_files}
%doc README.md template
%{_bindir}/op1svg
%{_mandir}/man1/op1svg.1*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.10

* Fri Apr 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1.0-2.20210419git50a3b01
- Add man page contributed by Ben Beasley

* Sat Apr 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1.0-1.20210419git50a3b01
- Initial package.
