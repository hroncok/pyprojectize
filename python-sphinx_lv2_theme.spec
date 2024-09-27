%global pypi_name sphinx_lv2_theme

%global common_description %{expand:
This is a minimal pure-CSS theme for Sphinx that uses the documentation
style of the LV2 plugin specification and related projects.

This theme is geared toward producing beautiful API documentation for C, C++,
and Python that is documented using the standard Sphinx domains.
The output does not use Javascript at all, and some common features are not
implemented, so this theme should not be considered a drop-in replacement
for typical Sphinx themes.}


Name:           python-%{pypi_name}
Version:        1.4.2
Release:        1%{?dist}
Summary:        A minimal pure-CSS theme for Sphinx
License:        ISC
URL:            https://gitlab.com/lv2/%{pypi_name}
Source0:        %{url}/-/archive/v%{version}/%{pypi_name}-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description %{common_description}


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%if 0%{?epel} && 0%{?epel} <= 8
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%endif

%if 0%{?fedora} == 32
%py_provides python3-%{pypi_name}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name} %{common_description}


%prep
%autosetup -p1 -n %{pypi_name}-v%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%files -n  python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Sep 23 2024 Guido Aulisi <guido.aulisi@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Guido Aulisi <guido.aulisi@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.12

* Mon Jan 30 2023 Guido Aulisi <guido.aulisi@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Guido Aulisi <guido.aulisi@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 15:54:29 CET 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.0.0-2
- Spec cleanup

* Fri Jan 15 08:38:05 CET 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.0.0-1
- Initial package release
