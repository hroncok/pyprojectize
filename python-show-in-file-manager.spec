%global srcname show-in-file-manager
%{?python_enable_dependency_generator}

Name:          python-%{srcname}
Version:       1.1.4
Release:       11%{?dist}
Summary:       Show in File Manager is a Python package to open the system file manager and optionally select files in it.

License:       MIT
URL:           https://github.com/damonlynch/showinfilemanager
Source0:       %{pypi_source}
BuildArch:     noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Provides:      %{srcname} = %{version}-%{release}
BuildRequires: python3-devel

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}


%install
%{pyproject_install}

%files -n python3-%{srcname}
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/showinfilemanager
%{python3_sitelib}/showinfm/
%{python3_sitelib}/show_in_file_manager.dist-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.4-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.4-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.4-3
- Rebuilt for Python 3.11

* Sat Apr 02 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.1.4-1
- Initial Package
