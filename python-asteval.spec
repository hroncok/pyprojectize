%global pypi_name asteval

Name:           python-%{pypi_name}
Version:        1.0.4
Release:        1%{?dist}
Summary:        Evaluator of Python expression using ast module

License:        MIT
URL:            http://github.com/newville/asteval
Source0:        %{pypi_source}
BuildArch:      noarch

%description
ASTEVAL is a safe(ish) evaluator of Python expressions and statements,
using Python's ast module. The idea is to provide a simple, safe, and robust
miniature mathematical language that can handle user-input. The emphasis here
is on mathematical expressions, and so many functions from numpy are imported
and used if available.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools_scm

%description -n python3-%{pypi_name}
ASTEVAL is a safe(ish) evaluator of Python expressions and statements,
using Python's ast module. The idea is to provide a simple, safe, and robust
miniature mathematical language that can handle user-input. The emphasis here
is on mathematical expressions, and so many functions from numpy are imported
and used if available.

%package -n python-%{pypi_name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' asteval/asteval.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo} html/_static/empty

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Sep 17 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.4-1
- Update to latest upstream release 1.0.4 (closes rhbz#2295426)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.33-1
- Update to latest upstream release 0.9.33 (closes rhbz#2283028)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.32-2
- Rebuilt for Python 3.13

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.32-1
- Update to latest upstream release 0.9.32 (closes rhbz#2267569)

* Sat Feb 03 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.31-1
- Update to latest upstream release 0.9.31 (closes rhbz#2215732)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.9.29-2
- Rebuilt for Python 3.12

* Sat Feb 11 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.29-1
- Update to latest upstream release 0.9.29 (closes rhbz#2169113)

* Fri Jan 27 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.28-1
- Update to latest upstream release 0.9.28 (closes rhbz#2089878)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.27-1
- Update to latest upstream release 0.9.27 (closes #2089878)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.26-2
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.26-1
- Update to latest upstream release 0.9.26 (#2041226)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.25-1
- Update to 0.9.25 (fixes RHBZ#1974537, fixes RHBZ#1899470)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.23-2
- Rebuilt for Python 3.10

* Sat Feb 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.23-1
- Update to latest upstream release 0.9.23 (#1927934)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.22-1
- Update to latest upstream release 0.9.22 (#1927934)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.21-1
- Update to latest upstream release 0.9.21 (#1897861)

* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.19-1
- Tests were fixed upstream for Python 3.9
- Update to latest upstream release 0.9.19

* Tue Aug 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.18-5
- Fix FTBFS (rhbz#1819177)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.18-2
- Rebuilt for Python 3.9

* Sat Dec 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.18-1
- Initial package for Fedora
