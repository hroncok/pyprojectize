%global pypi_name dbf
%global sum Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf
%global desc Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf\
files (including memos)\
\
Currently supports dBase III, Clipper, FoxPro, and Visual FoxPro tables. Text is\
returned as unicode, and codepage settings in tables are honored. Memos and Null\
fields are supported.

Name:           python-%{pypi_name}
Version:        0.99.3
Release:        6%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         prevent-synthax-error.patch
Patch1:         remove-distutil.patch

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{sum}
BuildRequires:  python3-devel
Requires:       python3-aenum

%description -n python3-%{pypi_name}
%{desc}


%prep
%setup -qn %{pypi_name}-%{version}
# Correct line endings for setup.py
sed -i "s|\r||g" setup.py
%autopatch -p1
rm -f dbf/ver_32.py
rm -f dbf/ver_2.py
sed -i "s|\r||g" dbf/README.md


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc dbf/README.md

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.99.3-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.99.3-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Julien Enselme <jujens@jujens.eu> - 0.99.3-1
- Update to 0.99.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.99.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Julien Enselme <jujens@jujens.eu> - 0.99.2-4
- Remove dependency to distutil.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Python Maint <python-maint@redhat.com> - 0.99.2-2
- Rebuilt for Python 3.11

* Sat Jun 18 2022 Julien Enselme <jujens@jujens.eu> - 0.99.2
- Update to 0.99.2

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.96.005-23
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.96.005-20
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.96.005-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.96.005-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.96.005-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.96.005-11
- Remove Python 2 subpackage (#1627309)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.96.005-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.96.005-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.96.005-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.005-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 9 2015 Julien Enselme <jujens@jujens.eu> - 0.96.005-1
- Inital package
