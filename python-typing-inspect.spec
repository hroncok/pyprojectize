%global pypi_name typing-inspect
%global pypi_srcname typing_inspect

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        6%{?dist}
Summary:        Runtime inspection utilities for typing module

License:        MIT
URL:            https://github.com/ilevkivskyi/%{pypi_srcname}
Source0:        %{pypi_source %pypi_srcname}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(mypy-extensions) >= 0.3.0
BuildRequires:  python3dist(typing-extensions) >= 3.7.4
BuildRequires:  python3dist(pytest)

%description
Typing Inspect The "%{pypi_srcname}" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(mypy-extensions) >= 0.3.0
Requires:       python3dist(typing-extensions) >= 3.7.4
%description -n python3-%{pypi_name}
The "%{pypi_srcname}" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.


%prep
%autosetup -n %{pypi_srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_srcname}

%check
%pyproject_check_import
%{__python3} setup.py test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.9.0-2
- Affirm SPDX license tag

* Mon Nov 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.9.0-1
- 0.9.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Anna Khaitovich <akhaitov@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Anna Khaitovich <akhaitov@redhat.com> - 0.5.0-1
- Initial package.
