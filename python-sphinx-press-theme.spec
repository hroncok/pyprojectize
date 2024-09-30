%global pypi_name sphinx-press-theme

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        20%{?dist}
Summary:        A Sphinx-doc theme based on Vuepress

# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://schettino72.github.io/sphinx_press_site/
Source0:        %{pypi_source sphinx_press_theme}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A modern responsive theme for python's Sphinx documentation generator.
See it in action on Press Theme own website.
This theme is based on VuePress.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A modern responsive theme for python's Sphinx documentation generator.
See it in action on Press Theme own website.
This theme is based on VuePress.


%prep
%autosetup -n sphinx_press_theme-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/sphinx_press_theme
%{python3_sitelib}/sphinx_press_theme-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-20
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.1-18
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.1-14
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.1-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.1-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-5
- Rebuilt for Python 3.9

* Fri Mar 20 2020 José Matos <jamatos@fedoraproject.org> - 0.5.1-4
- Add pypi_source by setting the appropriate argument.

* Fri Mar 20 2020 José Matos <jamatos@fedoraproject.org> - 0.5.1-3
- It is not possible to use pypi_source because of the change between - and _ in the name.
- Add BSD to the license since some of the files are under that license.

* Thu Mar 19 2020 José Matos <jamatos@fedoraproject.org> - 0.5.1-2
- Small cleanups: replace source with canonical name.
- Removed extraneous formating from description.
- Removed the Requires since they are autogenerated for python packages.

* Thu Mar 19 2020 José Abílio Matos <jamatos@fedoraproject.org> - 0.5.1-1
- Initial package.
