%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif
%global pypi_name murano-pkg-check
%global library muranopkgcheck

%global with_docs 0

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        35%{?dist}
Summary:        Murano package validator tool

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://docs.openstack.org/developer/murano/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Use-unittest.mock-instead-of-third-party-mock.patch
Patch0002:      0002-Fix-py38-ut.patch
Patch0003:      0003-Drop-lower-constraints.txt-and-its-testing.patch
BuildArch:      noarch

BuildRequires:  git

%description
Murano package validator tool


%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Murano package validator tool
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-coverage
BuildRequires:  python2-subunit
BuildRequires:  python2-sphinx
BuildRequires:  python2-oslotest
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-reno
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
# Required for tests
BuildRequires:  python2-semantic_version
BuildRequires:  python2-oslo-i18n
BuildRequires:  python2-yaql
BuildRequires:  python2-stevedore
Requires:       python2-pbr >= 1.6
Requires:       python2-pyyaml >= 3.10
Requires:       python2-yaql >= 1.1.0
Requires:       python2-six >= 1.9.0
Requires:       python2-stevedore >= 1.16.0
Requires:       python2-semantic_version >= 2.3.1
Requires:       python2-oslo-i18n >= 2.1.0
Requires:       python2-setuptools

%description -n python2-%{pypi_name}
%{description}
%endif


%if 0%{?with_docs}
%package -n python-%{pypi_name}-doc
Summary:        murano-pkg-check documentation
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery) = 3.1.0
Provides:       bundled(js-searchtools)
Provides:       bundled(js-underscore) = 1.3.1
Provides:       bundled(js-websupport)

%description -n python-%{pypi_name}-doc
Documentation for murano-pkg-check
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        Murano package validator tool
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-coverage
BuildRequires:  python3-subunit
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-reno
# Required for tests
BuildRequires:  python3-semantic_version
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-yaql
BuildRequires:  python3-stevedore
Requires:       python3-pbr >= 1.6
Requires:       python3-PyYAML >= 3.10
Requires:       python3-yaql >= 1.1.0
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore >= 1.16.0
Requires:       python3-semantic_version >= 2.3.1
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
%{description}
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Let's handle requirements from the RPM side
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%generate_buildrequires
%pyproject_buildrequires

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%pyproject_wheel
%endif

%if 0%{?with_docs}
%if %{with python3}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# generate man page
sphinx-build-3 -b man doc/source doc/build/man
%else
# generate html docs
sphinx-build -b html doc/source doc/build/html
# generate man page
sphinx-build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
%endif
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if %{with python3}
%pyproject_install
mv %{buildroot}/%{_bindir}/murano-pkg-check %{buildroot}/%{_bindir}/murano-pkg-check-3
ln -s ./murano-pkg-check-3 %{buildroot}%{_bindir}/murano-pkg-check
%endif

%if %{with python2}
%py2_install
mv %{buildroot}/%{_bindir}/murano-pkg-check %{buildroot}/%{_bindir}/murano-pkg-check-2
ln -s ./murano-pkg-check-2 %{buildroot}%{_bindir}/murano-pkg-check
%endif

%if 0%{?with_docs}
install -p -D -m 644 doc/build/man/murano-pkg-check.1 %{buildroot}%{_mandir}/man1/murano-pkg-check.1
%endif

%check
%if %{with python2}
PYTHON=python2 %{__python2} setup.py test
%endif
%if %{with python3}
rm -rf .testrepository
PYTHON=python3 %{__python3} setup.py test
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/murano-pkg-check
%{_bindir}/murano-pkg-check-2
%{_mandir}/man1/murano-pkg-check.1.gz
%{python2_sitelib}/%{library}
%exclude %{python2_sitelib}/%{library}/tests
%{python2_sitelib}/murano_pkg_check-*.egg-info
%endif

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/murano-pkg-check-3
%{_bindir}/murano-pkg-check
%if 0%{?with_docs}
%{_mandir}/man1/murano-pkg-check.1.gz
%endif
%{python3_sitelib}/%{library}
%exclude %{python3_sitelib}/%{library}/tests
%{python3_sitelib}/murano_pkg_check-*.dist-info
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-35
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.3.0-33
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Joel Capitao <jcapitao@redhat.com> - 0.3.0-30
- Remove oslo-sphinx as BR

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.3.0-28
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Joel Capitao <jcapitao@redhat.com> - 0.3.0-25
- Apply upstream patches in order to be able to rebuild on Python 3.11

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.3.0-24
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-21
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Javier Peña <jpena@redhat.com> - 0.3.0-18
- Remove python-hacking BR, it is not actually needed for unit tests (bz#1841741)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-14
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Alfredo Moralejo <amoralej@redhat.com> - 0.3.0-13
- Remove docs building as it does not support recent sphinx

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Javier Peña <jpena@redhat.com> - 0.3.0-10
- Remove the python2 package for Fedora 30+ (bz#1666190)

* Tue Aug 07 2018 Javier Peña <jpena@redhat.com> - 0.3.0-9
- Fixed rawhide build (bz#1605782)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Mar 15 2018 Javier Peña <jpena@redhat.com> - 0.3.0-5
- Fix man page build (bz#1556215)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Javier Peña <jpena@redhat.com> - 0.3.0-2
- Updated PyYAML version dependency

* Mon Feb 13 2017 Javier Peña <jpena@redhat.com> - 0.3.0-1
- Updated to upstream 0.3.0
- Fixed License tag
- Added manpage for murano-pkg-check-3

* Mon Nov 14 2016 jpena <jpena@redhat.com> - 0.2.0-1
- Initial package.
