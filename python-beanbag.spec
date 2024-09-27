Name:           python-beanbag
Version:        1.9.2
Release:        34%{?dist}
Summary:        A helper module for accessing REST APIs
License:        MIT
URL:            https://github.com/ajtowns/beanbag
BuildArch:      noarch

Source0:        https://pypi.python.org/packages/source/b/beanbag/beanbag-%{version}.tar.gz
# Python 3.6 changed the way it was handling the initialization of classes in a metaclass
# thus making tests to fail. This patch addresses the issue.
# Relevant info:
# http://bugs.python.org/issue23722
# https://docs.python.org/3/reference/datamodel.html#class-object-creation
# Patch sent upstream: https://github.com/ajtowns/beanbag/pull/10
Patch0:			py36-metaclass-compatibility.patch

# pytst 5.1+
# pytest.raises no longer supports strings as the second argument
# switch to context managers
Patch1:         pytest5.1-compatibility.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-requests


%description
BeanBag is a simple module that lets you access REST APIs in an easy way. For
example:

>>> import beanbag
>>> github = beanbag.BeanBag("https://api.github.com")
>>> watchers = github.repos.ajtowns.beanbag.watchers()
>>> for w in watchers:
...     print(w["login"])

See http://beanbag.readthedocs.org/ for more information.

%package -n python3-beanbag
Summary:        A helper module for accessing REST APIs
%{?python_provide:%python_provide python3-beanbag}
Requires:  python3-requests

%description -n python3-beanbag
BeanBag is a simple module that lets you access REST APIs in an easy way. For
example:

>>> import beanbag
>>> github = beanbag.BeanBag("https://api.github.com")
>>> watchers = github.repos.ajtowns.beanbag.watchers()
>>> for w in watchers:
...     print(w["login"])
See http://beanbag.readthedocs.org/ for more information.

%prep
%autosetup -p1 -n beanbag-%{version}

# Fix compatibility with pytest 7.2.0
sed -i "s/py\.test/pytest/g" tests/test_attrdict.py tests/test_bbv1.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-beanbag
%doc README.rst
%license LICENSE
%{python3_sitelib}/beanbag*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.9.2-33
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.9.2-29
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Kevin Fenzi <kevin@scrye.com> - 1.9.2-27
- Fix compatibility with pytest 7.2.0.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.2-25
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.2-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-20
- Fix FTBFS with pytest 5.1+
- Fixes: rhbz#1865274

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-15
- Subpackage python2-beanbag has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-10
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Ralph Bean <rbean@redhat.com> - 1.9.2-2
- Some changes during package review.

* Fri Jan 08 2016 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.9.2-1
- Initial version
