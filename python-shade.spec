
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global srcname shade

%global common_desc shade is a simple client library for operating OpenStack clouds.

Name:           python-%{srcname}
Version:        1.33.0
Release:        15%{?dist}
Summary:        Python module for operating OpenStack clouds

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/shade
Source0:        https://tarballs.openstack.org/shade/shade-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python3-pbr
BuildRequires:  python3-devel

# test-requirements.txt
BuildRequires: python3-mock
BuildRequires: python3-betamax

# requirements.txt
BuildRequires:  python3-six
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-munch
BuildRequires:  python3-os-client-config
BuildRequires:  python3-requestsexceptions
BuildRequires:  python3-jmespath
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-decorator
BuildRequires:  python3-netifaces
BuildRequires:  python3-dogpile-cache
BuildRequires:  python3-requests-mock

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-jmespath                 >= 0.9.0
Requires:       python3-keystoneauth1            >= 3.3.0
Requires:       python3-munch                    >= 2.1.0
Requires:       python3-os-client-config         >= 1.28.0
Requires:       python3-openstacksdk             >= 0.15.0
Requires:       python3-pbr                      >= 2.0.0
Requires:       python3-requestsexceptions       >= 1.2.0
Requires:       python3-six                      >= 1.10.0
Requires:       python3-dogpile-cache            >= 0.6.2
Requires:       python3-decorator                >= 3.4.0
Requires:       python3-netifaces                >= 0.10.4

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -n %{srcname}-%{upstream_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
#PYTHON=%{__python3} %{__python3} setup.py testr

%install
%pyproject_install
mv $RPM_BUILD_ROOT%{_bindir}/shade-inventory \
        $RPM_BUILD_ROOT%{_bindir}/shade-inventory-3
ln -s shade-inventory-3 \
        $RPM_BUILD_ROOT%{_bindir}/shade-inventory

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitelib}/shade*

%{_bindir}/shade-inventory-3
%{_bindir}/shade-inventory

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.33.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Python Maint <python-maint@redhat.com> - 1.33.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Python Maint <python-maint@redhat.com> - 1.33.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.33.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 1.33.0-1
- Update to upstream version 1.33.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.32.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.32.0-1
- Update to upstream version 1.32.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.31.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.31.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 1.31.0-1
- Update to 1.31.0

