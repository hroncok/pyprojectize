%global pypi_name socialscan
%bcond_with network

Name:           %{pypi_name}
Version:        1.4.2
Release:        11%{?dist}
Summary:        CLI and library for usage checking of user names and email addresses

License:        MPL-2.0
URL:            https://github.com/iojw/socialscan
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with network}
BuildRequires:  python3-pytest
BuildRequires:  python3-aiohttp
%endif

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
socialscan offers accurate and fast checks for email address and user name
usage on online platforms. Given an email address or user name, socialscan
returns whether it is available, taken or invalid on online platforms.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
socialscan offers accurate and fast checks for email address and user name
usage on online platforms. Given an email address or user name, socialscan
returns whether it is available, taken or invalid on online platforms.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with network}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
  -k "not Instagram"
%endif

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.2-10
- Rebuilt for Python 3.13

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.2-9
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.2-6
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.2-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.2-1
- Update to latest upstream release 1.4.2 (rhbz#1983316)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream release 1.4.0 (#1893069)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0 (#1882611)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.6-1
- Initial package
