%global srcname xcffib

Summary:   A drop in replacement for xpyb, an XCB python binding
Name:      python-xcffib
Version:   1.5.0
Release:   5%{?dist}
Source0:   %{pypi_source}
License:   Apache-2.0
URL:       https://github.com/tych0/xcffib
BuildArch: noarch

BuildRequires:  libxcb-devel

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi >= 1.1.2
BuildRequires:  python3-six


%description
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.


%package -n python3-xcffib
Summary: A drop in replacement for xpyb, an XCB python binding
Requires:  python3-cffi
Requires:  libxcb

%description -n python3-xcffib
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.


%prep
%setup -q -n xcffib-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-xcffib
%doc LICENSE
%doc README.md
%{python3_sitelib}/xcffib
%{python3_sitelib}/xcffib*.egg-info


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Orion Poplawski <orion@nwra.com> - 1.5.0-1
- Update to 1.5.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.12

* Sat Jun 03 2023 Orion Poplawski <orion@nwra.com> - 1.4.0-1
- Update to 1.4.0

* Fri Jan 20 2023 Orion Poplawski <orion@nwra.com> - 1.2.0-1
- Update to 1.2.0
- Use SPDX License tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.11.1-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 02 2021 Orion Poplawski <orion@nwra.com> - 0.11.1-1
- Update to 0.11.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.9.0-1
- Upgrade to latest release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.8.1-1
- Upgrade to latest release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.7

* Tue Mar 20 2018 John Dulaney <jdulaney@fedoraproject> - 0.6.0-2
- Drop python2 subpackage

* Fri Mar 09 2018 John Dulaney <jdulaney@fedoraproject> - 0.6.0-1
- Update to latest release

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.1-4
- Fix creation of python2- subpackage

* Thu Aug 10 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.1-2
- Modernize spec file a bit, including expressly build python2- binary package

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuild for Python 3.6

* Fri May 06 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Fri Feb 12 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.1-1
- Update to latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 13 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.4.0-3
- Rebuild against new cffi

* Thu Nov 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.4.0-2
- Prepare for epel

* Thu Nov 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.4.0-1
- Update to latest upstream

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.6-1
- Update to latest upstream

* Mon Oct 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-5
- Rebuild against newest python-cairocffi (bz #1249821)

* Mon Aug 03 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-4
- Switch to noarch as no longer shipping C code

* Sun Jul 12 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-2
- Require newer python-cffi

* Sun Jul 12 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-1
- Update to latest upstream

* Fri Jul 10 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.1.11-3
- Python3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 14 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.1.11-1
- Update to latest upstream

* Thu Jan 22 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.1.10-2
- Updated to latest version

* Tue Nov 04 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.1.8-1
- Update to latest version

* Wed Oct 08 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.1.7-1
- Initial packaging
- Spec based on python-nose
