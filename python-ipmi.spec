%global pypi_name python-ipmi
%global srcname ipmi

Name:           python-%{srcname}
Version:        0.5.5
Release:        2%{?dist}
Summary:        Pure python IPMI library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/kontron/python-ipmi
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3dist(markdown)


%description
Pure Python IPMI Library.

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Pure Python IPMI Library.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyipmi

%check
%pyproject_check_import

export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/ipmitool.py

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.5-2
- convert license to SPDX

* Wed Aug 07 2024 Filipe Rosset <rosset.filipe@gmail.com> - 0.5.5-1
- Update to 0.5.5 fixes rhbz#2301154 rhbz#2267993 rhbz#2276613 rhbz#2291743

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 0.5.4-2
- Rebuilt for Python 3.12

* Wed Mar 08 2023 Luis Bazan <lbazan@fedoraproject.org> - 0.5.4-1
- New upstream version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Luis Bazan <lbazan@fedoraproject.org> - 0.5.2-2
- remove tests

* Mon Jun 27 2022 Luis Bazan <lbazan@fedoraproject.org> - 0.5.2-1
- New upstream version

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 Luis Bazan <lbazan@fedoraproject.org> - 0.5.1-1
- New upstream version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Luis Bazan <lbazan@fedoraproject.org> - 0.5.0-1
- New upstream version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.4.2-4
- Fix compatibility with Python 3.9 (#1792985)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.2-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.1-2
- Fix comment #1 BZ #1676987

* Wed Feb 13 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.1-1
- Initial package
