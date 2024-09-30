%{?python_enable_dependency_generator}
%global modname stuf

Name:               python-stuf
Version:            0.9.16
Release:            38%{?dist}
Summary:            Fancy python dictionary types

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/stuf
Source0:            https://pypi.python.org/packages/source/s/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch


%description
A collection of Python dictionary types that support attribute-style
access. Includes *defaultdict*,  *OrderedDict*, restricted, *ChainMap*,
*Counter*, and frozen implementations plus miscellaneous utilities for
writing Python software.

%package -n python3-%{modname}
Summary:            Fancy python dictionary types
BuildRequires:      python3-devel

%description -n python3-%{modname}
A collection of Python dictionary types that support attribute-style
access. Includes *defaultdict*,  *OrderedDict*, restricted, *ChainMap*,
*Counter*, and frozen implementations plus miscellaneous utilities for
writing Python software.

%prep
%autosetup -n %{modname}-%{version}

# Remove upstreams egg info
rm -rf *.egg*

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

# https://bitbucket.org/lcrees/stuf/issues/9/find_packages-should-exclude-tests
rm -rf %{buildroot}%{python3_sitelib}/tests/

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.16-38
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.16-36
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.16-32
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.16-29
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.16-26
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-23
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-21
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-20
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.16-17
- Enable python dependency generator

* Mon Jan 07 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-16
- Subpackage python2-stuf has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-14
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.16-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-9
- Rebuild for Python 3.6

* Tue Jul 05 2016 Ralph Bean <rbean@redhat.com> - 0.9.16-8
- Loosen up python-parse dependency for epel7.

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 0.9.16-7
- Rebundle six, since it is highly customized, #1335144.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Ralph Bean <rbean@redhat.com> - 0.9.16-5
- Fix python2-setuptools dep on F22 and older.

* Wed Dec 02 2015 Ralph Bean <rbean@redhat.com> - 0.9.16-4
- Specbump (to test a local dev tool).

* Tue Dec 01 2015 Ralph Bean <rbean@redhat.com> - 0.9.16-3
- Fix python3-six unbundling as per review.

* Mon Nov 30 2015 Ralph Bean <rbean@redhat.com> - 0.9.16-2
- Fixed initial changelog entry.
- Rename dep from python2-parse to python-parse
- Unbundle and add dep on python-six and python3-six.
- Fix python_provide usage.

* Fri Nov 13 2015 Ralph Bean <rbean@redhat.com> - 0.9.16-1
- Initial packaging for Fedora.
