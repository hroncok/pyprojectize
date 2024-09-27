%global pypi_name neurosynth

# The test require internet to download data and so cannot be run in koji
# Test disable
%bcond_with tests

Name:		python-%{pypi_name}
Version:	0.3.8
Release:	15%{?dist}
Summary:	Large-scale synthesis of functional neuroimaging data

License:	MIT
URL:		https://github.com/neurosynth/neurosynth
Source0:	%{pypi_source}
BuildArch:	noarch
 
BuildRequires:	python3-devel
BuildRequires:	python3dist(biopython)
BuildRequires:	python3dist(nibabel)
BuildRequires:	python3dist(nose)
BuildRequires:	python3dist(nose) >= 0.10.1
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pandas)
BuildRequires:	python3dist(ply)
BuildRequires:	python3dist(scikit-learn)
BuildRequires:	python3dist(scipy)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(six)

%description
Neurosynth is a Python package for large-scale synthesis of 
functional neuroimaging data.

%package -n	python3-%{pypi_name}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:	python3dist(biopython)
Requires:	python3dist(nibabel)
Requires:	python3dist(nose) >= 0.10.1
Requires:	python3dist(numpy)
Requires:	python3dist(pandas)
Requires:	python3dist(ply)
Requires:	python3dist(scikit-learn)
Requires:	python3dist(scipy)
Requires:	python3dist(six)

%description -n	python3-%{pypi_name}
Neurosynth is a Python package for large-scale synthesis of 
functional neuroimaging data.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

chmod 0644 neurosynth/tests/data/sgacc_mask.nii.gz

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.3.8-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.3.8-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.8-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-2
- Rebuilt for Python 3.9

* Sun Feb 16 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.8-1
- Update to 0.3.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.7-2
- Test need download data

* Fri Jun 14 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.7-1
- Initial package.
