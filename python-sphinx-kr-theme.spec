%bcond_without tests

%global pypi_name sphinx-kr-theme

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        17%{?dist}
Summary:        Kenneth Reitz's krTheme for Sphinx

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/tonyseek/sphinx-kr-theme
Source0:        %{pypi_source}
%if %{with tests}
# Tests are not included in the PyPI tarball
Source1:        https://raw.githubusercontent.com/tonyseek/sphinx-kr-theme/57834e237e35b59b5957aacb7ac072e434dd5e93/tests.py
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description
This is a repackaging of Kenneth Reitz's krTheme, a theme for use in 
Sphinx documentation, originally derived from Mitsuhiko's Flask theme.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(setuptools)
%if 0%{?fedora} < 33 || 0%{?rhel} < 9
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
This is a repackaging of Kenneth Reitz's krTheme, a theme for use in 
Sphinx documentation, originally derived from Mitsuhiko's Flask theme.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if %{with tests}
%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%pytest %{SOURCE1}
%endif

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinx_kr_theme
%{python3_sitelib}/sphinx_kr_theme-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.1-17
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.1-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.1-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.1-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.1-3
- Add py_provides for F32
- Run tests

* Wed Oct 28 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.1-2
- Use pypi_source
- Fix license

* Wed Oct 28 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.1-1
- Initial package.
