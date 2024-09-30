%global srcname pytest-shutil
%global sum A goodie-bag of unix shell and environment tools for py.test

Name:           python-%{srcname}
Version:        1.7.0
Release:        26%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Patch1:         https://github.com/manahl/pytest-plugins/pull/144.patch
Patch2:         https://github.com/manahl/pytest-plugins/pull/217.patch
Patch3:         https://github.com/man-group/pytest-plugins/pull/219.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-mock
BuildRequires:  python3-path
BuildRequires:  python3-execnet
BuildRequires:  python3-termcolor

%description
This library is a goodie-bag of Unix shell and 
environment management tools for automated tests.

%package -n python3-%{srcname}
Summary:        %{sum}
Recommends:     %{py3_dist termcolor}

%description -n python3-%{srcname}
This library is a goodie-bag of Unix shell and 
environment management tools for automated tests.

%prep
%autosetup -n %{srcname}-%{version} -p2

# https://bugzilla.redhat.com/show_bug.cgi?id=1702355
sed -i "/'termcolor'/d" setup.py

# Upstream pins pytest to older than 4.0.0 until they finish cleaning up deprecications. 
# However, we have no choice and all the tests do pass fine, so we unpin here.
sed -i -e 's|pytest<4.0.0|pytest|' setup.py

# This is not needed when building from the sdist
sed -i -e '/setuptools-git/d' common_setup.py

# path.py changed names to path a long time ago. Since we always use newer than python3.5
# we can just change it here to always use path. 
# https://bugzilla.redhat.com/show_bug.cgi?id=1702355
sed -i -e 's|path.py|path|' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# test_pretty_formatter requires termcolor
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest

%files -n python3-%{srcname}
%doc README.md CHANGES.md
%{python3_sitelib}/*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7.0-25
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Michael J Gruber <mjg@fedoraproject.org> - 1.7.0-21
- Adjust to Python 3.12

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.7.0-20
- Rebuilt for Python 3.12

* Sun May 13 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.7.0-19
- Add patch for new termcolor

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.7.0-16
- Rebuilt for Python 3.11

* Mon Apr 11 2022 Kevin Fenzi <kevin@scrye.com> - 1.7.0-15
- Fix python-path dependence. Fixes rhbz#2071948

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-10
- Don't BuildRequire setuptools_git

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-5
- Drop requirement on contextlib2, contextlib is in the Python 3 stdlib

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-2
- Drop python2 subpackages. Fixes bug #1723588

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-1
- Update to 1.7.0. Fixes bug #1714449

* Tue Apr 23 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Only recommend termcolor (#1702355)

* Sun Apr 14 2019 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0. Fixes bug #1697356

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.6-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-2
- Add Requires for pytest

* Wed Jul 26 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-1
- Initial version. 
