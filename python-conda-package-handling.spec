%?python_enable_dependency_generator
%global srcname conda-package-handling
%global pkgname conda_package_handling

Name:           python-%{srcname}
Version:        2.3.0
Release:        3%{?dist}
Summary:        Create and extract conda packages of various formats

License:        BSD-3-Clause
URL:            https://github.com/conda/%{srcname}
Source0:        https://github.com/conda/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Create and extract conda packages of various formats.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-conda-package-streaming
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-mock

%description -n python%{python3_pkgversion}-%{srcname}
Create and extract conda packages of various formats.

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e s/archive_and_deps/archive/ setup.py
# do not run coverage in pytest
sed -i -E '/--(no-)?cov/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pkgname}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v tests 

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.md CHANGELOG.md README.md
%{_bindir}/cph

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Orion Poplawski <orion@nwra.com> - 2.3.0-1
- Update to 2.3.0

* Tue Mar 12 2024 Lumír Balhar <lbalhar@redhat.com> - 2.2.0-4
- Clean-up of buildtime and runtime dependencies

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 26 2023 Orion Poplawski <orion@nwra.com> - 2.2.0-1
- Update to 2.2.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.12

* Sat May 06 2023 Orion Poplawski <orion@nwra.com> - 2.1.0-1
- Update to 2.1.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Orion Poplawski <orion@nwra.com> - 2.0.2-1
- Update to 2.0.2
- Use SPDX License tag

* Fri Sep 23 2022 Orion Poplawski <orion@nwra.com> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.8.1-2
- Rebuilt for Python 3.11

* Sun Apr 03 2022 Orion Poplawski <orion@nwra.com> - 1.8.1-1
- Update to 1.8.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.3-2
- Rebuilt for Python 3.10

* Tue Apr 13 2021 Orion Poplawski <orion@nwra.com> - 1.7.3-1
- Update to 1.7.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 18 2020 Orion Poplawski <orion@nwra.com> - 1.7.2-1
- Update to 1.7.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Orion Poplawski <orion@nwra.com> - 1.7.0-3
- Add BR on python-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Orion Poplawski <orion@nwra.com> - 1.7.0-1
- Update to 1.7.0

* Thu May 07 2020 Orion Poplawski <orion@nwra.com> - 1.6.1-1
- Update to 1.6.1

* Sun Feb 2 2020 Orion Poplawski <orion@nwra.com> - 1.6.0-3
- Exclude failing test that is not ready upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov  8 2019 Orion Poplawski <orion@nwra.com> - 1.6.0-1
- Update to 1.6.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Orion Poplawski <orion@nwra.com> - 1.4.1-1
- Update to 1.4.1
- Enable python dependency generator

* Mon Jul 29 2019 Orion Poplawski <orion@nwra.com> - 1.3.11-1
- Update to 1.3.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Orion Poplawski <orion@nwra.com> - 1.3.1-1
- Update to 1.3.1

* Sat May 18 2019 Orion Poplawski <orion@nwra.com> - 1.1.1-1
- Initial Fedora package
