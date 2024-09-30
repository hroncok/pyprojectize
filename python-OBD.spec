%bcond_without check
%global srcname OBD

Name:          python-%{srcname}
Version:       0.7.2
Release:       5%{?dist}
Summary:       OBD-II serial module for reading engine data
License:       GPL-2.0-or-later
URL:           https://github.com/brendan-w/%{name}
Source0:       https://github.com/brendan-w/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix python dependency generator error
# error: Illegal char '*' (0x2a) in: 0.7.*
# error: Illegal char '*' (0x2a) in: 3.*
Patch0:        %{name}-dep-ver.patch
BuildArch:     noarch

%global desc A python module for handling realtime sensor data from OBD-II vehicle ports.\
Works with ELM327 OBD-II adapters, and is fit for the Raspberry Pi.

%description
%{desc}

%package -n python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3-pint >= 0.16
BuildRequires: python3-pytest
BuildRequires: python3-pyserial >= 3
%endif
%if 0%{fedora} < 30
Requires:      python3-pint >= 0.7
Requires:      python3-pyserial >= 3
%endif

%description -n python3-%{srcname}
%{desc}

Python 3 version.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l obd

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v
%endif

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.7.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Dominik Mierzejewski <rpm@greysector.net> - 0.7.2-1
- update to 0.7.2 (resolves rhbz#2221848)
- relax pint dependency
- switch to SPDX expression in License tag

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Python Maint <python-maint@redhat.com> - 0.7.1-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.7.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.7.1-1
- update to 0.7.1 (#1710329)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.7.0-1
- initial packaging
- fix dependency version declarations in setup.py
