Name:		cinch
Version:	1.4.0
Release:	21%{?dist}
Summary:	A tool for provisioning Jenkins components for CI

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://github.com/RedHatQE/cinch
Source0:	http://github.com/RedHatQE/%{name}/archive/v%{version}.tar.gz

BuildRequires:	ansible
BuildRequires:	python3-plumbum
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Requires:	ansible
Requires:	python3-plumbum

BuildArch:	noarch

%description
Cinch is an Ansible-based tool for configuring Jenkins systems to enhance
the Continuous Integration experience.


%prep
%autosetup -n %{name}-%{version}

find . -name '*.sh' -exec chmod +x '{}' \;
find . -name '*.py' -exec chmod -x '{}' \;

%build
%py3_build


%install
%py3_install

# This is improperly installed by pip
rm -rf %{buildroot}%{python3_sitelib}/tests


%files
%doc README.md
%license LICENSE
%{_bindir}/cinch
%{_bindir}/teardown
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{name}


%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.4.0-19
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.4.0-15
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.4.0-12
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-9
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Greg Hellings <greg.hellings@gmail.com> - 1.4.0-1
- Upstream release 1.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Greg Hellings <greg.hellings@gmail.com> - 1.2.0-1
- New upstream 1.2.0

* Wed Sep 05 2018 Greg Hellings <greg.hellings@gmail.com> - 1.1.0-2
- Fixed up spec file for RPM lint errors

* Tue Aug 28 2018 Greg Hellings <greg.hellings@gmail.com> - 1.1.0-1
- New upstream version 1.1.0
- Fedora Ansible is now Python3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 1.0.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Greg Hellings <greg.hellings@gmail.com> - 1.0.0-1
- New upstream 1.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Greg Hellings <greg.hellings@gmail.com> - 0.9.0-1
- New upstream release 0.9.0
- Intervening versions depended on an unpackaged library, which is now removed
- Added new "teardown" command
- Updated SOURCE0 URL
- Remove tests from install path
- Updated several lines to use the "name" macro

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Greg Hellings <greg.hellings@gmail.com> - 0.2.1-3
- Updated Source0 with name macro substitution

* Mon Dec 12 2016 Greg Hellings <greg.hellings@gmail.com> - 0.2.1-2
- Removed python-devel BR

* Tue Dec 06 2016 Greg Hellings <greg.hellings@gmail.com> - 0.2.1-1
- Upstream release 0.2.1
- Remove setup.py patch

* Wed Nov 09 2016 Greg Hellings <greg.hellings@gmail.com> - 0.2.0-1
- First upstream release
