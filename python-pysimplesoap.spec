%global pypi_name PySimpleSOAP
%global rpmname pysimplesoap

Name:           python-%{rpmname}
Version:        1.16.2
Release:        23%{?dist}
Summary:        Python simple and lightweight SOAP Library

License:        LGPL-3.0-or-later
URL:            https://github.com/pysimplesoap/pysimplesoap
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/pysimplesoap/pysimplesoap/master/license.txt
Patch0:         httplib2.patch 
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Python simple and lightweight SOAP library for client and
server web services interfaces, aimed to be as small and easy
as possible, supporting most common functionality. 

%package -n     python3-%{rpmname}
Summary:        %{summary}
%py_provides    python3-%{pypi_name}

%description -n python3-%{rpmname}
Python simple and lightweight SOAP library for client and 
server web services interfaces, aimed to be as small and easy 
as possible, supporting most common functionality. 

%prep
%autosetup -n %{pypi_name}-%{version} -p1
for lib in pysimplesoap/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pysimplesoap

%check
%pyproject_check_import

%files -n python3-%{rpmname} -f %{pyproject_files}
%license license.txt

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.16.2-22
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.16.2-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.16.2-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.16.2-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.16.2-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.16.2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-6
- Apply https://github.com/pysimplesoap/pysimplesoap/pull/170

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.2-4
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-3
- Add license, fix some other errors

* Sun Aug 11 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-2
- Ensure there are no rpmlint warnings

* Sat Aug 10 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-1
- Initial package.
