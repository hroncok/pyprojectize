%global pypi_name mockito

Summary:        Python spying framework inspired by Java's Mockito
Name:           python-mockito
Version:        1.5.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/kaste/%{pypi_name}-python
Source0:        %{url}/archive/%{version}/%{pypi_name}-python-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

%global _description %{expand:
This spying framework allows to easily create mocks with a very readable syntax.}

%description
%{_description}

%prep
%autosetup -n %{pypi_name}-python-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%check
%pytest

%install
%{pyproject_install}

%package -n python3-mockito
Summary: %{summary}

%description -n python3-mockito
%{_description}

%files -n python3-mockito
%doc AUTHORS
%doc CHANGES.txt
%doc README.rst
%{python3_sitelib}/mockito/
%{python3_sitelib}/mockito.dist-info
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.3.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.11

* Thu Dec 16 2021 Fabrice BAUZAC <noon@mykolab.com> 1.3.0-1
- Initial version.
