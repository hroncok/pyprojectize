%global sum Python library to write SQL queries
%global module_name sql
%global srcname python_sql

Name:           python-%{module_name}
Version:        1.5.1
Release:        3%{?dist}
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{name}
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{name} is a library to write SQL queries in a pythonic way.


%package -n python3-%{module_name}
Summary:        %{sum}
%py_provides    python3-%{name}

%description -n python3-%{module_name}
%{name} is a library to write SQL queries in a pythonic way.


%prep
%setup -q -n %{srcname}-%{version}

# remove upstream egg-info
rm -rf */*.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
%{__python3} setup.py test


%files -n python3-%{module_name}
%doc {CHANGELOG,README}
%{python3_sitelib}/%{srcname}*.dist-info/
%{python3_sitelib}/%{module_name}/
%exclude %{python3_sitelib}/*/tests


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Dan Horák <dan[at]danny.cz> - 1.5.1-1
- updated to 1.5.1 (rhbz#2283663)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Dan Horák <dan[at]danny.cz> - 1.4.3-1
- updated to 1.4.3 (rhbz#2215589)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.11

* Tue May 03 2022 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- updated to 1.4.0 (#2080914)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Dan Horák <dan[at]danny.cz> - 1.3.0-1
- updated to 1.3.0 (#2003949)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.10

* Sun May 16 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2 (#1960909)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Dan Horák <dan[at]danny.cz> - 1.2.1-1
- updated to 1.2.1 (#1886384)

* Mon Oct 05 2020 Dan Horák <dan[at]danny.cz> - 1.2.0-1
- updated to 1.2.0 (#1885348)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Dan Horák <dan[at]danny.cz> - 0.9-7
- drop Python2 subpackage (#1627362)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Dan Horák <dan[at]danny.cz> - 0.9-1
- updated to 0.9 (#1444846)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Dan Horák <dan[at]danny.cz> - 0.8-2
- remove upstream egg-info

* Tue Dec 29 2015 Dan Horák <dan[at]danny.cz> - 0.8-1
- initial Fedora package
