# Created by pyp2rpm-3.3.2
%global pypi_name freecell_solver

Name:           python-%{pypi_name}
Version:        0.2.6
Release:        15%{?dist}
Summary:        Freecell Solver Python bindings

License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(openstackdocstheme)
BuildRequires:  python3dist(oslotest) >= 1.10.0
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pbr) >= 2.0
BuildRequires:  python3dist(python-subunit) >= 0.0.18
BuildRequires:  python3dist(testtools) >= 1.4.0
BuildRequires:  python3dist(sphinx)

%description
Python bindings for Freecell Solver using cffi.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(pbr) >= 2.0
%description -n python3-%{pypi_name}
Python bindings for Freecell Solver using cffi.

%package -n python-%{pypi_name}-doc
Summary:        freecell_solver documentation
%description -n python-%{pypi_name}-doc
Documentation for freecell_solver

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst doc/source/readme.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.2.6-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Python Maint <python-maint@redhat.com> - 0.2.6-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.2.6-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Shlomi Fish <shlomif@shlomifish.org> 0.2.6-1
- New Upstream Version

* Fri May 29 2020 Shlomi Fish <shlomif@shlomifish.org> 0.2.3-6
- Rebuild for Python 3.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Shlomi Fish <shlomif@shlomifish.org> - 0.2.3-1
- Initial package.
