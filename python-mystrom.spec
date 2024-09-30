%global pypi_name mystrom

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        14%{?dist}
Summary:        Python API client for interacting with myStrom devices

License:        MIT
URL:            https://github.com/home-assistant-ecosystem/python-mystrom
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Asynchronous Python API client for interacting with myStrom devices like bulbs
and plugs. The buttons can be programmed easily with the command-line tool.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Asynchronous Python API client for interacting with myStrom devices like bulbs
and plugs. The buttons can be programmed easily with the command-line tool.

%package -n %{pypi_name}
Summary:        CLI tool to interact with myStrom devices

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
%py_provides    python3-%{pypi_name}

%description -n %{pypi_name}
CLI tool to interact with myStrom devices (bulbs, buttons and plugs).

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l py%{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-2
- Add python3-setuptools as BR

* Mon Jun 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-1
- Update to latest upstream release 1.1.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.2-1
- Update to latest upstream release 1.1.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Initial package for Fedora
