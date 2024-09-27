%global pypi_name pysmb

Name:           python-%{pypi_name}
Version:        1.2.4
Release:        14%{?dist}
Summary:        Python SMB/CIFS library

# smb/utils/sha256.py is MIT
License:        zlib and MIT
URL:            https://github.com/miketeo/pysmb
# Upstream source is hard to use
# https://github.com/miketeo/pysmb/issues/163
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

%description
pysmb is an experimental SMB/CIFS library written in Python. It implements the
client-side SMB/CIFS protocol which allows your Python application to access
and transfer files to/from SMB/CIFS shared folders like your Windows file
sharing and Samba folders.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyasn1)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pysmb is an experimental SMB/CIFS library written in Python. It implements the
client-side SMB/CIFS protocol which allows your Python application to access
and transfer files to/from SMB/CIFS shared folders like your Windows file
sharing and Samba folders.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' python3/smb/utils/sha256.py

%build
%py3_build

%install
%py3_install

#%%check
# https://github.com/miketeo/pysmb/issues/165
#%%pytest -v python3/tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG README.txt python3/tests/README_1st.txt
%{python3_sitelib}/nmb/
%{python3_sitelib}/smb/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.4-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.2.4-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.4-1
- Update to latest upstream release 1.2.4 (#1879992)

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Initial package for Fedora