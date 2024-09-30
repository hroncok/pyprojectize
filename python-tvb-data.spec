%global pypi_name tvb-data
%global module_name tvb_data

%global desc %{expand: \
The Virtual Brain Project (TVB Project) has the purpose of offering some modern
tools to the Neurosciences community, for computing, simulating and analyzing
functional and structural data of human brains.

Various demonstration datasets for use with The Virtual Brain are provided here.
}

Name:           python-%{pypi_name}
Version:        1.5.9
Release:        18%{?dist}
Summary:        Demo data for The Virtual Brain software

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/the-virtual-brain/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

# Not included in setup.py
Requires:       %{py3_dist numpy}
Requires:       %{py3_dist nibabel}
Requires:       %{py3_dist pillow}
Requires:       %{py3_dist scipy}
Requires:       %{py3_dist h5py}
Requires:       %{py3_dist mayavi}
Requires:       %{py3_dist networkx}

# Needs packaging but is py2 only, so we can't package it yet
# Upstream currently does not plan to migrate to py3. Trying:
# https://github.com/LTS5/cfflib/issues/7
# Leaving the cff bits in the package at the moment.
Recommends:     %{py3_dist cfflib}
# Cyclic deps. Depends on this package, so using weak deps
Recommends:     %{py3_dist tvb-library}


%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Upstream included a commit to prepare for 1.5.10 in the release tar
sed -i 's/1.5.10/1.5.9/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{module_name}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.9-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.5.9-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.9-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.9-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.9-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.9-1
- Update to 1.5.9
- Update autosetup command
- Fix wrong version in setup.py

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.6-8.20191229git7d2d05b
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.6-7.20191229git7d2d05b
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-6.20191229git7d2d05b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-5.20191229git7d2d05b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-4.20181229git7d2d05b
- Add required requires

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-3.20181229git7d2d05b
- Correct license

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-2.20181229git7d2d05b
- Remove empty check
- Add setuptools BR

* Sat Dec 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-1.20181229git7d2d05b
- Initial build
