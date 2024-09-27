%{?python_enable_dependency_generator}
%global srcname spur
%global sum Run commands locally or over SSH using the same interface
%global desc Run commands and manipulate files locally or over SSH using the same interface.

Name:           python-%{srcname}
Version:        0.3.23
Release:        7%{?dist}
Summary:        %{sum}

License:        BSD-2-Clause
URL:            https://github.com/mwilliamson/spur.py
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?rhel} < 9
BuildRequires:  python3-nose
%endif
BuildRequires:  python3dist(paramiko) >= 1.13.1
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}.py-%{version}
sed -i -e "s/’/'/g" README.rst


%build
%py3_build


%install
%py3_install


# skip tests on EL9 due to deprecated python-nose
%if 0%{?rhel} && 0%{?rhel} < 9
%check
# Exclude tests which require SSH server
nosetests-%{python3_version} -v -e testing -e ssh_tests
%endif


%files -n python3-%{srcname}
%license LICENSE
%doc CHANGES CONTRIBUTING.rst README.rst
%{python3_sitelib}/%{srcname}*


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.3.23-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.3.23-2
- Rebuilt for Python 3.12

* Wed Mar 15 2023 Orion Poplawski <orion@nwra.com> - 0.3.23-1
- Update to 0.3.23

* Sun Jan 22 2023 Orion Poplawski <orion@nwra.com> - 0.3.22-4
- Relax paramiko version requirement
- Use SPDX License tag
- Fix check version conditional

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Orion Poplawski <orion@nwra.com> - 0.3.22-2
- Skip tests on EL9 due to deprecated python-nose

* Wed Jan 04 2023 Orion Poplawski <orion@nwra.com> - 0.3.22-1
- Update to 0.3.22

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.3.21-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.21-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.21-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.21-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Orion Poplawski <orion@nwra.com> - 0.3.21-4
- Exclude failing tests (bugz#1705954)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.21-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Orion Poplawski <orion@nwra.com> - 0.3.21-1
- Update to 0.3.21

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.20-1
- Update to 0.3.20

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-10
- Subpackage python2-spur has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.17-9
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.17-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.17-2
- Rebuild for Python 3.6

* Fri Apr 29 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.17-1
- Update to 0.3.17

* Mon Apr 25 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.16-1
- Update to 0.3.16

* Tue Apr 5 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.15-1
- Initial package
