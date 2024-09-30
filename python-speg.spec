%{?python_enable_dependency_generator}
%global py2support 0
%global srcname speg
%global commit 877acddfd5ac5ae8b4a4592d045e74e108477643
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.3
Release:        23.git%{shortcommit}%{?dist}
Summary:        A PEG-based parser interpreter with memoization (in time)
License:        MIT
URL:            https://github.com/avakar/speg
Source0:        https://github.com/avakar/speg/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
A PEG-based parser interpreter with memoization.

%if %{py2support}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{srcname}
A PEG-based parser interpreter with memoization.
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
A PEG-based parser interpreter with memoization.

%prep
%autosetup -n %{srcname}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{py2support}
%py2_build
%endif
%pyproject_wheel

%install
%if %{py2support}
%py2_install
%endif
%pyproject_install
%pyproject_save_files -l %{srcname}

# Note that there is no %%files section for the unversioned python module
%if %{py2support}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3-22.git877acdd
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3-18.git877acdd
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3-15.git877acdd
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3-12.git877acdd
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-9.git877acdd
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-7.git877acdd
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-6.git877acdd
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3-3.git877acdd
- Enable python dependency generator

* Thu Jan  3 2019 Tom Callaway <spot@fedoraproject.org> - 0.3-2.git877acdd
- disable py2support

* Wed Jan  2 2019 Tom Callaway <spot@fedoraproject.org> - 0.3-1.git877acdd
- new package

