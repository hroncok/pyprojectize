%global pypi_name XStatic-Bootstrap-SCSS

Name:           python-%{pypi_name}
Version:        3.3.7.1
Release:        26%{?dist}
Summary:        Bootstrap-SCSS (XStatic packaging standard)

License:        MIT
URL:            http://getbootstrap.org/
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        halflings-license.eml
BuildArch:      noarch

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

Requires:       python3-XStatic
Requires:       xstatic-bootstrap-scss-common


%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%package -n xstatic-bootstrap-scss-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-bootstrap-scss-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep
%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/bootstrap_scss'|" xstatic/pkg/bootstrap_scss/__init__.py

# Include email identifying the license for the Glyphicons Halflings font
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xstatic

mkdir -p %{buildroot}%{_jsdir}/bootstrap_scss
mv %{buildroot}%{python3_sitelib}/xstatic/pkg/bootstrap_scss/data/* %{buildroot}%{_jsdir}/bootstrap_scss
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/bootstrap_scss/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/bootstrap_scss/js/*.js
chmod 644 %{buildroot}%{_jsdir}/bootstrap_scss/js/bootstrap/*.js

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt
%{python3_sitelib}/XStatic_Bootstrap_SCSS-%{version}-py%{python3_version}-nspkg.pth

%files -n xstatic-bootstrap-scss-common
%doc README.txt
%license halflings-license.eml
%{_jsdir}/bootstrap_scss

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.7.1-25
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.3.7.1-21
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.7.1-18
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.7.1-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.7.1-6
- Subpackage python2-XStatic-Bootstrap-SCSS has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb  6 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 3.3.7.1-1
- Upstream 3.3.7.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.0.0-7
- Rebuild for Python 3.6

* Thu Nov 17 2016 Stephen Gallagher <sgallagh@redhat.com> - 3.2.0.0-6
- Include license reference for bundled Glyphicons Halfling font

* Wed Oct 12 2016 Jan Beran <jberan@redhat.com> - 3.2.0.0-5
- Provides a Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Matthias Runge <mrunge@redhat.com> - 3.2.0.0-1
- Initial package (rhbz#1148956).

