# Enable Python dependency generation

%global pypi_name python-freeipa
%global srcname freeipa

Name:           python-%{srcname}
Version:        1.0.8
Release:        3%{?dist}
Summary:        Lightweight FreeIPA client

License:        MIT
URL:            https://python-freeipa.readthedocs.io/
Source0:        https://github.com/opennode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist responses}

%description
python-freeipa is lightweight FreeIPA client.

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary} for Python %{python3_version}

%description -n python%{python3_pkgversion}-%{srcname}
python-freeipa is lightweight FreeIPA client.

This package provides the Python %{python3_version} variant.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix version
sed -e "s/version='1.0.6',/version='%{version}',/" -i setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l python_freeipa

%check
%python3 setup.py test

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.0.8-2
- Rebuilt for Python 3.13

* Wed Feb 07 2024 Ryan Lerch <rlerch@redhat.com> - 1.0.8-1
- Update to Version 1.0.8

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.0.7-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.7-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 10:45:18 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.7-1
- Update to 1.0.7 (#1893204)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.6-1
- Update to 1.0.6 (#1829511)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.9

* Tue Apr 21 19:45:43 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.4-1
- Update to 1.0.4 (#1826547)

* Fri Apr 17 15:22:42 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.3-1
- Update to 1.0.3 (#1825360)

* Mon Apr 13 10:26:54 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.2-1
- Initial package for Fedora (#1823091)
