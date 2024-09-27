%global pypi_name pyshark

Name:           python-%{pypi_name}
Version:        0.4.3
Release:        11%{?dist}
Summary:        Python packet parsing using wireshark dissectors

License:        MIT
URL:            https://github.com/KimiNewt/pyshark
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       wireshark-cli

%description
Python wrapper for tshark that allowing python packet parsing using wireshark
dissectors. It doesn't actually parse any packets, it simply uses tshark's
ability to export XMLs to use its parsing.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-logbook
BuildRequires:  python3-lxml
BuildRequires:  python3-pytest
BuildRequires:  wireshark-cli
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper for tshark that allowing python packet parsing using wireshark
dissectors. It doesn't actually parse any packets, it simply uses tshark's
ability to export XMLs to use its parsing.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
pushd src
%py3_build
popd

%install
pushd src
%py3_install
popd

# TShark is crashing during the tests, need upstream fix
#%%check
#%%pytest tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.4.3-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.4.3-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.4.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 22 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.3-1
- Update to latest upstream release 0.4.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.2.11-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2.11-3
- Update spec file

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2.11-1
- Update to latest upstream release 0.4.2.11

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2.3-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2.3-3
- Add requirement
- Disable tests

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2.3-2
- Enable tests (rhbz#1714001)
- Add license file
- Use source from GitHub

* Sun May 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2.3-1
- Initial package for Fedora
