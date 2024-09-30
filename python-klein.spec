%global pypi_name klein

Name:           python-%{pypi_name}
Version:        23.5.0
Release:        6%{?dist}
Summary:        Python microframework built on werkzeug + twisted.web

License:        MIT
URL:            https://github.com/twisted/klein
Source0:        %{pypi_source}
BuildArch:      noarch
Patch0:         imp-removal.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(hyperlink)
BuildRequires:  python3dist(incremental)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(tubes)
BuildRequires:  python3dist(twisted) >= 15.5
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(zope-interface)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
Klein is a Web Micro-Framework built on Twisted and Werkzeug.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Klein is a Web Micro-Framework built on Twisted and Werkzeug.

%package -n python-%{pypi_name}-doc
Summary:        klein documentation

%description -n python-%{pypi_name}-doc
Documentation for klein

%prep
%autosetup -n %{pypi_name}-%{version} -p0
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 23.5.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.5.0-1
- 23.5.0

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 20.6.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 20.6.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20.6.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 23 2020 Neal Gompa <ngompa13@gmail.com> - 20.6.0-1
- Initial package (#1870883)
