Name: virt-bootstrap
Version: 1.1.1
Release: 24%{?dist}
Summary: System container rootfs creation tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://github.com/virt-manager/virt-bootstrap
Source0: http://virt-manager.org/download/sources/virt-bootstrap/%{name}-%{version}.tar.gz

# Upstream patches

# Fix for Python 3.11
Patch100: virt_bootstrap-Fix-build-with-Python-3.11.patch

BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/git
BuildRequires: python3-devel
BuildRequires: python3-libguestfs
BuildRequires: python3-passlib
BuildRequires: fdupes

Requires: python3-libguestfs
Requires: python3-passlib
Requires: skopeo
Requires: libvirt-sandbox

BuildArch: noarch

%description
Provides a way to create the root file system to use for
libvirt containers.

%prep
%autosetup -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l virtBootstrap
%fdupes %{buildroot}%{_prefix}

# Replace '#!/usr/bin/env python3' with '#!/usr/bin/python3'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
for f in $(find %{buildroot} -type f -executable -print); do
    sed -i '1 s/^#!\/usr\/bin\/env python3/#!%{__python3}/' $f || :
done

# Delete '#!/usr/bin/env python'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
for f in $(find %{buildroot} -type f \! -executable -print); do
    sed -i '/^#!\/usr\/bin\/env python/d' $f || :
done

%files -f %{pyproject_files}
%doc README.md ChangeLog AUTHORS
%{_bindir}/virt-bootstrap
%{_mandir}/man1/virt-bootstrap*

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-24
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 1.1.1-22
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.1.1-19
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 8 2022 Radostin Stoyanov <rstoyanov@fedoraproject.org> - 1.1.1-16
- Rebuilt for Python 3.11

* Mon Jun 27 2022 Radostin Stoyanov <rstoyanov@fedoraproject.org> - 1.1.1-15
- Fix built for Python 3.11

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.1.1-14
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Fabiano Fidêncio <fabiano@fidencio.org> - 1.1.1-1
- Update to new upstream release: 1.1.1
- Resolves: rhbz#1727771

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Thu May 31 2018 Fabiano Fidêncio <fabiano@fidencio.org> -1.1.0-1
- Update to new upstream release: 1.1.0

* Thu May 17 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 1.0.0-2
- Set "BuildArch: noarch" as this is an arch independent package
- Drop "Buildroot" tag as it's obsolete
- Drop "%%defattr" tag as it's obsolete
- Add "BuildRequires: /usr/bin/git" (due to %%autosetup -S git)
- Add a note to make clear that the patches are backported from upstream
- Replace '#!/usr/bin/env python3' with '#!/usr/bin/python3'
- Delete '#!/usr/bin/env python' from non executable files

* Wed May 16 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 1.0.0-1
- Initial release
