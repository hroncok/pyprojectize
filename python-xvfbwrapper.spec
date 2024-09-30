
%global pypi_name xvfbwrapper

Name:           python-%{pypi_name}
Version:        0.2.9
Release:        25%{?dist}
Summary:        run headless display inside X virtual framebuffer (Xvfb)

License:        MIT
URL:            https://github.com/cgoldberg/xvfbwrapper
Source0:        https://files.pythonhosted.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%description %_description


%package -n python3-%{pypi_name}
Summary:        run headless display inside X virtual framebuffer (Xvfb)

BuildRequires: python3-devel
BuildRequires: python3-mock
BuildRequires: python3-nose
BuildRequires: xorg-x11-server-Xvfb

%description -n python3-%{pypi_name}
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%prep
%autosetup -n %{pypi_name}-%{version}


# remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' xvfbwrapper.py




%generate_buildrequires
%pyproject_buildrequires




%build

%pyproject_wheel

%install

%pyproject_install
%pyproject_save_files %{pypi_name}

%check
export DISPLAY=:0.0


nosetests-%{python3_version}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.9-24
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.9-20
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.9-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.9-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.9-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Jul 23 2018 Matthias Runge <mrunge@redhat.com> - 0.2.9-4
- modernize spec
- fix ftbfs (rhbz#1606005)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Matthias Runge <mrunge@redhat.com> - 0.2.9-1
- update to 0.2.9-1

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.4-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.4-8
- Python 2 binary package renamed to python2-xvfbwrapper
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-5
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul 21 2015 Matthias Runge <mrunge@redhat.com> - 0.2.4-2
- add py3 subpackage (rhbz#1244817)

* Mon Jul 20 2015 Matthias Runge <mrunge@redhat.com> - 0.2.4-1
- Initial package.
