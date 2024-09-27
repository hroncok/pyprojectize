%global pypi_name pulsectl

Name:           python-%{pypi_name}
Version:        22.3.2
Release:        10%{?dist}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

License:        MIT
URL:            https://pypi.org/project/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/1a/a9/cdd1a19889f78ddd45775b9830045df2b4eb25f63911a2ddc3aaf8ec614f/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pulseaudio-libs

%description
Python (3.x and 2.x) high-level interface and ctypes-based bindings
for PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%package     -n python3-%{pypi_name}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

%description -n python3-%{pypi_name}
Python 3.x high-level interface and ctypes-based bindings for
PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%prep
%setup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%{pyproject_wheel}


%install
%{pyproject_install}


%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*egg-info/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 22.3.2-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 22.3.2-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 22.3.2-2
- Rebuilt for Python 3.11

* Fri Mar 25 2022 Paul W. Frields <pfrields@scarlett> - 22.3.2-1
- New upstream release 22.3.2 (#2067029)

* Fri Feb 11 2022 Paul W. Frields <pfrields@scarlett> - 22.1.3-1
- New upstream release 22.1.3 (#2002065)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.5.18-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Paul W. Frields <pfrields@scarlett> - 21.5.18-1
- New upstream release 21.5.18 (#1958563)

* Fri Apr 16 2021 Paul W. Frields <pfrields@scarlett> - 21.3.4-1
- New upstream release 21.3.4 (#1932817)

* Sat Mar  6 2021 Paul W. Frields <stickster@gmail.com> - 21.3.2-1
- New upstream release 21.3.2 (#1932817)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Paul W. Frields <stickster@gmail.com> - 20.5.1-2
- New upstream release 20.5.1 (#1837830)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.4.3-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Paul W. Frields <stickster@gmail.com> - 20.4.3-1
- New upstream release 20.4.3 (#1825597)

* Tue Mar  3 2020 Paul W. Frields <stickster@gmail.com> - 20.2.4-1
- New upstream release 20.2.4 (#1808016)

* Tue Feb 11 2020 Paul W. Frields <stickster@gmail.com> - 20.2.2-1
- New upstream release 20.2.2 (#1790078)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov  9 2019 Paul W. Frields <stickster@gmail.com> - 19.10.4-1
- Update to latest upstream 19.10.4 (#1759622)

* Mon Oct 14 2019 Paul W. Frields <stickster@gmail.com> - 19.10.0-1
- Update to latest upstream 19.10.0 (#1759622)

* Wed Sep 25 2019 Paul W. Frields <stickster@gmail.com> - 19.9.5-1
- Update to latest upstream 19.9.5 (#1754263)

* Wed Sep  4 2019 Paul W. Frields <stickster@gmail.com> - 18.12.5-1
- Initial RPM release
