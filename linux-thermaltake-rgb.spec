# Many modules not packaged. Some of them deprecated.
%bcond_with tests

%global pypi_name linux_thermaltake_rgb
%global sys_name linux_thermaltake_riing

Name: linux-thermaltake-rgb
Version: 0.2.0
Release: %autorelease
Summary: Python driver and daemon to control thermaltake Riing fans and pumps
BuildArch: noarch

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/chestm007/linux_thermaltake_riing

# GitHub source because pypi version outdated
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros

%if %{with tests}
# BuildRequires: python3dist(base_test_object)
# BuildRequires: python3dist(pep8)
# BuildRequires: python3dist(usb)
BuildRequires: python3dist(pytest)
%endif

%description
Linux driver and daemon for Thermaltake Riing

Currently supported devices are (as they show up in thermaltakes TTRGBPLUS
software:

- Flow Riing RGB
- Lumi Plus LED Strip
- Pacific PR22-D5 Plus
- Pacific Rad Plus LED Panel
- Pacific V-GTX 1080Ti Plus GPU Waterblock
- Pacific W4 Plus CPU Waterblock
- Riing Plus


%prep
%autosetup -n %{sys_name}-%{version} -p1
sed -i 's/PROJECTVERSION/%{version}/g' setup.py
# Fixed missing 1 positional argument in daemon/config.py
#
# For newer versions of python yaml, Simply loading the config with
# yaml.load(cfg) does not work due to it being deprecated, It has been fixed
# here.
# https://github.com/chestm007/linux_thermaltake_riing/pull/53
sed -i 's/yaml.load(cfg)/yaml.load(cfg, Loader=yaml.FullLoader)/' \
    %{pypi_name}/daemon/config.py

# fix wrong package requirement for GObject
# https://github.com/chestm007/linux_thermaltake_riing/pull/37
sed -i 's/GObject/PyGObject/g' setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_datadir}/%{pypi_name}/%{name}.service \
    %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sysconfdir}/%{pypi_name}
mv %{buildroot}%{_datadir}/%{pypi_name}/config.yml \
    %{buildroot}%{_sysconfdir}/%{pypi_name}


%if %{with tests}
%check
%pyproject_check_import

%{python3} -m pytest -v
%endif


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files -f %{pyproject_files}
%doc README.md roadmap.txt protocol.txt
%config(noreplace) %{_sysconfdir}/%{pypi_name}/config.yml
%dir %{_sysconfdir}/%{pypi_name}
%{_bindir}/%{name}
%{_unitdir}/*.service


%changelog
%autochangelog
