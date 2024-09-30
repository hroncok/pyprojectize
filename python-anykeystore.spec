%global modname anykeystore

Name:           python-%{modname}
Version:        0.2
Release:        42%{?dist}
Summary:        A key-value store supporting multiple backends
License:        MIT
URL:            http://pypi.python.org/pypi/%{modname}
Source0:        http://pypi.python.org/packages/source/a/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         python-anykeystore-use-unittest1.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Optional backends for the tests
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pymongo
BuildRequires:  python3-redis
#BuildRequires:  python3-memcached  # Not yet packaged..

%global _description\
A generic interface wrapping multiple different backends to provide a\
consistent key-value storage API. This library is intended to be used by\
other libraries that require some form of generic storage.

%description %_description

%package -n python3-%{modname}
Summary:        A key-value store supporting multiple backends

%description -n python3-%{modname}
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

%prep
%setup -q -n %{modname}-%{version}
%patch -P0 -p1

# Use the standard library instead of a backport
sed -i -e 's/^import mock/from unittest import mock/' \
       -e 's/^from mock import /from unittest.mock import /' \
    %{modname}/tests/test_backends/*

rm -rf %{modname}/tests/integration/tests.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst LICENSE.txt

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.2-41
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.2-37
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.2-34
- Rebuilt for Python 3.11

* Thu Feb 24 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.2-33
- Utilize pytest instead of the deprecated nose test runner
- Use mock from the standard library

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2-30
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2-27
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-25
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-24
- Subpackage python2-anykeystore has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-23
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2-19
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2-18
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-16
- Python 2 binary package renamed to python2-anykeystore
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-13
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Ralph Bean <rbean@redhat.com> - 0.2-8
- Python3 subpackage added.

* Thu Jun 12 2014 Ralph Bean <rbean@redhat.com> - 0.2-7
- Modernized python2 macros.
- Patched out use of unittest1 which fails oddly in rawhide.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 09 2012 Ralph Bean <rbean@redhat.com> - 0.2-3
- Remove failing test for el6
* Fri Nov 09 2012 Ralph Bean <rbean@redhat.com> - 0.2-2
- Removed CHANGES.txt since its of size zero
* Thu Nov 08 2012 Ralph Bean <rbean@redhat.com> - 0.2-1
- initial package for Fedora
