# Created by pyp2rpm-3.2.3
%global pypi_name sqlalchemy-collectd

%global with_checks 1

Name:           python-%{pypi_name}
Version:        0.0.8
Release:        2%{?dist}
Summary:        Send database connection pool stats to collectd

License:        MIT
URL:            https://github.com/sqlalchemy/%{pypi_name}
Source0:        https://github.com/sqlalchemy/%{pypi_name}/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
 sqlalchemy-collectd Send statistics on SQLAlchemy <>_ connection and
transaction metrics used by Python applications to the collectd <
service.sqlalchemy-collectd works as a SQLAlchemy plugin invoked via the
database URL, so can be used in any SQLAlchemy application (1.1 or greater)
that accepts arbitrary connection URLs. The plugin is loaded using setuptools
entrypoints and no code changes...

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3-setuptools
Requires:       python3-sqlalchemy >= 1.1
Requires:       collectd-python

BuildRequires:  python3-sqlalchemy >= 1.1
BuildRequires:  python3-devel
%if 0%{?with_checks} > 0
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
%endif

%description -n python3-%{pypi_name}
 sqlalchemy-collectd Send statistics on SQLAlchemy <>_ connection and
transaction metrics used by Python applications to the collectd <
service.sqlalchemy-collectd works as a SQLAlchemy plugin invoked via the
database URL, so can be used in any SQLAlchemy application (1.1 or greater)
that accepts arbitrary connection URLs. The plugin is loaded using setuptools
entrypoints and no code changes...

%prep
%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%if 0%{?with_checks} > 0
%{__python3} -m pytest
%endif

%files -n python3-%{pypi_name}
%doc README.rst LICENSE examples/
%{python3_sitelib}/sqlalchemy_collectd
%{python3_sitelib}/sqlalchemy_collectd-%{version}.dist-info
%{_bindir}/connmon

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Mike Bayer <mbayer@redhat.com> - 0.0.8-1
- upgrade to 0.0.7

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.0.7-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.0.7-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.0.7-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Mike Bayer <mbayer@redhat.com> - 0.0.7-1
- upgrade to 0.0.7

* Mon Jun 14 2021 Stephen Gallagher <sgallagh@redhat.com> - 0.0.4-10
- Build only python3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.4-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Mike Bayer <mbayer@redhat.com> - 0.0.4-1
- upgrade to 0.0.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Matthias Runge <mrunge@redhat.com> - 0.0.3-4
- drop python2 for Fedora > 29
- add collectd-python as dependency

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-2
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Matthias Runge <mrunge@redhat.com> - 0.0.3-1
- Initial package (rhbz#1564206)
