%global srcname bottle

Name:           python-%{srcname}
Version:        0.13.0
Release:        1%{?dist}
Summary:        Fast and simple WSGI-framework for small web-applications

License:        MIT
URL:            http://bottlepy.org
Source0:        https://github.com/bottlepy/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(pytest)

%description
Bottle is a fast and simple micro-framework for small web-applications.
It offers request dispatching (Routes) with URL parameter support, Templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines. All in a single file and with no dependencies other than the
Python Standard Library.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Fast and simple WSGI-framework for small web-applications

%description -n python%{python3_pkgversion}-%{srcname}
Bottle is a fast and simple micro-framework for small web-applications.
It offers request dispatching (Routes) with URL parameter support, Templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines. All in a single file and with no dependencies other than the
Python Standard Library.

%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i '/^#!/d' bottle.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm %{buildroot}%{_bindir}/bottle.py

%check
%{pytest} test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS README.rst docs/*
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/*.dist-info
%{python3_sitelib}/*.py

%changelog
* Fri Sep 06 2024 Federico Pellegrin <fede@evolware.org> - 0.13.0-1
- Bump to 0.13.0
- Drop upstreamed patch and drop python-legacy-cgi dependency

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.12.25-8
- Depend on python-legacy-cgi as a Python 3.13 workaround (close RHBZ#2245642)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.12.25-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Federico Pellegrin <fede@evolware.org> - 0.12.25-3
- Fix module loading for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.12.25-2
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Federico Pellegrin <fede@evolware.org> - 0.12.25-1
- Update to 0.12.25
- Drop now upstreamed patch for deprecation in tests

* Tue Feb 28 2023 Federico Pellegrin <fede@evolware.org> - 0.12.24-1
- Update to 0.12.24

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Federico Pellegrin <fede@evolware.org> - 0.12.23-2
- Fix deprecation in tests that breaks on Python 3.12

* Mon Dec 12 2022 Federico Pellegrin <fede@evolware.org> - 0.12.23-1
- Update to 0.12.23, drop upstreamed patches and add full test run

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.12.21-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Ali Erdinc Koroglu <aekoroglu@centosproject.org> - 0.12.21-2
- Cookie test fix backported from upstream (0.12)

* Thu Jun 09 2022 Ali Erdinc Koroglu <aekoroglu@centosproject.org> - 0.12.21-1
- Update to 0.12.21 (rhbz #2094655 + #2094654 and #2021856)

* Mon Feb 07 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.12.19-1
- Update to 0.12.19

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 0.12.18-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020  Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.12.18-1
- Update to 0.12.18

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.13-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.13-10
- Subpackage python2-bottle has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.13-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12.13-6
- Avoid use of undefined unversioned python macro (which leads to
  the binary package owning "/" :( )

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.13-4
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.13-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Stratakis Charalampos <cstratak@redhat.com> - 0.12.13-1
- Update to 0.12.13

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.12.9-4
- Rebuild for Python 3.6

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12.9-3
- Do not own __pycache__ dir

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.9-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12.9-1
- Update to 0.12.9
- Run tests but ignore python3 failure for now

* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12.6-5
- Use modern python packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jul 12 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.12.6-1
- resolves rhbz#1093257 - JSON content type not restrictive enough

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.11.6-1
- upstream release 0.11.6
- add python3 subpackage. resolves rhbz#949240
- spec file patch from Haïkel Guémar <hguemar@fedoraproject.org>

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Ian Weller <iweller@redhat.com> - 0.10.7-1
- Update to 0.10.7 (required by python-mwlib)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.5-1
- Initial spec
