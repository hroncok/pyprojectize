# Created by pyp2rpm-1.1.2 and rewrote manually afterwards
%global pypi_name docker-pycreds

%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
# Disable python2 build by default
%bcond_with python2
%else
%bcond_with python3
%bcond_without python2
%endif

# the test suite is diabled b/c it needs docker-credential-secretservice binary
# and we don't have that now (Sep 2016) in Fedora
%bcond_with tests

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        22%{?dist}
Summary:        Python bindings for the docker credentials store API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/shin-/dockerpy-creds/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch


%description
Python bindings for the docker credentials store API

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Python bindings for the docker credentials store API

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six

%if %{with tests}
BuildRequires:  python2-pytest
%endif # tests

%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:  python2-six

%description -n python2-%{pypi_name}
Python bindings for the docker credentials store API
%endif # with python2

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        Python bindings for the docker credentials store API

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%if %{with tests}
BuildRequires:  python3-pytest
%endif # tests

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:  python3-six

%description -n python3-%{pypi_name}
Python bindings for the docker credentials store API

%endif # python3


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%if %{with python2}
%py2_build
%endif # with python2
%if %{with python3}
%py3_build
%endif # with python3


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with python2}
%py2_install
%endif # with python2
%if %{with python3}
%py3_install
%endif # with python3


# we are not using setup.py test here b/c the project pins to specific versions
%check
# sanity test
%if %{with python2}
%{__python2} -c "import dockerpycreds"
%if %{with tests}
PYTHONPATH="${PWD}" py.test-%{python2_version} -vv tests/
%endif # tests
%endif # with python2

%if %{with python3}
%{__python3} -c "import dockerpycreds"
%if %{with tests}
PYTHONPATH="${PWD}" py.test-%{python3_version} -vv tests/
%endif # tests
%endif # python3

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.md
%license LICENSE
%{python2_sitelib}/dockerpycreds
%{python2_sitelib}/docker_pycreds-%{version}-py?.?.egg-info
%endif # with python2

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/dockerpycreds
%{python3_sitelib}/docker_pycreds-%{version}-py%{python3_version}.egg-info
%endif # python3


%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.0-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Yatin Karel <ykarel@redhat.com> - 0.4.0-2
- Enable python2 build for el7

* Tue Feb 05 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.4.0-1
- New upstream release 0.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.3.0-1
- New upstream release 0.3.0

* Wed May 02 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.2.3-1
- New upstream release 0.2.3

* Tue Apr 03 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.2.2-2
- Conditionalize the Python 2 subpackage and don't build it on EL > 7

* Mon Feb 19 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.2.2-1
- New upstream release 0.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Carl George <carl@george.computer> - 0.2.1-6
- Add BuildRequires for setuptools

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuild for Python 3.6

* Wed Oct 05 2016 Tomas Tomecek <ttomecek@redhat.com> - 0.2.1-2
- rebuilt

* Mon Sep 26 2016 Tomas Tomecek <ttomecek@redhat.com> - 0.2.1-1
- Initial package.
