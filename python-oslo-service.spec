%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name oslo.service
%global pkg_name oslo-service
%global with_doc 1

%global common_desc \
oslo.service provides a framework for defining new long-running services \
using the patterns established by other OpenStack applications.

Name:           python-%{pkg_name}
Version:        3.3.0
Release:        3%{?dist}
Summary:        Oslo service library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://opendev.org/openstack/oslo.service
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%package -n     python3-%{pkg_name}
Summary:        Oslo service library
%py_provides python3-%{pkg_name}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  git-core
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-eventlet
# Required for documentation build
BuildRequires:  python3-oslo-config
# Required for tests
BuildRequires:  procps-ng
BuildRequires:  python3-fixtures
BuildRequires:  python3-hacking
BuildRequires:  python3-requests
BuildRequires:  python3-routes
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-concurrency
BuildRequires:  python3-yappi
BuildRequires:  python3-webob
BuildRequires:  python3-paste
BuildRequires:  python3-paste-deploy
BuildRequires:  python3-tox

Requires:       python3-eventlet >= 0.25.2
Requires:       python3-greenlet
Requires:       python3-oslo-config >= 2:5.1.0
Requires:       python3-oslo-concurrency >= 3.25.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-utils >= 3.40.2
Requires:       python3-routes
Requires:       python3-yappi
Requires:       python3-debtcollector
Requires:       python3-webob
Requires:       python3-paste
Requires:       python3-paste-deploy >= 1.5.0


%description -n python3-%{pkg_name}
%{common_desc}

%package -n python3-%{pkg_name}-tests
Summary:        Oslo service tests
%py_provides python3-%{pkg_name}

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  procps-ng
Requires:  python3-fixtures
Requires:  python3-hacking
Requires:  python3-requests
Requires:  python3-routes
Requires:  python3-oslotest

%description -n python3-%{pkg_name}-tests
Tests for oslo.service

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:        Oslo service documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pkg_name}-doc
Documentation for oslo.service
%endif

%description
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -p0 -n %{pypi_name}-%{upstream_version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%if 0%{?with_doc}
# generate html docs
PYTHONPATH=. sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%{pyproject_install}

%check
# FIXME: https://review.openstack.org/279011 seems to break tests in CentOS7,
# creating an infinite loop
tox -e py3||
rm -rf .testrepository

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_service
%{python3_sitelib}/oslo_service-*.dist-info
%exclude %{python3_sitelib}/oslo_service/tests

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_service/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 20 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.3.0-1
- Update 3.3.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 24 2023 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.1.1-1
- Update to 3.1.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 03 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.0.0-6
- Applies a patch for tests and uses tox for tests
- Fixes issues on the packaging guidelines

* Wed Nov 16 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.0.0-5
- Fixes issues on the packaging guidelines

* Wed Nov 09 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.0.0-4
- Fixes issues on the packaging guidelines

* Tue Nov 08 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.0.0-3
- Fixes issues on the packaging guidelines

* Tue Nov 01 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.0.0-2
- Fixes issues on the packaging guidelines

* Wed Oct 26 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 3.0.0-1
- Update to 3.0.0

* Mon Sep 27 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.6.0-2
- Fixes issues on packaging guidelines

* Sat Aug 07 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> 2.6.0-1
- Un-retired and update to 2.6.0

* Tue Feb 26 2019 Alfredo Moralejo <amoralej@redhat.com> 1.29.0-3
- Drop eventlet capping

* Thu Jan 31 2019 Yatin Karel <ykarel@redhat.com> - 1.29.0-2
- Drop python2 sub packages (#1632343)

* Mon Jul 23 2018 Matthias Runge <mrunge@redhat.com> - 1.29.0-1
- update to Queens

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.19.0-6
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.19.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.19.0-2
- Fix python tests subpackages

* Wed Feb 08 2017 Alfredo Moralejo <amoralej@redhat.com> 1.19.0-1
- Update to 1.19.0
