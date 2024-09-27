%global pypi_name zope.hookable

Name:           python-zope-hookable
Version:        5.1.0
Release:        10%{?dist}
Summary:        Efficient creation of hookable objects

License:        ZPL-2.1
URL:            http://github.com/zopefoundation/zope.hookable
Source0:        %{pypi_source %{pypi_name}}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package supports the efficient creation of “hookable” objects, which
are callable objects that are meant to be optionally replaced.

The idea is that you create a function that does some default thing and
make it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation. All users of the function,
including those that imported it, will see the change.

Documentation is hosted at https://zopehookable.readthedocs.io}
%description %{_description}


%package -n python3-zope-hookable
Summary:        %{summary}


%description -n python3-zope-hookable %{_description}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%if 0%{?rhel} > 8 || 0%{?fedora}
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install


%else


%build
%py3_build


%install
%py3_install
%endif


%check
%pytest --pyargs %{pypi_name}


%files -n python3-zope-hookable
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python3_sitearch}/zope/hookable/
%{python3_sitearch}/%{pypi_name}-%{version}*-info/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}-nspkg.pth
%exclude %{python3_sitearch}/zope/hookable/tests


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.1.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.1.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Jonathan Wright <jonathan@almalinux.org> - 5.1.0-3
- Minor spec improvements

* Wed Aug 10 2022 Jonathan Wright <jonathan@almalinux.org> - 5.1.0-2
- Update spec to build on epel8

* Tue Aug 09 2022 Jonathan Wright <jonathan@almalinux.org> - 5.1.0-1
- Initial package build
- Fixes rhbz#2090769
