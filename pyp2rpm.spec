Name:           pyp2rpm
Version:        3.3.10
Release:        5%{?dist}
Summary:        Convert Python packages to RPM SPECFILES

License:        MIT
URL:            https://pypi.python.org/pypi/pyp2rpm
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(virtualenv-api)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest-runner)

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(flexmock) >= 0.9.3
BuildRequires:  python3dist(scripttest)
 
Requires:       python3dist(jinja2)
Requires:       python3dist(setuptools)
Requires:       python3dist(click)
Requires:       python3dist(virtualenv-api)
Requires:       python3-rpm
Requires:       rpmdevtools

# For Python 2 metadata extractor
Suggests:       python2dist(setuptools)

%description
Convert Python packages to RPM SPECFILES. The packages can be downloaded from
PyPI and the produced SPEC is in line with Fedora 201x-era Python Packaging
Guidelines or Mageia Python Policy.

Unfortunately, pyp2rpm does not generate spec files according to to the current
Fedora Python Packaging Guidelines.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%check
# TestMetadataExtractor requires Python 2 setuptools
PYTHONPATH="." py.test-3 -vv -m "not webtest" -k "not TestMetadataExtractor"

%files
%license LICENSE
%doc README.md
%{_bindir}/pyp2rpm
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.3.10-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 05 2023 Gordon Messmer <gordon.messmer@gmail.com> - 3.3.10-1
- Update to 3.3.10

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 3.3.9-2
- Rebuilt for Python 3.12

* Thu Apr 06 2023 Gordon Messmer <gordon.messmer@gmail.com> - 3.3.9-1
- Update to 3.3.9

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.3.8-2
- Rebuilt for Python 3.11

* Mon Feb 21 2022 Gordon Messmer <gordon.messmer@gmail.com> - 3.3.8-1
- Update to 3.3.8

* Mon Feb 21 2022 Miro Hrončok <mhroncok@redhat.com> - 3.3.7-4
- Update the description wrt the current Fedora Python Packaging Guidelines

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Gordon Messmer <gordon.messmer@gmail.com> - 3.3.7-1
- Update to 3.3.7. Fixes bug #1898087

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.6-2
- Rebuilt for Python 3.10

* Sun Mar 21 2021 Gordon Messmer <gordon.messmer@gmail.com> - 3.3.6-1
- Update to 3.3.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Gordon Messmer <gordon.messmer@gmail.com> - 3.3.5-1
- Update to 3.3.5. Fixes bug #1892478

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4 (#1822828)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-3
- Stop running Python 2 tests, don't recommend but only suggest Python 2 setuptools

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 3.3.3-1
- Update to 3.3.3. Fixes bug #1742365

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.2-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.2-7
- Only recommend python2-setuptools

* Thu Feb 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.2-6
- Only recommend python2-virtualenv-api

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.2-4
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.2-2
- Rebuilt for Python 3.7

* Wed Mar 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Michal Cyprian <mcyprian@redhat.com> - 3.3.0-2
- Use automatic provides style requires

* Sat Dec 16 2017 Kevin Fenzi <kevin@scrye.com> - 3.3.0-1
- Update to 3.3.0. Fixes bug #1526664

* Mon Aug 28 2017 Michal Cyprian <mcyprian@redhat.com> - 3.2.3-1
- Update to 3.2.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Michal Cyprian <mcyprian@redhat.com> - 3.2.2-1
- Update to 3.2.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Rebuild for Python 3.6

* Thu Oct 13 2016 Michal Cyprian <mcyprian@redhat.com> - 3.2.0-1
- Update to 3.2.1

* Wed Aug 10 2016 Michal Cyprian <mcyprian@redhat.com> - 3.1.3-1
- Update to 3.1.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 Michal Cyprian <mcyprian@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Wed Jun 01 2016 Michal Cyprian <mcyprian@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Thu Apr 21 2016 Michal Cyprian <mcyprian@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Wed Apr 13 2016 Michal Cyprian <mcyprian@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Aug 18 2015 Michal Cyprian <mcyprian@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 27 2014 Robert Kuska <rkuska@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Fri Sep 12 2014 Robert Kuska <rkuska@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.0b-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Apr 29 2014 Robert Kuska <rkuska@redhat.com> - 1.1.0b-1
- Update to v1.1.0b

* Wed Jan 29 2014 Robert Kuska <rkuska@redhat.com> - 1.0.1-4
- Change requires from distribute to setuptools
- Add rpmdevtools to requires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.5.1-6
- Update to 1.0.1.

* Mon Dec 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.5.1-5
- Properly require python3 deps only from the python3 subpackage.

* Mon Aug 06 2012 David Malcolm <dmalcolm@redhat.com> - 0.5.1-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Thu Aug  2 2012 David Malcolm <dmalcolm@redhat.com> - 0.5.1-3
- generalize py.test reference to work with Python 3.*

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.5.1-1
- Initial package.
