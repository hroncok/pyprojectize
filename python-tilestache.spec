%global pkgname tilestache
%global srcname TileStache

%global commit e96532bf59bf79c9991dcc06628f28b27bb19c08

Name:           python-%{pkgname}
Version:        1.51.14
Release:        18%{?dist}
Summary:        A stylish alternative for caching your map tiles

License:        BSD-3-Clause
URL:            http://tilestache.org
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

# Modify font search to find the system DejaVuSansMono.ttf - Not submitted upstream
Patch0:         %{name}-1.49.11-use-system-fonts.patch
# Don't install the bundled font or docs - Not submitted upstream
Patch1:         %{name}-1.49.11-unbundle-installs.patch
# Compatibility with Fedora's CGI - Not submitted upstream
Patch2:         %{name}-1.51.14-cgi-compat.patch
# Python 3 compatibility - Submitted upstream as TileStache/TileStache#345
Patch3:         %{name}-1.51.14-python3-compat.patch
# Non-standard python executable - Submitted upstream as TileStache/TileStache#359
Patch4:         %{name}-1.51.14-python3-executable.patch
# Bad escape in string literal - Submitted upstream as TileStache/TileStache#358
Patch5:         %{name}-1.51.14-escape-sequence.patch
# Support Shapely 2: Use shape instead of asShape from shapely.geometry
# Submitted upstream as TileStache/TileStache#375
Patch6:         %{name}-1.51.14-shapely2-compat.patch
# Replace assertEquals with assertEqual
# This deprecated unittest.TestCase alias was removed in Python 3.12.
# Submitted upstream as TileStache/TileStache#377
Patch7:         %{name}-1.51.14-assertEquals.patch

BuildArch:      noarch

%global _description\
TileStache is a Python-based server application that can serve up map tiles\
based on rendered geographic data. You might be familiar with TileCache, the\
venerable open source WMS server from MetaCarta. TileStache is similar, but we\
hope simpler and better-suited to the needs of designers and cartographers.

%description %_description


%package examples
Summary:        Example code for TileStache

%description examples
Example code for TileStache: A stylish alternative for caching your map tiles


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-gdal
BuildRequires:  python%{python3_pkgversion}-memcached
BuildRequires:  python%{python3_pkgversion}-modestmaps >= 1.3.0
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-shapely
BuildRequires:  python%{python3_pkgversion}-werkzeug
Requires:       font(dejavusansmono)
Conflicts:      python2-%{pkgname} < %{version}-%{release}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-imaging
Requires:       python%{python3_pkgversion}-modestmaps >= 1.3.0
Requires:       python%{python3_pkgversion}-simplejson
Requires:       python%{python3_pkgversion}-werkzeug
%endif # __pythondist_requires

%description -n python%{python3_pkgversion}-tilestache %_description


%prep
%autosetup -p1 -n %{srcname}-%{commit}

# Remove shebang from a script
sed -i '1{\@^#!/usr/bin/env python@d}' %{srcname}/Goodies/Caches/GoogleCloud.py

# Add shebang to a script
sed -i '1i #!%{_bindir}/bash' examples/zoom_example/run_server.sh

sed -i '1{s@^#!/usr/bin/env python@#!%{__python3}@}' examples/geotiff/server.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

install -d %{buildroot}%{_mandir}/man1
install -p -m0644 man/tilestache-clean.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-compose.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-list.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-render.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-seed.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 man/tilestache-server.1 %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_datadir}/%{srcname}
cp -a examples %{buildroot}%{_datadir}/%{srcname}/


%check
NO_DATABASE=1 OFFLINE_TESTS=1 %{__python3} -m nose \
  -I vectiles_tests.py \
  tests


%files examples
%license LICENSE
%doc README.md
%{_datadir}/%{srcname}

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc API.html CHANGELOG README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{_bindir}/tilestache-clean.py
%{_bindir}/tilestache-compose.py
%{_bindir}/tilestache-list.py
%{_bindir}/tilestache-render.py
%{_bindir}/tilestache-seed.py
%{_bindir}/tilestache-server.py
%{_mandir}/man1/tilestache-clean.1.gz
%{_mandir}/man1/tilestache-compose.1.gz
%{_mandir}/man1/tilestache-list.1.gz
%{_mandir}/man1/tilestache-render.1.gz
%{_mandir}/man1/tilestache-seed.1.gz
%{_mandir}/man1/tilestache-server.1.gz


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.51.14-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.51.14-14
- Patch for Shapely 2
- Update License to SPDX
- Patch for Python 3.12

* Thu Jul 20 2023 Python Maint <python-maint@redhat.com> - 1.51.14-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.51.14-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.51.14-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.51.14-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.51.14-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Scott K Logan <logans@cottsay.net> - 1.51.14-1
- Update to 1.51.14
- Drop python 2 subpackage (f32+) (rhbz#1738198)
- Handle automatic dependency generation (f30+)
- Add some of the tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.49.11-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.49.11-9
- Python 2 binary package renamed to python2-tilestache
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.49.11-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.49.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Scott K Logan <logans@cottsay.net> - 1.49.11-3
- More spec clean-ups for Package Review
- Use GitHub upstream
- Add examples subpackage

* Sun Nov 30 2014 Scott K Logan <logans@cottsay.net> - 1.49.11-2
- Spec clean-ups for Package Review

* Sun Sep 28 2014 Scott K Logan <logans@cottsay.net> - 1.49.11-1
- Initial package
