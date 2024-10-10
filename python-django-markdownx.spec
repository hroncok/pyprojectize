%global pypi_name django-markdownx

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        18%{?dist}
Summary:        A comprehensive Markdown editor built for Django

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/neutronX/django-markdownx
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)

%description
Django MarkdownX is a comprehensive Markdown plugin built for Django, 
the renowned high-level Python web framework, with flexibility, extensibility, 
and ease-of-use at its core.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:       python3dist(django)
Requires:       python3dist(markdown)
Requires:       python3dist(pillow)
Requires:       python3dist(pip)

%description -n python3-%{pypi_name}
Django MarkdownX is a comprehensive Markdown plugin built for Django, 
the renowned high-level Python web framework, with flexibility, extensibility, 
and ease-of-use at its core.

%prep
%autosetup -n %{pypi_name}-%{version}

rm -rf markdownx/static/.DS_Store
rm -rf markdownx/static/markdownx/.DS_Store
rm -rf markdownx/static/markdownx/admin/.DS_Store
rm -rf markdownx/templates/.DS_Store
rm -rf markdownx/templates/markdownx/.DS_Store

chmod 0644 README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%find_lang django
%files -n python3-%{pypi_name} -f django.lang
%license LICENSE
%doc README.rst
%{python3_sitelib}/markdownx
%exclude %{python3_sitelib}/markdownx/locale
%{python3_sitelib}/django_markdownx-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.1-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.0.1-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 3.0.1-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.0.1-1
- New upstream version

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.0-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.28-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.28-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Dec 11 2018 Luis Bazan <lbazan@fedoraproject.org> - 2.0.28-1
- Initial release
