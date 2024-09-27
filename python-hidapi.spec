%global py_setup_args --with-system-hidapi --with-libusb

Name:     python-hidapi
Version:  0.14.0.post2
Release:  3%{?dist}
Summary:  Interface to the hidapi library

# Automatically converted from old format: GPLv3+ or BSD or Public Domain - review is highly recommended.
License:  GPL-3.0-or-later OR LicenseRef-Callaway-BSD OR LicenseRef-Callaway-Public-Domain
URL:      https://github.com/trezor/cython-hidapi
Source0:  %{pypi_source hidapi}

BuildRequires: gcc
BuildRequires: hidapi-devel
BuildRequires: libusb1-devel
BuildRequires: libudev-devel

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-cython

%description
%{summary}.


%package -n python3-hidapi
Summary:  %{summary}

%description -n python3-hidapi
%{summary}.


%prep
%autosetup -n hidapi-%{version}

# Remove pre-built and bundled hidapi.
rm -rf hidapi hidapi.egg-info hid.c

%if 0%{?flatpak}
# hidapi is not part of the runtime and is also built into /app
sed -i -e 's|/usr/include/hidapi|%{_includedir}/hidapi|' setup.py
%endif

%build
%py3_build


%install
%py3_install


%check
%{pytest} tests.py


%files -n python3-hidapi
%license LICENSE*.txt
%doc README.rst try.py
%{python3_sitearch}/hid%{python3_ext_suffix}
%{python3_sitearch}/hidraw%{python3_ext_suffix}
%{python3_sitearch}/hidapi-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14.0.post2-3
- convert license to SPDX

* Sat Aug 24 2024 Jonny Heggheim <hegjon@gmail.com> - 0.14.0.post2-2
- Build against libusb1 instead of libusb-compat-0.1

* Sat Aug 24 2024 Jonny Heggheim <hegjon@gmail.com> - 0.14.0.post2-1
- Updated to version 0.14.0.post2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.14.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 12 2023 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-5
- Backport Cython 3 support
- Fixes: rhbz#2254042

* Thu Nov 23 2023 Jonny Heggheim <hegjon@gmail.com> - 0.14.0-4
- Build with older version of Cython, Cython 3 is not supported

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.14.0-2
- Rebuilt for Python 3.12

* Tue May 30 2023 Jonny Heggheim <hegjon@gmail.com> - 0.14.0-1
- Updated to version 0.14.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jonny Heggheim <hegjon@gmail.com> - 0.13.1-1
- Updated to version 0.13.1

* Mon Nov 14 2022 Jonny Heggheim <hegjon@gmail.com> - 0.12.0.post2-4
- Added missing BuildRequires for python3-setuptools
  Fixes rhbz#2142038

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.post2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.12.0.post2-2
- Rebuilt for Python 3.11

* Mon Jun 06 2022 Jonny Heggheim <hegjon@gmail.com> - 0.12.0.post2-1
- Updated to version 0.12.0.post2

* Sat Apr 30 2022 Jonny Heggheim <hegjon@gmail.com> - 0.11.2-1
- Updated to version 0.11.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.post2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Björn Esser <besser82@fedoraproject.org> - 0.11.0.post2-1
- Updated to version 0.11.0.post2
  Fixes rhbz#1504331

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Jonny Heggheim <hegjon@gmail.com> - 0.10.0-1
- Updated to version 0.10.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.post2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jonny Heggheim <hegjon@gmail.com> - 0.9.0.post2-1
- Updated to 0.9.0.post2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-11
- Subpackage python2-hidapi has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com>
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com>
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-3
- Rebuild for Python 3.6

* Sun Nov 06 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post20-2
- Rebuilt for ppc64

* Sat Oct 29 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post20-1
- Update to new release v0.7.99.post20
- Build against system hidapi
- Run testsuite
- Remove license-files from github, included in upstream-tarball

* Sat Oct 22 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post19-1
- Initial import (rhbz 1387837)

* Fri Oct 21 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post19-0.1
- Initial package (rhbz 1387837)
