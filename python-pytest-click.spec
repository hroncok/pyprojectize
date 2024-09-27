Name:           python-pytest-click
Version:        1.1.0
Release:        8%{?dist}
Summary:        Pytest plugin for Click

License:        MIT
URL:            https://github.com/Stranger6667/pytest-click
Source:         %{pypi_source pytest_click}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click) >= 6
BuildRequires:  python3dist(pytest) >= 5

%description
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%package -n     python3-pytest-click
Summary:        %{summary}

%description -n python3-pytest-click
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%prep
%autosetup -n pytest_click-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-pytest-click
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_click/
%{python3_sitelib}/pytest_click-%{version}.dist-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.1.0-1
- Initial package.
