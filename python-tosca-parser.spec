%global pypi_name tosca-parser

Name:           python-%{pypi_name}
Version:        2.9.1
Release:        6%{?dist}
Summary:        Parser for TOSCA Simple Profile in YAML

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/openstack/tosca-parser
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The TOSCA Parser is an OpenStack project and licensed under Apache 2.
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.

%package -n python3-%{pypi_name}
Summary:        Parser for TOSCA Simple Profile in YAML

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 1.3
BuildRequires:  python3-PyYAML
# Required for testing
BuildRequires:  python3-six
BuildRequires:  python3-dateutil
BuildRequires:  python3-cliff
BuildRequires:  python3-fixtures
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  python3-testscenarios
BuildRequires:  python3-oslotest
BuildRequires:  python3-subunit
BuildRequires:  python3-stestr
# Required for doc
BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

Requires:       python3-PyYAML
Requires:       python3-cliff
Requires:       python3-dateutil
Requires:       python3-requests
Requires:       python3-stevedore

%description -n python3-%{pypi_name}
The TOSCA Parser is an OpenStack project and licensed under Apache 2.
It is developed to parse TOSCA Simple Profile in YAML. It reads the TOSCA
templates and creates an in-memory graph of TOSCA nodes and their relationship.


%package -n python-%{pypi_name}-doc
Summary:        Parser for TOSCA Simple Profile in YAML - documentation
Provides:  python3-%{pypi_name}-doc = %{version}-%{release}
Obsoletes: python3-%{pypi_name}-doc < %{version}-%{release}

%description -n python-%{pypi_name}-doc
The TOSCA Parser is an OpenStack project and licensed under Apache 2.
This package contains its documentation


%prep
%setup -q -n %{pypi_name}-%{version}
# Let's manage requirements using rpm.
rm -f *requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%check
# Ignore test results for now, they are trying to access external URLs
# which are not accessible in Koji
PYTHON=python3 %{__python3} setup.py test || true
# Cleanup test repository
rm -rf .testrepository

%install
%{pyproject_install}
%pyproject_save_files -l toscaparser

# Set executable permission on test scripts
find %{buildroot}/%{python3_sitelib}/toscaparser/tests -name '*.sh' -execdir chmod +x '{}' \;
# Fix shebang on some test scripts
find %{buildroot}/%{python3_sitelib}/toscaparser/tests -name '*.py' -exec sed -i 's/^#!\/usr\/bin\/python/#!\/usr\/bin\/python3/' {} \;

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/tosca-parser

%files -n python-%{pypi_name}-doc
%doc html README.rst
%license LICENSE

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9.1-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.9.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 07 2023 Joel Capitao <jcapitao@redhat.com> - 2.9.1-1
- Update to 2.9.1 (#2144142)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.7.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Alfredo Moralejo <amoralej@redhat.com> - 2.7.0-1
- Update to 2.7.0
- Removed -3 sufixed binaries as it's only python3 packaged.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Joel Capitao <jcapitao@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Joel Capitao <jcapitao@redhat.com> - 2.1.0-1
- Update to 2.1.0
- Remove python2 subpackage

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Javier Peña <jpena@redhat.com> - 1.4.0-7
- Remove python-hacking requirement, it is not actually needed for the build

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Alfredo Moralejo <amoralej@redhat.xom> - 1.4.0-1
- Update to 1.4.0.
- Remove python2 subpackages in Fedora.
- Make documentation subpackage unversioned

* Tue Sep 11 2018 Javier Peña <jpena@redhat.com> - 1.1.0-1
- Updated to upsteam 1.1.0 (bz#1541379)
- Fix unversioned python shebangs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Javier Peña <jpena@redhat.com> - 0.8.1-1
- Updated to upstream release 0.8.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Javier Peña <jpena@redhat.com> - 0.7.0-1
- Updated to upstream release 0.7.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuild for Python 3.6

* Wed Nov 02 2016 Javier Peña <jpena@redhat.com> - 0.6.0-3
- Fix shebang for certain test scripts in python3 subpackage, so python2 is not included (bz#1390505)
- Invert test execution, so python3 tests are executed
- Use pypi.io for Source0 URL

* Tue Aug 16 2016 Javier Peña <jpena@redhat.com> - 0.6.0-2
- Ignore test results, they're trying to access the Internet

* Tue Aug 16 2016 Javier Peña <jpena@redhat.com> - 0.6.0-1
- Updated to upstream version 0.6.0

* Wed Sep 09 2015 jpena <jpena@redhat.com> - 0.1.0-3
- Fix file permissions for test scripts

* Wed Sep 09 2015 jpena <jpena@redhat.com> - 0.1.0-2
- Created docs subpackages
- Added tests
- Fixes for python3 subpkg

* Tue Sep 08 2015 jpena <jpena@redhat.com> - 0.1.0-1
- Initial package.
