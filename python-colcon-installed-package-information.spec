%global srcname colcon-installed-package-information

Name:           python-%{srcname}
Version:        0.2.1
Release:        3%{?dist}
Summary:        Extensions for colcon to inspect packages which have already been installed

License:        Apache-2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Not submitted upstream - compatibility with pytest < 3.9.0
Patch0:         %{name}-0.2.1-pytest-compat.patch

BuildArch:      noarch

%description
Extensions for colcon-core to inspect packages which have already been
installed.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
%endif

%description -n python%{python3_pkgversion}-%{srcname}
These colcon extensions provide a mechanism which can be used for getting
information about packages outside of the workspace, which have already been
built and installed prior to the current operation.

In general, they work similarly to and are based on the
PackageDiscoveryExtensionPoint and PackageAugmentationExtensionPoint
extensions provided by colcon_core.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l colcon_installed_package_information


%check
%pyproject_check_import

%pytest -m 'not linter' test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.13

* Fri Mar 22 2024 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Update to 0.2.1 (rhbz#2269532)
- Switch to SPDX license identifier

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Update to 0.1.0
- Change URL to point to GitHub repository
- Improve description

* Wed Mar 16 2022 Scott K Logan <logans@cottsay.net> - 0.0.1-1
- Initial package
