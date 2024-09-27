Name:           pgzero
Version:        1.2.1
Release:        14%{?dist}
Summary:        A zero-boilerplate 2D games framework

# Automatically converted from old format: LGPLv3 and ASL 2.0 and CC-BY-SA and CC0 and MIT and OFL - review is highly recommended.
License:        LGPL-3.0-only AND Apache-2.0 AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0 AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-OFL
# pgzero module and runner under LGPLv3
# examples/basic/fonts/Cherry_Cream_Soda and Roboto_Condensed under ASL 2.0
# examples/lander/lander.py under CC-BY-SA
# examples/basic/fonts/bubblegum_sans.ttf under CC0
# examples/memory/ under MIT
# examples/basic/fonts/Boogaloo and Bubblegum_Sans under OFL
URL:            http://pypi.python.org/pypi/pgzero
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-pygame
BuildRequires:  python3-numpy

%{?python_provide:%python_provide python3-%{name}}
 
Requires:       python3-pygame
Requires:       python3-setuptools
Requires:       python3-numpy

%description
Pygame Zero A zero boilerplate games programming framework for Python 3, based
on Pygame. Pygame Zero consists of a runner pgzrun that will run a
Pygame Zero script with a full game loop and a range of useful builtins.

%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info
# Remove version limit for pygame dependency
sed -i "s/\(pygame.*\), <2.0.*/\1'/" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Some tests cannot be run in a headles environment without display
rm test/test_screen.py test/test_actor.py test/test_sound_formats.py
%{__python3} -m unittest discover test/

%files
%license COPYING
%doc README.rst examples
%{_bindir}/pgzrun
%{python3_sitelib}/%{name}
%{python3_sitelib}/pgzrun.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}-%{version}.dist-info

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Python Maint <python-maint@redhat.com> - 1.2.1-12
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.1-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.10

* Wed Mar 03 2021 Lumír Balhar <lbalhar@redhat.com> - 1.2.1-1
- Update to 1.2.1
Resolves: rhbz#1934313

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Lumír Balhar <lbalhar@redhat.com> - 1.2-11
- Make it installable with pygame>=2.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-2
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Lumir Balhar <lbalhar@redhat.com> - 1.2-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Lumir Balhar <lbalhar@redhat.com> - 1.1-1
- Initial package.
