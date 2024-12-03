%global pypi_name ana

Name:           python-%{pypi_name}
Version:        0.06
Release:        18%{?dist}
Summary:        Python module to provide easy distributed data storage

License:        MIT
URL:            https://pypi.org/project/ana/
Source0:        %{pypi_source}
Patch:          https://github.com/zardus/ana/pull/17.patch
BuildArch:      noarch

%description
ANA is a project to provide easy distributed data storage. It provides every
object with a UUID and, when pickled, will first serialize the object's state
to a central location and then "pickle" the object into just its UUID.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
ANA is a project to provide easy distributed data storage. It provides every
object with a UUID and, when pickled, will first serialize the object's state
to a central location and then "pickle" the object into just its UUID.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.06-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Lumír Balhar <lbalhar@redhat.com> - 0.06-14
- Drop dependency on python3-future

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.06-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.06-9
- Rebuilt for Python 3.11

* Mon Mar 07 2022 Karolina Surma <ksurma@redhat.com> - 0.06-8
- Fix package build with setuptools >= 60.x

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.06-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.06-2
- Rebuilt for Python 3.9

* Tue Feb 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.06-1
- Initial package for Fedora
