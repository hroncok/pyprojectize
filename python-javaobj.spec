%global pypi_name javaobj

Name:           python-%{pypi_name}
Version:        0.4.4
Release:        1%{?dist}
Summary:        Python module for serializing and deserializing Java objects

License:        Apache-2.0
URL:            https://github.com/tcalmant/python-javaobj
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz 
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
python-javaobj is a python library that provides functions for reading
and writing (writing is WIP currently) Java objects serialized or will
be deserialized by ObjectOutputStream. This form of object representation
is a standard data interchange format in Java world.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  maven-local
BuildRequires:  xorg-x11-server-Xvfb

%description -n python3-%{pypi_name}
python-javaobj is a python library that provides functions for reading
and writing (writing is WIP currently) Java objects serialized or will
be deserialized by ObjectOutputStream. This form of object representation
is a standard data interchange format in Java world.

%prep
%autosetup -n %{name}-%{version}
# Remove shebang
sed -i -e '/^#!\//, 1d' {javaobj/*.py,javaobj/v1/*.py,javaobj/v2/*.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.4-1
- Update to latest upstream release (closes rhbz#2273933)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.3-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.3-13
- Rebuilt for Python 3.13

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.4.3-12
- Rebuilt for java-21-openjdk as system jdk

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.4.3-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.4.3-5
- Rebuilt for Drop i686 JDKs

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.3-4
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.4.3-3
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.3-1
- Update to latest upstream release 0.4.3 (rhbz#1924382)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.10

* Wed Feb 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream release 0.4.2 (#1924382)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream release 0.4.1 (#1825079)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0.1-1
- Remove Python 2 support
- Simplify spec file
- Update to latest upstream release 0.4.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20150606git64a6e0f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Raphael Groner <projects.rg@smart.ms> - 0-0.7.20150606git64a6e0f
- Python3 support
- New upstream snapshot

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20131228gitb8ae821
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.5.20131228gitb8ae821
- Introduce license macro

* Tue Jan 06 2015 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.4.20131228gitb8ae821
- BR python2

* Fri Dec 19 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.3.20142011svn31
- Use date of last commit (instead of checkout/export)
- Use GitHub (forked?)
- Remove sed fiddling
- Distribute tests folder as documentation samples

* Sat Nov 22 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.2.20142011svn31
- Fix swing/awt test

* Thu Nov 20 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0-0.1.20142011svn31
- Initial
