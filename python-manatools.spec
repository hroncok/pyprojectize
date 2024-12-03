%global module manatools

Name:           python-%{module}
Version:        0.0.4
Release:        11%{?dist}

Summary:        A Python framework to build ManaTools applications
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/manatools/python-manatools
Source0:        https://github.com/manatools/python-manatools/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Python ManaTools aim is to help in writing tools based on libYui
(SUSE widget abstraction library), to be collected under the
ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%package -n python3-%{module}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-yui
Requires:       python3-yui
Recommends:     (libyui-mga-qt if qt5-qtbase-gui)
Recommends:     (libyui-mga-gtk if gtk3)

%description -n python3-%{module}
Python ManaTools aim is to help in writing tools based on libYui
(SUSE widget abstraction library), to be collected under the
ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%prep
%autosetup -p1

sed -i 's|0.0.1|%{version}|' manatools/version.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{module}

%check
%pyproject_check_import

%files -n python3-%{module} -f %{pyproject_files}
%doc README.md NEWS

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.4-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.0.4-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.4-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.4-2
- Rebuilt for Python 3.11

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.0.4-1
- Version 0.0.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.3-1
- Initial package

