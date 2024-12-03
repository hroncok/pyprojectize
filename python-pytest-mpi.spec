%global srcname pytest-mpi

Name:           python-%{srcname}
Version:        0.6
Release:        11%{?dist}
Summary:        Pytest plugin for running tests under MPI

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/aragilar/pytest-mpi
Source0:        https://github.com/aragilar/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
pytest_mpi is a plugin for pytest providing some useful tools when running
tests under MPI, and testing MPI-related code.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Pytest plugin for running tests under MPI
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-sybil >= 3.0
BuildRequires:  mpich-devel
BuildRequires:  python%{python3_pkgversion}-mpi4py-mpich
BuildRequires:  openmpi-devel
BuildRequires:  python%{python3_pkgversion}-mpi4py-openmpi

%description -n python%{python3_pkgversion}-%{srcname}
pytest_mpi is a plugin for pytest providing some useful tools when running
tests under MPI, and testing MPI-related code.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pytest_mpi


%check
%pyproject_check_import

module load mpi/mpich-%{_host_cpu}
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$MPI_PYTHON3_SITEARCH
py.test-%{python3_version} -p pytester --runpytest=subprocess -vv
module unload mpi/mpich-%{_host_cpu}
module load mpi/openmpi-%{_host_cpu}
export OMPI_MCA_rmaps_base_oversubscribe=1
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$MPI_PYTHON3_SITEARCH
py.test-%{python3_version} -p pytester --runpytest=subprocess -vv
module unload mpi/openmpi-%{_host_cpu}


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.6-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.6-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6-2
- Rebuilt for Python 3.11

* Sat Mar 05 2022 Orion Poplawski <orion@nwra.com> - 0.6-1
- Update to 0.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Orion Poplawski <orion@nwra.com> - 0.5-1
- Update to 0.5

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4-5
- Rebuilt for Python 3.10

* Sat Jan 30 2021 Orion Poplawski <orion@nwra.com> - 0.4-4
- Set OMPI_MCA_rmaps_base_oversubscribe=1 for openmpi tests (bz#1900524)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov  1 2020 Orion Poplawski <orion@nwra.com> - 0.4-2
- Change URL
- Fix permissions

* Sun Oct 11 2020 Orion Poplawski <orion@nwra.com> - 0.4-1
- Initial package
