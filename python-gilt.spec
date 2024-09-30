%global srcname gilt
%global pkgname python-gilt
%global setup_flags PBR_VERSION=%{version}

Name:    python-%{srcname}
Version: 1.2.2
Release: 11%{?dist}
Summary: Gilt is a git layering tool
License: MIT

URL:     https://github.com/retr0h/gilt
Source0: https://pypi.io/packages/source/p/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: python3-pbr
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-sphinx
BuildRequires: python3-git-url-parse

%description
Gilt is a git layering tool

%package -n python-%{srcname}-doc
Summary: %summary

%description -n python-%{srcname}-doc
Documentation for python-gilt

%package -n python3-%{srcname}
Summary: %summary

Recommends: python-%{srcname}-doc

Requires: python3-sh
Requires: python3-pbr
Requires: python3-click
Requires: python3-pyyaml
Requires: python3-colorama
Requires: python3-fasteners
Requires: python3-git-url-parse

%{?python_disable_dependency_generator}
%description -n python3-%{srcname}
Gilt is a git layering tool

%prep
%autosetup -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{setup_flags} %{pyproject_wheel}

# generate html docs
cd doc
PYTHONPATH=.. make html
# remove the sphinx-build leftovers
rm -rf build/html/.{doctrees,buildinfo}

%install
%{setup_flags} %{pyproject_install}
%pyproject_save_files -l %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/%{srcname}

%files -n python-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc doc/build/html

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.2-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.2.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.2-1
- Upgrade to version 1.2.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.1-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.1-4
- Replace Python version globs with macros to support python 3.10

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.1
- Initial package
