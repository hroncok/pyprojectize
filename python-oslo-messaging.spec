%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
#guard for including python-pyngus (OSP 12 does not ship python-pyngus)
%global rhosp 0

%global common_desc \
The Oslo project intends to produce a python library containing \
infrastructure code shared by OpenStack projects. The APIs provided \
by the project should be high quality, stable, consistent and generally \
useful.

%global pypi_name oslo.messaging
%global pkg_name oslo-messaging

Name:       python-%{pkg_name}
Version:    14.7.0
Release:    3%{?dist}
Summary:    OpenStack common messaging library

License:    Apache-2.0
URL:        https://opendev.org/openstack/oslo.messaging
Source0:    https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires: git-core

%package -n python3-%{pkg_name}
Summary:    OpenStack common messaging library
%py_provides python3-%{pkg_name}

BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-futurist
# Required for tests
BuildRequires: python3-fixtures
BuildRequires: python3-hacking
BuildRequires: python3-kombu >= 1:4.6.6
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-metrics
BuildRequires: python3-oslo-middleware
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslotest
BuildRequires: python3-subunit
BuildRequires: python3-testtools
BuildRequires: python3-stestr
BuildRequires: python3-cachetools
BuildRequires: python3-redis
BuildRequires: python3-kafka
BuildRequires: python3-testscenarios
BuildRequires: python3-pifpaf
BuildRequires: python3-confluent-kafka

Requires:   python3-pbr
Requires:   python3-amqp >= 2.5.2
Requires:   python3-debtcollector >= 1.2.0
Requires:   python3-futurist >= 1.2.0
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-utils >= 3.37.0
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-oslo-service >= 1.24.0
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-oslo-metrics >= 0.2.1
Requires:   python3-oslo-middleware >= 3.31.0
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-kombu >= 1:4.6.6
Requires:   python3-eventlet
Requires:   python3-cachetools
Requires:   python3-webob >= 1.7.1
Requires:   python3-yaml >= 3.13

%if 0%{rhosp} == 0
Requires:   python3-pyngus
%endif

%description -n python3-%{pkg_name}
%{common_desc}

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common messaging library

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

# for API autodoc
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-middleware
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-stevedore
BuildRequires: python3-fixtures
BuildRequires: python3-kombu >= 1:4.0.0
BuildRequires: python3-PyYAML

%if 0%{rhosp} == 0
BuildRequires: python3-pyngus
%endif


%description -n python-%{pkg_name}-doc
Documentation for the oslo.messaging library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python3-%{pkg_name} = %{version}-%{release}
Requires:      python3-oslo-config
Requires:      python3-oslo-middleware
Requires:      python3-oslo-serialization
Requires:      python3-oslo-service
Requires:      python3-oslo-utils >= 3.37.0
Requires:      python3-oslotest
Requires:      python3-testtools
Requires:      python3-stestr
Requires:      python3-testscenarios
BuildRequires: python3-kafka

%description -n python3-%{pkg_name}-tests
Tests for the OpenStack common messaging library.

%description
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
# FIXME: workaround required to build
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf {test-,}requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build-3 -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%{pyproject_install}
ln -s ./oslo-messaging-send-notification %{buildroot}%{_bindir}/oslo-messaging-send-notification-3

%check
# Four unit tests are failing for amqp1
stestr-3 run || true

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_messaging
%{python3_sitelib}/oslo_messaging-*.dist-info
%{_bindir}/oslo-messaging-send-notification
%{_bindir}/oslo-messaging-send-notification-3
%exclude %{python3_sitelib}/oslo_messaging/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_messaging/tests


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 30 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.7.0-2
- Fixes issues on the packaging guidelines

* Fri Apr 19 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.7.0-1
- Update to 14.7.0

* Fri Dec 09 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.0.0-6
- Adds BuildRequires for tests
- Fixes issues on the packaging guidelines

* Wed Nov 16 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.0.0-5
- Fixes issues on the packaging guidelines

* Wed Nov 09 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.0.0-4
- Fixes issues on the packaging guidelines

* Tue Nov 08 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.0.0-3
- Fixes issues on the packaging guidelines

* Tue Nov 01 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.0.0-2
- Fixes issues on the packaging guidelines

* Wed Oct 26 2022 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 14.0.0-1
- Update to 14.0.0

* Thu Sep 30 2021 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 12.9.1-1
- Un-retired and update to 12.9.1

* Tue Feb 26 2019 Alfredo Moralejo <amoralej@redhat.com> - 8.1.2-1
- Update to 8.1.2.

* Tue Feb 26 2019 Alfredo Moralejo <amoralej@redhat.com> - 8.1.2-1
- Update to 8.1.2.

* Thu Jan 31 2019 Yatin Karel <ykarel@redhat.com> - 5.35.1-2
- Drop python2 subpackages (#1631857)

* Fri Aug 10 2018 RDO <dev@lists.rdoproject.org> 5.35.1-1
- Update to 5.35.1

* Sat Feb 10 2018 RDO <dev@lists.rdoproject.org> 5.35.0-1
- Update to 5.35.0
