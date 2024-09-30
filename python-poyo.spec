%global pkgname poyo

Name:           python-poyo
Version:        0.5.0
Release:        16%{?dist}
Summary:        A lightweight YAML Parser for Python

License:        MIT
URL:            https://github.com/hackebrot/poyo
Source0:        https://github.com/hackebrot/%{pkgname}/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A lightweight YAML Parser for Python

Please note that Poyo supports only a chosen subset of the YAML format.

It can only read but not write and is not compatible with JSON.

Poyo does not allow deserialization of arbitrary Python objects. Supported
types are str, bool, int, float, NoneType as well as dict and list values.
Please see the examples below to get an idea of what Poyo understands.

%package     -n python3-%{pkgname}
Summary:        %{summary}
%description -n python3-%{pkgname}
A lightweight YAML Parser for Python

Please note that Poyo supports only a chosen subset of the YAML format.

It can only read but not write and is not compatible with JSON.

Poyo does not allow deserialization of arbitrary Python objects. Supported
types are str, bool, int, float, NoneType as well as dict and list values.
Please see the examples below to get an idea of what Poyo understands.

%prep
%autosetup -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build

%{pyproject_wheel}

%install

%{pyproject_install}

%check

%{__python3} setup.py test

%files -n python3-%{pkgname}
%license LICENSE
%doc *.md
%{python3_sitelib}/*


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.0-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.0-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.0-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.10

* Fri May 07 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.5.0-3
- Added missing dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.5.0-1
- Update to version 0.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Subpackage python2-poyo has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.7

* Tue Mar  6 2018 Brett Lentz <brett.lentz@gmail.com> - 0.4.1-1
- initial package
