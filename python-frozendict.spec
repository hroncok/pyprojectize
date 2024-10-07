%global srcname frozendict

Name:           python-%{srcname}
Version:        2.4.4
Release:        3%{?dist}
Summary:        An immutable dictionary

License:        MIT
URL:            https://pypi.python.org/pypi/frozendict
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
frozendict is an immutable wrapper around dictionaries that implements
the complete mapping interface. It can be used as a drop-in
replacement for dictionaries where immutability is desired.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-wheel

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
# Build the python only version (no python 3.11 support)
export FROZENDICT_PURE_PY=1
%py3_build_wheel

%install
export FROZENDICT_PURE_PY=1
%pyproject_install
%pyproject_save_files -l %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.4.4-2
- Rebuilt for Python 3.13

* Tue May 07 2024 Orion Poplawski <orion@nwra.com> - 2.4.4-1
- Update to 2.4.4

* Mon Apr 15 2024 Orion Poplawski <orion@nwra.com> - 2.4.2-1
- Update to 2.4.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Orion Poplawski <orion@nwra.com> - 2.3.10-1
- Update to 2.3.10

* Sat Nov 25 2023 Orion Poplawski <orion@nwra.com> - 2.3.9-1
- Update to 2.3.9

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3.8-2
- Rebuilt for Python 3.12

* Fri May 05 2023 Orion Poplawski <orion@nwra.com> - 2.3.8-1
- Update to 2.3.8

* Sun Apr 09 2023 Orion Poplawski <orion@nwra.com> - 2.3.7-1
- Update to 2.3.7

* Wed Mar 22 2023 Orion Poplawski <orion@nwra.com> - 2.3.6-1
- Update to 2.3.6

* Sat Feb 18 2023 Orion Poplawski <orion@nwra.com> - 2.3.5-1
- Update to 2.3.5

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Orion Poplawski <orion@nwra.com> - 2.3.4-1
- Update to 2.3.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2-22
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2-19
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-16
- Rebuilt for Python 3.9

* Tue Feb  4 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2-15
- Fix compatibility with python3.9 (#1797691)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-9
- Subpackage python2-frozendict has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Dec 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-8
- Enable python dependency generator

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.2-1
- Initial package
