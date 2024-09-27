# Created by pyp2rpm-1.0.1
%global pypi_name testrepository

Name:           python-%{pypi_name}
Version:        0.0.20
Release:        37%{?dist}
Summary:        A repository of test results

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://launchpad.net/testrepository
Source0:        http://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.


%package -n python3-%{pypi_name}
Summary:        A repository of test results (for Python 3)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-fixtures
BuildRequires:  python3-subunit
BuildRequires:  python3-testtools
BuildRequires:  python3-extras
Requires:       python3-fixtures
Requires:       python3-subunit
Requires:       python3-testtools
Requires:       python3-extras
%{?python_provide:%python_provide python3-%{pypi_name}}

# Provide a clean upgrade path
Obsoletes:      python-%{pypi_name} < 0.0.20-20
Obsoletes:      python2-%{pypi_name} < 0.0.20-20

%description -n python3-%{pypi_name}
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

This package is for Python 3.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build


%install
%py3_install
mv %{buildroot}%{_bindir}/testr{,-%{python3_version}}
ln -s ./testr-%{python3_version} %{buildroot}%{_bindir}/testr


%files -n python3-%{pypi_name}
%doc README.txt Apache-2.0
%{_bindir}/testr
%{_bindir}/testr-%{python3_version}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.20-37
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.0.20-35
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.0.20-31
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.0.20-28
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.20-25
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-20
- Subpackage python2-testrepository has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-15
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Tomas Orsava <torsava@redhat.com> - 0.0.20-14
- Conditionalize the Python 2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.0.20-12
- Finish modernizing spec file

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.20-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.20-10
- Python 2 binary package renamed to python2-testrepository
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5
- Remove check phases as tests arent run at all

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Pádraig Brady <pbrady@redhat.com> - 0.0.20-2
- Fix python2 breakage in previous package

* Tue Dec 09 2014 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-1
- Update to 0.0.20
- Introduce Python 3 subpackage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Pádraig Brady <pbrady@redhat.com> - 0.0.18-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Pádraig Brady <P@draigBrady.com> - 0.0.15-4
- Update to 0.0.15

* Wed Feb 20 2013 Pádraig Brady <P@draigBrady.com> - 0.0.14-1
- Update to 0.0.14

* Thu Jan 03 2013 Pádraig Brady <P@draigBrady.com> - 0.0.11-1
- Initial package.
