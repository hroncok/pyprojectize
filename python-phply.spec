%global pypi_name phply
%global author viraptor

Name:           python-%{pypi_name}
Version:        1.2.5
Release:        10%{?dist}
Summary:        PHP parser written in Python using PLY 

License:        BSD-3-Clause
URL:            https://github.com/%{author}/%{pypi_name}
Source0:        https://github.com/%{author}/%{pypi_name}/archive/refs/tags/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-ply

%description
phply is a parser for the PHP programming language written using PLY.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
phply is a parser for the PHP programming language written using PLY

%prep
%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%pyproject_check_import
%py3_check_import %{pypi_name}

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/phplex
%{_bindir}/phpparse
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.5-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.5-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Sudip Shil <sshil@redhat.com> - 1.2.5-3
- spec file updated

* Wed Nov 23 2022 Sudip Shil <sshil@redhat.com> - 1.2.5-2
- spec file updated

* Fri Nov 18 2022 Sudip Shil <sshil@redhat.com> - 1.2.5-1
- New rpm package submission for Fedora
