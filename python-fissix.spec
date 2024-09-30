%global srcname fissix

%bcond_without tests

Name:           python-%{srcname}
Version:        20.8.0
Release:        15%{?dist}
Summary:        Monkeypatches to override default behavior of lib2to3
# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            https://github.com/jreese/fissix
Source0:        %{pypi_source}
Patch0:         %{srcname}-dont_ship_tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-test
BuildRequires:  %{py3_dist appdirs}
BuildRequires:  %{py3_dist pytest}
%endif


%global _description %{expand:
Backport of latest lib2to3, with enhancements.}


%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}
# not sure why but automatic requires don't work
Requires:       %{py3_dist appdirs}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i '1d' fissix/pgen2/token.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}
cp -p fissix/*.txt %{buildroot}%{python3_sitelib}/%{srcname}/


%check
# mv fissix-tests fissix/tests
%{python3} -m pytest --verbose fissix/tests


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 20.8.0-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 20.8.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 20.8.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 20.8.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20.8.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-1
- Initial package
