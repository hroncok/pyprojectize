%global pypi_name serpent

Name:           python-%{pypi_name}
Version:        1.40
Release:        9%{?dist}
Summary:        Serialization based on ast.literal_eval

License:        MIT
URL:            https://github.com/irmen/Serpent
Source0:        %{pypi_source}
# Python 3.11 compat
# https://github.com/irmen/Serpent/commit/dd77c8c06e387d3f981b094de2669cb7a030551f
Patch0:         dd77c8c06e387d3f981b094de2669cb7a030551f.patch
BuildArch:      noarch

%description
Serpent is a simple serialization library based on ast.literal_eval. Because
it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-attrs
BuildRequires:  python3-pytz
BuildRequires:  pytest

%description -n python3-%{pypi_name}
Serpent is a simple serialization library based on ast.literal_eval. Because
it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.
%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.40-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.40-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.40-1
- serpent 1.40
- Python 3.11 support (fixes rhbz#2084447)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.30.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.30.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.30.2-1
- Initial package for Fedora
