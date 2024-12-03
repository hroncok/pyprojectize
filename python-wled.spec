%global pypi_name wled

Name:           python-%{pypi_name}
Version:        0.4.4
Release:        15%{?dist}
Summary:        Python client for WLED

License:        MIT
URL:            https://github.com/frenck/python-wled
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# Replace async_timeout with asyncio.timeout
# https://github.com/frenck/python-wled/pull/1163
# Backported to 0.4.4
Patch:          0001-Replace-async_timeout-with-asyncio.timeout-1163.patch
BuildArch:      noarch

%description
This package allows you to control and monitor an WLED device
programmatically. It is mainly created to allow third-party
programs to automate the behavior of WLED.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist aiohttp}
BuildRequires:  %{py3_dist attrs}
BuildRequires:  %{py3_dist yarl}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist backoff}
BuildRequires:  %{py3_dist aresponses}
BuildRequires:  %{py3_dist pytest-asyncio}

%description -n python3-%{pypi_name}
This package allows you to control and monitor an WLED device
programmatically. It is mainly created to allow third-party
programs to automate the behavior of WLED.

%prep
%autosetup -n python-%{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%pytest -v tests
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.4.4-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 02 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.4.4-11
- Backport “Replace async_timeout with asyncio.timeout”, PR#1163

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.4.4-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.4.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.4-3
- Rebuilt for Python 3.10

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.4-2
- Update to new macros (#1903509)

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.4-1
- Initial package
