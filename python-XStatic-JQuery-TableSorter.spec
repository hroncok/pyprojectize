%global pypi_name XStatic-JQuery.TableSorter
%global pkgname XStatic-JQuery-TableSorter

Name:           python-%{pkgname}
Version:        2.14.5.1
Release:        33%{?dist}
Summary:        JQuery.TableSorter (XStatic packaging standard)

License:        MIT
URL:            https://github.com/Mottie/tablesorter
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python3-%{pkgname}
Summary:        %{summary}

BuildRequires:  python3-devel

Requires:       python3-XStatic
Requires:       xstatic-jquery-tablesorter-common


%description -n python3-%{pkgname}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pkgname}.

%package -n xstatic-jquery-tablesorter-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-jquery-tablesorter-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep
%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/jquery_tablesorter'|" xstatic/pkg/jquery_tablesorter/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xstatic

mkdir -p %{buildroot}%{_jsdir}/jquery_tablesorter
mv %{buildroot}%{python3_sitelib}/xstatic/pkg/jquery_tablesorter/data/jquery.tablesorter.js %{buildroot}%{_jsdir}/jquery_tablesorter
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/jquery_tablesorter/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/jquery_tablesorter/jquery.tablesorter.js

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.txt
%{python3_sitelib}/XStatic_JQuery.TableSorter-%{version}-py%{python3_version}-nspkg.pth

%files -n xstatic-jquery-tablesorter-common
%doc README.txt
%{_jsdir}/jquery_tablesorter

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.14.5.1-32
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.14.5.1-28
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.14.5.1-25
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.14.5.1-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.14.5.1-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.14.5.1-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.14.5.1-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.14.5.1-13
- Subpackage python2-XStatic-JQuery-TableSorter has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.14.5.1-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.14.5.1-7
- Rebuild for Python 3.6

* Wed Oct 12 2016 Jan Beran <jberan@redhat.com> - 2.14.5.1-6
- Provides a Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.5.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 04 2014 Matthias Runge <mrunge@redhat.com> - 2.14.5.1-2
- change BR to python2-devel (rhbz#1134912)

* Thu Aug 28 2014 Matthias Runge <mrunge@redhat.com> - 2.14.5.1-1
- Initial package.
