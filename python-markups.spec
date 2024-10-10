%global pypi_name markups

Name:           python-%{pypi_name}
Version:        3.1.3
Release:        13%{?dist}
Summary:        A wrapper around various text markups

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/retext-project/pymarkups
Source0:        %{pypi_source Markups}
BuildArch:      noarch

# Fix tests with Pygments 2.11.2
# Commit backported from: https://github.com/retext-project/pymarkups/commit/c13ae6633
Patch:          fix-tests-with-pygments-2.11.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(python-markdown-math)
BuildRequires:  python3dist(textile)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pyyaml)

%description
This module provides a wrapper around various text markup languages. Available
by default are Markdown, reStructuredText and Textile, but you can easily
add your own markups.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module provides a wrapper around various text markup languages. Available
by default are Markdown_, reStructuredText_ and Textile_, but you can easily
add your own markups.


%package -n python-%{pypi_name}-doc
Summary:        markups documentation
%description -n python-%{pypi_name}-doc
Documentation for markups


%prep
%autosetup -p1 -n Markups-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%{__python3} setup.py test -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.3-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.1.3-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 3.1.3-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.3-4
- Rebuilt for Python 3.11

* Mon Feb 07 2022 Karolina Surma <ksurma@redhat.com> - 3.1.3-3
- Fix tests failures with Pygments 2.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 José Matos <jamatos@fedoraproject.org> - 3.1.3-1
- Update source to 3.1.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul  6 2020 José Matos <jamatos@fedoraproject.org> - 3.0.0-2
- Remove manual Requires (they are autodetected)
- Clean the Description text

* Sun May 03 2020 José Abílio Matos <jamatos@fc.up.pt> - 3.0.0-1
- Update to 3.0.0 for resubmission

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-11
- Subpackage python2-markups has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-6
- Python 2 binary package renamed to python2-markups
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 13 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 2.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.0.1-1
- New upstream version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Sep 26 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-4
- Yet some more runtime requirements

* Thu Sep 24 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-3
- Fix runtime requirements

* Tue Sep 22 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-2
- Add python-docutils as runtime requirement

* Fri Sep 11 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-1
- New upstream version
- Disable the tests for now

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 31 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-4
- Fix the disttag
- Remove LICENSE from %%doc in the python3 package

* Tue Dec 30 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-3
- Use the %%license macro

* Sat Dec 06 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-2
- Some cleanup due to rpmlint warnings

* Sun Nov 30 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-1
- New upstream version
- Enable both Python 2 and 3

* Sun May 05 2013 Huaren Zhong <huaren.zhong@gmail.com> - 0.2.4
- Rebuild for Fedora
