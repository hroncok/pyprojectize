# Created by pyp2rpm-3.3.2
%global pypi_name collectd-puppet
%global module_name collectd_puppet

Name:           python-%{module_name}
Version:        2.0.0
Release:        22%{?dist}
Summary:        Collectd plugin to monitor puppet agents

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/cernops/collectd-puppet
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{module_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       collectd-python

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros


%description
Collectd plugin for puppet run status.

%package -n     python3-%{module_name}
Summary:        %{summary}

Requires:       python3dist(pyyaml)
%description -n python3-%{module_name}
Collectd plugin for puppet run status.

%prep
%autosetup -n %{module_name}-%{version}
# Remove bundled egg_info
rm -r src/%{module_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%postun
%systemd_postun_with_restart collectd.service

%files -n python3-%{module_name}
%license LICENSE
%doc README.rst NEWS.rst
%{_datadir}/collectd/puppet_types.db
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/%{module_name}-%{version}.dist-info

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-20
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.0-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.9

* Fri Feb 14 2020 Steve Traylen <steve.traylen@cern.ch> - 2.0.0-7
- condrestart collectd on upgrade

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Steve Traylen <steve.traylen@cern.ch> - 2.0.0-1
- Update to 2.0.0

* Wed Feb 06 2019 Steve Traylen <steve.traylen@cern.ch> - 1.5.1-1
- Initial package.
