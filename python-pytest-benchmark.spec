%global srcname pytest-benchmark

Name: python-%{srcname}
Version: 4.0.0
Release: 9%{?dist}
Summary: A py.test fixture for benchmarking code
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://pytest-benchmark.readthedocs.io
Source: https://github.com/ionelmc/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
# Tests
#BuildRequires: python3-cpuinfo
#BuildRequires: python3-pytest
#BuildRequires: python3-elasticsearch
#BuildRequires: python3-freezegun
#BuildRequires: python3-pytest-xdist
#BuildRequires: python3-pygal

%global _description\
This plugin provides a benchmark fixture. This fixture is a callable object\
that will benchmark any function passed to it.\
\
Notable features and goals:\
\
  - Sensible defaults and automatic calibration for microbenchmarks\
  - Good integration with pytest\
  - Comparison and regression tracking\
  - Exhausive statistics\
  - JSON export

%description %_description

%package -n python3-%{srcname}
Summary: %summary
%py_provides python3-%{srcname}
Requires: python3-pytest
Requires: python3-cpuinfo

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_benchmark

%check
# Tests disabled (missing dependency: aspectlib)
#%%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst AUTHORS.rst
%license LICENSE
%{_bindir}/py.test-benchmark
%{_bindir}/pytest-benchmark

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.0-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Juan Orti Alcaine <jortialc@redhat.com> - 4.0.0-1
- Version 4.0.0 (#2137873)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.4.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 3.4.1-2
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Juan Orti Alcaine <jortialc@redhat.com> - 3.4.1-1
- Version 3.4.1
- Disable tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 3.2.3-4
- BR: python3-setuptools

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.3-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 3.2.3-1
- Version 3.2.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-1
- Update to 3.2.2 for pytest 4 compatibility

* Sun Mar 03 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.1-8
- Subpackage python2-pytest-benchmark has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
- Fix FTBFS caused by removal of python2-cpuinfo (#1675780)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 3.1.1-3
- Reduce summary lenght

* Wed Aug 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 3.1.1-2
- Update BR

* Wed Aug 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 3.1.1-1
- Initial RPM release
