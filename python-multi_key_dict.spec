%{?!_without_python2:%global with_python2 0%{?_with_python2:1} || (0%{?fedora} < 31 && 0%{?rhel} < 8)}
%{?!_without_python3:%global with_python3 0%{?_with_python3:1} || !0%{?rhel} || 0%{?rhel} >= 7}

%global srcname multi_key_dict
%global commit 540e913b714187101d7a142eadc108c48ccbd8e1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        2.0.3
Release:        29%{?dist}
Summary:        Multi-key dictionary implementation in Python

License:        MIT
URL:            https://github.com/formiaczek/%{srcname}
Source0:        https://github.com/formiaczek/%{srcname}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Implementation of a multi-key dictionary, i.e.:

(key1[,key2, ..]) => value

This dictionary has a similar interface to the standard dictionary => but
is extended to support multiple keys referring to the same element.


%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{srcname}
Implementation of a multi-key dictionary, i.e.:

(key1[,key2, ..]) => value

This dictionary has a similar interface to the standard dictionary => but
is extended to support multiple keys referring to the same element.
%endif


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname}
Implementation of a multi-key dictionary, i.e.:

(key1[,key2, ..]) => value

This dictionary has a similar interface to the standard dictionary => but
is extended to support multiple keys referring to the same element.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%pyproject_wheel
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%pyproject_install
%pyproject_save_files -l %{srcname}
%endif


%check
%if 0%{?with_python2}
%{__python2} %{buildroot}%{python2_sitelib}/%{srcname}.py
%endif

%if 0%{?with_python3}
%{__python3} %{buildroot}%{python3_sitelib}/%{srcname}.py
%endif


%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.txt
%{python2_sitelib}/%{srcname}.py
%{python2_sitelib}/%{srcname}.py[co]
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.txt
%endif


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.3-28
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Scott K Logan <logans@cottsay.net> - 2.0.3-25
- Add missing BuildRequires: python3-setuptools (rhbz#2220343)

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.3-24
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.3-21
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.3-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Scott K Logan <logans@cottsay.net> - 2.0.3-10
- Subpackage python2-multi_key_dict has been removed from f31+ (rhbz#1716662)
- Python 3 subpackage has been added for epel7
- Update unified spec format

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 08 2016 Scott K Logan <logans@cottsay.net> - 2.0.3-1
- Initial package
