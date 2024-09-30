%define modname zope.deprecation

Name:           python-zope-deprecation
Version:        4.4.0
Release:        23%{?dist}
Summary:        Zope 3 Deprecation Infrastructure

License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.deprecation
Source0:        https://files.pythonhosted.org/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
This package provides a simple function called 'deprecated(names, reason)' to\
deprecate the previously mentioned Python objects.

%description %_description

%package -n python3-zope-deprecation
Summary:        Zope 3 Deprecation Infrastructure


%description -n python3-zope-deprecation
This package provides a simple function called 'deprecated(names, reason)' to
deprecate the previously mentioned Python objects.

%prep
%setup -q -n %{modname}-%{version}

rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zope
rm -f %{buildroot}%{python3_sitelib}/zope/deprecation/tests.py*

%check
%{__python3} setup.py test

%files -n python3-zope-deprecation -f %{pyproject_files}
%doc README.rst LICENSE.txt


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.4.0-22
- Rebuilt for Python 3.13

* Sun Apr 14 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.0-21
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.4.0-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.4.0-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 4.4.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-5
- Subpackage python2-zope-deprecation has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.4.0-1
- Upgrade to 4.4.0.
- https://github.com/zopefoundation/zope.deprecation/blob/4.4.0/CHANGES.rst

* Thu Sep 20 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.3.0-4
- Fix FTBFS by adding a BR on python2-devel (#1606009).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-3
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.3.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 06 2018 Lumír Balhar <lbalhar@redhat.com> - 4.3.0-1
- New upstream release
- URLs with SSL

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1.1-13
- Python 2 binary package renamed to python2-zope-deprecation
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
