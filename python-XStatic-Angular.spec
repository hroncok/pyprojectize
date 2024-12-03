%global pypi_name XStatic-Angular

Name:           python-%{pypi_name}
Version:        1.5.8.0
Release:        27%{?dist}
Epoch:          1
Summary:        Angular (XStatic packaging standard)

License:        MIT
URL:            http://angularjs.org
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Patch0001:      0001-fix-angular.merge-do-not-merge-__proto__-property.patch

%description
Angular JavaScript library packaged for
setuptools (easy_install) / pip.

This package is intended to be used by
**any** project that needs these files.

It intentionally does **not** provide
any extra code except some metadata
**nor** has any extra requirements. You MAY
use some minimal support code from
the XStatic base package, if you like.

%package -n python3-%{pypi_name}
Summary:        Angular (XStatic packaging standard)

BuildRequires:  python3-devel
BuildRequires:  web-assets-devel

Requires: python3-XStatic
Requires: XStatic-Angular-common = %{epoch}:%{version}-%{release}


%description -n python3-%{pypi_name}
Angular JavaScript library packaged for
setuptools (easy_install) / pip.

This package is intended to be used by
**any** project that needs these files.

It intentionally does **not** provide
any extra code except some metadata
**nor** has any extra requirements. You MAY
use some minimal support code from
the XStatic base package, if you like.

%package -n XStatic-Angular-common
Requires: web-assets-filesystem
Summary:     Common files for XStatic-Angular (XStatic packaging standard)
%description -n XStatic-Angular-common
Common files for XStatic-Angular (XStatic packaging standard)

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular'|" xstatic/pkg/angular/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
# due
# https://bitbucket.org/thomaswaldmann/xstatic/issue/2/
# this package can not be built with python-XStatic installed.
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files xstatic

# move angular.js to appropriate _jsdir
mkdir -p %{buildroot}/%{_jsdir}/angular
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular/data/angular* %{buildroot}/%{_jsdir}/angular


%check
%pyproject_check_import


%files -n XStatic-Angular-common
%{_jsdir}/angular


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt
%{python3_sitelib}/XStatic_Angular-%{version}-py%{python3_version}-nspkg.pth


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:1.5.8.0-26
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1:1.5.8.0-22
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Lon Hohberger <lon@redhat.com> - 1:1.5.8.0-20
- Backport fix for CVE-2019-10768

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:1.5.8.0-18
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:1.5.8.0-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:1.5.8.0-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.5.8.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.5.8.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.5.8.0-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.5.8.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb  6 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1:1.5.8.0-1
- Upstream 1.5.8.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:1.3.7.0-10
- Rebuild for Python 3.6

* Sun Sep 04 2016 Matthias Runge <mrunge@redhat.com> -1:1.3.7.0-9
- fix dependencies with -common

* Tue Aug 30 2016 Matthias Runge <mrunge@redhat.com> -1:1.3.7.0-8
- provide a python3 package (rhbz#1365037)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.7.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Matthias Runge <mrunge@redhat.com> - 1:1.3.7.0-4
- provide obsoleted python-XStatic-Angular-Cookies (rhbz#1210692)

* Thu Feb 12 2015 Matthias Runge <mrunge@redhat.com> - 1:1.3.7.0-3
- introduce epoch due to bump in f22

* Thu Jan 15 2015 Matthias Runge <mrunge@redhat.com> - 1.3.7.0-2
- include the rest of additional angular files
- obsolete python-XStatic-Angular-Cookies

* Mon Jan 12 2015 Matthias Runge <mrunge@redhat.com> - 1.3.7.0-1
- update to 1.3.7.0

* Wed Aug 27 2014 Matthias Runge <mrunge@redhat.com> - 1.2.1.1-1
- Initial package.
