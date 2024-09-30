%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global pypi_name oslo.metrics
%global pkg_name oslo-metrics
%global common_desc \
The OpenStack Oslo Metrics library. \
Oslo metrics API supports collecting metrics data from other Oslo \
libraries and exposing the metrics data to monitoring system.

Name:           python-oslo-metrics
Version:        0.8.0
Release:        %autorelease
Summary:        OpenStack Oslo Metrics library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://opendev.org/openstack/oslo.metrics
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:      https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:      https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Metrics library
%py_provides python3-%{pkg_name}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-pbr
BuildRequires:  python3-prometheus_client
# Required for testing
BuildRequires:  python3-oslotest

Requires:       python3-oslo-config >= 2:6.9.0
Requires:       python3-oslo-log >= 3.44.0
Requires:       python3-oslo-utils >= 3.41.0
Requires:       python3-prometheus_client >= 0.6.0
Requires:       python3-pbr >= 3.1.1

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Metrics library
Group:      Documentation

BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-%{pkg_name}-doc
Documentation for the Oslo Metrics library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Metrics library

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-oslotest

%description -n python3-%{pkg_name}-tests
Tests for the Oslo Metrics library.


%description
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the dependencies
rm -rf {test-,}requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyproject_install}

%check
%{__python3} setup.py test

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_metrics
%{python3_sitelib}/oslo_metrics-*.dist-info
%{_bindir}/oslo-metrics
%exclude %{python3_sitelib}/oslo_metrics/tests/

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_metrics/tests/

%changelog
%autochangelog
