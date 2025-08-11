%global pypi_name txaio

Name:           python-%{pypi_name}
Version:        23.1.1
Release:        8%{?dist}
Summary:        Compatibility API between asyncio/Twisted/Trollius

License:        MIT
URL:            https://txaio.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/t/txaio/txaio-%{version}.tar.gz
# The test_utils module can no longer be imported from asyncio
# and is undocumented intentionaly because it's private.
# This is a hack that calls stop on the loop soon after calling run_forever().
Patch2:         run_once.patch
BuildArch:      noarch

%description
Helper library for writing code that runs unmodified on both Twisted and
asyncio.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-six
BuildRequires:  python3-test
BuildRequires:  python3-enchant >= 1.6.6
Requires:       python3-six

%description -n python3-%{pypi_name}
Helper library for writing code that runs unmodified on both Twisted and
asyncio.

%package doc
Summary:        Documentation for txaio

BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
Requires:       js-jquery

%description doc
Helper library for writing code that runs unmodified on both Twisted and
asyncio. Documentation in html format.

%prep
%setup -qn %{pypi_name}-%{version}
%patch -P2 -p1
# Remove upstream's egg-info
# README is just a symlink to index.rst. Using this file as README
rm docs/index.rst
cp -a README.rst docs/index.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Build documentation
cd docs && make html
# Remove buildinfo
rm -rf _build/html/.buildinfo
# Unbundle jquery
rm -f  _build/html/_static/jquery.js
ln -s /usr/share/javascript/jquery/latest/jquery.min.js _build/html/_static/jquery.js

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest -v test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 23.1.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 23.1.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Julien Enselme <jujens@jujens.eu> - 23.1.1-1
- Update to 23.1.1

* Tue Jan 10 2023 Julien Enselme <jujens@jujens.eu> - 22.2.1-4
- Remove build dep on python3-mock:
  not needed causes issues when building for EPEL9.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 22.2.1-2
- Rebuilt for Python 3.11

* Fri Mar 04 2022 Fabian Affolter <mail@fabian-affolter.ch> - 22.2.1-1
- Update to latest upstream release 22.2.1 (closes rhbz#2057646)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.2.1-2
- Rebuilt for Python 3.10

* Mon Feb 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.2.1-1
- Update to latest upstream release 21.2.1 (#1909406)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 20.12.1-1
- Update to latest upstream release 20.12.1 (#1909406)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Julien Enselme <jujens@jujens.eu> - 20.4.1-1
- Update to 20.4.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 18.8.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Orion Poplawski <orion@nwra.com> - 18.8.1-7
- Drop BR on python3-pep8
- Use EL8 compatible coverage execution
- Add BR python3-test for EL8 compatibility

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 18.8.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 18.8.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 18.8.1-3
- Fix tests after pytest update.

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 18.8.1-2
- Remove Python 2 subpackage.

* Wed Feb 20 2019 Yatin Karel <ykarel@redhat.com> - 18.8.1-1
- Update to 18.8.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 18.7.1-1
- Update to 18.7.1

* Wed Aug 01 2018 Marcel Plch <mplch@redhat.com> - 2.10.0-5
- Patch for Python 3.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.10.0-3
- Rebuilt for Python 3.7

* Tue May 08 2018 Miro Hrončok <mhroncok@redhat.com> - 2.10.0-2
- Remove unused build dependency on tox

* Sun Apr 15 2018 Julien Enselme <jujens@jujens.eu> - 2.10.0-1
- Update to 2.10.0

* Tue Mar 06 2018 Julien Enselme <jujens@jujens.eu> - 2.9.0-1
- Update to 2.9.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.8.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Sep 06 2017 Julien Enselme <jujens@jujens.eu> - 2.8.2-1
- Update to 2.8.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Julien Enselme <jujens@jujens.eu> - 2.8.1-1
- Update to 2.8.1

* Sat Jun 10 2017 Julien Enselme <jujens@jujens.eu> - 2.8.0-1
- Update to 2.8.0

* Sun May 07 2017 Julien Enselme <jujens@jujens.eu> - 2.7.1-1
- Update to 2.7.1

* Tue Apr 18 2017 Julien Enselme <jujens@jujens.eu> - 2.7.0-1
- Update to 2.7.0

* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 2.6.2-1
- Update to 2.6.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Julien Enselme <jujens@jujens.eu> - 2.5.2-1
- Update to 2.5.2
- Skip failing tests on Python 3.6

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-3
- Rebuild for Python 3.6

* Sat Oct 01 2016 Julien Enselme <jujens@jujens.eu> - 2.5.1-2
- Fix tests for pytest3
- Correct build of documentation with sphinx 1.4.8

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Julien Enselme <jujens@jujens.eu> - 2.5.1-1
- Update to 2.5.1

* Sat Feb 27 2016 Julien Enselme <jujens@jujens.eu> - 2.2.1-1
- Update to 2.2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 6 2015 Julien Enselme <jujens@jujens.eu> - 2.0.4-2
- Rebuilt for python 3.5

* Sat Oct 17 2015 Julien Enselme <jujens@jujens.eu> - 2.0.4-1
- Update 2.0.4

* Mon Sep 28 2015 Julien Enselme <jujens@jujens.eu> - 2.0.2-1
- Update to 2.0.2

* Sat Aug 15 2015 Julien Enselme <jujens@jujens.eu> - 1.0.3-2
- Move python2 package in its own subpackage

* Sat Aug 15 2015 Julien Enselme <jujens@jujens.eu> - 1.0.3-1
- Update to 1.0.3

* Sat Aug 8 2015 Julien Enselme <jujens@jujens.eu> - 1.0.2-1
- Update to 1.0.2
- Use %%py2_build, %%py3_build, %%py2_install and %%py2_install

* Tue Aug 4 2015 Julien Enselme <jujens@jujens.eu> - 1.0.0-4
- Correct sphinx theme name in BuildRequires

* Thu Jul 30 2015 Julien Enselme <jujens@jujens.eu> - 1.0.0-3
- Add provides for python2-txaio
- Remove usage of python2 and python3 dirs
- Unbundle jquery
- Don't remove _sources of documentation

* Fri Jul 24 2015 Julien Enselme <jujens@jujens.eu> - 1.0.0-2
- Remove %%py3dir macro
- Add CFLAGS in %%build

* Sat Jul 18 2015 Julien Enselme <jujens@jujens.eu> - 1.0.0-1
- Initial packaging
