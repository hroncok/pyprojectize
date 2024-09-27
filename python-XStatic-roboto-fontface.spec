%global pypi_name XStatic-roboto-fontface

Name:           python-%{pypi_name}
Version:        0.5.0.0
Release:        30%{?dist}
Summary:        roboto-fontface (XStatic packaging standard)

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/choffmeister/roboto-fontface-bower
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
XStatic-roboto-fontface is a roboto-fontface JavaScript
library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.
It intentionally does not provide any extra code except some metadata nor
has any extra requirements.

%package -n roboto-fontface-common
Summary:    roboto-fontface commons
BuildRequires:  web-assets-devel

Requires:       web-assets-filesystem

%description -n roboto-fontface-common
Common roboto-fontface static content (font, CSS and SCSS)

# TODO
# use google-roboto-font instead of roboto-fontface-fonts
# currently google-roboto-font does not have .eot, .svg and .woff files
# reference: https://bugzilla.redhat.com/show_bug.cgi?id=1261022

%package -n roboto-fontface-fonts
Summary:    roboto-fontface fonts
BuildRequires:  fontpackages-filesystem

Requires:       fontpackages-filesystem

%description -n roboto-fontface-fonts
roboto-fontface fonts

#python3 packaging
%package -n     python3-%{pypi_name}
Summary:        roboto-fontface (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel

Requires:    python3-XStatic
Requires:    roboto-fontface-common = %{version}-%{release}
Requires:    roboto-fontface-fonts  = %{version}-%{release}

%description -n python3-%{pypi_name}
XStatic-roboto-fontface is a roboto-fontface JavaScript
library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.
It intentionally does not provide any extra code except some metadata nor
has any extra requirements.

%prep
%setup -q -n %{pypi_name}-%{version}

sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/roboto_fontface'|" xstatic/pkg/roboto_fontface/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%{__python3} setup.py build

%install
%pyproject_install

# Move fonts to the right directory
mkdir -p %{buildroot}/%{_datadir}/fonts/roboto_fontface
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/roboto_fontface/data/fonts/* %{buildroot}/%{_datadir}/fonts/roboto_fontface

# Fix shebang issues
for file in %{buildroot}/%{_datadir}/fonts/roboto_fontface/roboto/*.svg; do
 chmod -x $file
done

# Move static files
mkdir -p %{buildroot}/%{_jsdir}/roboto_fontface/css
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/roboto_fontface/data/css/* %{buildroot}/%{_jsdir}/roboto_fontface/css
rm -rf %{buildroot}/%{python3_sitelib}/xstatic/pkg/roboto_fontface/data
# link fonts
mkdir %{buildroot}/%{_jsdir}/roboto_fontface/fonts
pushd %{buildroot}/%{_jsdir}/roboto_fontface/fonts
ln -s ../../../fonts/roboto_fontface/* .
popd

%files -n roboto-fontface-common
%doc README.txt
%{_jsdir}/roboto_fontface

%files -n roboto-fontface-fonts
%doc README.txt
%{_datadir}/fonts/roboto_fontface

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/roboto_fontface
%{python3_sitelib}/XStatic_roboto_fontface-%{version}.dist-info
%{python3_sitelib}/XStatic_roboto_fontface-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0.0-30
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.0.0-28
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.0.0-24
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0.0-21
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0.0-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0.0-9
- Subpackage python2-XStatic-roboto-fontface has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.0-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.5.0.0-1
- Upstream 0.5.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3.2-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 12 2016 Matthias Runge <mrunge@redhat.com> - 0.4.3.2-8
- fix font location for xstatic package (rhbz#1333600)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 22 2015 Matthias Runge <mrunge@redhat.com> - 0.4.3.2-4
- fix location of css/scss files for roboto

* Tue Sep 08 2015 Chandan Kumar <chkumar246@gmail.com> - 0.4.3.2-3
- Fixed shebang rpmlint issue in .svg files
- use roboto-fontface-fonts due to bug in google-roboto-fonts

* Tue Sep 08 2015 Chandan Kumar <chkumar246@gmail.com> - 0.4.3.2-2
- use google-roboto-fonts and google-roboto-commons

* Sat Sep 05 2015 chandankumar <chkumar246@gmail.com> - 0.4.3.2-1
- Initial package.
