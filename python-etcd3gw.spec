%global srcname etcd3gw

%if 0%{?fedora} && 0%{?fedora} < 30
%bcond_without python2
%bcond_without python3
%else
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif
%endif

Name:           python-%{srcname}
Version:        2.4.1
Release:        1%{?dist}
Summary:        An etcd3 gateway Python client

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

%description
A python client for etcd3 grpc-gateway v3alpha API

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel

BuildRequires:  python2-futurist
BuildRequires:  python2-oslotest
BuildRequires:  python2-pytest
BuildRequires:  python2-requests

Requires:  python2-futurist
Requires:  python2-pbr
Requires:  python2-requests
Requires:  python2-six


%description -n python2-%{srcname}
A python client for etcd3 grpc-gateway v3alpha API
%endif

%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

BuildRequires:  python3-futurist
BuildRequires:  python3-oslotest
BuildRequires:  python3-pytest
BuildRequires:  python3-requests

Requires: python3-futurist
Requires: python3-pbr
Requires: python3-requests
Requires: python3-six


%description -n python3-%{srcname}
A python client for etcd3 grpc-gateway v3alpha API
%endif

%prep
%autosetup -n %{srcname}-%{version}

# Let's manage dependencies using rpm deps.
rm -f *requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%pyproject_wheel
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%pyproject_install
%pyproject_save_files -l %{srcname}
%endif

%check
%if %{with python2}
export PYTHON=%{__python2}
py.test
%endif

%if %{with python3}
export PYTHON=%{__python3}
# workaround for https://bugs.launchpad.net/testrepository/+bug/1229445
rm -rf .testrepository/times.dbm
py.test-3
%endif

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md CONTRIBUTING.rst HACKING.rst
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%if %{with python3}
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CONTRIBUTING.rst HACKING.rst
%endif


%changelog
* Mon Aug  5 2024 John Eckersberg <jeckersb@redhat.com> - 2.4.1-1
- New upstream version 2.4.1 (rhbz#2301633)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Python Maint <python-maint@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.13

* Tue Feb 27 2024 John Eckersberg <jeckersb@redhat.com> - 2.4.0-1
- New upstream version 2.4.0 (rhbz#2266334)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 14 2023 John Eckersberg <jeckersb@redhat.com> - 2.3.0-1
- New upstream version 2.3.0 (rhbz#2254543)

* Thu Nov 16 2023 John Eckersberg <jeckersb@redhat.com> - 2.2.0-1
- New upstream version 2.2.0 (rhbz#2250040)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 John Eckersberg <jeckersb@redhat.com> - 2.1.0-1
- New upstream version 2.1.0 (rhbz#2123402)

* Thu Aug  4 2022 John Eckersberg <jeckersb@redhat.com> - 2.0.0-1
- New upstream version 2.0.0 (rhbz#2115274)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Python Maint <python-maint@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.11

* Thu May 12 2022 John Eckersberg <jeckersb@redhat.com> - 1.0.2-1
- New upstream version 1.0.2 (rhbz#2082061)

* Wed Feb  9 2022 John Eckersberg <jeckersb@redhat.com> - 1.0.1-1
- New upstream version 1.0.1 (rhbz#2052448)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  1 2021 John Eckersberg <jeckersb@redhat.com> - 1.0.0-1
- New upstream version 1.0.0 (rhbz#1978274)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 2020 John Eckersberg <jeckersb@redhat.com> - 0.2.6-1
- New upstream version 0.2.6 (rhbz#1862104)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-2
- Rebuilt for Python 3.9

* Tue Jan 28 2020 John Eckersberg <eck@redhat.com> - 0.2.5-1
- New upstream version 0.2.5 (rhbz#1795745)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-10
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Alfredo Moralejo <amoralej@redhat.com> - 0.2.4-9
- Use pytest to run unit tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  8 2019 John Eckersberg <eck@redhat.com> - 0.2.4-7
- Before f30, build for both py2 and py3
- Add test workaround when run for both py2 and py3

* Tue Mar  5 2019 John Eckersberg <eck@redhat.com> - 0.2.4-6
- Add missing req for python3-pbr

* Tue Mar 05 2019 Eric Harney <eharney@redhat.com> - 0.2.4-5
- Add missing reqs for python3

* Mon Mar 04 2019 Eric Harney <eharney@redhat.com> - 0.2.4-4
- Remove runtime req on oslotest

* Thu Feb 28 2019 Alfredo Moralejo <amoralej@redhat.com> - 0.2.4-3
- Remve {test-,}requirements.txt to manage dependencies manually.

* Wed Feb 13 2019 John Eckersberg <eck@redhat.com> - 0.2.4-1
- Initial package

