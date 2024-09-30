%global module_name abimap

Name:           python-%{module_name}
Version:        0.3.2
Release:        21%{?dist}
License:        MIT
Summary:        A helper for library maintainers to use symbol versioning
Url:            https://github.com/ansasaki/abimap

Source:         https://files.pythonhosted.org/packages/source/a/%{module_name}/%{module_name}-%{version}.tar.gz

# This patch disables the test which depends on pytest-console-scripts
Patch0:         python-abimap-0.3.0-disable-script-test.patch
# This patch removes sphinx napoleon extension
Patch1:         python-abimap-0.3.1-remove-docs-napoleon.patch
# This patch removes sphinx rtd theme
Patch2:         python-abimap-0.3.1-remove-docs-rtd-theme.patch
# Use natural sorting to sort releases
Patch3:         python-abimap-0.3.2-use-natural-sort.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  python%{python3_pkgversion}-devel
# Required for testing
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-runner
BuildRequires:  python%{python3_pkgversion}-pytest-cov
# Not available yet, will be required once it is available in Fedora
# BuildRequires:  %%{py3_dist pytest-console-scripts}

%if 0%{?el7}
BuildRequires:  python%{python3_pkgversion}-yaml
# Required for documentation
BuildRequires:  python-sphinx
%else
BuildRequires:  python%{python3_pkgversion}-pyyaml
# Required for documentation
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

Requires:       setuptools

%description
This script allows to generate and update symbol version linker scripts which
adds version information to the exported symbols. The script is intended to be
integrated as part of a shared library build to check for changes in the set
of exported symbols and update the symbol version linker script accordingly.

%package -n python%{python3_pkgversion}-%{module_name}
Summary:        A helper for library maintainers to use symbol versioning

%description -n python%{python3_pkgversion}-%{module_name}
This script allows to generate and update symbol version linker scripts which
adds version information to the exported symbols. The script is intended to be
integrated as part of a shared library build to check for changes in the set
of exported symbols and update the symbol version linker script accordingly.

%package -n python-%{module_name}-doc
Summary:        Documentation for python-%{module_name}
%description -n python-%{module_name}-doc
Documentation for python-%{module_name}

%prep
%autosetup -n %{module_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if 0%{?el7}
# Generate html docs
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build -E -b html docs html
# Generate manpage
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build -E -b man docs man
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%else
# Generate html docs
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build-3 -E -b html docs html
# Generate manpage
PYTHONPATH=${PWD}/src:${PWD}/tests \
    sphinx-build-3 -E -b man docs man
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files abimap
# Install man page
mkdir -p %{buildroot}%{_mandir}/man1
install ${PWD}/man/abimap.1 %{buildroot}%{_mandir}/man1/abimap.1

%check
# Generate test data (copied bootstrap-tests from Makefile)
make -C tests ABIMAP_NAME_VERSION="abimap-%{version}" ABIMAP_VERSION="%{version}"
# Run the tests using py.test
PYTHONPATH=%{buildroot}%{python3_sitelib}:$PWD/tests \
    py.test-%{python3_version} -vv tests

%files -n python%{python3_pkgversion}-%{module_name} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{_bindir}/abimap
%{_mandir}/man1/abimap.1*

%files -n python-%{module_name}-doc
%license LICENSE
%doc html

%changelog
* Mon Sep 23 2024 Anderson Toshiyuki Sasaki <ansasaki@redhat.com> - 0.3.2-21
- Use natural sorting to sort releases

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.2-19
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Anderson Toshiyuki Sasaki <ansasaki> - 0.3.2-15
- Migrated to SPDX license

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.3.2-14
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.2-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.2-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.8

* Mon Aug 05 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.3.2-1
- Update to upstream version 0.3.2
- Fixed broken builds due to changes in warning output
- Changed tests to check error messages
- Added python 3.7 to testing matrix
- Added requirement to verify SNI when checking URLs in docs

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.1-2
- Make the specfile compatible with EPEL7
- Fixed incompatible macros
- Fixed patch to skip a test in older pytest versions
- Added patches to remove sphinx extensions not available in EPEL7

* Mon Aug 20 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.1-1
- Rebased to version 0.3.1
- argparse-manpage is no longer required since manpage is generated by sphinx

* Wed Aug 08 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.0-2
- Added Requires for setuptools
- Addressed a bug in the order of releases in output map

* Mon Aug 06 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.3.0-1
- Initial package.
