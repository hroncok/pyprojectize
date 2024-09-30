%global srcname pyrtlsdr
Name:             python-%{srcname}
Version:          0.3.0
Release:          7%{?dist}
Summary:          Python binding for librtlsdr
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only
URL:              https://github.com/roger-/pyrtlsdr
Source0:          https://github.com/roger-/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:        noarch

%description
Python binding for librtlsdr (a driver for Realtek RTL2832U based SDR's).

%package -n python3-%{srcname}
Summary:          Python 3 binding for librtlsdr
BuildRequires:    python3-devel
BuildRequires:    python3-pypandoc, python3-m2r
# needed for librtlsdr
Requires:         rtl-sdr
# faster arrays
Recommends:       python2-numpy

%description -n python3-%{srcname}
Python 3 binding for librtlsdr (a driver for Realtek RTL2832U based SDR's).

%prep
%setup -qn %{srcname}-%{version}
rm -rf pyrtlsdr.egg-info
chmod 644 rtlsdr/rtlsdrtcp/base.py

find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rtlsdr

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.0-4
- Rebuilt for new rtl-sdr

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.0-1
- New version
  Resolves: rhbz#2228947

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 0.2.93-4
- Rebuilt for Python 3.12

* Tue Jul 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.93-3
- Rebuilt for new python
  Resolves: rhbz#2220446

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug  4 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.93-1
- New version
  Resolves: rhbz#2113786

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.92-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.92-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.92-2
- Rebuilt for Python 3.9

* Mon Mar  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.92-1
- New version
  Resolves: rhbz#1811286

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.8-8
- Dropped Python 2 support
  Resolves: rhbz#1769827

* Mon Sep 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-7
- Remove unneeded build time dependencies

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-2
- Rebuilt for Python 3.7

* Mon May  7 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.8-1
- New version
  Resolves: rhbz#1575179

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.7-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.7-1
- New version
  Resolves: rhbz#1497493

* Fri Aug 18 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.5-3
- This is an update fixing missing rtlsdraio module with python 2
  Resolves: rhbz#1473513

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.5-1
- New version
  Resolves: rhbz#1468790
- Dropped no-markdown patch (not needed)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-6
- Fixed rtlsdrtcp location

* Tue Jul 12 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-5
- Release bump to fix upgrade path from f23

* Thu Apr 21 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-3
- Removed rtlsdrtcp python objects from the sitedir

* Wed Apr 20 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-2
- rtlsdrtcp packaged into /usr/bin

* Tue Apr 12 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-1
- Initial release
