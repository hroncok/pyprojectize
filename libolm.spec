%global appname olm

Name: libolm
Version: 3.2.16
Release: 4%{?dist}

Summary: Double Ratchet cryptographic library
License: Apache-2.0
URL: https://gitlab.matrix.org/matrix-org/%{appname}
Source0: https://gitlab.matrix.org/matrix-org/%{appname}/-/archive/%{version}/%{appname}-%{version}.tar.bz2

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(cffi)
BuildRequires: python3dist(wheel)

%description
An implementation of the Double Ratchet cryptographic ratchet in C++.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%package python3
Summary: Python 3 bindings for %{name}
%{?python_provide:%python_provide python3-%{appname}}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%description python3
%{summary}.

%prep
%autosetup -n %{appname}-%{version} -p1
sed -e "s@/build@/%{_vpath_builddir}@g" -e 's@"build"@"%{_vpath_builddir}"@g' -i python/olm_build.py

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DOLM_TESTS=ON
%cmake_build

pushd python
%py3_build
popd

%check
pushd %{_vpath_builddir}/tests
    ctest --output-on-failure
popd

%install
%cmake_install

pushd python
%py3_install
popd

%files
%license LICENSE
%doc *.md *.rst docs/*.md
%{_libdir}/%{name}.so.3*

%files devel
%{_includedir}/%{appname}
%{_libdir}/%{name}.so
%{_libdir}/cmake/Olm
%{_libdir}/pkgconfig/%{appname}.pc

%files python3
%{python3_sitearch}/%{appname}
%{python3_sitearch}/_%{name}.abi3.so
%{python3_sitearch}/python_%{appname}-*.egg-info

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.16-3
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.16-2
- Rebuilt for Python 3.13

* Tue Feb 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 3.2.16-1
- Update to version 3.2.16

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.15-3
- Removed no longer used python-future dependency. Fixes rhbz#2222263.

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 3.2.15-2
- Rebuilt for Python 3.12

* Thu Jun 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.15-1
- Updated to version 3.2.15.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.14-1
- Updated to version 3.2.14.

* Sun Oct 09 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.13-1
- Updated to version 3.2.13.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.12-2
- Rebuilt for Python 3.11

* Tue May 31 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.12-1
- Updated to version 3.2.12.

* Mon Apr 18 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.11-1
- Updated to version 3.2.11.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.10-1
- Updated to version 3.2.10.

* Sat Jan 08 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.9-1
- Updated to version 3.2.9.

* Mon Dec 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.8-1
- Updated to version 3.2.8 with CVE fixes.

* Tue Dec 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.7-1
- Updated to version 3.2.7.

* Fri Sep 17 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.6-1
- Updated to version 3.2.6.

* Thu Sep 16 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.5-1
- Updated to version 3.2.5.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.4-2
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.4-1
- Updated to version 3.2.4.

* Tue May 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.3-1
- Updated to version 3.2.3.

* Tue Feb 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.2-1
- Updated to version 3.2.2.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.1-1
- Updated to version 3.2.1.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.5-1
- Updated to version 3.1.5.

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.4-4
- Added python3-setuptools to build requirements.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.4-1
- Updated to version 3.1.4.
- Added Python 3 bindings.

* Tue Aug 06 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.3-1
- Updated to version 3.1.3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.2-1
- Initial SPEC release.
