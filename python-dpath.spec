%global pypi_name dpath

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        2%{?dist}
Summary:        Library for searching dictionaries using XPath-like expressions

License:        MIT
URL:            https://github.com/akesterson/dpath-python
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python library for accessing and searching dictionaries via /slashed/paths ala
xpath.

Basically it lets you glob over a dictionary as if it were a filesystem. It
allows you to specify globs (ala the bash eglob syntax, through some advanced
fnmatch.fnmatch magic) to access dictionary elements, and provides some facility
for filtering those results.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library for accessing and searching dictionaries via /slashed/paths ala
xpath

Basically it lets you glob over a dictionary as if it were a filesystem. It
allows you to specify globs (ala the bash eglob syntax, through some advanced
fnmatch.fnmatch magic) to access dictionary elements, and provides some facility
for filtering those results.

%prep
%autosetup -n %{pypi_name}-%{version}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-dpath
%doc LICENSE.txt README.rst
%{python3_sitelib}/%{pypi_name}*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release (closes rhbz#2292088)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.6-2
- Rebuilt for Python 3.13

* Sat Jan 27 2024 7Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.6-1
- Update to 2.1.6 (close RHBZ#2181770)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1.4-2
- Rebuilt for Python 3.12

* Sun Feb 19 2023 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.4-1
- Update to latest upstream release 2.1.4 (closes rhbz#2145018)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.6-2
- Rebuilt for Python 3.11

* Fri Mar 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.6-1
- Update to latest upstream release 2.0.6 (closes rhbz#2049315)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-1
- Update to latest upstream release 2.0.5 (closes rhbz#2003476)

* Sun Sep 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.4-1
- Update to latest upstream release 2.0.4 (closes rhbz#2003377)

* Wed Sep 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Update to latest upstream release 2.0.3 (closes rhbz#2002457)

* Fri Sep 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Update to latest upstream release 2.0.2 (closes rhbz#2000790)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Update to latest upstream release 2.0.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-16
- Subpackage python2-dpath has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-11
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-8
- Python 2 binary package renamed to python2-dpath
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 21 2015 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-1
- Update to new upstream version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.5.70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.2-0.3.70
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-0.2.70
- Update to new upstream version

* Wed Mar 19 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-0.1.52.20140319gita6ce774d
- Initial packaging

