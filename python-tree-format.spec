%global pkgname tree-format
%global commit 4c6de1074d96129b7e03eecdf42fac2cde3b5151
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pkgname}
Version:        0.1.2
Release:        25%{?dist}
Summary:        Python library to generate nicely formatted trees, like the UNIX tree command
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/jml/tree-format
Source0:        https://github.com/jml/%{pkgname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         version.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-testtools

%description
Python library to generate nicely formatted trees, like the UNIX `tree` command

%package     -n python3-%{pkgname}
Summary:        %{summary}
%description -n python3-%{pkgname}
Python library to generate nicely formatted trees, like the UNIX `tree` command

%prep
%autosetup -n %{pkgname}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files tree_format

%check
%{__python3} setup.py test

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
# TODO this is listed as 0.1.0, but our %%{version} is 0.1.2 :(

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.2-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.2-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.2-19
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.1.2-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.1.2-8
- Fixing the package version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-4
- Subpackage python2-tree-format has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.7

* Thu Mar  1 2018 Brett Lentz <brett.lentz@gmail.com> - 0.1.2-1
- initial package
