%global pypi_name PyKMIP
%global sname pykmip

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{sname}
Version:        0.8.0
Release:        22%{?dist}
Summary:        Python implementation of the Key Management Interoperability Protocol

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/OpenKMIP/PyKMIP
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         enum34.patch
BuildArch:      noarch

%description
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).

%if %{with python2}
%package -n python2-%{sname}
Summary:        Python implementation of the Key Management Interoperability Protocol

BuildRequires:       python2-devel
BuildRequires:       python2-six
BuildRequires:       python2-setuptools

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:       python2-enum34
%else
BuildRequires:       python-enum34
%endif

Requires:     python2-cryptography
Requires:     python2-requests
Requires:     python2-six
Requires:     python2-sqlalchemy

%if 0%{?fedora} || 0%{?rhel} > 7
Requires:     python2-enum34
%else
Requires:     python-enum34
%endif

%description -n python2-%{sname}
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).
%endif

%if %{with python3}
%package -n python3-%{sname}
Summary:        Python implementation of the Key Management Interoperability Protocol


BuildRequires:       python3-devel
BuildRequires:       python3-six

Requires:     python3-cryptography
Requires:     python3-requests
Requires:     python3-six
Requires:     python3-sqlalchemy

%description -n python3-%{sname}
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).

%endif

%prep
%autosetup -n %{pypi_name}-%{version}

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
%pyproject_save_files -l kmip
%endif

%if %{with python2}
%check
%pyproject_check_import
%files -n python2-%{sname}
%doc README.rst
%license LICENSE.txt
%if !%{with python3}
%{_bindir}/pykmip-server
%endif
%{python2_sitelib}/kmip
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{sname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pykmip-server
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.0-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-10
- Rebuilt for Python 3.10

* Sat Mar 06 2021 Alan Pevec <apevec AT gmail.com> 0.8.0-9
- Drop bogus enum34 requirement
  Resolves: rhbz#1924317 - F34FailsToInstall: python3-pykmip

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Yatin Karel <ykarel@redhat.com> - 0.8.0-1
- Bump to 0.8.0 and Enable python2 build for CentOS <=7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Jan Beran <jberan@redhat.com> 0.5.0-3
- Fix of python3-pykmip requiring both Python 2 and Python 3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Haikel Guemar <hguemar@fedoraproject.org> 0.5.0-1
- Update to 0.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5
- Remove python3-enum34 as enum is now part of stdlib in python3

* Wed Sep 30 2015 chandankumar <chkumar246@gmail.com> - 0.4.0-1
- Initial package.
