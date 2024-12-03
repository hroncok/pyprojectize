%global modname backlash

Name:               python-backlash
Version:            0.3.2
Release:            3%{?dist}
Summary:            Standalone WebOb port of the Werkzeug Debugger

License:            MIT
URL:                https://pypi.io/project/backlash
Source0:            %pypi_source backlash

BuildArch:          noarch

%global _description\
backlash is a standalone version of the Werkzeug Debugger based on WebOb\
adapted to support for Python3.\
\
backlash has born as a future replacement for WebError in upcoming TurboGears2\
versions.

%description %_description

%package -n python3-backlash
Summary:            Standalone WebOb port of the Werkzeug Debugger with Python3 support meant to replace WebError in TurboGears2
%py_provides        python3-backslash
BuildRequires:      python3-devel
Requires:           open-sans-fonts

%description -n python3-backlash %_description


%prep
%setup -q -n %{modname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{modname}
ln -sfv /usr/share/fonts/open-sans/OpenSans-Regular.ttf %{buildroot}/%{python3_sitelib}/%{modname}/statics/opensans.ttf


%check
%pyproject_check_import


%files -n python3-backlash -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.13

* Sat Mar 16 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.3.2-1
- Update to upstream.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.1-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.9

* Thu May 07 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.3.1-2
- Use bundled LICENSE file

* Thu May 07 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.3.1-1
- Update to upstream (bz#1832605)

* Sun Mar 22 2020 Carl George <carl@george.computer> - 0.2.0-1
- Latest upstream rhbz#1808838

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-3
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Subpackage python2-backlash has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.4-1
- Update to 0.1.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Oct 18 2017 Ralph Bean <rbean@redhat.com> - 0.1.3-1
- new version

* Fri Sep 15 2017 Kevin Fenzi <kevin@scrye.com> - 0.1.2-4
- Unbundle open-sans-font. Fixes #1465421

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.2-3
- Python 2 binary package renamed to python2-backlash
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Ralph Bean <rbean@redhat.com> - 0.1.2-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 0.1.0-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Ralph Bean <rbean@redhat.com> - 0.0.8-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 0.0.6-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Jan 22 2014 Ralph Bean <rbean@redhat.com> - 0.0.4-1
- Latest upstream
- Fixed python3 requires.
- Remove patch now that it has been pushed upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.4.a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Luke Macken <lmacken@redhat.com> 0.0.1-0.3.a2
- Build the python3 subpackage
- Fix pre-release version

* Wed Apr 03 2013 Luke Macken <lmacken@redhat.com> 0.0.1a2-2
- Remove the non-free ubuntu font
- Require python-webob

* Wed Apr 03 2013 Luke Macken <lmacken@redhat.com> 0.0.1a2-1
- Initial package for Fedora
