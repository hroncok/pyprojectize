Name:           home-assistant-cli
Version:        0.9.6
Release:        11%{?dist}
Summary:        Command-line tool for Home Assistant

License:        Apache-2.0
URL:            https://github.com/home-assistant/home-assistant-cli
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# Allow later dateparser
# https://github.com/home-assistant-ecosystem/home-assistant-cli/pull/403
Patch0:          %{url}/pull/403.patch

# Allow later ruamel
# https://github.com/home-assistant-ecosystem/home-assistant-cli/pull/412
Patch1:          %{url}/pull/412.patch

BuildRequires:  python3-devel
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-aiohttp
BuildRequires:  python3-regex
BuildRequires:  python3-mypy
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-sugar
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest
BuildRequires:  python3-requests-mock
BuildRequires:  python3-dateparser
BuildRequires:  python3-click-log
BuildRequires:  python3-click
BuildRequires:  python3-netdisco
BuildRequires:  python3-tabulate
BuildRequires:  python3-jsonpath-ng

%description
The Home Assistant Command-line interface (hass-cli) allows one to work with
a local or a remote Home Assistant instance directly from the command-line.

%prep
%autosetup -n %{name}-%{version} -p1
sed -i "/>=0.3.2,<0.4/d" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l homeassistant_cli

%check
%pyproject_check_import

PYTHONPATH=%{buildroot}/%{python3_sitelib}/ pytest-%{python3_version} -v tests \
  -k "not test_commands_loads[template]"

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/hass-cli

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.6-10
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Daniel Milnes <daniel@daniel-milnes.uk> - 0.9.6-7
- Migrate license to SPDX

* Sat Dec 30 2023 Daniel Milnes <daniel@daniel-milnes.uk> - 0.9.6-6
- Allow newer ruamel (closes rhbz#2246610)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.9.6-4
- Rebuilt for Python 3.12

* Sat Mar 11 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.6-3
- Allow later dateparser

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.6-1
- Update to latest upstream release 0.9.6

* Sat Oct 01 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Update to latest upstream release 0.9.5 (closes rhbz#2058155)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Update to latest upstream release 0.9.4 (closes rhbz#1946226)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.1-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to latest upstream release 0.9.1

* Mon Apr 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to latest upstream release 0.9.0

* Tue Mar 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-2
- Add missing BR

* Sun Nov 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update to latest upstream release 0.8.0

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Initial package for Fedora
