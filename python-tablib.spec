%global srcname tablib

Name:             python-tablib
Version:          3.0.0
Release:          11%{?dist}
Summary:          Format agnostic tabular data library (XLS, JSON, YAML, CSV)

License:          MIT
URL:              http://github.com/kennethreitz/tablib
Source0:          %{pypi_source}
BuildArch:        noarch

%global _description\
Tablib is a format-agnostic tabular dataset library, written in Python.\
\
Output formats supported:\
\
 - Excel (Sets + Books)\
 - JSON (Sets + Books)\
 - YAML (Sets + Books)\
 - HTML (Sets)\
 - TSV (Sets)\
 - CSV (Sets)

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm)
# ods
Requires:       python3dist(odfpy)
# xls
Requires:       python3dist(xlrd)
Requires:       python3dist(xlwt)
# xlsx
Requires:       python3dist(openpyxl) >= 2.6.0
# yaml
Requires:       python3dist(pyyaml)

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tablib
 
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.0-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

%autochangelog
