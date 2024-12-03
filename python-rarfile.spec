%global pypi_name rarfile

Name:           python-%{pypi_name}
Version:        4.2
Release:        1%{?dist}
Summary:        RAR archive reader for Python

License:        ISC
URL:            https://github.com/markokr/rarfile
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Buildarch:      noarch

%description
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Sep 17 2024 Fabian Affolter <mail@fabian-affolter.ch> - 4.2-1
- Update to latest upstream release 4.2 (closes rhbz#2273019)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.1-2
- Rebuilt for Python 3.13

* Sat Feb 03 2024 Fabian Affolter <mail@fabian-affolter.ch> - 4.1-1
- Update to latest upstream release 4.1 (closes rhbz#2239354)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.0-1
- Update to latest upstream release 4.0 (rhbz#1858640)

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.3-1
- Update to latest upstream release 3.3 (rhbz#1858640)

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.1-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 16 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.1-1
- Update to latest upstream release 3.1 (rhbz#1752271)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.0-9
- Remove superfluous variable

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0-7
- Subpackage python2-rarfile has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Fabian Affolter <mail@fabian-affolter.ch> - 3.0-1
- Update to new upstream version 3.0 (rhbz#1408888)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.8-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 07 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.8-1
- Update to new upstream version 2.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015  Fabian Affolter <mail@fabian-affolter.ch> - 2.7-4
- Cleanup

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.7-1
- Initial package
