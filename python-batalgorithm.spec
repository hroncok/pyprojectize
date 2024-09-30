%global pretty_name BatAlgorithm
%global extract_name buma-BatAlgorithm-d913e9d
%global new_name batalgorithm

%global _description %{expand:
Implementation of Bat Algorithm in Python.}

Name:           python-%{new_name}
Version:        0.3.1
Release:        13%{?dist}
Summary:        Bat Algorithm for optimization

License:        MIT
URL:            https://github.com/buma/BatAlgorithm
Source0:        %{url}/tarball/master/%{extract_name}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{new_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{new_name} %_description

%prep
%autosetup -n %{extract_name}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pretty_name}

%files -n python3-%{new_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.1-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.1-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Package rename (BatAlgorithm -> batalgorithm)

* Tue Feb 9 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Initial package
