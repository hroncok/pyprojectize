%global pypi_name pyone

Name:           python-%{pypi_name}
Version:        6.0.2
Release:        12%{?dist}
Summary:        Python Bindings for OpenNebula XML-RPC API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://opennebula.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://github.com/OpenNebula/addon-pyone/blob/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-aenum
BuildRequires:  python3-check-manifest
BuildRequires:  python3-coverage
BuildRequires:  python3-dicttoxml
BuildRequires:  python3-lxml
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-tblib
BuildRequires:  python3-xmltodict
%description
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-aenum
Requires:       python3-coverage
Requires:       python3-dicttoxml
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-tblib
Requires:       python3-xmltodict

%description -n python3-%{pypi_name}
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python. It has been integrated into upstream
OpenNebula release cycles from here <

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
install -pm 0644 %{SOURCE1} LICENSE
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 6.0.2-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 6.0.2-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 6.0.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 siddharthvipul <siddharthvipul1@gmail.com> - 6.0.2-1
- Update to upstream version

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.10.4-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.10.4-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 siddharthvipul <siddharthvipul1@gmail.com> - 5.10.4-1
- Initial package.
