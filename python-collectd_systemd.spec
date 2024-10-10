%global pypi_name collectd_systemd

%global commit 212cb7918fa6925213082d11a0fe0fb44fe84852
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20181018git%{shortcommit}

Name:           python-%{pypi_name}
Version:        0.0.1
Release:        0.32.%{snapinfo}%{?dist}
Summary:        Collectd plugin to monitor systemd services

License:        MIT
URL:            https://github.com/mbachry/collectd-systemd/
Source0:        https://github.com/mbachry/collectd-systemd/archive/%{commit}/collectd-system-%{shortcommit}.tar.gz
Source1:        collectd_systemd.te
# https://github.com/mbachry/collectd-systemd/pull/12
Patch0:         oneshot-dead.patch
# https://github.com/mbachry/collectd-systemd/pull/13
Patch1:         state-start.patch
# https://github.com/mbachry/collectd-systemd/pull/14
Patch2:         getunit_loadunit.patch
BuildArch:      noarch
 
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(mock)

BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros

%description
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.
%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3-dbus
Requires:       collectd-python
Requires:       %{name}-selinux = %{version}-%{release}

%description -n python3-%{pypi_name}
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.

%package selinux
Summary:        selinux policy for collectd systemd plugin
Requires:       selinux-policy
Requires:       policycoreutils

%description selinux
This package contains selinux rules to allow the collectd
systemd plugin to access service status via dbus.

%prep
%autosetup -n collectd-systemd-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
make -f /usr/share/selinux/devel/Makefile collectd_systemd.pp

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 644 -p collectd_systemd.pp \
    %{buildroot}%{_datadir}/selinux/packages/%{name}/collectd_systemd.pp

%post selinux
/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/collectd_systemd.pp >/dev/null 2>&1 || :

%postun selinux
if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r collectd_systemd >/dev/null 2>&1 || :
fi
%systemd_postun_with_restart collectd.service


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files selinux
%{_datadir}/selinux/packages/%{name}/collectd_systemd.pp

%check
PYTHONPATH=. pytest-3

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.32.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.1-0.31.20181018git212cb79
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.30.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.29.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.28.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.0.1-0.27.20181018git212cb79
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.26.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.25.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.0.1-0.24.20181018git212cb79
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.23.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.22.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.1-0.21.20181018git212cb79
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.20.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.19.20181018git212cb79
- Backport bug fix for start state of services.
- Backport bug fix for acceptable dead oneshot services.
- Backport bug fix for LoadUnit rather than GetUnit

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.18.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.17.20181018git212cb79
- Rebuilt for Python 3.9

* Fri Feb 14 2020 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.16.20181018git212cb79
- condrestart collectd on upgrade in particular

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.15.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.14.20181018git212cb79
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.13.20181018git212cb79
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.12.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.11.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.10.20181018git212cb79
- Subpackage python2-collectd_systemd has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 18 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.9.20181018git212cb79
- New HEAD from upstream.

* Tue Sep 18 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.8.20180604gitbe9c647
- Policy file updated for init.d services.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.7.20180604gitbe9c647
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.6.20180604gitbe9c647
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.5.20180604gitbe9c647
- New HEAD from upstream.

* Thu May 24 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.4.20180516gita7018ec
- Corect path to selinux module.

* Tue May 22 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.3.20180516gita7018ec
- Add selinux sub package

* Thu May 17 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.2.20180516gita7018ec
- Correct snapshot in string.

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.1.20180516gita7018ec
- Initial package.
