
%global upstream_name sphinxcontrib-httpdomain

Name:           python-%{upstream_name}
Version:        1.7.0
Release:        24%{?dist}
Summary:        Sphinx domain for documenting HTTP APIs
License:        BSD-2-Clause
URL:            http://packages.python.org/sphinxcontrib-httpdomain/
Source0:        https://files.pythonhosted.org/packages/source/s/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
# issue to be filed(?)
Patch4:         0004-httpdomain-bump-domain-data-version.patch
BuildArch:      noarch

%description
Using this Sphinx domain you can document your HTTP API. It includes support 
for generating documentation from Flask routing tables.

%package -n python3-%{upstream_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{upstream_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-sphinx
Requires:       python3-six

%description -n python3-%{upstream_name}
Using this Sphinx domain you can document your HTTP API. It includes support 
for generating documentation from Flask routing tables.


%prep
%setup -q -n %{upstream_name}-%{version}
%patch -P4 -p2
rm -r *.egg-info

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{upstream_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7.0-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 10 2023 Karolina Surma <ksurma@redhat.com> - 1.7.0-20
- Declare the license as an SPDX expression

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.7.0-18
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.0-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1.7.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Subpackage python2-sphinxcontrib-httpdomain has been removed
  See https://fedoraproject.org/wiki/Changes/Sphinx2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Dan Callaghan <dcallagh@redhat.com> - 1.7.0-1
- upstream release 1.7.0: https://sphinxcontrib-httpdomain.readthedocs.io/en/stable/#version-1-7-0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-2
- Rebuilt for Python 3.7

* Mon Mar 05 2018 Dan Callaghan <dcallagh@redhat.com> - 1.6.1-1
- Update to 1.6.1 bug fix release (RHBZ#1551209)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Dan Callaghan <dcallagh@redhat.com> - 1.6.0-1
- Update to 1.6.0 bug fix release (RHBZ#1534132)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Dan Callaghan <dcallagh@redhat.com> - 1.5.0-4
- fix for Sphinx 1.6 compatibility (RHBZ#1473447)

* Fri Jun 23 2017 Dan Callaghan <dcallagh@redhat.com> - 1.5.0-3
- added Python 3 subpackage (RHBZ#1459474)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Dan Callaghan <dcallagh@redhat.com> - 1.5.0-1
- upstream release 1.5.0: http://pythonhosted.org/sphinxcontrib-httpdomain/#version-1-5-0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Dan Callaghan <dcallagh@redhat.com> - 1.4.0-1
- upstream release 1.4.0: http://pythonhosted.org/sphinxcontrib-httpdomain/#version-1-4-0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Dan Callaghan <dcallagh@redhat.com> - 1.3.0-1
- upstream release 1.3.0: http://pythonhosted.org/sphinxcontrib-httpdomain/#version-1-3-0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 11 2014 Dan Callaghan <dcallagh@redhat.com> - 1.1.8-5
- really fix sphinx requirement

* Mon Feb 10 2014 Pádraig Brady <pbrady@redhat.com> - 1.1.8-4
- fix sphinx requirement on RHEL 7

* Wed Oct 09 2013 Dan Callaghan <dcallagh@redhat.com> - 1.1.8-3
- require python-sphinx10 on EPEL

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Dan Callaghan <dcallagh@redhat.com> - 1.1.8-1
- new upstream release 1.1.8
- require python-sphinx (except on EPEL5/6)

* Mon Mar 04 2013 Dan Callaghan <dcallagh@redhat.com> - 1.1.7-2
- support EPEL5 and EPEL6

* Mon Feb 11 2013 Dan Callaghan <dcallagh@redhat.com> - 1.1.7-1
- initial version
