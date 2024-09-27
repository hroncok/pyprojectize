%global pypi_name aiounittest

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        19%{?dist}
Summary:        Test asyncio code more easily

License:        MIT
URL:            https://github.com/kwarunek/aiounittest
Source0:        https://github.com/kwarunek/aiounittest/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Don't run @asyncio.coroutine tests with Python 3.11
Patch:          https://github.com/kwarunek/aiounittest/pull/21.patch

# test_sync_async_add: After closing the default event loop, set a new one
Patch:          https://github.com/kwarunek/aiounittest/pull/22.patch

BuildArch:      noarch

%description
The aiounittest is a helper library to ease your pain (and boilerplate),
when writing tests of asynchronous code (:code:asyncio). You can test:

- synchronous code (same as the :code:unittest.TestCase)
- asynchronous code, it supports syntax with async/await (Python 3.5+) and
  asyncio.coroutine/yield from (Python 3.4)

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The aiounittest is a helper library to ease your pain (and boilerplate),
when writing tests of asynchronous code (:code:asyncio). You can test:

- synchronous code (same as the :code:unittest.TestCase)
- asynchronous code, it supports syntax with async/await (Python 3.5+) and
  asyncio.coroutine/yield from Python 3.4

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# %%check
# No support for pytest 8, https://github.com/kwarunek/aiounittest/issues/25
# %%pytest -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-19
- Disable checks (rhbz#2277972)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.1-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.1-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.1-10
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-9
- Use pytest instead of nose to test the package
- Drop an unused dependency on coverage

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.9

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-2
- Fix description (rhbz#1786953)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Initial package for Fedora
