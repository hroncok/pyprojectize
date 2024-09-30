Name:           python-transaction
Version:        4.0
Release:        6%{?dist}
Summary:        Transaction management for Python

License:        ZPL-2.1
URL:            https://pypi.io/project/transaction
Source0:        %pypi_source transaction

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-zope-interface


%global _description\
This package contains a generic transaction implementation for Python. It is\
mainly used by the ZODB, though.

%description %_description

%package -n python3-transaction
Summary:        Transaction management for Python 3

Requires:       python3-zope-interface

%description -n python3-transaction %_description


%prep
%autosetup -n transaction-%{version} -p1

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%check
%pytest


%files -n python3-transaction
%doc README.rst LICENSE.txt COPYRIGHT.txt
%{python3_sitelib}/transaction/
%{python3_sitelib}/transaction-*.dist-info


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0-5
- Rebuilt for Python 3.13

* Sun Apr 14 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0-4
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 4.0-1
- Update to upstream.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.12

* Mon Mar 20 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.1.0-1
- Update to upstream.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.0.1-9
- Do not use glob in python sitelib.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.1-7
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.0.1-6
- According to deprecation of mock switch to unittest.mock
- Use pytest macro in check section

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.0.1-1
- Update to upstream.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-8
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.0.0-1
- Initial epel8 build
- Update to upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-5
- Subpackage python2-transaction has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-1
- Update to 2.4.0 (#1644768)

* Tue Jul 24 2018 Kevin Fenzi <kevin@scrye.com> - 2.2.1-1
- Fix FTBFS bug #1605958
- Update to 2.2.1. Fixes bug #1561256

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Ralph Bean <rbean@redhat.com> - 2.2.0-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.2-3
- Python 2 binary package renamed to python2-transaction
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Kevin Fenzi <kevin@scrye.com> - 2.1.2-1
- Update to 2.1.2. Fixes bug #1431394

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuild for Python 3.6

* Wed Nov 23 2016 Kevin Fenzi <kevin@scrye.com> - 2.0.3-1
- Update to 2.0.3. Fixes bug #1396317

* Mon Nov 14 2016 Kevin Fenzi <kevin@scrye.com> - 2.0.2-1
- Update to 2.0.2. Fixes bug #1394442

* Wed Nov 09 2016 Kevin Fenzi <kevin@scrye.com> - 1.7.0-1
- Update to 1.7.0. Fixes bug #1393196

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Kevin Fenzi <kevin@scrye.com> - 1.6.1-1
- Update to 1.6.1. Fixes bug #1346645

* Sun May 29 2016 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0. Fixes bug #1338430

* Fri May 06 2016 Ralph Bean <rbean@redhat.com> - 1.5.0-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Ralph Bean <rbean@redhat.com> - 1.4.4-1
- new version

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 1.4.3-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Jan 22 2014 Ralph Bean <rbean@redhat.com> - 1.4.1-3
- Fix python3 requires.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 1.4.1-1
- Update to 1.4.1 (#634901)
- Build a python3 subpackage
- Remove python-transaction-1.1.1-context-manager.patch
- Modernize the spec

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 26 2011 Nils Philippsen <nils@redhat.com> - 1.1.1-3
- fix content manager interface

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Luke Macken <lmacken@redhat.com> - 1.1.1-1
- Update to 1.1.1
- Run the test suite

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.0-1
- Update to upstream bugfix 1.1.0

* Thu Jan 28 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.0-2
- Correction to how the setuptools vs setuptools-devel BR

* Thu Jan 28 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.0-1
- Update to 1.0 final.  Few fixes for tests and build/install cleanliness.
  No code changes.
- Conditionalize portions of the spec that are only needed for older distro releases.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Luke Macken <lmacken@redhat.com> - 1.0-0.3.a1
- Fix the license tag

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-0.2.a1
- Rebuild for Python 2.6

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0-0.1.a2
- Initial package
