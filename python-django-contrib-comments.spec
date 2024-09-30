# Created by pyp2rpm-3.3.2
%global pypi_name django-contrib-comments

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        15%{?dist}
Summary:        The code formerly known as django.contrib.comments

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/django/django-contrib-comments
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(django) >= 1.11

%description
Django "excontrib" Comments Django used to include a comments framework; since
Django 1.6 it's been separated to a separate project. This is that project.This
framework can be used to attach comments to any model, so you can use it for
comments on blog entries, photos, book chapters, or anything else.For details,
consult the documentation.

Documentation: https://django-contrib-comments.readthedocs.io/en/latest/

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:       python3dist(django) >= 1.11

%description -n python3-%{pypi_name}
Django "excontrib" Comments Django used to include a comments framework; since
Django 1.6 it's been separated to a separate project. This is that project.This
framework can be used to attach comments to any model, so you can use it for
comments on blog entries, photos, book chapters, or anything else.For details,
consult the documentation.

Documentation: https://django-contrib-comments.readthedocs.io/en/latest/

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf django_contrib_comments.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files django_comments

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Chenxiong Qi <qcxhome@gmail.com> - 2.0.0-1
- Rebuilt version 2.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Chenxiong Qi <qcxhome@gmail.com> - 1.9.2-1
- Initial package.
