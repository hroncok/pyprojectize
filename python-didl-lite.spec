%global pypi_name python-didl-lite
%global srcname didl-lite

Name:           python-%{srcname}
Version:        1.2.5
Release:        16%{?dist}
Summary:        DIDL-Lite (Digital Item Declaration Language) tools

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/StevenLooman/python-didl-lite
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

%description
DIDL-Lite (Digital Item Declaration Language) tools for Python DIDL-Lite tools
for Python to read and write DIDL-Lite-xml.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
# Tests are only in the GitHub source tarball present which was not released as of today
#BuildRequires:  python3dist(defusedxml)
#BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname}
DIDL-Lite (Digital Item Declaration Language) tools for Python DIDL-Lite tools
for Python to read and write DIDL-Lite-xml.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

#%%check
#%%pytest -v tests

%files -n python3-%{srcname}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/didl_lite/
%{python3_sitelib}/python_didl_lite-%{version}.dist-info/

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.5-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.5-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.5-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.5-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.5-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.5-2
- Move comment (#1882470)

* Thu Sep 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.5-1
- Initial package for Fedora
