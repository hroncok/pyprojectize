%global pypi_name dtfabric
%global date 20230520

Name:           python-%{pypi_name}
Version:        0.0.%{date}
Release:        9%{?dist}
Summary:        Tool to manage data types and structures, as used by libyal

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/libyal/dtfabric
Source0:        %{url}/archive/%{date}/%{pypi_name}-%{date}.tar.gz
BuildArch:      noarch

%description
dtfabric is a project to manage data types and structures, as used in the
libyal projects.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pyyaml
BuildRequires:  python3-six
BuildRequires:  python3-pip
BuildRequires:  python3-pbr
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
dtfabric is a project to manage data types and structures, as used in the
libyal projects.

%prep
%autosetup -n %{pypi_name}-%{date}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{_defaultdocdir}/%{pypi_name}/*

%files -n python3-%{pypi_name}
%doc ACKNOWLEDGEMENTS AUTHORS README
%license LICENSE
%{_bindir}/*.py
%{python3_sitelib}/*.dist-info/
%{python3_sitelib}/%{pypi_name}/

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.20230520-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20230520-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.20230520-7
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Maxwell G <maxwell@gtmx.me> - 0.0.20230520-6
- Remove unused python3-mock test dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20230520-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20230520-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20230520-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.20230520-2
- Rebuilt for Python 3.12

* Tue May 23 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20230520-1
- Update to latest upstream release 20230520 (closes rhbz#2154653)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220213-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220213-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.20220213-2
- Rebuilt for Python 3.11

* Wed Feb 16 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20220213-1
- Update to latest upstream release 20220213 (closes rhbz#2046649)

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20220126-1
- Update to latest upstream release 20220126 (closes rhbz#2045968)

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20220125-1
- Update to latest upstream release 20220125 (closes rhbz#2045899)

* Tue Jan 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20220124-1
- Update to latest upstream release 20220124 (closes rhbz#2044246)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20210731-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20210731-1
- Update to latest upstream release 20210731 (rhbz#1988665)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200621-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.20200621-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200621-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200621-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200621-3
- Update summary

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200621-2
- Add python3-setuptools as BR

* Sun Jun 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200621-1
- Update to latest upstream release 20200621 (rhbz#20200621)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20200119-2
- Rebuilt for Python 3.9

* Fri Mar 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200119-1
- Update source URL
- Update to latet uptream release 20200119 (rhbz#1815602)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190120-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190120-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190120-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20190120-1
- Update version (rhbz#1720890)

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 20190120-1
- Initial package for Fedora
