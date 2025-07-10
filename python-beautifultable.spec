%global pypi_name beautifultable

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        8%{?dist}
Summary:        Print ASCII tables for terminals

License:        MIT
URL:            https://github.com/pri22296/beautifultable
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides the BeautifulTable class for easily printing tabular data
in a visually appealing ASCII format to a terminal.

Features included but not limited to:

- Full customization of the look and feel of the table
- Build the Table as you wish, By adding rows, or by columns or even mixing both
  these approaches
- Full support for colors using ANSI sequences or any library of your choice
- Plenty of predefined styles for multiple use cases and option to create
  custom ones
- Support for Unicode characters

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-wcwidth
 
%description -n python3-%{pypi_name}
This package provides the BeautifulTable class for easily printing tabular data
in a visually appealing ASCII format to a terminal.

Features included but not limited to:

- Full customization of the look and feel of the table
- Build the Table as you wish, By adding rows, or by columns or even mixing both
  these approaches
- Full support for colors using ANSI sequences or any library of your choice
- Plenty of predefined styles for multiple use cases and option to create
  custom ones
- Support for Unicode characters

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n %{name}-doc
%doc html
%license LICENSE.txt

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Update to latest upstream release 1.1.0 (closes #2082669)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Update to latest upstream release 1.0.1 (#1917935)

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream release 1.0.0 (#1858630)

* Thu Apr 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-2
- Add missing BR for tests (#1812435)

* Wed Mar 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Initial package for Fedora
