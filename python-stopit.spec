%bcond_without tests

%global pypi_name stopit

%global _description %{expand:
Raise asynchronous exceptions in other threads, control the timeout of
blocks or callables with two context managers and two decorators.

This module provides:

* a function that raises an exception in another thread, including the main
thread.
* two context managers that may stop its inner block activity on timeout.
* two decorators that may stop its decorated callables on timeout.}

Name:           python-%{pypi_name}
Version:        1.1.2
Release:        12%{?dist}
Summary:        Timeout control decorator and context managers

License:        MIT
URL:            https://github.com/glenfant/stopit
Source0:        https://github.com/glenfant/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}

Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# License changed from GPLv3 to MIT
# https://github.com/glenfant/stopit/pull/23
sed -i "s/license='GPLv3',/license='MIT',/g" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{__python3} tests.py
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.2-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.2-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 1.1.2-1
- Initial build
