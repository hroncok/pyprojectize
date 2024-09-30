%global srcname funcparserlib
%global srcdesc \
Parser combinators are just higher-order functions that take parsers as their\
arguments and return them as result values. Parser combinators are:\
* First-class values\
* Extremely composable\
* Tend to make the code quite compact\
* Resemble the readable notation of xBNF grammars\
\
Parsers made with funcparserlib are pure-Python LL(*) parsers. It means that\
it's very easy to write them without thinking about look-aheads and all that\
hardcore parsing stuff. But the recursive descent parsing is a rather slow\
method compared to LL(k) or LR(k) algorithms.\
\
So the primary domain for funcparserlib is parsing little languages or external\
DSLs (domain specific languages).

Name:           python-%{srcname}
Version:        1.0.1
Release:        8%{?dist}
Summary:        Recursive descent parsing library based on functional combinators

License:        MIT
URL:            https://github.com/vlasovskikh/funcparserlib
Source:         %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel


%description %{srcdesc}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %{srcdesc}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc PKG-INFO README.md


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 05 2022 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-1
- Bump version to 1.0.1

* Fri Jul 29 2022 Alfredo Moralejo <amoralej@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0a1-3.prerelease
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0a1-2.prerelease
- Rebuilt for Python 3.11

* Wed Apr 20 2022 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.0a1-1.prerelease
- Bump version to 1.0.0a1 prerelease

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0a0-2.prerelease
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.0a0-1.prerelease
- Bump version to 1.0.0a0 prerelease

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.6-27
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-19
- Catch up with packaging guidelines
- In general, use recommended RPM macros
- Drop the Python 2 package
- Inline package description

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.6-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.6-13
- Python 2 binary package renamed to python2-funcparserlib
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-11
- Python 3 detection for epel7

* Fri Feb 10 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-10
- Update URL

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Dec 21 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-2
- Using %%{python3_version} instead of hardcoded 3.3

* Mon Dec 09 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-1
- Initial spec
