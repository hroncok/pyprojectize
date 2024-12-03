%global srcname colcon-alias

Name:           python-%{srcname}
Version:        0.1.1
Release:        2%{?dist}
Summary:        Extension for colcon to create and modify command aliases

License:        Apache-2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Not submitted upstream - compatibility with pytest 2.9.X
Patch0:         %{name}-0.1.1-pytest-compat.patch

BuildArch:      noarch

%description
An extension for colcon-core to create and modify command aliases.

Aliases condense any number of colcon command invocations made up of a verb
followed by all associated arguments down to another 'alias' verb. When
invoking the alias verb, additional arguments can be appended to the original
invocations.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.17.0
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-filelock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
Conflicts:      python%{python3_pkgversion}-colcon-mixin < 0.2.2

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.17.0
Requires:       python%{python3_pkgversion}-filelock
Requires:       python%{python3_pkgversion}-PyYAML
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to create and modify command aliases.

Aliases condense any number of colcon command invocations made up of a verb
followed by all associated arguments down to another 'alias' verb. When
invoking the alias verb, additional arguments can be appended to the original
invocations.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l colcon_alias


%check
%pyproject_check_import

%pytest -m 'not linter' test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Scott K Logan <logans@cottsay.net> - 0.1.1-1
- Update to 0.1.1 (rhbz#2294185)
- Switch to SPDX license identifier

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.13

* Thu Feb 01 2024 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Update to 0.1.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.2-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Scott K Logan <logans@cottsay.net> - 0.0.2-2
- Update description
- Update project URL

* Sun Feb 20 2022 Scott K Logan <logans@cottsay.net> - 0.0.2-1
- Initial package (rhbz#2056369)
