%global pypi_name django-health-check

Name:           python-%{pypi_name}
Version:        3.16.5
Release:        10%{?dist}
Summary:        Checks for various conditions and provides reports

License:        MIT
URL:            https://github.com/KristianOellegaard/django-health-check
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-sphinx

%global _description\
A Django application that provides health check capabilities.\
Many of these checks involve connecting to back-end services and ensuring\
basic operations are successful.

%description %_description

%package -n python3-%{pypi_name}
Summary:        %summary
Requires:       python3-django
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        Documentation for django-health-check
%description -n python-%{pypi_name}-doc
Documentation for django-health-check

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# TODO: Enable once pytest-django is packaged
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/thread/QTZIBOTA5XHNOLEF22K46XC74LZ7OQP5/
# %%check
# export DJANGO_SETTINGS_MODULE=tests.testapp.settings
# %%{__python3} -m pytest tests

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/health_check/
%{python3_sitelib}/django_health_check-*.egg-info/

%files -n python-%{pypi_name}-doc
# There is a docs directory but it is no longer included in the release tarball
# https://github.com/KristianOellegaard/django-health-check/tree/master/docs
%doc README.rst
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.16.5-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.16.5-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.16.5-2
- Rebuilt for Python 3.11

* Wed Apr 6 2022 David Moreau-Simard - 3.16.5-1
- Update to latest upstream release
- Includes fix for django 4.x (https://github.com/KristianOellegaard/django-health-check/commit/93e9cdd1e881f255166df2d1189fcae838a077a9)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.11.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 David Moreau Simard <dmsimard@redhat.com> - 3.11.0-1
- First version of the package
