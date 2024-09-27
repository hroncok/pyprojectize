%global pypi_name dbus-next
%global srcname   dbus_next

%bcond_without  tests

Name:           python-%{pypi_name}
Version:        0.2.3
Release:        11%{?dist}
Summary:        Zero-dependency DBus library for Python with asyncio support

License:        MIT
URL:            https://github.com/altdesktop/python-dbus-next
# pypi_source archive does not include test data
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  /usr/bin/dbus-run-session
%endif

%global _description %{expand:
python-dbus-next is a Python library for DBus that aims to be a fully
featured high level library primarily geared towards integration of
applications into Linux desktop and mobile environments.

Desktop application developers can use this library for integrating their
applications into desktop environments by implementing common DBus
standard interfaces or creating custom plugin interfaces.

Desktop users can use this library to create their own scripts and
utilities to interact with those interfaces for customization of their
desktop environment.

python-dbus-next plans to improve over other DBus libraries for Python in
the following ways:

 -  Zero dependencies and pure Python 3.
 -  Support for multiple IO backends including asyncio and the GLib main
    loop.
 -  Nonblocking IO suitable for GUI development.
 -  Target the latest language features of Python for beautiful services
    and clients.
 -  Complete implementation of the DBus type system without ever guessing
    types.
 -  Integration tests for all features of the library.
 -  Completely documented public API.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Fix permissions for examples
chmod -x examples/*.py

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
# tests require dbus daemon to be running
%global __pytest  /usr/bin/dbus-run-session -- %{__pytest}
# test_tcp_connection_with_forwarding is broken by dbus 1.14.4
# altdesktop/python-dbus-next#135
PYTHONPATH="${PWD}" %pytest -k 'not test_tcp_connection_with_forwarding'

%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG.md README.md examples/
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.3-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.2.3-6
- Rebuilt for Python 3.12

* Mon Jan 23 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.3-5
- Skip failing test

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.10

* Mon Mar 01 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.2-1
- Initial import (#1929001)
