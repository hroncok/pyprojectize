%global modname kajiki

Name:               python-kajiki
Version:            0.9.2
Release:            8%{?dist}
Summary:            Really fast well-formed xml templates

License:            MIT
URL:                https://pypi.io/project/Kajiki
Source0:            %pypi_source kajiki

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-babel
BuildRequires:      python3-pytz
BuildRequires:      python3-pytest


%description
Are you tired of the slow performance of Genshi? But you still long for the
assurance that your output is well-formed that you miss from all those
other templating engines? Do you wish you had Jinja's blocks with Genshi's
syntax? Then look  no further, Kajiki is for you! Kajiki quickly compiles
Genshi-like syntax to *real python bytecode* that renders with blazing-fast
speed! Don't delay! Pick up your copy of Kajiki today!

%package -n python3-kajiki
Summary:            Really fast well-formed xml templates

Requires:           python3-babel
Requires:           python3-pytz

%description -n python3-kajiki
Are you tired of the slow performance of Genshi? But you still long for the
assurance that your output is well-formed that you miss from all those
other templating engines? Do you wish you had Jinja's blocks with Genshi's
syntax? Then look  no further, Kajiki is for you! Kajiki quickly compiles
Genshi-like syntax to *real python bytecode* that renders with blazing-fast
speed! Don't delay! Pick up your copy of Kajiki today!

%prep
%autosetup -n kajiki-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-kajiki
%doc README.rst LICENSE.rst CHANGES.rst PKG-INFO
%{_bindir}/kajiki
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/kajiki-%{version}-*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.2-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.2-1
- Update to upstream (bz#2148280).

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.1-1
- Update to upstream.
- Remove checks which have been removed upstream.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.0-3
- Remove unused dependency on nose (already using pytest)

* Tue Dec 28 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.0-2
- Remove unused dependency on nine

* Tue Nov 30 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.0-1
- Update to upstream

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Kevin Fenzi <kevin@scrye.com> - 0.8.3-1
- Update to 0.8.3. Fixes rhbz#1973883

* Fri Jun 11 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.8.2-7
- Apply upstream patch for python3.10
  https://github.com/nandoflorestan/kajiki/pull/52

* Sat Jun 05 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.8.2-6
- Nose replaced by pytest
- Disabled test_text test until this issue will be fixed:
  https://github.com/nandoflorestan/kajiki/issues/49

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.9

* Mon May 25 2020 Nils Philippsen <nils@redhat.com> - 0.8.2-1
- version 0.8.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Subpackage python2-kajiki has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 0.8.0-1
- Update to 0.8.0. Fixes bug #1716377

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.2
- Update to 0.7.2
- Add missing BR on python-nose to run the tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.1-2
- Fix creation of python2- subpackage

* Fri Sep 15 2017 Kevin Fenzi <kevin@scrye.com> - 0.7.1-1
- Update to 0.7.1. Fixes bug #1465427

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 27 2017 Kevin Fenzi <kevin@scrye.com> - 0.6.3-1
- Update to 0.6.3. Fixes bug #1455539

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Kevin Fenzi <kevin@scrye.com> - 0.6.1-1
- Update to 0.6.1. Fixes bug #1400145

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Ralph Bean <rbean@redhat.com> - 0.5.5-1
- new version

* Thu Jun 09 2016 Ralph Bean <rbean@redhat.com> - 0.5.4-1
- new version

* Tue Jun 07 2016 Kevin Fenzi <kevin@scrye.com> - 0.5.4-1
- Update to 0.5.4. Fixes bug #1342848

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 0.5.3-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Ralph Bean <rbean@redhat.com> - 0.5.2-2
- Add python3 subpackage and modernize python macros.

* Wed Oct 14 2015 Ralph Bean <rbean@redhat.com> - 0.5.2-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 0.5.1-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Ralph Bean <rbean@redhat.com> - 0.4.4-3
- Add req on python-nine.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- Latest upstream.
- Disabled tests now that they require python-nine which hasn't yet been
  packaged for Fedora.

* Tue Oct 08 2013 Ralph Bean <rbean@redhat.com> - 0.3.5-4
- Added dep on pytz.

* Tue Oct 08 2013 Ralph Bean <rbean@redhat.com> - 0.3.5-3
- Update dep from babel to python-babel.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Ralph Bean <rbean@redhat.com> - 0.3.5-1
- initial package for Fedora
