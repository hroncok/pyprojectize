# The check need root privilege hence disabled by default
%bcond_with check

Name:           nispor
Version:        1.2.19
Release:        %autorelease
Summary:        Unified interface for Linux network state querying
License:        Apache-2.0
URL:            https://github.com/nispor/nispor
Source:         https://github.com/nispor/nispor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/nispor/nispor/releases/download/v%{version}/nispor-vendor-%{version}.tar.xz
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  rust-packaging
BuildRequires:  (crate(clap/cargo) >= 4.2.0 with crate(clap/cargo) < 5.0)
BuildRequires:  (crate(clap/default) >= 4.2.0 with crate(clap/default) < 5.0)
BuildRequires:  (crate(env_logger/default) >= 0.10 with crate(env_logger/default) < 0.11)
BuildRequires:  (crate(ethtool/default) >= 0.2.5 with crate(ethtool/default) < 0.3)
BuildRequires:  (crate(futures/default) >= 0.3 with crate(futures/default) < 0.4)
BuildRequires:  (crate(libc/default) >= 0.2.126 with crate(libc/default) < 0.3)
BuildRequires:  (crate(log/default) >= 0.4 with crate(log/default) < 0.5)
BuildRequires:  (crate(mptcp-pm/default) >= 0.1.3 with crate(mptcp-pm/default) < 0.2)
BuildRequires:  (crate(netlink-packet-route/default) >= 0.19.0 with crate(netlink-packet-route/default) < 0.20)
BuildRequires:  (crate(netlink-packet-utils/default) >= 0.5.2 with crate(netlink-packet-utils/default) < 0.6)
BuildRequires:  (crate(netlink-sys/default) >= 0.8.4 with crate(netlink-sys/default) < 0.9)
BuildRequires:  (crate(rtnetlink/default) >= 0.14.1 with crate(rtnetlink/default) < 0.15)
BuildRequires:  (crate(serde/default) >= 1.0 with crate(serde/default) < 2.0)
BuildRequires:  (crate(serde/derive) >= 1.0 with crate(serde/derive) < 2.0)
BuildRequires:  (crate(serde_json/default) >= 1.0 with crate(serde_json/default) < 2.0)
BuildRequires:  (crate(serde_yaml/default) >= 0.9 with crate(serde_yaml/default) < 0.10)
BuildRequires:  (crate(tokio/macros) >= 1.18 with crate(tokio/macros) < 2.0)
BuildRequires:  (crate(tokio/rt) >= 1.18 with crate(tokio/rt) < 2.0)
%endif

%description
Unified interface for Linux network state querying.

%if ! 0%{?rhel}
%package -n     rust-%{name}-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}-devel

This package contains library source intended for building other packages
which use "%{name}" crate.

%package -n     rust-%{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}+default-devel

This package contains library source intended for building other packages
which use "%{name}" crate with default feature.
%endif

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       nispor = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch

%description -n python3-%{name}

This package contains python3 binding of %{name}.

%package        devel
Summary:        %{summary}
Requires:       nispor%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel

This package contains C binding of %{name}.

%prep
%autosetup -n %{name}-%{version_no_tilde} -p1 %{?rhel:-a1}

%if 0%{?rhel}
%cargo_prep -v vendor
%else
%cargo_prep
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?rhel}
%cargo_vendor_manifest
%endif

pushd src/python
%pyproject_wheel
popd

%install
%if ! 0%{?rhel}
# cargo_install has problem on detecting library when running in workspace
# due to bug https://pagure.io/fedora-rust/cargo2rpm/issue/5
# Removing the workspace Cargo.toml will workaround this problem.
rm Cargo.toml
pushd src/lib
%cargo_install
popd
%endif

env SKIP_PYTHON_INSTALL=1 PREFIX=%{_prefix} LIBDIR=%{_libdir} %make_install

pushd src/python
%pyproject_install
%pyproject_save_files -l 'nispor*'
popd

%if %{with check}
%check
%cargo_test
%endif

%files
%doc AUTHORS CHANGELOG DEVEL.md README.md
%license LICENSE
%license LICENSE.dependencies
%if 0%{?rhel}
%license cargo-vendor.txt
%endif
%{_bindir}/npc
%{_libdir}/libnispor.so.*

%files -n       python3-%{name} -f %{pyproject_files}

%files devel
%license LICENSE
%{_libdir}/libnispor.so
%{_includedir}/nispor.h
%{_libdir}/pkgconfig/nispor.pc

%if ! 0%{?rhel}
%files -n       rust-%{name}-devel
%license LICENSE
%{cargo_registry}/%{name}-%{version_no_tilde}/

%files -n       rust-%{name}+default-devel
%ghost %{cargo_registry}/%{name}-%{version_no_tilde}/Cargo.toml
%endif

%changelog
%autochangelog
