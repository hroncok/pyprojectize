Name:           reprotest
Version:        0.7.28
Release:        1%{?dist}
Summary:        Build packages and check them for reproducibility
URL:            https://salsa.debian.org/reproducible-builds/%{name}

License:        GPL-3.0-or-later
Source0:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}_%{version}.tar.xz
Source1:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}_%{version}.tar.xz.asc
Source2:        https://salsa.debian.org/reproducible-builds/reproducible-website/-/raw/master/reproducible-builds-developers-keys.asc
BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  python%{python3_pkgversion}-devel

Requires:       python%{python3_pkgversion}-rstr
Requires:       diffoscope
Requires:       disorderfs
Requires:       faketime
Requires:       fakeroot
Requires:       glibc-all-langpacks
Requires:       rpm-build

%description
reprotest builds the same source code twice in different environments, and
then checks the binaries produced by each build for differences. If any are
found, then diffoscope (or if unavailable then diff) is used to display them
in detail for later analysis.

It supports different types of environment such as a "null" environment (i.e.
doing the builds directly in /tmp) or various other virtual servers, for
example schroot, ssh, qemu, and several others.

reprotest is developed as part of the "reproducible builds" Debian project.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/reprotest

%changelog
* Tue Sep 10 2024 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 0.7.28-1
- version 0.7.28

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.26-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.26-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 0.7.26-1
- version 0.7.26

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.22-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 0.7.22-1
- version 0.7.22

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.19-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 0.7.19-1
- version 0.7.19

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.16-4
- Rebuilt for Python 3.10

* Tue Feb 09 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-3
- Use sources signature verification

* Mon Feb 08 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-2
- Update requirements

* Wed Feb 03 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.16-1
- version 0.7.16

* Mon Jan 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.7.15-1
- Initial RPM packaging.
