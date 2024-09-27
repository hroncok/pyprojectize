%global pypi_name pytest-trio

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        11%{?dist}
Summary:        Pytest plugin for trio

# Automatically converted from old format: MIT or ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT OR Apache-2.0
URL:            https://github.com/python-trio/pytest-trio
Source0:        https://github.com/python-trio/pytest-trio/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# Remove trio.tests import causing warnings
# https://github.com/python-trio/pytest-trio/pull/135
# We only backport the fix, not the additional formatting changes.
Patch:          https://github.com/python-trio/pytest-trio/pull/135/commits/9cda20bbb966fe1e4ae51921d566c668654ee5e1.patch

BuildArch:      noarch

%description
This is a pytest plugin to help you test projects that use Trio, a friendly
library for concurrency and async I/O in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-setuptools
BuildRequires:  python3-trio
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a pytest plugin to help you test projects that use Trio, a friendly
library for concurrency and async I/O in Python.

%package -n python-%{pypi_name}-doc
Summary:        pytest-trio documentation

#BuildRequires:  python3-sphinx
#BuildRequires:  python3-sphinxcontrib-trio
#BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info
sed -i /RemovedInPytest4Warning/d pytest_trio/_tests/conftest.py
sed -i s/--cov// pytest.ini

%build
%py3_build
#   An error happened in rendering the page history.
#   Reason: UndefinedError("'logo' is undefined")
# PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# https://github.com/python-trio/pytest-trio/issues/84
%check
%pytest -v -W "ignore::trio.TrioDeprecationWarning"

%files -n python3-%{pypi_name}
%license LICENSE.MIT LICENSE LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/pytest_trio/
%{python3_sitelib}/pytest_trio-%{version}-py%{python3_version}.egg-info

#%%files -n python-%%{pypi_name}-doc
#%%doc html
#%%license LICENSE.MIT LICENSE LICENSE.APACHE2

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.0-9
- Remove trio.tests imports (removed from trio 0.24+)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.0-8
- Rebuilt for Python 3.13

* Mon Apr 08 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-7
- Ignore trio.TrioDeprecationWarning (closes rhbz#2261596)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 11 2022 Lumír Balhar <lbalhar@redhat.com> - 0.8.0-1
- Update to 0.8.0 (#2142072)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Joel Capitao <jcapitao@redhat.com> - 0.7.0-1
- Update to latest upstream release 0.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Update to latest upstream release 0.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Initial package for Fedora
