%global pypi_name XStatic-JS-Yaml

Name:           python-%{pypi_name}
Version:        3.8.1.0
Release:        23%{?dist}
Summary:        JS-Yaml (XStatic packaging standard)

License:        MIT
URL:            https://github.com/nodeca/js-yaml
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JS-Yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.


%package -n xstatic-js-yaml-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-js-yaml-common
JS-Yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.


%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

Requires:       python3-XStatic
Requires:       xstatic-js-yaml-common


%description -n python3-%{pypi_name}
JS-Yaml JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Patch to use webassets directory
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/js_yaml'|" xstatic/pkg/js_yaml/__init__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files xstatic
mkdir -p %{buildroot}/%{_jsdir}/js_yaml
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/js_yaml/data/js-yaml.js %{buildroot}/%{_jsdir}/js_yaml
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/js_yaml/data/


%files -n xstatic-js-yaml-common
%doc README.txt
%{_jsdir}/js_yaml

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt
%{python3_sitelib}/XStatic_JS_Yaml-%{version}-py3.*-nspkg.pth


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.8.1.0-22
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.8.1.0-18
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.8.1.0-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.8.1.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.8.1.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.1.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.1.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 3.8.1.0-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Jul 29 2018 Miro Hrončok <mhroncok@redhat.com> - 3.8.1.0-2
- Remove bogus (build)requires from the common section
- Fix changelog entry syntax in 3.8.1.0-1

* Fri Jul 13 2018 Radomir Dopieralski <rdopiera@redhat.com> - 3.8.1.0-1
- Initial package
