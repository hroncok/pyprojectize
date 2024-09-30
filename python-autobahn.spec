%global pypi_name autobahn

Name:           python-%{pypi_name}
Version:        23.6.2
Release:        8%{?dist}
Summary:        Python networking library for WebSocket and WAMP

License:        MIT
URL:            https://autobahn.readthedocs.io/en/latest/
Source0:        https://github.com/crossbario/autobahn-python/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Autobahn a networking library that is part of the Autobahn project and provides
implementations of
* The WebSocket Protocol http://tools.ietf.org/html/rfc6455_
* The Web Application Messaging Protocol (WAMP) http://wamp.ws
for Twisted and for writing servers and clients.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  %py3_dist argon2_cffi
BuildRequires:  %py3_dist cffi
BuildRequires:  %py3_dist passlib
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist pytest-asyncio
BuildRequires:  %py3_dist six
BuildRequires:  %py3_dist twisted
BuildRequires:  %py3_dist txaio
BuildRequires:  %py3_dist pynacl
%if 0%{?fedora}
BuildRequires:  %py3_dist cbor2
%endif
BuildRequires:  %py3_dist cryptography
BuildRequires:  %py3_dist hyperlink

%description -n python3-%{pypi_name}
Autobahn a networking library that is part of the Autobahn project and provides
implementations of
* The WebSocket Protocol http://tools.ietf.org/html/rfc6455_
* The Web Application Messaging Protocol (WAMP) http://wamp.ws
for Twisted and for writing servers and clients.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  %py3_dist sphinx
BuildRequires:  %py3_dist sphinx-rtd-theme
#BuildRequires:  %%py3_dist sphinxcontrib.images
%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%pyproject_extras_subpkg -n python3-%{pypi_name} twisted

%prep
%autosetup -n %{pypi_name}-python-%{version}
rm -rf %{pypi_name}.egg-info
# There is a requirement for pytest 6.2+ in pytest.ini and we don't have that yet
# it works with 6.0 just fine and the config file is not needed
rm pytest.ini
# Some packages are always outdated...
sed -i -e "s/cryptography>=3.4.6/cryptography>=3.4.2/g" setup.py
# Remove packages that will try to import attrs (optionnal deps) since in EPEL it's outdated and doesn't allow the import of attrs
# See https://www.attrs.org/en/stable/changelog.html#id11
%if ! 0%{?fedora}
rm -rf autobahn/xbr/test/*
sed -i '\@recursive-include autobahn/xbr/test/catalog/schema@d' MANIFEST.in
sed -i '\@autobahn/xbr/test/profile@d' MANIFEST.in
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
# Disable in case local builder support NVX
AUTOBAHN_USE_NVX=false %pyproject_wheel
#PYTHONPATH=${PWD} sphinx-build-3 docs html
#rm -rf html/.{doctrees,buildinfo}

%install
AUTOBAHN_USE_NVX=false %pyproject_install
%pyproject_save_files -l %{pypi_name} twisted

%check
# Ignore tests that rely on optional and not packaged deps.
k="${k-}${k+ and }not test_no_memory_arg"
k="${k-}${k+ and }not test_basic"
k="${k-}${k+ and }not test_websocket_custom_loop"
k="${k-}${k+ and }not TestSerializer"
# Skip tests failing with pytest-asyncio >= 0.23.5.post1
# https://github.com/crossbario/autobahn-python/issues/1631
# https://bugzilla.redhat.com/show_bug.cgi?id=2270130
k="${k-}${k+ and }not test_vectors"
k="${k-}${k+ and }not test_authenticator"
k="${k-}${k+ and }not test_valid"
k="${k-}${k+ and }not test_auto_ping"
k="${k-}${k+ and }not test_interpolate_server_status_template"
k="${k-}${k+ and }not test_sendClose"
%if 0%{?fedora}
USE_ASYNCIO=1 %pytest --pyargs autobahn ${k+ -k} "${k-}"
%else
k="${k-}${k+ and }not TestDecimalSerializer"
USE_ASYNCIO=1 %pytest --ignore=xbr/test --pyargs autobahn ${k+ -k} "${k-}"
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc docs README.rst
%{_bindir}/wamp
%{_bindir}/xbrnetwork
%{_bindir}/xbrnetwork-ui

%files -n python-%{pypi_name}-doc
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 23.6.2-7
- Rebuilt for Python 3.13

* Tue Mar 26 2024 Julien Enselme <jujens@jujens.eu> - 23.6.2-6
- Version Bump

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 23.6.2-2
- Rebuilt for Python 3.12

* Tue Jul 04 2023 Julien Enselme <jujens@jujens.eu> - 23.6.2
- Update to 23.6.2

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 23.1.2-3
- Rebuilt for Python 3.12

* Sun Mar 26 2023 Julien Enselme <jujens@jujens.eu> - 23.1.2-2
- Correct build on EPEL

* Wed Feb 08 2023 Julien Enselme <jujens@jujens.eu> - 23.1.2-1
- Update to 23.1.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Julien Enselme <jujens@jujens.eu> - 23.1.1-1
- Update to 23.1.1

* Wed Jan 04 2023 Orion Poplawski <orion@nwra.com> - 22.12.1-1
- Update to 22.12.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Python Maint <python-maint@redhat.com> - 21.2.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.2.2-3
- Rebuilt for Python 3.10

* Mon Mar 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.2.2-2
- Allow other cryptography releases (package is always outdated)

* Fri Feb 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.2.2-1
- Fix CVE-2020-35678 (#1911315)
- Update to new upstream release 21.2.2 (#1925733)

* Fri Feb 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.2.2-1
- Update to new upstream release 21.2.2 (#1925733)

* Sun Feb 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.2.1-1
- Update to new upstream release 21.2.1 (#1925733)

* Sun Feb 07 2021 Fabian Affolter <mail@fabian-affolter.ch> - 21.1.1-1
- Update to new upstream release 21.1.1 (#1925733)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 20.12.3-1
- Update to new upstream release 20.12.3 (#1909439)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 20.12.2-1
- Simplify and update spec file
- Update to new upstream release 20.12.2 (#1907237)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Julien Enselme <jujens@jujens.eu> - 20.7.1-1
- Update to 20.7.1

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 19.10.1-4
- Add autobahn[twisted] subpackage

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 19.10.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Orion Poplawski <orion@nwra.com> - 19.10.1-1
- Update to 19.10.1
- Drop BR on pep8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.8.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Yatin Karel <ykarel@redhat.com> - 19.8.1-1
- Update to 19.8.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.7.2-3
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Julien Enselme <jujens@jujens.eu> - 19.7.2-2
- Lower requirement on python-cryptography.

* Tue Jul 30 2019 Julien Enselme <jujens@jujens.eu> - 19.7.2-1
- Update to 19.7.2
- Skip test about random generator which can make build hang.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 19.7.1-1
- Update to 19.7.1

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 19.3.2-1
- Update to 19.3.2

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-2
- Subpackage python2-autobahn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 18.7.1-1
- Update to 18.7.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6.1-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Julien Enselme <jujens@jujens.eu> - 18.6.1-1
- Update to 18.6.1

* Sat May 12 2018 Julien Enselme <jujens@jujens.eu> - 18.5.1-1
- Update to 18.5.1

* Sun Apr 15 2018 Julien Enselme <jujens@jujens.eu> - 18.4.1-2
- Correct requires

* Sun Apr 15 2018 Julien Enselme <jujens@jujens.eu> - 18.4.1-1
- Update to 18.4.1

* Tue Mar 06 2018 Julien Enselme <jujens@jujens.eu> - 18.3.1-1
- Update to 18.3.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17.10.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Nov 06 2017 Julien Enselme <jujens@jujens.eu> - 17.10.1-1
- Update to 17.10.1
- Use %%version to get the sources

* Tue Sep 26 2017 Julien Enselme <jujens@jujens.eu> - 17.9.3-1.gitd398c4d
- Update to 17.9.3

* Thu Sep 14 2017 Julien Enselme <jujens@jujens.eu> - 17.9.2-1.git164106a
- Update to 17.9.2

* Wed Sep 06 2017 Julien Enselme <jujens@jujens.eu> - 17.9.1-1.gitb813019
- Update to 17.9.1

* Sat Aug 19 2017 Julien Enselme <jujens@jujens.eu> - 17.8.1-1.git96543dd
- Update to 17.8.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.7.1-2.git9ad7878
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Julien Enselme <jujens@jujens.eu> - 17.7.1-1.git9ad7878
- Update to 17.7.1

* Sat Jul 01 2017 Julien Enselme <jujens@jujens.eu> - 17.6.2-1.gitbc2a1b3
- Update to 17.6.2

* Sat Jun 10 2017 Julien Enselme <jujens@jujens.eu> - 17.6.1-1.gite69b314
- Update to 17.6.1

* Sun May 07 2017 Julien Enselme <jujens@jujens.eu> - 17.5.1-1.git73bcac2
- Update to 17.5.1

* Tue Apr 18 2017 Julien Enselme <jujens@jujens.eu> - 0.18.2-1.git731228a
- Update to 0.18.2

* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 0.18.1-1.gitfd7ec41
- Update to 0.18.1

* Tue Feb 28 2017 Julien Enselme <jujens@jujens.eu> - 0.17.2-1.git0eef8c7
- Update to 0.17.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2.git81d9276
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

*  Mon Dec 26 2016 Julien Enselme <jujens@jujens.eu> - 0.17.0-1.git81d9276
- Update to 0.17.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-3.gitade9eb5
- Rebuild for Python 3.6

* Sat Oct 01 2016 Julien Enselme <jujens@jujens.eu> - 0.16.0-2.gitade9eb5
- Fix tests for pytest3

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 0.16.0-1.gitade9eb5
- Update to 0.16.0

* Mon Jul 25 2016 Julien Enselme <jujens@jujens.eu> - 0.15.0-1.git43b57f8
- Update to 0.15.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2.git81f693d
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Julien Enselme <jujens@jujens.eu> - 0.14.0-1.git81f693d
- Update to 0.14.0

* Sat Feb 27 2016 Julien Enselme <jujens@jujens.eu> - 0.12.1-1.git22b1183
- Update to 0.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3.gita69e704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-2.gita69e704
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 6 2015 Julien Enselme <jujens@jujens.eu> - 0.10.7-1.gita69e7048
- Update to 0.10.7

* Sun Sep 6 2015 Julien Enselme <jujens@jujens.eu> - 0.10.6-1.gitb35d99f1
- Update to 0.10.6

* Sat Aug 15 2015 Julien Enselme <jujens@jujens.eu> - 0.10.5-1.git3fce8ac
- Update to 0.10.5.post-2

* Wed Aug 5 2015 Julien Enselme <jujens@jujens.eu> - 0.10.4-3.git29f8acc
- Build python2 and python3 in the same dir
- Update dependencies
- Put python2 package in a subpackage
- Add provides
- Correct %%files section

* Fri Jul 24 2015 Julien Enselme <jujens@jujens.eu> - 0.10.4-2.git29f8acc
- Surround doc package with if
- Remove %%py3dir macro
- Add CFLAGS in %%build

* Sat Jul 18 2015 Julien Enselme <jujens@jujens.eu> - 0.10.4-1.git29f8acc
- Initial packaging
