%global desc Version of the glob module that can capture patterns and supports recursive\
wildcards.
%global pkg_name glob2
%global pypi_version 0.7

Name:           python-%{pkg_name}
Version:        0.7
Release:        23%{?dist}
Summary:        Glob module recursive wildcards support

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pkg_name}
Source0:        https://files.pythonhosted.org/packages/d7/a5/bbbc3b74a94fbdbd7915e7ad030f16539bfdc1362f7e9003b594f0537950/glob2-0.7.tar.gz

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pkg_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
Requires:       python3-setuptools

%description -n python3-%{pkg_name}
%{desc}

%prep
%setup -q -n %{pkg_name}-%{pypi_version}
# Compatibility with pytest 8
sed -i "s/setup(/setup_method(/" test.py
sed -i "s/teardown(/teardown_method(/" test.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pkg_name}

%check
%pyproject_check_import

%pytest test.py


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst CHANGES


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7-21
- Rebuilt for Python 3.13

* Wed Apr 17 2024 Lumír Balhar <lbalhar@redhat.com> - 0.7-20
- Fix compatibility with pytest 8 (rhbz#2274119)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7-16
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7-13
- Rebuilt for Python 3.11

* Thu Feb 24 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.7-12
- Utilize pytest and actually run the tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 0.7-1
- Update to 0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Julien Enselme <jujens@jujens.eu> - 0.6.0-6
- Remove Python 2 subpackage (#1627336)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Julien Enselme <jujens@jujens.eu> - 0.6.0-1
- Update to 0.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuild for Python 3.6

* Tue Nov 08 2016 Julien Enselme <jujens@jujens.eu> - 0.5.0-1
- Update to 0.5.0
- Update spec to new guidelines

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.4.1-4
- Rebuilt for python 3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Julien Enselme <jujens@jujens.eu> - 0.4.1.2
- Correct the source of the LICENSE

* Mon Jan 05 2015 Julien Enselme <jujens@jujens.eu> - 0.4.1-1
- Initial packaging
