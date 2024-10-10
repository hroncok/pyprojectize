%global pypi_name py3nvml

Name:           python-%{pypi_name}
Version:        0.2.7
Release:        11%{?dist}
Summary:        Python 3 Bindings for the NVIDIA Management Library

License:        BSD-3-Clause
URL:            https://github.com/fbcotter/py3nvml
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description \
Python 3 compatible bindings to the NVIDIA Management Library. Can be used to \
query the state of the GPUs on your system.

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(xmltodict)
%description -n python3-%{pypi_name} %{_description}


%package -n     python3-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python3-%{pypi_name}-doc %{_description}

This package contains the documentation for %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/py3smi

%files -n python3-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.7-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.2.7-6
- Rebuilt for Python 3.12

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.2.7-5
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.11

* Tue Apr 05 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.7-1
- chore(update): 0.2.7

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.6-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.9

* Tue Apr 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.6-1
- Update to 0.2.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.5-1
- Update to 0.2.5

* Fri Oct 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.4-1
- Update to 0.2.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.3-2
- Added docs and spec file fixes.

* Wed Mar 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.3-1
- Initial package.
