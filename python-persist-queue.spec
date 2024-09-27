%if 0%{?fedora}
%global with_python2 0
%global with_python3 1
%endif

%global pypi_name persist-queue

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        8%{?dist}
Summary:        A single process, persistent multi-producer, multi-consumer queue

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.io/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A single process, persistent multi-producer, multi-consumer queue

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose2
BuildRequires:  python2-msgpack

Requires: python2-msgpack

%description -n python2-%{pypi_name}
A single process, persistent multi-producer, multi-consumer queue

%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-nose2
BuildRequires:  python3-msgpack
BuildRequires:  python3-setuptools

Requires: python3-msgpack

%description -n python3-%{pypi_name}
A single process, persistent multi-producer, multi-consumer queue

%endif

%prep
%setup -n %{pypi_name}-%{version}

%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif

%check
%if 0%{?with_python2}
nose2-2.7 persistqueue.tests.test_queue
%endif
%if 0%{?with_python3}
nose2 persistqueue.tests.test_queue
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%exclude %{python2_sitelib}/tests
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%exclude %{python3_sitelib}/tests
%endif

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.12

* Thu Jan 26 2023 Eric Harney <eharney@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.11

* Mon Jan 24 2022 Eric Harney <eharney@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Eric Harney <eharney@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Eric Harney <eharney@redhat.com> - 0.5.1-1
- Update to 0.5.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Eric Harney <eharney@redhat.com> - 0.5.0-4
- Add python3-setuptools BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Eric Harney <eharney@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Eric Harney <eharney@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Eric Harney <eharney@redhat.com> - 0.4.0-4
- Remove Python 2 packages for Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Eric Harney <eharney@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Tue May 15 2018 Eric Harney <eharney@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Wed Feb 14 2018 Eric Harney <eharney@redhat.com> - 0.3.5-1
- Update to 0.3.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.4-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Dec 18 2017 Eric Harney <eharney@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Thu Nov 09 2017 Eric Harney <eharney@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Eric Harney <eharney@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Tue May 16 2017 Eric Harney <eharney@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Tue Mar 14 2017 Eric Harney <eharney@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Mon Mar 13 2017 Eric Harney <eharney@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Fri Mar 10 2017 Eric Harney <eharney@redhat.com> - 0.1.6-1
- Update to 0.1.6
- License is now BSD

* Wed Feb 15 2017 Eric Harney <eharney@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Tue Feb 14 2017 Eric Harney <eharney@redhat.com> - 0.1.4-1
- Initial package
