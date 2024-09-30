%global         srcname     DBUtils

Name:           python-dbutils
Version:        3.0.3
Release:        7%{?dist}
Summary:        Tools providing solid, persistent and pooled connections to a database
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)


%global _description %{expand:
DBUtils is a suite of tools providing solid, persistent and pooled connections
to a database that can be used in all kinds of multi-threaded environments.

The suite supports DB-API 2 compliant database interfaces.}

%description %{_description}


%package -n python3-dbutils
Summary:        %{summary}
# python3 renamed this to lower case, provide the upcase
# name for simplified compatibility
%py_provides python3-DBUtils

%description -n python3-dbutils %{_description}

%package doc
Summary:        %{summary}
%description doc %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# make docs
pushd docs
%{python3} make.py
popd

%install
%pyproject_install
%pyproject_save_files dbutils

# install docs
install -t '%{buildroot}%{_pkgdocdir}' -D -p -m 0644 README.md
pushd docs
install -t '%{buildroot}%{_pkgdocdir}/html' -D -p -m 0644 *.html *.css *.png
popd


%check
%{python3} -m unittest discover -v .


%files -n python3-dbutils -f %{pyproject_files}
%license LICENSE

%files doc
%license LICENSE
%doc %{_pkgdocdir}

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.3-2
- Rebuilt for Python 3.12

* Thu Apr 27 2023 Pat Riehecky <riehecky@fnal.gov> - 3.0.3-1
- Update to 3.0.3

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Pat Riehecky <riehecky@fnal.gov> - 3.0.1-1
- Update to current upstream

* Tue Dec 14 2021 Pat Riehecky <riehecky@fnal.gov> - 3.0.0-1
- Update to current

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 8 2021 Pat Riehecky <riehecky@fnal.gov> - 2.0.2-1
- Update to current RHBZ: 1980508

* Thu Jun 17 2021 Pat Riehecky <riehecky@fnal.gov> - 2.0.1-1
- Initial package.
