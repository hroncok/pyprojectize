%global pypi_name textfsm

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        5%{?dist}
Summary:        Python module for parsing semi-structured text into python tables

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/google/textfsm
Source0:        https://github.com/google/textfsm/archive/v%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2291946
# with apologies to the Sex Pistols, drop 'future' dep from setup.py
# because it's never used
# not upstreamed because upstream has a *much* larger fix pending for
# 2.0.0: https://github.com/google/textfsm/pull/121
Patch:          textfsm-1.1.3-no-future.patch
BuildArch:      noarch

%description
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
Requires:       python3-six

%description -n python3-%{pypi_name}
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Fix version in __init__.py, this was fixed in the repo in
# https://github.com/google/textfsm/commit/ca3755dcb8b1b043857d63f1d1352d62030f0d2d
 # (post-1.1.3 release)
sed -i 's/1.1.2/1.1.3/' textfsm/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pypi_name}
%license COPYING
%exclude %{python3_sitelib}/testdata
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{_bindir}/textfsm

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Adam Williamson <awilliam@redhat.com> - 1.1.3-3
- Patch 'future' dep out of setup.py so we don't get an auto-require (#2291946)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.13

* Mon Apr 22 2024 Javier Peña <jpena@redhat.com> - 1.1.3-1
- Update to upstream version 1.1.3 (#1697095)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Joel Capitao <jcapitao@redhat.com> - 1.1.2-5
- Remove future dependency and use %pytest

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Joel Capitao <jcapitao@redhat.com> - 1.1.2-1
- Update to upstream version 1.1.2 (#1697095)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.10

* Mon Feb 22 2021 Javier Peña <jpena@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0 (#1931302)
- Remove python2 subpackage
- Enable unit tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Javier Peña <jpena@redhat.com> - 0.3.2-6
- Switch sources to use GitHub release
- Disable unit tests until they are present in the tarball

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Javier Peña <jpena@redhat.com> - 0.3.2-4
- Removed Python 2 package from Fedora 30+ (bz#1634614)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Javier Peña <jpena@redhat.com> - 0.3.2-1
- Initial package.
