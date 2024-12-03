%global srcname colcon-override-check

Name:           python-%{srcname}
Version:        0.0.1
Release:        5%{?dist}
Summary:        Extension for colcon to check for problems overriding installed packages

License:        Apache-2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to check for potential problems when overriding
installed packages. Most notably, warn the user when overriding a package upon
which other packages in an underlay depend, but ones which are not also being
overridden.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.8.0
Requires:       python%{python3_pkgversion}-colcon-installed-package-information
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to check for potential problems when overriding
installed packages. Most notably, warn the user when overriding a package upon
which other packages in an underlay depend, but ones which are not also being
overridden.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l colcon_override_check


%check
%pyproject_check_import

%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 10 2022 Scott K Logan <logans@cottsay.net> - 0.0.1-1
- Initial package (rhbz#2143071)
