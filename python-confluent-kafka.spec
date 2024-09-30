%global pypi_name confluent-kafka

Name:           python-%{pypi_name}
Version:        1.6.1
Release:        9%{?dist}
Summary:        Confluent's Apache Kafka client for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/confluentinc/confluent-kafka-python
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

%description
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  librdkafka-devel
BuildRequires:  python3-devel
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# https://github.com/confluentinc/confluent-kafka-python/issues/508
#BuildRequires:  python3dist(pytest)

Requires:       python3-fastavro
Requires:       python3-requests
Requires:       librdkafka >= 1.6.1
%description -n python3-%{pypi_name}
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files confluent_kafka
# Remove license file installed in weird place
rm -f  %{buildroot}/%{_prefix}/LICENSE.txt

%check
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# So just import test
%py3_check_import confluent_kafka
#py.test-3 -v --ignore=tests/integration ./tests/

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Javier Peña <jpena@redhat.com> - 1.6.1-1
- Updated to version 1.6.1
- Removed Python 2 subpackage

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.11.6-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.11.6-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.6-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.6-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.6-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Javier Peña <jpena@redhat.com> - 0.11.16-3
- Fix python2-futures requirement
- Fix python2-enum34 for CentOS 7

* Fri Jan 11 2019 Javier Peña <jpena@redhat.com> - 0.11.16-2
- Fixed ambiguous shebangs
- Corrected description lines to avoid rpmlint errors

* Wed Dec 12 2018 Javier Peña <jpena@redhat.com> - 0.11.6-1
- Initial package.
