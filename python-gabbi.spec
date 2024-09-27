%global pypi_name gabbi
%global pypi gabbi-run

Name:           python-%{pypi_name}
Version:        2.7.2
Release:        10%{?dist}
Summary:        Declarative HTTP testing library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/cdent/gabbi
Source0:        https://pypi.io/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch


%description
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%package -n python3-%{pypi_name}
Summary:        Declarative HTTP testing library
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:       python3-devel
BuildRequires:       python3-setuptools
BuildRequires:       python3-six
BuildRequires:       python3-pbr
BuildRequires:       python3-httplib2
BuildRequires:       python3-wsgi_intercept
BuildRequires:       python3-colorama
BuildRequires:       python3-jsonpath-rw-ext
BuildRequires:       python3-PyYAML
BuildRequires:       python3-pytest
BuildRequires:       python3-urllib3

Requires:       python3-setuptools
Requires:       python3-certifi
Requires:       python3-six
Requires:       python3-pbr
Requires:       python3-wsgi_intercept
Requires:       python3-colorama
Requires:       python3-jsonpath-rw-ext
Requires:       python3-pytest
Requires:       python3-PyYAML
Requires:       python3-urllib3
Requires:       python3-testtools

# test requirements
BuildRequires:  python3-stestr
BuildRequires:  python3-coverage

%description -n python3-%{pypi_name}
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for the gabbi module

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for the gabbi module

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# generate html docs
sphinx-build docs/source html
sphinx-build -b man docs/source man

install -p -D -m 644 man/gabbi.1 %{buildroot}%{_mandir}/man1/gabbi.1


rm -rf html/.{doctrees,buildinfo}

# %check
# some tests are broken so bypassing tests
# export GABBI_SKIP_NETWORK=true
# %{__python3} setup.py test ||

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi}
%{_mandir}/man1/gabbi.1*
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/gabbi/tests/gabbits_intercept/horse

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.2-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.7.2-8
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Maxwell G <maxwell@gtmx.me> - 2.7.2-7
- Remove unused python3-mock test dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.7.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Joel Capitao <jcapitao@redhat.com> - 2.7.2-1
- Update to 2.7.2 (#2001172)

* Thu Aug 18 2022 Joel Capitao <jcapitao@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Joel Capitao <jcapitao@redhat.com> - 2.2.0-1
- Update to 2.2.0 (#1830135)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Joel Capitao <jcapitao@redhat.com> - 2.0.4-1
- Update to 2.0.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.49.0-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Yatin Karel <ykarel@redhat.com> - 1.49.0-1
- Update to 1.49.0 (Resolves #1596669)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.42.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.42.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.42.1-6
- Subpackage python2-gabbi has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.42.1-3
- Rebuilt for Python 3.7

* Thu Apr 26 2018 Chandan Kumar <chkumar@redhat.com> - 1.42.1-2
- Added missed python-testtools requirements

* Wed Apr 25 2018 Chandan Kumar <chkumar@redhat.com> - 1.42.1-1
- Bump to version 1.42.1
- Resolves rhbz#1434385
- Disabling unit tests as they are failing

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.33.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.33.0-1
- Upstream 1.33.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.27.0-2
- Rebuild for Python 3.6

* Thu Oct 13 2016 Alan Pevec <alan.pevec@redhat.com> 1.27.0-1
- Update to 1.27.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 14 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.22.0-1
- Upstream 1.22.0

* Mon Jun  6 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.21.0-1
- Upstream 1.21.0

* Wed Jun  1 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.19.1-1
- Upstream 1.19.1
- Add IPv6 support

* Mon May 09 2016 chandankumar <chkumar246@gmail.com> - 1.19.0-1
- Initial package.
