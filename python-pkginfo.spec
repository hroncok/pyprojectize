%global pypi_name pkginfo

%global common_description %{expand:
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distribution (an sdist) or a binary distribution
(e.g., created by running bdist_egg). It can also query the EGG-INFO directory
of an installed distribution, and the *.egg-info stored in a "development
checkout" (e.g, created by running setup.py develop).}

Name:           python-%{pypi_name}
Summary:        Query metadata from sdists / bdists / installed packages
Version:        1.10.0
Release:        3%{?dist}
License:        MIT

URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(wheel)

%description %{common_description}


%package -n python3-%{pypi_name}
Summary:        Query metadata from sdists / bdists / installed packages
Requires:       python3-setuptools

%description -n python3-%{pypi_name} %{common_description}


%package        doc
Summary:        Documentation for python-%{pypi_name}

%description    doc %{common_description}
This package contains the documentation.


%prep
%autosetup -n %{pypi_name}-%{version} -p1

# don't ship internal test subpackage
sed -i "s/, 'pkginfo.tests'//g" setup.py



%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import

%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt CHANGES.txt

%{_bindir}/pkginfo


%files -n python-%{pypi_name}-doc
%license LICENSE.txt
%doc html


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.13

* Tue Mar 12 2024 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.10.0-1
- Update to 1.10.0
- Fixes: rhbz#2267537

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.9.6-2
- Rebuilt for Python 3.12

* Wed Jan 25 2023 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.6-4
- Update to latest upstream release 1.9.6 (closes rhbz#2157943)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.9.2-1
- Update to 1.9.2
- Fixes: rhbz#2149410

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.8.3-1
- Update to 1.8.3
- Fixes rhbz#2094970

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.8.2-4
- Rebuilt for Python 3.11

* Mon Apr 25 2022 Major Hayden <major@mhtx.net> - 1.8.2-3
- Replace nose with pytest for easier EPEL 9 backports.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.7.1-1
- Update to 1.7.1
- Fixes rhbz#1889797

* Wed Jun 23 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.7.0-1
- Update to 1.7.0
- patch to add compatibility with Sphinx 4
- Fixes rhbz#1977625
- Fixes rhbz#1889797

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.0.1-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0.1-5
- Revert previous changes

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0.1-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.0.1-1
- Update to version 1.5.0.1.

* Mon Sep 23 2019 Fabio Valentini <decathorpe@gmail.com> - 1.4.2-7
- Drop python2-pkginfo and versioned symlinks for the binary.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.7

* Sat Mar 24 2018 Jeremy Cline <jeremy@jcline.org> - 1.4.2-1
- Update to latest upstream
- License change to MIT

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuild for Python 3.6

* Wed Jul 20 2016 Jeremy Cline <jeremy@jcline.org> - 1.3.2-3
- Remove hard-coded Python y release versions in /usr/bin entries

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.3.2-1
- Initial commit

