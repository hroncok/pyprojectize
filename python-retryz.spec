%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora}
%global with_python2 0
%global with_python3 1
%endif

%global pypi_name retryz


Name:           python-%{pypi_name}
Version:        0.1.9
Release:        28%{?dist}
Summary:        Retry decorator with a bunch of configuration parameters

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/retryz
Source0:        https://pypi.io/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Retry decorator with a bunch of configuration parameters.

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}


Requires:       python2

BuildRequires:  python2-devel

# for running tests
BuildRequires:  python2-pytest
BuildRequires:  python2-hamcrest


%description -n python2-%{pypi_name}
Retry decorator with a bunch of configuration parameters.

%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}


Requires:       python3

BuildRequires:  python3-devel

# for running tests
BuildRequires:  python3-pytest
BuildRequires:  python3-hamcrest

%description -n python3-%{pypi_name}
Retry decorator with a bunch of configuration parameters.

%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%pyproject_wheel
%endif

%check
%if 0%{?with_python2}
PYTHONPATH=. py.test-2.7
%endif
%if 0%{?with_python3}
PYTHONPATH=. py.test-3
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%pyproject_install
%pyproject_save_files -l 'retryz*'
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/retryz*
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.9-28
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.1.9-26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.1.9-22
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.9-19
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.9-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Eric Harney <eharney@redhat.com> - 0.1.9-13
- Add python3-setuptools BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Eric Harney <eharney@redhat.com> - 0.1.9-6
- Remove Python 2 package for Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Eric Harney <eharney@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Wed Feb 01 2017 Eric Harney <eharney@redhat.com> - 0.1.8-1
- Initial package
