%global pypi_name django-crispy-forms

Name:           python-%{pypi_name}
Version:        1.14.0
Release:        9%{?dist}
Summary:        Best way to have Django DRY forms
License:        MIT
URL:            https://github.com/django-crispy-forms/django-crispy-forms
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-django
Requires:	python3-coverage
Requires:	python3-pytest-cov
Requires:	python3-wheel
Requires:	python3-twine
Requires:	python3-pytest

%description
The best way to have Django DRY forms. Build programmatic reusable layouts out
of components, having full control of the rendered HTML without writing HTML in
templates. All this without breaking the standard way of doing things in Django,
so it plays nice with any other form application.

%package -n python3-%{pypi_name}
Summary: %{summary} - Python 3 version
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The best way to have Django DRY forms. Build programmatic reusable layouts out
of components, having full control of the rendered HTML without writing HTML in
templates. All this without breaking the standard way of doing things in Django,
so it plays nice with any other form application.

%prep
%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
 
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/crispy_forms/
%{python3_sitelib}/django_crispy_forms.dist-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.14.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.14.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Luis Bazan <lbazan@fedoraproject.org> - 1.14.0-1
- New upstream

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.13.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Luis Bazan <lbazan@fedoraproject.org> - 1.13.0-1
- New upstream

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Second attempt - Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.11.2-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Luis Bazan <lbazan@fedoraproject.org> - 1.11.2-1
- New Upstream version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Sat Aug 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.9.2-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.9.1-1
- New upstream version

* Tue Mar 03 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.9.0-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.8.1-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.7.2-2
- Fix comments in BZ#1597397

* Mon Jul 02 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.7.2-1
- New upstream
