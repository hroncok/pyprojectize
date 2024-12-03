%global pypi_name hddfancontrol

Name:           %{pypi_name}
Version:        1.6.2
Release:        2%{?dist}
Summary:        Control system fan speed by monitoring hard drive temperature

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/desbma/hddfancontrol

# The PyPI archives don't have unit tests in them anymore.
Source0:        https://github.com/desbma/hddfancontrol/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pypandoc, python3-daemon, python3-docutils
BuildRequires:  hddtemp, hdparm
BuildRequires:  systemd

Requires:       python3-daemon
Requires:       python3-docutils
Requires:       python3-setuptools

Requires:       hddtemp, hdparm

%py_provides    python3-%{pypi_name}

%description
HDD Fan control is a command line tool to dynamically control fan speed
according to hard drive temperature on Linux.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
cp %{buildroot}/%{_bindir}/hddfancontrol %{buildroot}/%{_bindir}/hddfancontrol-3
ln -sf %{_bindir}/hddfancontrol-3 %{buildroot}/%{_bindir}/hddfancontrol-%{python3_version}

# Remove the "tests" directory that gets installed systemwide.
rm -rf %{buildroot}%{python3_sitelib}/tests

# Install the systemd script and config file.
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/

sed 's,conf.d/hddfancontrol,hddfancontrol.conf,' -i systemd/hddfancontrol.service
cp -a systemd/hddfancontrol.service %{buildroot}%{_unitdir}/
cp -a systemd/hddfancontrol.conf %{buildroot}%{_sysconfdir}/

# Run the tests.
%check
%pyproject_check_import

%{__python3} setup.py test

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/hddfancontrol
%{_bindir}/hddfancontrol-3
%{_bindir}/hddfancontrol-%{python3_version}
%{_unitdir}/hddfancontrol.service
%config(noreplace) %{_sysconfdir}/hddfancontrol.conf

%changelog
* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.2-2
- convert license to SPDX

* Thu Jul 18 2024 Filipe Rosset <rosset.filipe@gmail.com> - 1.6.2-1
- Update to 1.6.2 fixes rhbz#2255191

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.12

* Thu Jun 29 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.1-1
- Update to 1.5.1 fixes rhbz#2217647

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.5.0-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.0-1
- Update to 1.5.0 fixes rhbz#1934528

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.1-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.3.1-1
- Update to latest upstream release.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.3.0-1
- Update to latest upstream release (#1754224).

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.10-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.10-1
- Update to latest upstream release, 1.2.10 (rhbz#1669729).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.8-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.8-1
- Rebuilt for new upstream version 1.2.8, fixes rhbz #1541821

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.2.7-1
- Updated to 1.2.7, fixing a bug in hdparm error handling.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.2.6-1
- Updated to latest upstream release.
- Added systemd service file and configuration file.

* Fri Jan 13 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.2.5-1
- Updated to latest upstream release.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-2
- Rebuild for Python 3.6

* Wed Aug 24 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.2.4-1
- Initial package.
