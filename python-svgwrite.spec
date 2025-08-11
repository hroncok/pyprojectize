%global pypi_name svgwrite

Name:           python-%{pypi_name}
Version:        1.4.3
Release:        10%{?dist}
Summary:        Python library to create SVG drawings

License:        MIT
URL:            https://github.com/mozman/svgwrite
Source0:        %{pypi_name}-%{version}.zip
Patch0:         0001-Skip-test-that-needs-internet-connection.patch

BuildArch: noarch

%description
Python library to create SVG drawings.

%package -n     python3-%{pypi_name}
Summary:        Python 3 library to create SVG drawings
BuildRequires:  python3-devel
BuildRequires:  python3-pyparsing
BuildRequires:  python3-pytest
Requires:       python3-setuptools
Requires:       python3-pyparsing

%description -n python3-%{pypi_name}
Python 3 library to create SVG drawings.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
# Remove shebang
for lib in %{buildroot}%{python3_sitelib}/%{pypi_name}/{,*/}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%check
%pyproject_check_import
%{__python3} -m unittest discover -s tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc NEWS.rst README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.3-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.3-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.3-2
- Rebuilt for pyparsing-3.0.9

* Fri Jul 15 2022 Vojtech Trefny <vtrefny@redhat.com> - 1.4.3-2
- Update to 1.4.3

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.11

* Wed Mar 23 2022 Vojtech Trefny <vtrefny@redhat.com> - 1.4.1-2
- Update to 1.4.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Vojtech Trefny <vtrefny@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Fri Aug 21 2020 Vojtech Trefny <vtrefny@redhat.com> - 1.4-1
- Update to 1.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Vojtech Trefny <vtrefny@redhat.com> - 1.3.1-2
- Skip 'test_pretty_print' test case due to Python 3.8 changes

* Thu Jul 04 2019 Vojtech Trefny <vtrefny@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Mon Jun 24 2019 Vojtech Trefny <vtrefny@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Mon Feb 25 2019 Vojtech Trefny <vtrefny@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.12-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.12-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Dec 27 2017 Julien Enselme <jujens@jujens.eu> - 1.1.12-1
- Update to 1.1.12

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017  Julien Enselme <jujens@jujens.eu> - 1.1.11-1
- Update to 1.1.11

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-2
- Rebuild for Python 3.6

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 1.1.8
- Update to 1.1.8

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 6 2015 Julien Enselme <jujens@jujens.eu> - 1.1.6-4
- Correct provides for python2 package

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 1.1.6-3
- Rebuilt for python 3.5

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 1.1.6-2
- Update package with new python guidelines

* Fri Jun 19 2015 Julien Enselme <jujens@jujens.eu> - 1.1.6-1
- Update to 1.1.6
- Reformat Requires and BuildRequires

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Apr 15 2014 Julien Enselme <jujens@jujens.eu> - 1.1.5-1
- Update to 1.1.5 from upstream

* Tue Mar 25 2014 Julien Enselme <jujens@jujens.eu> - 1.1.4-2
- Add python-setuptools as a dependancy

* Tue Mar 25 2014 Julien Enselme <jujens@jujens.eu> - 1.1.4-1
- Update to 1.1.4 from upstream
- The bundled library was removed upstream

* Fri Mar 14 2014 Julien Enselme <jujens@jujens.eu> - 1.1.3-4
- Add pyparsing and python3-pyparsing as requires
- Patch sources so that this bundled library is not used

* Wed Mar 12 2014 Julien Enselme <jujens@jujens.eu> - 1.1.3-3
- Add check macro for unitests

* Fri Feb 28 2014 Julien Enselme <jujens@jujens.eu> - 1.1.3-2
- Add python3 support
- Improve packaging

* Sun Feb 09 2014 Julien Enselme <jujens@jujens.eu> - 1.1.3-1
- Initial packaging
