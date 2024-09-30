%global shortname django-ipware
Name:          python-%{shortname}
Version:       4.0.2
Release:       10%{?dist}
Summary:       A Django application to retrieve client's IP address

License:       MIT
URL:           https://github.com/un33k/%{shortname}/
Source0:       https://github.com/un33k/%{shortname}/archive/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-django

%description
A Django application to retrieve client's IP address.

%package -n python3-%{shortname}
Summary:       A Django application to retrieve client's IP address
Requires:      python3-django

%description -n python3-%{shortname}
A Django application to retrieve client's IP address.

%prep
%autosetup -n %{shortname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'django_ipware*' ipware

%check
%{__python3} manage.py test

%files -n python3-%{shortname} -f %{pyproject_files}
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.0.2-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 4.0.2-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.0.2-2
- Rebuilt for Python 3.11

* Sun Jun 12 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-2
- Review updates

* Thu Dec 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-1
- Initial package
