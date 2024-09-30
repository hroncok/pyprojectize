%global srcname glyphsLib
%global with_check 0

Name:           python-%{srcname}
Version:        5.1.11
Release:        15%{?dist}
Summary:        A bridge from Glyphs source files to UFOs

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        %pypi_source %srcname %version zip

BuildArch:      noarch

%description
This library provides a bridge from Glyphs source files (.glyphs) to UFOs
(Unified Font Object).

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel

%if 0%{with_check}
# missing (xmldiff, ufoNormalizer)
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-fonttools
BuildRequires:  python3-defcon
%endif

%description -n python3-%{srcname}
This library provides a bridge from Glyphs source files (.glyphs) to UFOs
(Unified Font Object).

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Skipping check for now due to missing dependencies
%if 0%{?with_check}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CONTRIBUTING.md
%dir %{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.dist-info
%{python3_sitelib}/%{srcname}/*
%{_bindir}/glyphs2ufo
%{_bindir}/ufo2glyphs

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 5.1.11-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.1.11-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.1.11-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.1.11-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.11-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 5.1.11-1
- Update version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 5.1.10-1
- Update version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-2
- Rebuilt for Python 3.8

* Sun Jul 28 2019 Athos Ribeiro <athoscr@fedoraproject.org> - 4.0.0-1
- Update version
- Skip test suite due to missing test dependencies (xmldiff, ufoNormalizer)
- Use sources from pypi
- Drop v2 patches
- Drop all Requires in favor of auto generated dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-6
- Subpackage python2-glyphsLib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.2.1-2
- Include new subdirectories

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.2.1-1
- Update version
- Remove patch merged upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.7.5-2
- Apply patch to remove shebangs from non-executable modules

* Thu Jul 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.7.5-1
- Update version
- Change package name to use upstream cammelcase

* Mon Apr 10 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.6.0-1
- Update version
- Add pythonX-mock BR

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5.2-1
- Initial package
