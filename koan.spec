%global commit 4194967f02db8e9f85e8bab6f3803029a4d9a243
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           koan
Version:        3.0.1
Release:        13%{?dist}
Summary:        Kickstart over a network

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/cobbler/koan
Source0:        https://github.com/cobbler/koan/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python%{python3_pkgversion}-koan = %{version}-%{release}

%description
Koan stands for kickstart-over-a-network and allows for both network
installation of new virtualized guests and reinstallation of an existing
system. For use with a boot-server configured with Cobbler.


%package -n python%{python3_pkgversion}-koan
Summary:        koan python%{python3_pkgversion} module
BuildRequires:  python%{python3_pkgversion}-devel
%{?python_enable_dependency_generator}
%if 0%{?el7}
Requires:       python%{python3_pkgversion}-distro
Requires:       python%{python3_pkgversion}-libvirt
Requires:       python%{python3_pkgversion}-netifaces
Requires:       python%{python3_pkgversion}-simplejson
%endif
Requires:       virt-install

%description -n python%{python3_pkgversion}-koan
koan python%{python3_pkgversion} module.


%prep
%autosetup -p1
%py3_shebang_fix bin

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files koan

%files
%license COPYING
%doc README.md
%{_bindir}/koan
%{_bindir}/cobbler-register

%files -n python%{python3_pkgversion}-koan -f %{pyproject_files}
%license COPYING

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.1-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.1-11
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.1-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.1-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Orion Poplawski <orion@nwra.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-0.15.20200917git4194967
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.9.0-0.14.20200917git4194967
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-0.13.20200917git4194967
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Orion Poplawski <orion@nwra.com> - 2.9.0-0.12.202009017git4194967
- Update to latest git

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-0.11.20200412gitc67b526
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-0.10.20200412gitc67b526
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Orion Poplawski <orion@nwra.com> - 2.9.0-0.9.202004012gitc67b526
- Update to latest git

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-0.8.20191125gitcff96a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.7.20191125gitcff96a0
- Add requirement on netifaces

* Mon Nov 25 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.6.20191125gitcff96a0
- Update to latest git

* Fri Nov 15 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.5.20191115git18df5d4
- Update to latest git
- Use automatic python dependencies
- Use proper snapshot release tag

* Thu Nov  7 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.4.git
- Update to latest git

* Fri Oct 18 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.3.git
- Add patch to support cobbler 2 servers
- Add patch to fix quoting with grubby on EL8

* Fri Oct 11 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.2.git
- Split out again from cobbler
