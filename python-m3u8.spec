%global srcname m3u8

%bcond_without  tests

Name:           python-%{srcname}
Version:        3.6.0
Release:        5%{?dist}
Summary:        Python module %srcname parser
License:        MIT
Url:            https://github.com/globocom/m3u8
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Python module %srcname parser

%package -n     python3-%{srcname}
Summary:        %{summary}
%py_provides python3-%{srcname}
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-iso8601
BuildRequires:  python3-pytest
BuildRequires:  python3dist(wheel)
Requires:       python3dist(iso8601)

%description -n python3-%{srcname}
Python module %srcname parser


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
# needs BR: python3-devel
%pyproject_buildrequires -r

%build
# Bytecompile Python modules
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with tests}
%check
# 3 deselected tests require internet connection
%pytest -vv -k "not (test_load_should_ and (uri or redirect))"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.6.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Martin Gansser <martinkg@fedoraproject.org> 3.6.0-1
- Update to 3.6.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.5.0-2
- Rebuilt for Python 3.12

* Tue May 30 2023 Martin Gansser <martinkg@fedoraproject.org> 3.5.0-1
- Update to 3.5.0

* Mon May 29 2023 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-4
- Drop superfluous manual dependency on python(abi)

* Wed Mar 29 2023 Martin Gansser <martinkg@fedoraproject.org> 3.4.0-3
- Cleanup specfile

* Sun Mar 05 2023 Martin Gansser <martinkg@fedoraproject.org> 3.4.0-2
- remove version fix in setup.py
- use python3 version naming for info file
- use naming rule for python library

* Fri Mar 03 2023 Martin Gansser <martinkg@fedoraproject.org> 3.4.0-1
- Update to 3.4.0

* Mon Aug 08 2022 Martin Gansser <martinkg@fedoraproject.org> 3.3.0-1
- Update to 3.3.0

* Mon Aug 08 2022 Martin Gansser <martinkg@fedoraproject.org> 3.1.0-2
- Delete superfluous dependencies

* Mon Aug 08 2022 Martin Gansser <martinkg@fedoraproject.org> 3.1.0-1
- initial import by package builder
