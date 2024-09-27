%global pypi_name djangoql

Name:           python-%{pypi_name}
Version:        0.17.1
Release:        10%{?dist}
Summary:        DjangoQL: Advanced search language for Django

License:        MIT
URL:            https://github.com/ivelum/djangoql
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:	python3-django
BuildRequires:	pyproject-rpm-macros
%py_provides python3-%{pypi_name}

%description
Advanced search language for Django, with auto-completion.
Supports logical operators, parenthesis, table joins,
works with any Django models.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:	python3-ply

%description -n python3-%{pypi_name}
Advanced search language for Django, with auto-completion.
Supports logical operators, parenthesis, table joins,
works with any Django models.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel
%py3_build

%install
%pyproject_install
%pyproject_save_files djangoql

%check
PYTHONPATH=$(pwd) %{__python3} test_project/manage.py test core.tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.17.1-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.17.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.17.1-2
- Rebuilt for missing dep installability functional downgrade/upgrade 

* Sat Jun 25 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.17.1-1
- Update to 0.17.1 (RHBZ #1972193 and #2094383)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.14.5-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.14.5-2
- Rebuilt for Python 3.10

* Tue Apr 20 2021 Viliam Krizan <vkrizan@redhat.com> - 0.14.5-1
- New version 0.14.5 (#1947307)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Viliam Krizan <vkrizan@redhat.com> - 0.14.3-1
- New version 0.14.3 (#1908498)

* Thu Dec 03 2020 Viliam Krizan <vkrizan@redhat.com> - 0.14.2-1
- New release 0.14.2 (#1893438)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Viliam Krizan <vkrizan@redhat.com> - 0.14.0-1
- New release 0.14.0 (#1851319)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Viliam Krizan <vkrizan@redhat.com> - 0.13.1-1
- Support for Django 3.0

* Tue Sep 10 2019 Viliam Krizan <vkrizan@redhat.com> - 0.13.0-2
- New release 0.13.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Viliam Krizan <vkrizan@redhat.com> 0.12.6-1
- New release 0.12.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Viliam Krizan <vkrizan@redhat.com> 0.12.3-1
- New release 0.12.3

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12.0-2
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Nov 12 2018 Viliam Krizan <vkrizan@redhat.com> 0.12.0-1
- New release 0.12.0

* Wed Oct 24 2018 Viliam Krizan <vkrizan@redhat.com> 0.10.2-1
- New release 0.10.2
- .DS_Store files removed in upstream

* Wed Oct 24 2018 Viliam Krizan <vkrizan@redhat.com> 0.10.1-1
- New release 0.10.1
- Added tests

* Mon Oct 22 2018 Viliam Krizan <vkrizan@redhat.com> 0.10.0-1
- Initial packaging

