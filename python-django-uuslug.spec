%global pypi_name django-uuslug

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        10%{?dist}
Summary:        A Django slugify application that guarantees uniqueness and handles Unicode

License:        MIT
URL:            https://github.com/un33k/django-uuslug
Source0:        %{pypi_source}
BuildArch:      noarch

# Test suite is not included in sdist package of upstream release 2.0.0
Patch0:         0001-Add-upstream-test-suite.patch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(python-slugify)

%description
A Django slugify application that guarantees Uniqueness and handles Unicode


%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:       python3dist(python-slugify) >= 1.2.0
Requires:       python3dist(six)
Requires:       python3dist(django)

%description -n python3-%{pypi_name}
A Django slugify application that guarantees Uniqueness and handles Unicode


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import

%{__python3} manage.py test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l uuslug

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.12

* Sun Feb 05 2023 Chenxiong Qi <qcxhome@gmail.com> - 2.0.0-4
- Migrate to SPDX license, use MIT

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Chenxiong Qi <qcxhome@gmail.com> - 2.0.0-1
- Build 2.0.0

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Chenxiong Qi <qcxhome@gmail.com> - 1.2.0-1
- Initial package.
