Name:           python-dijitso
Version:        2019.1.0
Release:        20%{?dist}
Summary:        Distributed just-in-time building of shared libraries

License:        LGPL-3.0-or-later
URL:            https://fenics-dijitso.readthedocs.org/
Source0:        https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-%{version}.tar.gz.asc
Source2:        3083BE4C722232E28AD0828CBED06106DD22BAB3.key

ExcludeArch: i686

BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

BuildRequires:  python3-mpi4py-mpich
BuildRequires:  mpich-devel
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  openmpi-devel

# We want to build on all architectures to test mpi and compilation,
# but the package itself is fully noarch.
%global debug_package %{nil}

%global _description %{expand:
%{summary}. This module is
used internally in the FEniCS framework to provide just in time
compilation of C++ code that is generated from Python modules. It is
only called from within a C++ library, and thus does not need wrapping
in a nice Python interface.}

%description %_description

%package -n python3-dijitso
Summary: %summary
%{?python_provides python3-dijitso}
Requires:       python3-mpi4py-runtime
Requires:       gcc-c++
BuildArch:      noarch

%description -n python3-dijitso %_description

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n dijitso-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
# We test with both mpi implementations, just because we can :_]

%_mpich_load
%__python3 -m pytest -v test/
%_mpich_unload

%_openmpi_load
%__python3 -m pytest -v test/
%_openmpi_unload

%files -n python3-dijitso
%license COPYING
%license COPYING.LESSER
%doc README.rst
%{_bindir}/dijitso
%{python3_sitelib}/dijitso
%{python3_sitelib}/fenics_dijitso-%{version}-py%{python3_version}.egg-info/
%{_mandir}/man1/dijitso.1*

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2019.1.0-19
- Rebuilt for Python 3.13

* Wed Jan 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 2019.1.0-18
- ExcludeArch i686

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2019.1.0-14
- Rebuilt for Python 3.12

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 2019.1.0-13
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2019.1.0-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2019.1.0-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2019.1.0-1
- Initial packaging
