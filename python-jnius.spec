%global modname jnius
%global srcname py%{modname}
%global sum     Dynamic access to Java classes from Python


Name:           python-%{modname}
Version:        1.6.1
Release:        4%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/kivy/%{srcname}

ExclusiveArch:  %{java_arches}

Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  make
# avoid strict pointer checks with gcc 14, https://bugs.gentoo.org/917562
BuildRequires:  clang

BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)

BuildRequires:  python3dist(sphinx) 
BuildRequires:  python3dist(furo)

BuildRequires:  ant
BuildRequires:  java-devel

ExclusiveArch:  %{java_arches}

# https://github.com/kivy/pyjnius/issues/307
#ExcludeArch:    ppc64 s390x

%description
%{summary}.

%package     -n python3-%{srcname}
Summary:        %{sum}
Requires:       java-headless
Requires:       python3-six
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       python3-%{modname}


%description -n python3-%{srcname}
%{summary}.

%package        doc
Summary:        Documentation files for %{srcname}
BuildArch:      noarch

%description    doc
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
CC=%{_bindir}/clang %pyproject_wheel

make %{_smp_mflags} -C docs SPHINXBUILD='sphinx-build-3 %{_smp_mflags}' html

# build java classes for tests
# there is also Makefile, but it calls python setup.py build_ext --inplace
# together with ant, so we don't use it not to build python bits twice
ant all


%install
%pyproject_install


%check
pushd tests
export CLASSPATH=../build/test-classes:../build/classes
export JAVA_HOME=%{_prefix}/lib/jvm/java
# json options fail on some arches
%pytest \
 %ifarch s390x ppc64le
  -k 'not jvm_options' \
 %endif
 -v
popd


%files -n python3-%{srcname}
%license LICENSE
%doc *.md
%{python3_sitearch}/%{modname}/
%{python3_sitearch}/%{modname}_config.py*
%{python3_sitearch}/%{srcname}-%{version}.dist-info/
%{python3_sitearch}/__pycache__/%{modname}_config.cpython-*.pyc
%exclude %{python3_sitearch}/__pycache__
%exclude %{python3_sitearch}/setup_sdist.py

%files doc
%license LICENSE
%doc docs/build/html/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.13

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.6.1-2
- Rebuilt for java-21-openjdk as system jdk

* Mon Feb 26 2024 Raphael Groner <raphgro@fedoraproject.org> - 1.6.1-1
- bump to latest version
- migrate to Cython 3, rhbz#2254033
- use clang instead of gcc 14 to avoid strict pointer checks

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 Raphael Groner <raphgro@fedoraproject.org> - 1.3.0-17
- exclude i686, rhbz#2104095
- use pytest macro 

* Sat Jul 29 2023 Raphael Groner <raphgro@fedoraproject.org> - 1.3.0-16
- avoid Cython 3 

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.3.0-14
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-11
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.3.0-10
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.3.0-5
- use pytest instead of nose as upstream decided, see changes in Makefile
- skip useless additional setup

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.0-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Jun 06 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.3.0-1
- bump to v1.3.0 

* Sat Jun 06 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.2.0-6
- rebuilt

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Raphael Groner <projects.rg@smart.ms> - 1.2.0-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.1.4-1
- new version

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Subpackage python2-pyjnius has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 18 2018 Raphael Groner <projects.rg@smart.ms> - 1.1.1-6
- several fixes for Python

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
-- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Raphael Groner <projects.rg@smart.ms> - 1.1.1-2
- be more precisely about owned files

* Sun Oct 22 2017 Raphael Groner <projects.rg@smart.ms> - 1.1.1-1
- initial
