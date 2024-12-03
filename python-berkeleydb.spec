%global pypi_name berkeleydb
%global pypi_version 18.1.4

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        14%{?dist}
Summary:        Python bindings for Oracle Berkeley DB

# For a breakdown of the licensing, see licenses.txt
License:        BSD-3-Clause AND ZPL-2.0
URL:            https://www.jcea.es/programacion/pybsddb.htm
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  chrpath

%description
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module. The database objects can use various access methods:
btree, hash, recno, queue and heap. Complete support of Oracle Berkeley DB
distributed transactions. Complete support for Oracle Berkeley DB Replication
Manager. Complete support for Oracle Berkeley DB Base Replication.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module. The database objects can use various access methods:
btree, hash, recno, queue and heap. Complete support of Oracle Berkeley DB
distributed transactions. Complete support for Oracle Berkeley DB Replication
Manager. Complete support for Oracle Berkeley DB Base Replication.

%package -n     python3-%{pypi_name}-devel
Summary:        %{summary}
Requires:       python3-%{pypi_name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{pypi_name}-devel
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module. The database objects can use various access methods:
btree, hash, recno, queue and heap. Complete support of Oracle Berkeley DB
distributed transactions. Complete support for Oracle Berkeley DB Replication
Manager. Complete support for Oracle Berkeley DB Base Replication.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

chrpath --delete $RPM_BUILD_ROOT%{python3_sitearch}/berkeleydb/_berkeleydb.cpython-*-linux-gnu*so

sed -i /env\ python/d $RPM_BUILD_ROOT%{python3_sitearch}/berkeleydb/dbshelve.py

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license licenses.txt
%doc README.txt

%files -n python3-%{pypi_name}-devel
%{_includedir}/python%{python3_version}/berkeleydb/


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 18.1.4-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 18.1.4-9
- Rebuilt for Python 3.12

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 18.1.4-8
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 18.1.4-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 18.1.4-3
- Review fixes.

* Wed Jan 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 18.1.4-2
- Review fixes.

* Wed Jan 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 18.1.4-1
- Initial package.
