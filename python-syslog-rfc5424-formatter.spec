%global pypi_name syslog-rfc5424-formatter

Name:           python-%{pypi_name}
Version:        1.2.3
Release:        8%{?dist}
Summary:        Logging formatter which produces well-formatted RFC5424 Syslog Protocol messages

License:        ISC
URL:            https://github.com/easypost/syslog-rfc5424-formatter
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This module implements a python logging formatter which produces well-formed
RFC5424-compatible Syslog messages to a given socket.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module implements a python logging formatter which produces well-formed
RFC5424-compatible Syslog messages to a given socket.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%py3_check_import syslog_rfc5424_formatter

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%doc CHANGES.md
%{python3_sitelib}/syslog_rfc5424_formatter
%{python3_sitelib}/syslog_rfc5424_formatter-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.3-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.3-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 10 2022 Laura Barcziova <lbarczio@redhat.com> - 1.2.3-1
- Initial package.
