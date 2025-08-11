Name:           python-pypresence
Version:        4.3.0
Release:        6%{?dist}
Summary:        A Discord Rich Presence Client in Python 
License:        MIT
URL:            https://qwertyquerty.github.io/pypresence/html/index.html
Source0:        https://github.com/qwertyquerty/pypresence/archive/v%{version}/pypresence-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description \
Python-pypresence is a simple Discord Rich Presence Client in Python. \
Note that in order to use most of it's functions, an authorized app \
is required.


%description %{_description}


%package -n python3-pypresence
Summary:        %{summary}


%description -n python3-pypresence %{_description}


%prep
%autosetup -p1 -n pypresence-%{version}
# docs include files that are under a different license model, omitting them
rm -rf %{buildroot}/docs


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pypresence


%check
%pyproject_check_import
%py3_check_import pypresence


%files -n python3-pypresence -f %{pyproject_files}
%doc README.md


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.3.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 8 2023 Steve Cossette <farchord@gmail.com> - 4.3.0-1
- Various bugfixes and upgrades

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.2.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 2 2022 Steve Cossette <farchord@gmail.com> - 4.2.1-1
- Initital release of pypresence (4.2.1)
