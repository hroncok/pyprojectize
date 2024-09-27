%global pypi_name ipgetter2
%bcond_with network

Name:           python-%{pypi_name}
Version:        1.1.11
Release:        15%{?dist}
Summary:        Python library to fetch your external IP address

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/starofrainnight/ipgetter2
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

%description
Utility to fetch your external IP address. This module is designed to fetch
your external IP address from the internet. It is used mostly when behind
a NAT. It picks your IP randomly from a server list to minimize request
overhead on a single server.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner

%if %{with network}
BuildRequires:  python3-chardet
BuildRequires:  python3-click
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
Python library to fetch your external IP address. This module is designed to
fetch your external IP address from the internet. It is used mostly when behind
a NAT. It picks your IP randomly from a server list to minimize request
overhead on a single server.

%package -n     %{pypi_name}
Summary:        Utility to fetch your external IP address

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
 
%description -n %{pypi_name}
Utility to fetch your external IP address.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' ipgetter2/*.py

%build
%py3_build

%install
%py3_install

%if %{with network}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst CONTRIBUTING.rst HISTORY.rst AUTHORS.rst
%{python3_sitelib}/%{pypi_name}
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%files -n %{pypi_name}
%{_bindir}/ipgetter2

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.11-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.11-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.11-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.11-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.11-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.11-1
- Update to latest upstream release 1.1.11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.9-1
- Initial package for Fedora